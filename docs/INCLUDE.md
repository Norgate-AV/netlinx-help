---
title: INCLUDE
---

# INCLUDE

The keyword allows you to include programming instructions from an external file and have those instructions inserted at any point in the program.

Syntax:

```c linenums="1"
INCLUDE '\<filename\>'

```
- The parameter filename can be any valid (long) filename.
- If the file extension is omitted, "AXI" is assumed.
- The contents of the file can be thought of as being copied to the location of the INCLUDE statement.
-  An INCLUDE statement can appear anywhere in a program.

Note: There is no difference in functionality between the INCLUDE reserved identifier and the [\#INCLUDE](_INCLUDE.md) compiler directive. INCLUDE is supported for backward-compatibility to Axcess.

See Also

- [File Operation Keywords](File_Operation_Keywords.md)
