---
title: SMTP_SERVER_CONFIG_SET
---

# SMTP_SERVER_CONFIG_SET

Note: SMTP functionality is supported by NetLinx Controller firmware version 4 or higher.

Set a configuration value for the current SMTP server. SMTP Server configuration will be retained between boots of the master.

Once the server configuration values have been set, e-mail can be sent using the [SMTP_SEND()](SMTP_SEND.md) API.

Syntax:

```c linenums="1"
SMTP_SERVER_CONFIG_SET(CONSTANT CHAR CONFIG_NAME, CONSTANT CHAR CONFIG_VALUE)

```
Where CONFIG_NAME is one of the following:

- SMTP_ADDRESS - Used to set the address of the SMTP server.  Ex. 'mail.amx.com'
- SMTP_PORT_NUMBER - Used to set the IP port number to connect to on the SMTP server.  Ex. '25'.

Supplying a port number of 0 means "use the best default port" which would imply use 25 which is the SMTP well-known port.

- SMTP_USERNAME - Used to set the username for server authentication. If username length is set to 0, authentication is not attempted when connecting to the server.
- SMTP_PASSWORD - Used to set the password for server authentication. If password length is set to 0, authentication is still attempted but a zero-length password (NULL_STR) is sent.
- SMTP_FROM - Used to set the 'Mail-From:' field in outgoing emails.
- SMTP_REQUIRE_TLS - Used to set whether TLS authentication security should be required when connecting to the server.

Valid values are SMTP_TLS_TRUE and SMTP_TLS_FALSE.

Example:

```c linenums="1"
SMTP_SERVER_CONFIG_SET(SMTP_ADDRESS,'mail.amx.com')

```
SMTP_SERVER_CONFIG_SET(SMTP_PORT_NUMBER,'25')

SMTP_SERVER_CONFIG_SET(SMTP_USERNAME,'john.doe@amx.com')

SMTP_SERVER_CONFIG_SET(SMTP_PASSWORD,'mypassword')

SMTP_SERVER_CONFIG_SET(SMTP_FROM,'john.doe@amx.com')

SMTP_SERVER_CONFIG_SET(SMTP_REQUIRE_TLS,SMTP_TLS_TRUE)

See Also

- [SMTP_SERVER_CONFIG_GET](SMTP_SERVER_CONFIG_GET.md)
- [SMTP_SEND](SMTP_SEND.md)

