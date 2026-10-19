# Files deserve a closing ceremony

Use pathlib, UTF-8 and context-managed file access.

## Read a file within a clear lifetime

- **Open text with its encoding.** Use UTF-8 when that is the format promised by the contract.

- **Use `with` for cleanup.** The file is closed when the block ends, including on failure.

- **Separate blank data from missing data.** Strip and filter lines as requested, but let a missing file raise `FileNotFoundError`.

## Walk through an example

```python
from pathlib import Path

with Path("notes.txt").open(encoding="utf-8") as handle:
    text = handle.read()
# handle is closed here, even if reading failed.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A file connects your program to persistent bytes outside its normal variables. Text mode decodes those bytes using an encoding. Choose UTF-8 explicitly when your format expects it rather than relying on a machine-specific default. A `with` block closes the file when the block ends, including on an exception.

`pathlib.Path` represents filesystem paths and supports methods such as open, read_text and write_text. Imports bring definitions from another module into your file; keep reusable functions at module scope and put optional command-line execution under `if __name__ == "__main__":` so importing does not start the app.

In larger projects, split related responsibilities into modules and use a virtual environment for project dependencies (`python -m venv .venv`). This exercise uses only the standard library. Pip once left every log file open 'for emotional support'. The operating system imposed a less sentimental limit.

</details>

## Before you run

Why should a missing file not silently become an empty report?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
