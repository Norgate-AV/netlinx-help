---
title: WC_CONCAT_STRING
---

# WC_CONCAT_STRING

This keyword concatenates two WIDECHAR arrays.

Syntax:

```
WIDECHAR\[\] WD_CONCAT_STRING(WIDECHAR STR1\[\], WIDECHAR STR2\[\])

```

Parameters:

- STR1 – the first WIDECHAR string to be concatenated.

- STR2 – the first WIDECHAR string to be concatenated.

Result:

Result is a WIDECHAR string which concatenates STR1 and STR2

Example:

```
wcMyString = WC_CONCAT_STRING(wcString1,wcString2)

```

See Also

- [Unicode Keywords](Unicode_Keywords.md)
