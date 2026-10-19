import {highlightTree,classHighlighter} from '@lezer/highlight';
import {python} from '@codemirror/lang-python';
import {go} from '@codemirror/lang-go';

const element=(tag,className,text)=>{const node=document.createElement(tag);if(className)node.className=className;if(text!==undefined)node.textContent=text;return node};

function highlight(code,language){
  const source=code.textContent;
  const parser=language==='python'?python().language.parser:language==='go'?go().language.parser:null;
  if(!parser)return;
  const result=document.createDocumentFragment();let cursor=0;
  highlightTree(parser.parse(source),classHighlighter,(from,to,classes)=>{
    if(from>cursor)result.append(document.createTextNode(source.slice(cursor,from)));
    result.append(element('span',classes,source.slice(from,to)));cursor=to;
  });
  if(cursor<source.length)result.append(document.createTextNode(source.slice(cursor)));
  code.replaceChildren(result);
}

function examples(article,language){
  for(const pre of [...article.querySelectorAll('pre')]){
    if(pre.closest('.worked-example,.example-output'))continue;
    const code=pre.querySelector('code');if(!code)continue;
    const declared=code.className.match(/language-(\w+)/)?.[1];
    const chosen=declared||language;
    highlight(code,chosen);
    const output=pre.nextElementSibling?.matches('.example-output')?pre.nextElementSibling:null;
    const figure=element('figure','worked-example');const caption=element('figcaption','example-caption');
    caption.append(element('span','','Example'),element('span','example-language',chosen==='python'?'Python':chosen==='go'?'Go':chosen||'Code'));
    pre.replaceWith(figure);figure.append(caption,pre);if(output)figure.append(output);
  }
}

function callouts(article){
  const names={NOTE:'Note',TIP:'Remember',IMPORTANT:'Key idea',WARNING:'Watch out',CAUTION:'Watch out'};
  for(const quote of [...article.querySelectorAll('blockquote')]){
    const first=quote.querySelector('p');const marker=first?.textContent.match(/^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*/);
    if(!marker||first.firstChild?.nodeType!==Node.TEXT_NODE)continue;
    first.firstChild.nodeValue=first.firstChild.nodeValue.replace(/^\[!\w+\]\s*/,'');
    if(!first.textContent.trim())first.remove();
    const box=element('div','markdown-alert markdown-alert-'+marker[1].toLowerCase());
    const title=element('p','markdown-alert-title');const icon=element('i');icon.dataset.lucide=marker[1]==='TIP'?'lightbulb':'circle-alert';
    title.append(icon,document.createTextNode(names[marker[1]]));box.append(title,...quote.childNodes);quote.replaceWith(box);
  }
}

export function formatLesson({intro,after,task,language}){
  const goal=intro.querySelector(':scope > p:not(.lesson-concept)');
  if(goal&&goal.textContent.length<280){
    const box=element('div','lesson-goal');box.append(element('span','goal-label','Your goal'));
    goal.replaceWith(box);box.append(goal);
  }
  for(const article of [intro,after,task]){
    examples(article,language);callouts(article);
    for(const heading of article.querySelectorAll('h2,h3'))heading.classList.add('lesson-section-heading');
  }
  const reflection=after.querySelector('h2');
  if(reflection&&/Before you run|Think it through/.test(reflection.textContent))reflection.textContent='Quick check';
  for(const paragraph of after.querySelectorAll(':scope > p'))if(paragraph.textContent.startsWith('Read the explanation, predict'))paragraph.classList.add('study-tip');
  for(const paragraph of task.querySelectorAll(':scope > p')){
    if(/^This is a |^Write directly in /.test(paragraph.textContent))paragraph.classList.add('task-kind');
  }
  return intro.querySelector('.worked-example')||intro.querySelector('.program-picture,.list-picture')||after.querySelector('.worked-example');
}
