import {build} from 'esbuild';
import {mkdir,copyFile,readFile,writeFile} from 'node:fs/promises';
const ui = new URL(process.argv.includes('--preview')?'../.tools/studio-preview/ui/':'../ui/', import.meta.url);
const out = new URL('assets/', ui);
await mkdir(out,{recursive:true});
await build({entryPoints:['workbench.js'],bundle:true,minify:true,format:'iife',target:'es2022',outfile:new URL('workspace.js',out).pathname.replace(/^\/([A-Za-z]:\/)/,'$1'),legalComments:'eof'});
await copyFile(new URL('studio.html',import.meta.url),new URL('studio.html',ui));
await copyFile(new URL('workspace.css',import.meta.url),new URL('studio.css',ui));
const markdownThemes=[];
for(const [mode,file] of [['light','github-markdown-light.css'],['dark','github-markdown-dark-dimmed.css']]){
  const css=await readFile(new URL('vendor/github-markdown-css/'+file,import.meta.url),'utf8');
  markdownThemes.push(css.replaceAll('.markdown-body',`:where([data-bs-theme=${mode}]) .markdown-body`));
}
await writeFile(new URL('markdown.css',out),markdownThemes.join('\n'));
await copyFile(new URL('lesson.css',import.meta.url),new URL('lesson.css',out));
await copyFile(new URL('challenge.css',import.meta.url),new URL('challenge.css',out));
for (const [from,to] of [
  ['bootstrap/dist/css/bootstrap.min.css','bootstrap.min.css'],
  ['@fontsource-variable/inter/files/inter-latin-wght-normal.woff2','inter.woff2'],
  ['@fontsource-variable/lora/files/lora-latin-wght-normal.woff2','lora.woff2'],
  ['@fontsource-variable/jetbrains-mono/files/jetbrains-mono-latin-wght-normal.woff2','jetbrains-mono.woff2']
]) await copyFile(new URL('./node_modules/'+from,import.meta.url),new URL(to,out));
const packages=['bootstrap','codemirror','@codemirror/view','@codemirror/state','@codemirror/lang-python','@codemirror/lang-go','@codemirror/commands','@codemirror/theme-one-dark','@codemirror/language','@lezer/highlight','lucide','marked','dompurify','@fontsource-variable/inter','@fontsource-variable/lora','@fontsource-variable/jetbrains-mono'];
const notices=[];
for(const name of packages){
  const dir=new URL('./node_modules/'+name+'/',import.meta.url);
  const pkg=JSON.parse(await readFile(new URL('package.json',dir),'utf8'));
  let license='See package repository for license.';
  for(const file of ['LICENSE','LICENSE.txt','LICENSE.md','OFL.txt']){try{license=await readFile(new URL(file,dir),'utf8');break}catch{}}
  notices.push(`${name} ${pkg.version}\n${JSON.stringify(pkg.repository||'')}\n\n${license}`);
}
const markdownLicense=await readFile(new URL('vendor/github-markdown-css/license',import.meta.url),'utf8');
const markdownSource=JSON.parse(await readFile(new URL('vendor/github-markdown-css/source.json',import.meta.url),'utf8'));
await writeFile(new URL('THIRD_PARTY_NOTICES.txt',out),notices.join('\n\n'+ '='.repeat(72)+'\n\n')+'\n\ngithub-markdown-css\n'+markdownSource.repository+'\nCommit: '+markdownSource.commit+'\n\n'+markdownLicense);
console.log('Built offline UI assets.');
