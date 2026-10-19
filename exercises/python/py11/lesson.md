# SQLite task storage

Store and list tasks using parameterized SQLite queries.

## Keep SQL and user data separate

- **Declare the requested table.** The schema defines the ID and required title fields.

- **Bind values as parameters.** Quotes in a title belong to the data and must not become SQL syntax.

- **Commit writes and request an order.** Other connections need committed changes; `ORDER BY id` makes listing predictable.

## Walk through an example

```python
cursor = connection.execute(
    "SELECT name FROM users WHERE id = ?",
    (user_id,),
)
row = cursor.fetchone()
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

SQL text describes a query. **Parameters** carry user data separately. This preserves literal characters in titles and avoids interpreting a value as part of the SQL program.

> [!WARNING]
> A one-element tuple needs a trailing comma. Never interpolate a title into an SQL statement.

</details>

## Before you run

How will quotes in a title be handled? What result should a missing row produce?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
