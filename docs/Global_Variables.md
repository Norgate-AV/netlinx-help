---
title: Global_Variables
---

# Global Variables

Global variables are defined in the [DEFINE_VARIABLE](DEFINE_VARIABLE.md) section of any program module. For example,

DEFINE_VARIABLE

CONSTANT INTEGER MAXLEN = 64

CHAR STR\[MAXLEN\] = 'No errors were found.'

INTEGER ARRAY\[ \] = {100, 200, 300}

A global variable is accessible throughout the module in which it is defined. Global variables retain their value for as long as the program runs. They may retain their value after powering down or reloading the system depending on the variable’s persistence attributes ([VOLATILE](VOLATILE.md) and [PERSISTENT](PERSISTENT.md)).

The general form of a global variable definition is:

\[NON_VOLATILE \| VOLATILE \| PERSISTENT\] \[CONSTANT\] \[\<type\>\] name \[= \<value\>\]

Note: Modules are reusable NetLinx sub-programs that can be inserted into the main program.

See Also

- [NetLinx Modules](NetLinx_Modules_Advanced_Programmers_.md)

- [Variables](Variables.md)

- [Variables & Constants](Variables_&_Constants.md)

- [Variables Keywords](Variables_Keywords.md)

