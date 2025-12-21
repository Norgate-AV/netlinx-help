---
title: Data Events
---

# Data Events

Data Events provide the ability to receive strings of data from a device.

The structure for a `DATA_EVENT` is:

```c linenums="1"
DATA_EVENT[DEVICE]
{
    COMMAND:
    {
        // Command processing goes here
    }
    STRING:
    {
        // String processing goes here
    }
    ONLINE:
    {
        // OnLine processing goes here
    }
    OFFLINE:
    {
        // OffLine processing goes here
    }
    ONERROR:
    {
        // OnError processing goes here
    }
    STANDBY:
    {
        // Standby processing goes here
    }
    AWAKE:
    {
        // Awake processing goes here
    }
}
```

## Data Object

The Data Object is available to the data event handler as a local variable.

The following table lists the information contained in Data Objects:

## Data Objects

| Property Name        | Type                  | Description                    |
| -------------------- | --------------------- | ------------------------------ |
| `Data.Device`        | [DEV](DEV.md)         | Device                         |
| `Data.Device.Number` | [INTEGER](INTEGER.md) | Device number                  |
| `Data.Device.Port`   | [INTEGER](INTEGER.md) | Device port                    |
| `Data.Device.System` | [INTEGER](INTEGER.md) | System number                  |
| `Data.Number`        | [LONG](LONG.md)       | Event number                   |
| `Data.Text`          | [CHAR](CHAR.md) Array | Text associated with the event |

-   The _event number_ is a number associated with a command or error condition or the device ID
    associated with an online/offline event.
-   The numeric value is stored either as a floating point number or integer as appropriate, but the
    value can be assigned to a variable of any numeric type. This field could be a value associated
    with a command event or error condition.
-   _Text associated with the event_ is text associated with a command, string, or error
    notification. It can also be the device ID string in the case of an online/offline event.

The following table shows the fields that contain relevant information for data or notifications
received via Internet protocol (IP):

| Property Name     | Type                       | Description                                                                                                       |
| ----------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `Data.SourceIP`   | [CHAR](CHAR.md) <br> Array | IP address of the client/source application <br> **_Note_**: _The returned IP address appears as an IPv6 address_ |
| `Data.SourcePort` | [LONG](LONG.md)            | Server/source port number                                                                                         |

Not all fields in the `DATA` object apply to all types of events. The following table shows which
fields apply to which events.

An ‘X’ indicates that the field applies (or could apply) to the given event.

| Property Name          | Command | String | OnLine | OffLine | OnError | AWAKE | STANDBY |
| ---------------------- | ------- | ------ | ------ | ------- | ------- | ----- | ------- |
| `Data.Device`          | X       | X      | X      | X       | X       | X     | X       |
| `Data.Number`          |         |        | X      | X       | X       | X     | X       |
| `Data.Text`            | X       | X      | X      | X       | X       | X     | X       |
| `Data.SourceIPAddress` | X       | X      | X      | X       | X       | X     | X       |
| `Data.ServerIPAddress` | X       | X      | X      | X       | X       | X     | X       |
| `Data.SourcePort`      | X       | X      | X      | X       | X       | X     | X       |

NetLinx processes data received by a DATA_EVENT in real time. When data is received, it enters the
message queue and triggers a data event. If a buffer has been created for the device, the data is
placed within the buffer and can be used by either the DATA_EVENT or mainline.

The data can be evaluated in two ways:

1.  The actual string that is received by the message queue can be evaluated using the `DATA.TEXT`
    object within the event. The string in `DATA.TEXT` is also added to the end of the device's
    buffer. This becomes a factor when receiving large strings, or when receiving strings with an
    embedded string length or start and end characters.

2.  `DATA_EVENT` then evaluates the buffer to see if the entire string has been received before
    processing it; however, the evaluation is done immediately upon receipt of another chunk of
    data, and is only done when data is received. For example, `DATA.TEXT` may equal
    `{'over the lazy brown dog',ETX}` and the `DATA_BUFFER[500]` might equal
    `{STX,'The quick gray fox jumps over the lazy brown dog',ETX}`. By evaluating the buffer value,
    you can evaluate the entire string at once.

Two other important aspects of the `DATA_EVENT` are the [ONLINE](ONLINE.md) and
[OFFLINE](OFFLINE.md) event handlers. [ONLINE](ONLINE.md) and [OFFLINE](OFFLINE.md) events are
triggered when the master recognizes a device has come on the bus or has dropped off the bus.

NetLinx handles all device initializations and offline warning through the `DATA_EVENT`. Since every
device triggers an [ONLINE](ONLINE.md) event when the master is reset, this not only ensures that
the device will be initialized on startup, but also insures that the device will be initialized any
time the device comes online.

The `DATA_EVENT` is evaluated on a need to know basis, rather than on each pass through mainline.

## Example

The following example shows basic code for tracking a touch panel page.

-   Assume that the variables have been properly defined in the
    [DEFINE_VARIABLE](DEFINE_VARIABLE.md) section.
-   The [DEFINE_START](DEFINE_START.md) section contains the creation of the buffer and the
    [DEFINE_PROGRAM](DEFINE_PROGRAM.md) section contains the string evaluation.

```c linenums="1"
DEFINE_START

CREATE_BUFFER TP1, TP1_BUFFER
.
.
DEFINE_EVENT
..
DATA_EVENT[TP1](* EVALUATE TP1 DATA *)
{
    STRING:
    {
        SELECT
        {
            ACTIVE (FIND_STRING (DATA.TEXT,'PAGE-',1)):
            {
                JUNK = REMOVE_STRING (DATA.TEXT,'PAGE-',1)
                CUR_PAGE = DATA.TEXT
            }
            ACTIVE (FIND_STRING (DATA.TEXT,'KEYP-',1)):
            {
                (* keypad code *)
            }
            ACTIVE (FIND_STRING (DATA.TEXT,'KEYB-',1)):
            {
                (* keyboard code *)
            }
            ACTIVE (1):
            {
                (* default code *)
            }
        }
        CLEAR_BUFFER TP1_BUFFER
    }
    ONLINE:
    {
        SEND_COMMAND TP1, 'TPAGEON'
    }
}
.
.
```

Each event handler contains several imbedded data objects that pass data values into the event
handler code.

## See Also

-   [Button Events](Button_Events.md)
-   [Channel Events](Channel_Events.md)`
