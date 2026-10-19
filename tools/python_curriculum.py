"""Original Python curriculum. Content source, not an importer of commercial lessons.

Run build_python_course.py to install missing lessons without replacing learner code.
Every lesson has its own explanation, contract, starter, reference and executable tests.
"""
from textwrap import dedent

CHAPTERS = [
    ('First contact', 'Get comfortable reading, editing and running small programs.'),
    ('Names, values and strings', 'Represent real information and make readable messages.'),
    ('Functions with a job', 'Build reusable operations with clear inputs and outputs.'),
    ('Scope and side effects', 'Understand which names and objects a call can change.'),
    ('Testing and detective work', 'Turn a surprising result into a reproducible, fixable case.'),
    ('Computing without magic', 'Reason about integer arithmetic, bits and floating point.'),
    ('Decisions and comparisons', 'Translate rules into precise conditions and branches.'),
    ('Loops that know when to stop', 'Repeat work, keep state and handle boundaries.'),
    ('Lists, tuples and sequences', 'Index, slice, transform and copy ordered collections.'),
    ('Dictionaries and records', 'Look up, update, group and reshape structured data.'),
    ('Sets and membership', 'Compare collections when uniqueness matters more than order.'),
    ('Errors with useful messages', 'Validate inputs, recover selectively and clean up reliably.'),
    ('Types as documentation', 'Describe contracts without mistaking annotations for validation.'),
    ('The helpdesk needs a hero', 'Combine the fundamentals in practical backend missions.'),
    ('Checkpoint: ship it thoughtfully', 'Apply several concepts together without a step-by-step recipe.'),
    ('Objects with responsibilities', 'Model independent state, invariants, inheritance and composition.'),
    ('Functional tools and lazy work', 'Use pure transformations, callbacks, recursion and generators.'),
    ('Files, data and backend foundations', 'Work with files, structured formats, storage and async tasks.'),
]
LESSONS = []


def add(title, goal, teaching, example, task, starter, solution, checks, hint, reflection):
    number = 101 + len(LESSONS)
    chapter = (number - 101) // 4 + 1
    LESSONS.append(dict(id=f'py{number}', title=title, chapter=chapter, goal=goal,
        teaching=dedent(teaching).strip(), example=dedent(example).strip(),
        task=dedent(task).strip(), starter=dedent(starter).strip()+'\n',
        solution=dedent(solution).strip()+'\n', checks=checks, hint=hint, reflection=reflection))


# Chapters 1-4: no prior programming experience assumed.
add('Hello, slightly suspicious server',
    'Run your first Python program and distinguish printed output from returned values.',
    '''A program is a sequence of instructions. Python executes those instructions, and `print()` sends a value to the console. Text inside matching quotes is a **string**; the quotes mark its boundaries and are not printed. Parentheses hold the arguments supplied to an operation.

    The tiny function wrapper in the editor lets our tests call your code repeatedly. For now, put your instruction on its indented line. We will unpack functions properly in chapter 3. Lines beginning with `#` are comments for humans, including future-you, who is famously forgetful.

    **Printing and returning are different.** Printing creates visible output. Returning hands a result to the caller. A function without an explicit return produces `None`. Our office robot, Pip, cannot eat `None`, but has submitted a procurement request anyway.''',
    'print("Service online")\n# Console: Service online',
    '''Inside `announce()`, print exactly `Helpdesk online!` followed by the normal newline. Do not return that text. The function should return `None`, as a function with no explicit return does.''',
    'def announce():\n    # Replace this line with your first instruction.\n    raise NotImplementedError("Wake up the helpdesk")',
    'def announce():\n    print("Helpdesk online!")',
    [('exact_message', 'with redirect_stdout(StringIO()) as output:\n    result = announce()\nself.assertEqual(output.getvalue(), "Helpdesk online!\\n")\nself.assertIsNone(result)'),
     ('repeatable', 'with redirect_stdout(StringIO()) as output:\n    announce()\n    announce()\nself.assertEqual(output.getvalue(), "Helpdesk online!\\n" * 2)'),
     ('no_extra_output', 'with redirect_stdout(StringIO()) as output:\n    announce()\nself.assertEqual(len(output.getvalue().splitlines()), 1)')],
    'Call print with the message inside matching quotes. Keep it indented under def.',
    'What changes if you replace print with return? Ask the tutor, then try it in Extra practice.')

add('The deployment countdown', 'Predict execution order and produce several lines of output.',
    '''Python normally runs statements from top to bottom. Each call to `print()` finishes its line with a newline, so three calls produce three lines. A string containing `\\n` can also describe several lines, but separate calls make execution order easy to inspect.

    A **syntax error** means Python cannot read the program: an unmatched quote or missing parenthesis can prevent the whole file from running. A **wrong result** means the program runs but does something different from the requirement. These call for different investigations: repair syntax first, then compare behavior with the contract.

    Pip has scheduled deployment before breakfast. Nobody agreed to this. Your job is to make the startup sequence unambiguous so the console can tell us what happened and in what order. Exact output matters when another program reads your messages.''',
    'print("Connect")\nprint("Check")\nprint("Ready")\n# Connect appears before Check.',
    'Make `countdown()` print three lines in order: `3`, `2`, then `Launch!`. Use print; return no value.',
    'def countdown():\n    raise NotImplementedError("Launch sequence missing")',
    'def countdown():\n    print(3)\n    print(2)\n    print("Launch!")',
    [('line_order','with redirect_stdout(StringIO()) as output:\n    countdown()\nself.assertEqual(output.getvalue().splitlines(), ["3", "2", "Launch!"])'),
     ('newline','with redirect_stdout(StringIO()) as output:\n    result = countdown()\nself.assertTrue(output.getvalue().endswith("\\n"))\nself.assertIsNone(result)'),
     ('independent_calls','with redirect_stdout(StringIO()) as output:\n    countdown()\n    countdown()\nself.assertEqual(output.getvalue(), "3\\n2\\nLaunch!\\n" * 2)')],
    'Write one print call per line. Numeric literals do not need quotes.',
    'If the second line has an unmatched quote, will the first line print? Why?')

add('Quotes are not comments', 'Use comments, escapes and string literals correctly.',
    '''A `#` starts a comment only when it is outside a string. Inside quotes it is ordinary text. Likewise, Python cares about matching opening and closing quotes, not whether you prefer single or double quotes. Pick the pair that makes the content easiest to read.

    An escape sequence uses a backslash to represent a special character. `\\n` represents a newline; `\\"` can include a double quote inside a double-quoted string. You can often avoid an escape by choosing the other quote style. A triple-quoted string can span several source lines, but includes those newlines in its value.

    Comments should explain a decision rather than narrate every obvious line. `# Pip insisted` is funny, but a note explaining why a legacy client requires an exact status message is more useful during an outage.''',
    '''print('The robot said "ready".')\nprint("Queue #7")  # This part is a comment.''',
    '''Return the exact string `Pip says: "Ship it!" #probably`. The hash and double quotes are part of the value. Do not print it.''',
    'def robot_message():\n    raise NotImplementedError("Pip has lost the quotation marks")',
    '''def robot_message():\n    return 'Pip says: "Ship it!" #probably' ''',
    [('punctuation','self.assertEqual(robot_message(), \'Pip says: "Ship it!" #probably\')'),
     ('string_value','self.assertIsInstance(robot_message(), str)'),
     ('no_console_side_effect','with redirect_stdout(StringIO()) as output:\n    robot_message()\nself.assertEqual(output.getvalue(), "")')],
    'Use single quotes around the whole string so the double quotes can stay inside it.',
    'Where would you put a comment explaining why the punctuation must stay exact?')

add('Read the value, not the vibes', 'Inspect a value with len and type, and read function calls inside out.',
    '''Built-in functions are operations Python makes available without an import. `len(text)` counts the elements in a string, while `type(value)` identifies the kind of object. `type(value).__name__` is the readable name, such as `str` or `int`. The double underscores look dramatic; here you only need to read the attribute.

    Calls can be nested. In `print(len("queue"))`, Python evaluates the inner call first, then passes its result to the outer call. The console displays `5`, not the word `queue`.

    A function can return several values separated by commas. Python packages them into a tuple, an ordered collection we will explore later. The supplied wrapper lets you practice observing inputs without needing all the surrounding syntax at once. Debugging starts with looking at evidence. Pip's gut feeling is currently a fan bearing.''',
    'print(len("queue"))  # 5\nprint(type(42).__name__)  # int',
    'Implement `inspect_text(text)`. Inputs are strings. Return `(length, type_name)`, for example `inspect_text("API") == (3, "str")`. Spaces count; an empty string has length zero.',
    'def inspect_text(text):\n    raise NotImplementedError("Collect evidence")',
    'def inspect_text(text):\n    return len(text), type(text).__name__',
    [('ordinary','self.assertEqual(inspect_text("API"), (3, "str"))'),('empty','self.assertEqual(inspect_text(""), (0, "str"))'),('spaces_count','self.assertEqual(inspect_text("a b"), (3, "str"))')],
    'Return two comma-separated expressions: len(text), then type(text).__name__.',
    'What does len("123") describe? Is that the same as the number 123?')

add('Give your numbers useful names', 'Assign names, update a value and convert units without changing the caller.',
    '''Assignment binds a name to a value: `minutes = 4`. The `=` symbol is an instruction to assign, not a mathematical claim of equality. You can reuse a name later, and an expression on the right is evaluated before the new binding is made.

    Python has integer values (`int`), decimal approximations (`float`), text (`str`), booleans (`bool`), and the absence marker `None`. A name can be rebound to a different type, but changing its meaning mid-function makes code harder to follow. Name quantities after what they mean and include units when confusion would be costly.

    `total += extra` is a shorter way to write `total = total + extra`. For immutable numbers it creates a new numeric result. It does not reach back into the caller and alter their integer. Pip once confused seconds and minutes. The incident review lasted six hours, or possibly six minutes.''',
    'seconds_per_minute = 60\nminutes = 3\nseconds = minutes * seconds_per_minute\nseconds += 5\n# seconds is 185; minutes is still 3',
    'Return the total seconds in `minutes` plus `extra_seconds`. Both inputs are non-negative integers. Use the supplied parameter names; zero values are valid.',
    'def duration_seconds(minutes, extra_seconds):\n    raise NotImplementedError("Check the units")',
    'def duration_seconds(minutes, extra_seconds):\n    seconds = minutes * 60\n    seconds += extra_seconds\n    return seconds',
    [('normal','self.assertEqual(duration_seconds(3, 5), 185)'),('zeros','self.assertEqual(duration_seconds(0, 0), 0)'),('large_remainder','self.assertEqual(duration_seconds(1, 90), 150)')],
    'Multiply minutes by 60, then add extra_seconds.',
    'Why is a name like duration_seconds safer than a name like x at a service boundary?')

add('Clean up the robot username', 'Transform strings using strip, lower, replace and chaining.',
    '''Strings are immutable: a string method returns a result rather than editing the existing string. `strip()` removes surrounding whitespace, `lower()` changes case, and `replace(old, new)` substitutes matching pieces. Internal whitespace is different from surrounding whitespace; `strip()` does not remove spaces in the middle.

    Method chaining sends one result into the next operation. Read it left to right: `raw.strip().lower()` first trims, then lowercases. If you discard the result and return `raw`, nothing has been cleaned.

    Normalization is a business rule, not a universal truth. Lowercasing an account handle may be appropriate, while lowercasing a password would be a very exciting incident. State the allowed transformation explicitly. This mission concerns display handles only. Pip's proposed handle contained sixteen spaces and a cry for help.''',
    'raw = "  Night Shift  "\nclean = raw.strip().lower()\n# clean: "night shift"; raw is unchanged',
    'Return a handle after trimming outside whitespace, lowercasing letters, and replacing each internal ASCII space with `_`. Do not collapse repeated spaces. Leave punctuation and other characters unchanged.',
    'def normalize_handle(raw):\n    raise NotImplementedError("Name tag printer jammed")',
    'def normalize_handle(raw):\n    return raw.strip().lower().replace(" ", "_")',
    [('ordinary','self.assertEqual(normalize_handle("  Night Shift  "), "night_shift")'),('repeated_spaces','self.assertEqual(normalize_handle("A  B"), "a__b")'),('empty','self.assertEqual(normalize_handle("   "), "")'),('punctuation','self.assertEqual(normalize_handle("Pip-7!"), "pip-7!")')],
    'Keep the result from each string method, or chain the methods.',
    'Why should the contract say whether repeated spaces are collapsed?')

add('A status message worth reading', 'Build f-strings and format a numeric result deliberately.',
    '''An f-string starts with `f` before its opening quote. Expressions inside braces are evaluated and inserted into the text. This avoids awkward chains of string concatenation and explicit conversions. Literal text outside braces stays exactly as written.

    A format specifier follows a colon. `:.2f` displays a number with two decimal places; it changes the displayed representation, not the original value. `:03d` pads an integer with zeros to a minimum width of three. Formatting is part of the interface when a human or another system expects a stable shape.

    Avoid building a sentence from a dozen print calls unless you intentionally want separate lines. Return one complete string here; the caller decides where to display it. Pip's dashboard used to say `success rate: 0.8333333333333334-ish`. The new contract is slightly more professional.''',
    'worker = "Mira"\nload = 7.5\nmessage = f"{worker}: {load:.2f}% load"\n# Mira: 7.50% load',
    'Return `NAME processed COUNT jobs (RATE/s)` with rate shown to two decimal places. Example: `status_line("Pip", 7, 2.5)` returns `Pip processed 7 jobs (2.50/s)`. Inputs are already valid.',
    'def status_line(name, count, rate):\n    raise NotImplementedError("Dashboard wants fewer decimal places")',
    'def status_line(name, count, rate):\n    return f"{name} processed {count} jobs ({rate:.2f}/s)"',
    [('normal','self.assertEqual(status_line("Pip", 7, 2.5), "Pip processed 7 jobs (2.50/s)")'),('zero','self.assertEqual(status_line("A", 0, 0), "A processed 0 jobs (0.00/s)")'),('rounding','self.assertEqual(status_line("Mira", 12, 1.236), "Mira processed 12 jobs (1.24/s)")')],
    'Use f before the string and put :.2f after rate inside its braces.',
    'If you format rate to two decimals, has the numeric rate itself changed?')

add('Numbers wearing string costumes', 'Convert valid text to numbers and use None to represent absence.',
    '''HTTP forms, command-line arguments and configuration files often begin as text. `int("12")` produces an integer; `float("1.5")` produces a floating-point value. Adding strings concatenates them, so `"12" + "3"` produces `"123"`, not fifteen. Convert at a clear boundary before doing numeric work.

    `None` marks a missing value. It differs from zero, an empty string and the string `"None"`. Test identity with `is None` when absence is the rule. A supplied zero can be a meaningful setting, such as disabling retries.

    Conversion can fail on malformed input. Later we will catch selected exceptions and validate ranges. For this exercise the supplied text is a valid integer, or the value is actually `None`. Do not invent extra fallback behavior. Pip's last fallback was to replace every missing number with a motivational quote.''',
    'count = int("12")\nprint(count + 3)  # 15\nmissing = None\nprint(missing is None)  # True',
    'Implement `retry_setting(raw, default=3)`: return default only when raw is None; otherwise return int(raw). Valid integer text may have surrounding whitespace or a sign. Preserve a supplied zero.',
    'def retry_setting(raw, default=3):\n    raise NotImplementedError("Parse the setting")',
    'def retry_setting(raw, default=3):\n    if raw is None:\n        return default\n    return int(raw)',
    [('missing','self.assertEqual(retry_setting(None), 3)\nself.assertEqual(retry_setting(None, 8), 8)'),('zero','self.assertEqual(retry_setting("0", 9), 0)'),('valid_text','self.assertEqual(retry_setting("  +12 "), 12)')],
    'Check raw is None before converting. Do not use raw or default.',
    'Why does the string "0" need conversion before a numeric comparison?')

add('Return to sender', 'Write a function with a clear input/output contract.',
    '''A function gives a group of instructions a name. `def` defines it; a later call runs it. Parameters are local names filled with arguments from that call. Indentation identifies the body, so keep every instruction belonging to the function at the same nesting level.

    `return` ends the call and sends a value to the caller. Code after an unconditional return will not run. Printing a value does not make it the function's result, which matters when tests or another function need to use it.

    A useful contract says which inputs are accepted and what the result means. Here we use integer cents so a simple price calculation avoids floating-point currency surprises. Validation is not required unless the contract says so. Pip asked whether a function could return a sandwich; technically it can return an object representing one. Procurement remains unconvinced.''',
    'def double(number):\n    return number * 2\n\nanswer = double(6)\n# answer is 12',
    'Return total price in cents for quantity items at unit_price cents each, plus one delivery_fee for the whole order. All inputs are non-negative integers, and the fee applies even to quantity zero.',
    'def order_total(unit_price, quantity, delivery_fee):\n    raise NotImplementedError("Return the bill")',
    'def order_total(unit_price, quantity, delivery_fee):\n    return unit_price * quantity + delivery_fee',
    [('normal','self.assertEqual(order_total(125, 4, 50), 550)'),('zero_quantity','self.assertEqual(order_total(500, 0, 20), 20)'),('no_printing','with redirect_stdout(StringIO()) as output:\n    self.assertEqual(order_total(1, 1, 0), 1)\nself.assertEqual(output.getvalue(), "")')],
    'Multiply the per-item price by quantity before adding the one delivery fee.',
    'What would the caller receive if your function only printed the total?')

