---
title: RELEASE
---

# RELEASE

The RELEASE keyword is used to declare a block of code to be executed when a
release event is received for the associated device and channel.

RELEASE \[DEVICE,CHANNEL\]

RELEASE \[DEVCHAN[]\]

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

- [DEVCHAN](DEVCHAN.md)[]: a device-channel array.

Note: This keyword also defines a section in a [BUTTON_EVENT](BUTTON_EVENT.md)
handler for processing [RELEASE](RELEASE.md) events.

See Also

- [PUSH](PUSH.md)
- [PUSH_CHANNEL](PUSH_CHANNEL.md)
- [PUSH_DEVCHAN](PUSH_DEVCHAN.md)
- [PUSH_DEVICE](PUSH_DEVICE.md)
- [RELEASE_CHANNEL](RELEASE_CHANNEL.md)
- [RELEASE_DEVCHAN](RELEASE_DEVCHAN.md)
- [RELEASE_DEVICE](RELEASE_DEVICE.md)
