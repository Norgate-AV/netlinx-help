---
title: SSH_CLIENT_CLOSE
---

# SSH_CLIENT_CLOSE

This function closes an open SSH communication port with a server.

Syntax:

```
slong SSH_CLIENT_CLOSE(INTEGER LocalPort)

```
Parameters:

- LocalPort - A user-defined (non-zero) integer value representing the local port on the client machine to use for this conversation. This local port number must be passed to [SSH_CLIENT_OPEN](SSH_CLIENT_OPEN.md) to open the conversation.

Returns:

This function always returns 0. Errors are returned via the [DATA_EVENT](DATA_EVENT.md) [ONERROR](ONERROR.md) method. The following errors may be returned from the call:

- 2 - General failure (out of memory)

- 4 - Unknown host

- 6 - Connection refused

- 7 - Connection timed out

- 8 - Unknown connection error

- 9 - Already closed

- 14 - Local port already used

- 16 - Too many open sockets

Example:

```
SSH_CLIENT_CLOSE(5000)

```