add('Defaults without guesswork', 'Use default parameters and keyword arguments.',
    '''A parameter can have a default value: `def greet(name, prefix="Hi")`. Callers may leave it out, pass it positionally, or use a keyword. Defaults make common calls concise, while keyword arguments make less obvious choices readable.

    Required parameters come before parameters with defaults in this ordinary signature. A default is used when an argument is omitted, not when an argument happens to be empty, zero or false. A caller passing an empty prefix has made a choice you should preserve.

    Keep a function's interface small and predictable. Reaching into globals for a hidden option makes repeated tests harder to reason about. For immutable strings a default is safe; we will examine the shared mutable default trap in the scope chapter. Pip wants seventeen greeting options. We have approved two parameters and a small nap.''',
    'def greet(name, prefix="Hi"):\n    return f"{prefix}, {name}"\n\ngreet("Mira")\ngreet(name="Mira", prefix="Welcome")',
    'Implement `badge(name, role="learner")`, returning `name [role]`. Both parameters accept strings, including empty strings. Calls using keyword arguments must work.',
    'def badge(name, role="learner"):\n    raise NotImplementedError("Print a badge")',
    'def badge(name, role="learner"):\n    return f"{name} [{role}]"',
    [('default','self.assertEqual(badge("Pip"), "Pip [learner]")'),('keyword','self.assertEqual(badge(role="operator", name="Mira"), "Mira [operator]")'),('explicit_empty','self.assertEqual(badge("Pip", ""), "Pip []")')],
    'Let the signature supply the default; use the received role directly.',
    'How is an omitted role different from role=""?')

add('Small helpers, fewer tiny disasters', 'Compose functions and reuse a supplied helper.',
    '''One function can call another. The caller waits for the helper's return value, then uses it like any other value. This lets you give a meaningful name to a small rule and apply that rule in more than one place.

    Reuse is also about keeping rules consistent. Copying a formula into several functions means a future correction can miss one copy. Calling a helper gives the rule one home. The helper's parameters and return value form an interface; callers need not duplicate its internal instructions.

    Watch argument units and order at the boundary. A helper expecting cents cannot safely receive pounds merely because both values are numbers. We test helper use by replacing it temporarily: if the caller ignores the helper, the replacement result cannot flow through. Pip calls this a surprise inspection. We call it dependency testing.''',
    'def add_fee(amount, fee):\n    return amount + fee\n\ndef checkout(amount):\n    return add_fee(amount, 10)',
    'The supplied `service_fee(subtotal)` returns subtotal // 10. Implement checkout(subtotal, delivery=0) as subtotal + service_fee(subtotal) + delivery. Call the helper so future changes to that rule are honored.',
    'def service_fee(subtotal):\n    return subtotal // 10\n\ndef checkout(subtotal, delivery=0):\n    raise NotImplementedError("Ask the helper")',
    'def service_fee(subtotal):\n    return subtotal // 10\n\ndef checkout(subtotal, delivery=0):\n    return subtotal + service_fee(subtotal) + delivery',
    [('normal','self.assertEqual(checkout(105, 20), 135)'),('default','self.assertEqual(checkout(0), 0)'),('uses_helper','with patch("exercise.service_fee", return_value=7) as helper:\n    self.assertEqual(checkout(100, 2), 109)\n    helper.assert_called_once_with(100)')],
    'Call service_fee inside checkout; add the returned result, not the function object.',
    'Why does replacing the helper reveal a copied fee formula?')

add('Two answers, one return trip', 'Return and unpack tuples without losing the remainder.',
    '''Comma-separated return values form a tuple. A caller can unpack it into the same number of names: `first, second = result`. The position of each value is part of the contract; swapping them creates a valid tuple with the wrong meaning.

    Tuples are useful for a small, fixed group of related results. When a group grows or positions become difficult to remember, a named record is usually clearer. Unpacking does not run the calculation twice; it assigns each component from one returned result.

    Integer division and remainder are handy when dividing a quantity into full units and leftovers. `//` counts complete groups and `%` gives what remains. For non-negative values, these describe exactly how many full minutes fit into a duration. Pip's time tracker reports ninety seconds as one and a half coffee breaks. Your interface must be more conventional.''',
    'def split_boxes(items):\n    return items // 6, items % 6\n\nfull, loose = split_boxes(14)\n# full == 2, loose == 2',
    'Return (minutes, seconds_left) for a non-negative integer total_seconds. There are 60 seconds in a minute; seconds_left must be between 0 and 59.',
    'def split_duration(total_seconds):\n    raise NotImplementedError("Recover the spare seconds")',
    'def split_duration(total_seconds):\n    return total_seconds // 60, total_seconds % 60',
    [('mixed','self.assertEqual(split_duration(125), (2, 5))'),('boundaries','self.assertEqual(split_duration(0), (0, 0))\nself.assertEqual(split_duration(60), (1, 0))'),('reconstruct','for total in [1, 59, 61, 3601]:\n    minutes, seconds = split_duration(total)\n    self.assertEqual(minutes * 60 + seconds, total)\n    self.assertTrue(0 <= seconds < 60)')],
    'Use // for the complete minutes and % for the remainder.',
    'What happens if you use / instead of // for minutes?')

add('Local names, local business', 'Read a global constant while keeping call-specific variables local.',
    '''Each function call has its own local namespace. Assigning `label = ...` inside a function creates or rebinds that local name. It does not automatically rebind a name with the same spelling outside the function.

    When reading an ordinary name, Python looks through enclosing scopes and then the module and built-ins. A module-level constant can supply a default rule, but a local result should be returned explicitly. Uppercase names are a convention for constants, not an enforcement mechanism.

    Assignment inside a function makes that name local unless `global` or `nonlocal` says otherwise. Reading a name before its local assignment can produce `UnboundLocalError`; moving a line at random does not explain the real issue. Prefer explicit inputs and outputs when the job does not require shared state. Pip says all variables should be global because sharing is caring. Pip is not reviewing this pull request.''',
    'PREFIX = "job"\n\ndef make_label(number):\n    label = f"{PREFIX}-{number}"\n    return label',
    'Keep module constant REGION = "local" unchanged. Implement route_label(service, region=None), returning `region/service`. Use REGION only when region is None, and preserve an explicitly empty region.',
    'REGION = "local"\n\ndef route_label(service, region=None):\n    raise NotImplementedError("Keep the constant constant-ish")',
    'REGION = "local"\n\ndef route_label(service, region=None):\n    chosen = REGION if region is None else region\n    return f"{chosen}/{service}"',
    [('default','self.assertEqual(route_label("api"), "local/api")'),('override','self.assertEqual(route_label("api", "west"), "west/api")\nself.assertEqual(REGION, "local")'),('explicit_empty','self.assertEqual(route_label("api", ""), "/api")')],
    'Choose a new local name for the selected region instead of assigning REGION.',
    'Why would adding global REGION make this tiny function harder to use safely?')

add('The list with two name tags', 'Distinguish aliasing, shallow copying and nested object mutation.',
    '''Assignment does not copy an object. If `other = original` and original is a list, both names refer to the same list. Appending through either name is visible through the other. Rebinding one name to a new list is different: it changes that binding rather than editing the shared object.

    `list(original)` or `original.copy()` creates a shallow list copy. Its outer list is independent, but references to nested mutable objects are still shared. Copying a dictionary has the same shallow limitation. For a known shape, copying only the containers you intend to modify can be clearer than blindly copying an entire graph.

    A non-mutating transformation makes retries and tests easier because the input remains usable. This mission has a dictionary containing a list, so copying just the dictionary is insufficient. Pip put two labels on one lunchbox and was surprised the second lunch vanished too.''',
    'source = {"tags": ["new"], "owner": "Mira"}\ncopy = dict(source)\ncopy["tags"] = list(source["tags"])\ncopy["tags"].append("checked")\n# source still has only "new"',
    'Return a new record with tag appended to its `tags` list. Records have tags (a list of strings) and may have other fields. Preserve all other fields. Do not mutate the record or its original tags list; duplicates are allowed.',
    'def tagged_copy(record, tag):\n    raise NotImplementedError("One lunchbox is not two lunchboxes")',
    'def tagged_copy(record, tag):\n    result = dict(record)\n    result["tags"] = list(record["tags"]) + [tag]\n    return result',
    [('result','self.assertEqual(tagged_copy({"tags": ["a"], "id": 7}, "b"), {"tags": ["a", "b"], "id": 7})'),('independence','original = {"tags": [], "id": 1}\nresult = tagged_copy(original, "x")\nself.assertEqual(original, {"tags": [], "id": 1})\nself.assertIsNot(result, original)\nself.assertIsNot(result["tags"], original["tags"])'),('duplicates','self.assertEqual(tagged_copy({"tags": ["x"]}, "x")["tags"], ["x", "x"])')],
    'Copy the outer dictionary and create a new tags list before adding the tag.',
    'Would copying only the outer dictionary protect its original tags list?')

add('The haunted default argument', 'Avoid shared mutable defaults across function calls.',
    '''Default argument expressions are evaluated when a function is defined, not once per call. A default like `items=[]` therefore creates one list that later calls can share. Appending into it makes a supposedly fresh call remember earlier visitors. This is a real source of bugs, even though the syntax looks friendly.

    Use an immutable sentinel such as `None`, then create a new list when the caller omits the value. Also decide whether a caller-provided list should be changed. Those are separate contract choices: avoiding a shared default does not automatically make a function non-mutating.

    Here the contract requests a new result every time. Copy an incoming list before appending, and use an empty list only for a missing argument. An explicitly empty list is still the caller's object. Pip has declared the shared default haunted. We have declared it a lifetime problem.''',
    'def add_note(note, notes=None):\n    result = [] if notes is None else list(notes)\n    result.append(note)\n    return result',
    'Implement add_job(job, jobs=None). Return a fresh list containing the supplied jobs, then job. Omitted jobs means an empty starting list. Never modify a supplied list or leak jobs between calls.',
    'def add_job(job, jobs=None):\n    raise NotImplementedError("Evict the default-argument ghost")',
    'def add_job(job, jobs=None):\n    result = [] if jobs is None else list(jobs)\n    result.append(job)\n    return result',
    [('fresh_calls','self.assertEqual(add_job("a"), ["a"])\nself.assertEqual(add_job("b"), ["b"])'),('caller_list','jobs = ["a"]\nresult = add_job("b", jobs)\nself.assertEqual(result, ["a", "b"])\nself.assertEqual(jobs, ["a"])\nself.assertIsNot(result, jobs)'),('empty_input','jobs = []\nself.assertEqual(add_job("a", jobs), ["a"])\nself.assertEqual(jobs, [])')],
    'Create a fresh result whether jobs is omitted or supplied.',
    'When is [] created in def f(items=[]), and why does that matter?')

add('A counter with a private office', 'Use a closure and nonlocal for intentionally retained state.',
    '''An inner function can retain access to variables from its enclosing function after that outer call has finished. This combination of a function and its retained environment is a closure. Separate outer calls create separate environments, which is useful for small independent counters or configured callbacks.

    Reading an enclosing name requires no extra keyword. Rebinding it inside the inner function requires `nonlocal`; otherwise the assignment makes a new local name, and an earlier read fails. `nonlocal` refers to an enclosing function scope, while `global` refers to module scope.

    Stateful code is appropriate when state is the point. Make that state deliberate and scoped rather than letting unrelated calls share a global counter. A closure is not automatically safe under simultaneous access; that is a separate concern. Pip wants private offices for integers. This is the budget version.''',
    'def make_counter(start):\n    current = start\n    def tick():\n        nonlocal current\n        current += 1\n        return current\n    return tick',
    'Return a callable from make_ticket_counter(start=0). Each call increments its private count by one and returns it. Two counters must remain independent. The first result from start=10 is 11.',
    'def make_ticket_counter(start=0):\n    raise NotImplementedError("Give the counter its own office")',
    'def make_ticket_counter(start=0):\n    current = start\n    def next_ticket():\n        nonlocal current\n        current += 1\n        return current\n    return next_ticket',
    [('sequence','counter = make_ticket_counter()\nself.assertEqual([counter(), counter(), counter()], [1, 2, 3])'),('custom_start','counter = make_ticket_counter(10)\nself.assertEqual(counter(), 11)'),('independent','a, b = make_ticket_counter(2), make_ticket_counter(20)\nself.assertEqual(a(), 3)\nself.assertEqual(b(), 21)\nself.assertEqual(a(), 4)')],
    'Keep current in the outer function, and use nonlocal current in the returned inner function.',
    'How would storing current at module scope break independent counters?')

# Chapters 5-8: testing, computing, decisions and loops.
add('The off-by-one incident', 'Read a failing assertion and repair a boundary error.',
    '''A test compares observed behavior with an expected result. A failure is evidence about one input, not a verdict on your ability. Read the assertion and its input before changing code. If a boundary fails while ordinary cases pass, investigate the boundary rule rather than rewriting everything.

    An inclusive upper bound uses `<=`; an exclusive upper bound uses `<`. Neither is universally correct. The contract decides. Test immediately below, exactly at, and immediately above a threshold to distinguish them.

    The editor contains a plausible but wrong implementation. Use the failing cases to explain its mistake, fix the smallest rule, then run the whole suite. A passing example does not prove all inputs work. Pip filed this incident as 'one number being dramatic'. The incident manager would prefer a reproducible case.''',
    'def within_budget(cost, budget):\n    return cost <= budget\n\n# An exact match is permitted.',
    'Fix can_join(current, capacity). One more person may join only when current is strictly less than capacity. Inputs are non-negative integers. A full room and a zero-capacity room must reject admission.',
    'def can_join(current, capacity):\n    # This implementation has a boundary bug.\n    return current <= capacity',
    'def can_join(current, capacity):\n    return current < capacity',
    [('below','self.assertTrue(can_join(4, 5))'),('exactly_full','self.assertFalse(can_join(5, 5))'),('zero_and_overfull','self.assertFalse(can_join(0, 0))\nself.assertFalse(can_join(8, 5))')],
    'At current == capacity, is there a space left for one more person?',
    'Which single input best distinguishes < from <= here?')

add('Test the test, detective', 'Write assertions that detect several different broken implementations.',
    '''An assertion expresses something that must be true. `assertEqual(actual, expected)` reports the values when they differ. In ordinary Python, `assert condition` raises `AssertionError` if the condition is false. Assertions are useful for internal expectations and tests, but are not a replacement for validating untrusted input: Python can disable assert statements under optimization.

    A test that only checks one happy example may approve a broken implementation. Choose cases for different risks: zero, negative numbers, and a representative positive value. Testing a candidate that always returns the same answer exposes weak tests quickly.

    This mission reverses the usual roles. You supply the checks and our suite feeds them both a correct function and impostors. Pip's first test was 'seems fine'. Pip's second test was 'still seems fine'. We need stronger evidence.''',
    'def check_identity(candidate):\n    assert candidate(0) == 0\n    assert candidate(9) == 9',
    'Implement verify_double(candidate). Use assertions to check that candidate doubles numbers. It must return None for a correct implementation and raise AssertionError for incorrect behavior at 0, -3, or 4. Call the supplied function; do not inspect its source.',
    'def verify_double(candidate):\n    raise NotImplementedError("Cross-examine the impostors")',
    'def verify_double(candidate):\n    assert candidate(0) == 0\n    assert candidate(-3) == -6\n    assert candidate(4) == 8',
    [('correct','self.assertIsNone(verify_double(lambda value: value * 2))'),('constant_impostor','with self.assertRaises(AssertionError):\n    verify_double(lambda value: 8)'),('negative_bug','with self.assertRaises(AssertionError):\n    verify_double(lambda value: abs(value) * 2)'),('zero_bug','with self.assertRaises(AssertionError):\n    verify_double(lambda value: 1 if value == 0 else value * 2)')],
    'Assert exact results for a zero, a negative and a positive input.',
    'Why would checking only candidate(4) let an always-8 function pass?')

