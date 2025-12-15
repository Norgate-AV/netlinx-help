# POWER_VALUE

Note: Math functions are supported by NetLinx Controller firmware version 4 or higher.  

Returns BASE raised to the power EXPONENT.  

POWER_VALUE(CONSTANT VARIANT BASE, CONSTANT VARIANT EXPONENT)

Where BASE and EXPONENT can be any intrinsic type (INTEGER, FLOAT,  DOUBLE, etc).

The following combinations are error conditions which will return 0:

- BASE = 0 and EXPONENT=negative

- BASE=negative and EXPONENT=non-integral value

See Also

- [EXP_VALUE(X)](EXP_VALUE(X).htm)

- [LOG_VALUE(X)](LOG_VALUE(X).htm)

- [LOG10_VALUE(X)](LOG10_VALUE(X).htm)

- [SQRT_VALUE(X)](SQRT_VALUE(X).htm)
