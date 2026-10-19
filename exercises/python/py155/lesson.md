# Mission: the polite rate limiter

Maintain per-key state and make one decision for every event.

## Make one decision for every event

- **Track accepted events per user.** A dictionary gives each user an independent counter.

- **Consume a slot only on acceptance.** Once the user's limit is reached, later attempts stay rejected.

- **Reset for the next batch.** Emit decisions in input order with fresh per-call state; a zero limit accepts nothing.

## Walk through an example

```python
used = {}
allowed = []
for user in ["a", "b", "a"]:
    count = used.get(user, 0)
    allowed.append(count < 1)
    if count < 1:
        used[user] = count + 1
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A rate limiter makes admission decisions while tracking prior work. This mission simplifies time away: each call processes one batch with a fixed per-user limit. State is local to the batch and must reset for the next call.

Distinguish attempted events from accepted events. Only an accepted event consumes an available slot. When a user has reached the limit, later attempts remain rejected. Emit one decision per input so positions still correspond to original requests.

A dictionary gives each user an independent counter. Duplicated IDs are expected because one user may make several attempts. Zero limit rejects every event. Real distributed rate limiting needs a time model, shared storage and concurrency handling; this exercise isolates the decision logic. Pip's limiter rejected everyone equally. Fairness is not the only requirement.

</details>

## Before you run

What additional state would a time-window limiter need?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