add('Breadcrumbs in the console', 'Trace intermediate state while preserving a useful return value.',
    '''A trace records how state changes during execution. When a total is wrong, observing the total after each input can reveal the first step that diverges from your prediction. Start with a tiny example and predict the trace by hand before running it.

    Use messages that identify the values you need. A hundred anonymous numbers can be less useful than three labeled observations. Remove temporary noisy tracing when the investigation ends, or use deliberate logging appropriate to the application. Never log secrets just because the console is convenient.

    Tracing is an observation, not the returned result. A function can print diagnostics and still return a numeric answer. Here the output itself is part of the exercise contract so tests can verify your reasoning. Pip left breadcrumb logs in production. Unfortunately, they were all labeled 'breadcrumb'.''',
    'total = 0\nfor amount in [3, 2]:\n    total += amount\n    print(f"total={total}")\n# total=3, then total=5',
    'Implement trace_total(amounts). Start at zero; for each integer amount add it and print `total=N` with the updated total. Return the final total. Empty input prints nothing and returns zero.',
    'def trace_total(amounts):\n    raise NotImplementedError("Leave useful breadcrumbs")',
    'def trace_total(amounts):\n    total = 0\n    for amount in amounts:\n        total += amount\n        print(f"total={total}")\n    return total',
    [('intermediate_state','with redirect_stdout(StringIO()) as output:\n    result = trace_total([3, -1, 5])\nself.assertEqual(result, 7)\nself.assertEqual(output.getvalue(), "total=3\\ntotal=2\\ntotal=7\\n")'),('empty','with redirect_stdout(StringIO()) as output:\n    self.assertEqual(trace_total([]), 0)\nself.assertEqual(output.getvalue(), "")'),('zero','with redirect_stdout(StringIO()) as output:\n    self.assertEqual(trace_total([0]), 0)\nself.assertEqual(output.getvalue(), "total=0\\n")')],
    'Print after the addition, inside the loop; return after the loop.',
    'What trace would reveal that a print call was accidentally placed before the addition?')

add('The bug that only happens twice', 'Detect accidental shared state by calling a function repeatedly.',
    '''Some bugs depend on history. A function may work once and fail on a second call because it changed module state or a shared input. To reproduce this, test a sequence of calls in one process rather than restarting after every example.

    A pure calculation uses its arguments and returns its result without leaving changes behind. If a running total is only needed for one call, initialize it inside that call. A cache or counter can intentionally retain state, but its contract should say so.

    Diagnose the lifetime of each variable: per iteration, per call, per object, or per process. That question often explains a mysterious growing answer. The starter below accumulates into a global total; the repair is about state ownership, not adding a reset button elsewhere. Pip suggested restarting the server after each invoice. We are going to try a smaller fix.''',
    'def total_lengths(words):\n    total = 0  # new for every call\n    for word in words:\n        total += len(word)\n    return total',
    'Fix sum_request(values) to return the sum of this call\'s integers only. Keep module variable AUDIT_TOTAL unchanged at zero. Do not mutate the input list. Empty input returns zero.',
    'AUDIT_TOTAL = 0\n\ndef sum_request(values):\n    global AUDIT_TOTAL\n    for value in values:\n        AUDIT_TOTAL += value\n    return AUDIT_TOTAL',
    'AUDIT_TOTAL = 0\n\ndef sum_request(values):\n    total = 0\n    for value in values:\n        total += value\n    return total',
    [('repeat_calls','self.assertEqual(sum_request([2, 3]), 5)\nself.assertEqual(sum_request([2, 3]), 5)'),('empty_after_work','sum_request([9])\nself.assertEqual(sum_request([]), 0)'),('no_shared_mutation','values = [-2, 5]\nself.assertEqual(sum_request(values), 3)\nself.assertEqual(values, [-2, 5])\nimport exercise\nself.assertEqual(exercise.AUDIT_TOTAL, 0)')],
    'Use a local total initialized inside the function. Remove the global assignment.',
    'Why might this bug disappear when each manual check uses a fresh process?')

add('Boxes, leftovers and division', 'Use /, // and % according to the meaning of the result.',
    '''`/` produces ordinary division, usually a float. `//` produces floor division, and `%` produces the corresponding remainder. For non-negative integers and a positive divisor, floor division counts whole groups and the remainder counts what is left.

    A partial group may need another container. A ceiling calculation can be built from the whole-group count plus one if a remainder exists. Be careful at exact multiples: an already full final box does not require an extra empty box.

    Floor division rounds toward negative infinity, so negative values need deliberate interpretation. This exercise avoids that ambiguity with non-negative quantities. Python integers can grow beyond machine-word size, but that does not make computations free in time or memory. Pip ordered a box for every item and a separate box for each item's feelings. The warehouse has requested arithmetic.''',
    'items, size = 13, 5\nwhole = items // size  # 2\nloose = items % size   # 3\nboxes = whole + (1 if loose else 0)  # 3',
    'Return the smallest number of boxes needed for items objects, each box holding capacity objects. items >= 0 and capacity > 0 are integers. Zero items need zero boxes.',
    'def boxes_needed(items, capacity):\n    raise NotImplementedError("The warehouse awaits")',
    'def boxes_needed(items, capacity):\n    return (items + capacity - 1) // capacity',
    [('partial','self.assertEqual(boxes_needed(13, 5), 3)'),('exact','self.assertEqual(boxes_needed(10, 5), 2)'),('zero_and_single','self.assertEqual(boxes_needed(0, 7), 0)\nself.assertEqual(boxes_needed(1, 100), 1)')],
    'An exact multiple needs no extra box; any remainder needs one.',
    'Why does items // capacity + 1 fail when items is exactly divisible?')

add('Parentheses prevent incident reports', 'Apply operator precedence and exponentiation deliberately.',
    '''Python evaluates expressions using precedence rules. Exponentiation (`**`) binds more tightly than multiplication and division, which bind more tightly than addition and subtraction. Parentheses explicitly group work and are often worth using even when you remember the rules.

    `2 + 3 * 4` is fourteen; `(2 + 3) * 4` is twenty. A correct business rule can become an incorrect expression if its grouping is lost during translation. Name an intermediate value when a formula is hard to scan.

    Exponentiation expresses repeated multiplication, not an increase by a fixed amount. A backoff delay that doubles on each retry is exponential; adding two seconds on each retry is linear. In real clients, a cap and jitter often avoid synchronized retry storms. Here we implement a precise deterministic cap. Pip calls it 'waiting with ambition'.''',
    'base = 3\nattempt = 2\ndelay = base * (2 ** attempt)\n# 12, not (3 * 2) ** 2',
    'Implement backoff(base, attempt, cap). Return min(base * 2**attempt, cap). base and cap are non-negative integers; attempt is a non-negative integer starting at zero.',
    'def backoff(base, attempt, cap):\n    raise NotImplementedError("Wait exponentially, within reason")',
    'def backoff(base, attempt, cap):\n    return min(base * (2 ** attempt), cap)',
    [('growth','self.assertEqual(backoff(3, 2, 100), 12)'),('first_attempt','self.assertEqual(backoff(5, 0, 100), 5)'),('cap','self.assertEqual(backoff(5, 10, 30), 30)\nself.assertEqual(backoff(0, 4, 10), 0)')],
    'Calculate the power before multiplying, then apply min with the cap.',
    'At attempt zero, why should the multiplier be one?')

add('Tiny permission switches', 'Represent flags with binary integers and bitwise operators.',
    '''A binary digit is a bit, either zero or one. An integer can represent several independent flags by giving each flag a different power-of-two position. Binary literal `0b0100` is the same numeric value as decimal four; `bin(value)` shows a binary representation and `int(text, 2)` parses binary text.

    Bitwise `&` keeps positions set in both operands. Bitwise `|` combines positions set in either. These operate on bits and differ from logical `and` and `or`, which choose values based on truthiness.

    To require several permissions, check that every required bit appears in the granted flags: the intersection must equal the required mask. Requiring no flags is always satisfied. This is a simplified representation exercise, not a complete authorization system. Pip requested administrator access to the toaster. We granted the crumb tray read-only permissions.''',
    'READ, WRITE = 0b01, 0b10\ngranted = READ | WRITE\nprint(granted & READ == READ)  # True',
    'Implement has_flags(granted, required). Inputs are non-negative integers. Return a bool indicating whether all bits in required are present in granted. A zero requirement is satisfied.',
    'def has_flags(granted, required):\n    raise NotImplementedError("Inspect the permission switches")',
    'def has_flags(granted, required):\n    return (granted & required) == required',
    [('single','self.assertTrue(has_flags(0b101, 0b001))\nself.assertFalse(has_flags(0b101, 0b010))'),('all_required','self.assertFalse(has_flags(0b001, 0b011))\nself.assertTrue(has_flags(0b111, 0b011))'),('empty_requirement','self.assertIs(has_flags(0, 0), True)\nself.assertIs(has_flags(12, 0), True)')],
    'Compare the bitwise intersection with the entire required mask.',
    'Why would bool(granted & required) accept only one of two required permissions?')

add('The decimal that would not behave', 'Use tolerances for floating-point comparisons.',
    '''Most decimal fractions cannot be represented exactly by a finite binary floating-point number. Operations use nearby representable values, so `0.1 + 0.2 == 0.3` is false. This is a representation issue, not Python being bored with arithmetic.

    A useful comparison may allow a small difference. `abs(actual - expected) <= tolerance` is an absolute-tolerance rule. `math.isclose` also supports relative tolerance, which scales with magnitude. Choose the rule from the domain; a tolerance suitable for a sensor reading may be unsuitable for money.

    Rounding for display does not repair every numerical algorithm. For exact cents, integers are often simpler; for decimal business arithmetic, the standard library's Decimal can be appropriate. This mission uses finite floats and an explicitly supplied non-negative tolerance. Pip reports the kettle temperature as 'approximately soup'. We need a number.''',
    'difference = abs((0.1 + 0.2) - 0.3)\nclose = difference <= 1e-9\n# True, although exact equality is False',
    'Return whether two finite numbers differ by at most tolerance. tolerance is a non-negative number. Use an absolute tolerance only; exact equality must still work when tolerance is zero.',
    'def approximately_equal(actual, expected, tolerance=1e-9):\n    raise NotImplementedError("Negotiate with floating point")',
    'def approximately_equal(actual, expected, tolerance=1e-9):\n    return abs(actual - expected) <= tolerance',
    [('representation','self.assertTrue(approximately_equal(0.1 + 0.2, 0.3))'),('outside','self.assertFalse(approximately_equal(10.2, 10.0, 0.1))'),('absolute_and_exact','self.assertTrue(approximately_equal(-5, -5, 0))\nself.assertFalse(approximately_equal(1000001, 1000000, 0.1))')],
    'Take the absolute difference and compare it with tolerance using <=.',
    'Why would a relative tolerance behave differently for very large values?')

add('The door has three rules', 'Combine comparisons with and, or and not.',
    '''Comparisons produce boolean results. `==` checks equality, `!=` checks inequality, and ordering operators compare size or position. Logical `and` requires both conditions, `or` accepts either, and `not` reverses a truth value.

    Translate a sentence into small rules before combining it. Parentheses make mixed logic easier to read even when precedence would produce the same result. A banned user should not sneak through because an `or` condition was grouped incorrectly.

    Python's logical operators can return operands instead of literal booleans. When your contract promises a bool, a comparison or an explicit `bool(...)` conversion makes the intent clear. Identity `is` answers whether two references point to the same object; use equality `==` to compare text values. Pip's access policy was 'looks friendly'. The security team has requested actual conditions.''',
    'allowed = (has_ticket or is_staff) and not is_banned',
    'Implement may_enter(has_ticket, is_staff, is_banned), accepting booleans. A visitor needs a ticket or staff status, and must not be banned. Return a bool.',
    'def may_enter(has_ticket, is_staff, is_banned):\n    raise NotImplementedError("Replace the vibes-based door policy")',
    'def may_enter(has_ticket, is_staff, is_banned):\n    return (has_ticket or is_staff) and not is_banned',
    [('ticket_or_staff','self.assertTrue(may_enter(True, False, False))\nself.assertTrue(may_enter(False, True, False))'),('ban_wins','self.assertFalse(may_enter(True, True, True))\nself.assertFalse(may_enter(False, True, True))'),('no_credentials','self.assertFalse(may_enter(False, False, False))')],
    'Group the two ways to qualify, then apply the ban to that whole group.',
    'Which case would expose a mistaken expression has_ticket or is_staff and not is_banned?')

add('Choose one response', 'Order if/elif/else branches so specific rules are reachable.',
    '''An `if` branch runs only when its condition is truthy. `elif` tries another condition if earlier branches did not match, and `else` handles the remaining case. Only one branch in this chain runs. Indentation defines which instructions belong to each branch.

    Branch order matters when conditions overlap. A general condition placed first can swallow a more specific case. Write the priority rule in words, then test overlaps deliberately. Independent `if` statements mean something different: several bodies can run.

    An early return can make a guard clause clear, especially for invalid or exceptional states. It also means later code is skipped. Keep your decision table small enough to reason about and use exact status values rather than guessing from substrings. Pip would like every server response to be 'probably fine'. The monitoring team has declined.''',
    'if status >= 500:\n    label = "server error"\nelif status >= 400:\n    label = "client error"\nelse:\n    label = "other"',
    'Classify an integer HTTP-like status from 100 through 599: 500+ -> "server", 400+ -> "client", 300+ -> "redirect", 200+ -> "success", otherwise "info". Inputs are within that range.',
    'def status_family(status):\n    raise NotImplementedError("Give monitoring something useful")',
    'def status_family(status):\n    if status >= 500:\n        return "server"\n    elif status >= 400:\n        return "client"\n    elif status >= 300:\n        return "redirect"\n    elif status >= 200:\n        return "success"\n    return "info"',
    [('families','for code, expected in [(101,"info"),(204,"success"),(302,"redirect"),(404,"client"),(503,"server")]:\n    self.assertEqual(status_family(code), expected)'),('boundaries','for code, expected in [(199,"info"),(200,"success"),(399,"redirect"),(400,"client"),(500,"server")]:\n    self.assertEqual(status_family(code), expected)'),('high','self.assertEqual(status_family(599), "server")')],
    'Check the highest threshold first so lower thresholds do not catch it.',
    'Why would checking status >= 200 first misclassify a 503?')

add('Look before you index', 'Use short-circuit evaluation to guard an operation.',
    '''Python evaluates logical `and` from left to right and stops as soon as a falsy operand decides the result. With `or`, it stops at the first truthy operand. This is short-circuit evaluation, and it can prevent unsafe work rather than merely save time.

    For a possibly missing string, test its existence before calling a string method or indexing it. Reversing the order can produce an error before the guard is reached. An empty string has no first character; `None` has no string methods.

    Because logical operators return operands, `text and ...` can return the empty string or None. If the public contract promises a boolean, wrap the combined expression in `bool` or use clear branches. Pip installed a warning sign after the trapdoor. Your guard must come before the risky operation.''',
    'has_letter = bool(text and text[0].isalpha())\n# The index operation is skipped for empty text.',
    'Return a bool indicating whether text starts with "/". text is a string or None. None and the empty string return False. Guard before accessing the first character.',
    'def is_absolute_route(text):\n    raise NotImplementedError("Move the warning sign")',
    'def is_absolute_route(text):\n    return bool(text and text[0] == "/")',
    [('paths','self.assertIs(is_absolute_route("/jobs"), True)\nself.assertIs(is_absolute_route("jobs"), False)'),('empty','self.assertIs(is_absolute_route(""), False)'),('missing','self.assertIs(is_absolute_route(None), False)')],
    'Check text before text[0]; make the final result an actual bool.',
    'Why does text[0] == "/" and text fail for an empty string?')

add('Missing is not the same as empty', 'Distinguish truthiness from a precise missing-value test.',
    '''Empty containers, empty strings, zero, False and None are all falsy. That makes `if values:` convenient when you want to know whether a collection has members. It is too broad when your rule is specifically about absence.

    `value or fallback` chooses the fallback for every falsy value. If an empty label or numeric zero is a legitimate user choice, this silently overwrites it. `value is None` expresses the narrower rule. Use `is` for this singleton absence marker and `==` for ordinary value equality.

    Defaults belong in a documented contract, not in a guess about what the caller meant. Test an omitted value and each allowed empty value separately. Pip renamed an intentionally blank status to 'MYSTERY' because blank looked suspicious. It was a feature, briefly, until somebody noticed.''',
    'chosen = "default" if supplied is None else supplied\n# supplied == "" stays empty.',
    'Implement choose_label(supplied, fallback). Return fallback only when supplied is None. Otherwise return supplied unchanged, even if it is "", 0, False, or an empty list.',
    'def choose_label(supplied, fallback):\n    raise NotImplementedError("Respect the deliberate blank")',
    'def choose_label(supplied, fallback):\n    return fallback if supplied is None else supplied',
    [('missing','self.assertEqual(choose_label(None, "default"), "default")'),('falsy_values','for value in ["", 0, False, []]:\n    self.assertIs(choose_label(value, "default"), value)'),('ordinary','self.assertEqual(choose_label("ready", "default"), "ready")')],
    'Use is None rather than not supplied or supplied or fallback.',
    'When would using truthiness be the correct rule instead?')

