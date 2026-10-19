# Credits and source references

Local Studio was built by Qasim Ali with Codex. Its lesson prose and exercises are original. The public beginner Python concept outline was used as a coverage reference, not as imported commercial lesson text.

## Inspiration

- [Boot.dev](https://www.boot.dev/) and Lane Wagner: hands-on programming education.
- [Boot.dev learning principles](https://www.boot.dev/about): related background on practice-based learning.

## Software used

- [CodeMirror basic setup](https://github.com/codemirror/basic-setup) and the [CodeMirror project](https://github.com/codemirror/dev): editor and language tooling.
- [Bootstrap](https://github.com/twbs/bootstrap): interface components and styling.
- [Lucide](https://github.com/lucide-icons/lucide): icons.
- [Marked](https://github.com/markedjs/marked): Markdown rendering.
- [DOMPurify](https://github.com/cure53/DOMPurify): rendered-content sanitization.
- [github-markdown-css](https://github.com/sindresorhus/github-markdown-css), by Sindre Sorhus: vendored lesson typography themes. Its pinned source record and license are retained in `ui-src/vendor/github-markdown-css`.
- [Inter](https://github.com/rsms/inter), [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) and [Lora](https://github.com/cyrealtype/Lora-Cyrillic): typefaces, packaged through [Fontsource](https://github.com/fontsource/font-files).
- [esbuild](https://github.com/evanw/esbuild): frontend bundling.
- [Python](https://www.python.org/) and [Go](https://go.dev/): language runtimes; users install their own.

Exact UI package versions are recorded in `ui-src/package-lock.json`. Bundled upstream copyright and license notices remain in [ui/assets/THIRD_PARTY_NOTICES.txt](ui/assets/THIRD_PARTY_NOTICES.txt).

Tailwind Typography was a reading-layout reference during development; it is not an installed dependency in this release.

## Demo and creative assets

The demo uses an isolated workspace with synthetic learner state and real program/test output. Its opening cover was created with built-in image generation using the actual interface as reference. [The prompt](docs/social/cover-prompt.txt) is included. Transition tones were synthesized for the demo; no third-party music is used. These credits do not imply endorsement or affiliation.
