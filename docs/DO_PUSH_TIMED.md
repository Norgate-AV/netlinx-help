---
title: DO_PUSH_TIMED
---

# DO_PUSH_TIMED

Similar to [DO_PUSH](DO_PUSH.md) except this one lets you specify the timeout.

- DO_PUSH defaults to a 0.5s push on a channel before issuing a DO_RELEASE for you (unless another DO_PUSH is executed for the same channel).
- DO_PUSH_TIMED lets you control the length of time that will pass before the automatic DO_RELEASE is generated.

Syntax:

```c linenums="1"
DO_PUSH_TIMED(DEV Device, INTEGER Channel, LONG Timeout)

```
Parameters:

- Device - the device to PUSH.
- Channel - the channel to PUSH.
- Timeout - the time (in 1/10ths of seconds) that the PUSH shall remain active. If zero is specified as the timeout then the timeout is 0.5s. If DO_PUSH_TIMED_INFINITE is specified as the timeout then the push never times out.

Returns: None

Example:

```c linenums="1"
DO_PUSH_TIMED (dvTouchPanel, 5, 10) // push button 5 for 1.0S

```
See Also

- [DO_PUSH](DO_PUSH.md)
- [DO_RELEASE](DO_RELEASE.md)
- [PUSH & RELEASE Keywords](PUSH_&_RELEASE_Keywords.md)
