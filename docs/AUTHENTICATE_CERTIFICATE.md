---
title: AUTHENTICATE_CERTIFICATE
---

# AUTHENTICATE_CERTIFICATE

This function allows programs to authenticate/authorize an X.509 certificate against the OCSP responder included in the Authority Information Access field of the certificate. The OCSP option does NOT impact the availability/functionality of this feature. The OCSP security option is ONLY for authenticating/validating incoming ICSP/ICSPS connections.

Syntax:

```c linenums="1"
sinteger AUTHENTICATE_CERTIFICATE(DEV handler, LONG id, LONG eventType, LONG transactionId, LONG authType, CHAR certificate\[\], CHAR ca\[\])

```
Parameters:

- handler - DPS (similar to IP sockets) that will handle the custom event.
- id - The custom event ID
- eventType - The custom event eventType.
- transactionId - A unique transaction ID. This aids in correlating responses.
- authType - unused (enter 0)
- certificate - X.509 certificate (likely from a custom event on the UI device)
- ca - X.509 certificate of the CA used to sign the certificate

Returns:

This function returns 0 if the query was submitted, otherwise it returns an error.
