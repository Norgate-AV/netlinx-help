---
title: Combining_and_uncombining_device_channel_sets
---

# Combining and Uncombining Device/Channel Sets

Combining [DEVCHAN](DEVCHAN.md) sets is unique to NetLinx. The format for [COMBINE_CHANNELS](COMBINE_CHANNELS.md) and [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md) is:

SLONG COMBINE_CHANNELS (\<virtual DEVCHAN\[\]\>, \<DEVCHAN1\[\]\>, \<DEVCHAN2\[\]\>…)

SLONG UNCOMBINE_CHANNELS (\<virtual DEVCHAN\[\]\>)

To explain the concept of combining DEVCHAN sets, it is necessary to understand how the DEVCHAN sets are arranged. Rather than the DEVCHAN set being a set of like functions, such as a set of volume mute buttons across different devices, the DEVCHAN set should be a group of different functions on the same device, such as 5 lighting presets on an AXU-MSP16. For example:

DEVCHAN dcMSP1 =

{{MSP1,PRESET1},{MSP1,PRESET2},{MSP1,PRESET3},{MSP1,PRESET4},{MSP1,PRESET5}}

DEVCHAN dcMSP2 =

{{MSP2,PRESET1},{MSP2,PRESET2},{MSP2,PRESET3},{MSP2,PRESET4},{MSP2,PRESET5}}

DEVCHAN dcMSP3 =

{{MSP3,PRESET1},{MSP3,PRESET2},{MSP3,PRESET3},{MSP3,PRESET4},{MSP3,PRESET5}}

Similar to COMBINE_DEVICES and COMBINE_LEVELS, the first DEVCHAN set in a COMBINE_CHANNEL function needs to be referenced to a Virtual Device, as shown below:

DEVCHAN dcVDEV =

{{VDEV,PRESET1},{VDEV,PRESET2},{VDEV,PRESET3},{VDEV,PRESET4},{VDEV,PRESET5}}

All of the DEVCHAN sets in the COMBINE_CHANNELS function must have the same number of array elements. The actual COMBINE_CHANNELS statement is:

COMBINE_CHANNELS (dcVDEV, dcMSP1, dcMSP2, dcMSP3)

The actual element positions of the DEVCHAN arrays are combined within the program. In essence, all of the PRESET1 channels are handled through \[VDEV,PRESET1\] defined as dcVDEV\[1\].

Note: When using COMBINE_XXXX and UNCOMBINE_XXXX functions dynamically based upon a button event, the combining and combining must be done on the release of the button (the active event must be complete before a  COMBINE_XXXX or UNCOMBINE_XXXX function is invoked).

See Also:

- [Intrinsic Data Types](Intrinsic_Data_Types.md)

- [Conversion Keywords](Conversion_Keywords.md)

