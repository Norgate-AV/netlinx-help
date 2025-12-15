---
title: DEFINE_CONNECT_LEVEL
---

# DEFINE_CONNECT_LEVEL

This keyword is used to define level connections. A single connection is defined by listing the device-level pairs inside parentheses.

The first level in the list (the primary level) must be virtual, in other words, a level on a virtual device. A virtual level does not actually exist but merely represents one or more physical levels (levels on physical devices).

By specifying a virtual level as the primary level in a DEFINE_CONNECT_LEVEL statement, NetLinx code can be written targeting the virtual level but having the effect of operating on each physical level.

Furthermore, since the primary level is virtual, the primary device (a virtual device) cannot be taken off-line or be removed from the system.

The example below combines the levels \[DEVICE1, LEVEL1\] and \[DEVICE2, LEVEL2\].

DEFINE_CONNECT_LEVEL

(VDevice, LEVEL1, DEVICE1, LEVEL1, DEVICE2, LEVEL1)

The second example combines all levels in the device-level array. Changes to any level listed in the connection will automatically be reflected in the other levels so that all level values are the same.

DEFINE_CONNECT_LEVEL

(VDevLev, MyDL\[ \])

See Also

- [Level Keywords](LEVEL_Keywords.md)

- [DEFINE Keywords](DEFINE_Keywords.md)

