---
title: ~LEVSYNCON
---

# ~LEVSYNCON

This SEND_COMMAND enables a feature that helps synchronize level values.

Note: By default, this feature is disabled for compatibility reasons.

The synchronization algorithm works by setting the level value of a level five
seconds after receiving a level value from a level. While it may not be
apparent, this makes sure that level values remain in sync with each other if
they ever get out of sync. The only way levels could ever get out of sync is
when the situation of "dueling levels" arises.

A typical example of "dueling levels" is when two touch panels with active
sliders are combined with a volume control. If one slider attempts to raise the
volume level while the other is attempting to lower the volume level the level
value bounces back and forth somewhere between the desired levels. If both
sliders are released at the exact same time, it is possible that one of level
values displayed on the touch panel's slider is inaccurate. The level
synchronization algorithm corrects the incorrect level five seconds after
activity ceases.

The commands ~LEVSYNCON and [~LEVSYNCOFF](~LEVSYNCOFF.md) are sent to the level
that should have the synchronization algorithm enabled or disabled. The command
itself is never sent to the device because the master intercepts the command and
processes it internally. Both commands accept a single parameter that specifies
the level number.

Using the "dueling levels" example above, the following send commands will turn
on the synchronization algorithm for level \#1 of Touch Panel 1, level \#4 of
touch panel \#2, and level \#2 of the volume control.

SEND_COMMAND dvTouchPanel1,'~LEVSYNCON 1'

SEND_COMMAND dvTouchPanel2,'~LEVSYNCON 4'

SEND_COMMAND dvVolume,'~LEVSYNCON 2'

Note that for some devices, turning the level synchronization algorithm on can
cause undesired results. The undesired results will vary from device to device
so it is difficult to indicate any specific failure mode. Keep in mind that the
algorithm should only be turned on when necessary.

Also note that the LEVSYNCON and LEVSYNCOFF SEND_COMMANDs may not be sent to
remote devices (devices that belong to other systems) and only the device's
master may issue these commands.

See Also

- [Level Keywords](LEVEL_Keywords.md)
- [~LEVSYNCOFF](~LEVSYNCOFF.md)
