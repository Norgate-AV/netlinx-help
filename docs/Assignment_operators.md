# Assignment Operators

The Assignment Operators are described below:

|          |                |
|----------|----------------|
| Operator | Function       |
| =        | Assignment     |
| ++       | Increment by 1 |
| --       | Decrement by 1 |

An Assignment Operator may appear only once in a single NetLinx statement.

The following rules apply to the use of assignment Operators:

The "=" Operator may be used to assign

- Expressions to [intrinsic type](Intrinsic_Data_Types.md) variables

- Arrays to other array of matching size and type

- Structures to other structures of the same type

The "++" and "–" Operators are statements and cannot appear within expressions.

Example:

```
FOR (I=1; I\<10; I++) // Legal

```
I = j++              // Illegal

See Also

- [Arithmetic Operators](Arithmetic_operators.md)

- [Bitwise Operators](Bitwise_operators.md)

- [Logical Operators](Logical_operators.md)

- [Relational Operators](Relational_operators.md)

- [Operator Precedence](Operator_Precedence.md)

