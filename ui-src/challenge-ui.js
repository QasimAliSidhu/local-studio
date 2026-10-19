// Presentation only. Run, grading, saving and learner files stay in workbench.js.
const $=id=>document.getElementById(id);
const el=(tag,cls,text)=>{const node=document.createElement(tag);if(cls)node.className=cls;if(text!==undefined)node.textContent=text;return node};
const icon=name=>{const node=el('i');node.dataset.lucide=name;node.setAttribute('aria-hidden','true');return node};

export function editorPosition(view){
  if(!view)return;
  const head=view.state.selection.main.head,line=view.state.doc.lineAt(head);
  $('cursor-position').textContent=`Ln ${line.number}, Col ${head-line.from+1}`;
}

export function editorIdentity({language,mode,executionMode,practice}){
  const name=language==='python'?'Python':'Go';
  $('editor-file-icon').textContent=language==='python'?'PY':'GO';
  $('editor-file-icon').dataset.language=language;
  $('editor-language').textContent=name;
  $('editor-kind').textContent=mode==='playground'?'Scratchpad':practice?'Extra exercise':executionMode==='script'?'Program':'Function challenge';
}

function testRows(text,language){
  const rows=[];
  const pattern=language==='go'?/^\s*--- (PASS|FAIL|SKIP): (\S+) \(/gm:/^(test_\S+) \([^\n]+\) \.\.\. (ok|FAIL|ERROR|skipped[^\n]*|expected failure|unexpected success)\s*$/gm;
  for(const match of text.matchAll(pattern)){
    const raw=language==='go'?match[1]:match[2],name=language==='go'?match[2]:match[1];
    const state=/^(ok|PASS|expected failure)$/.test(raw)?'passed':/^(skipped|SKIP)/.test(raw)?'skipped':'failed';
    const label=name.replace(/^test_|^Test/,'').replaceAll('_',' ').replace(/([a-z])([A-Z])/g,'$1 $2');
    rows.push({state,name:label.charAt(0).toUpperCase()+label.slice(1)});
  }
  return rows;
}

function summary(state,title,description,metadata=[]){
  const host=$('console-summary');host.className='console-summary result-'+state;
  const symbol=el('span','result-symbol');symbol.append(icon(state==='passed'?'check-circle-2':state==='failed'||state==='error'?'circle-alert':state==='running'?'loader-circle':state==='stale'?'refresh-cw':'terminal'));
  const copy=el('div','result-copy');copy.append(el('h2','',title));
  if(description)copy.append(el('p','',description));
  if(metadata.length){const line=el('div','result-meta');for(const text of metadata)line.append(el('span','',text));copy.append(line)}
  host.replaceChildren(symbol,copy);$('pane-console').dataset.state=state;
}

export function pendingResult(action){
  $('console-kind').textContent=action==='submit'?'Submitting':'Running';
  $('console-checks').hidden=true;$('console-details').hidden=true;$('console-output').hidden=true;
  summary('running',action==='submit'?'Checking your answer…':'Running your code…',action==='submit'?'Checking the lesson requirements.':'Try it out. This run does not submit your answer.');
  $('console-body').scrollTop=0;
}

export function resultError(action){
  summary('error',(action==='submit'?'Submission':'Run')+' could not start.','Your code draft is still in the editor.');
  $('console-kind').textContent='Could not start';
}

export function challengeResult({result,mode,item}){
  $('console-body').scrollTop=0;
  const debug=result?.graded===false,program=mode==='playground'||result?.run_kind==='program';
  const list=$('console-checks'),details=$('console-details'),output=$('console-output');
  list.replaceChildren();list.hidden=true;details.hidden=true;output.hidden=true;output.textContent='';
  $('pane-console').classList.toggle('ready-to-submit',!!result?.passed&&!result.stale&&debug&&!program);
  if(!result){
    $('console-kind').textContent=mode==='playground'?'Scratchpad':'Ready';
    summary('idle',mode==='playground'?'Room to experiment.':'Ready when you are.',mode==='playground'?'Try an idea here. Your challenge has its own file.':item?.execution_mode==='script'?'Run to see your output. Submit when it matches the task.':'Run to try your solution. Submit to save completion.');
    return;
  }
  const state=result.stale?'stale':result.passed?'passed':'failed';
  const heading=result.stale?'Code changed. Run again.':program?(result.passed?'Program finished.':'Program needs attention.'):debug?(result.passed?'Checks passed. Ready to submit.':'Something needs a closer look.'):result.passed?'Challenge complete.':'A few things to work on.';
  const rows=program?[]:testRows(result.output||'',item?.language);
  const counts=rows.length?`${rows.filter(row=>row.state==='passed').length} of ${rows.length} checks passed` : '';
  const meta=[];if(Number.isFinite(Number(result.duration)))meta.push(`${result.duration} s`);
  meta.push(result.stale?'Earlier code':debug?'Not submitted':'Submitted');
  if(result.xp_earned)meta.push(`+${result.xp_earned} XP`);
  summary(state,heading,result.stale?'These results are from your earlier code.':counts||'',meta);
  $('console-summary').title=result.checked_at?.replace('T',' ')||'';
  $('console-kind').textContent=result.stale?'Run again':program?'Program output':debug?'Test run':'Submission';
  for(const row of rows){
    const li=el('li','check-result');li.dataset.state=result.stale?'stale':row.state;
    li.append(icon(row.state==='passed'?'check':row.state==='skipped'?'minus':'x'),el('span','check-name',row.name),el('span','check-state',row.state==='passed'?'Passed':row.state==='skipped'?'Skipped':'Needs work'));list.append(li);
  }
  list.hidden=!rows.length;
  const showProgram=program||(result.passed&&!result.stale&&result.program_output!==undefined);
  output.textContent=showProgram?(result.program_output??result.output)||'(Your program did not print anything.)':result.output||'(No output)';
  $('console-output-label').textContent=showProgram?'Program output':'Full test output';
  details.hidden=false;output.hidden=false;details.open=showProgram||!rows.length||!result.passed;
}
