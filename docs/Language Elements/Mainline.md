---
title: Mainline
---

# Mainline

_Mainline_ is the section of the program that is executed continuously by the
NetLinx Master Controller. [DEFINE_PROGRAM](DEFINE_PROGRAM.md) contains the code
known as _mainline_ that is executed continuously as long as the Controller has
power. Mainline is where all input (button events, level changes, command/string
input, etc.) is processed. After each pass through mainline, NetLinx services
the NetLinx bus and updates its internal structures.

NetLinx runs on multiple threads; mainline and event handlers run on parallel
threads. Event handlers are defined within NetLinx and operate like
mini-mainlines. They contain far less code and run faster than mainline. If an
event occurs, and an event handler has been defined for that event, NetLinx
bypasses mainline and runs the event handler.

A typical NetLinx program is composed of a number of different sections. Each
section defines some aspect of a program such as device definitions, variable
declarations, channel characteristics or event processing. The sections that can
comprise a NetLinx program are listed below:

|                                                 |                                                           |
| ----------------------------------------------- | --------------------------------------------------------- |
| [DEFINE_DEVICE](DEFINE_DEVICE.md)               | [DEFINE_MUTUALLY_EXCLUSIVE](DEFINE_MUTUALLY_EXCLUSIVE.md) |
| [DEFINE_COMBINE](DEFINE_COMBINE.md)             | [DEFINE_TOGGLING](DEFINE_TOGGLING.md)                     |
| [DEFINE_CONSTANT](DEFINE_CONSTANT.md)           | [DEFINE_CALL](DEFINE_CALL.md)                             |
| [DEFINE_TYPE](DEFINE_TYPE.md)                   | [DEFINE_FUNCTION](DEFINE_FUNCTION.md)                     |
| [DEFINE_VARIABLE](DEFINE_VARIABLE.md)           | [DEFINE_START](DEFINE_START.md)                           |
| [DEFINE_CONNECT_LEVEL](DEFINE_CONNECT_LEVEL.md) | [DEFINE_EVENT](DEFINE_EVENT.md)                           |
| [DEFINE_LATCHING](DEFINE_LATCHING.md)           | [DEFINE_PROGRAM](DEFINE_PROGRAM.md)                       |

Not all of the sections listed above are required to create a complete program.
Only DEFINE_PROGRAM or DEFINE_EVENT is required. Other sections are required
only to support code in one of these two sections, although the compiler might
require more.

The event processing is managed through code in the DEFINE_EVENT section. This
provides an efficient mechanism for processing events, in that mainline does not
have to be traversed to process a single I/O request. A handler can be defined
for processing device-specific events as well as providing feedback for the
device initiating the event notification. If a handler is present, mainline will
not be called to process the event; the handler is called instead. Once the
handler completes its execution, the system is ready to process the next input
message. When no more messages are pending, mainline is run. In effect, mainline
becomes an idle time process.

> Note: Even if you do not include any code in mainline (the DEFINE_PROGRAM
> section), feedback statements from button event handlers are still run as part
> of mainline.

The illustration below illustrates message and mainline processing as it appears
in the NetLinx system. Note that bus servicing is taken care of by a separate
process thread (Connection Manager & Message Dispatcher) and therefore is not a
task that must follow mainline as in an Axcess system.

![../../assets/img/Message_and_Mainline_processing.gif](./../../assets/img/Message_and_Mainline_processing.gif "../../assets/img/Message_and_Mainline_processing.gif")

## See Also

- [Statements and Expressions](Statements_and_Expressions.md)
- [Keywords](Keywords.md)
- [Devices](Devices.md)
- [Virtual Devices](Virtual_Devices.md)
- [Comments](Comments.md)
- [Identifiers](Identifiers.md)
- [Variables & Constants](Variables_&_Constants.md)
- [Subroutines](Subroutines.md)
- [Compiler Directives](Compiler_Directives.md)
- [Arrays](Arrays.md)
- [Assignments](Assignments.md)
- [Intrinsic Data Types](Intrinsic_Data_Types.md)
- [Event Handlers](Event_Handlers.md)
- [Loops](Loops.md)
- [Strings](Strings.md)
- [Structures](Structures.md)
- [Timeline Functions](Timeline_Functions.md)
- [Waits](Waits.md)
