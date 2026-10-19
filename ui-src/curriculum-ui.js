const node=(tag,cls,text)=>{const result=document.createElement(tag);if(cls)result.className=cls;if(text!==undefined)result.textContent=text;return result};
export const passing=(state,id)=>!!(state.progress[id]?.passed&&!state.progress[id]?.stale);
export const courseItems=(state,course)=>course.exercises.map(id=>state.catalog.find(item=>item.id===id)).filter(Boolean);

export function chapterList(host,{course,state,makeLesson,query=''}){
  const chapters=course.chapters;
  if(!chapters?.length){for(const item of courseItems(state,course))if(!query||(item.title.toLowerCase().includes(query)||item.concept?.toLowerCase().includes(query)))host.append(makeLesson(item,course));return}
  const candidate=state.item?.id||state.resume?.last_exercises?.[course.number];
  const active=course.exercises.includes(candidate)?candidate:null;
  const next=course.exercises.find(id=>!passing(state,id));
  for(const chapter of chapters){
    const chapterMatch=chapter.title.toLowerCase().includes(query);
    const items=chapter.lessons.map(id=>state.catalog.find(item=>item.id===id)).filter(item=>item&&(!query||chapterMatch||(item.title.toLowerCase().includes(query)||item.concept?.toLowerCase().includes(query))));
    if(!items.length)continue;
    const group=node('details','curriculum-chapter');group.dataset.chapter=chapter.number;
    group.open=!!query||chapter.lessons.includes(active)||(!active&&chapter.lessons.includes(next));
    const summary=node('summary');const heading=node('span','chapter-heading');heading.append(node('span','chapter-number',String(chapter.number).padStart(2,'0')),node('strong','',chapter.title));
    const count=chapter.lessons.filter(id=>passing(state,id)).length;
    const status=node('small','chapter-count',`${count}/${chapter.lessons.length} passed`);if(count===chapter.lessons.length)group.classList.add('chapter-complete');
    summary.append(heading,status);group.append(summary);
    const body=node('div','chapter-lessons');if(chapter.description)body.append(node('p','chapter-description',chapter.description));
    for(const item of items)body.append(makeLesson(item,course));group.append(body);host.append(group);
  }
}

export function courseActions(host,{course,state,navigate,close=()=>{},compact=false}){
  if(!course.exercises.length)return;
  const passed=course.exercises.filter(id=>passing(state,id)).length;
  const card=node('section','course-launch'+(compact?' compact':''));card.setAttribute('aria-label',course.title+' progress');
  card.append(node('strong','',`${passed} of ${course.exercises.length} missions passed`));
  const progress=node('progress');progress.max=course.exercises.length;progress.value=passed;progress.setAttribute('aria-label','Course completion');card.append(progress);
  const buttons=node('div','course-launch-buttons');
  const button=(label,id,primary)=>{const action=node('button',primary?'btn btn-primary':'btn btn-outline-secondary',label);action.dataset.courseAction=primary?'continue':'start';action.addEventListener('click',()=>{close();navigate('exercise/'+id)});buttons.append(action)};
  const saved=state.resume?.last_exercises?.[course.number];
  const resume=saved&&course.exercises.includes(saved)?saved:null;
  const next=course.exercises.find(id=>!passing(state,id));
  if(resume)button('Resume my lesson',resume,true);
  else if(next)button(passed?'Next unfinished mission':'Start the course',next,true);
  else button('Revisit the first mission',course.exercises[0],true);
  if(!compact&&resume&&next&&next!==resume)button('Next unfinished mission',next,false);
  if(!compact&&((resume&&resume!==course.exercises[0])||(next&&next!==course.exercises[0])))button('Start from the beginning',course.exercises[0],false);
  card.append(buttons);host.append(card);
}
