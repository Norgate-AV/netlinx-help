---
title: Button_Events
---

# Button Events

Button Events include Pushes, Releases and Holds. These events are associated
with a push or release on a particular device-channel.

- A [HOLD](HOLD.md) event handler specifies the actions that should be performed
  when a button is pressed and held for a minimum length of time indicated by
  the [TIME](TIME.md) parameter (specified in 0.1 second increments).
- The [REPEAT](REPEAT.md) keyword is used to specify that the event notification
  should be repeated in TIME increments as long as the button is held.
- The BUTTON object is available to the button event handler as a local
  variable.

The following table lists the information contained in Button Objects.

Button Objects

|                            |                       |                                                        |
| -------------------------- | --------------------- | ------------------------------------------------------ |
| Property Name              | Type                  | Description                                            |
| Button.Input               | [DEVCHAN](DEVCHAN.md) | Device + Channel                                       |
| Button.Input.Channel       | [INTEGER](INTEGER.md) | Channel                                                |
| Button.Input.Device        | [DEV](DEV.md)         | Device                                                 |
| Button.Input.Device.Number | [INTEGER](INTEGER.md) | Device number                                          |
| Button.Input.Device.Port   | [INTEGER](INTEGER.md) | Device port                                            |
| Button.Input.Device.System | [INTEGER](INTEGER.md) | System number                                          |
| Button.Holdtime            | [LONG](LONG.md)       | Current hold time in one-millisecond (1 ms) increments |
| Button.SourceDev           | [DEV](DEV.md)         | Source device of button event                          |
| Button.SourceDev.Number    | [INTEGER](INTEGER.md) | Source device number                                   |
| Button.SourceDev.Port      | [INTEGER](INTEGER.md) | Source device port                                     |
| Button.SourceDev.System    | [INTEGER](INTEGER.md) | Source device system.                                  |

If the event handler is specified using an array for DEV, CHANNEL, or a DEVCHAN
array, [GET_LAST](GET_LAST.md) can determine which index in the array caused the
event to run.

Example:

```c linenums="1"
BUTTON_EVENT[DEVICE,CHANNEL] or
```

BUTTON_EVENT\[(DEVCHAN[])\]

{

 PUSH:

 {

  // PUSH event handler

 }

 RELEASE:

 {

  // RELEASE event handler

 }

 HOLD\[TIME\]: or HOLD\[TIME, REPEAT\]:

 {

  // HOLD event handler

 }

}

See Also

- [Channel Events](Channel_Events.md)
- [Data Events](Data_Events.md)
- [Level Events](Level_Events.md)
- [Custom Events](Custom_Events.md)
- [Event Parameters](Event_Parameters.md)
- [Event Handler Keywords](Event_Handler_Keywords.md)
