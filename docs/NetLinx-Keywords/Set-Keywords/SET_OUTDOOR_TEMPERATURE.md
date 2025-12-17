---
title: SET_OUTDOOR_TEMPERATURE
---

# SET_OUTDOOR_TEMPERATURE

Establishes the value for the outdoor temperature.

- This value is broadcast to all devices periodically.

- A value of 32768 indicates that no outdoor temperature is available.

Syntax:

```
SET_OUTDOOR_TEMPERATURE(INTEGER Temp)

```

Parameters:

- Temp - the outdoor temperature as it shall be displayed. It is up to the
  programmer to provide the correct temperature scale (Celsius or Fahrenheit).

Returns:  None

Example:

```
SET_OUTDOOR_TEMPERATURE (32) // show 32 degrees

```

See Also

- [SET Keywords](SET_Keywords.md)
