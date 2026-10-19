# Mission: the dependency inventory

Combine nested iteration, uniqueness and stable output.

## Choose what you are counting

- **Count projects, not raw mentions.** The same library appearing twice in one project counts once for that project.

- **Deduplicate locally before aggregating.** A per-project set separates this rule from the overall counter.

- **Keep the inputs reusable.** Empty projects add nothing, and source mappings and lists must stay unchanged.

## Walk through an example

```python
usage = {}
for libraries in {"web": ["a", "a"], "api": ["a", "b"]}.values():
    for library in set(libraries):
        usage[library] = usage.get(library, 0) + 1
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A nested mapping can describe projects and the libraries each one uses. The same library may appear in several projects or even twice in one list. An inventory should count distinct projects using a library, not raw occurrences.

Separate the local uniqueness rule from global aggregation. Convert one project's library list to a set, then increment each library once for that project. A library absent from every project should not appear in the result.

This is a useful pattern for analytics: decide the unit you are counting before choosing an accumulator. Counting events, users and projects are different questions even if the input looks similar. Keep source data untouched so another report can use it. Pip announced that ten projects use a library after finding ten copies in one project. The executive chart was briefly very exciting.

</details>

## Before you run

How would the answer differ if the requested metric were installation occurrences?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
