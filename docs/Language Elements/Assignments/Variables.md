---
title: Variables
---

# Variables

NetLinx provides support for several different types of variables distinguished
by attributes such as scope, constancy and persistence.

Scope differentiates the two basic classes of NetLinx variables:

- Local variable: variable declared within a subroutine or function whose scope
  is limited to that subroutine or function. See
  [Local Variables](Local_Variables.md) for details.

- Global variable: variable declared in the
  [DEFINE_VARIABLE](DEFINE_VARIABLE.md) section and its scope extends throughout
  the module in which it is declared. See
  [Global Variables](Global_Variables.md) for details.

Any variable may also be assigned the attribute [CONSTANT](CONSTANT.md). This
declares a variable to be immutable (cannot change at run-time). The variable
must be initialized as part of its declaration if this keyword is used.

The persistence of a variable is controlled through the
[NON_VOLATILE](NON_VOLATILE.md), [VOLATILE](VOLATILE.md) and
[PERSISTENT](PERSISTENT.md) keywords:

- Non-volatile variables:A variable declared with the
  [NON_VOLATILE](NON_VOLATILE.md) keyword is stored in non-volatile memory. It
  will retain its value in the event of a system power-down, but is reset to
  zero if the program is reloaded. Unless specified otherwise, all variables are
  stored in non-volatile memory.

- Volatile variables:A variable declared with the [VOLATILE](VOLATILE.md)
  keyword is stored in volatile memory and reset to zero after either power-down
  or reload. Volatile memory is generally faster and more plentiful than
  non-volatile memory. For this reason, you should use the VOLATILE keyword when
  declaring large data arrays where persistence of the data is not a
  requirement.

- Persistent variables:If a variable is declared with the
  [PERSISTENT](PERSISTENT.md) keyword, it is initialized to zero the first time
  the program is loaded but will retain its value after either power-down or
  reload. See [Persistent Variables](Persistent_Variables.md) for details.

If the data type is omitted from the variable definition, the following defaults
are assumed:

- Single variables are [INTEGER](INTEGER.md) type

- Arrays are [CHAR](CHAR.md) type

See Also

- [Variables & Constants](Variables_&_Constants.md)

- [Local Variables](Local_Variables.md)

- [Global Variables](Global_Variables.md)

- [Persistent Variables](Persistent_Variables.md)

- [Variables Keywords](Variables_Keywords.md)

- [DEFINE_MUTUALLY_EXCLUSIVE and Variables](DEFINE_MUTUALLY_EXCLUSIVE_and_Variables.md)

- [Constants](Constants.md)
