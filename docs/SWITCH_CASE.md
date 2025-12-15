---
title: SWITCH_CASE
---

# SWITCH...CASE

SWITCH...CASE statements provide selective execution of code blocks evaluated by a single condition. The value of the SWITCH expression is tested against each CASE value (a numeric constant or a string literal).

- If a match is found, the statements associated with the CASE are executed. All other CASE statements are ignored.
- If no match is found, the [DEFAULT](DEFAULT.md) case statements (if any) are executed.

Structure:

SWITCH (x)

{

CASE 1 : //do stuff when x = 1

{

}

CASE 2 : //do stuff when x = 2

{

}

default : // do stuff when x is not 1 or 2

{

}

}

This is programmatically the same as:

If (x = 1) //do stuff when x = 1

{

}

else if (x=2) //do stuff when x = 2

{

}

else // do stuff when x is not 1 or 2

Rules:

- The SWITCH expression is evaluated only once.
- Only the statements associated with the first case that matches the value of the expression are executed. Multiple CASE statements can be stacked within the SWITCH...CASE statement. If the value matches one of the CASE statements, the statements associated with the stack will be executed.
- If no CASE matches the SWITCH expression, then the statements under the default case (if available) are executed. The default statement must be the last case within the SWITCH...CASE, otherwise the remaining case statements will not execute.
- All cases must be unique.
- Braces should be used to bracket the statements in a case. They are required only if variables are declared within the case.
- The [BREAK](BREAK.md) statement applies to the SWITCH and takes execution to the end of the SWITCH. Unlike C and C++, cases do not fall through to the next case if a break is not used. Because of this, BREAK statements are not required between cases.

For example:

SWITCH (var)

{

     CASE 1:

     {

               (\*statements go here\*)

     BREAK

     }

     CASE 3:

     {

               (\*statements go here\*)

     BREAK

     }

     CASE 5:

     {

               (\*statements go here\*)

     BREAK

     }

     DEFAULT:

     {

               (\*statements go here\*)

     BREAK

     }

}

See Also:

- [Conditional Keywords](Conditional_Keywords.md)
- [BREAK](BREAK.md)
