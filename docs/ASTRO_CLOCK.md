---
title: ASTRO_CLOCK
---

# ASTRO_CLOCK

This routine calculates the time of sunset and sunrise at a specified location
(specified by longitude and latitude) on a specified date.

Syntax:

```c linenums="1"
SINTEGER ASTRO_CLOCK(DOUBLE Longitude,DOUBLE Latitude,DOUBLE HoursFromGMT,CHAR[] Date,CHAR[] Sunrise,CHAR[] Sunset)
```

Parameters:

- Longitude - Longitude in Degrees.Fraction of Degrees. West longitudes must be
  negative.
- Latitude - Latitude in Degrees.Fraction of Degrees. South latitudes must be
  negative.
- HoursFromGMT - Number of hours from GMT. Hours West of GMT can be entered as
  negative (e.g., -5 for EST, -4 for EDT)
- Date - In mm/dd/yyyy format.
- Sunrise - In 24-hour format. Value gets filled in by the function.
- Sunset - In mm/dd/yyyy format. Value gets filled in by the function.

Result:

- 0 = Success
- -1 = Latitude Entry Error
- -2 = Longitude Entry Error
- -3 = Hours Entry Error
- -4 = Date Entry Error

See Also

- [Time and Date Keywords](Time_and_Date_Keywords.md)
- [SINTEGER](SINTEGER.md)