add('Repeat responsibly', 'Use range and an accumulator with correct inclusive bounds.',
    '''A `for` loop takes one value at a time from an iterable. `range(stop)` generates integers from zero up to, but excluding, stop. `range(start, stop)` lets you choose the beginning. The exclusive stop is a common source of off-by-one bugs.

    An accumulator stores a partial result. Initialize it before the loop, update it inside, and return it after all iterations. Initializing inside the loop throws away earlier work; returning inside the loop stops after the first item.

    Empty iteration is a real case, not an error. Choose an initial value that already represents the empty result, such as zero for a sum or an empty list for collected values. Pip was told to repeat a task five times and counted zero through five. The team appreciates the enthusiasm, but the invoice does not.''',
    'total = 0\nfor number in range(1, 4):\n    total += number\n# 1 + 2 + 3 == 6',
    'Return the sum of integers from 1 through n, inclusive. n is a non-negative integer. Use a loop for practice; n=0 returns 0.',
    'def sum_through(n):\n    raise NotImplementedError("Count the repeats")',
    'def sum_through(n):\n    total = 0\n    for number in range(1, n + 1):\n        total += number\n    return total',
    [('normal','self.assertEqual(sum_through(5), 15)'),('empty_and_one','self.assertEqual(sum_through(0), 0)\nself.assertEqual(sum_through(1), 1)'),('larger','self.assertEqual(sum_through(100), 5050)')],
    'range excludes its stop, so the stop must be n + 1.',
    'What result would you get if return were indented inside the loop?')

add('While the queue is still awake', 'Maintain a while-loop invariant and guarantee progress.',
    '''A `while` loop repeats while its condition is truthy. Unlike a for loop over a fixed range, it needs you to update the state that eventually makes the condition false. If no progress occurs, the loop may run forever.

    State an invariant: a fact that remains true before and after each iteration. Here remaining work never becomes negative, and processed work plus remaining work always equals the starting workload. Each iteration removes at most the capacity of one batch.

    Check termination before coding: for positive capacity, each iteration reduces positive remaining work. Zero workload therefore runs the body zero times. The runner can stop a hung program, but the goal is to understand why termination follows from your rule. Pip's retry loop had no stop condition. It is still optimistic about a printer disconnected in 2019.''',
    'remaining = 8\nbatches = 0\nwhile remaining > 0:\n    remaining = max(0, remaining - 3)\n    batches += 1\n# batches is 3',
    'Implement drain_batches(work, capacity). Return (batch_count, remaining). work >= 0 and capacity > 0 are integers. Each batch handles up to capacity; stop when no work remains. Use a while loop to practice state updates.',
    'def drain_batches(work, capacity):\n    raise NotImplementedError("Help the queue go to sleep")',
    'def drain_batches(work, capacity):\n    remaining = work\n    batches = 0\n    while remaining > 0:\n        remaining = max(0, remaining - capacity)\n        batches += 1\n    return batches, remaining',
    [('partial','self.assertEqual(drain_batches(8, 3), (3, 0))'),('empty','self.assertEqual(drain_batches(0, 2), (0, 0))'),('exact','self.assertEqual(drain_batches(12, 4), (3, 0))')],
    'Make remaining smaller every iteration, and count a batch only when work exists.',
    'What would happen if capacity were zero and we did not validate it?')

add('Skip the nonsense, stop at success', 'Use continue and break without skipping valid falsy results.',
    '''`continue` skips the rest of the current loop iteration and moves to the next item. `break` exits the loop entirely. They express different decisions: 'ignore this candidate' and 'we have found enough'.

    A return inside a function can also end a search immediately by returning its result. If no item qualifies, return a clear sentinel after the loop. Do not confuse a qualifying value of zero with no result; absence is represented by None in this contract.

    Search order belongs in the requirements. The first qualifying item is not necessarily the smallest one, and sorting to find a minimum can silently change the requested answer. Avoid mutating the input just to inspect it. Pip's search strategy was to stop at the first number because every number deserves encouragement. Some numbers still fail the requirement.''',
    'for number in [-2, 7, 8, 10]:\n    if number < 0:\n        continue\n    if number % 2 == 0:\n        found = number\n        break\n# found is 8, not 10',
    'Return the first non-negative even integer in values, preserving input order. Return None if none qualifies. Zero qualifies. Do not mutate values.',
    'def first_even_job(values):\n    raise NotImplementedError("Find a suitable job")',
    'def first_even_job(values):\n    for value in values:\n        if value < 0:\n            continue\n        if value % 2 == 0:\n            return value\n    return None',
    [('first_not_smallest','self.assertEqual(first_even_job([-2, 9, 8, 2]), 8)'),('zero','self.assertEqual(first_even_job([3, 0, 4]), 0)'),('none','self.assertIsNone(first_even_job([]))\nself.assertIsNone(first_even_job([-4, 1, 3]))'),('preserved','values = [7, 4, 2]\nfirst_even_job(values)\nself.assertEqual(values, [7, 4, 2])')],
    'Skip negatives, then return on the first even value. Put return None after the loop.',
    'Why would if found: misinterpret a successful result of zero?')

add('Nested loops, tiny city', 'Traverse a grid in a defined order using nested iteration.',
    '''A nested loop runs an inner iteration for each outer value. With rows outside and columns inside, the traversal visits every column in the first row before moving to the next row. Reversing the loops changes order even if it visits the same coordinate pairs.

    Nested iteration can multiply work: rows times columns visits, rather than rows plus columns. For a small grid that is expected. For large datasets, understand the cost before nesting searches thoughtlessly. `enumerate(sequence)` is useful when you need both a position and a value, and `zip` pairs values from separate sequences until the shorter ends.

    Coordinates are pairs, naturally represented by tuples. Accumulate them in a list when order matters. An empty dimension means there are no cells. Pip drew a server room map with columns first and forgot to tell anyone. Three engineers are now in the stationery cupboard.''',
    'cells = []\nfor row in range(2):\n    for column in range(3):\n        cells.append((row, column))',
    'Return every (row, column) coordinate for a grid of rows by columns, in row-major order. Dimensions are non-negative integers. Either zero dimension returns an empty list.',
    'def grid_cells(rows, columns):\n    raise NotImplementedError("Map the tiny server room")',
    'def grid_cells(rows, columns):\n    result = []\n    for row in range(rows):\n        for column in range(columns):\n            result.append((row, column))\n    return result',
    [('order','self.assertEqual(grid_cells(2, 2), [(0,0),(0,1),(1,0),(1,1)])'),('empty','self.assertEqual(grid_cells(0, 3), [])\nself.assertEqual(grid_cells(2, 0), [])'),('rectangle','self.assertEqual(grid_cells(1, 3), [(0,0),(0,1),(0,2)])')],
    'Put the row loop outside and the column loop inside.',
    'How many iterations does a 100 by 100 grid require?')

# Chapters 9-12: ordered sequences, mappings, sets and exceptions.
add('First, last, and absolutely not there', 'Index sequences safely, including negative indexes.',
    '''A list stores values in an order. Index zero selects the first element; index `-1` selects the last. The last positive index is `len(values) - 1`. Indexing an empty list, or going beyond either end, raises `IndexError`.

    A tuple also has an order, but its elements cannot be reassigned. Use a tuple for a small fixed grouping and a list for a collection you may extend. Both support indexing and length. A tuple containing a list is not deeply immutable: the nested list can still change.

    Check the empty case before indexing when emptiness is allowed. Do not catch every exception just to hide a missing guard. This contract asks for the endpoints, not a sorted minimum and maximum. Pip rearranged a queue alphabetically to discover its first person. The queue has lodged a complaint.''',
    'jobs = ["backup", "email", "report"]\nfirst = jobs[0]\nlast = jobs[-1]\n# backup, report',
    'Return (first, last) from an input list or tuple. Return None for an empty sequence. A one-element sequence returns that element twice. Preserve the original order and input.',
    'def endpoints(values):\n    raise NotImplementedError("Find the actual ends")',
    'def endpoints(values):\n    if not values:\n        return None\n    return values[0], values[-1]',
    [('normal','self.assertEqual(endpoints([8, 2, 5]), (8, 5))'),('empty_single','self.assertIsNone(endpoints([]))\nself.assertEqual(endpoints([0]), (0, 0))'),('tuple_preserved','values = ("b", "a")\nself.assertEqual(endpoints(values), ("b", "a"))\nself.assertEqual(values, ("b", "a"))')],
    'Handle emptiness first, then use indexes 0 and -1.',
    'Why is the last item not necessarily the largest item?')

add('Slices without paper cuts', 'Use start:stop:step and understand exclusive bounds.',
    '''A slice selects a sequence region: `values[start:stop:step]`. The stop is excluded. Omitted start and stop use the relevant ends; a negative step walks backward. Unlike direct indexing, an out-of-range slice normally clips to the available region rather than raising IndexError.

    A list slice creates a new outer list. Nested mutable objects are still shared, just as with a shallow copy. A slice also preserves order unless a negative step reverses traversal. Think through the endpoints with a tiny example before trusting an elaborate expression.

    A zero step is invalid. Here the inputs do not require one; focus on finding a tail without the `-0` trap. `values[-0:]` means `values[0:]`, which returns everything. Pip asked for the last zero incidents and received the entire incident history. A tense meeting followed.''',
    'values = [10, 20, 30, 40]\nprint(values[1:3])  # [20, 30]\nprint(values[::-1])  # [40, 30, 20, 10]',
    'Return a new list containing the last count items in their original order. count is a non-negative integer. count=0 returns []; a count exceeding the list length returns a shallow copy of the full list. Do not mutate the input.',
    'def recent_items(values, count):\n    raise NotImplementedError("Defuse the minus-zero trap")',
    'def recent_items(values, count):\n    return list(values[-count:]) if count else []',
    [('tail','self.assertEqual(recent_items([1,2,3,4], 2), [3,4])'),('zero','self.assertEqual(recent_items([1,2], 0), [])'),('oversize_copy','values = [1,2]\nresult = recent_items(values, 9)\nself.assertEqual(result, [1,2])\nself.assertIsNot(result, values)\nself.assertEqual(values, [1,2])')],
    'Handle count == 0 separately before using a negative start index.',
    'Why does values[-0:] not mean an empty tail?')

add('A queue, with manners', 'Use list append and pop while understanding mutation.',
    '''`append(value)` adds one item at the end of a list. `pop(index)` removes and returns an item; omitting the index removes the last item. These methods mutate the list, and append returns None rather than the updated list.

    A first-in, first-out queue takes the oldest item first. For a short learning example, `pop(0)` expresses that behavior, but removing the first element of a long list shifts the remaining elements. `collections.deque` supports efficient removal from the left for real queue workloads.

    Decide whether your operation owns the input. Here the caller retains its list, so build a shallow copy before changing it. Return both the served item and the remaining collection so state changes are explicit. Pip's queue served the last arrival first because they brought biscuits. The specification remains unmoved.''',
    'waiting = ["a", "b"]\ncopy = list(waiting)\nserved = copy.pop(0)\n# served == "a"; waiting is unchanged',
    'Implement serve_next(waiting). Return (oldest_item, remaining_list), leaving waiting unchanged. For an empty input return (None, []). The returned list must be a different object.',
    'def serve_next(waiting):\n    raise NotImplementedError("Biscuits do not change FIFO")',
    'def serve_next(waiting):\n    remaining = list(waiting)\n    if not remaining:\n        return None, remaining\n    return remaining.pop(0), remaining',
    [('fifo','self.assertEqual(serve_next(["a","b","c"]), ("a", ["b","c"]))'),('empty','self.assertEqual(serve_next([]), (None, []))'),('no_mutation','waiting = [0,1]\nserved, remaining = serve_next(waiting)\nself.assertEqual(served, 0)\nself.assertEqual(waiting, [0,1])\nself.assertIsNot(waiting, remaining)')],
    'Copy before using pop(0), and guard an empty list.',
    'Why would return waiting.append(item) produce None?')

add('Comprehend the work order', 'Transform and filter a sequence with enumerate and comprehensions.',
    '''A list comprehension combines iteration, an output expression and an optional filter: `[expression for item in items if condition]`. It builds a new list. Read it as 'produce this expression for each item that passes this condition'. Prefer an ordinary loop when a comprehension becomes difficult to explain.

    `enumerate(items, start=1)` supplies a counter alongside each value, which avoids manually keeping an index in sync. Filtering after enumeration preserves the original positions; numbering after filtering would have a different meaning.

    `zip(left, right)` pairs corresponding items and normally stops at the shorter input. When equal lengths are required, `zip(..., strict=True)` can expose a mismatch. Choose these tools because their behavior fits the contract, not because shorter code earns extra points. Pip submitted a one-line expression nobody could read. It has been framed as a warning.''',
    'labels = [f"{position}: {name}"\n          for position, name in enumerate(["A", "", "B"], 1)\n          if name]\n# ["1: A", "3: B"]',
    'Return `POSITION: NAME` labels for non-empty strings in names, numbered from one using their original positions. Do not strip names; a string containing a space is non-empty. Do not mutate names.',
    'def job_labels(names):\n    raise NotImplementedError("Make the clever code readable")',
    'def job_labels(names):\n    return [f"{position}: {name}" for position, name in enumerate(names, 1) if name]',
    [('positions','self.assertEqual(job_labels(["A", "", "B"]), ["1: A", "3: B"])'),('empty','self.assertEqual(job_labels([]), [])\nself.assertEqual(job_labels(["", ""]), [])'),('space_and_input','names = [" ", "Pip"]\nself.assertEqual(job_labels(names), ["1:  ", "2: Pip"])\nself.assertEqual(names, [" ", "Pip"])')],
    'Enumerate the original list before applying the non-empty filter.',
    'How would the output change if you filtered first and enumerated afterward?')

add('A dictionary is not a tiny list', 'Use keys, membership and get without confusing absence with None.',
    '''A dictionary maps keys to values. `mapping[key]` retrieves a value and raises KeyError when the key is missing. `mapping.get(key, default)` supplies a default instead. `key in mapping` tests keys, not values.

    Missing keys and present keys whose value is None are distinct states. `get` without a default cannot distinguish them by itself. If your rule treats a present None as meaningful, test membership before choosing a fallback. Keys must be hashable; immutable strings and integers are common choices, while mutable lists cannot be keys.

    Dictionaries preserve insertion order, but lookup is by key rather than a positional index. A numeric key is still a key, not a request for the nth item. Pip stored the Wi-Fi password under key 'somewhere'. It is technically a mapping; the naming review is ongoing.''',
    'settings = {"timeout": None}\nprint("timeout" in settings)  # True\nprint(settings.get("retries", 3))  # 3',
    'Return settings[key] if key exists, even when its value is None, False, or zero. Return fallback only when the key is absent. Leave settings unchanged.',
    'def configured_value(settings, key, fallback):\n    raise NotImplementedError("Find the actual key")',
    'def configured_value(settings, key, fallback):\n    return settings[key] if key in settings else fallback',
    [('present','self.assertEqual(configured_value({"x": 7}, "x", 9), 7)'),('meaningful_falsy','for value in [None, False, 0, ""]:\n    self.assertIs(configured_value({"x": value}, "x", 9), value)'),('missing','settings = {"x": 1}\nself.assertEqual(configured_value(settings, "y", 3), 3)\nself.assertEqual(settings, {"x": 1})')],
    'Use membership to distinguish a missing key from a stored None.',
    'Why would settings.get(key) or fallback violate this contract?')

add('Update the record, spare the original', 'Merge dictionaries and deliberately copy nested mutable data.',
    '''Assigning `record[key] = value` inserts or replaces one entry. `update(other)` applies entries from another mapping and mutates the target. `{**base, **changes}` creates a new dictionary in which later entries win. These are shallow operations.

    A patch is not the same as a replacement record. Fields absent from the patch normally remain, while present fields override even when their values are empty or None. Here we explicitly allow that override; another API might use None to mean deletion, but it would need to say so.

    Avoid changing caller-owned dictionaries while preparing a request. The input may be reused for a retry or comparison. Values nested inside the record remain shared unless the contract requests deeper copying. Pip updated a profile by deleting every unspecified field. The profile is now admirably minimalist and entirely unusable.''',
    'base = {"name": "Mira", "active": True}\nupdated = {**base, **{"active": False}}\n# base stays active; updated is inactive.',
    'Return a new dictionary combining base and changes, with changes winning duplicate keys. Keep both inputs unchanged. This is a shallow merge; a supplied None is a real replacement value.',
    'def patched_record(base, changes):\n    raise NotImplementedError("Apply a patch, not a disappearing act")',
    'def patched_record(base, changes):\n    return {**base, **changes}',
    [('override','self.assertEqual(patched_record({"x":1,"y":2}, {"x":3}), {"x":3,"y":2})'),('none','self.assertEqual(patched_record({"x":1}, {"x":None}), {"x":None})'),('new_and_preserved','base, changes = {"x":1}, {"y":2}\nresult = patched_record(base, changes)\nself.assertEqual(base, {"x":1})\nself.assertEqual(changes, {"y":2})\nself.assertIsNot(result, base)\nself.assertIsNot(result, changes)')],
    'Create a new mapping, then apply changes after base.',
    'Would a shallow merge make a nested list independent?')

