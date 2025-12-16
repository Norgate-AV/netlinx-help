---
title: WC_COMPARE_STRING
---

# WC_COMPARE_STRING

This keyword compares two Unicode strings.

 If either string contains a '?' character, the matching character in the other
string is not compared.

Note: The '?' is equivalent to a wildcard.

Syntax::

INTEGER WC_COMPARE_STRING(WIDECHAR STR1\[\], WIDECHAR STR2\[\])

Parameters:

- STR1 – the first WIDECHAR string to be compared.

- STR2 – the first WIDECHAR string to be compared.

Result: The returned result can only be True (1) or False (0).

-  0 = the strings don't match

-  1 = the strings are the same

Example:

```
See [COMPARE_STRING](COMPARE_STRING.md) for a code example.

```

See Also

- [Unicode Keywords](Unicode_Keywords.md)
