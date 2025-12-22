---
title: Combining and Uncombining_Channels
---

# Combining and Uncombining Channels

The NetLinx functions [COMBINE_CHANNELS](COMBINE_CHANNELS.md) and
[UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md) are used within events and mainline code to dynamically
change what levels are connected to each other.

The 6 examples in the program below demonstrate the use of [COMBINE_CHANNELS](COMBINE_CHANNELS.md)
and [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md):

```c linenums="1"
PROGRAM_NAME='CombineChannelsExample'

DEFINE_DEVICE // common devices for all examples below

dvTP = 128:1:0
dvREL10 = 301:1:0
dvIO10 = 310:1:0
vdvControl = 33000:1:0

// example of combining a DEVCHAN set to a virtual [DEV,CHAN] pair
DEFINE_VARIABLE
DEVCHAN dc1[] = {{dvIO10,1},{dvREL10,1},{dvTP,1}}

DEFINE_EVENT
BUTTON_EVENT[dvTP,11] // COMBINE_CHANNELS 1
{
    RELEASE:
    {
        COMBINE_CHANNELS (vdvControl,1,dc1)
    }
}

BUTTON_EVENT[dvTP,12] // UNCOMBINE_CHANNELS 1
{
    RELEASE:
    {
        UNCOMBINE_CHANNELS (vdvControl,1)
    }
}

BUTTON_EVENT[vdvControl,1] // this will work when the COMBINE_CHANNELS above is invoked
{
    PUSH:
    {
        TO[BUTTON.INPUT]
    }
}

// example of combining individual DEVCHANs to a virtual \[DEV,CHAN\] pair
DEFINE_VARIABLE
DEVCHAN dc2[] = {{dvIO10,2},{dvREL10,2},{dvTP,2}}

DEFINE_EVENT
BUTTON_EVENT[dvTP,13] // COMBINE_CHANNELS 2
{
    RELEASE:
    {
        COMBINE_CHANNELS (vdvControl,2,dc2[1],dc2[2],dc2[3])
    }
}

BUTTON_EVENT[dvTP,14] // UNCOMBINE_CHANNELS 2
{
    RELEASE:
    {
        UNCOMBINE_CHANNELS (vdvControl,2)
    }
}

BUTTON_EVENT[vdvControl,2] // this will work when the COMBINE_CHANNELS above is invoked
{
    PUSH:
    {
        TO[BUTTON.INPUT]
    }
}

// example of combining individual [DEV,CHAN] pairs to a virtual [DEV,CHAN] pair
DEFINE_VARIABLE
DEVCHAN dc3[] = {{dvIO10,3},{dvREL10,3},{dvTP,3}}

DEFINE_EVENT
BUTTON_EVENT[dvTP,15] // COMBINE_CHANNELS 3
{
    RELEASE:
    {
        COMBINE_CHANNELS (vdvControl,3,
            dc3\[1\].DEVICE,
            dc3\[1\].CHANNEL,
            dc3\[2\].DEVICE,
            dc3\[2\].CHANNEL,
            dc3\[3\].DEVICE,
            dc3\[3\].CHANNEL)
    }
}

BUTTON_EVENT[dvTP,16] // UNCOMBINE_CHANNELS 3
{
    RELEASE:
    {
        UNCOMBINE_CHANNELS (vdvControl,3)
    }
}

BUTTON_EVENT[vdvControl,3] // this will work when the COMBINE_CHANNELS above is invoked
{
    PUSH:
    {
        TO[BUTTON.INPUT]
    }
}

// example of combining a DEVCHAN set to a virtual DEVCHAN
DEFINE_VARIABLE
DEVCHAN vdc4 = {vdvControl,4}
DEVCHAN dc4[] = {{dvIO10,4},{dvREL10,4},{dvTP,4}}

DEFINE_EVENT
BUTTON_EVENT[dvTP,17] // COMBINE_CHANNELS 4
{
    RELEASE:
    {
        COMBINE_CHANNELS (vdc4,dc4)
    }
}

BUTTON_EVENT[dvTP,18] // UNCOMBINE_CHANNELS 4
{
    RELEASE:
    {
        UNCOMBINE_CHANNELS (vdc4)
    }
}

BUTTON_EVENT[vdc4] // this will work when the COMBINE_CHANNELS above is invoked
{
    PUSH:
    {
        TO[BUTTON.INPUT]
    }
}

// example of combining individual DEVCHANs to a virtual DEVCHAN
DEFINE_VARIABLE
DEVCHAN vdc5 = {vdvControl,5}
DEVCHAN dc5[] = {{dvIO10,5},{dvREL10,5},{dvTP,5}}

DEFINE_EVENT
BUTTON_EVENT[dvTP,19] // COMBINE_CHANNELS 5
{
    RELEASE:
    {
        COMBINE_CHANNELS (vdc5,dc5[1],dc5[2],dc5[3])
    }
}

BUTTON_EVENT[dvTP,20] // UNCOMBINE_CHANNELS 5
{
    RELEASE:
    {
        UNCOMBINE_CHANNELS (vdc5)
    }
}

BUTTON_EVENT[vdc5] // this will work when the COMBINE_CHANNELS above is invoked
{
    PUSH:
    {
        TO[BUTTON.INPUT]
    }
}

// example of combining individual [DEV,CHAN] pairs to a virtual DEVCHAN
DEFINE_VARIABLE
DEVCHAN vdc6 = {vdvControl,6}
DEVCHAN dc6[] = {{dvIO10,6},{dvREL10,6},{dvTP,6}}

DEFINE_EVENT
BUTTON_EVENT[dvTP,21] // COMBINE_CHANNELS 6
{
    RELEASE:
    {
        COMBINE_CHANNELS (vdc6,
            dc6[1].DEVICE,
            dc6[1].CHANNEL,
            dc6[2].DEVICE,
            dc6[2].CHANNEL,
            dc6[3].DEVICE,
            dc6[3].CHANNEL)
    }
}

BUTTON_EVENT[dvTP,16] // UNCOMBINE_CHANNELS 6
{
    RELEASE:
    {
        UNCOMBINE_CHANNELS (vdc6)
    }
}

BUTTON_EVENT[vdc6] // this will work when the COMBINE_CHANNELS above is invoked
{
    PUSH:
    {
        TO[BUTTON.INPUT]
    }
}

// end
```

## See Also

-   [Combining and Uncombining Devices](Combining_and_Uncombining_Devices.md)
-   [Combining and Uncombining Levels](Combining_and_Uncombining_Levels.md)
-   [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)
