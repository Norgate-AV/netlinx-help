---
title: SET_TIMER
---

# SET_TIMER

This function resets the system timer. The system timer counts up in .10 second
units.

- The value passed to this function ([TIME](TIME.md)) may be any unsigned 32-bit
  variable or constant.

- This provides a timer with a maximum range of over 13 years.

Syntax:

```
SET_TIMER (TIME)

```

The system timer is reset to zero on power up.

See Also

- [SET Keywords](SET_Keywords.md)

- [GET_TIMER](GET_TIMER.md)

- [GET Keywords](GET_Keywords.md)
