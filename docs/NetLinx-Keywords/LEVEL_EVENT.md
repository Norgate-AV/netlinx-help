---
title: LEVEL_EVENT
---

# LEVEL_EVENT

This keyword defines a level event handler. This type of handler is invoked when
a level change occurs on the specified device-channel.

-  It can only be used in the [DEFINE_EVENT](DEFINE_EVENT.md) section of the
  program.
- The level object is available to the level event handler as a local variable.

LEVEL_EVENT\[DEVICE,LEVEL\] or LEVEL_EVENT\[(\[DEVLEV[])\]

{

 // level event handler

}

See Also

- [Event Handlers](Event_Handlers.md)
- [Event Parameters](Event_Parameters.md)
- [Level Events](Level_Events.md)
- [Event Handler Keywords](Event_Handler_Keywords.md)
