---
title: DEFINE_DEVICE
---

# DEFINE_DEVICE

This keyword is used to define the devices referenced in the program.

NetLinx defines devices by D:P:S (Device:Port:System).

- Device is a 16-bit integer representing the device number. Physical devices range from 1 to 32,000. Virtual devices range from 32,768 to 36,863

Note: These numbers do not seem so random when represented in hexadecimal. Physical devices range from \$0001 to \$7FFF. Virtual devices range from \$8000 to \$8FFF

- Port is a 16-bit integer representing the port number in a range of 1 through the number of ports on the device (1 = this port)

- System is a 16-bit integer representing the system number (0 = this system)

Example:

```
DEFINE_DEVICE

```
TP1 = 128:1:0 // device number = 128, port = 1, system = 0

TP2 = 129:1:0 // device number = 128, port = 1, system = 0

TP3 = 130:1:0 // device number = 128, port = 1, system = 0

 

VCR1 = 10:1:0 // device number = 10, port = 1, system = 0

VCR2 = 11:1:0 // device number = 10, port = 1, system = 0

See Also

- [DEFINE Keywords](DEFINE_Keywords.md)

- [DEVICE_ID](DEVICE_ID.md)

- [DEVICE_ID_STRING](DEVICE_ID_STRING.md)

- [DEVICE_INFO](DEVICE_INFO.md)

- [SYSTEM_NUMBER](SYSTEM_NUMBER.md)

