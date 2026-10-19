# All permissions, not merely one

Check subset and disjointness relationships.

## Check every requirement

- **Use a subset test.** `required <= granted` asks whether all required members are present, allowing equality.

- **Use disjointness for exclusions.** `isdisjoint` asks whether two sets have no members in common.

- **Combine both rules.** Empty requirements are satisfied, but any granted forbidden permission must still reject the request.

## Walk through an example

```python
required = {"read", "write"}
granted = {"read", "write", "audit"}
print(required <= granted)  # True
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A set is a subset of another if every one of its members appears in the other set. `required <= granted` is a subset test; it is unrelated to lexicographic ordering. Equality is allowed in a non-strict subset test, while `<` requires a proper subset.

Two sets are disjoint if they have no members in common. `isdisjoint` expresses this directly. Combining subset and disjointness checks is useful when a request has both required and forbidden features.

Empty requirements are satisfied because there is no unmet member. A non-empty forbidden intersection must reject the request even when all required permissions are present. This is a small logic exercise, not a full security design. Pip has both 'read reports' and 'operate confetti cannon'. Only one belongs on the payroll service.

</details>

## Before you run

Why would a non-empty intersection with required prove too little?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
