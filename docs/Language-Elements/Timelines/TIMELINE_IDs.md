---
title: TIMELINE IDs
---

# TIMELINE IDs

When creating a [TIMELINE_EVENT](TIMELINE_EVENT.md),  the timeline ID must be a user defined long
constant.

-   The NetLinx compiler will not semantic check the type of the timeline ID, and the NetLinx
    runtime system will attempt to cast the contents of the timeline ID constant, to a long
    constant.

-   A runtime error will occur if the cast is unsuccessful.

Example:

```c linenums="1"
DEFINE_VARIABLE

CONSTANT LONG TimelineID_1 = 1
CONSTANT LONG TimelineID_2 = 2
CONSTANT LONG TimelineID_3 = 3
CONSTANT LONG TimelineID_4 = 4
LONG TimeArray\[4\] =
{
1000, // 1 second
2000, // 2 seconds
3000, // 3 seconds
4000  // 4 seconds
}

DEFINE_START
TIMELINE_CREATE (TimelineID_1,TimeArray,LENGTH_ARRAY(TimeArray),TIMELINE_RELATIVE,TIMELINE_REPEAT)
TIMELINE_CREATE (TimelineID_2,TimeArray,LENGTH_ARRAY(TimeArray),TIMELINE_RELATIVE,TIMELINE_REPEAT)
TIMELINE_CREATE (TimelineID_3,TimeArray,LENGTH_ARRAY(TimeArray),TIMELINE_RELATIVE,TIMELINE_REPEAT)
TIMELINE_CREATE (TimelineID_4,TimeArray,LENGTH_ARRAY(TimeArray),TIMELINE_RELATIVE,TIMELINE_REPEAT)

DEFINE_EVENT
// typical TIMELINE_EVENT statement
TIMELINE_EVENT\[TimelineID_1\] // capture all events for Timeline 1
{
SEND_STRING 0,"'TL ID = ', itoa(timeline.id),', sequence = ',itoa(timeline.sequence)"
}

// example of "stacked" TIMELINE_EVENT statements
TIMELINE_EVENT\[TimelineID_2\] // capture all events for Timeline 2
TIMELINE_EVENT\[TimelineID_3\] // capture all events for Timeline 3
TIMELINE_EVENT\[TimelineID_4\] // capture all events for Timeline 4
{
SEND_STRING 0,"'TL ID = ', itoa(timeline.id),', sequence = ',itoa(timeline.sequence)"
}

// end
```

## See Also

-   [Timeline Functions](Timeline_Functions.md)
-   [TIMELINE example](TIMELINE_example.md)
-   [TIMELINE Keywords](TIMELINE_Keywords.md)
