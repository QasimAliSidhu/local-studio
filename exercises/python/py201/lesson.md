# Run a script without surprising its importer

Use the __name__ guard after functions and imports are understood.

## Separate importing from running

- **Put the script's work in `main()`.** Defining the function does not run its body.

- **Check `__name__`.** Direct execution sets it to `"__main__"`; importing uses the module's name.

- **Guard the call.** `if __name__ == "__main__":` lets a direct run call `main()` while an import stays quiet.

## Walk through an example

```python
def main():
    print("Started")

if __name__ == "__main__":
    main()
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Python supplies a module-level name called `__name__`. When a file is executed as the entry script, that name has the value `"__main__"`. When the file is imported normally, it has its module name instead.

The familiar if syntax can use this difference: `if __name__ == "__main__":` guards the code that should run only for direct execution. Definitions remain available for import, while the guarded action stays quiet. The double underscores are part of the exact supplied name.

A small main function makes the entry behavior easy to find. Defining main does not run it; the call inside the guard does. This is useful when a test or another program imports your helper functions.

The example prints Started when run directly and prints nothing merely because somebody imports the module. Pip's last utility launched a countdown every time it was imported. The test suite now flinches at imports.

</details>

## Before you run

Why should importing a reusable module not execute its command-line workflow?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
