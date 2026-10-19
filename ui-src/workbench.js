import Offcanvas from 'bootstrap/js/dist/offcanvas';
import Modal from 'bootstrap/js/dist/modal';
import {basicSetup} from 'codemirror';
import {EditorView,keymap} from '@codemirror/view';
import {EditorState,Compartment,Prec} from '@codemirror/state';
import {python} from '@codemirror/lang-python';
import {go} from '@codemirror/lang-go';
import {indentWithTab,indentMore,indentLess,undo,redo} from '@codemirror/commands';
import {oneDark} from '@codemirror/theme-one-dark';
import {HighlightStyle,syntaxHighlighting} from '@codemirror/language';
import {tags} from '@lezer/highlight';
import {marked} from 'marked';
import DOMPurify from 'dompurify';
import {createPicker,createPanels,createTutor} from './study-ui.js';
import {chapterList,courseActions,courseItems} from './curriculum-ui.js';
import {formatLesson} from './lesson-format.js';
import {editorPosition,editorIdentity,challengeResult,pendingResult,resultError} from './challenge-ui.js';
import {MessagesSquare,Maximize2,Lightbulb,X,ArrowUp} from 'lucide';
import {createIcons,PanelLeft,Search,NotebookPen,ChevronDown,ChevronRight,Play,SlidersHorizontal,ArrowRight,ArrowLeft,ListChecks,Save,Undo2,Redo2,IndentIncrease,IndentDecrease,Eye,Terminal,Sun,Moon,RefreshCw,Check,CheckCircle2,LoaderCircle,CircleAlert,Minimize2,Minus} from 'lucide';

const $=id=>document.getElementById(id);
const token=document.querySelector('meta[name=workspace-token]').content;
const base=document.querySelector('meta[name=workspace-base]')?.content||'';
const openingOwnerLink=location.hash.startsWith('#access=');
if(openingOwnerLink)location.replace(base+'/account'+location.hash);
const iconSet={PanelLeft,Search,NotebookPen,ChevronDown,ChevronRight,Play,SlidersHorizontal,ArrowRight,ArrowLeft,ListChecks,Save,Undo2,Redo2,IndentIncrease,IndentDecrease,Eye,Terminal,Sun,Moon,RefreshCw,Check,CheckCircle2,LoaderCircle,CircleAlert,MessagesSquare,Maximize2,Minimize2,Minus,Lightbulb,X,ArrowUp};
const icons=()=>createIcons({icons:iconSet});
const stored=(key,fallback)=>{try{return JSON.parse(localStorage.getItem('studio:'+key))??fallback}catch{return fallback}};
const remember=(key,value)=>{try{localStorage.setItem('studio:'+key,JSON.stringify(value))}catch{}};
const forget=key=>{try{localStorage.removeItem('studio:'+key)}catch{}};
const markdown=text=>DOMPurify.sanitize(marked.parse(text));
function spaceLesson(article){
  // Separate complete sentences without changing lesson text or inline code.
  if(!Intl.Segmenter)return;
  const sentences=new Intl.Segmenter('en',{granularity:'sentence'});
  for(const paragraph of [...article.querySelectorAll(':scope > p, :scope > details > p')]){
    const text=paragraph.textContent;if(text.length<300)continue;
    const nodes=[];const walker=document.createTreeWalker(paragraph,NodeFilter.SHOW_TEXT);let total=0,node;
    while(node=walker.nextNode()){nodes.push({node,start:total,end:total+node.length});total+=node.length}
    const point=offset=>{const part=nodes.find(part=>offset<=part.end)||nodes.at(-1);return {node:part.node,offset:offset-part.start}};
    const boundaries=[0];
    for(const sentence of sentences.segment(text)){
      const end=sentence.index+sentence.segment.length;
      if(end===text.length||end-boundaries.at(-1)<140||text.length-end<45)continue;
      if(point(end).node.parentElement.closest('code,a'))continue;
      boundaries.push(end);
    }
    if(boundaries.length===1)continue;
    boundaries.push(text.length);const fragment=document.createDocumentFragment();
    for(let i=1;i<boundaries.length;i++){const from=point(boundaries[i-1]),to=point(boundaries[i]);const range=document.createRange();range.setStart(from.node,from.offset);range.setEnd(to.node,to.offset);const next=document.createElement('p');next.className=paragraph.className;next.append(range.cloneContents());fragment.append(next)}
    paragraph.replaceWith(fragment);
  }
}
const state={catalog:[],courses:[],progress:{},item:null,course:null,view:null,testView:null,solutionView:null,version:null,savedCode:'',busy:false,pane:'lesson',load:0,editor:'challenge',saveTask:null,saveError:false,conflict:false,playgroundResult:null,runResult:null,action:null};
const settings={theme:stored('theme','dark'),reading:Math.min(28,Math.max(18,stored('reading',20))),code:Math.min(28,Math.max(18,stored('code',20))),wrap:stored('wrap',true),autosave:stored('autosave',true)};
const language=new Compartment(), theme=new Compartment(), wrapping=new Compartment();
const lightSyntax=syntaxHighlighting(HighlightStyle.define([
  {tag:tags.keyword,color:'#8b49ad'},
  {tag:[tags.string,tags.special(tags.string)],color:'#287a58'},
  {tag:[tags.number,tags.bool,tags.null],color:'#a65f20'},
  {tag:tags.function(tags.variableName),color:'#3b67af'},
  {tag:tags.variableName,color:'#333a52'},
  {tag:[tags.typeName,tags.className],color:'#94631d'},
  {tag:tags.comment,color:'#7b879d',fontStyle:'italic'},
  {tag:[tags.operator,tags.punctuation],color:'#63718a'}
]));
const sidebar=new Offcanvas($('sidebar'));
const settingsModal=new Modal($('settings-modal'));
const coursesModal=new Modal($('courses-modal'));
const practiceModal=new Modal($('practice-modal'));
let practiceShowAll=false;
function currentGrade(){return state.item?.practice?state.item.progress:state.progress[state.item?.id]}
function itemApi(id=state.item?.id){return '/api/'+(state.item?.practice?'practices':'exercises')+'/'+id}
let notebook=null;
let autoTimer=null;
const picker=createPicker({Modal,state,navigate,icons});
const tutor=createTutor({Modal,api,markdown,icons,remember,stored,context:()=>({code:state.view?.state.doc.toString()||'',editor:state.item?state.editor:'none',console:(state.editor==='playground'?state.playgroundResult:(state.runResult||currentGrade()))?.output||''}),onPractice:()=>!!state.item,onOpenPractice:id=>navigate('practice/'+id)});
const panels=createPanels({stored,remember,getView:()=>state.view,onStacked:stacked=>tutor.layout(stacked),icons});

