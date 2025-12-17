---
title: TLS_CLIENT_OPEN
---

# TLS_CLIENT_OPEN

Opens a port for TLS communication with a remote device.

Syntax:

```
integer TLS_CLIENT_OPEN(LocalPort, hostname, port, mode)

```

Parameters:

- LocalPort- A user-defined (non-zero) integer value representing the local port
  on the client machine to use for this conversation. This local port number
  must be passed to [TLS_CLIENT_CLOSE](TLS_CLIENT_CLOSE.md) to close the
  conversation.

- hostname - The host name or IP address of the remote host.

- port - The connecting port on the remote host, usually port 443 for standard
  HTTPS connections.

- mode - 0: TLS_VALIDATE_CERTIFICATE (perform certificate validation), 1:
  TLS_IGNORE_CERTIFICATE_ERRORS (connect to the remote site while ignoring
  certificate errors or mismatches)

Returns:

This function returns 0 is all parameters are accepted, or a positive value
indicating the offending parameter if there is an error.

Example:

```
TLS_CLIENT_OPEN(5000, '192.168.0.1', 443, 0)

```
