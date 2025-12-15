---
title: Event_Handlers
---

# Event Handlers

The NetLinx language provides a special program section called [DEFINE_EVENT](DEFINE_EVENT.md) to define handlers for incoming events/notifications. These handlers are stored in an event table providing quick access to code that must be executed when an event is received. There are handlers to support five types of events:

- [Button events](Button_Events.md) - include pushes, releases and holds. These events are associated with a push or release on a particular device-channel. Button events may include an optional feedback handler that runs immediately after the event handler finishes. The feedback handler is also executed every time mainline runs.
- [Channel events](Channel_Events.md) - occur when an output change (on/off) is detected on a device-channel.
- [Data events](Data_Events.md) - include commands, strings, status and error messages. These events are associated with a device only.
- [Level events](Level_Events.md) - are received as a result of a level change on a particular device.
- [Timeline events](Timeline_Functions.md) - trigger events based on a sequence of times.

Note: The processing of an event associated with a given member of a device, channel, device-channel, level or device-array must be completed before processing can begin on another event associated with the same array.

All incoming events are stored in a queue pending processing. Messages are processed in the order they are received. The steps in processing an event are:

1.  Check the event table for a handler(s) matching the specified device, device-channel or device-level associated with the event.

2.  If no handler is found, go to step 2.

3.  If a handler is found, go to step 3.

&nbsp;

2.  Execute MAINLINE to process the event (this is how the current NetLinx system processes events). Go to step 5.

3.  Execute the code in the event handler(s) pertaining to the type of event received.

4.  If the event is a button event, execute code (if any) found in the corresponding FEEDBACK section.

5.  Stop – message processing complete.

Note: More than one handler can be defined for the same event. In this case, the handlers are executed in the order in which they are defined in the program.

The Event Handler descriptions are:

DEVICE refers to a device specification:

- DEVICE: A single device number constant
- D:P:S: A constant device specification such as 128:1:0
- DEV\[ \]: A device array

CHANNEL refers to a device specification:

- CHANNEL: A single channel number constant
- CHAN \[ \]: An integer array of channel numbers
- DEVCHAN\[ \]: A device-channel array

LEVEL refers to a device specification:

- LEVEL: A single level number constant
- LEV \[ \]: An integer array of level numbers
- DEVLEV\[ \]: A device-level array

See Also

- [Event Parameters](Event_Parameters.md)
- [Event Handler Keywords](Event_Handler_Keywords.md)
- [TIMELINE Keywords](TIMELINE_Keywords.md)