async function api(path,data){
  const response=await fetch(base+path,data===undefined?{}:{method:'POST',headers:{'Content-Type':'application/json','X-Workspace-Token':token},body:JSON.stringify(data)});
  const result=await response.json();
  if(response.status===401){location.assign(base+'/#next='+encodeURIComponent(location.hash.slice(1)));throw new Error('Sign in to open your workspace.')}
  if(!response.ok)throw new Error(result.error||'The request could not be completed.');
  return result;
}
function notice(text='',error=false){$('notice').textContent=text;$('notice').hidden=!text;$('notice').classList.toggle('error',error)}
function applySettings(){
  document.documentElement.dataset.bsTheme=settings.theme;
  document.documentElement.style.setProperty('--prose-size',settings.reading+'px');
  document.documentElement.style.setProperty('--code-size',settings.code+'px');
  $('reading-size').value=settings.reading;$('code-size').value=settings.code;
  $('reading-size-label').textContent=settings.reading+'px';$('code-size-label').textContent=settings.code+'px';
  $('wrap-code').checked=settings.wrap;
  $('autosave').checked=settings.autosave;
  for(const mode of ['light','dark']){$('theme-'+mode).classList.toggle('selected',settings.theme===mode);$('theme-'+mode).setAttribute('aria-pressed',String(settings.theme===mode))}
  if(state.view)state.view.dispatch({effects:[theme.reconfigure(settings.theme==='dark'?oneDark:lightSyntax),wrapping.reconfigure(settings.wrap?EditorView.lineWrapping:[])]});
  for(const view of [state.testView,state.solutionView])if(view){view.destroy()}
  state.testView=null;state.solutionView=null;
  if(state.item){renderTestsSource();if(!$('solution-content').hidden&&state.solutionCode)renderSolution(state.solutionCode)}
  state.view?.requestMeasure();
}
function setTheme(mode){settings.theme=mode;remember('theme',mode);applySettings()}
function dirty(){return !!state.view&&state.view.state.doc.toString()!==state.savedCode}
function updateSave(){
  const changed=dirty();$('save-state').textContent=state.saveTask?'Saving...':changed?(state.saveError||state.conflict?'Device draft':settings.autosave?'Saving soon':'Device draft'):'Saved on LocalMachine';$('save').disabled=state.busy||!!state.saveTask||!changed;
  $('save-state').dataset.state=state.saveError||state.conflict?'error':state.saveTask?'saving':changed?'draft':'saved';
  $('save-state').title=changed?'Your device draft is safe. Saved files are shared across your devices.':'Your code is saved on LocalMachine and available from your other devices.';
}
function draftKey(){return 'draft:'+(state.editor==='playground'?'playground:':'')+state.item.id+(state.editor!=='playground'&&state.item.content_revision?':v'+state.item.content_revision:'')}
function keepDraft(schedule=false){if(state.item&&state.view){const code=state.view.state.doc.toString();if(code!==state.savedCode)remember(draftKey(),{code,version:state.version});else forget(draftKey());if(schedule){state.saveError=false;queueAutoSave()}updateSave()}}
function queueAutoSave(){clearTimeout(autoTimer);if(settings.autosave&&dirty()&&!state.busy&&!state.conflict&&!state.saveError)autoTimer=setTimeout(()=>save(true),1400)}
function makeReadonly(host,code,lang){
  $(host).replaceChildren();
  return new EditorView({parent:$(host),state:EditorState.create({doc:code,extensions:[basicSetup,EditorState.readOnly.of(true),EditorView.editable.of(false),EditorView.cspNonce.of(token),lang==='python'?python():go(),settings.theme==='dark'?oneDark:lightSyntax,EditorView.lineWrapping,EditorView.contentAttributes.of({'aria-label':host==='tests-editor'?'Test source code':'Reference solution'})]})});
}
function renderTestsSource(){if(!state.item)return;state.testView=makeReadonly('tests-editor',state.item.tests,state.item.language)}
function renderSolution(code){state.solutionView?.destroy();state.solutionView=makeReadonly('solution-editor',code,state.item.language)}
function pane(name,focus=false){
  if(state.course&&name!=='lesson')return;
  if(name==='challenge'){panels.showEditor();requestAnimationFrame(()=>{state.view?.requestMeasure();if(focus)state.view?.focus()});return}
  if(name==='console'){panels.expandConsole();if(panels.stacked)$('pane-console').scrollIntoView({block:'nearest'});return}
  if(!['lesson','tests','solution'].includes(name))name='lesson';
  state.pane=name;remember('pane',name);
  document.querySelectorAll('[data-pane]').forEach(button=>{const active=button.dataset.pane===name;button.setAttribute('aria-selected',String(active));button.tabIndex=active?0:-1;$('pane-'+button.dataset.pane).hidden=!active});
  if(name==='challenge')requestAnimationFrame(()=>{state.view?.requestMeasure();if(focus)state.view?.focus()});
  if(name==='tests')state.testView?.requestMeasure();if(name==='solution')state.solutionView?.requestMeasure();
}
function setBusy(value){
  state.busy=value;$('run').disabled=value||!!state.course;$('submit').disabled=value||!!state.course||state.editor==='playground';$('submit').hidden=state.editor==='playground';$('console-next').disabled=value||!nextItem();$('save').disabled=value||!dirty();$('picker-open').disabled=value;$('lesson-select').disabled=value;$('course-filter').disabled=value;$('mode-challenge').disabled=value;$('mode-playground').disabled=value;
  $('run').innerHTML=value&&state.action==='run'?'<i data-lucide="loader-circle"></i><span>Running</span>':'<i data-lucide="play"></i><span>Run</span>';
  $('submit').innerHTML=value&&state.action==='submit'?'<i data-lucide="loader-circle"></i> Submitting':'<i data-lucide="check-circle-2"></i> Submit answer';
  if(state.view)state.view.contentDOM.setAttribute('aria-busy',String(value));icons();
}
function readTests(text,lang){
  const matches=lang==='python'?[...text.matchAll(/def test_([a-zA-Z0-9_]+)\(/g)].map(m=>m[1].replaceAll('_',' ')):[...text.matchAll(/func Test([a-zA-Z0-9_]+)\(/g)].map(m=>m[1].replace(/([a-z])([A-Z])/g,'$1 $2'));
  return matches.length?matches:['Run all checks in the test file'];
}
function renderConsole(result){
  if(result?.prior_curriculum)result=null;
  const debug=result?.graded===false;
  $('console-next').innerHTML=state.item?.practice?'Back to lesson <i data-lucide="arrow-left"></i>':'Next lesson <i data-lucide="arrow-right"></i>';$('console-next').disabled=state.busy||!nextItem();$('console-next').hidden=!!state.course;
  $('console-next').className='btn '+(result?.passed&&!result.stale&&!debug&&!result.playground?'btn-primary':'btn-outline-primary');
  challengeResult({result,mode:state.editor,item:state.item});icons();
}
function nextItem(){if(state.item?.practice)return state.catalog.find(item=>item.id===state.item.parent_id);const course=state.courses.find(course=>course.exercises.includes(state.item?.id));if(!course)return;const index=course.exercises.indexOf(state.item.id);return state.catalog.find(item=>item.id===course.exercises[index+1])}
async function navigate(route){if(state.busy){notice('Wait for this check to finish before switching lessons.');return}keepDraft();clearTimeout(autoTimer);if(dirty()&&!state.conflict)await save(true);remember('pane','lesson');if(location.hash==='#'+route)loadRoute();else location.hash=route;closeSidebar()}
function goNext(){const next=nextItem();if(next)navigate('exercise/'+next.id)}
function closeSidebar(){if(!document.body.classList.contains('sidebar-pinned'))sidebar.hide()}
function setPinned(value){
  if(value&&innerWidth<1000)value=false;
  document.body.classList.toggle('sidebar-pinned',value);$('sidebar-toggle').setAttribute('aria-expanded',String(value));$('pin-sidebar').setAttribute('aria-label',value?'Unpin sidebar':'Keep sidebar open');remember('pinned',value);state.view?.requestMeasure();
}
function lessonButton(item){
  const button=document.createElement('button');button.className='lesson-link'+(state.item?.id===item.id?' active':'')+(state.progress[item.id]?.passed&&!state.progress[item.id]?.stale?' done':'');button.dataset.id=item.id;
  const dot=document.createElement('span');dot.className='lesson-dot';dot.setAttribute('aria-hidden','true');const name=document.createElement('span');name.textContent=item.title;if(item.concept){const concept=document.createElement('small');concept.className='lesson-link-concept';concept.textContent=item.concept;name.append(concept)}button.append(dot,name);button.addEventListener('click',()=>navigate('exercise/'+item.id));return button;
}
function renderNavigation(){
  const query=$('lesson-search').value.trim().toLowerCase(), filter=$('course-filter').value;
  $('lesson-list').replaceChildren();
  const courses=state.courses.filter(course=>!filter||String(course.number)===filter);
  for(const course of courses){
    const items=courseItems(state,course).filter(item=>!query||item.title.toLowerCase().includes(query)||item.chapter_title?.toLowerCase().includes(query)||item.concept?.toLowerCase().includes(query));
    if(query&&!items.length&&!course.title.toLowerCase().includes(query))continue;
    if(!filter){const title=document.createElement('div');title.className='nav-group-title';title.textContent=course.title;$('lesson-list').append(title)}
    const overview=document.createElement('button');overview.className='lesson-link'+(state.course?.number===course.number?' active':'');overview.textContent=items.length?'Course overview':course.title;overview.addEventListener('click',()=>navigate('course/'+course.number));$('lesson-list').append(overview);
    chapterList($('lesson-list'),{course,state,makeLesson:lessonButton,query});
  }
  const complete=Object.values(state.progress).filter(p=>p.passed&&!p.stale).length;$('completion-summary').textContent=`${complete} of ${state.catalog.length} challenges passing`;
}
function fillSelectors(){
  $('lesson-select').replaceChildren();$('course-filter').replaceChildren(new Option('All courses',''));$('course-select').replaceChildren();
  for(const course of state.courses){
    const group=document.createElement('optgroup');group.label=course.title;
    group.append(new Option(course.title+' \u00b7 overview','course/'+course.number));
    for(const ident of course.exercises){const item=state.catalog.find(item=>item.id===ident);if(item)group.append(new Option(item.title+(item.concept?' ('+item.concept+')':''),'exercise/'+ident))}
    $('lesson-select').append(group);$('course-filter').append(new Option(course.title,String(course.number)));$('course-select').append(new Option(course.title,String(course.number)));
  }
}
function loadEditor(data,mode='challenge'){
  clearTimeout(autoTimer);state.view?.destroy();$('code-editor').replaceChildren();state.editor=mode;state.version=data.version;state.savedCode=data.code;state.saveError=false;state.conflict=false;
  const draft=stored(draftKey(),null),code=draft?.code??data.code;
  if(draft&&draft.version!==data.version&&draft.code!==data.code){state.version=draft.version;state.conflict=true;notice('Your device draft is restored, but the LocalMachine file changed. Compare your work before using Reload file from disk.',true)}
  else if(draft?.code===data.code)forget(draftKey());
  $('editor-filename').textContent=data.filename;
  editorIdentity({language:data.language,mode,executionMode:state.item.execution_mode,practice:state.item.practice});
  for(const value of ['challenge','playground']){$('mode-'+value).classList.toggle('active',value===mode);$('mode-'+value).setAttribute('aria-pressed',String(value===mode))}
  state.view=new EditorView({parent:$('code-editor'),state:EditorState.create({doc:code,extensions:[basicSetup,EditorView.cspNonce.of(token),language.of(data.language==='python'?python():go()),theme.of(settings.theme==='dark'?oneDark:lightSyntax),wrapping.of(settings.wrap?EditorView.lineWrapping:[]),Prec.highest(keymap.of([{key:'Mod-Enter',run:()=>{run();return true}},{key:'Mod-Shift-Enter',run:()=>{submit();return true}},{key:'Mod-s',run:()=>{save();return true}},indentWithTab])),EditorView.contentAttributes.of({'aria-label':mode==='playground'?'Extra practice code':'Your challenge code','spellcheck':'false','autocapitalize':'off','autocorrect':'off'}),EditorView.updateListener.of(update=>{if(update.selectionSet||update.docChanged)editorPosition(update.view);if(update.docChanged){keepDraft(true);const result=mode==='playground'?state.playgroundResult:(state.runResult||currentGrade());if(result)result.stale=true;if(mode!=='playground'&&currentGrade())currentGrade().stale=true;if(!state.busy)renderConsole(result)}})]})});
  editorPosition(state.view);
  renderConsole(mode==='playground'?state.playgroundResult:(state.runResult||currentGrade()));setBusy(false);updateSave();queueAutoSave();
}
async function switchEditor(mode){
  if(!state.item||state.item.practice||state.busy||state.editor===mode)return;keepDraft();clearTimeout(autoTimer);if(dirty()&&!state.conflict)await save(true);
  const id=state.item.id;
  try{const data=await api((mode==='playground'?'/api/playgrounds/':'/api/exercises/')+id);if(state.item?.id!==id)return;loadEditor(data,mode);remember('editor:'+id,mode);panels.showEditor()}catch(error){notice(error.message,true)}
}
async function loadRoute(){
  if(location.hash.startsWith('#access=')){keepDraft();clearTimeout(autoTimer);location.replace(base+'/account'+location.hash);return}
  const request=++state.load;clearTimeout(autoTimer);if(state.saveTask)await state.saveTask;if(request!==state.load)return;notice();
  let route=location.hash.slice(1);if(!/^(exercise\/[a-z]+\d+|practice\/[a-f0-9]{32}|course\/\d+)$/.test(route))route=state.resume?.route||stored('route','course/1');
  if(route.startsWith('course/')&&!state.courses.some(course=>String(course.number)===route.slice(7))){route='course/'+state.courses[0].number;history.replaceState(null,'','#'+route)}
  const [type,ident]=route.split('/');
  try{
    if(type==='course'){const fresh=await api('/api/bootstrap');if(request!==state.load)return;Object.assign(state,{progress:fresh.progress,resume:fresh.resume})}
    const data=await api(type==='course'?'/api/courses/'+ident:type==='practice'?'/api/practices/'+ident:'/api/exercises/'+ident);if(request!==state.load)return;
    state.view?.destroy();state.testView?.destroy();state.solutionView?.destroy();state.view=null;state.testView=null;state.solutionView=null;state.solutionCode=null;state.playgroundResult=null;state.runResult=null;
    $('code-editor').replaceChildren();$('tests-editor').replaceChildren();$('solution-editor').replaceChildren();$('course-lesson-links').replaceChildren();$('course-launch-top').replaceChildren();
    state.course=type==='course'?data:null;state.item=type!=='course'?data:null;if(state.course)panels.exitCodingFocus();remember('route',route);$('lesson-select').value=route;document.title=data.title+' | Local Studio';document.body.classList.toggle('course-overview',!!state.course);
    const course=state.course||state.courses.find(course=>course.exercises.includes(data.parent_id||data.id));$('course-filter').value=String(course?.number||'');$('current-course').textContent=course?.title||'Local Studio';$('current-lesson').textContent=state.course?'Course overview':data.title;$('sidebar-course-name').textContent=course?.title||'All courses';
    $('mode-challenge').textContent=data.practice?'Extra exercise':data.execution_mode==='script'?'Your program':'Challenge';$('mode-playground').hidden=!!data.practice;
    if(state.item&&!data.practice&&course){state.resume??={};state.resume.last_exercises??={};state.resume.last_exercises[course.number]=data.id;if(data.chapter)$('current-course').textContent=`Python \u00b7 Mission ${data.course_position}/${course.exercises.length} \u00b7 ${data.chapter_title}`}
    if(data.practice)$('current-course').textContent='Extra exercise \u00b7 '+data.parent_title;
    $('current-course').title=$('current-course').textContent;
    for(const tab of document.querySelectorAll('[data-pane]'))tab.disabled=!!state.course&&tab.dataset.pane!=='lesson';
    $('start-challenge').hidden=!!state.course;$('console-next').hidden=!!state.course;$('console-next').disabled=!nextItem();$('submit').disabled=!!state.course;$('reload-file').disabled=!!state.course;$('run').disabled=!!state.course;$('assignment-card').hidden=!!state.course;$('lesson-guide').hidden=!!state.course;
    if(state.course){
      $('lesson-intro').innerHTML=markdown(data.chapters?`# ${data.title}\n\n${data.description}\n\n${data.story}\n\n**Choose a chapter below.** Start from the beginning, resume your lesson, or ask the tutor about a concept.`:data.instructions);$('lesson-content').replaceChildren();
      courseActions($('course-launch-top'),{course:data,state,navigate});
      chapterList($('course-lesson-links'),{course:data,state,makeLesson:lessonButton});
      if(!data.exercises.length){const note=document.createElement('p');note.className='learning-note';note.textContent='This course currently has a practice brief and notebook. Interactive challenges can be added here as you build out the course.';$('course-lesson-links').append(note)}
      const notes=document.createElement('button');notes.className='btn btn-outline-primary';notes.textContent='Open course notebook';notes.addEventListener('click',()=>openNotebook(data.number));$('course-lesson-links').append(notes);pane('lesson');
    }else{
      if(data.practice&&data.progress)data.progress.stale=data.progress.code_hash!==data.version;
      if(!data.practice&&state.progress[data.id]){const result=state.progress[data.id];result.stale=result.code_hash!==data.version;result.prior_curriculum=!!(data.content_revision&&result.content_revision!==data.content_revision&&result.stale)}
      if(data.lesson_layout==='teach-first'){const sections=data.lesson.split(/\n(?=## Before you run|## Think it through)/);$('lesson-intro').innerHTML=markdown(sections[0]);$('lesson-content').innerHTML=markdown(sections.slice(1).join('\n'))}
      else{const sections=data.lesson.split(/\n\n/);$('lesson-intro').innerHTML=markdown(sections.slice(0,2).join('\n\n'));$('lesson-content').innerHTML=markdown(sections.slice(2).join('\n\n'))}
      spaceLesson($('lesson-intro'));spaceLesson($('lesson-content'));
      if(data.concept){const concept=document.createElement('p');concept.className='lesson-concept';concept.textContent=(data.language==='python'?'Python':'Go')+' \u00b7 '+data.concept;const heading=$('lesson-intro').querySelector('h1');if(heading)heading.after(concept)}
      document.querySelector('#pane-tests .section-intro').textContent=data.execution_mode==='script'?'These checks compare your program with the requested output and values. You do not need to write or understand the test framework to solve this mission.':'Run checks while debugging. Submit answer grades your work and saves completion.';
      $('task-content').innerHTML=markdown(data.instructions.replace(/^# .*\n/m,'').replace(/^## Your (?:task|mission)\s*$/m,''));$('hint-text').hidden=true;$('hint-text').textContent=data.hint;$('hint').textContent='Show a hint';$('solution-content').hidden=true;$('reveal-solution').hidden=false;
      state.exampleTarget=formatLesson({intro:$('lesson-intro'),after:$('lesson-content'),task:$('task-content'),language:data.language});$('read-example').hidden=!state.exampleTarget;$('lesson-guide').classList.toggle('no-example',!state.exampleTarget);
      $('test-list').replaceChildren();for(const test of readTests(data.tests,data.language)){const li=document.createElement('li');const icon=document.createElement('i');icon.dataset.lucide='check';const name=document.createElement('span');name.textContent=test.charAt(0).toUpperCase()+test.slice(1);li.append(icon,name);$('test-list').append(li)}
      const mode=data.practice?'challenge':stored('editor:'+data.id,'challenge');const editorData=mode==='playground'?await api('/api/playgrounds/'+data.id):data;if(request!==state.load)return;loadEditor(editorData,mode);renderTestsSource();pane(stored('pane','lesson'));
    }
    renderNavigation();icons();for(const el of document.querySelectorAll('.material-pane'))el.scrollTop=0;
    tutor.changeScope(state.course?'course-'+state.course.number:data.practice?'practice-'+data.id:data.id);api('/api/session',{route}).catch(()=>{});
  }catch(error){notice(error.message,true)}
}
async function save(automatic=false){
  if(state.saveTask)return state.saveTask;if(state.busy||!state.item||!state.view||!dirty())return true;
  clearTimeout(autoTimer);const code=state.view.state.doc.toString(),id=state.item.id,mode=state.editor,version=state.version;
  state.saveTask=(async()=>{try{const result=await api((mode==='playground'?'/api/playgrounds/'+id:itemApi(id))+'/save',{code,version});state.version=result.version;state.savedCode=code;state.saveError=false;keepDraft();if(!automatic)notice('Saved on LocalMachine.');return true}catch(error){state.saveError=true;state.conflict=error.message.includes('changed outside');notice(error.message,true);return false}finally{state.saveTask=null;updateSave();if(dirty()&&!state.saveError)queueAutoSave()}})();updateSave();return state.saveTask;
}
function run(){return execute('run')}
function submit(){if(state.editor!=='playground')return execute('submit')}
async function execute(action){
  if(state.busy||!state.item)return;if(state.saveTask)await state.saveTask;if(state.busy)return;clearTimeout(autoTimer);notice();state.action=action;setBusy(true);pane('console');
  pendingResult(action);icons();
  const id=state.item.id,code=state.view.state.doc.toString(),mode=state.editor;
  try{const response=await api((mode==='playground'?'/api/playgrounds/'+id:itemApi(id))+'/'+action,{code,version:state.version});state.version=response.version;state.savedCode=code;response.result.stale=state.view.state.doc.toString()!==code;if(mode==='playground')state.playgroundResult=response.result;else if(action==='submit'){if(state.item.practice)state.item.progress=response.result;else state.progress[id]=response.result;state.runResult=null}else{state.runResult=response.result;if(currentGrade())currentGrade().stale=currentGrade().code_hash!==response.version}keepDraft();renderConsole(response.result);renderNavigation()}
  catch(error){notice(error.message,true);resultError(action);icons()}
  finally{state.action=null;setBusy(false);updateSave();queueAutoSave()}
}
async function reveal(){
  const id=state.item?.id;if(!id)return;
  try{const result=await api(itemApi(id)+'/solution');if(state.item?.id!==id)return;state.solutionCode=result.code;$('solution-content').hidden=false;$('reveal-solution').hidden=true;renderSolution(result.code)}catch(error){notice(error.message,true)}
}
async function loadNotebook(number){
  if(notebook){if($('course-notes').value!==notebook.notes)remember('notes:'+notebook.number,{notes:$('course-notes').value,version:notebook.version});else forget('notes:'+notebook.number)}
  const request=Number(number);$('save-notes').disabled=true;$('notes-status').textContent='Opening notebook...';
  try{const data=await api('/api/courses/'+request);if(Number($('course-select').value)!==request)return;notebook=data;$('course-content').innerHTML=markdown(data.instructions);const draft=stored('notes:'+request,null);$('course-notes').value=draft?.notes??data.notes;if(draft&&draft.notes!==data.notes)notebook.version=draft.version;$('notes-status').textContent=draft?'Device draft restored.':'Saved';$('save-notes').disabled=false}catch(error){$('notes-status').textContent=error.message}
}
function openNotebook(number){closeSidebar();$('course-select').value=String(number||state.course?.number||state.courses.find(course=>course.exercises.includes(state.item?.id))?.number||1);coursesModal.show();loadNotebook($('course-select').value)}

$('sidebar-toggle').addEventListener('click',()=>{if(document.body.classList.contains('sidebar-pinned'))setPinned(false);else sidebar.toggle()});
$('sidebar').addEventListener('shown.bs.offcanvas',()=>$('sidebar-toggle').setAttribute('aria-expanded','true'));
$('sidebar').addEventListener('hidden.bs.offcanvas',()=>$('sidebar-toggle').setAttribute('aria-expanded',String(document.body.classList.contains('sidebar-pinned'))));
$('sidebar').addEventListener('studio-close-sidebar',()=>sidebar.hide());
$('pin-sidebar').addEventListener('click',()=>{if(document.body.classList.contains('sidebar-pinned')){setPinned(false);return}const el=$('sidebar');el.addEventListener('hidden.bs.offcanvas',()=>setPinned(true),{once:true});sidebar.hide()});
matchMedia('(min-width:1000px)').addEventListener('change',event=>{if(!event.matches)setPinned(false)});
$('lesson-select').addEventListener('change',event=>navigate(event.target.value));
$('course-filter').addEventListener('change',event=>{renderNavigation();if(event.target.value)navigate('course/'+event.target.value)});
$('lesson-search').addEventListener('input',renderNavigation);
document.querySelectorAll('[data-pane]').forEach(button=>button.addEventListener('click',()=>pane(button.dataset.pane)));
document.querySelector('.material-tabs').addEventListener('keydown',event=>{if(!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return;const tabs=[...document.querySelectorAll('[data-pane]')].filter(tab=>!tab.disabled);const current=tabs.indexOf(document.activeElement);let index=event.key==='Home'?0:event.key==='End'?tabs.length-1:(current+(event.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;tabs[index].focus();pane(tabs[index].dataset.pane);event.preventDefault()});
$('run').addEventListener('click',run);$('submit').addEventListener('click',submit);$('save').addEventListener('click',()=>save(false));
$('mode-challenge').addEventListener('click',()=>switchEditor('challenge'));$('mode-playground').addEventListener('click',()=>switchEditor('playground'));
$('jump-task').addEventListener('click',()=>readSection($('assignment-card')));
function readSection(target){panels.exitCodingFocus();pane('lesson');if(panels.stacked)document.body.classList.add('reading-expanded');target?.scrollIntoView({block:'start',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})}
$('read-learn').addEventListener('click',()=>readSection($('lesson-intro')));
$('read-example').addEventListener('click',()=>readSection(state.exampleTarget));
$('read-task').addEventListener('click',()=>readSection($('assignment-card')));
$('start-challenge').addEventListener('click',()=>pane('challenge',true));
for(const id of ['tests-to-code','console-to-code'])$(id).addEventListener('click',()=>pane('challenge',true));
$('console-next').addEventListener('click',goNext);
$('hint').addEventListener('click',()=>{$('hint-text').hidden=!$('hint-text').hidden;$('hint').textContent=$('hint-text').hidden?'Show a hint':'Hide hint'});
$('reveal-solution').addEventListener('click',reveal);
for(const [id,command] of [['undo',undo],['redo',redo],['indent',indentMore],['outdent',indentLess]])$(id).addEventListener('click',()=>{if(state.view){command(state.view);state.view.focus()}});
$('settings-open').addEventListener('click',()=>settingsModal.show());
for(const mode of ['light','dark'])$('theme-'+mode).addEventListener('click',()=>setTheme(mode));
for(const [id,key] of [['reading-size','reading'],['code-size','code']])$(id).addEventListener('input',event=>{settings[key]=Number(event.target.value);remember(key,settings[key]);applySettings()});
$('wrap-code').addEventListener('change',event=>{settings.wrap=event.target.checked;remember('wrap',settings.wrap);applySettings()});
$('autosave').addEventListener('change',event=>{settings.autosave=event.target.checked;remember('autosave',settings.autosave);if(settings.autosave)queueAutoSave();else clearTimeout(autoTimer);updateSave()});
$('reload-file').addEventListener('click',()=>{if(dirty()&&!confirm('Replace this device draft with the file currently saved on LocalMachine?'))return;clearTimeout(autoTimer);forget(draftKey());settingsModal.hide();loadRoute()});
$('courses-open').addEventListener('click',()=>openNotebook());
$('course-select').addEventListener('change',event=>loadNotebook(event.target.value));
$('course-notes').addEventListener('input',()=>{if(notebook){remember('notes:'+notebook.number,{notes:$('course-notes').value,version:notebook.version});$('notes-status').textContent='Draft on device'}});
$('save-notes').addEventListener('click',async()=>{if(!notebook)return;$('save-notes').disabled=true;try{const notes=$('course-notes').value;const result=await api('/api/courses/'+notebook.number+'/notes',{notes,version:notebook.version});notebook.version=result.version;notebook.notes=notes;forget('notes:'+notebook.number);$('notes-status').textContent='Saved on LocalMachine.'}catch(error){$('notes-status').textContent=error.message}finally{$('save-notes').disabled=false}});
window.addEventListener('hashchange',loadRoute);
window.addEventListener('pagehide',()=>keepDraft());
document.addEventListener('keydown',event=>{if(event.defaultPrevented||event.target.closest('#tutor-panel')||document.querySelector('.modal.show'))return;if((event.ctrlKey||event.metaKey)&&event.key==='Enter'){event.preventDefault();event.shiftKey?submit():run()}else if((event.ctrlKey||event.metaKey)&&event.key==='s'){event.preventDefault();save()}});

async function openPracticeLibrary(all=false){
  practiceShowAll=all;practiceModal.show();$('practice-list').textContent='Opening saved exercises...';$('practice-create').disabled=!state.item;
  try{const parent=state.item?.parent_id||state.item?.id;const data=await api('/api/practices'+(!all&&parent?'?lesson='+encodeURIComponent(parent):''));$('practice-list').replaceChildren();
    if(!data.exercises.length){const empty=document.createElement('p');empty.className='learning-note';empty.textContent='No saved exercises here yet. Create a similar exercise, or use Make this an exercise on an earlier tutor task.';$('practice-list').append(empty)}
    for(const exercise of data.exercises){const link=document.createElement('a');link.className='practice-card';link.href=location.pathname+'#practice/'+exercise.id;const title=document.createElement('strong');title.textContent=exercise.title;const concept=document.createElement('span');concept.textContent=exercise.concept;const status=document.createElement('small');status.textContent=(exercise.passed?'Completed':'Ready to work')+' \u00b7 '+exercise.parent_title;link.append(title,concept,status);link.addEventListener('click',event=>{event.preventDefault();practiceModal.hide();navigate('practice/'+exercise.id)});$('practice-list').append(link)}
  }catch(error){$('practice-list').textContent=error.message}
}
$('practice-open').addEventListener('click',()=>openPracticeLibrary());
$('practice-all').addEventListener('click',()=>openPracticeLibrary(true));
$('practice-create').addEventListener('click',()=>{practiceModal.hide();tutor.open();tutor.generate()});
$('account-open').addEventListener('click',()=>{keepDraft();location.assign(base+'/account')});
$('sign-out').addEventListener('click',async()=>{try{keepDraft();clearTimeout(autoTimer);if(dirty()&&!await save(false))return;const response=await fetch(base+'/auth/logout',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'});if(!response.ok)throw Error('Could not sign out. Try again.');location.replace(base+'/')}catch(error){notice(error.message,true)}});
$('connect-device').addEventListener('click',async()=>{try{const data=await api('/api/access-link',{});$('device-url').value=data.url+'&next='+encodeURIComponent(location.hash.slice(1));$('device-link').hidden=false;$('device-url').focus();$('device-url').select()}catch(error){notice(error.message,true)}});

applySettings();icons();
(async()=>{if(openingOwnerLink)return;try{const boot=await api('/api/bootstrap');Object.assign(state,{catalog:boot.catalog,courses:boot.courses,progress:boot.progress,resume:boot.resume});$('connect-device').hidden=true;$('account-open').hidden=!boot.public_access?.password_login;$('sign-out').hidden=!boot.public_access?.password_login;$('access-description').textContent=boot.public_access?.enabled?'Your personal login protects this workspace. Sign in with your username and password on another device. Saved work stays on LocalMachine.':'Remote access currently uses your private Tailscale account. Public mobile access is not enabled.';fillSelectors();setPinned(stored('pinned',false));await loadRoute()}catch(error){notice('Could not open the workspace. '+error.message,true)}})();
