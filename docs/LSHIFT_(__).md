# LSHIFT (\<\<)

This [Bitwise Operator](Bitwise_operators.md) causes the bits in the associated integer field to be shifted left. This has the effect of multiplying by 2n where n is the number of bit positions to shift.

Note: The symbol \<\< is equivalent to LSHIFT.

For example,

INT2 = INT1 LSHIFT 2

is equivalent to

INT2 = INT1 \<\< 2

Both statements shift INT1 left 2 positions.

Either statement could be replaced with the following:

INT2 = INT1 \* 4

See Also

- [Operator Keywords](Operator_Keywords.md)

- [Operator Precedence](Operator_Precedence.md)

- [Arithmetic Operators](Arithmetic_operators.md)

- [Assignment Operators](Assignment_operators.md)

- [Bitwise Operators](Bitwise_operators.md)

- [Logical Operators](Logical_operators.md)

- [Relational Operators](Relational_operators.md)

