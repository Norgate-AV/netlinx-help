---
title: Constants
---

# Constants

Constants are defined in the [DEFINE_CONSTANT](DEFINE_CONSTANT.md) section.

DEFINE_CONSTANT

\<constant name\> = \<constant expression\>

- The scope of a constant extends throughout the module or program in which it is defined.
- The name assigned to a constant must be unique among all other identifiers defined in the module or program.
- Constants may be assigned expressions that consist only of other constants and Operators.
- Variables are not allowed in constant expressions.

DEFINE_CONSTANT

VALUE_OFFSET = 500

VALUE1 = VALUE_OFFSET + 1

STR1 = 'This is a string constant.'

Constants can be used anywhere that a numeric or string constant is allowed.

The value assigned to a constant can be specified in one the formats listed below:

|                      |                      |            |
|----------------------|----------------------|------------|
| Type                 | Format               | Example    |
| Decimal Integer      | 0000                 | 1500       |
| Hexadecimal Integer  | \$000                | \$DE60     |
| Floating Point       | 000.0                | 924.5      |
| Exponential Notation | 0.0e0                | 1.5e-12    |
| Character            | ‘c’ or \<char code\> | ‘R’ or 255 |
| String Literal       | ‘ ssss’              | ‘Reverse’  |

See Also

- [Variables & Constants](Variables_&_Constants.md)
- [Variables](Variables.md)
- [Local Variables](Local_Variables.md)
- [Global Variables](Global_Variables.md)
- [Persistent Variables](Persistent_Variables.md)
- [Variables Keywords](Variables_Keywords.md)
- [DEFINE_MUTUALLY_EXCLUSIVE and Variables](DEFINE_MUTUALLY_EXCLUSIVE_and_Variables.md)

