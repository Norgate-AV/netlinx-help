---
title: AUTHENTICATE
---

# AUTHENTICATE

This function allows programs to authenticate/authorize a local or remote user depending on the parameters used. The authenticate command responds with custom events. The ID and event are completely customizable at the programmer's discretion.

Syntax:

```c linenums="1"
sinteger authenticate(DEV deviceHandler, LONG id, LONG eventType, LONG transactionId, LONG authType, CHAR username\[\], CHAR password\[\], CHAR facility\[\])

```
Parameters:

- deviceHandler - DPS (similar to IP sockets) that will handle the custom event.
- id - The custom event ID
- eventType - The custom event eventType.
- transactionId - A unique transaction ID. This aids in correlating responses.
- authType - The format of the password (0-clear text, 1-G5/PKI encrypted)
- username - A character array containing the user name to validate.
- password - A character array containing the password to validate.
- facility - The specific permission being queried. Each permission must be queried individually. If just authenticating, this should be an empty string. The following permissions are valid: AuditLog, Configuration, DeviceConfig, FTP, HTTP, NetworkConfig, ProgramPort, SecurityControl, SoftwareManagement, Terminal, User1, User2, User3, User4, UserManagement

Returns:

This function returns 0 if the query was submitted.
