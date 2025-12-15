---
title: GET_LAST
---

# GET_LAST

This function returns the index of the array element that most recently caused an [Event Handler](Event_Handlers.md) to be triggered.

Example:

```
DEFINE_VARIABLE

```
DEVCHAN dcMyDCSet\[\] = { {TP,5}, {TP,4}, {TP,3}, {TP,2},

{TP,1}}

INTEGER Index

BUTTON_EVENT\[dcMyDCSet\]

{

   PUSH:

   {

   Index = GET_LAST(dcMyDCSet)

   Switch (Index)

   {

      Case 1: {} (\* Button 5 was pressed \*)

      Case 2: {} (\* Button 4 was pressed \*)

      Case 3: {} (\* Button 3 was pressed \*)

      Case 4: {} (\* Button 2 was pressed \*)

      Case 5: {} (\* Button 1 was pressed \*)

   }

   }

}

Result:

- 0: No event was triggered using this array.

- \>0: The index that causes an event to be triggered.

Since the [PUSH](PUSH.md) and [RELEASE](RELEASE.md) keywords can be written using [DEVCHAN](DEVCHAN.md) arrays, this function can also be used to determine which element causes a push or release to be triggered.

- The function can be called anywhere in code but is usually called from within an event handler.

- A classic application of this function is to determine the keypad number pressed when the channel codes for the keypad are out of order, which they typically are for a wireless transmitter.

See Also

- [Event Parameters](Event_Parameters.md)

- [GET Keywords](GET_Keywords.md)

- [DEFINE_VARIABLE](DEFINE_VARIABLE.md)

