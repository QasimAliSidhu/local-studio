import {chapterList,courseActions} from './curriculum-ui.js';
const $=id=>document.getElementById(id);
const element=(tag,className,text)=>{const node=document.createElement(tag);if(className)node.className=className;if(text!==undefined)node.textContent=text;return node};

export function createPicker({Modal,state,navigate,icons}){
  const modal=new Modal($('picker-modal'));let chosen=1;
  function lessonButton(item,course){
    const button=element('button','picker-lesson'+(state.item?.id===item.id?' current':'')+(state.progress[item.id]?.passed&&!state.progress[item.id]?.stale?' done':''));
    button.dataset.lesson=item.id;const text=element('span');text.append(element('strong','',item.title),element('small','',item.concept||item.chapter_title||course.title));
    const icon=element('i');icon.dataset.lucide=button.classList.contains('done')?'check-circle-2':'chevron-right';button.append(text,icon);button.addEventListener('click',()=>{modal.hide();navigate('exercise/'+item.id)});return button;
  }
  function render(){
    const query=$('picker-search').value.trim().toLowerCase();$('picker-courses').replaceChildren();$('picker-lessons').replaceChildren();$('picker-body').classList.toggle('searching',!!query);
    for(const course of state.courses){const button=element('button',chosen===course.number?'active':'',course.title);button.dataset.course=course.number;button.addEventListener('click',()=>{chosen=course.number;$('picker-body').classList.add('show-lessons');render()});$('picker-courses').append(button)}
    if(query){
      $('picker-lessons').append(element('h3','','Search results'));let count=0;const seen=new Set();
      for(const course of state.courses){
        const courseMatches=course.title.toLowerCase().includes(query);
        for(const id of course.exercises){const item=state.catalog.find(item=>item.id===id);if(item&&!seen.has(id)&&(courseMatches||(item.title.toLowerCase().includes(query)||item.concept?.toLowerCase().includes(query))||item.chapter_title?.toLowerCase().includes(query))){seen.add(id);$('picker-lessons').append(lessonButton(item,course));count++}}
        if(courseMatches&&!course.exercises.length){const button=element('button','picker-lesson',course.title+' \u00b7 course overview');button.addEventListener('click',()=>{modal.hide();navigate('course/'+course.number)});$('picker-lessons').append(button);count++}
      }
      if(!count)$('picker-lessons').append(element('p','','No matching lessons. Try another topic.'));
    }else{
      const course=state.courses.find(course=>course.number===chosen)||state.courses[0];if(!course)return;
      $('picker-lessons').append(element('h3','',course.title),element('p','',course.chapters?`${course.chapters.length} chapters \u00b7 ${course.exercises.length} missions`:course.exercises.length?`${course.exercises.length} interactive lessons. Choose where you want to work.`:'A course brief and notebook are available. Interactive lessons can be added to this course.'));
      courseActions($('picker-lessons'),{course,state,navigate,close:()=>modal.hide(),compact:true});
      const overview=element('button','picker-lesson picker-overview');const text=element('span');text.append(element('strong','','Course overview & notebook'));overview.append(text);overview.dataset.overview=course.number;overview.addEventListener('click',()=>{modal.hide();navigate('course/'+course.number)});$('picker-lessons').append(overview);
      chapterList($('picker-lessons'),{course,state,makeLesson:lessonButton});
    }icons();
  }
  function open(){chosen=state.course?.number||state.courses.find(course=>course.exercises.includes(state.item?.id))?.number||1;$('picker-search').value='';$('picker-body').classList.add('show-lessons');render();modal.show()}
  $('picker-open').addEventListener('click',open);$('sidebar-course').addEventListener('click',()=>{bootstrapCloseSidebar();open()});
  function bootstrapCloseSidebar(){$('sidebar').dispatchEvent(new CustomEvent('studio-close-sidebar'))}
  $('picker-search').addEventListener('input',render);$('picker-back').addEventListener('click',()=>$('picker-body').classList.remove('show-lessons'));
  $('picker-modal').addEventListener('shown.bs.modal',()=>$('picker-search').focus());
  return{open,render};
}

