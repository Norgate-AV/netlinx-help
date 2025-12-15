# DEFINE_CONSTANT

This keyword is used to define program constants.

The value of a constant cannot be changed within the program.

Example:

```
DEFINE_CONSTANT

```
PLAY = 1

STOP = 2

STRING='HELLO'

Note: Expressions defined in the DEFINE_CONSTANT section  cannot contain any variables.

The standard format for DEFINE_CONSTANT is:

\<constant name\> = \<constant expression\>

NetLinx allows variables to be defined as constants in the DEFINE_VARIABLE section of the program or module, and in the LOCAL_VAR section of a DEFINE_CALL or a DEFINE_FUNCTION.

The scope of the constant extends throughout the module in which it is defined. If the DEFINE_CONSTANT section appears in the main program or in an include file, the constant's scope extends globally throughout the program.

DEFINE_CONSTANT accepts data in these formats:

|                      |                      |            |
|----------------------|----------------------|------------|
| Types                | Formats              | Examples   |
| Decimal Integer      | 0000                 | 1500       |
| Hexadecimal Integer  | \$000                | \$DE60     |
| Floating Point       | 000.0                | 924.5      |
| Exponential Notation | 0.0e0                | 5e-12      |
| Character            | 'c' or \<char code\> | 'R' or 255 |
| String Literal       | 'ssss’               | 'Reverse'  |

See Also

- [DEFINE Keywords](DEFINE_Keywords.md)

- [CONSTANT](CONSTANT.md)

