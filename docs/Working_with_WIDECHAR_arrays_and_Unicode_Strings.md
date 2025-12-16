---
title: Working_with_WIDECHAR_arrays_and_Unicode_Strings
---

# Working with WIDECHAR arrays and Unicode Strings

Working with [WIDECHAR](WIDECHAR.md) arrays and [Unicode](Working_With_UniCode.md) strings is very similar to working with [CHAR](CHAR.md) arrays and ASCII strings.

Most operations that can be performed on a CHAR array can be performed on a WIDECHAR array.  For instance, to assign a string to a variable use this syntax:

```c linenums="1"
wcMyString = _WC(‘My String’)
```

The string functions defined for CHAR arrays have been defined for WIDECHAR array for use in Unicode programming.

These functions allow you to operate on strings similar to the way you would with CHAR array.  For instance, to remove the first 3 characters from a WIDECHAR array and return those characters as a WIDECHAR array, use [WC_GET_BUFFER_STRING](WC_GET_BUFFER_STRING.md):

```c linenums="1"
WCRemoved = WC_GET_BUFFER_STRING(wcMyString,3)
```

You will find that most other functions work exactly as their CHAR counterpart do except they work on and return WIDECHAR arrays.

The list of Unicode compatible functions is:

- [WC_COMPARE_STRING](WC_COMPARE_STRING.md)
- [WC_GET_BUFFER_CHAR](WC_GET_BUFFER_CHAR.md)
- [WC_GET_BUFFER_STRING](WC_GET_BUFFER_STRING.md)
- [WC_LEFT_STRING](WC_LEFT_STRING.md)
- [WC_FIND_STRING](WC_FIND_STRING.md)
- [WC_LENGTH_STRING](WC_LENGTH_STRING.md)
- [WC_LOWER_STRING](WC_LOWER_STRING.md)
- [WC_MAX_LENGTH_STRING](WC_MAX_LENGTH_STRING.md)
- [WC_MID_STRING](WC_MID_STRING.md)
- [WC_REMOVE_STRING](WC_REMOVE_STRING.md)
- [WC_RIGHT_STRING](WC_RIGHT_STRING.md)
- [WC_SET_LENGTH_STRING](WC_SET_LENGTH_STRING.md)
- [WC_UPPER_STRING](WC_UPPER_STRING.md)

See Also

- [Working With Unicode](Working_With_UniCode.md)
- [Reading and Writing to Files](Reading_and_Writing_to_Files.md)
- [Unicode-Related Compiler Errors](Unicode-Related_Compiler_Errors.md)
