---
title: DEFINE_MUTUALLY_EXCLUSIVE
---

# DEFINE_MUTUALLY_EXCLUSIVE

When a channel is turned on in a mutually exclusive set, it activates its physical output as long as the button is pressed. When the button is released, the physical output stops. Even after the physical output stops, the status still indicates the channel is on until another channel in the mutually exclusive set is activated. The feedback remains on to indicate which channel in the set was activated last ("last button pushed" feedback).

 When a channel or variable in a mutually exclusive set is activated, all other members of the set are turned off beforehand ("break before make" logic).

Members of a mutually exclusive set are placed in parentheses underneath the [DEFINE_MUTUALLY_EXCLUSIVE](DEFINE_MUTUALLY_EXCLUSIVE.md) keyword. The double period (..) specifies a range of channels on the particular device to be defined as mutually exclusive.

Example:

```
DEFINE_MUTUALLY_EXCLUSIVE

(\[RELAY,SCREEN_UP\], \[RELAY,SCREEN_DOWN\])

```
DEFINE_TOGGLING

\[RELAY,SCREEN_UP\]\[RELAY,SCREEN_DOWN\]

The last entry specifies a set of mutually exclusive variables – VCR_SELECT, CD_SELECT, and CASS_SELECT. If any one of the three variables is turned on (e.g., "ON \[VCR_SELECT\]") the other two are turned off.

If a channel is defined to be both mutually exclusive and latching, it has the same behavior described above except that the channel stays on even after the button that activated it is released. Theoretically, a channel in a mutually exclusive latching set cannot be turned off without activating another channel in the same set.

However, in NetLinx you can bypass this rule by using [TOTAL_OFF](TOTAL_OFF.md). The TOTAL_OFF function turns a channel or variable off. Unlike OFF, TOTAL_OFF turns off the status of a channel or variable that is in a mutually exclusive set.

Note: If you have a set of variables that are mutually exclusive and you set one of the variables to a non-zero value by assignment, e.g. Var1 = 1 or the Studio Debug window, then the other variables in the set stay "on" i.e. non-zero. See [DEFINE_MUTUALLY_EXCLUSIVE and Variables](DEFINE_MUTUALLY_EXCLUSIVE_and_Variables.md) for details.

See Also

- [DEFINE_LATCHING](DEFINE_LATCHING.md)

- [DEFINE_TOGGLING](DEFINE_TOGGLING.md)

- [ON](ON.md)

- [OFF](OFF.md)

- [TOTAL_OFF](TOTAL_OFF.md)

- [PUSH_CHANNEL](PUSH_CHANNEL.md)

- [RELEASE_CHANNEL](RELEASE_CHANNEL.md)

- [PUSH_DEVCHAN](PUSH_DEVCHAN.md)

- [RELEASE_DEVCHAN](RELEASE_DEVCHAN.md)

- [PULSE](PULSE.md)

- [SET_VIRTUAL_CHANNEL_COUNT](SET_VIRTUAL_CHANNEL_COUNT.md)

&nbsp;

- [COMBINE_CHANNELS](COMBINE_CHANNELS.md)

- [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md)

