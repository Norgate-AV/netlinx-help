---
title: Level_Events
---

# Level Events

The level object is available to the level event handler as a local variable. Level events are triggered by a level change on a particular device. This eliminates having to constantly evaluate a level against a previous value.

LEVEL.VALUE is an embedded object value in the LEVEL_EVENT statement. The LEVEL.VALUE object eliminates the need to create a level for the TEMP device.

Syntax:

```c linenums="1"
LEVEL_EVENT\[DEVICE,LEVEL\] or LEVEL_EVENT\[(\[DEVLEV\[ \])\]

{

 // level event handler

}

```
It contains the information shown in the table below:

Level Value Object

|  |  |  |
|----|----|----|
| Property Name | Type | Description |
| Level.Input | [DEVLEV](DEVLEV.md) | Device + Level that caused the event to occur |
| Level.Input.Device | [DEV](DEV.md) | Device |
| Level.Input.Device.Number | [INTEGER](INTEGER.md) | Device number |
| Level.Input.Device.Port | [INTEGER](INTEGER.md) | Device port |
| Level.Input.Device.System | [INTEGER](INTEGER.md) | System number |
| Level.Input.Level | [INTEGER](INTEGER.md) | Level number |
| Level.SourceDev | [DEV](DEV.md) | Source Device of Level Event |
| Level.SourceDev.Number | [INTEGER](INTEGER.md) | Source Device Number |
| Level.SourceDev.Port | [INTEGER](INTEGER.md) | Source Device Port |
| Level.SourceDev.System | [INTEGER](INTEGER.md) | Source Device System |
| Level.Value | Numeric | Level value |

The numeric value is stored either as a floating-point number or integer as appropriate, but the value can be assigned to a variable of any numeric type.

Button Event example:

LEVEL_EVENT \[TEMP, 1\]

{

IF (LEVEL.VALUE\>= COOL_POINT)

{

ON\[RELAY,FAN\]

}

ELSE IF (LEVEL.VALUE \<= HEAT_POINT)

{

OFF\[RELAY,FAN\]

}

}

See Also

- [Event Handlers](Event_Handlers.md)

- [Button Events](Button_Events.md)

- [Channel Events](Channel_Events.md)

- [Data Events](Data_Events.md)

- [Event Parameters](Event_Parameters.md)

- [Custom Events](Custom_Events.md)

