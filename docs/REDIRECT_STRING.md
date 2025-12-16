---
title: REDIRECT_STRING
---

# REDIRECT_STRING

This command is used to pass all strings from device 1 to device 2 and all
strings from device 2 to device 1. This is called a redirection and you can
assign up to eight of them at one time.

Syntax:

```c linenums="1"
REDIRECT_STRING (Number, Device1, Device2)
```

Parameters:

- Number -  identifies the particular redirection (1-8).

To cancel a redirection, pass zero for Device1 and Device2.

Note: Redirections are lost if system power is turned off.

See Also

- [STRING Keywords](STRING_Keywords.md)
