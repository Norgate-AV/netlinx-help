---
title: CHANNEL_EVENT
---

# CHANNEL_EVENT

This keyword defines a channel event handler.

- This type of handler is invoked when an output change occurs on the specified device-channel.

- It can only be used in the [DEFINE\_EVENT](DEFINE_EVENT.md) section of the program.

Example:

```c linenums="1"
CHANNEL_EVENT\[DEVICE,CHANNEL\] or

```
CHANNEL_EVENT\[DEVCHAN\[ \]\]

{

 ON:

 {

  // Channel ON event handling

 }

 OFF:

 {

  // Channel OFF event handling

 }

}

Where:

- DEVICE refers to:

Device – a single device number constant.

D:P:S – a constant device specification such as TP:1:0.

- CHANNEL refers to a single channel number constant.

- DEVCHAN\[ \] refers to a device-channel array.

See Also

- [Event Handlers](Event_Handlers.md)

- [Event Parameters](Event_Parameters.md)

- [Channel Events](Channel_Events.md)

&nbsp;

- [Event Handler Keywords](Event_Handler_Keywords.md)

