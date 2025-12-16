---
title: AMX_LOG
---

# AMX_LOG

Note: This command is supported by NetLinx Controller firmware version 4 or higher.

Sends the specified message to the NetLinx master’s logging facilities if the current log level setting is at least as large as LEVEL.  For example, if the current log level setting is AMX_WARNING, calling log with level of AMX_ERROR will cause a log, while AMX_INFO would not.

The AMX_LOG function is meant to replace the "SEND_STRING 0,…" log method.

AMX_LOG(CONSTANT INTEGER LEVEL, CHAR MSG[])

Where level is one of the following values:

- INTEGER AMX_ERROR = 1;
- INTEGER AMX_WARNING = 2;
- INTEGER AMX_INFO = 3;
- INTEGER AMX_DEBUG = 4;

Example:

```c linenums="1"
AMX_LOG(AMX_ERROR,"'FAILURE OCCURRED, VALUE=',ITOA(ERR_VAL)")
```

See Also

- [SET_LOG_LEVEL](SET_LOG_LEVEL.md)
- [GET_LOG_LEVEL](GET_LOG_LEVEL.md)
