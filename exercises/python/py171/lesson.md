# CSV: commas are allowed in names

Use the csv module instead of splitting structured text by hand.

## Let a CSV parser handle quoting

- **Use `csv.DictReader`.** Headers become field names; quoted commas remain part of a field.

- **Convert numeric fields yourself.** CSV fields arrive as strings. `StringIO` lets the parser read text already in memory.

- **Respect exact names.** Aggregate by the parsed account text. For actual CSV files, open with `newline=""`.

## Walk through an example

```python
import csv
from io import StringIO

rows = csv.DictReader(StringIO('name,cents\n"Tea, Ltd",125\n'))
# The name field is one value: Tea, Ltd
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

CSV allows fields to contain commas and newlines when they are quoted according to the format. Splitting every line on commas breaks these records. The standard library's csv module understands quoting and escapes, so use the parser for the format rather than a homemade approximation.

`csv.DictReader` uses the header row as field names and yields one dictionary per data row. Numeric values remain strings until you convert them. With actual files, open using `newline=""` so the csv module can handle newline rules correctly. `StringIO` provides a file-like interface for text already in memory.

Validate according to your input contract; this mission guarantees the header and row shapes so you can focus on parsing and aggregation. Keep account spelling exact, including spaces and punctuation. Pip declared commas illegal in customer names. The customers have declined the schema migration.

</details>

## Before you run

Why can a quoted newline make even splitting into lines unsafe for general CSV?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