export function createPanels({stored,remember,getView,onStacked,icons}){
  const defaults={column:50,lesson:70,editor:65};let values={...defaults,...stored('panel-sizes',{})};let stacked=null;
  const clamp=(value,min,max)=>Math.max(min,Math.min(max,Number(value)||min));
  function apply(){
    values.column=clamp(values.column,28,65);values.lesson=clamp(values.lesson,35,80);values.editor=clamp(values.editor,35,85);
    for(const [key,variable,handle] of [['column','--column-width','column-resizer'],['lesson','--lesson-height','tutor-resizer'],['editor','--editor-height','console-resizer']]){document.documentElement.style.setProperty(variable,values[key]+'%');$(handle).setAttribute('aria-valuenow',String(Math.round(values[key])))}getView()?.requestMeasure();
  }
  function reset(){values={...defaults};remember('panel-sizes',values);document.body.classList.remove('reading-expanded','console-minimized');setCodingFocus(false);$('console-toggle').setAttribute('aria-expanded','true');apply()}
  for(const [id,key,parent,vertical,min,max] of [['column-resizer','column','workstage',true,28,65],['tutor-resizer','lesson','learning-column',false,35,80],['console-resizer','editor','coding-column',false,35,85]]){
    const handle=$(id);let dragging=false;
    handle.addEventListener('pointerdown',event=>{if(stacked||event.button!==0)return;dragging=true;handle.setPointerCapture(event.pointerId);document.body.classList.add('resizing');event.preventDefault()});
    handle.addEventListener('pointermove',event=>{if(!dragging)return;const rect=$(parent).getBoundingClientRect();values[key]=clamp(100*(vertical?event.clientX-rect.left:event.clientY-rect.top)/(vertical?rect.width:rect.height),min,max);apply()});
    const end=()=>{dragging=false;document.body.classList.remove('resizing');remember('panel-sizes',values)};
    handle.addEventListener('pointerup',end);handle.addEventListener('pointercancel',end);handle.addEventListener('lostpointercapture',end);
    handle.addEventListener('dblclick',()=>{values[key]=defaults[key];apply();remember('panel-sizes',values)});
    handle.addEventListener('keydown',event=>{const negative=vertical?'ArrowLeft':'ArrowUp',positive=vertical?'ArrowRight':'ArrowDown';if(![negative,positive,'Home','End'].includes(event.key))return;values[key]=event.key==='Home'?min:event.key==='End'?max:clamp(values[key]+(event.key===negative?-1:1)*(event.shiftKey?10:2),min,max);apply();remember('panel-sizes',values);event.preventDefault()});
  }
  function expandConsole(){document.body.classList.remove('console-minimized');$('console-toggle').setAttribute('aria-expanded','true');getView()?.requestMeasure()}
  $('console-toggle').addEventListener('click',()=>{const minimized=document.body.classList.toggle('console-minimized');$('console-toggle').setAttribute('aria-expanded',String(!minimized));$('console-toggle').setAttribute('aria-label',minimized?'Expand console':'Minimize console');getView()?.requestMeasure()});
  function setCodingFocus(value){document.body.classList.toggle('coding-focused',value);if(value)document.body.classList.remove('reading-expanded');$('coding-focus').setAttribute('aria-pressed',String(value));$('coding-focus').setAttribute('aria-label',value?'Exit coding focus':'Focus coding area');$('coding-focus').innerHTML=value?'<i data-lucide="minimize-2"></i><span>Exit focus</span>':'<i data-lucide="maximize-2"></i><span>Focus</span>';icons();getView()?.requestMeasure()}
  $('coding-focus').addEventListener('click',()=>{setCodingFocus(!document.body.classList.contains('coding-focused'));getView()?.focus()});
  document.addEventListener('keydown',event=>{if(event.key==='Escape'&&!event.defaultPrevented&&!document.querySelector('.modal.show')&&document.body.classList.contains('coding-focused')){setCodingFocus(false);$('coding-focus').focus();event.preventDefault()}});
  $('lesson-expand').addEventListener('click',()=>{setCodingFocus(false);const expanded=document.body.classList.toggle('reading-expanded');$('lesson-expand').setAttribute('aria-label',expanded?'Restore lesson size':'Expand lesson');getView()?.requestMeasure()});
  $('reset-layout').addEventListener('click',reset);
  const observer=new ResizeObserver(()=>{const next=$('workstage').getBoundingClientRect().width<900;if(next!==stacked){stacked=next;document.body.classList.toggle('stacked',next);onStacked(next)}getView()?.requestMeasure()});observer.observe($('workstage'));apply();
  return{reset,expandConsole,exitCodingFocus(){setCodingFocus(false)},get stacked(){return stacked},showEditor(){document.body.classList.remove('reading-expanded');if(stacked)$('pane-challenge').scrollIntoView({block:'nearest'});getView()?.requestMeasure()}};
}

