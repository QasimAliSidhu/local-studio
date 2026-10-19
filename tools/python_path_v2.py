"""Prerequisite-first teaching path. Early missions are actual scripts, not test wrappers."""
from copy import deepcopy
from inspect import cleandoc
from textwrap import dedent

PATH = [
 ('Your first programs','Foundation',['py101','py102','py103','py104']),
 ('Names, numbers and values','Foundation',['py105','py173','py174','py181','py182','py175']),
 ('Working with text','Foundation',['py191','py176','py177','py106','py178','py107','py108']),
 ('Build your own functions','Foundation',['py184','py185','py186','py109','py110','py111','py112']),
 ('Make decisions','Foundation',['py179','py189','py125','py126','py127','py128','py124','py121','py122']),
 ('Scope, tests and debugging','Foundation',['py187','py188','py113','py192','py193','py194','py117']),
 ('Lists and tuples','Core Python',['py195','py133','py134','py135']),
 ('Loops and transformations','Core Python',['py129','py130','py131','py132','py196','py136','py119','py120','py180']),
 ('Dictionaries and grouping','Core Python',['py137','py138','py139','py140','py02']),
 ('Sets and uniqueness','Core Python',['py141','py142','py143','py144','py03','py123']),
 ('Errors and validation','Core Python',['py145','py146','py147']),
 ('Describe and validate types','Core Python',['py149','py150','py151','py05','py07']),
 ('Mutation and reliable contracts','Core Python',['py114','py115','py04','py01','py06']),
 ('Modules and program boundaries','Intermediate',['py199','py200','py201']),
 ('Objects, interfaces and records','Intermediate',['py161','py162','py163','py164','py148','py152','py08']),
 ('Functions as tools','Intermediate',['py203','py204','py165','py166','py118']),
 ('Lazy streams and recursion','Intermediate',['py168','py09','py167']),
 ('Advanced Python patterns','Advanced Python',['py116','py207','py205','py206']),
 ('Files and structured data','Backend practice',['py169','py170','py171']),
 ('Storage, searching and time','Backend practice',['py10','py208','py11','py12']),
 ('Concurrency and capstone missions','Backend practice',['py172','py153','py154','py155','py156','py157','py158','py159','py160']),
]


