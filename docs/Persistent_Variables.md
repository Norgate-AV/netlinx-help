---
title: Persistent_Variables
---

# Persistent Variables

Persistent variables are NetLinx program variables that maintain their value between updates to the NetLinx program. The user can define a variable to be persistent using the PERSISTENT storage modifier as show below:

PERSISTENT CHAR cMyString\[100\]

All persistent variables are automatically non-volatile. It is not legal to define a variable as [VOLATILE](VOLATILE.md) and [PERSISTENT](PERSISTENT.md).

When a NetLinx program has a persistent variable declared, subsequent downloads of new NetLinx programs containing the same persistent variable will retain the variable settings. By default, non-persistent variables are set to zero after a NetLinx program download. Persistence overrides this behavior by setting the variable in the newly downloaded program to be the same as it was before the download.

Typically, persistent variables are used for saving preset information. Suppose you have a system that contains several PosiTrack camera positioning systems, and that the user interface to the system allows the user to set the position of any of the cameras and record that position for recalling later. The position presets are stored in a non-volatile array variable so they are maintained during a power cycle. Without persistent variables, an update to the NetLinx program would zero out all of the presets the user had stored. With persistent variables, the new NetLinx program can be downloaded and all of the presets remain intact.

When a new NetLinx program is downloaded to the Master, the Master iterates through all non-volatile variables from the new program looking for persistent ones. When it finds a persistent variable in the new program, it searches the old programs persistent variable space for the same variable. When it finds the same variable, the value of the new variable is set to the same value as the old variable. The Master identifies the same variable by verifying the following:

- Variable name
- Variable source location
- Variable type

Therefore, in order for persistence to function properly the name, type, and file location declared must be the same as the previously downloaded NetLinx program. If you changed any of the three, the new persistent variable will not be set with the old variable's value.

Note: Persistent Variables do not work in [Modules](NetLinx_Modules_Advanced_Programmers_.md).

See Also

- [Variables & Constants](Variables_&_Constants.md)
- [Variables](Variables.md)
- [Local Variables](Local_Variables.md)
- [Global Variables](Global_Variables.md)
- [Persistent Variables](Persistent_Variables.md)
- [Variables Keywords](Variables_Keywords.md)
- [DEFINE_MUTUALLY_EXCLUSIVE and Variables](DEFINE_MUTUALLY_EXCLUSIVE_and_Variables.md)
- [Constants](Constants.md)

