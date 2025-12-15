---
title: PERSISTENT
---

# PERSISTENT

If a variable is declared with the PERSISTENT keyword, it is initialized to zero the first time the program is loaded but will retain its value after either power-down or reload.

- The PERSISTENT attribute does not apply to non-static local variables, since non-static local variables are allocated on the program stack (a block of memory reserved for allocation of temporary variables).

- The PERSISTENT attribute does not apply to the individual members of a structure.

Note: [Persistent variables](Persistent_Variables.md) do not work in [Modules](NetLinx_Modules_Advanced_Programmers_.md).

See Also

- [Variables](Variables.md)

- [Persistent Variables](Persistent_Variables.md)

- [Variables Keywords](Variables_Keywords.md)

