---
title: SET_LOG_LEVEL
---

# SET_LOG_LEVEL

Sets the current log level for the program.  All subsequent logs at the
specified level or lower will cause a log message out the NetLinx master’s
logging facilities.  

SET_LOG_LEVEL(CONSTANT INTEGER LEVEL)

The four valid log levels are:

- INTEGER AMX_ERROR = 1

- INTEGER AMX_WARNING = 2

- INTEGER AMX_INFO = 3

- INTEGER AMX_DEBUG = 4

See Also

- [GET_LOG_LEVEL](GET_LOG_LEVEL.md)

- AMX_LOG
