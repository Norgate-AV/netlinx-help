---
title: SELECT_ACTIVE
---

# SELECT...ACTIVE

The SELECT…ACTIVE statement provides a programming structure for selective
execution of code blocks based on the evaluation of a series of conditions.

- The first block whose ACTIVE condition evaluates to true is executed; the
  remaining blocks are ignored.
- If no ACTIVE condition evaluates to true, no statements are executed.

Example:

```c linenums="1"
SELECT

{
```

 ACTIVE (<condition 1>) :

 {

  (\* statements for condition 1\*)

 }

 ACTIVE (<condition 2>) :

 {

  (\* statements for condition 2\*)

 }

 ACTIVE (<condition n>) :

 {

 ACTIVE (1)

  (\* statements for condition n\*)

 }

}

Regarding SELECT...ACTIVE statements:

- Only the statements associated with the first condition evaluated to true are
  executed
- If no condition evaluates to true, then no statements are executed
- Braces underneath individual ACTIVE statements are required only if multiple
  statements are assigned to a given condition

See Also

- [Conditional Keywords](Conditional_Keywords.md)
