---
title: SSH_CLIENT_OPEN
---

# SSH_CLIENT_OPEN

This function opens a port for SSH communication with a server.

Syntax:

```
slong SSH_CLIENT_OPEN(INTEGER LocalPort, CHAR ServerAddress\[\], INTEGER remotePort, CHAR username\[\], char password\[\], char privateKeyPathname\[\], char privateKeyPassphrase\[\])

```

Parameters:

- LocalPort- A user-defined (non-zero) integer value representing the local port
  on the client machine to use for this conversation. This local port number
  must be passed to [SSH_CLIENT_CLOSE](SSH_CLIENT_CLOSE.md) to close the
  conversation.

- ServerAddress - A string containing either the IP address (in
  dotted-quad-notation) or the domain name of the server to which you want to
  connect.

- remotePort - The port number on the server that identifies the program or
  service that the client is requesting, typically 22

- username - Login user name

- password - Password for the user name, null if using PKI

- privateKeyPathname - Path to private key

- privateKeyPassphrase - Password for private key.

Returns:

This function always returns 0. Errors are returned via the
[DATA_EVENT](DATA_EVENT.md) [ONERROR](ONERROR.md) method .The following errors
may be returned from the call:

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
SSH_CLIENT_OPEN(5000, '192.168.0.1', 22, 'user1', 'password', '/certs/id_rsa', '')

```
