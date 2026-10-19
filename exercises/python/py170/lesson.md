# JSON is data, not Python in a coat

Decode JSON and validate the resulting runtime values.

## Parse JSON, then validate its shape

- **Decode with `json.loads`.** JSON text becomes ordinary Python values; never use `eval` as a JSON parser.

- **Validate after parsing.** Valid JSON can still contain the wrong container or member types. Reject booleans explicitly when integers are required.

- **Report failures honestly.** Malformed JSON raises `JSONDecodeError`; valid JSON with the wrong shape needs the contract's validation error.

## Walk through an example

```python
import json

record = json.loads('{"active": true, "count": 2}')
# {"active": True, "count": 2}
text = json.dumps(record, sort_keys=True)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

JSON is a data format, not executable Python source. `json.loads` decodes text into Python values: objects become dictionaries, arrays become lists, true becomes True, and null becomes None. `json.dumps` produces JSON text from supported Python values. Never use eval to parse untrusted data.

Successful decoding proves the text is valid JSON, not that its shape matches your application. Validate the top-level container, required fields and value types separately. A decoded boolean still needs special attention when an integer is required.

Keep serialization at the boundary and ordinary data processing in small functions. A malformed document should produce an honest error rather than a partially invented result. Pip attempted to parse a JSON object with a sticky note reading 'looks dictionary-ish'. We are trying the standard library instead.

The built-in `any(conditions)` is True when at least one supplied condition is truthy. A generator expression can supply validation conditions one at a time, stopping as soon as an invalid member is found.

</details>

## Before you run

Why is valid JSON not enough to establish that a request is a valid job list?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
