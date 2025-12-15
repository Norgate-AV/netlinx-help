# DEFINE_MODULE

This keyword declares a module to be used by either the main program or by another module. It is the counterpart to the [MODULE_NAME](MODULE_NAME.md) entry that appears as part of the implementation of the module.

Syntax:

```
DEFINE_MODULE '\<module name\>' InstanceName(\<parameter list\>)

```
Parameters:

- \<module name\> - is the name of the module as specified in the MODULE_NAME statement in the module implementation file.

- InstanceName - is the name to assign to the instance of the module.

- \<parameter list\> - is the list of parameters that is available to the module.

Technically, modules can contain declarations to other modules, provided that no circular references are involved. However, because different instances of the same module must not be separated by instances of a different module, it is highly recommended that you do not declare modules from within other modules if you have multiple declarations of the parent module they will then be separated by the declarations of the child module.

See Also

- [DEFINE Keywords](DEFINE_Keywords.md)

- [Module Keywords](Module_Keywords.md)

- [NetLinx Modules (Advanced Programmers)](NetLinx_Modules_Advanced_Programmers_.md)

- [Defining a Module](Defining_a_Module.md)

