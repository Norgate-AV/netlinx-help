---
title: Defining_a_Module
---

# Defining a Module

To use a module in a program, you must declare it using the [DEFINE_MODULE](DEFINE_MODULE.md) keyword. This tells the NetLinx compiler to add the module to the program, effectively merging the module’s event handling and mainline code with the containing program (or module). In other words, the program will have one event table and one mainline routine consisting of code from the main program and all modules declared using the MODULE statement.

The example below demonstrates how a NetLinx module is incorporated into a main program. In this example the main program has no event table or mainline code.

PROGRAM_NAME = 'Switcher Program'

 

DEFINE_DEVICE

SW1 = 5

SW2 = 6

SW3 = 7

TP = 128

 

DEFINE_VARIABLE

 

INTEGER nInputs = 5

INTEGER nOutputs = 4

INTEGER nLevels = 3

 

DEVCHAN InputDCSet\[ \] = {{TP,1}, {TP,2}, {TP,3}, {TP,4}, {TP,5}}

DEVCHAN OutputDCSet\[ \] = {{TP,6}, {TP,7}, {TP,8}, {TP,9}}

DEVCHAN LevelDCSet\[ \] = {{TP,10}, {TP,11}, {TP,12}}

DEVCHAN TakeDCSet\[ \] = {{TP,13}}

 

DEV\[ \] Switchers = {SW1, SW2, SW3}

 

DEFINE_MODULE 'XYZ Switcher' ModXYZ(nInputs, nOutputs, nLevels, InputDCSet, OutputDCSet,

 LevelDCSet, TakeDCSet, Switchers)

A module is defined by the [MODULE_NAME](MODULE_NAME.md) entry on the first line of the file.

Syntax:

```c linenums="1"
MODULE_NAME = '\<module name\>' \[(\<parameter list\>)\]

```
The MODULE_NAME entry identifies the file as containing a NetLinx module, as opposed to a standard NetLinx source code file. The module name is any valid string literal not to exceed 64 characters. A file can contain only one module and the file name must be the same as the module name with the addition of the ".AXS" extension.

Module parameters behave exactly like subroutine parameters; the parameter list is optional. The value for each parameter is set either by the main program or another module. If the value of a parameter is changed, both the main program and the module see the change.

- Constants and expressions cannot be used as arguments in the parameter list.

- [Persistent variables](Persistent_Variables.md) do not work in Modules.

All parameters to a module must be on of the intrinsic types: [CHAR](CHAR.md), [INTEGER](INTEGER.md), [SINTEGER](SINTEGER.md), [LONG](LONG.md), [SLONG](SLONG.md), [FLOAT](FLOAT.md), [DOUBLE](DOUBLE.md), [DEV](DEV.md), [DEVCHAN](DEVCHAN.md) or [DEVLEV](DEVLEV.md). Also, any array of any of the  intrinsic types can be used.

The example below defines a module named ModuleExample.

Aside from the MODULE_NAME entry, the code looks like any standard NetLinx source code file:

MODULE_NAME = 'Switcher' (INTEGER nInputs,

INTEGER nOutputs,

INTEGER nLevels,

DEVCHAN InputDCSet\[\],

DEVCHAN OutputDCSet\[\],

DEVCHAN LevelDCSet\[\],

DEVCHAN TakeDCSet\[\],

DEV Switchers\[\])

 

 

DEFINE_CONSTANT

MaxIn = 10

MaxOut = 10

MaxLev = 10

 

DEFINE_VARIABLE

INTEGER SwitchPending\[MaxOut\]\[MaxIn\]\[MaxLev\]

INTEGER SwitchStatus\[MaxOut\]\[MaxIn\]\[MaxLev\]

INTEGER Input, nLevel

 

DEFINE_FUNCTION DoSwitch()

{

 INTEGER Output

 FOR (Output = 1; Output \<= nOutputs; Output = Output + 1)

 {

  IF (SwitchPending\[Output\]\[Input\]\[nLevel\] \<\> 0)

  {

   SEND_STRING Switchers, SwitchString(Input, Output, nLevel)

  }

 

  SwitchStatus\[Output\]\[Input\]\[nLevel\] = SwitchPending\[Output\]\[Input\]\[nLevel\]

  SwitchPending\[Output\]\[Input\]\[nLevel\] = 0

  OFF\[OutputDCSet\[Output\]\]

 }

}

 

DEFINE_FUNCTION char\[10\] SwitchString(INTEGER In, INTEGER Out, INTEGER cLevel)

{

 RETURN '' // return an empty string

}

 

DEFINE_START

Input = 1

nLevel = 1

ON\[InputDCSet\[Input\]\]

ON\[LevelDCSet\[nLevel\] \]

 

DEFINE_EVENT

 

BUTTON_EVENT\[InputDCSet\]

{

 PUSH:

 {

  Input = get_last(InputDCSet)

  ON\[Input\]

 }

}

 

BUTTON_EVENT\[OutputDCSet\]

{

 PUSH:

 {

  SwitchPending\[get_last(OutputDCSet)\]\[Input\]\[nLevel\] =

   !SwitchPending\[get_last(OutputDCSet)\]\[Input\]\[nLevel\]

 

  \[OutputDCSet\[get_last(OutputDCSet)\]\] =

   SwitchPending\[get_last(OutputDCSet)\]\[Input\]\[nLevel\]

 

}

}

 

BUTTON_EVENT\[LevelDCSet\]

{

 PUSH:

 {

  nLevel = get_last(LevelDCSet)

  ON\[nLevel\]

 }

}

 

BUTTON_EVENT\[TakeDCSet\]

{

 PUSH:

 {

  DoSwitch()

  PULSE\[TakeDCSet\]

 }

}

Technically, modules can contain declarations to other modules, provided that no circular references are involved.

However, because different instances of the same module must not be separated by instances of a different module, it is highly recommended that you do not declare modules from within other modules if you have multiple declarations of the parent module they will then be separated by the declarations of the child module.

See Also

- [NetLinx Modules](NetLinx_Modules_Advanced_Programmers_.md)

- [Module Keywords](Module_Keywords.md)

