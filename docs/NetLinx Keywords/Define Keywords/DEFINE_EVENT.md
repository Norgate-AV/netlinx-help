---
title: DEFINE_EVENT
---

# DEFINE_EVENT

In NetLinx, events thread runs parallel to the mainline thread. Events describe certain types of conditions within the control system. If the conditions are defined as a DEFINE_EVENT, the event code is run and mainline is bypassed.

The DEFINE_EVENT program section is where event handling code is placed and it provides the basis for the construction of the event table. When an incoming event is received by NetLinx, the event table is searched for a handler for that event.

Note: A handler is a block of code that performs the necessary processing for an event notification received from a given device (and possibly associated with a particular channel).

There are five different types of events:

- [Button Events](Button_Events.md)

- [Channel Events](Channel_Events.md)

- [Data Events](Data_Events.md)

- [Level Events](Level_Events.md)

- [Time line Events](TIMELINE_EVENT.md)

Example:

```
DEFINE_EVENT

```
BUTTON_EVENT\[TP,21\]

   (\* KC REPEAT 'A' \*)

{

   PUSH:

   {SEND_STRING KC, 'A'

   }

   RELEASE:

   {

   }

   HOLD\[5,REPEAT\]:

   {

   SEND_STRING KC, 'A'

   }

}

See Also

- [DEFINE Keywords](DEFINE_Keywords.md)

- [Event Handler Keywords](Event_Handler_Keywords.md)

