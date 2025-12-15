---
title: RANDOM_NUMBER
---

# RANDOM_NUMBER

This function returns a random number X in the range 0 \<= X \< Max.

Syntax:

```c linenums="1"
LONG RANDOM_NUMBER (LONG Max)

```
Parameters:

- Max - Unsigned long integer (must be greater than zero) that will serve as the upper limit for the random number generator.

Result:

- An unsigned long integer \>= 0 and \< Max.

Example:

```c linenums="1"
Num = RANDOM_NUMBER(1000) // 0 \<= Num \< 1000

```
See Also

- [Variables Keywords](Variables_Keywords.md)

