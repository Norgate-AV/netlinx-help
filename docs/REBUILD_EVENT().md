---
title: REBUILD_EVENT()
---

# REBUILD_EVENT()

The NetLinx runtime supports the run-time library function REBUILD_EVENT(), which rebuilds the NetLinx event table for level, channel, button, timeline, and data events.  Modifications to variables used in event declarations affect NetLinx event handling when REBUILD_EVENT() is called after the variables are modified.

- REBUILD_EVENT() works on a module-by-module basis (i.e. calling the function in one module does not affect the event table of another module).
- REBUILD_EVENT() rebuilds the event table for variables modified in the same block of code in which it resides.
- With no braces, a REBUILD_EVENT() in DEFINE_START rebuilds event tables that use any variable modified in DEFINE_START, above the REBUILD_EVENT() statement.
- You can reduce the scope of the REBUILD_EVENT() by delineating a block with braces as shown at the bottom of the following example:

The code below demonstrates how to use the NetLinx REBUILD_EVENT() function:

DEFINE_DEVICE

dvApoc1 = 128:1:0

dvApoc2 = 1505:1:0

dvApoc3 = 1303:1:0

(\*---------------------------------------------------------\*)

(\* CONSTANT DEFINITIONS GO BELOW \*)

(\*---------------------------------------------------------\*)

DEFINE_CONSTANT

DEV panel[] = {dvApoc1,dvApoc2}

(\*---------------------------------------------------------\*)

(\* DEFINE TYPE DEFINITIONS GO BELOW \*)

(\*---------------------------------------------------------\*)

DEFINE_TYPE

(\*---------------------------------------------------------\*)

(\* VARIABLE DEFINITIONS GO BELOW \*)

(\*---------------------------------------------------------\*)

DEFINE_VARIABLE

DEV curModApoc

(\*---------------------------------------------------------\*)

(\* EVENT DEFINITIONS GO BELOW \*)

(\*---------------------------------------------------------\*)

DEFINE_EVENT

BUTTON_EVENT\[panel,1\]

{

  PUSH:

  {

ON\[panel,1\]

curModApoc = dvApoc2

// updates program event table to handle BUTTON_EVENT\[1505:1:0,5\]

REBUILD_EVENT()

  }

  RELEASE: OFF\[panel,1\]

}

BUTTON_EVENT\[panel,2\]

{

  PUSH:

  {

ON\[panel,2\]

curModApoc = dvApoc3

    // updates program event table to handle BUTTON_EVENT\[1303:1:0, 5\]

REBUILD_EVENT()

// the following assignment has no affect on the program event table

  curModApoc = dvApoc1

  }

  RELEASE: OFF\[panel,2\]

}

BUTTON_EVENT\[curModApoc,5\]

{

  PUSH: ON\[dvApoc3,5\]

  RELEASE: OFF\[dvApoc3,5\]

}

//  end

//  REBUILD_EVENT() rebuilds the event table for variables modified

//  in the same block of code in which it resides.

//

//  With no braces a REBUILD_EVENT() in DEFINE_START should rebuild the

//  event tables that use any variable modified in DEFINE_START, above

//  the REBUILD_EVENT() statement.

//  You can reduce the scope of the REBUILD_EVENT() by delineating

//  a block with braces:

DEFINE_DEVICE

dvTP = 10001:1:0

DEFINE_VARIABLE

INTEGER X // loop counter

INTEGER nBTNS\[4000\]

DEFINE_START

FOR (X = 1; X \<= 4000; X++)

{

   nBtns\[X\] = X

}

// the braces below enclose a variable update and

// rebuild_event statement in a single block

{

   SET_LENGTH_ARRAY(nBtns,4000)

  REBUILD_EVENT()

}

BUTTON_EVENT\[dvTP,nBtns\]

{

  PUSH:

  {

// ...

  }

}

// end

See Also

- [Event Handlers](Event_Handlers.md)
- [Event Parameters](Event_Parameters.md)
- [Event Handler Keywords](Event_Handler_Keywords.md)
- [Run-Time Errors](Run_Time_Errors.md)
- [Run-Time Binding](DDD_-_Run-Time_Binding.md)
- [Run-Time Dynamic Device Discovery](DDD_-_Run-Time_Dynamic_Device_Discovery.md)
