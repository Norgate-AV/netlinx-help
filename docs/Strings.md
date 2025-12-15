---
title: Strings
---

# Strings

A string is an array of characters of known length. This length may be less than the dimensioned length.

Example:

```c linenums="1"
DEFINE_VARIABLE

```
CHAR MyString\[32\]

INTEGER StrLen

 

DEFINE_START

MyString = 'STOP'

StrLen = LENGTH_STRING(MyString)

In the example above, StrLen holds the value 4, the length of MyString.

The length of MyString can be anywhere from 0 to 32.

If an attempt is made to assign a string longer than the capacity of the destination string, the copied string is truncated to fit. The string length is implicitly set when a string literal, string expression or variable is assigned to the string.

The function [SET_LENGTH_STRING](SET_LENGTH_STRING.md) can be used to explicitly set the length of a string to any arbitrary length between 0 and the dimension of the character array.

Example:

```c linenums="1"
SET_LENGTH_STRING(MyString, 3)

```
This causes the contents of MyString to read ‘STO’, even though the character ‘P’ still resides in MYSTRING\[4\].

A string expression is a string enclosed in double quotes containing a series of constants and/or variables evaluated at run-time to form a string result. String expressions can contain up to 16000 characters consisting of string literals, variables, arrays, and ASCII values between 0 and 255.

Example:

```c linenums="1"
CHAR StrExp\[6\]

```
StrExp = "STOP, 25, 'OFF', X"

In the example above, the string expression contains the constant STOP, the value 25, the string literal ‘OFF’, and the variable X. Assuming STOP is 2 and X = 5, the string expression will evaluate to  
"2, 25, ‘OFF’, 5".

Note: While Axcess automatically converted data types to strings when necessary, in NetLinx, you must be more precise. NetLinx does not accommodate converting data types to strings, and requires that all strings be enclosed in double-quotes.

For example,

In Axcess, you could use:  
ATOI(STRING)

Where NetLinx requires:  
ATOI("STRING")

See Also

- [Wide Strings](Wide_Strings.md)