add('Sort the tickets into departments', 'Group records with dict.items, setdefault and fresh lists.',
    '''Grouping changes a flat collection into a mapping from group names to lists of members. Initialize a group only when you first encounter its key, then append each member. `setdefault(key, [])` can retrieve an existing list or install a new one for a missing key.

    Every group must have its own list. Reusing one list for all keys makes every department see everyone else's tickets. Preserve encounter order within each group when the contract requires it. Iterating `.items()` later provides both each group key and its value.

    Input records may be shared safely if the result only stores selected immutable values. If you return mutable records and later edit them, think again about ownership. This mission collects IDs, leaving the original records untouched. Pip created one department called 'miscellaneous' and assigned the entire company. It was efficient until payday.''',
    'groups = {}\nfor team, job in [("ops", 7), ("web", 8), ("ops", 9)]:\n    groups.setdefault(team, []).append(job)\n# {"ops": [7, 9], "web": [8]}',
    'Group tickets by their "team" string. Return a dictionary mapping each team to its ticket IDs in encounter order. Tickets contain "team" and "id"; repeated IDs remain. Empty input returns {}. Do not mutate tickets.',
    'def group_tickets(tickets):\n    raise NotImplementedError("Miscellaneous cannot be every department")',
    'def group_tickets(tickets):\n    groups = {}\n    for ticket in tickets:\n        groups.setdefault(ticket["team"], []).append(ticket["id"])\n    return groups',
    [('group_order','self.assertEqual(group_tickets([{ "team":"a","id":2},{"team":"b","id":9},{"team":"a","id":1}]), {"a":[2,1],"b":[9]})'),('empty_duplicates','self.assertEqual(group_tickets([]), {})\nself.assertEqual(group_tickets([{"team":"a","id":1}]*2), {"a":[1,1]})'),('no_mutation','tickets = [{"team":"ops","id":7}]\nself.assertEqual(group_tickets(tickets), {"ops":[7]})\nself.assertEqual(tickets, [{"team":"ops","id":7}])')],
    'Get a fresh list for each unseen team, then append that ticket\'s ID.',
    'What symptom would reveal that all groups accidentally share one list?')

add('Invert carefully, the last one wins', 'Build a dictionary transformation and specify collision behavior.',
    '''A dictionary comprehension builds a mapping from a key expression and a value expression. Iterating `.items()` gives each original pair. Reversing key and value can be useful for lookup, but the original values may not be unique.

    A dictionary can hold only one value per key. When multiple inputs produce the same new key, a later assignment replaces the earlier value. That is acceptable only when the contract deliberately chooses last-wins behavior. Otherwise you might reject duplicates or group several originals under one key.

    The values used as new keys must be hashable. This mission restricts them to strings, so the key constraint is clear. Keep the source unchanged and let input insertion order decide which collision wins. Pip promised a reversible mapping without checking uniqueness. The lost keys are filing a support ticket.''',
    'codes = {"first": "x", "second": "x"}\nreverse = {value: key for key, value in codes.items()}\n# {"x": "second"}',
    'Invert a string-to-string dictionary so each original value maps to its original key. On duplicate values, the last key in input iteration order wins. Return a new dict and preserve the input.',
    'def invert_labels(labels):\n    raise NotImplementedError("Choose a collision policy")',
    'def invert_labels(labels):\n    return {value: key for key, value in labels.items()}',
    [('unique','self.assertEqual(invert_labels({"a":"A","b":"B"}), {"A":"a","B":"b"})'),('collision','self.assertEqual(invert_labels({"old":"x","new":"x"}), {"x":"new"})'),('empty_preserved','self.assertEqual(invert_labels({}), {})\nlabels = {"a":"A"}\nresult = invert_labels(labels)\nself.assertEqual(labels, {"a":"A"})\nself.assertIsNot(result, labels)')],
    'Iterate labels.items() and swap the key/value positions in a new dictionary.',
    'What additional condition would make inversion fully reversible?')

add('One domain, one invitation', 'Use a set to collect unique normalized values.',
    '''A set stores unique hashable values. Adding an existing value leaves the set unchanged. `value in seen` expresses membership without making ordering promises. Create an empty set with `set()`; `{}` creates an empty dictionary.

    Normalization should happen before deduplication when values differing only by a permitted variation count as equivalent. Here domain names are case-insensitive for our simplified input, while local parts of addresses are irrelevant to the requested result.

    Sets deliberately discard duplicates and do not provide positional indexing. If you need a stable order, keep an additional list or sort the result according to an explicit rule. Do not rely on the order you happen to see during one run. Pip invited the same company seventeen times because the capital letters kept changing. Catering has requested a set.''',
    'domains = set()\nfor address in ["a@Example.org", "b@example.org"]:\n    domains.add(address.split("@", 1)[1].lower())\n# {"example.org"}',
    'Return a set of lowercased domains from addresses. Each input is valid text with exactly one @ and a non-empty domain; no whitespace cleaning is required. Preserve the input list.',
    'def invited_domains(addresses):\n    raise NotImplementedError("One buffet invitation per domain")',
    'def invited_domains(addresses):\n    return {address.split("@", 1)[1].lower() for address in addresses}',
    [('dedup','self.assertEqual(invited_domains(["a@Example.org","b@example.org","x@other.net"]), {"example.org","other.net"})'),('empty','self.assertEqual(invited_domains([]), set())'),('preserved','addresses = ["A@X.NET"]\nself.assertEqual(invited_domains(addresses), {"x.net"})\nself.assertEqual(addresses, ["A@X.NET"])')],
    'Extract the part after @, lowercase it, and collect it in a set.',
    'Why does deduplicating before normalizing miss some equivalents?')

add('Who is on both shifts?', 'Use union, intersection and difference for collection comparison.',
    '''Set union (`|`) includes values from either collection. Intersection (`&`) keeps values in both. Difference (`-`) keeps values in the left collection that are absent from the right. Difference is directional: `before - after` and `after - before` answer different questions.

    These operators create new sets rather than changing their operands. In-place forms such as `|=` can mutate a set, so choose intentionally. Convert an input list to a set when uniqueness is the desired meaning and duplicates should not count.

    Comparing snapshots is a common backend task: what was added, what disappeared, and what stayed? A precise result shape prevents a caller from mixing up the directions. Pip reports every roster change as 'someone is somewhere'. We are replacing that with three named categories.''',
    'before, after = {"a", "b"}, {"b", "c"}\nadded = after - before\nremoved = before - after\nstayed = before & after',
    'Return {"added": ..., "removed": ..., "stayed": ...} as sets comparing before and after iterables of string IDs. Ignore duplicate IDs; do not mutate input sets or lists.',
    'def roster_changes(before, after):\n    raise NotImplementedError("Someone is somewhere is not a report")',
    'def roster_changes(before, after):\n    old, new = set(before), set(after)\n    return {"added": new-old, "removed": old-new, "stayed": old & new}',
    [('directions','self.assertEqual(roster_changes(["a","b"],["b","c"]), {"added":{"c"},"removed":{"a"},"stayed":{"b"}})'),('duplicates_empty','self.assertEqual(roster_changes([], ["x","x"]), {"added":{"x"},"removed":set(),"stayed":set()})'),('no_mutation','old, new = {"a"}, {"b"}\nroster_changes(old, new)\nself.assertEqual(old, {"a"})\nself.assertEqual(new, {"b"})')],
    'Added is after minus before; removed is the opposite difference.',
    'Which operation would give every person appearing in either roster?')

add('All permissions, not merely one', 'Check subset and disjointness relationships.',
    '''A set is a subset of another if every one of its members appears in the other set. `required <= granted` is a subset test; it is unrelated to lexicographic ordering. Equality is allowed in a non-strict subset test, while `<` requires a proper subset.

    Two sets are disjoint if they have no members in common. `isdisjoint` expresses this directly. Combining subset and disjointness checks is useful when a request has both required and forbidden features.

    Empty requirements are satisfied because there is no unmet member. A non-empty forbidden intersection must reject the request even when all required permissions are present. This is a small logic exercise, not a full security design. Pip has both 'read reports' and 'operate confetti cannon'. Only one belongs on the payroll service.''',
    'required = {"read", "write"}\ngranted = {"read", "write", "audit"}\nprint(required <= granted)  # True',
    'Return True only if every required permission is granted and none of the forbidden permissions is granted. All inputs are iterables of strings; duplicates do not matter. Return a bool.',
    'def permission_check(granted, required, forbidden):\n    raise NotImplementedError("Keep confetti out of payroll")',
    'def permission_check(granted, required, forbidden):\n    granted = set(granted)\n    return set(required) <= granted and granted.isdisjoint(forbidden)',
    [('required_all','self.assertTrue(permission_check(["r","w"],["r","w"],[]))\nself.assertFalse(permission_check(["r"],["r","w"],[]))'),('forbidden_wins','self.assertFalse(permission_check(["r","danger"],["r"],["danger"]))'),('empty','self.assertIs(permission_check([], [], []), True)')],
    'Combine a subset test with a no-overlap test.',
    'Why would a non-empty intersection with required prove too little?')

add('Merge the tag clouds', 'Accumulate unique values from nested collections without aliasing.',
    '''A set can be updated with values from any iterable. `update(values)` adds each element, while `add(value)` inserts the argument itself. Adding a list fails because lists are unhashable; updating from a list of strings adds its string members.

    Repeated updates build a union across many collections. Initialize a fresh accumulator inside the call so separate requests do not leak data. If inputs are sets, avoid using the first input as the accumulator unless mutation is explicitly allowed.

    Normalize values according to the contract and discard values only when a rule says to. This mission keeps exact tag spellings, including an empty string; it does not silently trim or lowercase. Pip keeps tidying people's labels without asking. One team's 'US' tag became 'us', which changed the meeting agenda considerably.''',
    'all_tags = set()\nfor tags in [["api", "sql"], ["sql", "go"]]:\n    all_tags.update(tags)\n# {"api", "sql", "go"}',
    'Return the union of all tag groups as a new set. Each group is an iterable of strings. Preserve exact spelling and every input; an empty outer input returns an empty set.',
    'def merged_tags(groups):\n    raise NotImplementedError("Do not tidy other teams\' labels")',
    'def merged_tags(groups):\n    result = set()\n    for group in groups:\n        result.update(group)\n    return result',
    [('union','self.assertEqual(merged_tags([["a","b"],["b","c"]]), {"a","b","c"})'),('exact_empty','self.assertEqual(merged_tags([]), set())\nself.assertEqual(merged_tags([["US","us",""]]), {"US","us",""})'),('no_alias','group = {"a"}\nresult = merged_tags([group, ["b"]])\nself.assertEqual(group, {"a"})\nself.assertIsNot(result, group)')],
    'Create set() inside the function and update it with each group.',
    'What is the difference between result.add(group) and result.update(group)?')

add('Reject nonsense at the boundary', 'Raise a specific exception for an invalid domain value.',
    '''An exception interrupts normal control flow and travels outward until matching handling is found. `raise ValueError("message")` reports that an argument has an unacceptable value. A useful message states the violated rule rather than blaming the caller.

    Validate before performing work that would produce an invalid result. Differentiate type errors from range errors when the contract requires it. In Python, bool is a subclass of int, so a naive integer check can accept True as one; explicit type rules matter at interfaces.

    A function should not silently clamp or guess unless that behavior is specified. Rejecting an invalid port is safer than turning it into a different port behind the caller's back. Exceptions are not failures of learning; they are part of expressing the contract. Pip's parser accepts 'roughly twelve'. The network stack does not.''',
    'def positive(value):\n    if value <= 0:\n        raise ValueError("value must be positive")\n    return value',
    'Implement validate_port(value). Accept an int from 1 through 65535 and return it. Reject bool and non-int inputs with TypeError. Reject out-of-range integers with ValueError. Include "port" in each error message.',
    'def validate_port(value):\n    raise NotImplementedError("Ports require actual numbers")',
    'def validate_port(value):\n    if type(value) is not int:\n        raise TypeError("port must be an integer")\n    if not 1 <= value <= 65535:\n        raise ValueError("port must be between 1 and 65535")\n    return value',
    [('valid_bounds','self.assertEqual(validate_port(1), 1)\nself.assertEqual(validate_port(65535), 65535)'),('wrong_types','for value in [True, False, "80", 80.0, None]:\n    with self.assertRaisesRegex(TypeError, "port"):\n        validate_port(value)'),('range','for value in [0, -1, 65536]:\n    with self.assertRaisesRegex(ValueError, "port"):\n        validate_port(value)')],
    'Check the type before comparing the range; bool needs rejection too.',
    'Why is isinstance(True, int) an important surprise for validation?')

add('Catch the error you expect', 'Handle selected conversion failures without masking unrelated bugs.',
    '''A `try` block contains work that may raise an exception. A matching `except` block handles a specific kind of failure; code after the handler can continue. Catching `Exception` around a large function may hide unrelated programming mistakes and make debugging harder.

    Put the smallest relevant operation in the try block. `int(text)` raises ValueError for malformed numeric text and TypeError for an unsuitable object such as None. This contract accepts strings or None, so both conversion errors have defined fallback behavior.

    Handling an error should leave a result with a clear meaning. A fallback of None signals that parsing failed; zero remains a successful value. In a user-facing API you might instead return structured error information. Pip used to catch every error and return 'all good'. Monitoring briefly became very cheerful and entirely wrong.''',
    'try:\n    value = int(raw)\nexcept (ValueError, TypeError):\n    value = None',
    'Return int(raw) for valid integer text, otherwise None. raw is a string or None. Valid text may have whitespace and a sign. Do not replace valid zero with None.',
    'def try_integer(raw):\n    raise NotImplementedError("All good is not an error strategy")',
    'def try_integer(raw):\n    try:\n        return int(raw)\n    except (ValueError, TypeError):\n        return None',
    [('valid','self.assertEqual(try_integer(" -12 "), -12)\nself.assertEqual(try_integer("0"), 0)'),('malformed','for raw in ["", "12.5", "twelve", "7x"]:\n    self.assertIsNone(try_integer(raw))'),('missing','self.assertIsNone(try_integer(None))')],
    'Catch ValueError and TypeError from int(raw), and return None only in that handler.',
    'What kind of bug could a broad except around a whole request handler conceal?')

add('Always put the mop away', 'Use finally for cleanup on success and failure.',
    '''A `finally` block runs when control leaves its try statement, including after a successful return or an exception. This makes it suitable for cleanup that must happen regardless of the operation's result. It does not mean you should catch and suppress the original exception.

    Keep cleanup small and reliable. A return or a new exception inside finally can replace the original result or error, which is often an unpleasant surprise. Context managers, introduced with `with`, package acquisition and cleanup into reusable operations; file objects already support them.

    This mission uses a supplied resource object so you can observe the protocol without opening a real connection. Call its work method, propagate its result or failure, and close exactly once. Pip washed the mop only on successful cleaning days. The cupboard has requested a finally clause.''',
    'try:\n    result = resource.read()\n    return result\nfinally:\n    resource.close()',
    'Implement use_resource(resource): call resource.read() once and return its result. Always call resource.close() once, even if read raises. Let the original read exception propagate. The close method itself will not raise.',
    'def use_resource(resource):\n    raise NotImplementedError("The mop must go away")',
    'def use_resource(resource):\n    try:\n        return resource.read()\n    finally:\n        resource.close()',
    [('success','resource = Mock()\nresource.read.return_value = "data"\nself.assertEqual(use_resource(resource), "data")\nresource.read.assert_called_once_with()\nresource.close.assert_called_once_with()'),('failure','resource = Mock()\nresource.read.side_effect = RuntimeError("offline")\nwith self.assertRaisesRegex(RuntimeError, "offline"):\n    use_resource(resource)\nresource.close.assert_called_once_with()'),('falsy_result','resource = Mock()\nresource.read.return_value = None\nself.assertIsNone(use_resource(resource))\nresource.close.assert_called_once_with()')],
    'Return from the try block and close in finally. Do not return from finally.',
    'How could a return statement inside finally accidentally hide an error?')

add('Give the error a useful name', 'Define and raise a custom exception while retaining ordinary validation.',
    '''A custom exception is a class that inherits from Exception or an appropriate existing exception type. It lets callers distinguish a domain problem from unrelated failures without parsing a message string. A descriptive message still helps the human reading a traceback.

    Exception type and message have different jobs. The type supports programmatic handling; the message describes this particular violation. Subclassing ValueError makes the error catchable either specifically or as a broader invalid-value problem.

    Do not catch your custom exception in the same function merely to return an ambiguous default. Let the caller decide how to recover. Here invalid amounts differ from insufficient funds, so tests expect two distinct errors. Pip named every exception Oops. It saved keystrokes and cost everyone else an afternoon.''',
    'class LimitExceeded(ValueError):\n    pass\n\ndef check(value, limit):\n    if value > limit:\n        raise LimitExceeded("limit exceeded")',
    'Keep InsufficientFunds as a ValueError subclass. Implement withdraw(balance, amount): reject a negative amount with ValueError; reject amount > balance with InsufficientFunds("insufficient funds"); otherwise return the new balance. Inputs are integers and balance is non-negative.',
    'class InsufficientFunds(ValueError):\n    pass\n\ndef withdraw(balance, amount):\n    raise NotImplementedError("Oops needs a better name")',
    'class InsufficientFunds(ValueError):\n    pass\n\ndef withdraw(balance, amount):\n    if amount < 0:\n        raise ValueError("amount must be non-negative")\n    if amount > balance:\n        raise InsufficientFunds("insufficient funds")\n    return balance - amount',
    [('valid','self.assertEqual(withdraw(10, 10), 0)\nself.assertEqual(withdraw(10, 0), 10)'),('insufficient','self.assertTrue(issubclass(InsufficientFunds, ValueError))\nwith self.assertRaisesRegex(InsufficientFunds, "insufficient funds"):\n    withdraw(3, 4)'),('negative','with self.assertRaises(ValueError) as caught:\n    withdraw(10, -1)\nself.assertNotIsInstance(caught.exception, InsufficientFunds)')],
    'Check negative amount first, then insufficient funds, then return the subtraction.',
    'Why should a caller catch InsufficientFunds instead of searching an error message for words?')

