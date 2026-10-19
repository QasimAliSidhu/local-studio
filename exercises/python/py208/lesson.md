# Make a tiny database before building storage

Use an in-memory SQLite table, bound parameters and fetched rows.

## Store data, then read it back

- **Open an in-memory SQLite connection.** Create a table, insert rows and select the stored values.

- **Bind values with `?` placeholders.** Pass parameters separately; a one-item tuple needs a trailing comma, as in `(name,)`.

- **Make order and lifetime explicit.** Use `ORDER BY` for a guaranteed result order and close the connection in cleanup. Its own `with` block handles transactions, not closing.

## Walk through an example

```python
import sqlite3

conn = sqlite3.connect(":memory:")
try:
    conn.execute("CREATE TABLE workers (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO workers(name) VALUES (?)", ("Pip",))
    rows = conn.execute("SELECT name FROM workers ORDER BY id").fetchall()
finally:
    conn.close()
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

SQLite is a database available through Python's standard-library sqlite3 module. `sqlite3.connect(":memory:")` creates a temporary database for this connection. SQL statements describe operations on tables: CREATE TABLE defines columns, INSERT adds rows, and SELECT reads them.

`connection.execute(sql, parameters)` binds data through ? placeholders. Keep user values out of the SQL string itself. A one-item parameter tuple needs a comma: `(name,)`. Parentheses alone would still contain a string. The returned cursor's fetchall() gives a list of row tuples.

Use ORDER BY when a result needs a guaranteed order. Closing the connection releases it; a connection's own with block manages transactions and does not itself close the connection. Here a try/finally closes the temporary database regardless of errors. Later storage tasks use persistent connections supplied by callers.

This is a small bridge into storage, not an entire SQL course. Pip's previous database was a list written on a sandwich wrapper. Parameter binding is an upgrade.

</details>

## Before you run

Why must a customer name be bound as data instead of inserted into the SQL text?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
