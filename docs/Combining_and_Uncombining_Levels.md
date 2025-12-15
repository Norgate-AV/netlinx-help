---
title: Combining_and_Uncombining_Levels
---

# Combining and Uncombining Levels

The NetLinx functions [COMBINE_LEVELS](COMBINE_LEVELS.md) and [UNCOMBINE_LEVELS](UNCOMBINE_LEVELS.md) are used within events and mainline code to dynamically change what levels are connected to each other.

It is recommended that a Virtual [DEVLEV](DEVLEV.md) set be used as the first DEVLEV set in the COMBINE_LEVELS function.

The format for COMBINE_LEVELS and UNCOMBINE_LEVELS is:

SLONG COMBINE_LEVELS (\<virtual DEVLEV\>, \<DEVLEV1\>, \<DEVLEV2\> …)

SLONG UNCOMBINE_LEVELS (\<virtual DEVLEV\>)

DEVLEV structures defined within the COMBINE_LEVELS are either individual DEVLEV structures or one dimension of a DEVLEV array. Any reference to the levels is handled through the first device in the list.

The following example code illustrates how to dynamically combine and uncombine levels utilizing  the COMBINE_LEVELS and UNCOMBINE_LEVELS keywords.

DEFINE_DEVICE

VIRTUAL1 = 33000

TP1 = 128

TP2 = 129

TP3 = 130

 

TP4 = 131

 

DEFINE_PROGRAM

 (\*Activate dynamic device combine\*)

PUSH\[TP4,1\]

{

COMBINE_LEVELS(VIRTUAL1,1,TP1,1,TP2,1,TP3,1)

}

 

 (\*Remove dynamic device combine\*)

PUSH\[TP4,1\]

{

UNCOMBINE_LEVELS(VIRTUAL1,1)

}

See Also

- [Combining and Uncombining Channels](Combining_and_Uncombining_Channels.md)
- [Combining and Uncombining Devices](Combining_and_Uncombining_Devices.md)
- [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)
