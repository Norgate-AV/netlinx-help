---
title: VALIDATE_NETLINX_ACCOUNT
---

# VALIDATE_NETLINX_ACCOUNT

This function validates the specified user name and password against the NetLinx
Master Controller's internal user account database. For the account to be valid
the user name must exist with the matching password and the specified user
account must have been set up with ICSP Authorization.

Syntax:

```c linenums="1"
sinteger VALIDATE_NETLINX_ACCOUNT(CHAR USERNAME[], CHAR PASSWORD[],LAST_LOGIN_INFO INFO)
```

Parameters:

- username - A character array containing the user name to validate.
- password - A character array containing the password to validate.
- info - A return structure of type LAST_LOGIN_INFO which contains the following
  values:

STRUCTURE LAST_LOGIN_INFO

{

INTEGER FAILED_LOGIN_COUNT;

CHAR LAST_SUCCESSFUL_LOGIN_DATE\[46\];

CHAR LAST_SUCCESSFUL_LOGIN_LOCATION\[46\];

CHAR LAST_FAILED_LOGIN_DATE\[46\];

CHAR LAST_FAILED_LOGIN_LOCATION\[46\];

}

Returns:

The following values are returned from the call:

- 0 - Valid user account.
- -1 - Username parameter is not a valid string
- -2 - Password parameter is not a valid string
- -3 - Invalid user account
- -4 - User account does not have ICSP Authorization
- -5 - Third argument is not a LAST_LOGIN_INFO
- -6 -User account matching name is locked out
- -7 - User account matching name has expired
