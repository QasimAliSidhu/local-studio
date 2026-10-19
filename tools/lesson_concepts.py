"""Plain concept names kept separate from the course's story titles."""
CONCEPTS = dict(line.split('|', 1) for line in '''
py101|print() and strings
py102|Execution order
py103|Quotes and comments
py104|Numbers and expressions
py105|Variables and assignment
py173|Variable reassignment
py174|str, int and float
py181|Arithmetic and parentheses
py182|Floor division and modulo
py175|len() and returned values
py191|String indexing
py176|String methods: strip()
py177|String methods: lower()
py106|replace() and method chaining
py178|f-strings
py107|Numeric format specifiers
py108|Type conversion: int()
py184|Defining and calling functions
py185|Parameters and arguments
py186|return versus print()
py109|Function return values
py110|Default and keyword arguments
py111|Function composition
py112|Tuples and unpacking
py179|Booleans, comparisons and None
py189|if, else and indentation
py125|Boolean operators
py126|if / elif / else
py127|Short-circuit evaluation
py128|Truthiness and None checks
py124|Floating-point comparisons
py121|Division and remainder
py122|Operator precedence and powers
py187|Local and global scope
py188|Local state per function call
py113|Scope and constants
py192|Debugging with examples
py193|Assertions and expected results
py194|Debugging print versus return
py117|Boundary conditions
py195|List literals and len()
py133|Sequence indexing
py134|Slicing: start, stop and step
py135|List mutation: append() and pop()
py129|for, range() and accumulators
py130|while loops
py131|break and continue
py132|Nested loops
py196|enumerate() and zip()
py136|List comprehensions
py119|Debugging with print()
py120|Shared-state bugs
py180|split() and join()
py137|Dictionaries, keys and get()
py138|Dictionary merging and copying
py139|Grouping with setdefault()
py140|Dictionary comprehensions
py02|Dictionary counting
py141|Sets and uniqueness
py142|Set union, intersection and difference
py143|Subsets and disjoint sets
py144|Accumulating sets
py03|Stable deduplication
py123|Binary flags and bitwise operators
py145|Raising exceptions
py146|try / except
py147|finally and cleanup
py149|Type annotations
py150|Optional results and unions
py151|Union narrowing and validation
py05|Configuration validation
py07|Type hints and runtime validation
py114|Aliasing and shallow copies
py115|Mutable default arguments
py04|Scope and pure functions
py01|Numeric aggregation
py06|Pagination and slicing
py199|Standard-library imports
py200|Local modules
py201|The __name__ guard
py161|Classes, instances and methods
py162|Properties and invariants
py163|Inheritance and super()
py164|Dataclasses and composition
py148|Custom exceptions
py152|TypedDict
py08|Classes and FIFO queues
py203|Functions as values
py204|lambda and sort keys
py165|Pure transformations and sorted()
py166|Callbacks and pipelines
py118|Writing effective assertions
py168|Generators and yield
py09|Functional aggregation
py167|Recursion and base cases
py116|Closures and nonlocal
py207|Argument unpacking: * and **
py205|Decorators
py206|Context-manager protocol
py169|pathlib and file handling
py170|JSON parsing and validation
py171|Reading CSV
py10|Binary search
py208|SQLite and bound parameters
py11|SQLite persistence
py12|Cache expiry and clocks
py172|async, await and gather()
py153|Normalization and counting
py154|Aggregation with integer money
py155|Stateful rate limiting
py156|Nested iteration and uniqueness
py157|Nested copying and mutation
py158|Truthiness and explicit defaults
py159|Filtering, sorting and projection
py160|State machines and validation
go01|Slices and error returns
go02|Maps and word counting
go03|Interfaces
go04|Error wrapping and errors.Is
go05|Strict JSON decoding
go06|HTTP clients and context
go07|HTTP handlers and JSON
go08|Goroutines and concurrency
'''.strip().splitlines())
