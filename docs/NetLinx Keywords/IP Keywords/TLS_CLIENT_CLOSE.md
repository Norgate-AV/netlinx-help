# TLS_CLIENT_CLOSE

Closes an open TLS communication port with a remote device. Typically, the remote host closes the connection and you do not need to send this command.

Syntax:

```
integer TLS_CLIENT_CLOSE(LocalPort)

```
Parameters:

- LocalPort - A user-defined (non-zero) integer value representing the local port on the client machine to use for this conversation. This local port number must be passed to [TLS_CLIENT_OPEN](TLS_CLIENT_OPEN.md) to open the conversation.

Returns:

- 0 - Success

- 1 - Error

Example:

```
TLS_CLIENT_CLOSE(443)

```