# Chapters 13-15: annotations, integration missions and checkpoints.
add('Type hints are signs, not force fields', 'Annotate a function while implementing its runtime contract.',
    '''Annotations describe the intended types of inputs and outputs: `def size(text: str) -> int`. Editors and static checkers can use them to catch mismatches before a program runs. Python itself does not enforce these annotations during an ordinary function call.

    A collection hint such as `list[int]` describes both the container and its members. An empty list is still compatible with that hint. Write annotations to communicate the interface, and use explicit validation when the runtime boundary needs it.

    Do not confuse a float return annotation with conversion: returning an int does not automatically turn it into a float. This exercise asks for a consistent result type, including the empty case. Pip installed a 'no bugs' sign on the server. It has had roughly the same enforcement power as a type hint without a checker.''',
    'def half(value: int) -> float:\n    return value / 2\n\n# A checker helps, but half("oops") can still be attempted at runtime.',
    'Implement average(values: list[int]) -> float. Return the arithmetic mean, or 0.0 for an empty list. Keep both annotations and return a float. Inputs already contain valid integers.',
    'def average(values: list[int]) -> float:\n    raise NotImplementedError("The sign needs actual code behind it")',
    'def average(values: list[int]) -> float:\n    return sum(values) / len(values) if values else 0.0',
    [('mean','self.assertEqual(average([2, 5, 8]), 5.0)\nself.assertIsInstance(average([2]), float)'),('empty','self.assertEqual(average([]), 0.0)\nself.assertIsInstance(average([]), float)'),('annotations','hints = get_type_hints(average)\nself.assertEqual(hints["values"], list[int])\nself.assertIs(hints["return"], float)')],
    'Guard the empty case before dividing; / produces a float.',
    'Would an annotation prevent a caller passing a list of strings at runtime?')

add('Maybe there is no ticket', 'Describe an optional result with a union and preserve valid falsy IDs.',
    '''A type union permits more than one kind of value. `int | None` means an integer or the absence marker None. It does not mean zero should be treated as missing. Older code may spell the same idea as Optional[int].

    Callers need to narrow an optional value before using integer-only operations. A check like `if result is not None:` communicates that distinction to readers and static analysis tools. A truthiness check would incorrectly discard a valid zero ID.

    Type hints are especially useful at boundaries where a search may find nothing. They make the exceptional shape visible without forcing an exception for an expected empty result. They still need matching implementation and tests. Pip numbered the first ticket zero and then declared it nonexistent. The customer was less philosophical.''',
    'def first_value(values: list[int]) -> int | None:\n    return values[0] if values else None\n\nresult = first_value([0])\nif result is not None:\n    print(result)',
    'Implement first_ticket(ids: list[int]) -> int | None. Return the first ID, or None for empty input. Zero and negative IDs are valid in this simplified contract; do not change the input.',
    'def first_ticket(ids: list[int]) -> int | None:\n    raise NotImplementedError("Ticket zero still exists")',
    'def first_ticket(ids: list[int]) -> int | None:\n    return ids[0] if ids else None',
    [('present','self.assertEqual(first_ticket([0, 9]), 0)\nself.assertEqual(first_ticket([-1]), -1)'),('missing','self.assertIsNone(first_ticket([]))'),('annotations_input','ids = [8,2]\nself.assertEqual(first_ticket(ids), 8)\nself.assertEqual(ids, [8,2])\nhints = get_type_hints(first_ticket)\nself.assertEqual(hints["ids"], list[int])\nself.assertEqual(hints["return"], int | None)')],
    'Use sequence emptiness to choose a result; do not test the first ID\'s truthiness.',
    'How would a caller safely use the result in an arithmetic expression?')

add('Two input types, one honest boundary', 'Narrow union inputs and validate beyond annotations.',
    '''A parameter annotated `int | str` accepts two intended representations. The implementation must decide how each representation becomes the promised output. `isinstance` can narrow a branch, but remember that bool is an int subclass when validating identifiers.

    Type hints do not encode every business rule. A string annotation says nothing about whether the string is empty, contains only digits, or fits a numeric range. Those rules belong in runtime validation and documentation.

    Converting first and validating later can accidentally accept values you did not intend, such as a float truncated by int(). Preserve a clear boundary: reject unsupported types, parse supported text, then validate the parsed value. Pip's ID system accepts anything with 'number energy'. The database has no matching column type.''',
    'def nonnegative(value: int | str) -> int:\n    if isinstance(value, bool):\n        raise TypeError("bool is not an ID")\n    number = int(value)\n    if number < 0:\n        raise ValueError("negative ID")\n    return number',
    'Implement normalize_id(value: int | str) -> int. Accept non-negative integers or text parseable by int. Reject bool and all other types with TypeError; reject malformed text and negative results with ValueError. Keep annotations.',
    'def normalize_id(value: int | str) -> int:\n    raise NotImplementedError("Number energy is not a type")',
    'def normalize_id(value: int | str) -> int:\n    if isinstance(value, bool) or not isinstance(value, (int, str)):\n        raise TypeError("ID must be int or str")\n    result = int(value)\n    if result < 0:\n        raise ValueError("ID must be non-negative")\n    return result',
    [('accepted','self.assertEqual(normalize_id(" 12 "), 12)\nself.assertEqual(normalize_id(0), 0)'),('types','for value in [True, 1.2, None, []]:\n    with self.assertRaises(TypeError):\n        normalize_id(value)'),('values','for value in ["x", "", -1, "-3"]:\n    with self.assertRaises(ValueError):\n        normalize_id(value)'),('annotations','self.assertEqual(get_type_hints(normalize_id), {"value":int | str,"return":int})')],
    'Reject unsupported types first, convert next, then reject a negative result.',
    'Why is int(1.9) dangerous when the contract does not accept floats?')

add('A record with a declared shape', 'Use TypedDict as documentation while constructing a fresh record.',
    '''TypedDict describes expected dictionary keys and their value types for static analysis. At runtime its instances are ordinary dictionaries. It does not automatically validate an incoming JSON object or supply missing fields.

    Named fields are clearer than a long tuple when callers need to remember several meanings. A declaration like `class Ticket(TypedDict): id: int` helps tools and people understand the shape. You still construct the dictionary and perform any required validation yourself.

    Separate a trusted constructor from an untrusted parser when useful. This mission receives valid inputs and builds a known shape; an earlier validation exercise handles hostile values. Returning a fresh record prevents one caller's later edits from changing another call's result. Pip's schema was a sticky note saying 'dictionary probably'. We have upgraded the sticky note.''',
    'from typing import TypedDict\n\nclass User(TypedDict):\n    name: str\n    active: bool\n\ndef new_user(name: str) -> User:\n    return {"name": name, "active": True}',
    'Keep the Ticket TypedDict fields id:int, title:str, done:bool. Implement new_ticket(ticket_id:int, title:str) -> Ticket, returning exactly those fields with done=False. Inputs are valid; preserve title exactly.',
    'from typing import TypedDict\n\nclass Ticket(TypedDict):\n    id: int\n    title: str\n    done: bool\n\ndef new_ticket(ticket_id: int, title: str) -> Ticket:\n    raise NotImplementedError("Give the sticky note a schema")',
    'from typing import TypedDict\n\nclass Ticket(TypedDict):\n    id: int\n    title: str\n    done: bool\n\ndef new_ticket(ticket_id: int, title: str) -> Ticket:\n    return {"id": ticket_id, "title": title, "done": False}',
    [('shape','self.assertEqual(new_ticket(7,"Fix robot"), {"id":7,"title":"Fix robot","done":False})'),('exact_fresh','a, b = new_ticket(0," "), new_ticket(0," ")\nself.assertIsNot(a, b)\nself.assertEqual(a["title"], " ")\nself.assertIs(a["done"], False)'),('annotations','self.assertEqual(get_type_hints(Ticket), {"id":int,"title":str,"done":bool})\nself.assertIs(get_type_hints(new_ticket)["return"], Ticket)')],
    'Construct a new dict with the three declared keys; annotations do not build it for you.',
    'Why must a JSON request still be validated even if you annotate it as Ticket?')

add('Mission: the noisy incident report', 'Combine string normalization, counting and deterministic ordering.',
    '''Integration problems ask you to choose the tools rather than name one in advance. Break the contract into stages: tokenize the input, normalize each token, count occurrences, then produce a predictable output order. Each stage should have one clear meaning.

    `text.split()` separates on arbitrary whitespace and discards empty pieces. It differs from `split(" ")`, which treats literal spaces as separators and can retain empty pieces. Lowercasing can merge equivalent words. Punctuation remains unless the contract asks you to remove it.

    Sorting output makes a report reproducible even when dictionary insertion order depends on the input. Test the empty report and repeated mixed-case words. This is a small pure function you could later put behind a CLI or file-reading boundary. Pip wrote an incident report consisting entirely of 'ALERT alert Alert'. At least the word count is impressive.''',
    'counts = {}\nfor word in "Ping ping PONG".split():\n    key = word.lower()\n    counts[key] = counts.get(key, 0) + 1\n# {"ping": 2, "pong": 1}',
    'Return a list of (word, count) tuples sorted by word. Split text on whitespace and lowercase each token. Preserve punctuation as part of the token. Empty or whitespace-only text returns [].',
    'def word_report(text):\n    raise NotImplementedError("Count the alerts, not the panic")',
    'def word_report(text):\n    counts = {}\n    for word in text.split():\n        key = word.lower()\n        counts[key] = counts.get(key, 0) + 1\n    return sorted(counts.items())',
    [('normal','self.assertEqual(word_report("Ping ping PONG"), [("ping",2),("pong",1)])'),('whitespace','self.assertEqual(word_report("  A\\nB\\tA "), [("a",2),("b",1)])\nself.assertEqual(word_report("  "), [])'),('punctuation','self.assertEqual(word_report("Hi hi!"), [("hi",1),("hi!",1)])')],
    'Build a frequency dictionary, then sort its items.',
    'What should change in the contract before you start removing punctuation?')

add('Mission: reconcile the snack ledger', 'Aggregate records while keeping money in integer cents.',
    '''A ledger is a sequence of changes, not merely a current balance. Processing it means applying each signed amount to the correct account. A deposit is positive and a charge is negative in this simplified contract.

    Initialize an account the first time it appears, including when its first entry is zero. Do not drop an account just because its final balance is zero; its presence in the ledger is meaningful. Integer cents avoid binary decimal representation issues for these whole-cent calculations.

    Keep records unchanged so the same ledger can be reconciled again. This repeatability is valuable when debugging and retrying data pipelines. The output dictionary needs no extra ordering promise because callers look up balances by account key. Pip spent the entire snack budget on a subscription to more snack budgets. Accounting would like a deterministic function.''',
    'balances = {}\nfor account, cents in [("tea", 500), ("tea", -125)]:\n    balances[account] = balances.get(account, 0) + cents',
    'Input entries are dicts with account:str and cents:int. Return account balances as a dictionary, retaining every encountered account even if its balance is zero. Do not mutate entries.',
    'def reconcile(entries):\n    raise NotImplementedError("Audit the snack budget")',
    'def reconcile(entries):\n    balances = {}\n    for entry in entries:\n        name = entry["account"]\n        balances[name] = balances.get(name, 0) + entry["cents"]\n    return balances',
    [('mixed','self.assertEqual(reconcile([{"account":"tea","cents":500},{"account":"cake","cents":-100},{"account":"tea","cents":-125}]), {"tea":375,"cake":-100})'),('zero_account','self.assertEqual(reconcile([{"account":"a","cents":0}]), {"a":0})\nself.assertEqual(reconcile([]), {})'),('repeatable','entries = [{"account":"a","cents":3}]\nself.assertEqual(reconcile(entries), reconcile(entries))\nself.assertEqual(entries, [{"account":"a","cents":3}])')],
    'Use get(account, 0) before adding each signed amount.',
    'Why should a zero balance not automatically remove an account from this report?')

add('Mission: the polite rate limiter', 'Maintain per-key state and make one decision for every event.',
    '''A rate limiter makes admission decisions while tracking prior work. This mission simplifies time away: each call processes one batch with a fixed per-user limit. State is local to the batch and must reset for the next call.

    Distinguish attempted events from accepted events. Only an accepted event consumes an available slot. When a user has reached the limit, later attempts remain rejected. Emit one decision per input so positions still correspond to original requests.

    A dictionary gives each user an independent counter. Duplicated IDs are expected because one user may make several attempts. Zero limit rejects every event. Real distributed rate limiting needs a time model, shared storage and concurrency handling; this exercise isolates the decision logic. Pip's limiter rejected everyone equally. Fairness is not the only requirement.''',
    'used = {}\nallowed = []\nfor user in ["a", "b", "a"]:\n    count = used.get(user, 0)\n    allowed.append(count < 1)\n    if count < 1:\n        used[user] = count + 1',
    'Return a list of bools for users, accepting only the first limit events per distinct user in this batch. limit is a non-negative integer. Keep input order, do not mutate users, and reset counters for each function call.',
    'def admit_requests(users, limit):\n    raise NotImplementedError("Be polite, but count")',
    'def admit_requests(users, limit):\n    used = {}\n    decisions = []\n    for user in users:\n        count = used.get(user, 0)\n        allowed = count < limit\n        decisions.append(allowed)\n        if allowed:\n            used[user] = count + 1\n    return decisions',
    [('per_user','self.assertEqual(admit_requests(["a","b","a","a","b"],2), [True,True,True,False,True])'),('zero_empty','self.assertEqual(admit_requests(["a","b"],0), [False,False])\nself.assertEqual(admit_requests([],2), [])'),('reset','users = ["a","a"]\nself.assertEqual(admit_requests(users,1), [True,False])\nself.assertEqual(admit_requests(users,1), [True,False])\nself.assertEqual(users, ["a","a"])')],
    'Look up a user\'s count before each decision and increment only when accepted.',
    'What additional state would a time-window limiter need?')

add('Mission: the dependency inventory', 'Combine nested iteration, uniqueness and stable output.',
    '''A nested mapping can describe projects and the libraries each one uses. The same library may appear in several projects or even twice in one list. An inventory should count distinct projects using a library, not raw occurrences.

    Separate the local uniqueness rule from global aggregation. Convert one project's library list to a set, then increment each library once for that project. A library absent from every project should not appear in the result.

    This is a useful pattern for analytics: decide the unit you are counting before choosing an accumulator. Counting events, users and projects are different questions even if the input looks similar. Keep source data untouched so another report can use it. Pip announced that ten projects use a library after finding ten copies in one project. The executive chart was briefly very exciting.''',
    'usage = {}\nfor libraries in {"web": ["a", "a"], "api": ["a", "b"]}.values():\n    for library in set(libraries):\n        usage[library] = usage.get(library, 0) + 1',
    'Given a dict mapping project names to lists of library names, return a dict counting how many distinct projects use each library. Repeats within one project count once. Empty projects add no keys. Do not mutate input.',
    'def dependency_usage(projects):\n    raise NotImplementedError("Count projects, not enthusiasm")',
    'def dependency_usage(projects):\n    usage = {}\n    for libraries in projects.values():\n        for library in set(libraries):\n            usage[library] = usage.get(library, 0) + 1\n    return usage',
    [('per_project','self.assertEqual(dependency_usage({"web":["a","a"],"api":["a","b"]}), {"a":2,"b":1})'),('empty','self.assertEqual(dependency_usage({}), {})\nself.assertEqual(dependency_usage({"web":[]}), {})'),('preserve','projects = {"x":["b","a","b"]}\nself.assertEqual(dependency_usage(projects), {"a":1,"b":1})\nself.assertEqual(projects, {"x":["b","a","b"]})')],
    'Deduplicate each project\'s list before updating the usage dictionary.',
    'How would the answer differ if the requested metric were installation occurrences?')

