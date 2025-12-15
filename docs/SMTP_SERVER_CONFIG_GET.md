---
title: SMTP_SERVER_CONFIG_GET
---

# SMTP_SERVER_CONFIG_GET

Note: SMTP functionality is supported by NetLinx Controller firmware version 4 or higher.

Get a configuration value for the current SMTP server.

Syntax:

```c linenums="1"
CHAR\[\] SMTP_SERVER_CONFIG_GET(CONSTANT CHAR CONFIG_NAME)

```
Where CONFIG_NAME is one of the following:

- SMTP_ADDRESS - Used to get the address of the SMTP server.  Ex. 'mail.amx.com'
- SMTP_PORT_NUMBER - Used to get the IP port number to connect to on the SMTP server.  Ex. '25'. Supplying a port number of 0 means "use the best default port" which would imply use 25 which is the SMTP well-known port.
- SMTP_FROM - Used to set the 'Mail-From:' field in outgoing emails.
- SMTP_REQUIRE_TLS - Used to set whether TLS authentication security should be required when connecting to the server.  

Valid return values are SMTP_TLS_TRUE and SMTP_TLS_FALSE

Note: Query of SMTP_USERNAME and SMTP_PASSWORD is disabled for security reasons.

Example:

```c linenums="1"
CURRENT_ADDRESS = SMTP_SERVER_CONFIG_GET(SMTP_ADDRESS)

```
CURRENT_PORT = SMTP_SERVER_CONFIG_GET(SMTP_PORT_NUMBER)

CURRENT_FROM = SMTP_SERVER_CONFIG_GET(SMTP_FROM)

CURRENT_TLS = SMTP_SERVER_CONFIG_GET(SMTP_REQUIRE_TLS)

See Also

- [SMTP_SERVER_CONFIG_SET](SMTP_SERVER_CONFIG_SET.md)
- [SMTP_SEND](SMTP_SEND.md)