def revised_path(base):
    lessons={item['id']:deepcopy(item) for item in base}
    for item in lessons.values():
        item['teaching']=cleandoc(item['teaching'])
        item['task']=cleandoc(item['task'])

    def put(ident,title,goal,teaching,example,task,starter,solution,checks,hint,reflection,*,mode='script',teaches=(),requires=(),fixtures=None):
        lessons[ident]=dict(id=ident,title=title,goal=goal,teaching=cleandoc(teaching),
            example=dedent(example).strip(),task=cleandoc(task),starter=dedent(starter).strip()+'\n',
            solution=dedent(solution).strip()+'\n',checks=checks,hint=hint,reflection=reflection,
            execution_mode=mode,teaches=list(teaches),requires=list(requires),fixtures=fixtures or {})

    put('py101','Hello, slightly suspicious server','Write one instruction. See your message appear.',
        '''Python follows the instructions you write. The **editor** is where you write them. The **console** is where you see their output.

        ## Show a message

        `print` is a tool Python already provides. It displays a message in the console:

        <figure class="program-picture" aria-label="The code print Service online displays Service online in the console.">
        <div class="program-step"><span>Your code</span><code>print("Service online")</code></div>
        <span class="program-arrow" aria-hidden="true">&#8594;</span>
        <div class="program-step program-result"><span>What appears in the console</span><code>Service online</code></div>
        </figure>

        ## Read the line

        - **print** names the tool.
        - **( )** hold the message you give it.
        - **" "** mark the beginning and end of the text. The quotes do not appear in the console.

        Text inside quotes is called a **string**. You can change the words between the quotes to display a different message.''',
        'print("Service online")',
        'Change the editor greeting to print exactly **Helpdesk online!**. Keep the matching quotes and both parentheses. Press **Run** and look for your message in the console. You only need one line of Python.',
        'print("Hello!")','print("Helpdesk online!")',
        [('message','self.assertEqual(self.output, "Helpdesk online!\\n", "The console should show Helpdesk online! on one line.")')],
        'Keep print("...") and change only the text between the quotes.',
        'The example prints Service online without quotation marks. What text will your edited line display?',teaches=['print','strings'])

    put('py102','The deployment countdown','Read and write instructions in the order Python executes them.',
        '''You have used one print instruction. Now use several. In a simple script, Python executes the first line, then the next, then the next. Each print begins where the previous one left off; its normal newline puts the next message on a new console line.

        The editor and console are different things. The editor contains source code, including quotes and parentheses. The console contains the output of running that code. Do not type the example's output into your program as extra instructions.

        In the example, `Connect` appears first because its instruction is first. Swap the two instructions and you swap their output order. You can use digits inside quotes too: `"3"` is text that displays as 3. We will use actual numeric values in a later mission.

        Before pressing Run, say the three expected lines out loud or write them in your notebook. Comparing a prediction with actual output is a useful habit, not an exam. Pip starts every countdown at 'eventually'. Operations would like something more specific.''',
        'print("Connect")\nprint("Ready")',
        'Write three print instructions. Display **3**, then **2**, then **Launch!**, each on its own line. Use quoted strings, as in the worked example. The starter has the right tools but the wrong order.',
        'print("Launch!")\nprint("2")\nprint("3")',
        'print("3")\nprint("2")\nprint("Launch!")',
        [('three_lines','self.assertEqual(self.output.splitlines(), ["3","2","Launch!"], "Check which instruction runs first, second and third.")'),('normal_newline','self.assertTrue(self.output.endswith("\\n"), "Keep the normal newline from print.")')],
        'Move the Launch instruction below the two number messages.',
        'Predict the example output, then reverse the two lines. What changes?',requires=['print','strings'])

    put('py103','Quotes are not comments','Distinguish the text Python prints from notes Python ignores.',
        '''Quotes have a precise job: they surround text that belongs to a string. You can use a matching pair of single quotes or a matching pair of double quotes. Using single quotes on the outside makes it convenient to include double quotes inside the text, and vice versa.

        A `#` outside a string starts a **comment**. Python ignores the rest of that line. A comment can explain your intention to another person; it does not display a message. A `#` inside quotes is ordinary string content and will be printed.

        Read the example carefully. The first line is a note, so it produces no output. The second line displays a sentence containing quotation marks. The last instruction displays the hash character because it is inside its string.

        You do not need backslash escapes for this mission: choose the convenient outer quote style instead. There are no new function definitions, return values or hidden wrappers to maintain. Pip has submitted a comment saying 'this is definitely correct'. Python ignores that too.''',
        '''# A note for the next engineer\nprint('The robot says "ready".')\nprint("Queue #7")''',
        '''Print exactly this one line: **Pip says: "Ship it!" #probably**. The double quotes and hash are part of the required output. A comment outside the string will not print.''',
        '''# Keep the message inside one matching pair of quotes.\nprint('Pip says: Ship it!')''',
        '''print('Pip says: "Ship it!" #probably')''',
        [('punctuation','self.assertEqual(self.output, \'Pip says: "Ship it!" #probably\\n\')')],
        'Use single quotes around the full message so its double quotes can stay inside.',
        'Which of the example lines is ignored, and why?',teaches=['comments'],requires=['print','strings'])

    put('py104','Numbers do not need costumes','Distinguish numeric expressions from text that looks like arithmetic.',
        '''The quotes you have used make a string. Without quotes, a numeric literal such as `7` is a number. Python can calculate with numbers: `+` adds and `-` subtracts. A calculation such as `7 + 2` is an **expression**: Python evaluates it to a value.

        The input to print can be an expression. In `print(7 + 2)`, Python calculates nine, then gives that value to print. In `print("7 + 2")`, the input is text, so Python displays the characters without doing arithmetic.

        In the example, the console shows `9` on the first line and `7 + 2` on the second. Parentheses around print's input are still required in both cases; quotation marks make the important difference.

        For now, use whole numbers. We will give values names next, then learn multiplication, division and decimal numbers in small steps. Pip has put the calculator inside quotation marks. It now works beautifully as a sign.''',
        'print(7 + 2)\nprint("7 + 2")',
        'First print the numeric result of **2 + 3**. On the next line, print the text **2 + 3**, including the spaces. The console should show 5, then 2 + 3.',
        'print("2 + 3")\nprint("2 + 3")',
        'print(2 + 3)\nprint("2 + 3")',
        [('number_then_text','self.assertEqual(self.output, "5\\n2 + 3\\n")')],
        'Remove the quotes only from the first line\'s arithmetic expression.',
        'Why does the example print two different things even though both lines contain 7 + 2?',teaches=['arithmetic'],requires=['print','strings'])

    put('py105','Give your numbers useful names','Create a variable, calculate a new value and print it.',
        '''A **variable** is a name referring to a value. `minutes = 3` assigns the value three to the name minutes. Read `=` as 'assign', not as a question about equality. On a later line, using the name retrieves its current value.

        You can use named values in an expression. The `*` operator means multiplication, so `minutes * 60` calculates the number of seconds. The right side of an assignment is calculated first; its result is then assigned to the name on the left.

        In the example, minutes refers to 2, seconds refers to 120, and `print(seconds)` displays 120. Do not quote the name when you want its value: `print("seconds")` displays the word instead.

        Choose names that tell you the quantity and units. This helps prevent mixing minutes with seconds, a hobby Pip has unfortunately taken up. You do not need to define a function or accept inputs yet. This mission is still a plain script.''',
        'minutes = 2\nseconds = minutes * 60\nprint(seconds)',
        'The starter supplies minutes = 3 and extra_seconds = 5. Create a variable named **seconds** equal to minutes * 60 + extra_seconds, then print seconds. Keep the supplied inputs. Expected output: **185**.',
        'minutes = 3\nextra_seconds = 5\n# Calculate seconds below, then print its value.',
        'minutes = 3\nextra_seconds = 5\nseconds = minutes * 60 + extra_seconds\nprint(seconds)',
        [('value','self.assertEqual(self.state.get("seconds"),185,"Create the seconds variable from the supplied quantities.")'),('output','self.assertEqual(self.output,"185\\n")')],
        'Put seconds on the left of = and the calculation on its right. Then use print(seconds).',
        'What would print("seconds") display instead?',teaches=['variables'],requires=['arithmetic','print'])

    put('py173','A name can change its mind','Reassign a variable using its previous value.',
        '''Assignment can bind an existing name to a new value. In `jobs = jobs + 1`, Python first reads the old jobs value, adds one, and then assigns the result back to jobs. This is not a circular mathematical equation; it is a sequence of actions.

        A print observes the value at that point in the script. It does not change later when the variable is reassigned. Trace the example one line at a time: first jobs is two, the first print displays two, the update makes jobs three, and the final print displays three.

        Variable names are case-sensitive, so jobs and Jobs are different names. A new name must be assigned before you can read it. The mission keeps a single name so you can focus on the update.

        This is the beginning of program state: values changing as work happens. Pip's work counter was stuck at 'busy'. A number is easier to audit.''',
        'jobs = 2\nprint(jobs)\njobs = jobs + 1\nprint(jobs)',
        'Start with jobs = 4. Increase jobs by 2 using its current value, then print it. Keep the updated value in jobs. Expected output: 6.',
        'jobs = 4\n# Update jobs here.\nprint(jobs)',
        'jobs = 4\njobs = jobs + 2\nprint(jobs)',
        [('state','self.assertEqual(self.state.get("jobs"),6)'),('output','self.assertEqual(self.output,"6\\n")')],
        'Use jobs = jobs + 2 before the print.',
        'In the example, why does the first printed line remain 2?',requires=['variables','arithmetic','print'])

    put('py174','Text, whole numbers and decimals','Recognize strings, ints and floats before converting between them.',
        '''Values have **types**, meaning different kinds of information with different supported operations. A whole number such as `12` is an `int`. A number with a decimal point such as `1.5` is a `float`. Quoted text such as `"12"` is a `str`, even when its characters look numeric.

        With numbers, `+` adds. With two strings, `+` joins their characters, an operation called concatenation. Python does not automatically choose how to combine a string and a number; that usually needs an explicit conversion, which we will learn later.

        The built-in tool `type(value)` reports the kind of value. Its console representation contains the word class, such as `<class 'int'>`. That is Python's type label; you are not being asked to create classes here.

        In the example, the first result is fifteen and the second is the text 123. Pip stored the number of snacks as text and tried adding three. The budget became enormous.''',
        'count = 12\nlabel = "12"\nprint(count + 3)\nprint(label + "3")',
        'Create count = 8, label = "8", and rate = 1.5. Print count + 2, then label + "2". Keep those three variables with their intended types. Expected lines: 10 and 82.',
        'count = 8\nlabel = "8"\nrate = 1.5\n# Print the numeric addition, then the text concatenation.',
        'count = 8\nlabel = "8"\nrate = 1.5\nprint(count + 2)\nprint(label + "2")',
        [('types','self.assertIs(type(self.state.get("count")),int)\nself.assertIs(type(self.state.get("label")),str)\nself.assertIs(type(self.state.get("rate")),float)'),('outputs','self.assertEqual(self.output,"10\\n82\\n")')],
        'Use unquoted 2 with count and quoted "2" with label.',
        'Is "1.5" a float or a string? Which punctuation tells you?',teaches=['types'],requires=['variables','arithmetic','strings'])

    put('py181','Multiply, divide, and keep the units','Use multiplication, division and parentheses in a named calculation.',
        '''You have used `+`, `-` and `*`. The `/` operator divides and produces a float, even when the division comes out evenly. `8 / 2` gives 4.0. The decimal point is a representation difference, not an extra item.

        Multiplication and division happen before addition and subtraction. Parentheses group a calculation when you want a different order: `(2 + 3) * 4` is twenty, while `2 + 3 * 4` is fourteen. Parentheses here group arithmetic; parentheses after a tool name supply its input. Context tells you the job.

        Store an intermediate calculation in a named variable if that makes the units clearer. You should be able to explain what a result means, not merely reproduce its digits. Division by zero is an error; our supplied capacity is positive.

        Pip measured server speed in biscuits per worry. We will use jobs per second.''',
        'jobs = 12\nseconds = 4\nrate = jobs / seconds\nprint(rate)\n# The value displayed is 3.0.',
        'Keep jobs = 15 and seconds = 6. Assign jobs / seconds to rate, then print rate. The result should be 2.5.',
        'jobs = 15\nseconds = 6\n# Calculate rate and print it.',
        'jobs = 15\nseconds = 6\nrate = jobs / seconds\nprint(rate)',
        [('rate','self.assertEqual(self.state.get("rate"),2.5)'),('display','self.assertEqual(self.output,"2.5\\n")')],
        'Divide the number of jobs by the number of seconds.',
        'Predict (2 + 3) * 4 and 2 + 3 * 4 before running either.',requires=['arithmetic','variables','types'])

    put('py182','Full boxes and leftovers','Use integer division and remainder before they appear in larger functions.',
        '''Ordinary division answers how much each group gets, including fractions. Sometimes we need whole groups instead. For non-negative integers, `items // size` counts complete groups and `items % size` gives the leftover items. The symbols are called floor division and modulo.

        With fourteen items and boxes holding six, there are two full boxes and two loose items. Reconstructing the total verifies the reasoning: two times six plus two equals fourteen. At an exact multiple, the remainder is zero.

        These expressions return numeric values you can assign or print just like addition. We restrict this mission to non-negative quantities and a positive capacity. Negative floor-division behavior deserves its own careful interpretation rather than an accidental assumption.

        Do not add an extra full box for the remainder: it is not full. Pip is attempting to invoice the empty space, but that is outside this contract.''',
        'items = 14\nsize = 6\nprint(items // size)\nprint(items % size)\n# Two lines, both displaying 2.',
        'Keep items = 17 and size = 5. Store the complete box count in full_boxes and the leftover count in loose_items. Print full_boxes, then loose_items. Expected lines: 3 and 2.',
        'items = 17\nsize = 5\n# Calculate full_boxes and loose_items, then print both.',
        'items = 17\nsize = 5\nfull_boxes = items // size\nloose_items = items % size\nprint(full_boxes)\nprint(loose_items)',
        [('quantities','self.assertEqual(self.state.get("full_boxes"),3)\nself.assertEqual(self.state.get("loose_items"),2)'),('output','self.assertEqual(self.output,"3\\n2\\n")')],
        'Use // for full_boxes and % for loose_items.',
        'What should both expressions produce when items is zero?',teaches=['integer_division'],requires=['variables','arithmetic'])

    put('py175','A tool can give back a value','Use len and assign its result before printing it.',
        '''Some tools give a value back for the next part of your program to use. The built-in function `len` counts the characters in a string. Calling `len("queue")` produces the number five. You can assign that result to a variable, calculate with it, or pass it into print.

        This is a **return value**: a result handed back to the caller. You do not need a return statement to use a built-in tool. Later, when we build functions, we will write return statements to supply our own results.

        Spaces count as characters too. An empty string has length zero. In `print(len("queue"))`, Python calculates the inner len call first, then prints its result. Splitting that into two named steps can be easier to follow at first.

        Pip counted only the letters that looked productive. The standard library is less judgmental.''',
        'word = "queue"\nletters = len(word)\nprint(letters)',
        'Keep message = "hi pip". Assign its length to characters, then print characters. Count the space too. Expected output: 6.',
        'message = "hi pip"\n# Use len to calculate characters, then print the result.',
        'message = "hi pip"\ncharacters = len(message)\nprint(characters)',
        [('count','self.assertEqual(self.state.get("characters"),6)'),('output','self.assertEqual(self.output,"6\\n")')],
        'Assign len(message) to characters; the space is one of the six characters.',
        'What would len("") give back?',teaches=['builtin_results'],requires=['variables','strings','print'])

    put('py191','Find a character by its position','Read string indexes starting at zero.',
        '''A string has an order. An **index** identifies one character's position, starting at zero. In `"Pip"`, index 0 is P, index 1 is i, and index 2 is p. Square brackets ask for the character at a position: `name[0]`.

        Negative indexes count backward from the end. Index -1 is the last character, so you do not have to calculate the length first. Strings are not changed by reading a character. Asking for a position that does not exist causes an IndexError; our supplied string is non-empty.

        The example displays Q and e on separate lines. Notice the difference between parentheses, which call a tool, and square brackets, which select a position. A quoted `"0"` is text, not the numeric index expected here.

        Indexing will also work on lists later, but this exercise only uses text. Pip has requested that counting start at eleven for branding reasons. Python's answer is zero.''',
        'name = "Queue"\nprint(name[0])\nprint(name[-1])',
        'Keep code = "PYTHON". Print its first character, then its last character. Use indexing with code; expected output lines are P and N.',
        'code = "PYTHON"\n# Print the two endpoint characters.',
        'code = "PYTHON"\nprint(code[0])\nprint(code[-1])',
        [('characters','self.assertEqual(self.output,"P\\nN\\n")')],
        'The first index is 0 and the last can be reached with -1.',
        'Why is code[1] the second character, rather than the first?',teaches=['indexing'],requires=['strings','variables'])

    put('py176','Trim the space around the message','Call one string method and keep its returned result.',
        '''A **method** is a named tool attached to a value. Put a dot after that value, then the method's name and parentheses. For a string, `raw.strip()` makes a version without whitespace at either end. Whitespace includes spaces, tabs and line breaks.

        The empty parentheses mean we supply no extra arguments in this call. The string before the dot is already the thing the method works on. You have used built-in calls such as len(message); this is another calling form, with its object on the left.

        Strings are **immutable**: their characters are not edited in place. strip returns a new result. Assign it to a name so you can use it; the original raw string stays the same. Internal spaces stay too, because only the outside is trimmed.

        The example preserves the space between night and shift. Pip's last cleanup removed every space and produced a very long username.''',
        'raw = "  night shift  "\nclean = raw.strip()\nprint(clean)',
        'Keep raw = "  Pip on call  ". Assign raw.strip() to clean and print clean. Do not change raw. The output should be Pip on call, with its internal spaces intact.',
        'raw = "  Pip on call  "\n# Create clean and display it.',
        'raw = "  Pip on call  "\nclean = raw.strip()\nprint(clean)',
        [('new_value','self.assertEqual(self.state.get("clean"),"Pip on call")\nself.assertEqual(self.state.get("raw"),"  Pip on call  ")'),('output','self.assertEqual(self.output,"Pip on call\\n")')],
        'Use a new name for the value returned by raw.strip().',
        'Does strip remove the space between night and shift in the example?',teaches=['methods'],requires=['strings','variables','builtin_results'])

    put('py177','Lowercase without losing the original','Use lower as a second example of a string method.',
        '''The string method `lower()` returns a version with uppercase letters changed to lowercase. Its calling shape is the same as strip: put the method after a dot and keep the parentheses. A method name without parentheses refers to the tool rather than running it.

        Like strip, lower leaves the original string unchanged. The returned value needs to be assigned or used. Numbers and punctuation in the text stay as they are; lower is not a general cleaning rule.

        Case normalization can make a display label consistent, but it is a choice you should state. Passwords, for example, must not be silently lowercased. Here we are working only with a status label.

        Read the example in three steps: create raw text, make normalized text, display the normalized value. The next lesson will combine methods you have now practiced individually. Pip's dashboard used to shout every status, including 'everything is quiet'.''',
        'raw = "READY-7!"\nnormalized = raw.lower()\nprint(normalized)',
        'Keep status = "On CALL!". Store status.lower() in normalized, then print normalized. Keep status unchanged. Expected output: on call!',
        'status = "On CALL!"\n# Create normalized, then print it.',
        'status = "On CALL!"\nnormalized = status.lower()\nprint(normalized)',
        [('result','self.assertEqual(self.state.get("normalized"),"on call!")\nself.assertEqual(self.state.get("status"),"On CALL!")'),('output','self.assertEqual(self.output,"on call!\\n")')],
        'Call status.lower(), including its parentheses.',
        'Which characters in READY-7! change, and which remain?',requires=['methods','strings','variables'])

    put('py106','Clean up the robot username','Combine familiar string methods with one new replacement rule.',
        '''You have used strip to trim and lower to change case. The method `replace(old, new)` returns text with each occurrence of old replaced by new. Its two inputs are separated by a comma. `text.replace(" ", "_")` changes each ASCII space into an underscore.

        You can keep each intermediate result in a named variable or **chain** the methods. In `raw.strip().lower()`, Python first trims raw, then calls lower on the returned string. Read the chain left to right.

        The original raw string remains unchanged. Trimming removes only outside whitespace, and replacing each space does not collapse repeated spaces. Two internal spaces therefore become two underscores. These rules are specific to a handle, not to every kind of user input.

        The example turns Night Shift into night_shift after trimming. Pip would like to include twelve invisible spaces in its handle. The name-tag printer has declined.''',
        'raw = "  Night Shift  "\nclean = raw.strip().lower().replace(" ", "_")\nprint(clean)',
        'Keep raw = "  Pip  Seven  ". Build clean by trimming, lowercasing, then replacing every internal space with _. Print clean. The two internal spaces must become two underscores: pip__seven.',
        'raw = "  Pip  Seven  "\n# Build clean, then print it.',
        'raw = "  Pip  Seven  "\nclean = raw.strip().lower().replace(" ", "_")\nprint(clean)',
        [('normalized','self.assertEqual(self.state.get("clean"),"pip__seven")\nself.assertEqual(self.state.get("raw"),"  Pip  Seven  ")'),('output','self.assertEqual(self.output,"pip__seven\\n")')],
        'Use strip(), lower(), then replace(" ", "_") on their successive results.',
        'Why do two internal spaces produce two underscores?',requires=['methods','variables','strings'])

    put('py178','Put a value inside a message','Build a basic f-string before using format specifiers.',
        '''A string written with f before its opening quote is an **f-string**. Text inside braces `{...}` is evaluated and inserted into the message. Text outside braces stays as written. This is useful when a sentence includes a named value.

        In `f"Worker {name}"`, the braces mean 'insert the current value of name here'. Leaving off the f means the braces are ordinary characters instead. Quoting the word name inside the braces would insert that word rather than reading the variable.

        An f-string can include several values, including numbers. Python makes a readable text representation when inserting them. You do not need to convert an integer to a string yourself for this form.

        Predict the example: it displays Mira has 3 jobs. The variable names and braces are not in the output. Pip has requested a dashboard where every message contains its name. For one lesson, we can indulge that.''',
        'name = "Mira"\njobs = 3\nmessage = f"{name} has {jobs} jobs"\nprint(message)',
        'Keep name = "Pip" and jobs = 4. Assign an f-string to message so printing it displays exactly Pip has 4 jobs. Use the two variable values inside braces.',
        'name = "Pip"\njobs = 4\n# Build message, then display it.',
        'name = "Pip"\njobs = 4\nmessage = f"{name} has {jobs} jobs"\nprint(message)',
        [('message','self.assertEqual(self.state.get("message"),"Pip has 4 jobs")'),('output','self.assertEqual(self.output,"Pip has 4 jobs\\n")')],
        'Place f immediately before the opening quote, then use {name} and {jobs}.',
        'What would print("{name} has {jobs} jobs") display without the f?',teaches=['fstrings'],requires=['variables','strings'])

    put('py107','A status message worth reading','Format a decimal inside an f-string after learning basic interpolation.',
        '''An f-string already lets you insert values into a message. A **format specifier** controls how an inserted value is displayed. Put a colon after the expression inside its braces, followed by the formatting rule.

        The rule `.2f` displays a number with two digits after the decimal point. In `f"{rate:.2f}"`, a rate of 2.5 becomes the text 2.50. Formatting changes the representation used in that message; the numeric rate itself stays 2.5.

        Keep literal punctuation outside the braces and the expression plus format rule inside. The example displays Mira: 7.50/s. You can build the message in a variable to check it before printing.

        Two decimal places are a display choice, not a universal precision guarantee. We will discuss floating-point arithmetic after comparisons. For now, the supplied value formats cleanly. Pip's previous dashboard had thirty decimal places and no room for the service name.''',
        'name = "Mira"\nrate = 7.5\nmessage = f"{name}: {rate:.2f}/s"\nprint(message)',
        'Keep name = "Pip", count = 7, rate = 2.5. Build message and print exactly Pip processed 7 jobs (2.50/s). Format rate with two decimal places.',
        'name = "Pip"\ncount = 7\nrate = 2.5\n# Build and print message.',
        'name = "Pip"\ncount = 7\nrate = 2.5\nmessage = f"{name} processed {count} jobs ({rate:.2f}/s)"\nprint(message)',
        [('message','self.assertEqual(self.state.get("message"),"Pip processed 7 jobs (2.50/s)")\nself.assertEqual(self.state.get("rate"),2.5)'),('output','self.assertEqual(self.output,"Pip processed 7 jobs (2.50/s)\\n")')],
        'Use {rate:.2f} for the rate, and ordinary {name} and {count} for the others.',
        'Has the value stored in rate changed because the message shows 2.50?',requires=['fstrings','types','variables'])

    put('py108','Numbers wearing string costumes','Convert valid text to an integer before calculating.',
        '''Text from a configuration file or a form often looks like a number but is still a string. The built-in tool `int(text)` converts valid whole-number text into an integer. Its result can be assigned and used in arithmetic.

        Compare the example's two lines: adding quoted "3" to raw joins strings; converting raw with int lets you add the number 3. Python does not guess which meaning you intend. A separate function, `str(value)`, gives a text representation when you need one.

        Not every string is valid integer text. A decimal like "1.5" is not a whole-number representation for int. We will learn to handle conversion errors in the errors chapter; this mission supplies valid text, so there is no recovery code to invent yet.

        Keep the original text and store the parsed number under a new name. Pip tried to order "12" plus "3" biscuits and created an impressive string. The kitchen requires arithmetic.''',
        'raw = "12"\nprint(raw + "3")\ncount = int(raw)\nprint(count + 3)',
        'Keep raw = "8". Convert it with int into a variable count, then print count + 2. The output should be 10, not 82. Keep raw as its original string.',
        'raw = "8"\n# Convert raw into count and print count + 2.',
        'raw = "8"\ncount = int(raw)\nprint(count + 2)',
        [('conversion','self.assertIs(type(self.state.get("count")),int)\nself.assertEqual(self.state.get("count"),8)\nself.assertEqual(self.state.get("raw"),"8")'),('output','self.assertEqual(self.output,"10\\n")')],
        'Use count = int(raw) before doing numeric addition.',
        'Why do the example\'s two lines display 123 and 15?',teaches=['conversions'],requires=['types','arithmetic','variables'])

    put('py184','Build a tool of your own','Explain def, a function body and a call before asking for a function.',
        '''You have called Python's built-in print and len tools. Now you will **define** a function: give a name to instructions you want to reuse. `def` begins a definition. The name comes next, followed by parentheses and a colon.

        The indented lines below the definition are its **body**. Use four spaces of indentation. They belong to the function and run when it is called, not merely because the definition has been read. A call uses the name with parentheses, just like print.

        In the example, Python first defines ring_bell without printing. The final unindented line calls it, so the body runs and the console displays Ding!. Without that final call, the script would define the tool but never use it.

        Keep this first function simple: no parameters or return statement yet. Those get their own next lessons. Pip has been calling a function that nobody defined. We are starting with the other half of the agreement.''',
        'def ring_bell():\n    print("Ding!")\n\nring_bell()',
        'Define a function named greet with no parameters. Its indented body must print Hello, helpdesk! Then call greet() once from an unindented line. The console should show the greeting once.',
        '# Define greet, put its print inside the body, then call it below.',
        'def greet():\n    print("Hello, helpdesk!")\n\ngreet()',
        [('defined','self.assertTrue(callable(self.state.get("greet")),"Define a function named greet.")'),('called','self.assertEqual(self.output,"Hello, helpdesk!\\n","Define and call greet once.")')],
        'Start with def greet():, indent the print by four spaces, and put greet() at the left edge below.',
        'What would the example print if the final ring_bell() line were removed?',teaches=['functions'],requires=['print','variables'])

    put('py185','Give your function an input','Distinguish a parameter in a definition from an argument in a call.',
        '''A function can accept an input so the same instructions work with different values. The definition puts a **parameter name** between its parentheses: `def greet(name):`. A call supplies an **argument value**, such as greet("Mira"). During that call, name refers to the supplied string.

        Use the parameter inside the body just like another variable. Do not put quotes around its name when you mean its value. An f-string can insert that value into a greeting, using the syntax you have already practiced.

        Every call supplies its own input. The example calls welcome twice, once for Mira and once for Pip, so it prints two different messages. The body is written only once. This is the practical reason for introducing a function rather than duplicating instructions.

        Define the function before calling it. Pip would like all callers to say its name, but the whole point is that Mira can call too.''',
        'def welcome(name):\n    print(f"Welcome, {name}!")\n\nwelcome("Mira")\nwelcome("Pip")',
        'Define greet(name) to print Hello, NAME! using the supplied name. In the script, call it for Mira, then Pip. The checks also try another name, so do not hardcode the greeting inside the function.',
        'def greet(name):\n    print("Hello, name!")\n\ngreet("Mira")\ngreet("Pip")',
        'def greet(name):\n    print(f"Hello, {name}!")\n\ngreet("Mira")\ngreet("Pip")',
        [('calls','self.assertEqual(self.output,"Hello, Mira!\\nHello, Pip!\\n")'),('uses_parameter','self.assertTrue(callable(self.state.get("greet")))\nwith redirect_stdout(StringIO()) as output:\n    self.state["greet"]("Jo")\nself.assertEqual(output.getvalue(),"Hello, Jo!\\n")')],
        'Put name inside braces in an f-string, rather than inside ordinary text.',
        'In welcome("Mira"), which part is the argument and which name is the parameter?',teaches=['parameters'],requires=['functions','fstrings'])

    put('py186','Hand a result back','Explain return separately from printing before graded function challenges.',
        '''A function can hand a result back to its caller with `return`. The caller can assign that value, calculate with it or pass it to print. Returning is different from printing: printing displays something, while returning makes a result available to another part of the program.

        Read the example in order. Defining triple does not calculate yet. The call triple(4) runs the body and returns twelve. That value is assigned to answer, and print(answer) displays it. The function itself does not print.

        A return ends the current call, so instructions after an unconditional return in the same body will not run. You can test a useful function with several inputs instead of tying it to one display message.

        The next lesson will remove the example calls from the editor because the test runner will call your function for you. You will know exactly which function to define and which result it must return. Pip has finally learned that printing a receipt is not the same as returning the borrowed biscuits.''',
        'def triple(number):\n    return number * 3\n\nanswer = triple(4)\nprint(answer)',
        'Define double(number) to return number * 2 without printing inside the function. In the script, assign double(5) to answer and print answer. The checks also call double with other numbers.',
        'def double(number):\n    return number\n\nanswer = double(5)\nprint(answer)',
        'def double(number):\n    return number * 2\n\nanswer = double(5)\nprint(answer)',
        [('script','self.assertEqual(self.output,"10\\n")\nself.assertEqual(self.state.get("answer"),10)'),('returned_result','self.assertTrue(callable(self.state.get("double")))\nwith redirect_stdout(StringIO()) as output:\n    self.assertEqual(self.state["double"](-3),-6)\n    self.assertEqual(self.state["double"](0),0)\nself.assertEqual(output.getvalue(),"","Return the result; printing it belongs to the caller.")')],
        'The function needs return number * 2. Its caller prints the returned answer.',
        'Which example line displays text, and which line hands a numeric result back?',teaches=['returns'],requires=['functions','parameters','arithmetic'])

    put('py179','True, False, and nothing supplied','Read a comparison result and distinguish None from zero.',
        '''A comparison asks a question and produces a **boolean**: either True or False. The names use capital first letters and no quotes. `==` asks whether two values are equal, while `=` assigns a value to a name. `>` asks whether the left value is greater; `<` asks whether it is smaller. Adding `=` makes the boundary inclusive: `>=` and `<=`.

        You can print a comparison to inspect its answer before using it to control the program. `3 > 2` produces True; `3 == 2` produces False. These values are different from the strings "True" and "False".

        **None** is Python's absence marker. A function that supplies no return value gives None. It is not zero, an empty string, or the word "None". Use `value is None` when the question is specifically whether a value is absent.

        The example asks two different questions about a missing setting. Pip calls every missing value 'probably twelve'. We will keep absence explicit.''',
        'setting = None\nprint(setting is None)\nprint(0 == None)',
        'Keep jobs = 0 and setting = None. Print jobs == 0, then setting is None, then jobs > 0. Expected lines: True, True, False. Use the expressions rather than quoted answers.',
        'jobs = 0\nsetting = None\n# Print the three comparisons in the requested order.',
        'jobs = 0\nsetting = None\nprint(jobs == 0)\nprint(setting is None)\nprint(jobs > 0)',
        [('booleans','self.assertEqual(self.output,"True\\nTrue\\nFalse\\n")'),('absence','self.assertIsNone(self.state.get("setting"))\nself.assertEqual(self.state.get("jobs"),0)')],
        'Use == for value equality and is None for the absence check.',
        'Why is jobs == 0 a question, while jobs = 0 is an instruction?',teaches=['comparisons','booleans','none'],requires=['variables','print'])

    put('py189','Choose which instruction runs','Introduce if, else and indentation using a comparison you understand.',
        '''An `if` statement lets a boolean result choose what happens next. Put a condition after if and finish its line with a colon. The indented body runs only when that condition is True. An optional `else:` body runs when it is False.

        The indentation marks the two bodies, just as indentation marked a function body earlier. An unindented line afterward runs regardless of the decision. Only one side of this if/else choice runs.

        Trace the example with jobs equal to two, then with jobs equal to zero. The first case prints busy and the second prints idle. The script does not print both labels, and it does not keep repeating the condition; repetition is a later topic.

        This is your first branch. More complex rules should be built from clear small decisions rather than guessed punctuation. Pip's scheduling rule was to do both choices simultaneously. The printer is still recovering.''',
        'jobs = 2\nif jobs > 0:\n    print("busy")\nelse:\n    print("idle")',
        'Keep jobs = 0. Fix the two messages so the script prints busy when jobs > 0 and idle otherwise. The supplied condition is correct; the starter messages are swapped.',
        'jobs = 0\nif jobs > 0:\n    print("idle")\nelse:\n    print("busy")',
        'jobs = 0\nif jobs > 0:\n    print("busy")\nelse:\n    print("idle")',
        [('chosen_branch','self.assertEqual(self.output,"idle\\n")')],
        'A zero job count makes jobs > 0 False, so the else body must print idle.',
        'Which body would run if jobs were changed to one?',teaches=['branches'],requires=['comparisons','variables','booleans'])

    put('py187','Names inside and outside a call','Explain local names before mutation or closures.',
        '''A name assigned inside a function normally belongs to that call's **local scope**. A name assigned at the top level belongs to the module. A local name may have the same spelling as an outer name without replacing that outer binding.

        Read the example by following the two labels separately. The module label starts as outside. Calling local_label creates a local label equal to inside and returns it. Printing the module label afterward still displays outside.

        A return makes the local result available to the caller; it does not promote all of the function's local names into global variables. Explicit inputs and returned results keep small calculations easy to reason about.

        For now, we are discussing immutable strings and numbers. Shared mutable lists introduce a different issue, which has its own chapter after collections. Closures and nonlocal also wait until the advanced patterns chapter. Pip has put two identical name tags on two different desks. The tags do not merge the desks.''',
        'label = "outside"\ndef local_label():\n    label = "inside"\n    return label\n\nprint(local_label())\nprint(label)',
        'Keep label = "global" at module level. Implement local_label() to create a local label = "local" and return it. Calling it must leave the module label unchanged.',
        'label = "global"\n\ndef local_label():\n    pass',
        'label = "global"\n\ndef local_label():\n    label = "local"\n    return label',
        [('local','self.assertEqual(local_label(),"local")'),('outer_unchanged','local_label()\nimport challenge\nself.assertEqual(challenge.label,"global")')],
        'Assign label inside the function and return that local name. No global keyword is needed.',
        'Predict both lines from the example before running it.',mode='function',teaches=['scope'],requires=['functions','returns','variables'])

    put('py188','Each call gets fresh local work','Initialize call-specific state inside the function.',
        '''A function can be called many times. Each call creates its own local names for the parameters and any local assignments. When the calculation needs a temporary running value, initialize it inside the function rather than retaining it at module level.

        The example calls add_bonus twice with the same input. Each call starts from its own amount and produces twelve. It does not produce fourteen on the second call because total is not shared between calls.

        The shorthand `total += bonus` means update total using its current value; for numbers it is equivalent to `total = total + bonus`. It does not alter the caller's numeric variable. You can keep the longer form while learning if it is clearer.

        Later we will deliberately model retained state with objects and closures. First, make repeated pure calculations predictable. Pip has a calculator that remembers every previous invoice. Accounting has asked for fresh local work.''',
        'def add_bonus(amount):\n    total = amount\n    total = total + 2\n    return total\n\nprint(add_bonus(10))\nprint(add_bonus(10))',
        'Implement adjusted_total(amount, bonus). Create a local total from amount, add bonus and return it. Calls must remain independent. Inputs are integers, including zero and negative values.',
        'def adjusted_total(amount, bonus):\n    pass',
        'def adjusted_total(amount, bonus):\n    total = amount\n    total += bonus\n    return total',
        [('normal','self.assertEqual(adjusted_total(10,2),12)'),('fresh','self.assertEqual(adjusted_total(10,2),12)\nself.assertEqual(adjusted_total(10,2),12)\nself.assertEqual(adjusted_total(0,0),0)'),('signed','self.assertEqual(adjusted_total(-2,5),3)')],
        'Keep the temporary total inside the function, then return the sum.',
        'Why do repeated example calls both display 12?',mode='function',requires=['scope','functions','returns','arithmetic'])

    put('py192','A failing example is a clue','Fix one arithmetic rule using known input and expected output.',
        '''A **test** runs your program with an input and compares the actual result with an expected result. If the two differ, it reports a failure. Read it as a small reproducible example: 'with this input, I expected this value, but observed that value'.

        A function can be valid Python and still implement the wrong rule. Syntax tells Python how to read your instructions; the contract tells you which behavior those instructions need to produce. Changing random punctuation is less useful than finding the first point where behavior differs from the rule.

        The example function adds two when its name and contract say to double. It happens to work for input two, so one passing example is weak evidence. Try zero and another positive number to reveal the difference.

        Start with this small arithmetic bug before debugging loops or stateful callbacks. Pip's first test was 'it ran'. We would also like it to do the requested job.''',
        'def broken_double(number):\n    return number + 2\n\nprint(broken_double(2))\nprint(broken_double(5))',
        'Fix double_number(number) to return twice the supplied integer. It must work for zero, negatives and repeated calls. Do not print inside the function.',
        'def double_number(number):\n    return number + 2',
        'def double_number(number):\n    return number * 2',
        [('ordinary','self.assertEqual(double_number(5),10)'),('zero_negative','self.assertEqual(double_number(0),0)\nself.assertEqual(double_number(-3),-6)'),('repeatable','self.assertEqual(double_number(7),14)\nself.assertEqual(double_number(7),14)')],
        'Adding two is different from multiplying by two for most inputs.',
        'Which example input accidentally makes the broken rule look correct?',mode='function',requires=['functions','returns','arithmetic'])

    put('py193','Read the check before changing the code','Connect an assertion with a precise behavioral rule.',
        '''An **assertion** states a condition a test expects to be true. Plain Python `assert result == expected` raises AssertionError when the condition is false. Our test runner reports actual and expected values using more descriptive assertions, but the basic idea is the same.

        Separate a test failure from a syntax error. A failing equality assertion usually means the program ran and returned the wrong result. A SyntaxError means Python could not read the program. Inspect the reported line and the kind of error before deciding what to fix.

        Use boundary cases that distinguish competing interpretations of a rule. Here the fee applies once to the whole order, even when the item quantity is zero. That empty-order case is not an invitation to guess a different business policy.

        Assertions are useful for tests and internal expectations, not a replacement for validating untrusted input: Python can disable them under optimization. Pip has written 'correct' in a comment. An assertion requires evidence.''',
        'def add_fee(amount, fee):\n    return amount + fee\n\nassert add_fee(10, 2) == 12',
        'Fix billed_total(price, quantity, fee). Return price * quantity + fee, charging the fee once. Inputs are non-negative integers. Use the failing zero-quantity and multiple-item cases to explain the bug.',
        'def billed_total(price, quantity, fee):\n    return (price + fee) * quantity',
        'def billed_total(price, quantity, fee):\n    return price * quantity + fee',
        [('fee_once','self.assertEqual(billed_total(10,3,2),32)'),('zero_quantity','self.assertEqual(billed_total(10,0,2),2)'),('no_fee','self.assertEqual(billed_total(7,2,0),14)')],
        'The fee belongs after the multiplication, rather than inside its parentheses.',
        'Which test case proves the fee applies once even when no items are ordered?',mode='function',teaches=['assertions'],requires=['functions','comparisons','arithmetic'])

    put('py194','The console is not the return value','Recognize a print-versus-return mistake in a graded function.',
        '''A familiar source of confusion is seeing the right number in the console while a test still fails. The test may be checking a returned value, not printed text. A function that only prints reaches its end without explicitly returning a value; its caller receives None.

        Trace the example: show_total displays twelve, but saved becomes None because printing has not supplied a return result. The final print therefore displays None. A useful calculation can return twelve and let its caller decide whether to display it.

        Read each task's contract. Some early script missions explicitly ask for console output; a function challenge normally names the function and the value it should return. Our editor labels the active file, and the assignment states the expected behavior.

        This lesson repeats a concept in a debugging setting rather than introducing a new syntax shortcut. Pip printed a shipping label and considered the parcel delivered. The receiving function disagreed.''',
        'def show_total(amount):\n    print(amount + 2)\n\nsaved = show_total(10)\nprint(saved)',
        'Fix plus_two(number) to return number + 2 without printing. Inputs are integers. A correct returned value with extra console output still violates this contract.',
        'def plus_two(number):\n    print(number + 2)',
        'def plus_two(number):\n    return number + 2',
        [('returned','self.assertEqual(plus_two(10),12)\nself.assertEqual(plus_two(-2),0)'),('quiet','with redirect_stdout(StringIO()) as output:\n    plus_two(0)\nself.assertEqual(output.getvalue(),"")')],
        'Use return where the starter uses print.',
        'Why does saved become None in the example even though 12 appears in the console?',mode='function',requires=['returns','functions','none'])

    put('py195','Several values, one ordered list','Keep related values together, then count them.',
        '''A **list** holds several values in order. Picture a row of boxes, with one value in each box:

        <figure class="list-picture" aria-label="The list jobs contains backup, email and report: three items.">
        <figcaption><strong>jobs</strong><span>One list, three items</span></figcaption>
        <div class="list-items"><code>"backup"</code><code>"email"</code><code>"report"</code></div>
        </figure>

        In Python, put square brackets **[ ]** around the values and a comma between them.

        ## Count the items

        Use `len(jobs)` to count the boxes. Each value counts as **one item**, however long its text is.

        An empty list, `[]`, contains **zero items**.''',
        'jobs = ["backup", "email", "report"]\nprint(len(jobs))  # Displays 3',
        '''Complete `job_count(jobs)`:

        - **Return** the number of items using `len(jobs)`.
        - Leave the list unchanged.
        - An empty list must return `0`.

        For example, `job_count(["backup", "email"])` returns `2`.''',
        'def job_count(jobs):\n    pass',
        'def job_count(jobs):\n    return len(jobs)',
        [('count','self.assertEqual(job_count(["a","b"]),2)'),('empty','self.assertEqual(job_count([]),0)'),('items_not_characters','jobs=["a long job name"]\nself.assertEqual(job_count(jobs),1)\nself.assertEqual(jobs,["a long job name"])')],
        'The same len tool that counted string characters counts list items.',
        'Why does len(["backup"]) return one rather than six?',mode='function',teaches=['lists'],requires=['functions','indexing','builtin_results'])

    put('py196','Positions and pairs without manual counters','Use enumerate and zip after ordinary loops are familiar.',
        '''`enumerate(values, start=1)` supplies a position alongside each value. A for loop can unpack each pair into two names. This removes the need to initialize and increment your own counter. Choose whether positions start at zero or one according to the contract.

        `zip(left, right)` pairs corresponding values from two iterables. Normally it stops when the shorter input ends. When equal lengths are a requirement, `zip(..., strict=True)` can report a mismatch rather than silently dropping unmatched values.

        The example pairs each job name with a duration and then collects those pairs into a list. We will keep equal-length inputs here. You already know loops, tuples and list append, so the new idea is which values these two tools provide.

        Order still matters. Do not sort a collection when its original correspondence is meaningful. Pip paired the newest invoice with the oldest customer because both looked lonely. Corresponding positions are a better rule.''',
        'pairs = []\nfor name, seconds in zip(["email", "backup"], [2, 5]):\n    pairs.append((name, seconds))\n# [("email", 2), ("backup", 5)]',
        'Implement numbered_jobs(names), returning (position, name) tuples starting at one in original order. Include empty names; empty input returns []. Use enumerate for the positions.',
        'def numbered_jobs(names):\n    pass',
        'def numbered_jobs(names):\n    result = []\n    for position,name in enumerate(names,1):\n        result.append((position,name))\n    return result',
        [('positions','self.assertEqual(numbered_jobs(["a","b"]),[(1,"a"),(2,"b")])'),('empty_names','self.assertEqual(numbered_jobs(["", "x"]),[(1,""),(2,"x")])\nself.assertEqual(numbered_jobs([]),[])')],
        'Unpack position and name from enumerate(names, 1), then append their tuple.',
        'Why can zip silently lose an unmatched last item?',mode='function',teaches=['enumeration'],requires=['loops','lists','tuples'])

    put('py180','Split the message, join the pieces','Use lists of words as the bridge between text and collection processing.',
        '''The string method `split()` breaks text on whitespace and returns a list of words. With no separator argument it treats runs of spaces, tabs and line breaks as separators and omits empty pieces. `split(",")` instead splits on literal commas and can preserve empty fields.

        To go in the other direction, call `separator.join(parts)`. The separator string supplies the text placed between members. For example, `"-".join(["night", "shift"])` produces night-shift. It does not put a dash at either end.

        This method returns a new string; neither the input text nor an existing list is edited. The list members must be strings. Use a real parser for formats with quoting rules, such as CSV, which we will study later.

        This lesson waits until lists and loops are familiar, so a list of pieces is no mystery. Pip has been splitting logs with scissors. The digital version leaves less confetti.''',
        'parts = "  night   shift  ".split()\nlabel = "-".join(parts)\nprint(label)',
        'Implement dash_words(text), returning its whitespace-separated words joined with one dash. Preserve word spelling and case. All-whitespace or empty text returns an empty string.',
        'def dash_words(text):\n    pass',
        'def dash_words(text):\n    return "-".join(text.split())',
        [('spaces','self.assertEqual(dash_words("  Night   Shift  "),"Night-Shift")'),('other_whitespace','self.assertEqual(dash_words("a\\nb\\tc"),"a-b-c")'),('empty','self.assertEqual(dash_words(" "),"")\nself.assertEqual(dash_words(""),"")')],
        'Call split() with no argument, then use "-".join on the returned list.',
        'How would split(" ") behave differently for repeated spaces?',mode='function',requires=['methods','lists','strings'])

    put('py199','Borrow a tool from the standard library','Explain import and module-qualified calls before files or JSON.',
        '''A **module** is a Python file or library unit that groups reusable definitions. Python's **standard library** comes with the language and includes tools for mathematics, dates, structured data and more. An import makes a module available under a name in your program.

        `import math` gives you the module name math. A dot selects one of its tools, so `math.ceil(value)` rounds upward to a whole number. The import does not copy its source into your editor or require a package download. Standard-library imports work on the course laptop already.

        Another form, `from math import ceil`, binds that particular tool directly to the name ceil. Keep import style consistent so readers can tell where a definition comes from. Avoid a wildcard import in application code when it makes names ambiguous.

        You have used methods after dots too; the shape is familiar, but math is a module here. Pip attempted to import coffee. Python reports that module is not installed.''',
        'import math\n\nprint(math.ceil(2.3))\n# This prints 3.',
        'Import math. Keep seconds = 2.2, assign math.ceil(seconds) to billed_seconds, and print billed_seconds. The result should be 3.',
        'seconds = 2.2\n# Import math, calculate billed_seconds and print it.',
        'import math\n\nseconds = 2.2\nbilled_seconds = math.ceil(seconds)\nprint(billed_seconds)',
        [('value','self.assertEqual(self.state.get("billed_seconds"),3)'),('output','self.assertEqual(self.output,"3\\n")')],
        'Use import math before calling math.ceil(seconds).',
        'Which name identifies the module and which identifies its tool?',teaches=['modules'],requires=['methods','variables','types'])

    put('py200','Keep a helper in another module','Import a provided local module instead of duplicating its rule.',
        '''Your own modules use the same import system as library modules. A file named fees.py can define packaging_fee; another file in the same project can use `from fees import packaging_fee`. The `.py` extension belongs in the filename, not the import statement.

        This mission supplies fees.py alongside your script. Its contents are `def packaging_fee(): return 15`, written on normal indented lines. You only edit main.py. Importing the helper gives the caller a reusable rule with one home rather than another copied constant.

        Defining a function inside an imported module does not call it. The caller still needs parentheses to run that function and obtain its result. Keep module-level side effects limited: importing a helper should not unexpectedly send messages or launch an application.

        In a larger project you might organize modules into packages, but a local pair of files is enough to understand this boundary. Pip copied a fee rule into every file and then changed only half the copies. Finance is requesting one source of truth.''',
        '# fees.py provides packaging_fee(). In the caller:\nfrom fees import packaging_fee\n\nprint(packaging_fee())',
        'Use the provided fees module. Keep subtotal = 100. Assign subtotal + packaging_fee() to total and print total. Do not replace the helper call with a copied fee number. Expected output: 115.',
        'from fees import packaging_fee\n\nsubtotal = 100\n# Call the helper, calculate total and print it.',
        'from fees import packaging_fee\n\nsubtotal = 100\ntotal = subtotal + packaging_fee()\nprint(total)',
        [('total','self.assertEqual(self.state.get("total"),115)'),('output','self.assertEqual(self.output,"115\\n")')],
        'The imported function still needs parentheses when you use its result.',
        'What is the difference between importing a function and calling it?',requires=['modules','functions','returns'],fixtures={'fees.py':'def packaging_fee():\n    return 15\n'})

    put('py201','Run a script without surprising its importer','Use the __name__ guard after functions and imports are understood.',
        '''Python supplies a module-level name called `__name__`. When a file is executed as the entry script, that name has the value `"__main__"`. When the file is imported normally, it has its module name instead.

        The familiar if syntax can use this difference: `if __name__ == "__main__":` guards the code that should run only for direct execution. Definitions remain available for import, while the guarded action stays quiet. The double underscores are part of the exact supplied name.

        A small main function makes the entry behavior easy to find. Defining main does not run it; the call inside the guard does. This is useful when a test or another program imports your helper functions.

        The example prints Started when run directly and prints nothing merely because somebody imports the module. Pip's last utility launched a countdown every time it was imported. The test suite now flinches at imports.''',
        'def main():\n    print("Started")\n\nif __name__ == "__main__":\n    main()',
        'Define main() to print Ready. Call it only under if __name__ == "__main__". Running the script must print Ready once; importing it under a different module name must not print anything.',
        'def main():\n    print("Ready")\n\n# Add the entry guard and call here.',
        'def main():\n    print("Ready")\n\nif __name__ == "__main__":\n    main()',
        [('direct','self.assertEqual(self.output,"Ready\\n")'),('quiet_import','with redirect_stdout(StringIO()) as output:\n    imported = runpy.run_path(str(Path(__file__).with_name("main.py")),run_name="quiet_import")\nself.assertEqual(output.getvalue(),"")\nself.assertTrue(callable(imported.get("main")))')],
        'Use the existing if/== syntax to compare __name__ with the string "__main__".',
        'Why should importing a reusable module not execute its command-line workflow?',requires=['modules','functions','branches','comparisons'])

    put('py203','Pass a tool without running it yet','Use a function as a value before callbacks, lambdas or pipelines.',
        '''A function is a value you can pass to another function. Writing its name refers to the tool; adding parentheses calls it. In `apply_once(4, double)`, double is supplied for later use. In `double(4)`, it runs now and produces a result.

        A function received for the caller to invoke is often called a **callback**. The receiving function can use any suitable callable rather than hardcoding one particular operation. Its contract must say which inputs it will pass and how often it will call the tool.

        In the example, apply_once gets the number four and a reference to double. It calls double with four and returns eight. A different supplied operation can reuse the same wrapper. No new anonymous-function syntax is needed yet.

        Do not silently call a callback twice or discard its returned value. Side effects and expensive operations would then happen twice too. Pip repeatedly presses the doorbell to confirm the doorbell works. Our contract says once.''',
        'def double(number):\n    return number * 2\n\ndef apply_once(value, operation):\n    return operation(value)\n\nprint(apply_once(4, double))',
        'Implement apply_once(value, operation). Call operation(value) exactly once and return its result unchanged. Propagate its errors. Do not guess the operation from the input type.',
        'def apply_once(value, operation):\n    pass',
        'def apply_once(value, operation):\n    return operation(value)',
        [('callback','operation=Mock(return_value=9)\nself.assertEqual(apply_once(4,operation),9)\noperation.assert_called_once_with(4)'),('different_types','self.assertEqual(apply_once("hi",str.upper),"HI")'),('propagates','operation=Mock(side_effect=ValueError("no"))\nwith self.assertRaisesRegex(ValueError,"no"):\n    apply_once(1,operation)')],
        'Use operation as a function name and put value inside its call parentheses.',
        'Why is passing double different from passing double(4)?',mode='function',teaches=['callbacks'],requires=['functions','returns'])

    put('py204','A small anonymous sorting rule','Introduce lambda and key functions before using them in reports.',
        '''A **lambda** creates a small function from one expression: `lambda item: item["score"]`. Parameters go after lambda and the expression goes after its colon. The expression's result is returned automatically. Use a named def when several statements or a useful descriptive name would be clearer.

        `sorted(items, key=...)` calls the supplied key function for each item and orders by those key values. It returns a new list instead of changing the original order. The callback concept is the same one you just practiced.

        A tuple key gives a tie-breaker: `(score, name)` sorts by score first and then name. Negating a numeric score can make that part descending while the name stays ascending. You will use that pattern in the next mission.

        Keep these rules readable. Lambda is a convenience, not a requirement to squeeze a whole program onto one line. Pip sorted reports by the number of exclamation marks. We are specifying the key.''',
        'records = [{"name":"B","score":2},{"name":"A","score":1}]\nordered = sorted(records, key=lambda record: record["score"])',
        'Implement sort_by_name(records), returning a new list sorted by each record\'s "name" string ascending. Keep records and their dictionaries unchanged; references to the same records may be reused in this task.',
        'def sort_by_name(records):\n    pass',
        'def sort_by_name(records):\n    return sorted(records,key=lambda record:record["name"])',
        [('order','self.assertEqual(sort_by_name([{"name":"B"},{"name":"A"}]),[{"name":"A"},{"name":"B"}])'),('new_list','records=[{"name":"B"},{"name":"A"}]\nresult=sort_by_name(records)\nself.assertEqual(records,[{"name":"B"},{"name":"A"}])\nself.assertIsNot(result,records)'),('empty','self.assertEqual(sort_by_name([]),[])')],
        'Pass a small function as key, selecting record["name"].',
        'When would a named def make a key function easier to read?',mode='function',teaches=['lambdas'],requires=['callbacks','dictionaries','tuples'])

    put('py207','Unpack inputs without guessing the signature','Use * and ** to pass tuple and dictionary arguments.',
        '''A call can unpack positional arguments from an iterable with `*args` and keyword arguments from a mapping with `**kwargs`. Here the stars are call syntax, not multiplication or exponentiation. The argument container types and position make the meaning clear.

        The matching function-definition forms collect extra arguments: `def wrapper(*args, **kwargs)` receives a tuple of positional values and a dictionary of keyword values. Those names are conventions, not mandatory spellings. This is useful when a wrapper should forward a call without knowing every parameter in advance.

        In the example, the tuple supplies the first argument and the dictionary supplies a named argument. The receiving function still applies its normal signature rules; unpacking does not make invalid arguments valid.

        Keep the forwarded call exact, including empty containers. The next lesson uses this to wrap a function with extra behavior. Pip forwards every request with an extra biscuit parameter. Most interfaces do not accept it.''',
        'def add(left, right=0):\n    return left + right\n\nargs = (3,)\nkwargs = {"right":4}\nprint(add(*args, **kwargs))',
        'Implement forward_call(operation, args, kwargs). Return operation(*args, **kwargs), preserving the arguments and propagating failures. args is a tuple and kwargs is a dict of keyword arguments.',
        'def forward_call(operation, args, kwargs):\n    pass',
        'def forward_call(operation, args, kwargs):\n    return operation(*args,**kwargs)',
        [('forwarded','operation=Mock(return_value="ok")\nself.assertEqual(forward_call(operation,(1,),{"x":2}),"ok")\noperation.assert_called_once_with(1,x=2)'),('empty','self.assertEqual(forward_call(lambda:7,(),{}),7)'),('unchanged','args,kwargs=(1,),{"x":2}\nforward_call(Mock(),args,kwargs)\nself.assertEqual(args,(1,))\nself.assertEqual(kwargs,{"x":2})')],
        'Use one star before args and two before kwargs inside the call.',
        'How is *args inside a call different from *args in a definition?',mode='function',teaches=['argument_unpacking'],requires=['callbacks','tuples','dictionaries'])

    put('py205','Wrap a function without changing its job','Combine closures and forwarding to build a decorator.',
        '''A **decorator** takes a function and returns a replacement function with additional behavior. The original calculation can remain focused on its own job while the wrapper adds logging, measurement or validation. This builds on callbacks, closures and argument forwarding you have already practiced.

        In `@decorate` above a function definition, Python applies the decorator and binds the resulting callable to that function's name. It is shorthand for `function = decorate(function)`. A wrapper usually accepts *args and **kwargs so it can forward the original call.

        `functools.wraps(original)` copies useful metadata such as __name__ onto the wrapper. It does not execute the original function. Append the log entry once, call the original once, and return its result; losing the return value is a common wrapper bug.

        We are writing a small logging decorator, not a production logging framework. Avoid recording secrets in real call logs. Pip logs that it is logging the logging function. Your wrapper should be less enthusiastic.''',
        'from functools import wraps\n\ndef announce_calls(operation):\n    @wraps(operation)\n    def wrapped(*args, **kwargs):\n        print("calling")\n        return operation(*args, **kwargs)\n    return wrapped',
        'Implement logged(operation, history). Return a wrapper preserving operation.__name__. Each call appends its positional args tuple to history, calls operation once with all positional and keyword arguments, and returns its result. Let errors propagate; their calls must still be logged.',
        'from functools import wraps\n\ndef logged(operation, history):\n    pass',
        'from functools import wraps\n\ndef logged(operation, history):\n    @wraps(operation)\n    def wrapped(*args, **kwargs):\n        history.append(args)\n        return operation(*args, **kwargs)\n    return wrapped',
        [('wrapped_call','history=[]\ndef add(a,b=0):\n    return a+b\nwrapped=logged(add,history)\nself.assertEqual(wrapped(3,b=4),7)\nself.assertEqual(history,[(3,)])\nself.assertEqual(wrapped.__name__,"add")'),('repeat','history=[]\noperation=Mock(return_value=2)\noperation.__name__="operation"\nwrapped=logged(operation,history)\nwrapped(1)\nwrapped(0)\nself.assertEqual(history,[(1,),(0,)])\nself.assertEqual(operation.call_count,2)'),('failed_call_logged','history=[]\ndef fail(value):\n    raise ValueError("offline")\nwith self.assertRaisesRegex(ValueError,"offline"):\n    logged(fail,history)(7)\nself.assertEqual(history,[(7,)])')],
        'Create an inner wrapper, decorate it with wraps(operation), then return it.',
        'Why must the wrapper return the original function\'s result?',mode='function',teaches=['decorators'],requires=['closures','argument_unpacking','callbacks','modules'])

    put('py206','Manage a resource with with','Implement the context-manager protocol after classes and cleanup are familiar.',
        '''A **context manager** defines what happens on entry to and exit from a `with` block. Python calls its __enter__ method, runs the body, and calls __exit__ when leaving, including when the body raises. It packages the try/finally cleanup pattern into a reusable object.

        The value returned by __enter__ is assigned to the name after `as`. On a normal exit, __exit__ receives three None values. On failure it receives the exception type, value and traceback. Return False to let an exception continue outward; returning True would suppress it.

        The two double-underscore names are special protocol hooks: Python calls them at the defined moments. You still write ordinary methods using self and the parameter rules you know. Validate the resource state inside and after a block to see that cleanup actually occurs.

        File objects already implement this protocol, which makes the next chapter's file handling easier to understand. Pip would like a context manager for meetings that guarantees everyone leaves. We are starting with a simpler flag.''',
        '# A manager with these methods supports:\n# with manager as resource:\n#     use(resource)\n# __enter__ supplies resource; __exit__ performs cleanup.',
        'Implement ManagedFlag. It starts with active=False. __enter__ sets active=True and returns self. __exit__(exc_type, exc, traceback) sets active=False and returns False, so errors propagate. Reusing the same instance for sequential blocks is allowed.',
        'class ManagedFlag:\n    def __init__(self):\n        pass\n    def __enter__(self):\n        pass\n    def __exit__(self, exc_type, exc, traceback):\n        pass',
        'class ManagedFlag:\n    def __init__(self):\n        self.active=False\n    def __enter__(self):\n        self.active=True\n        return self\n    def __exit__(self, exc_type, exc, traceback):\n        self.active=False\n        return False',
        [('normal','flag=ManagedFlag()\nself.assertIs(flag.active,False)\nwith flag as resource:\n    self.assertIs(resource,flag)\n    self.assertIs(flag.active,True)\nself.assertIs(flag.active,False)'),('error','flag=ManagedFlag()\nwith self.assertRaisesRegex(ValueError,"oops"):\n    with flag:\n        raise ValueError("oops")\nself.assertIs(flag.active,False)'),('reuse','flag=ManagedFlag()\nwith flag:\n    pass\nwith flag:\n    self.assertTrue(flag.active)\nself.assertFalse(flag.active)')],
        'The entry method returns self; the exit method restores the flag and returns False.',
        'What dangerous behavior would returning True from __exit__ introduce?',mode='function',teaches=['context_managers'],requires=['classes','exception_handling','booleans'])

    put('py208','Make a tiny database before building storage','Use an in-memory SQLite table, bound parameters and fetched rows.',
        '''SQLite is a database available through Python's standard-library sqlite3 module. `sqlite3.connect(":memory:")` creates a temporary database for this connection. SQL statements describe operations on tables: CREATE TABLE defines columns, INSERT adds rows, and SELECT reads them.

        `connection.execute(sql, parameters)` binds data through ? placeholders. Keep user values out of the SQL string itself. A one-item parameter tuple needs a comma: `(name,)`. Parentheses alone would still contain a string. The returned cursor's fetchall() gives a list of row tuples.

        Use ORDER BY when a result needs a guaranteed order. Closing the connection releases it; a connection's own with block manages transactions and does not itself close the connection. Here a try/finally closes the temporary database regardless of errors. Later storage tasks use persistent connections supplied by callers.

        This is a small bridge into storage, not an entire SQL course. Pip's previous database was a list written on a sandwich wrapper. Parameter binding is an upgrade.''',
        'import sqlite3\n\nconn = sqlite3.connect(":memory:")\ntry:\n    conn.execute("CREATE TABLE workers (id INTEGER PRIMARY KEY, name TEXT)")\n    conn.execute("INSERT INTO workers(name) VALUES (?)", ("Pip",))\n    rows = conn.execute("SELECT name FROM workers ORDER BY id").fetchall()\nfinally:\n    conn.close()',
        'Implement roundtrip_names(names). Open an in-memory SQLite database, store each supplied name using bound parameters, read names back in insertion order, and return them as strings in a list. Preserve duplicates and punctuation. Close the connection before returning.',
        'import sqlite3\n\ndef roundtrip_names(names):\n    pass',
        'import sqlite3\n\ndef roundtrip_names(names):\n    conn=sqlite3.connect(":memory:")\n    try:\n        conn.execute("CREATE TABLE workers (id INTEGER PRIMARY KEY, name TEXT)")\n        for name in names:\n            conn.execute("INSERT INTO workers(name) VALUES (?)",(name,))\n        return [row[0] for row in conn.execute("SELECT name FROM workers ORDER BY id").fetchall()]\n    finally:\n        conn.close()',
        [('order_duplicates','self.assertEqual(roundtrip_names(["B","A","B"]),["B","A","B"])'),('data_not_sql','names=["Pip\'s desk", "x\'); DROP TABLE workers;--"]\nself.assertEqual(roundtrip_names(names),names)'),('empty','self.assertEqual(roundtrip_names([]),[])')],
        'Bind each (name,) to one ? placeholder, then read row[0] from each fetched row.',
        'Why must a customer name be bound as data instead of inserted into the SQL text?',mode='function',requires=['modules','context_managers','exception_handling','loops','comprehensions'])

    lessons['py186']['teaching'] += '\n\nIf a function finishes without a return statement, its result is `None`, Python\'s marker for no value. A provided `pass` line is a placeholder that does nothing; replace it with the instructions required by the mission.'
    lessons['py186']['teaches'].append('none')
    lessons['py200']['checks'].append(('uses_imported_rule','with patch("fees.packaging_fee",return_value=7):\n    with redirect_stdout(StringIO()):\n        state=runpy.run_path(str(Path(__file__).with_name("main.py")),run_name="__main__")\nself.assertEqual(state.get("total"),107,"Call the helper instead of copying its current fee value.")'))
    lessons['py206']['example']='class Visit:\n    def __enter__(self):\n        print("open")\n        return self\n    def __exit__(self, *details):\n        print("close")\n        return False\n\nwith Visit():\n    print("work")'

    additions={
      'py109':'This is the first **function challenge**, rather than a whole script. The editor provides the definition line; the checks call your function with several inputs. You do not need a call at the bottom of this file. Replace `pass`, the do-nothing placeholder, with a return statement. Printed text is not the requested result.',
      'py112':'The comma creates the tuple. Unpacking assigns its first and second members to the two caller names. A one-item tuple needs a trailing comma, such as `(7,)`; `(7)` alone is just a parenthesized integer.',
      'py120':'In the buggy starter, `global AUDIT_TOTAL` explicitly directs assignments to the module-level name. That is precisely the shared state we do not want for this per-request sum. Remove the global write and initialize a local total inside each call.',
      'py122':'The built-in `min(left, right)` returns the smaller of two values. The `**` operator raises a number to a power: `2 ** 0` is one, `2 ** 1` is two, and `2 ** 2` is four. These are arithmetic operations, not argument-unpacking syntax.',
      'py124':'The built-in `abs(number)` returns its distance from zero, so both abs(-3) and abs(3) are three. Applying it to actual - expected measures the size of the difference without depending on which number is larger.',
      'py130':'The built-in `max(left, right)` returns the larger value. Using max(0, remaining - capacity) prevents the remaining count from going below zero when a final batch has spare room.',
      'py137':'A dictionary literal uses `{key: value}` pairs, separated by commas. The colon connects a key to its value. `mapping.keys()` provides the keys, `mapping.values()` the values, and `mapping.items()` the key/value pairs. Choose the view that matches the question you are answering.',
      'py138':'In a dictionary display, `**mapping` expands all key/value pairs from that mapping. This is not exponentiation: it appears where dictionary entries belong. Later entries replace earlier entries with the same key.',
      'py149':'The built-in `sum(values)` adds the numeric members of an iterable; for an empty list it returns zero. Guard the empty case before dividing by len(values), because a valid empty mean is a contract decision rather than a division by zero.',
      'py162':'The `@property` line asks Python to expose the following getter method as an attribute-like read. It is a built-in decorator: a standard transformation applied to the method definition. There is no setter here, so ordinary assignment to balance is rejected. General-purpose decorators come later.',
      'py164':'The `@dataclass(frozen=True)` line applies a standard-library decorator to the class below it. It generates record behavior from the annotated fields. You do not need to write a decorator yourself yet; the advanced patterns chapter explains that general mechanism.',
      'py168':'The built-in iter(collection) supplies an iterator and next(iterator) asks for its next value. A generator expression such as `(value * 2 for value in values)` is the lazy counterpart of a list comprehension: it yields results on demand rather than constructing a full list.',
      'py170':'The built-in `any(conditions)` is True when at least one supplied condition is truthy. A generator expression can supply validation conditions one at a time, stopping as soon as an invalid member is found.',
      'py172':'A coroutine is not a background thread. Awaiting it gives the event loop a chance to run other ready asynchronous work. The supplied fetch function already follows that async contract, so the exercise needs no live network access.',
    }
    for ident,text in additions.items():
        lessons[ident]['teaching'] += '\n\n'+text

    # Reading revisions: short sections, explicit contracts, and original diagrams.
    lessons['py101']['teaching']+='\n\n> [!TIP]\n> Change <mark>only the text inside the quotes</mark>. Keep the tool name and punctuation in place.'
    lessons['py101']['example_output']='Service online\n'
    lessons['py101']['task']=cleandoc('''Make the greeting say **Helpdesk online!**:

        - Replace the text between the quotes.
        - Keep `print`, the matching quotes, and both parentheses.
        - Press **Run**. The console should show your greeting on one line.''')
    lessons['py195']['teaching']=cleandoc('''A **list** keeps related values together, in order. Think of it as a row of boxes, with one value in each box.

        <figure class="list-picture" aria-label="The list jobs contains backup, email and report: three items.">
        <figcaption><strong>jobs</strong><span>One list, three items</span></figcaption>
        <div class="list-items"><code>"backup"</code><span aria-hidden="true">,</span><code>"email"</code><span aria-hidden="true">,</span><code>"report"</code></div>
        </figure>

        ## Write a list

        - Put **square brackets** `[ ]` around the values.
        - Use a **comma** between items.
        - Give the collection a name, such as `jobs`.

        ## Count the items

        `len(jobs)` tells you how many items the list holds. An empty list, `[]`, has a length of **0**.

        > [!TIP]
        > <mark>Count items, not letters.</mark> A list containing only `"backup"` has **one item**, even though that word has six letters.''')
    lessons['py195']['example']='jobs = ["backup", "email", "report"]\nprint(len(jobs))'
    lessons['py195']['example_output']='3\n'
    lessons['py133'].update(goal='Pick the first and last items without going past the ends.',teaching=cleandoc('''An **index** is an item's position. Python starts counting positions at **0**.

        <figure class="list-picture" aria-label="backup is at index zero, email at index one, and report at index two.">
        <figcaption><strong>jobs</strong><span>Positions start at zero</span></figcaption>
        <div class="index-map"><div class="index-item"><span>Index 0</span><code>"backup"</code></div><div class="index-item"><span>Index 1</span><code>"email"</code></div><div class="index-item"><span>Index 2</span><code>"report"</code></div></div>
        </figure>

        ## Pick one item

        - `jobs[0]` selects the **first** item.
        - `jobs[-1]` selects the **last** item.
        - The last positive index is `len(jobs) - 1`.

        > [!WARNING]
        > <mark>Check for an empty collection before indexing.</mark> An empty list has no first or last item. An invalid index raises `IndexError`.

        ## Lists and tuples

        Both support indexes and `len`. A list can grow or have items replaced; a tuple's existing items cannot be reassigned. A list inside a tuple can still change.

        **First and last describe the original order.** They do not mean smallest and largest.'''),example='jobs = ["backup", "email", "report"]\nprint(jobs[0])\nprint(jobs[-1])',example_output='backup\nreport\n',task=cleandoc('''Complete `endpoints(values)`:

        - Return `(first, last)` for a list or tuple.
        - Return `None` when it is empty.
        - For one item, return that item twice.
        - Keep the original order and leave the input unchanged.'''))
    lessons['py134'].update(goal='Take part of a list and understand where the slice stops.',teaching=cleandoc('''A **slice** selects part of a collection. Write it as `values[start:stop]`.

        <figure class="list-picture" aria-label="values one to three selects twenty and thirty. Index three is excluded.">
        <figcaption><strong>values[1:3]</strong><span>Keep the highlighted values</span></figcaption>
        <div class="slice-cells"><div><span>0</span><code>10</code></div><div class="is-selected"><span>1</span><code>20</code></div><div class="is-selected"><span>2</span><code>30</code></div><div><span>3</span><code>40</code></div></div>
        </figure>

        ## Read the boundaries

        - **start is included:** begin at that index.
        - **stop is excluded:** finish just before that index.
        - Omit an end to continue to the edge of the collection.

        > [!TIP]
        > <mark>Start here; stop before there.</mark> `values[1:3]` selects indexes **1 and 2**.

        ## Steps and copies

        A third value controls the step: `values[start:stop:step]`. A step of `-1` walks backward; a step of `0` is invalid.

        A list slice creates a **new outer list**. Nested objects are still shared. Bounds beyond an edge are clipped to the available items.

        ## The zero-item case

        `-0` is still `0`. That makes `values[-0:]` the same as `values[0:]`: the whole list. Handle a requested count of **0** separately.'''),example='values = [10, 20, 30, 40]\nprint(values[1:3])\nprint(values[::-1])',example_output='[20, 30]\n[40, 30, 20, 10]\n',task=cleandoc('''Complete `recent_items(values, count)`. `count` is a non-negative integer.

        - Return a **new list** containing the last `count` items, in their original order.
        - Return `[]` when `count` is `0`.
        - When `count` exceeds the length, return a shallow copy of the full list.
        - Leave the input unchanged.'''))
    lessons['py135'].update(goal='Add and remove list items while protecting the caller\'s list.',teaching=cleandoc('''List methods can **change the list itself**. This is called **mutation**.

        ## Two useful methods

        - `append(value)` adds one item at the **end**. It returns `None`.
        - `pop(index)` **removes and returns** an item.
        - `pop()` with no index removes the **last** item. `pop(0)` removes the **first**.

        ## Serve a queue

        A queue serves the oldest arrival first. For this small exercise, `pop(0)` picks that first item.

        > [!IMPORTANT]
        > <mark>Copy before changing the caller's list.</mark> `list(waiting)` makes a new outer list. Change that copy so the caller keeps its original collection.

        `pop(0)` shifts the remaining items. For large, real queues, `collections.deque` provides efficient removal from the front.

        **Remember the return value:** `append` changes the list but returns `None`. It does not return the updated collection.'''),example='waiting = ["backup", "email"]\nremaining = list(waiting)\nserved = remaining.pop(0)\n\nprint(served)\nprint(remaining)\nprint(waiting)',example_output="backup\n['email']\n['backup', 'email']\n",task=cleandoc('''Complete `serve_next(waiting)`:

        - Return `(oldest_item, remaining_list)`.
        - Leave `waiting` unchanged.
        - Return a **different list object** for the remaining items.
        - For an empty input, return `(None, [])`.'''))

    # These introductions are explicit claims, checked against learner-visible syntax.
    introduces={
      'py112':['tuples'], 'py125':['logic'], 'py126':['branches'],
      'py120':['global_state'], 'py122':['powers'], 'py123':['bitwise'],
      'py129':['loops'], 'py130':['while_loops'], 'py131':['loop_control'],
      'py134':['slicing'], 'py135':['list_methods'], 'py136':['comprehensions'],
      'py137':['dictionaries'], 'py138':['mapping_unpacking'], 'py141':['sets'], 'py142':['set_operations'],
      'py145':['raising'], 'py146':['exception_handling'], 'py147':['cleanup'],
      'py149':['annotations'], 'py161':['classes'], 'py162':['properties'],
      'py163':['inheritance'], 'py164':['dataclasses'], 'py168':['generators'],
      'py167':['recursion'], 'py116':['closures'], 'py172':['async'],
    }
    for ident,features in introduces.items():
        lessons[ident].setdefault('teaches',[]).extend(features)
    # An authoring placeholder must not introduce exception syntax before errors are taught.
    import re
    for item in lessons.values():
        item.setdefault('execution_mode','function')
        if item['execution_mode']=='function':
            item['starter']=re.sub(r'^(\s*)raise NotImplementedError.*$',r'\1pass',item['starter'],flags=re.M)
        item.setdefault('teaches',[])
        item.setdefault('requires',[])
        item['content_revision']=2
        item['source_filename']='main.py' if item['execution_mode']=='script' else 'challenge.py'
    ordered=[ident for _,_,ids in PATH for ident in ids]
    assert len(ordered)==len(set(ordered)), 'Duplicate lesson placement'
    legacy={f'py{number:02}' for number in range(1,13)}
    assert set(ordered)==set(lessons)|legacy,(set(lessons)-set(ordered),set(ordered)-set(lessons)-legacy)
    for chapter,(title,level,ids) in enumerate(PATH,1):
        for ident in ids:
            if ident in lessons:
                lessons[ident].update(chapter=chapter,chapter_title=title,level=level)
    return lessons
