---
title: DEFINE_VARIABLE
---

# DEFINE_VARIABLE

This program section is used to declare global variables. Any variable defined
in this section is static (its value is maintained throughout the duration of
program execution) with module scope (it is accessible from any instruction in
the current module).

- Variables may be declared volatile, non-volatile or persistent. Variables are
  by default stored in non-volatile memory, in other words, their values are
  maintained when the system is powered-down. The keyword
  [VOLATILE](VOLATILE.md) is used to declare a variable that is stored in
  volatile memory.

- Both volatile and non-volatile variables are initialized to zero when the
  system is reloaded. On power-down/restart, only volatile variables are
  re-initialized to zero; non-volatile variable will retain their values.

- A variable declared as [PERSISTENT](PERSISTENT.md) is initialized to zero when
  the program is first loaded but will retain its value after power-down or
  reload.

Example:

```
DEFINE_VARIABLE

```

INTEGER INT1

FLOAT FP1

VOLATILE INTEGER BIGARRAY\[1000\]\[1000\]

Note: 1000 marks the limit of the string.

See Also

- [Variables](Variables.md)

- [DEFINE Keywords](DEFINE_Keywords.md)

- [Variables Keywords](Variables_Keywords.md)
