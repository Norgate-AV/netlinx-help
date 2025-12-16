---
title: SMTP_SEND
---

# SMTP_SEND

Note: SMTP functionality is supported by NetLinx Controller firmware version 4 or higher.

SMTP_SEND sends an email to a single destination.  It returns an identifier associated with the email event.  The email is sent asynchronously by the onboard SMTP client.

If the mail transmission fails, an [ONERROR](ONERROR.md) DATA event will be sent to the supplied status DPS with DATA.NUMBER set to the error code, and DATA.TEXT set to the string representation of the email identifier.

Syntax:

```c linenums="1"
SINTEGER SMTP_SEND(DEV DPS, CONSTANT CHAR TO_ADDRESS[], CONSTANT CHAR SUBJECT[], CONSTANT CHAR BODY[], CONSTANT CHAR TEXT_ATTACHMENT[]
```

Where

- DPS - a DEV to receive asynchronous send status
- TO_ADDRESS - a string containing the email address of the destination. String must be less than 127 characters.
- SUBJECT - a string containing the email subject line
- BODY - a string containing the email body text
- TEXT_ATTACHMENT - a string containing the filename of a text file to be attached to the email.

Filename must be less than 256 characters and file size must be under 65536 bytes.

Can be specified as NULL_STR when no attachment is desired.

Example:

```c linenums="1"
MAIL_IDX1 = SMTP_SEND (0:3:0, 'john.doe@acme.com','Mail Subject','This is the mail text','attachment.txt')
```

MAIL_IDX2 = SMTP_SEND(0:3:0,'jane.doe@acme.com','Mail Alert','This is an email alert!',NULL_STR)

DEFINE_EVENT

   DATA_EVENT \[0:3:0\]

   {

       ONERROR

      {

         SEND_STRING 0,"'Email send failed: idx=',DATA.TEXT,'error=',ITOA(DATA.NUMBER)"

      }

   }

See Also

- [SMTP_SERVER_CONFIG_SET](SMTP_SERVER_CONFIG_SET.md)
- [SMTP_SERVER_CONFIG_GET](SMTP_SERVER_CONFIG_GET.md)
