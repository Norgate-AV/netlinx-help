---
title: PUSH
---

# PUSH

The PUSH keyword is used to declare a block of code to be executed when a push
event is received for the associated device and channel.

Example:

```c linenums="1"
PUSH [DEVICE,CHANNEL]
```

PUSH \[DEVCHAN[]\]

{

 // statements

}

Parameters:

- DEVICE:

Device – a single device number.

Dps – a DEV structure.

D:P:S – a device specification such as TP:1:0.

DEV[] – a device array.

- CHANNEL:

Channel – a single channel number.

CHAN[] – a channel array.

- [DEVCHAN](DEVCHAN.md)[]:  a device-channel array.
- Variable: a variable defined under the [DEFINE_VARIABLE](DEFINE_VARIABLE.md)
  section.

Note: This keyword also defines a section in a [BUTTON_EVENT](BUTTON_EVENT.md)
handler for processing [PUSH](PUSH.md) events.

See Also

- [PUSH_CHANNEL](PUSH_CHANNEL.md)
- [PUSH_DEVCHAN](PUSH_DEVCHAN.md)
- [PUSH_DEVICE](PUSH_DEVICE.md)
- [RELEASE](RELEASE.md)
- [RELEASE_CHANNEL](RELEASE_CHANNEL.md)
- [RELEASE_DEVCHAN](RELEASE_DEVCHAN.md)
- [RELEASE_DEVICE](RELEASE_DEVICE.md)
