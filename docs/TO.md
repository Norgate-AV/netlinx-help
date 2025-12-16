---
title: TO
---

# TO

The TO command is used to activate a channel or variable for as long as the corresponding channel of its [PUSH](PUSH.md) statement is activated.

When the channel referenced by the PUSH statement changes from Off to On, the TO command starts activating the associated channel or variable.

When the channel is released, the TO command stops activating the channel or variable. For this reason, a TO statement must be found only underneath a PUSH statement or [BUTTON_EVENT](BUTTON_EVENT.md).

TO is valid:

1.  Under a [PUSH](PUSH.md) statement

2.  Under a [BUTTON_EVENT](BUTTON_EVENT.md)/PUSH handler

3.  Under a [BUTTON_EVENT](BUTTON_EVENT.md)/HOLD handler

4.  In a [DEFINE_FUNCTION](DEFINE_FUNCTION.md) or [DEFINE_CALL](DEFINE_CALL.md) that gets invoked in one of the areas above. In this case,  the function or call could be potentially be invoked anywhere in the program. It is an intractable problem to check for misplacement of <any possible function name> and <any possible call name>, so TO outside of PUSH'es will not generate an error, just a warning.

Note: This all applies to [MIN_TO](MIN_TO.md)  also.

Syntax:

```c linenums="1"
TO [DEVICE,CHANNEL]
```

TO \[DEVCHAN[]\]

TO \[Variable\]

Parameters

DEVICE refers to:

- Device – a single device number.
- Dps – a DEV structure.
- D:P:S – a device specification such as TP:1:0.
- DEV[] – a device array.

CHANNEL refers to:

- Channel – a single channel number.
- CHAN[] – a channel array.
- The channel or variable will act under the rules set by [DEFINE_LATCHING](DEFINE_LATCHING.md), [DEFINE_MUTUALLY_EXCLUSIVE](DEFINE_MUTUALLY_EXCLUSIVE.md) and [DEFINE_TOGGLING](DEFINE_TOGGLING.md).

DEVCHAN[] refers to a device-channel array.

- Variable refers to a variable defined under the [DEFINE_VARIABLE](DEFINE_VARIABLE.md) section.

See Also

- [MIN_TO](MIN_TO.md)
