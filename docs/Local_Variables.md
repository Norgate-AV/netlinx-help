# Local Variables

Local variables are restricted in scope to the statement block in which they are declared. A statement block is one or more NetLinx statements enclosed in a pair of braces, like the blocks following subroutines, functions, conditionals, loops, waits, and so on.

Local variables must be declared immediately after the opening brace of a block but before the first executable statement. To provide compatibility with the Axcess language, local variables may be declared right before the opening brace for [DEFINE_CALL](DEFINE_CALL.md) declarations only. For example, both formats shown below are legal in the NetLinx language:

DEFINE_CALL 'My Subroutine' (INTEGER INT1)

LOCAL_VAR INTEGER INT2

{

 (\* body of subroutine \*)

}

 

DEFINE_CALL 'My Subroutine' (INTEGER INT1)

{

 LOCAL_VAR INTEGER INT2

 (\* body of subroutine \*)

}

The scope of a local variable is restricted to the statement block in which it is declared. A local variable is either static or non-static, depending on whether it is declared as [LOCAL_VAR](LOCAL_VAR.md) or [STACK_VAR](STACK_VAR.md):

- The keyword [LOCAL_VAR](LOCAL_VAR.md) specifies a static variable. A static variable's value is initialized the first time the statement block in which it is declared is executed and retained after execution of the statement block has finished.

- The [STACK_VAR](STACK_VAR.md) keyword specifies a non-static variable. A non-static variable's value is re-initialized every time the statement block in which it is declared is executed.

- If neither the [LOCAL_VAR](LOCAL_VAR.md) nor the [STACK_VAR](STACK_VAR.md) keyword is specified, STACK_VAR is assumed (default).

Example:

```
IF (X \> 10)

{

```
 LOCAL_VAR INTEGER INT2  // static (permanent)

 STACK_VAR CHAR ARRAY1\[10\] // non-static (temporary)

 (\* statements \*)

}

LOCAL_VAR and STACK_VAR can be used interchangeably in any statement block except for waits. Only LOCAL_VAR variables may be declared inside a wait block.

Example:

```
WAIT 10, 'My Wait Name'

{

```
 LOCAL_VAR CHAR TempBuf\[80\]

 (\* statements \*)

}

A name assigned to a local variable must be unique within the statement block in which it is declared and any statement block enclosing that block. Therefore, non-nested statement blocks can define the same local variable name without conflict.

Example:

```
DEFINE_FUNCTION integer MyFunc(INTEGER nFlag)

{

```
 LOCAL_VAR INTEGER n

 

 IF (nFlag \> 0)

 {

  LOCAL_VAR INTEGER n  // illegal declaration

  .

  .

 }

.

.

}

 

DEFINE_FUNCTION integer MyFunc(INTEGER nFlag)

{

 IF (nFlag \> 0)

 {

  LOCAL_VAR INTEGER n

  .

  .

 }

 else

{

  LOCAL_VAR INTEGER n  // legal declaration

 }

}

If a local variable shares the same name as a global variable, the local variable always takes precedence.

The general form of a static local variable declaration is:

\[LOCAL_VAR\] \[VOLATILE \| PERSISTENT\] \[CONSTANT\]

\[\<type\>\] name \[= \<value\>\]

The general form of the non-static local variable declaration is:

\[STACK_VAR\] \[\<type\>\] name \[= \<value\>\]

Since non-static local variables are allocated on the program stack (a block of memory reserved for allocation of temporary variables), the keywords [VOLATILE](VOLATILE.md), [PERSISTENT](PERSISTENT.md) and [CONSTANT](CONSTANT.md) do not apply.

See Also

- [Variables & Constants](Variables_&_Constants.md)

- [Variables](Variables.md)

- [Global Variables](Global_Variables.md)

- [Persistent Variables](Persistent_Variables.md)

- [Variables Keywords](Variables_Keywords.md)

- [DEFINE_MUTUALLY_EXCLUSIVE and Variables](DEFINE_MUTUALLY_EXCLUSIVE_and_Variables.md)

- [Constants](Constants.md)

