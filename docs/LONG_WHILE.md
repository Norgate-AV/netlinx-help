---
title: LONG_WHILE
---

# LONG_WHILE

A [LONG_WHILE](LONG_WHILE.md) differs from a [WHILE](WHILE.md) statement in the way input change notifications are processed during the programming loop. Before execution of each loop after the first, the system checks the input queue for a change notification message. The message is retrieved if one exists.

This message must be processed before another one is retrieved either at the start of the next loop or at the beginning of the next mainline iteration. Otherwise, the message is lost.

Example:

```
LONG_WHILE (\<conditional expression\>)

{

 (\* conditional statements \*)

}

```
Notes:

- DEFINE_EVENTs events are still processed even if mainline is in a LONG_WHILE.

- Special care should be taken to avoid spawning concurrent LONG_WHILEs via [DEFINE_EVENT](DEFINE_EVENT.md) code. This can cause excessive drag on system resources.

See Also

- [Conditional Keywords](Conditional_Keywords.md)

- [WHILE](WHILE.md)

- [MEDIUM_WHILE](MEDIUM_WHILE.md)

