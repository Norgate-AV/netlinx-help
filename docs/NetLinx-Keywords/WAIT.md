---
title: WAIT
---

# WAIT

This keyword is used to delay execution of one or more statements for a
specified period of time.

Syntax:

```c linenums="1"
WAIT time ['<name>']

{

 (\* wait statements \*)

}
```

The NetLinx interpreter accepts any type of number (including Floats and
Doubles) for WAIT times but it casts them to an unsigned 32-bit number, i.e. a
long.

So the max wait time 2^32 or 4294967295 100th's of a second.

Example:

```c linenums="1"
WAIT 42949672l9.5 // wait ~1.36 years

{

// do something a long time from now

}
```

See Also

- [WAITs](Waits.md)
- [WAIT Keywords](WAIT_Keywords.md)
