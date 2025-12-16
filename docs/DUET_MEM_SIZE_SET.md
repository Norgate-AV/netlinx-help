---
title: DUET_MEM_SIZE_SET
---

# DUET_MEM_SIZE_SET

Set the amount of memory allocated for Duet Java pool (the current Java memory heap size), measured in MB.

Syntax:

```c linenums="1"
DUET_MEM_SIZE_SET(int)
```

This feature is used so that if a NetLinx program requires a certain size of memory be allotted for its currently used Duet Modules, it can be reserved on the target Master.

This setting does not take effect until the next reboot.

Valid values are:

- 2 - 8 for 32MB systems
- 2 - 36 for 64MB systems

Note:" DUET_MEM_SIZE_SET(int)" should call REBOOT() following a set.

See Also

- [DUET_MEM_SIZE_GET](DUET_MEM_SIZE_GET.md)
- [NetLinx Modules](NetLinx_Modules_Advanced_Programmers_.md)
- [Defining a Module](Defining_a_Module.md)