export function createTutor({Modal,api,markdown,icons,remember,stored,context,onPractice,onOpenPractice}){
  const modal=new Modal($('tutor-modal'));let scope=null,epoch=0,pending=null,timer=null,quote='',selection='',available=true;
  function busy(value){$('tutor-send').disabled=value||!available;$('tutor-question').setAttribute('aria-busy',String(value));for(const button of document.querySelectorAll('[data-tutor-prompt]'))button.disabled=value||!available}
  function render(data){
    const box=$('tutor-messages');box.replaceChildren();
    if(!data.messages.length){const intro=element('div','tutor-empty');const greeting=element('p');greeting.append(element('strong','','Need a hand? '),'Ask about this lesson, get a hint, or work through your code.');intro.append(greeting);box.append(intro)}
    for(const message of data.messages){const bubble=element('div','chat-message '+message.role);bubble.append(element('div','chat-author',message.role==='user'?'You':'Tutor'));const body=element('div','prose');if(message.role==='assistant')body.innerHTML=markdown(message.content);else body.textContent=message.content;bubble.append(body);if(message.role==='assistant'&&!scope.startsWith('course-')){if(message.practice_id){const link=element('a','btn btn-primary open-extra-exercise','Open exercise');link.href=location.pathname+'#practice/'+message.practice_id;link.addEventListener('click',event=>{event.preventDefault();modal.hide();onOpenPractice(message.practice_id)});bubble.append(link)}else{const convert=element('button','btn btn-outline-primary convert-extra-exercise','Make this an exercise');convert.addEventListener('click',()=>generate('Turn this earlier tutor task into a separate runnable exercise. Preserve its requirements and do not include the solution in the instructions:\n'+message.content.slice(0,5000)));bubble.append(convert)}}if(message.status==='failed'&&message.role==='user')bubble.append(element('p','tutor-error',message.error||'This answer did not finish. Try again.'));box.append(bubble)}
    pending=data.active_job?.id||null;
    if(pending)box.append(element('div','chat-pending','Thinking about your question...'));
    busy(!!pending);box.scrollTop=data.messages.length?box.scrollHeight:0;icons();
  }
  async function poll(job,request){
    if(request!==epoch||!scope)return;
    try{const result=await api('/api/tutor/jobs/'+job);if(request!==epoch)return;if(['completed','failed'].includes(result.status)){const history=await api('/api/tutor/'+scope);if(request!==epoch)return;render(history);if(result.status==='failed'){$('tutor-error').textContent=result.error;$('tutor-error').hidden=false}return}}catch(error){if(request!==epoch)return;$('tutor-error').textContent='Connection interrupted. Your question stays saved on the laptop.';$('tutor-error').hidden=false}
    timer=setTimeout(()=>poll(job,request),1500);
  }
  async function changeScope(value){
    scope=value;const request=++epoch;clearTimeout(timer);pending=null;quote='';$('tutor-quote').hidden=true;$('tutor-error').hidden=true;$('tutor-question').value=stored('question:'+scope,'');busy(true);
    try{const data=await api('/api/tutor/'+scope);if(request!==epoch)return;render(data);if(pending)poll(pending,request)}catch(error){if(request!==epoch)return;$('tutor-error').textContent=error.message;$('tutor-error').hidden=false;busy(false)}
  }
  function open(){document.body.classList.remove('reading-expanded');if(document.body.classList.contains('stacked')){if($('tutor-panel').parentElement!==$('tutor-mobile-slot'))$('tutor-mobile-slot').append($('tutor-panel'));modal.show()}else $('tutor-question').focus()}
  async function send(question,mode='question'){
    if(pending||!scope||!question.trim())return;const request=epoch;busy(true);$('tutor-error').hidden=true;
    try{const data=await api('/api/tutor/'+scope,{question,mode,selection:quote,...context()});if(request!==epoch)return;$('tutor-question').value='';remember('question:'+scope,'');quote='';$('tutor-quote').hidden=true;render({...data,active_job:{id:data.job_id}});poll(data.job_id,request)}catch(error){if(request!==epoch)return;$('tutor-error').textContent=error.message;$('tutor-error').hidden=false;busy(false)}
  }
  $('tutor-form').addEventListener('submit',event=>{event.preventDefault();send($('tutor-question').value)});
  $('tutor-question').addEventListener('input',()=>{if(scope)remember('question:'+scope,$('tutor-question').value)});
  $('tutor-question').addEventListener('keydown',event=>{if(event.key==='Enter'&&!event.shiftKey&&!event.isComposing){event.preventDefault();send(event.target.value)}});
  const prompts={explain:'Explain this lesson using a small example and check my understanding.',hint:'Give me one useful hint for this challenge without showing the full solution.',debug:'Help me understand the issue in my current code and console output. Guide me through the next debugging step.',practice:'Give me one new, similar practice mission for this lesson, with a clear task, two examples and an edge case. Save it as its own runnable exercise with an editor and checks. Keep it playful and do not show the solution yet.'};
  async function generate(question=prompts.practice){if(await onPractice()===false)return send('Give me an original practice task for this course, with a clear goal and example. Do not show the solution yet.');return send(question,'practice')}
  for(const button of document.querySelectorAll('[data-tutor-prompt]'))button.addEventListener('click',()=>{const mode=button.dataset.tutorPrompt;if(mode==='practice')generate();else send(prompts[mode],mode)});
  $('tutor-open').addEventListener('click',open);$('tutor-modal').addEventListener('shown.bs.modal',()=>$('tutor-question').focus());
  $('quote-clear').addEventListener('click',()=>{quote='';$('tutor-quote').hidden=true});
  function capture(){const chosen=window.getSelection();if(chosen&&!chosen.isCollapsed&&chosen.anchorNode&&$('lesson-panel').contains(chosen.anchorNode)){selection=chosen.toString().trim().slice(0,4000);$('selection-bar').hidden=!selection}}
  $('lesson-panel').addEventListener('pointerup',capture);$('lesson-panel').addEventListener('keyup',capture);
  document.addEventListener('selectionchange',()=>requestAnimationFrame(capture));
  $('ask-selection').addEventListener('click',()=>{quote=selection;$('tutor-quote-text').textContent=quote.slice(0,160)+(quote.length>160?'...':'');$('tutor-quote').hidden=!quote;$('selection-bar').hidden=true;open()});
  api('/api/tutor/status').then(status=>{available=status.available;document.body.classList.toggle('tutor-unavailable',!available);$('tutor-status').textContent=available?'ChatGPT connected':'Sign-in needed';$('tutor-status').classList.toggle('connected',available);$('tutor-status').title=status.message;busy(!!pending);if(!available){$('tutor-error').textContent=status.message;$('tutor-error').hidden=false}}).catch(()=>{$('tutor-status').textContent='Connection unavailable'});
  return{changeScope,open,generate,layout(stacked){if(stacked){$('tutor-mobile-slot').append($('tutor-panel'))}else{modal.hide();$('tutor-slot').append($('tutor-panel'))}},get scope(){return scope}};
}