add('Checkpoint: aliases under pressure', 'Apply copying rules to a nested update without a recipe.',
    '''Checkpoints combine familiar concepts with less scaffolding. Before coding, identify which objects the caller still owns, which containers need independent copies, and which values can safely remain shared. Draw arrows between names and objects if the references feel confusing.

    This update changes a nested list inside one record. A fresh outer dictionary is necessary but not sufficient; the selected list also needs to be independent. Other immutable fields can be preserved as they are.

    Empty input collections should still produce valid results. Avoid a mutable default or hidden global accumulator, or a later call can inherit earlier work. Explain why your result is independent before revealing the reference solution. Pip has offered to label every object 'mine'. Ownership in Python requires slightly more precision.''',
    'original = {"events": ["open"], "id": 4}\n# A safe transformation returns a new dict and a new events list.\n# Assigning a new name alone does not copy either container.',
    'Return a new audit record with event appended to its "events" list, keeping all other fields. Do not modify the input or reuse its events list. Events can repeat; missing keys need not be handled.',
    'def append_audit(record, event):\n    raise NotImplementedError("Draw the arrows before editing")',
    'def append_audit(record, event):\n    result = dict(record)\n    result["events"] = [*record["events"], event]\n    return result',
    [('content','self.assertEqual(append_audit({"id":2,"events":["a"]},"b"), {"id":2,"events":["a","b"]})'),('references','record = {"events":[]}\nresult = append_audit(record,"x")\nself.assertIsNot(result, record)\nself.assertIsNot(result["events"], record["events"])\nself.assertEqual(record, {"events":[]})'),('repeat','self.assertEqual(append_audit({"events":["x"]},"x")["events"], ["x","x"])')],
    'The objects you modify are the outer mapping and its events list. Both need new containers.',
    'Which nested objects could still be shared safely under this specific contract?')

add('Checkpoint: a suspicious fallback', 'Repair a truthiness bug and test explicit empty settings.',
    '''A code review can begin with a function that looks elegant and is subtly wrong. Compare the implementation against each word of the contract. A compact use of `or` often hides a policy decision about empty values.

    Here the caller distinguishes an omitted setting from an explicitly empty one. `None`, zero and an empty string are not interchangeable, even though each can be falsy. Membership in a dictionary distinguishes a missing key from an existing key, while an identity check distinguishes None from other values.

    Work through a small decision table before editing. A correct repair should preserve good behavior on ordinary inputs and change only the violated cases. Pip suggests fixing every problem with a default of twelve. The on-call schedule has vetoed this approach.''',
    'settings = {"delay": 0}\n# settings.get("delay") or 10 gives 10, losing the explicit zero.\n# A precise missing-value rule preserves zero.',
    'Fix get_timeout(settings, default=30). Use default when "timeout" is absent or its value is None. Otherwise return the stored value unchanged, including 0, False, and "". Preserve settings.',
    'def get_timeout(settings, default=30):\n    return settings.get("timeout") or default',
    'def get_timeout(settings, default=30):\n    value = settings.get("timeout")\n    return default if value is None else value',
    [('missing_none','self.assertEqual(get_timeout({}),30)\nself.assertEqual(get_timeout({"timeout":None},8),8)'),('falsy','for value in [0, False, ""]:\n    self.assertIs(get_timeout({"timeout":value}), value)'),('ordinary_preserved','settings = {"timeout":5}\nself.assertEqual(get_timeout(settings),5)\nself.assertEqual(settings,{"timeout":5})')],
    'The rule is absence or None, rather than every falsy value.',
    'Would this repair be correct if the contract treated a stored None as meaningful?')

add('Checkpoint: reshape the response', 'Select, filter and order records using several core tools.',
    '''Data shaping is a common boundary task: the storage record may contain more fields than a response should expose. Choose the fields deliberately instead of returning every input field by accident. This exercise constructs strings rather than a public API, but the habit transfers.

    Filtering and ordering are independent rules. First decide which records qualify, then ensure the output order matches the contract. Python's `sorted` returns a new list, while a list's `.sort()` mutates it and returns None. A `key` callback tells sorting which value to compare.

    Preserve zero IDs and empty titles unless the rule excludes them. Being thorough means testing these boundaries, not adding guesses about nicer behavior. Pip sorted by title length because longer titles seemed more senior. The product team has supplied a less creative ordering rule.''',
    'records = [{"id":2,"name":"B"},{"id":1,"name":"A"}]\nordered = sorted(records, key=lambda record: record["id"])\n# sorted creates a new list; it does not reorder records.',
    'Return "ID: TITLE" strings for tickets whose done field is False, sorted by numeric ID ascending. IDs are unique integers; titles are strings; done is bool. Do not mutate or reorder the input records.',
    'def open_ticket_lines(tickets):\n    raise NotImplementedError("Longer titles are not more senior")',
    'def open_ticket_lines(tickets):\n    ordered = sorted((ticket for ticket in tickets if not ticket["done"]), key=lambda ticket: ticket["id"])\n    return [f"{ticket[\'id\']}: {ticket[\'title\']}" for ticket in ordered]',
    [('filter_order','self.assertEqual(open_ticket_lines([{"id":3,"title":"C","done":False},{"id":1,"title":"A","done":False},{"id":2,"title":"B","done":True}]), ["1: A","3: C"])'),('zero_empty','self.assertEqual(open_ticket_lines([{"id":0,"title":"","done":False}]), ["0: "])\nself.assertEqual(open_ticket_lines([]), [])'),('preserve','tickets = [{"id":2,"title":"B","done":False},{"id":1,"title":"A","done":False}]\noriginal = deepcopy(tickets)\nopen_ticket_lines(tickets)\nself.assertEqual(tickets, original)')],
    'Filter first, sort using ticket["id"] as the key, then build the output strings.',
    'Why would tickets.sort(...) violate this function\'s contract?')

add('Boss mission: the tiny ticket engine', 'Process a command stream with explicit state transitions and errors.',
    '''A small command processor combines parsing, branching, state and validation. Define each command's effect before implementing the loop. The same command can be valid or invalid depending on the current state: closing a nonexistent ticket is different from closing an existing one.

    Fail clearly on invalid operations rather than silently creating surprising state. Work on a copy so even a later failure cannot partially alter caller-owned data. This is a simple form of transactional thinking, although it is not a database transaction.

    Break the problem into initialization, one-command handling and final output. Use readable branches; a clever nested expression is not a requirement. This checkpoint is designed to be harder than earlier drills. Ask the tutor for a hint about one failing case at a time. Pip is now managing tickets. The team has bravely left the building.''',
    '# State transition example:\n# {} --("add", 7)--> {7: False}\n# {7: False} --("close", 7)--> {7: True}\n# Closing a missing ID must report an error.',
    'Implement ticket_engine(initial, commands). Copy initial (ID -> done bool). Commands are (action, ID) tuples: "add" inserts False and rejects an existing ID; "close" sets True and rejects a missing ID. Unknown actions also raise ValueError. Return the new state. Never change initial, even on failure.',
    'def ticket_engine(initial, commands):\n    raise NotImplementedError("Pip has been given a clipboard")',
    'def ticket_engine(initial, commands):\n    state = dict(initial)\n    for action, ticket_id in commands:\n        if action == "add":\n            if ticket_id in state:\n                raise ValueError("ticket exists")\n            state[ticket_id] = False\n        elif action == "close":\n            if ticket_id not in state:\n                raise ValueError("ticket missing")\n            state[ticket_id] = True\n        else:\n            raise ValueError("unknown action")\n    return state',
    [('workflow','self.assertEqual(ticket_engine({},[("add",0),("add",2),("close",0)]), {0:True,2:False})'),('errors','for initial, commands in [({1:False},[("add",1)]),({},[("close",1)]),({},[("dance",1)])]:\n    with self.assertRaises(ValueError):\n        ticket_engine(initial,commands)'),('atomic_input','initial = {1:False}\nwith self.assertRaises(ValueError):\n    ticket_engine(initial,[("close",1),("dance",1)])\nself.assertEqual(initial,{1:False})\nself.assertIsNot(ticket_engine(initial,[]), initial)')],
    'Copy initial first. Handle add, close and unknown actions as separate branches.',
    'Why is copying before the command loop important when a later command fails?')

# Chapters 16-18 extend the beginner foundation into practical Python.
add('Objects that remember their own jobs', 'Create independent instances with attributes and methods.',
    '''A class describes objects that share behavior. Calling the class creates an instance. `__init__` initializes that instance, and `self` refers to it inside instance methods. Assigning `self.completed` stores state on this particular worker rather than in a shared module variable.

    A class attribute is shared through the class unless an instance overrides it. A mutable class-level list is therefore a dangerous default for per-worker history. Initialize each worker's history inside __init__ so independent workers stay independent.

    Methods are functions reached through an object; Python supplies the instance as self. Their contract should still say what they return and which state they change. Object-oriented design is useful when data and behavior have a clear shared responsibility. Pip created a Worker class whose only method was take_break. We have expanded the interface.''',
    'class Counter:\n    def __init__(self):\n        self.value = 0\n\n    def tick(self):\n        self.value += 1\n        return self.value',
    'Implement Worker(name). Store name and a fresh completed list. finish(job_id) appends the ID, allows duplicates, and returns the number completed so far. Workers must not share history.',
    'class Worker:\n    def __init__(self, name):\n        raise NotImplementedError("A break is not the whole job")\n\n    def finish(self, job_id):\n        raise NotImplementedError',
    'class Worker:\n    def __init__(self, name):\n        self.name = name\n        self.completed = []\n\n    def finish(self, job_id):\n        self.completed.append(job_id)\n        return len(self.completed)',
    [('state','worker = Worker("Pip")\nself.assertEqual(worker.name,"Pip")\nself.assertEqual(worker.finish(7),1)\nself.assertEqual(worker.finish(8),2)\nself.assertEqual(worker.completed,[7,8])'),('independent','a,b = Worker("A"),Worker("B")\na.finish(1)\nself.assertEqual(b.completed,[])\nself.assertIsNot(a.completed,b.completed)'),('duplicates','worker = Worker("A")\nworker.finish(0)\nself.assertEqual(worker.finish(0),2)\nself.assertEqual(worker.completed,[0,0])')],
    'Create self.completed = [] inside __init__, not at class scope.',
    'What changes if completed is defined once on the class instead?')

add('Protect the snack fund', 'Enforce an invariant through methods and a read-only property.',
    '''An invariant is a condition that should remain true for every valid object state. A wallet might require a non-negative balance. Validate both construction and later updates, or the object can enter an invalid state through one unguarded path.

    A property exposes a method as an attribute-like read. Without a setter, ordinary assignment to that property fails. Store the backing value under a separate name such as `_balance`. The underscore is a convention for internal use, not a security boundary against hostile Python code.

    Validate before modifying state so an exception leaves the previous valid value intact. Returning the new balance can make operations convenient while preserving the invariant. This is encapsulation: callers use a defined interface rather than reconstructing the object's rules. Pip has been placed in charge of snack funds, a decision the invariant will have to survive.''',
    'class Meter:\n    def __init__(self):\n        self._value = 0\n\n    @property\n    def value(self):\n        return self._value',
    'Implement Wallet(balance=0) with read-only balance property. Reject negative starting balance or negative deposits with ValueError. deposit(amount) adds a non-negative amount and returns the balance. Invalid deposits leave state unchanged. Inputs are integers.',
    'class Wallet:\n    def __init__(self, balance=0):\n        raise NotImplementedError("Protect the biscuits")\n\n    @property\n    def balance(self):\n        raise NotImplementedError\n\n    def deposit(self, amount):\n        raise NotImplementedError',
    'class Wallet:\n    def __init__(self, balance=0):\n        if balance < 0:\n            raise ValueError("negative balance")\n        self._balance = balance\n\n    @property\n    def balance(self):\n        return self._balance\n\n    def deposit(self, amount):\n        if amount < 0:\n            raise ValueError("negative deposit")\n        self._balance += amount\n        return self._balance',
    [('valid','wallet = Wallet(5)\nself.assertEqual(wallet.deposit(3),8)\nself.assertEqual(wallet.balance,8)\nself.assertEqual(wallet.deposit(0),8)'),('invariant','with self.assertRaises(ValueError):\n    Wallet(-1)\nwallet=Wallet(5)\nwith self.assertRaises(ValueError):\n    wallet.deposit(-2)\nself.assertEqual(wallet.balance,5)'),('read_only','wallet=Wallet()\nwith self.assertRaises(AttributeError):\n    wallet.balance=99\nself.assertEqual(wallet.balance,0)')],
    'Use _balance for storage and @property for the public read; validate before changing it.',
    'Why is a leading underscore a convention rather than a security mechanism?')

add('Inheritance, with a real reason', 'Override behavior and use super without duplicating initialization.',
    '''Inheritance lets a subclass reuse and specialize a base class. If a subclass does not override a method, attribute lookup can find the base implementation. An overridden method defines the specialized behavior for that subtype.

    `super()` gives access to inherited behavior in a way that cooperates with Python's method resolution order. Calling `super().__init__(...)` lets the base initialize its part of the object rather than duplicating those assignments in each subclass.

    Choose inheritance for an actual 'is a kind of' relationship whose behavior stays compatible with callers. A long hierarchy built only to avoid a few repeated lines can be harder to understand than composition. Here a priority job is still a job, and both expose cost(). Pip proposed that a sandwich inherit from a database because both can contain rows. The architecture review was brief.''',
    'class Job:\n    def __init__(self, units):\n        self.units = units\n    def cost(self):\n        return self.units\n\nclass DoubleJob(Job):\n    def cost(self):\n        return super().cost() * 2',
    'Implement Job(units) with cost() returning units. Implement PriorityJob(units, surcharge) inheriting Job, initializing the base, and overriding cost() to return base cost plus surcharge. Inputs are non-negative integers.',
    'class Job:\n    def __init__(self, units):\n        raise NotImplementedError("Model the actual relationship")\n    def cost(self):\n        raise NotImplementedError\n\nclass PriorityJob(Job):\n    def __init__(self, units, surcharge):\n        raise NotImplementedError\n    def cost(self):\n        raise NotImplementedError',
    'class Job:\n    def __init__(self, units):\n        self.units = units\n    def cost(self):\n        return self.units\n\nclass PriorityJob(Job):\n    def __init__(self, units, surcharge):\n        super().__init__(units)\n        self.surcharge = surcharge\n    def cost(self):\n        return super().cost() + self.surcharge',
    [('base','self.assertEqual(Job(7).cost(),7)'),('subtype','job=PriorityJob(7,3)\nself.assertIsInstance(job,Job)\nself.assertEqual(job.units,7)\nself.assertEqual(job.cost(),10)'),('zero','self.assertEqual(PriorityJob(0,0).cost(),0)\nself.assertEqual(Job(0).cost(),0)')],
    'Let the base initializer store units, then add surcharge as subclass state.',
    'When would an object containing a Job be clearer than an object inheriting Job?')

add('Compose the delivery crew', 'Use a dataclass for a record and inject a collaborator.',
    '''Composition means one object uses another object to do part of its work. Passing a collaborator into the constructor makes the dependency explicit and lets tests supply a harmless fake instead of making a real network call.

    A dataclass generates common record behavior, including initialization and equality, from annotated fields. `frozen=True` rejects ordinary field reassignment. It does not make every possible nested object deeply immutable, so choose field types deliberately.

    Separate the data record from the service responsible for sending it. The service should call the supplied transport rather than construct an invisible global dependency. This improves testability and makes later transport changes local. Pip hired a notification service that only notifies itself. We are introducing a collaborator and a written contract.''',
    'from dataclasses import dataclass\n\n@dataclass(frozen=True)\nclass Message:\n    recipient: str\n    text: str\n\n# A sender can accept any transport with a send method.',
    'Define frozen dataclass Notice(recipient:str, text:str). Implement Dispatcher(transport). deliver(notice) calls transport.send(notice.recipient, notice.text) once and returns that call\'s result. Let transport errors propagate.',
    'from dataclasses import dataclass\n\n@dataclass(frozen=True)\nclass Notice:\n    recipient: str\n    text: str\n\nclass Dispatcher:\n    def __init__(self, transport):\n        raise NotImplementedError("Notify someone other than yourself")\n    def deliver(self, notice):\n        raise NotImplementedError',
    'from dataclasses import dataclass\n\n@dataclass(frozen=True)\nclass Notice:\n    recipient: str\n    text: str\n\nclass Dispatcher:\n    def __init__(self, transport):\n        self.transport = transport\n    def deliver(self, notice):\n        return self.transport.send(notice.recipient, notice.text)',
    [('record','self.assertEqual(Notice("a","hi"), Notice("a","hi"))\nwith self.assertRaises(AttributeError):\n    Notice("a","hi").text="bye"'),('collaborator','transport=Mock()\ntransport.send.return_value="queued"\nself.assertEqual(Dispatcher(transport).deliver(Notice("a","hi")),"queued")\ntransport.send.assert_called_once_with("a","hi")'),('error','transport=Mock()\ntransport.send.side_effect=RuntimeError("offline")\nwith self.assertRaisesRegex(RuntimeError,"offline"):\n    Dispatcher(transport).deliver(Notice("a","hi"))')],
    'Store the supplied transport on self and delegate to its send method.',
    'Why is passing a fake transport better than sending a real message in a unit test?')

