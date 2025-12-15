---
title: BUTTON_EVENT
---

# BUTTON_EVENT

This keyword defines a button event handler.

- This type of handler processes [PUSH](PUSH.md), [RELEASE](RELEASE.md) and [HOLD](HOLD.md) events.
- It can only be used in the [DEFINE_EVENT](DEFINE_EVENT.md) section of the program.

Example:

```c linenums="1"
BUTTON_EVENT\[DEVICE,CHANNEL\] or

```
BUTTON_EVENT \[DEVCHAN\[ \]\]

{

 PUSH:

    {

       // Push statements go here

    }

 RELEASE:

    {

       // Release statements go here

    }

 HOLD\[TIME\]: or HOLD\[TIME, REPEAT\]:

    {

       // Hold statements go here

    }

}

where:

- DEVICE refers to:

Device – a single device number constant.

D:P:S – a constant device specification such as TP:1:0.

- CHANNEL refers to  a single channel number constant.
- DEVCHAN\[ \] refers to a device-channel array.

See Also

- [Event Handlers](Event_Handlers.md)
- [Event Parameters](Event_Parameters.md)
- [Button Events](Button_Events.md)
- [Event Handler Keywords](Event_Handler_Keywords.md)

