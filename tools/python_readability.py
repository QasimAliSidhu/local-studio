"""Small, curated reading steps for the complete Python learning path.

These are teaching summaries, not machine-generated sentence bullets. The original
explanation stays available in a disclosure after the unchanged worked example.
Task formatting preserves every word of the contract.
"""
from __future__ import annotations

import re


_READINGS = r'''
py102|Follow the lines in order
- **Start at the top.** Python runs these instructions one after another.
- **One print, one line.** Each ordinary `print(...)` ends with a newline in the console.
- **Code and output have different jobs.** Write the instructions in the editor; read their results in the console.

py103|Tell text and comments apart
- **Match the outer quotes.** A string can use single quotes or double quotes; the opening and closing kind must match.
- **Choose the convenient kind.** Single outer quotes let you include double quotes inside your message.
- **Notice where `#` sits.** Outside a string it starts an ignored comment. Inside a string it is text that prints.

py104|Ask Python to calculate
- **Without quotes, use numbers.** `7 + 2` is an expression that evaluates to `9`.
- **Inside quotes, keep the text.** `"7 + 2"` is a string containing those characters.
- **Print the result.** `print(7 + 2)` calculates first, then displays the answer.

py105|Give each value a name
- **Assign with `=`.** `minutes = 3` makes the name `minutes` refer to the value `3`.
- **Calculate the right side first.** In `seconds = minutes * 60`, `*` multiplies before the result is assigned.
- **Use the name without quotes.** `print(seconds)` displays its value; `print("seconds")` displays the word.

py173|Update a value in three steps
- **Read the old value.** In `jobs = jobs + 1`, the right-hand `jobs` means the value already stored.
- **Calculate, then assign.** Add one, then make `jobs` refer to that result.
- **Trace each print at its own line.** An earlier printed result stays the same when the variable changes later. Names are case-sensitive.

py174|Recognize the kind of value
- **`int` means a whole number.** `12` is an integer; `1.5` is a decimal value of type `float`.
- **`str` means text.** `"12"` stays a string even though it looks numeric. `type(value)` reports the type.
- **Let the type explain `+`.** Two numbers add; two strings join. Combining text and a number needs an explicit conversion.

py181|Keep the calculation readable
- **Multiply with `*`; divide with `/`.** Ordinary division returns a float: `8 / 2` gives `4.0`.
- **Group with parentheses.** Multiplication and division happen before addition and subtraction unless you group another part first.
- **Name the units.** Dividing `jobs` by `seconds` gives jobs per second. The divisor must not be zero.

py182|Separate full groups from leftovers
- **Count full groups with `//`.** For these non-negative inputs, `14 // 6` gives `2` complete boxes.
- **Find leftovers with `%`.** `14 % 6` gives `2` items left over.
- **Check the relationship.** `full_boxes * size + loose_items` should equal the original count. The box size must be positive.

py175|Keep the value a tool returns
- **Call `len(text)` to count characters.** Spaces count too; an empty string has length `0`.
- **Store the return value.** `characters = len(message)` gives the numeric result a name.
- **Use that result next.** Print it or calculate with it. Receiving a result does not require writing your own `return` statement yet.

py191|Read a character by position
- **Start at zero.** In `"Pip"`, index `0` is `P`, index `1` is `i`, and index `2` is `p`.
- **Select with square brackets.** `name[0]` gets the first character; `name[-1]` gets the last.
- **Stay inside the string.** An unavailable position raises `IndexError`. Reading an index leaves the original text unchanged.

py176|Trim the outside, keep the inside
- **Call a method after a dot.** `raw.strip()` asks the string to remove whitespace from both ends.
- **Keep the returned text.** Strings are immutable: assign the result to `clean`; `raw` stays unchanged.
- **Keep internal spaces.** `strip()` removes outside spaces, tabs and line breaks, rather than every space in the message.

py177|Make a lowercase copy
- **Call `status.lower()`.** The dot finds the method; the parentheses run it.
- **Use the returned result.** Assign it to a new name. The original string stays unchanged.
- **Change case deliberately.** Numbers and punctuation stay in place. Lowercasing is appropriate for this label, not every kind of text.

py106|Clean the text in a clear order
- **Trim first.** `strip()` removes whitespace at the edges.
- **Normalize the case.** `lower()` makes a lowercase result; chaining passes each returned string to the next method.
- **Replace each internal space.** `replace(" ", "_")` makes two spaces become two underscores. These methods leave the original string unchanged.

py178|Put a value inside text
- **Start with `f`.** An f-string begins like `f"Worker {name}"`.
- **Put expressions inside braces.** `{name}` inserts the variable's current value; text outside braces stays literal.
- **Let Python display numbers.** You can insert several values without converting each one to a string yourself.

py107|Choose how a number looks
- **Keep the value inside braces.** An f-string inserts expressions into a message.
- **Add the display rule after a colon.** `f"{rate:.2f}"` displays two digits after the decimal point.
- **Separate display from arithmetic.** `2.5` can appear as `2.50` in the message while the numeric variable stays unchanged.

py108|Convert before calculating
- **Recognize numeric text.** `"8"` is still a string; joining it with `"2"` produces `"82"`.
- **Call `int(raw)`.** Valid whole-number text becomes an integer you can calculate with.
- **Keep the original if needed.** Assign the converted value to `count`. Invalid integer text raises `ValueError`.

py184|Define first, then call
- **Begin with `def`.** `def greet():` names a function. The colon starts its body.
- **Indent the instructions.** The indented lines belong to the function; defining them does not run them yet.
- **Call with parentheses.** An unindented `greet()` runs the body once. Define it before the call.

py185|Give the same function different inputs
- **Name a parameter in the definition.** In `def greet(name):`, `name` is the input name used inside the body.
- **Supply an argument in a call.** `greet("Mira")` makes `name` refer to `"Mira"` during that call.
- **Use the supplied value.** Build the greeting from `name` so the same body works for another caller too.

py186|Return a result to the caller
- **Use `return` for a result.** The caller can store that value, calculate with it or print it.
- **Keep printing separate.** Printing displays text in the console; it does not supply the function's return value.
- **Stop at `return`.** It ends the current call. Reaching the end without one returns `None`; `pass` is only a do-nothing placeholder.

py109|Describe the result before coding
- **Read the supplied inputs.** Multiply the quantity by the unit price to find the item cost.
- **Apply the order-level rule once.** A delivery fee belongs to the whole order, including an order with zero items.
- **Return from the provided function.** Replace `pass`; the checks call your function. Printing or adding a manual call is unnecessary here.

py110|Use defaults deliberately
- **Set a default in the definition.** `role="learner"` is used when the caller omits that argument.
- **Allow positional or named arguments.** Keyword arguments identify a parameter by its name.
- **Keep explicit values.** An empty string supplied by the caller is still a value; it does not mean the argument was omitted.

py111|Let each helper own one rule
- **Call the supplied helper.** `service_fee(subtotal)` calculates the fee from the current rule.
- **Combine named parts.** Add the subtotal, returned service fee and delivery charge.
- **Avoid copying the helper's formula.** Calling it keeps checkout correct when the service-fee rule changes.

py112|Return two related values
- **Make a tuple with a comma.** `return minutes, seconds_left` hands back one pair of values.
- **Unpack the pair in order.** The caller can assign its first and second values to separate names.
- **Remember the one-item form.** `(7,)` is a tuple; `(7)` is just the integer in parentheses. Use `//` and `%` for complete minutes and leftover seconds.

py179|Ask a question with an expression
- **Compare values with `==`.** The result is a boolean: `True` or `False`.
- **Use `>` to ask whether a number is greater.** Zero is equal to zero, but it is not greater than zero.
- **Check missing values with `is None`.** `None` represents no supplied value; it is different from a valid numeric zero.

py189|Choose one branch
- **Write a condition after `if`.** A true condition runs the indented instructions beneath it.
- **Use `else` for the other case.** Only the selected branch runs.
- **Keep the messages with the right condition.** Trace the supplied value first, then check which message belongs in that branch.

py125|Combine the admission rules
- **Use `or` for alternatives.** A ticket or staff status can satisfy the first rule.
- **Use `and` for requirements together.** Passing one rule is insufficient when another must also hold.
- **Use `not` to reverse a boolean.** Group the alternatives with parentheses, then apply the rule excluding a banned visitor.

py126|Put specific branches first
- **Test the largest threshold first.** A status of `503` also meets lower thresholds, so order matters.
- **Continue with `elif`.** Python runs the first matching branch in an `if` / `elif` / `else` chain.
- **Finish with the remaining case.** An `else` handles valid inputs that met none of the earlier thresholds.

py127|Guard before reading a character
- **Check the input first.** `None` and an empty string have no first character to inspect.
- **Use short-circuit evaluation.** With `and`, Python skips the right side when the left side is false.
- **Return a boolean.** `and` can return an operand rather than a literal bool, so make the function's result match its contract.

py128|Distinguish missing from empty
- **Check `is None` explicitly.** This asks whether no value was supplied.
- **Preserve other values.** `""`, `0`, `False` and `[]` can all be deliberate inputs.
- **Avoid an accidental fallback.** `supplied or fallback` replaces every falsy input, which is broader than this rule.

py124|Compare the size of the difference
- **Expect representation limits.** Some decimal fractions cannot be stored exactly as binary floats.
- **Use an absolute difference.** `abs(actual - expected)` measures distance without depending on which value is larger.
- **Include the boundary.** A difference equal to the tolerance qualifies; a tolerance of zero requires equality.

py121|Count all the boxes you need
- **Count full boxes with `//`.** The divisor is the positive capacity of one box.
- **Check leftovers with `%`.** Any remainder needs one additional box.
- **Test both edges.** Zero items need no boxes; an exact multiple needs no extra box.

py122|Build the calculation in stages
- **Raise with `**`.** `2 ** attempt` doubles the factor at each step, starting with `1` at attempt zero.
- **Multiply by the base.** Group the expression so its meaning stays clear.
- **Apply the cap with `min`.** `min(calculated, cap)` keeps the smaller value, including a cap of zero.

py187|Keep local and module names separate
- **A module name lives outside the function.** It remains available between calls.
- **An assignment inside a function is normally local.** A local `label` can have a different value from the module's `label`.
- **Return the local value.** The call should not change the module-level name.

py188|Start fresh for each call
- **Create local work inside the function.** Initialize a total from the input for this call.
- **Update that local value.** Add the supplied bonus, including zero or a negative amount.
- **Return this call's answer.** A later call gets its own local work instead of inheriting an earlier total.

py113|Choose a default without changing it
- **Read the module constant when needed.** `REGION` supplies the default only when `region is None`.
- **Preserve an explicit empty region.** An empty string is different from a missing value.
- **Build and return the label.** Use local values; leave the module constant unchanged.

py192|Use a small failure as evidence
- **Compare expected and actual results.** A failing check shows a specific mismatch to investigate.
- **Try a tiny set of inputs.** Positive, zero and negative values can expose different wrong assumptions.
- **Fix the rule for every call.** Return the calculation rather than printing or hardcoding one expected answer.

py193|Check what each term means
- **Read the contract before editing.** Decide which charge applies per item and which applies once per order.
- **Test more than one item.** A single-item case can hide misplaced parentheses or a repeated fee.
- **Test zero items too.** Boundary cases reveal whether the fixed charge is being applied correctly.

py194|Check the value and the console separately
- **A return value goes to the caller.** It is what another expression or a test can use.
- **A print goes to the console.** Displaying the right number does not return that number.
- **Honor both parts of the contract.** Return the requested result and leave the console quiet when printing is forbidden.

py117|Test the boundary, then its neighbors
- **Translate the rule precisely.** One more person fits only while the current count is below capacity.
- **Distinguish `<` from `<=`.** Equality means the room is already full.
- **Try nearby cases.** Check just below capacity, exactly at capacity and a room with zero capacity.

py129|Repeat a small, clear update
- **Loop with `for`.** `range(start, stop)` supplies integers up to, but excluding, `stop`.
- **Start an accumulator at zero.** Add each value to the running total.
- **Match the endpoints.** Include `n` when the contract says “through n”; no iterations should still leave a valid total.

py130|Make progress on every pass
- **Use `while` for a changing condition.** Repeat while work remains.
- **Update both pieces of state.** Track how many batches ran and how much work is left.
- **Stop at zero.** `max(0, remaining - capacity)` avoids negative remaining work. A positive capacity makes progress possible.

py131|Skip, stop or return
- **Skip with `continue`.** Ignore an unsuitable value and move to the next one.
- **Stop with `break` or a return.** Once you have the requested first match, later values should not replace it.
- **Check all parts of the rule.** Zero is even and non-negative. Use `None` only when no value qualifies.

py132|Visit a grid in a predictable order
- **Use an outer loop for rows.** Each row is visited before moving to the next.
- **Use an inner loop for columns.** Finish every column in the current row first: this is row-major order.
- **Collect coordinate tuples.** Each cell needs a `(row, column)` pair; either zero dimension means there are no cells.

py196|Let Python supply positions and pairs
- **Use `enumerate` for positions.** `enumerate(names, start=1)` produces `(position, name)` pairs starting at one.
- **Unpack in the loop.** The two names receive the position and its corresponding value.
- **Use `zip` for corresponding inputs.** It pairs values and normally stops at the shorter input; `strict=True` can report unequal lengths.

py136|Transform, then filter with care
- **Read the comprehension aloud.** `[expression for item in items if condition]` builds one new list from qualifying items.
- **Number before filtering when positions matter.** `enumerate(..., start=1)` retains the original positions even when some items are skipped.
- **Keep the exact text rule.** Empty strings and strings containing spaces are different. Use an ordinary loop if it is clearer.

py119|Trace an update without losing its result
- **Predict a tiny example first.** Work out how the total changes after each input.
- **Print an identifiable trace.** A label such as `total=N` explains which value you are observing.
- **Return the final answer separately.** An empty input has no updates to print but still has a numeric total.

py120|Look for state left behind
- **Try two calls in the same process.** A shared-state bug can be invisible on the first call.
- **Initialize per-call totals locally.** Each request needs a fresh accumulator.
- **Remove the global write.** `global AUDIT_TOTAL` directs assignment to module state; this calculation must leave that state unchanged.

py180|Move between text and words
- **Split on whitespace with `text.split()`.** Runs of spaces, tabs and newlines separate words without creating empty pieces.
- **Join with the separator on the left.** `"-".join(parts)` places one dash between string members, with none at the edges.
- **Preserve the agreed spelling.** Splitting and joining do not require changing case. No words means an empty result string.

py137|Look up by key
- **Write `{key: value}` pairs.** A dictionary maps keys to values; lookup is by key, not position.
- **Check membership with `key in mapping`.** A present value of `None`, zero or `False` is still present.
- **Choose the right view.** `.keys()`, `.values()` and `.items()` supply keys, values and pairs. `.get()` can supply a default for a missing key.

py138|Merge without changing the inputs
- **Create a fresh dictionary.** `{**base, **changes}` expands the entries into a new outer mapping.
- **Let later entries win.** A key present in `changes` replaces the corresponding value, even when the new value is `None`.
- **Know the copy depth.** This is a shallow merge: nested objects remain shared unless you copy them separately.

py139|Give each group its own list
- **Choose a grouping key.** Each team becomes one key in the result dictionary.
- **Initialize only when needed.** `setdefault(key, [])` retrieves a group's list or creates one for a missing key.
- **Append in encounter order.** Use a separate list per group, preserve repeated IDs and leave source records unchanged.

py140|Decide what happens to collisions
- **Swap each key and value.** Iterating `.items()` gives both parts of an original dictionary entry.
- **Require hashable new keys.** Strings work as keys; mutable lists do not.
- **Name the collision rule.** A dictionary holds one value per key, so a later assignment replaces an earlier one when new keys collide.

py02|Count one occurrence at a time
- **Start with an empty dictionary.** Each status code will be a key and its count will be the value.
- **Use zero for a new key.** `counts.get(code, 0)` provides the count before the next increment.
- **Keep the accumulator across the loop.** Initialize once per call, then update for every input occurrence.

py141|Keep only unique values
- **Create a set with `set()`.** A set stores unique hashable values; `{}` creates a dictionary instead.
- **Normalize before deduplicating.** Equivalent domains should have the same lowercase spelling before they enter the set.
- **Do not depend on set order.** Use membership to ask whether a value exists; sets have no positional index.

py142|Compare the two collections
- **Union `|` means either set.** Intersection `&` means both sets.
- **Difference `-` has a direction.** `after - before` finds additions; `before - after` finds removals.
- **Choose new results.** These operators create sets without modifying the original inputs; duplicates have no effect on membership.

py143|Check every requirement
- **Use a subset test.** `required <= granted` asks whether all required members are present, allowing equality.
- **Use disjointness for exclusions.** `isdisjoint` asks whether two sets have no members in common.
- **Combine both rules.** Empty requirements are satisfied, but any granted forbidden permission must still reject the request.

py144|Build a union without borrowing storage
- **Start a fresh set for each call.** Reusing an input set would let updates change the caller's data.
- **Use `update(group)` for the members.** `add(value)` inserts a single value instead; a list itself is not hashable.
- **Preserve the stated spelling.** Collect exact values, including an empty string, without silently trimming or lowercasing them.

py03|Remember membership and order separately
- **Use a set for “seen before?”.** Membership tells you whether this value has already appeared.
- **Use a list for the result.** Append only the first occurrence, in its original position relative to the other first occurrences.
- **Keep case significant.** Distinct strings stay distinct; converting straight to a set would not express first-seen order.

py123|Read permission bits as switches
- **Use `&` to keep shared bits.** Integer bitwise operations compare the individual binary positions.
- **Compare against the required mask.** Every required bit must survive the intersection with the granted bits.
- **Include the zero case.** A mask requiring no bits is satisfied. Bitwise `&` and boolean `and` do different jobs.

py145|Reject an invalid value clearly
- **Check the type first.** A boolean is an `int` subclass in Python, but this contract rejects it explicitly.
- **Check the allowed range next.** Distinguish a wrong kind of input from an integer outside the accepted limits.
- **Raise an informative exception.** Use `TypeError` or `ValueError` as requested, with a message identifying the port.

py146|Catch only the expected conversion errors
- **Try the conversion.** `int(raw)` accepts valid integer text, including permitted whitespace and a sign.
- **Catch the relevant failures.** `ValueError` covers malformed text; `TypeError` covers an unsupported input such as `None`.
- **Preserve valid zero.** Return the converted integer on success, rather than treating a falsy result as a failure.

py147|Guarantee cleanup
- **Put the operation in `try`.** Read and keep its result normally.
- **Put cleanup in `finally`.** That block runs when the read succeeds and when it raises an exception.
- **Let the original error continue.** Cleanup should not invent a success result or hide the failure.

py149|Use annotations as documentation
- **Describe inputs and output.** `values: list[int]` and `-> float` express the expected types.
- **Handle the empty case before division.** `sum(values)` adds the numbers; `len(values)` counts them.
- **Keep validation separate.** Hints do not check runtime inputs automatically. Return the float required by this contract.

py150|Say when a result can be absent
- **Use a union annotation.** `int | None` means the result may be an integer or `None`.
- **Check whether the collection is empty.** An empty list has no first item to index.
- **Preserve a real ID of zero.** A valid falsy integer is different from an absent result.

py151|Convert at an honest boundary
- **State both accepted types.** `int | str` documents the input choices, but runtime checks are still your job.
- **Reject bool explicitly.** Being an `int` subclass does not make a boolean an accepted ID here.
- **Convert, then validate the result.** Malformed text and a negative integer violate the contract for different reasons from an unsupported type.

py05|Validate the text before converting
- **Trim only the outer whitespace.** An empty result is invalid.
- **Require ASCII digits.** Signs, other characters and non-ASCII digit forms are outside this contract.
- **Check the numeric range.** Convert the accepted text, then require a port from `1` through `65535`.

py07|Build a clean record at the boundary
- **Validate the title as text.** Strip its outer whitespace and reject an empty result.
- **Validate a boolean as a boolean.** `bool("false")` is `True`; coercion cannot replace this type check.
- **Create a fresh, exact shape.** Keep only `title` and `done`, defaulting an absent `done` to `False`. Type hints describe this shape without enforcing it.

py114|Copy the container you will change
- **Assignment can create an alias.** Two names may refer to the same mutable list.
- **An outer copy is only shallow.** A copied record can still share its original `tags` list.
- **Copy the nested list too.** Add the new tag to an independent list, preserve the other fields and allow repeated tags.

py115|Avoid a shared default list
- **Defaults are created when a function is defined.** A list used as a default can survive across calls.
- **Use `None` to mean omitted.** Initialize fresh work inside the function instead.
- **Copy a supplied list too.** A fresh result protects caller-owned data and keeps separate calls independent.

py04|Calculate from inputs without leaving changes
- **Build a new list.** The caller's prices and the module default must remain unchanged.
- **Apply the stated integer rule.** `//` floors the discounted calculation to integer units.
- **Validate the percentage boundary.** Zero and one hundred are valid; values outside that range must be rejected.

py01|Accumulate an invoice in cents
- **Unpack each pair.** Each line contains a unit price in cents and a quantity.
- **Add the line totals.** Multiply price by quantity, then add it to a local accumulator starting at zero.
- **Validate before accepting a line.** Negative prices or quantities are invalid; an empty invoice has no charges.

py06|Translate a page into a slice
- **Convert from one-based pages.** Page one begins at index zero; each later page advances by the page size.
- **Take a new list slice.** The stop is excluded, and a slice past the end naturally contains fewer items or no items.
- **Validate both controls.** Require positive integers and reject booleans explicitly rather than accepting their integer behavior.

py199|Borrow a standard-library tool
- **Import the module.** `import math` makes its tools available under the name `math`.
- **Use the qualified name.** `math.ceil(value)` rounds upward to the smallest integer at least as large as the value.
- **Keep the returned result.** Store it in a variable, then print it; importing alone does not perform this calculation.

py200|Use a helper from another file
- **A module can be your own file.** The supplied `fees` module keeps the packaging rule in one place.
- **Import the helper you need.** A `from ... import ...` statement makes that helper available by name.
- **Call it when calculating.** Keeping the call, rather than copying today's fee, respects later changes to the rule.

py201|Separate importing from running
- **Put the script's work in `main()`.** Defining the function does not run its body.
- **Check `__name__`.** Direct execution sets it to `"__main__"`; importing uses the module's name.
- **Guard the call.** `if __name__ == "__main__":` lets a direct run call `main()` while an import stays quiet.

py161|Give each object its own state
- **Define a class, create instances.** `__init__` initializes a new object's values.
- **Use `self` for this object.** Attributes such as `self.name` and `self.completed` belong to the current instance.
- **Create mutable storage per instance.** A fresh history list lets each worker remember its own jobs without sharing another worker's history.

py162|Change state through a clear interface
- **Expose a read-only property.** `@property` lets callers read `balance` through a getter without supplying a setter.
- **Validate before changing state.** An invalid deposit must leave the old balance intact.
- **Keep the update in a method.** `deposit(amount)` applies the permitted change and returns the resulting balance.

py163|Extend a useful base behavior
- **Inherit from the base class.** The subclass keeps the relationship and behavior the contract asks it to extend.
- **Initialize the base part.** `super().__init__(...)` sets up the fields owned by the base class.
- **Override the method deliberately.** Add the surcharge to the base cost instead of duplicating or ignoring the base calculation.

py164|Separate the record from its delivery
- **Use a dataclass for the record.** Annotated fields declare the recipient and text; `frozen=True` prevents ordinary field reassignment.
- **Use composition for delivery.** A dispatcher holds a transport object and delegates sending to it.
- **Preserve the transport's behavior.** Call `send` once, return its result and let its errors propagate.

py148|Give a specific failure a name
- **Subclass a suitable exception.** `InsufficientFunds` is a specialized `ValueError` that callers can catch separately.
- **Validate the amount first.** A negative withdrawal is a different invalid request from one exceeding the balance.
- **Return only on success.** A valid withdrawal returns the new balance; a failure raises its specified error.

py152|Describe a dictionary's shape
- **Use `TypedDict` for named fields.** It documents the expected key names and value types.
- **Keep runtime behavior in mind.** The result is an ordinary dictionary; the declaration does not validate its contents automatically.
- **Construct the promised shape.** Return a fresh dictionary with exactly the declared fields and preserve values the contract says to keep.

py08|Keep a queue first-in, first-out
- **Append at the back.** `deque.append(job)` adds a new arrival.
- **Remove from the front.** `deque.popleft()` removes and returns the oldest job efficiently.
- **Keep storage per instance.** Implement `__len__` for `len(queue)` and let an empty removal raise `IndexError`.

py203|Pass a function as a value
- **Pass the tool without calling it yet.** `operation` refers to the function; `operation(value)` calls it.
- **Let the caller choose the behavior.** Your helper should use the supplied operation instead of guessing a replacement.
- **Preserve the outcome.** Call once, return its result unchanged and let an exception reach the caller.

py204|Tell sorting what to compare
- **Use `sorted` for a new list.** The original order in the caller's list stays untouched.
- **Supply a key function.** A short `lambda` can select the `"name"` field from each record.
- **Separate list and record ownership.** This task permits references to the same dictionaries; you still must not edit them.

py165|Transform and sort without side effects
- **Construct only the requested fields.** A new dictionary keeps the output shape deliberate.
- **Use a sorting key for both rules.** Compare score descending, then name ascending when scores tie.
- **Protect every input layer.** A new list alone is insufficient if you later mutate the original record dictionaries.

py166|Pass each result to the next step
- **Functions can be inputs.** Each supplied step accepts one current value.
- **Apply steps in order.** Feed each returned result into the next operation.
- **Keep an empty pipeline valid.** With no steps, the original value is already the result. Exceptions should propagate.

py118|Check the behavior of a supplied function
- **Call the candidate.** Test what it does rather than inspecting its source text.
- **Use assertions for expected results.** A false assertion raises `AssertionError`.
- **Choose revealing cases.** Zero, a negative input and a positive input expose different mistakes; successful checks need no explicit result.

py168|Produce values only when requested
- **Use an iterator for one-at-a-time work.** `iter` obtains one and `next` asks it for another value.
- **Use `yield` or a generator expression.** Computation can pause between results instead of building a whole list.
- **Respect one-shot inputs.** Avoid pre-consuming or restarting the source; yield qualifying values in their original order.

py09|Filter, then add the matching amounts
- **Read each status explicitly.** `.get("status")` can handle an absent status without a lookup error.
- **Keep only the specified success value.** Other statuses do not contribute to the total.
- **Accumulate without changing events.** A generator expression can supply qualifying amounts to `sum`; an empty sum is zero.

py167|Give recursion a stopping case
- **Recognize a leaf first.** An integer already has the numeric value you need.
- **Apply the same rule to smaller parts.** For a list, process each child and combine the returned sums.
- **Make the empty case natural.** An empty list contributes zero. Deep or cyclic inputs need additional care beyond this task's guarantees.

py116|Keep state in a closure
- **Return an inner function.** It can remember names from the enclosing call after that call finishes.
- **Use `nonlocal` to reassign that remembered name.** This differs from creating a new local or writing module state.
- **Create a new closure per counter.** Each returned counter owns its own count and updates it independently.

py207|Forward the caller's arguments
- **Unpack positional inputs with `*args`.** In a call, the tuple's members become separate positional arguments.
- **Unpack named inputs with `**kwargs`.** Its entries become keyword arguments.
- **Return the operation's outcome.** Forward once, preserve the argument containers and let failures propagate.

py205|Wrap a function carefully
- **Return a wrapper from the decorator.** `@decorate` is shorthand for replacing a function with `decorate(function)`.
- **Forward and return the original call.** Use `*args` and `**kwargs`, call once and preserve the return value or exception.
- **Keep metadata with `functools.wraps`.** Record the call before invoking the original so failed calls are logged too.

py206|Enter, work, then clean up
- **Enter with `__enter__`.** Its return value becomes the name after `as` in a `with` statement.
- **Exit with `__exit__`.** Python calls it after the body, including when the body raises an error.
- **Return `False` to propagate errors.** A true return would suppress them. Keep entry and cleanup state changes balanced.

py169|Read a file within a clear lifetime
- **Open text with its encoding.** Use UTF-8 when that is the format promised by the contract.
- **Use `with` for cleanup.** The file is closed when the block ends, including on failure.
- **Separate blank data from missing data.** Strip and filter lines as requested, but let a missing file raise `FileNotFoundError`.

py170|Parse JSON, then validate its shape
- **Decode with `json.loads`.** JSON text becomes ordinary Python values; never use `eval` as a JSON parser.
- **Validate after parsing.** Valid JSON can still contain the wrong container or member types. Reject booleans explicitly when integers are required.
- **Report failures honestly.** Malformed JSON raises `JSONDecodeError`; valid JSON with the wrong shape needs the contract's validation error.

py171|Let a CSV parser handle quoting
- **Use `csv.DictReader`.** Headers become field names; quoted commas remain part of a field.
- **Convert numeric fields yourself.** CSV fields arrive as strings. `StringIO` lets the parser read text already in memory.
- **Respect exact names.** Aggregate by the parsed account text. For actual CSV files, open with `newline=""`.

py10|Keep shrinking a sorted interval
- **Inspect the middle.** Binary search requires sorted input to decide which half can still contain the target.
- **Move beyond the inspected position.** Each unsuccessful iteration must make the remaining interval smaller.
- **Stop when the interval is empty.** That means the target is absent; return the sentinel required by the task.

py208|Store data, then read it back
- **Open an in-memory SQLite connection.** Create a table, insert rows and select the stored values.
- **Bind values with `?` placeholders.** Pass parameters separately; a one-item tuple needs a trailing comma, as in `(name,)`.
- **Make order and lifetime explicit.** Use `ORDER BY` for a guaranteed result order and close the connection in cleanup. Its own `with` block handles transactions, not closing.

py11|Keep SQL and user data separate
- **Declare the requested table.** The schema defines the ID and required title fields.
- **Bind values as parameters.** Quotes in a title belong to the data and must not become SQL syntax.
- **Commit writes and request an order.** Other connections need committed changes; `ORDER BY id` makes listing predictable.

py12|Store a value with its deadline
- **Calculate expiry from the supplied clock.** A deadline is `now + ttl`, which keeps time-dependent tests predictable.
- **Compare time explicitly.** A value is valid before the deadline and expired exactly at the deadline.
- **Separate presence from truthiness.** Zero, `False` and an empty string can all be valid cached values. Keep each cache instance independent.

py172|Await several operations together
- **Call an `async def` to get a coroutine.** Awaiting lets cooperative asynchronous work share the event loop; it is not automatically a background thread.
- **Gather the operations concurrently.** `asyncio.gather` returns results in input order even when completion order differs.
- **Keep waiting asynchronous.** Blocking calls stall the event loop. Use the supplied fetch operation and let its errors propagate.

py153|Build the report in stages
- **Split and normalize.** `text.split()` separates whitespace-delimited words; lowercase each token as specified.
- **Count the resulting tokens.** Punctuation stays part of each word unless the contract says otherwise.
- **Sort for a predictable report.** Return word/count pairs in word order, with an empty list when there are no words.

py154|Reconcile each account independently
- **Use signed integer cents.** Positive and negative entries change the corresponding account's balance.
- **Initialize when an account first appears.** An entry of zero still establishes that account's presence.
- **Keep zero balances and the original ledger.** Reconciliation should be repeatable without changing the input records.

py155|Make one decision for every event
- **Track accepted events per user.** A dictionary gives each user an independent counter.
- **Consume a slot only on acceptance.** Once the user's limit is reached, later attempts stay rejected.
- **Reset for the next batch.** Emit decisions in input order with fresh per-call state; a zero limit accepts nothing.

py156|Choose what you are counting
- **Count projects, not raw mentions.** The same library appearing twice in one project counts once for that project.
- **Deduplicate locally before aggregating.** A per-project set separates this rule from the overall counter.
- **Keep the inputs reusable.** Empty projects add nothing, and source mappings and lists must stay unchanged.

py157|Reason about both container layers
- **Identify the caller-owned objects.** The audit record and its nested events list must stay unchanged.
- **Copy the containers you will edit.** A fresh outer record alone still leaves a shared events list.
- **Keep unrelated fields and repeated events.** Add only the requested event without inventing cleanup or uniqueness rules.

py158|Check absence before choosing a fallback
- **A missing key is one case.** Membership tells you whether `"timeout"` was supplied.
- **A stored `None` is another case.** This contract also uses the default for that specific value.
- **Keep other stored values exactly.** An `or` fallback would accidentally replace `0`, `False` and `""` too.

py159|Filter and order as separate rules
- **Select only the requested records.** Read the boolean `done` field rather than guessing from a title or ID.
- **Sort by the numeric ID.** `sorted` returns a new list; `.sort()` changes an existing list and returns `None`.
- **Construct the output strings.** Preserve legitimate zero IDs and empty titles, and keep the original records untouched.

py160|Describe each state transition
- **Start from an independent copy.** The caller's initial ticket state must survive success and failure unchanged.
- **Check a command against the current state.** Adding an existing ID and closing a missing ID are invalid operations.
- **Apply valid commands in order.** Reject unknown actions clearly, then return the new state only when processing succeeds.
'''