add('Pure functions, less cleanup', 'Transform records immutably and use sorted with a key.',
    '''A pure function computes a result from explicit inputs and leaves caller-owned state unchanged. Repeating the same call with the same values produces the same result. This makes many transformations easier to test and compose.

    Immutability is a design choice even when Python's objects are mutable. Construct new containers when the contract requests a transformation, and be conscious of nested references. `sorted` creates a new outer list but does not copy every record in it, so create fresh records as well when the caller needs independence.

    A small lambda can supply a sorting key, while a named helper is clearer for a more substantial rule. Neither option makes an impure operation pure by itself. Pip's cleanup strategy is now 'do not spill the state in the first place'. It is surprisingly sound.''',
    'ordered = sorted(records, key=lambda record: record["score"], reverse=True)\n# The list is new, but its records are still shared unless copied.',
    'Return new {"name", "score"} dictionaries for every input record, sorted by score descending then name ascending. Drop other fields. Leave the input list and its dictionaries unchanged. Names are strings; scores are integers.',
    'def leaderboard(records):\n    raise NotImplementedError("Do not spill the state")',
    'def leaderboard(records):\n    result = [{"name":record["name"], "score":record["score"]} for record in records]\n    return sorted(result, key=lambda record: (-record["score"], record["name"]))',
    [('ordering','self.assertEqual(leaderboard([{"name":"Z","score":2},{"name":"B","score":5},{"name":"A","score":5}]), [{"name":"A","score":5},{"name":"B","score":5},{"name":"Z","score":2}])'),('new_records','records=[{"name":"A","score":1,"secret":"x"}]\noriginal=deepcopy(records)\nresult=leaderboard(records)\nself.assertEqual(records,original)\nself.assertIsNot(result[0],records[0])\nself.assertNotIn("secret",result[0])'),('empty','self.assertEqual(leaderboard([]),[])')],
    'Use the sort key (-score, name) and construct selected fields in fresh dicts.',
    'Why is sorted(records) alone not enough to guarantee independent result records?')

add('Functions that take functions', 'Pass callbacks and apply a transformation pipeline in order.',
    '''Functions are values: you can store them in variables, put them in a list and pass them as arguments. A higher-order function takes a function or returns one. Call a callback when you need its result; merely referring to it does not execute it.

    A pipeline passes the result of one stage into the next. Stage order matters: multiplying then adding differs from adding then multiplying. An empty pipeline leaves its input unchanged, which is a useful identity behavior.

    `map` and `filter` are familiar higher-order tools, but a clear loop can express a pipeline without obscuring control flow. Let exceptions propagate unless the pipeline contract defines a recovery strategy; otherwise a failing stage should not produce a falsely successful result. Pip arranged the pipeline alphabetically. The mathematics declined to cooperate.''',
    'steps = [lambda n: n + 2, lambda n: n * 3]\nvalue = 4\nfor step in steps:\n    value = step(value)\n# (4 + 2) * 3 == 18',
    'Implement apply_pipeline(value, steps), calling each single-argument function in sequence and returning the final value. An empty steps list returns value unchanged. Propagate exceptions and do not modify the list of steps.',
    'def apply_pipeline(value, steps):\n    raise NotImplementedError("Order the pipeline by meaning")',
    'def apply_pipeline(value, steps):\n    result = value\n    for step in steps:\n        result = step(result)\n    return result',
    [('order','self.assertEqual(apply_pipeline(4,[lambda n:n+2,lambda n:n*3]),18)'),('identity','value=[]\nself.assertIs(apply_pipeline(value,[]),value)'),('calls_errors','first,second=Mock(return_value=5),Mock(return_value=9)\nsteps=[first,second]\nself.assertEqual(apply_pipeline(2,steps),9)\nfirst.assert_called_once_with(2)\nsecond.assert_called_once_with(5)\nself.assertEqual(len(steps),2)\nwith self.assertRaises(ZeroDivisionError):\n    apply_pipeline(1,[lambda n:n/0])')],
    'Start with value, then replace the running result with step(result) for each step.',
    'Why is passing a function name different from passing a call like function(value)?')

add('Recursion with an exit sign', 'Use a base case and reduce a nested problem on each call.',
    '''A recursive function calls itself on a smaller version of the problem. It needs a base case that returns without another recursive call, plus a step that makes progress toward that base case. Without either, it can recurse until Python's recursion limit is reached.

    Nested trees are a natural example because each child has the same shape as its parent. A flat loop is often simpler for flat data. Recursion uses call-stack space, so it is not a universal replacement for iteration, especially for extremely deep structures.

    Define the allowed input shape precisely. Here leaves are integers and branches are lists; there are no cyclic references. An empty branch contributes zero. Negative and zero leaves still count as values. Pip put an exit sign in every hallway except the one leading to itself. Your base case needs to do actual work.''',
    'def leaf_sum(node):\n    if isinstance(node, int):\n        return node\n    return sum(leaf_sum(child) for child in node)\n\n# leaf_sum([1, [2, 3]]) == 6',
    'Implement nested_sum(node). node is an integer or a possibly nested list with the same shape. Return the sum of integer leaves. Empty lists contribute zero. Inputs are finite, acyclic and reasonably shallow. Do not mutate them.',
    'def nested_sum(node):\n    raise NotImplementedError("Install a working exit sign")',
    'def nested_sum(node):\n    if isinstance(node, int):\n        return node\n    return sum(nested_sum(child) for child in node)',
    [('leaf','self.assertEqual(nested_sum(-3),-3)\nself.assertEqual(nested_sum(0),0)'),('nested','self.assertEqual(nested_sum([1,[2,[-3,4]],5]),9)'),('empty_preserved','node=[[],[0,[]],2]\noriginal=deepcopy(node)\nself.assertEqual(nested_sum(node),2)\nself.assertEqual(nested_sum([]),0)\nself.assertEqual(node,original)')],
    'Return an integer leaf directly; otherwise combine recursive results from its children.',
    'Why would a list containing itself violate this function\'s termination assumptions?')

add('Lazy work is sometimes good work', 'Yield values on demand and stop consuming when the caller stops.',
    '''A generator function contains `yield`. Calling it creates an iterator without running the entire body. Each request for a next value resumes execution until another yield or completion. This supports streaming data without building the full result in memory.

    Laziness also affects side effects: input values should not be consumed before the caller asks for output. A generator can skip several nonmatching values before yielding a match, but it should not eagerly read past that match.

    Iterators are usually one-shot. Once exhausted, they do not automatically restart. Lists are reusable collections; an iterator over a list tracks a particular traversal. Choose the interface according to the workload. Pip calls every unfinished task 'lazy evaluation'. This is the one lesson where the phrase might be justified.''',
    'def positives(values):\n    for value in values:\n        if value > 0:\n            yield value\n\nstream = positives(iter([-1, 3, 4]))\nnext(stream)  # 3; 4 has not been requested yet',
    'Implement even_stream(values) as a lazy iterator yielding even integers in original order. Do not pre-consume input or build a list. Negative even integers and zero qualify; input may be a one-shot iterator.',
    'def even_stream(values):\n    raise NotImplementedError("Be lazy in the useful way")',
    'def even_stream(values):\n    for value in values:\n        if value % 2 == 0:\n            yield value',
    [('values','self.assertEqual(list(even_stream(iter([-4,-1,0,3,6]))),[-4,0,6])'),('empty','self.assertEqual(list(even_stream(iter([]))),[])'),('lazy','consumed=[]\ndef source():\n    for value in [1,2,4]:\n        consumed.append(value)\n        yield value\nstream=even_stream(source())\nself.assertEqual(consumed,[])\nself.assertIs(iter(stream),stream)\nself.assertEqual(next(stream),2)\nself.assertEqual(consumed,[1,2])\nself.assertEqual(next(stream),4)')],
    'Loop over input and yield only matching values; avoid list(...).',
    'Why can a lazy iterator handle a very large stream better than a list comprehension?')

add('Files deserve a closing ceremony', 'Use pathlib, UTF-8 and context-managed file access.',
    '''A file connects your program to persistent bytes outside its normal variables. Text mode decodes those bytes using an encoding. Choose UTF-8 explicitly when your format expects it rather than relying on a machine-specific default. A `with` block closes the file when the block ends, including on an exception.

    `pathlib.Path` represents filesystem paths and supports methods such as open, read_text and write_text. Imports bring definitions from another module into your file; keep reusable functions at module scope and put optional command-line execution under `if __name__ == "__main__":` so importing does not start the app.

    In larger projects, split related responsibilities into modules and use a virtual environment for project dependencies (`python -m venv .venv`). This exercise uses only the standard library. Pip once left every log file open 'for emotional support'. The operating system imposed a less sentimental limit.''',
    'from pathlib import Path\n\nwith Path("notes.txt").open(encoding="utf-8") as handle:\n    text = handle.read()\n# handle is closed here, even if reading failed.',
    'Implement nonblank_lines(path). Read UTF-8 text and return stripped non-empty lines in original order. Do not change the file. Missing files must raise FileNotFoundError rather than looking like empty files.',
    'from pathlib import Path\n\ndef nonblank_lines(path):\n    raise NotImplementedError("Give the file a proper goodbye")',
    'from pathlib import Path\n\ndef nonblank_lines(path):\n    with Path(path).open(encoding="utf-8") as handle:\n        return [line.strip() for line in handle if line.strip()]',
    [('content','with TemporaryDirectory() as directory:\n    path=Path(directory)/"notes.txt"\n    path.write_text("  alpha  \\n\\n beta\\t\\n",encoding="utf-8")\n    original=path.read_bytes()\n    self.assertEqual(nonblank_lines(path),["alpha","beta"])\n    self.assertEqual(path.read_bytes(),original)'),('utf8_empty','with TemporaryDirectory() as directory:\n    path=Path(directory)/"notes.txt"\n    path.write_text("caf\\u00e9\\n",encoding="utf-8")\n    self.assertEqual(nonblank_lines(str(path)),["caf\\u00e9"])\n    path.write_text("  \\n",encoding="utf-8")\n    self.assertEqual(nonblank_lines(path),[])'),('missing','with TemporaryDirectory() as directory:\n    with self.assertRaises(FileNotFoundError):\n        nonblank_lines(Path(directory)/"missing.txt")')],
    'Use Path(path).open(encoding="utf-8") in a with block, then filter stripped lines.',
    'Why should a missing file not silently become an empty report?')

add('JSON is data, not Python in a coat', 'Decode JSON and validate the resulting runtime values.',
    '''JSON is a data format, not executable Python source. `json.loads` decodes text into Python values: objects become dictionaries, arrays become lists, true becomes True, and null becomes None. `json.dumps` produces JSON text from supported Python values. Never use eval to parse untrusted data.

    Successful decoding proves the text is valid JSON, not that its shape matches your application. Validate the top-level container, required fields and value types separately. A decoded boolean still needs special attention when an integer is required.

    Keep serialization at the boundary and ordinary data processing in small functions. A malformed document should produce an honest error rather than a partially invented result. Pip attempted to parse a JSON object with a sticky note reading 'looks dictionary-ish'. We are trying the standard library instead.''',
    'import json\n\nrecord = json.loads(\'{"active": true, "count": 2}\')\n# {"active": True, "count": 2}\ntext = json.dumps(record, sort_keys=True)',
    'Implement load_job_ids(text). Decode a JSON array of non-negative integers; reject a non-list, any bool, non-int, or negative member with ValueError. Let malformed JSON raise its normal JSONDecodeError (a ValueError subclass). Return a new list.',
    'import json\n\ndef load_job_ids(text):\n    raise NotImplementedError("JSON has removed its Python coat")',
    'import json\n\ndef load_job_ids(text):\n    values = json.loads(text)\n    if not isinstance(values,list) or any(type(value) is not int or value < 0 for value in values):\n        raise ValueError("expected a list of non-negative integer IDs")\n    return list(values)',
    [('valid','self.assertEqual(load_job_ids("[0, 7, 7]"),[0,7,7])\nself.assertEqual(load_job_ids("[]"),[])'),('invalid_shape','for text in ["{}","null","[true]","[-1]","[1.5]",\'["7"]\']:\n    with self.assertRaises(ValueError):\n        load_job_ids(text)'),('malformed','with self.assertRaises(json.JSONDecodeError):\n    load_job_ids("[not json")')],
    'Decode first, validate list shape and every member type/range, then return.',
    'Why is valid JSON not enough to establish that a request is a valid job list?')

add('CSV: commas are allowed in names', 'Use the csv module instead of splitting structured text by hand.',
    '''CSV allows fields to contain commas and newlines when they are quoted according to the format. Splitting every line on commas breaks these records. The standard library's csv module understands quoting and escapes, so use the parser for the format rather than a homemade approximation.

    `csv.DictReader` uses the header row as field names and yields one dictionary per data row. Numeric values remain strings until you convert them. With actual files, open using `newline=""` so the csv module can handle newline rules correctly. `StringIO` provides a file-like interface for text already in memory.

    Validate according to your input contract; this mission guarantees the header and row shapes so you can focus on parsing and aggregation. Keep account spelling exact, including spaces and punctuation. Pip declared commas illegal in customer names. The customers have declined the schema migration.''',
    'import csv\nfrom io import StringIO\n\nrows = csv.DictReader(StringIO(\'name,cents\\n"Tea, Ltd",125\\n\'))\n# The name field is one value: Tea, Ltd',
    'Implement csv_balances(text). CSV has headers account,cents and valid integer cent values. Sum by exact account name and return a dictionary. Quoted commas in account names must work. Header-only input returns {}.',
    'import csv\nfrom io import StringIO\n\ndef csv_balances(text):\n    raise NotImplementedError("Let the parser handle the commas")',
    'import csv\nfrom io import StringIO\n\ndef csv_balances(text):\n    balances = {}\n    for row in csv.DictReader(StringIO(text)):\n        name = row["account"]\n        balances[name] = balances.get(name,0) + int(row["cents"])\n    return balances',
    [('aggregate','self.assertEqual(csv_balances("account,cents\\nA,100\\nB,-20\\nA,50\\n"),{"A":150,"B":-20})'),('quoted','self.assertEqual(csv_balances(\'account,cents\\n"Tea, Ltd",125\\n"Tea, Ltd",-25\\n\'),{"Tea, Ltd":100})'),('header_only','self.assertEqual(csv_balances("account,cents\\n"),{})')],
    'DictReader understands quoted fields. Convert each cents field with int before adding.',
    'Why can a quoted newline make even splitting into lines unsafe for general CSV?')

add('Async without the spaghetti', 'Await coroutines concurrently while retaining input order.',
    '''An `async def` function returns a coroutine when called. Awaiting it lets an event loop manage its progress. While a coroutine waits on cooperative asynchronous work, other tasks may run. This is useful for many I/O workloads; it does not automatically make CPU-heavy Python code run in parallel.

    Awaiting several calls one after another is sequential. `asyncio.gather` schedules supplied awaitables together and returns results in the same order as the supplied awaitables, even when completion order differs. Exceptions normally propagate to the awaiting caller.

    Blocking operations such as time.sleep inside an async function block the event-loop thread; use async-aware operations when waiting. Our tests use fake fetch operations, so there is no network dependency. Pip made a function async and expected the coffee machine to run faster. The keyword has politely declined responsibility.''',
    'import asyncio\n\nasync def collect(keys, fetch):\n    return await asyncio.gather(*(fetch(key) for key in keys))\n\n# asyncio.run(collect(keys, fetch)) is an entry point from synchronous code.',
    'Implement async collect_statuses(names, fetch). Call async fetch(name) for each name and await them concurrently. Return results in input order; empty input returns []; propagate fetch errors. Do not use actual network calls.',
    'import asyncio\n\nasync def collect_statuses(names, fetch):\n    raise NotImplementedError("Concurrency is not a coffee accelerator")',
    'import asyncio\n\nasync def collect_statuses(names, fetch):\n    return await asyncio.gather(*(fetch(name) for name in names))',
    [('order_concurrency','async def scenario():\n    started=[]\n    gate=asyncio.Event()\n    async def fetch(name):\n        started.append(name)\n        if len(started)==3:\n            gate.set()\n        await asyncio.wait_for(gate.wait(),timeout=1)\n        return name.upper()\n    result=await collect_statuses(["b","a","c"],fetch)\n    self.assertEqual(result,["B","A","C"])\n    self.assertCountEqual(started,["a","b","c"])\nasyncio.run(scenario())'),('empty','async def fetch(name):\n    raise AssertionError("must not fetch")\nself.assertEqual(asyncio.run(collect_statuses([],fetch)),[])'),('errors','async def fetch(name):\n    raise RuntimeError("offline")\nwith self.assertRaisesRegex(RuntimeError,"offline"):\n    asyncio.run(collect_statuses(["api"],fetch))')],
    'Build awaitables for every name and await asyncio.gather once.',
    'Why does awaiting fetch inside a normal for loop fail the concurrency test?')

assert len(LESSONS) == 72, 'Four original missions per chapter are required.'