def _parse_readings():
    readings = {}
    ident = None
    for line in _READINGS.splitlines():
        if not line.strip():
            continue
        if line.startswith('- '):
            assert ident is not None
            readings[ident]['points'].append(line[2:])
        else:
            ident, heading = line.split('|', 1)
            assert ident not in readings, ident
            readings[ident] = {'heading': heading, 'points': []}
    assert all(len(item['points']) == 3 for item in readings.values())
    return readings


READINGS = _parse_readings()
# These five already have purpose-written bullets, diagrams and callouts.
ILLUSTRATED = {'py101', 'py195', 'py133', 'py134', 'py135'}


def reading_sections(lesson):
    """Return the visible teaching steps and the optional original explanation."""
    if lesson['id'] in ILLUSTRATED:
        return lesson['teaching'], ''
    item = READINGS[lesson['id']]
    steps = '## ' + item['heading'] + '\n\n' + '\n\n'.join('- ' + point for point in item['points'])
    original = lesson['teaching'].strip()
    more = ('<details class="lesson-deeper">\n<summary>A little more explanation</summary>\n\n'
            + original + '\n\n</details>\n\n')
    return steps, more


def task_bullets(text):
    """Format existing contract sentences; keep quoted/code text intact."""
    if re.search(r'^- ', text, re.M):
        return text
    parts, start, quote, ticks, depth = [], 0, None, False, 0
    for index, char in enumerate(text):
        if char == '`' and quote is None:
            ticks = not ticks
        if ticks:
            continue
        if char == '"':
            quote = None if quote == '"' else '"'
        if quote:
            continue
        if char in '([':
            depth += 1
        elif char in ')]':
            depth -= 1
        if char == '.' and depth == 0 and (index + 1 == len(text) or text[index + 1].isspace()):
            parts.append(text[start:index + 1].strip())
            start = index + 1
    if text[start:].strip():
        parts.append(text[start:].strip())
    assert re.sub(r'\s+', ' ', ' '.join(parts)) == re.sub(r'\s+', ' ', text.strip())
    return '\n\n'.join('- ' + part for part in parts)
