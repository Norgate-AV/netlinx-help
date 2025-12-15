# TIMELINE example

The following code is an example of using [TIMELINE functions](Timeline_Functions.md).

PROGRAM_NAME='TimelineExample'

(\*{{PS_SOURCE_INFO(PROGRAM STATS)                          \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*  FILE CREATED ON: 05/22/2001 AT: 12:05:56               \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*  FILE_LAST_MODIFIED_ON: 05/22/2001 AT: 12:15:56         \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*  ORPHAN_FILE_PLATFORM: 1                                \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*!!FILE REVISION:                                         \*)

(\*  REVISION DATE: 05/22/2001                              \*)

(\*                                                         \*)

(\*  COMMENTS:                                              \*)

(\*                                                         \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*}}PS_SOURCE_INFO                                         \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*          DEVICE NUMBER DEFINITIONS GO BELOW             \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_DEVICE

dvPanel    = 128:1:0

DvDEBUG    = 0:0:0

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*               CONSTANT DEFINITIONS GO BELOW             \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_CONSTANT

MY_LINE_1 = 1

MY_LINE_2 = 2

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*               VARIABLE DEFINITIONS GO BELOW             \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_VARIABLE

LONG TimeArray\[100\]

INTEGER iLoop

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*                STARTUP CODE GOES BELOW                  \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_START

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*                THE EVENTS GOES BELOW                    \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_EVENT

TIMELINE_EVENT\[MY_LINE_1\]

{

  switch(Timeline.Sequence)

  {

   case 1: { SEND_COMMAND dvPanel,"'TEXT1-1 1'"  }

   case 2: { SEND_COMMAND dvPanel,"'TEXT1-1 2'"  }

   case 3: { SEND_COMMAND dvPanel,"'TEXT1-1 3'"  }

   case 4: { SEND_COMMAND dvPanel,"'TEXT1-1 4'"  }

   case 5: { SEND_COMMAND dvPanel,"'TEXT1-1 5'"  }

  }

  SEND_STRING  DvDEBUG,"'Timer ',ITOA(Timeline.ID),' Event ',ITOA(Timeline.Sequence), ' Time= ',ITOA(Timeline.Time),

            'Repetition = ',ITOA(Timeline.Repetition),' Relative = ',ITOA(Timeline.Relative)"

}

TIMELINE_EVENT\[MY_LINE_2\]

{

  switch(Timeline.Sequence)

  {

   case 1: { SEND_COMMAND dvPanel,"'TEXT2-2 1'"  }

   case 2: { SEND_COMMAND dvPanel,"'TEXT2-2 2'"  }

   case 3: { SEND_COMMAND dvPanel,"'TEXT2-2 3'"  }

   case 4: { SEND_COMMAND dvPanel,"'TEXT2-2 4'"  }

   case 5: { SEND_COMMAND dvPanel,"'TEXT2-2 5'"  }

  }

SEND_STRING  DvDEBUG,"'Timer ',ITOA(Timeline.ID),' Event ',ITOA(Timeline.Sequence), ' Time = ',ITOA(Timeline.Time),

           ' Repetition = ',ITOA(Timeline.Repetition),' Relative = ',ITOA(Timeline.Relative)"

}

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*            THE ACTUAL PROGRAM GOES BELOW                \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_PROGRAM

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* create will sort the order of the times but index stays \*)

(\* with the time. This example will execute 1 2 4 3 5      \*)

(\* sequence numbers                                        \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

PUSH\[dvPanel,1\]

{

TimeArray\[1\] = 1000

TimeArray\[2\] = 2000

TimeArray\[4\] = 3000

TimeArray\[3\] = 4000

TimeArray\[5\] = 5000

TIMELINE_CREATE(MY_LINE_1,TimeArray,5,TIMELINE_ABSOLUTE,TIMELINE_ONCE)

}

PUSH\[dvPanel,2\]

{

  TimeArray\[1\] = 1000

  TimeArray\[2\] = 2000

  TimeArray\[3\] = 3000

  TimeArray\[4\] = 4000

  TimeArray\[5\] = 5000

    TIMELINE_CREATE(MY_LINE_2,TimeArray,5,TIMELINE_ABSOLUTE,TIMELINE_REPEAT)

}

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* Modify the timeline my kill, pause and restarting       \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

PUSH\[dvPanel,3\]

{

  IF(TIMELINE_ACTIVE(MY_LINE_1))TIMELINE_KILL(MY_LINE_1)

  IF(TIMELINE_ACTIVE(MY_LINE_2))TIMELINE_KILL(MY_LINE_2)

}

PUSH\[dvPanel,4\]

{

  IF(TIMELINE_ACTIVE(MY_LINE_1))TIMELINE_PAUSE(MY_LINE_1)

  IF(TIMELINE_ACTIVE(MY_LINE_2))TIMELINE_PAUSE(MY_LINE_2)

}

PUSH\[dvPanel,5\]

{

  IF(TIMELINE_ACTIVE(MY_LINE_1))TIMELINE_RESTART(MY_LINE_1)

  IF(TIMELINE_ACTIVE(MY_LINE_2))TIMELINE_RESTART(MY_LINE_2)

}

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* Force time to a different value                         \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

PUSH\[dvPanel,6\]

{

  IF (TIMELINE_ACTIVE(MY_LINE_1))

   TIMELINE_SET(MY_LINE_1,2000)

}

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* Get the current time from create                        \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

PUSH\[dvPanel,7\]

{

SEND_COMMAND dvPanel,"'TEXT3-','Timer 1 Time is ',ITOA(TIMELINE_GET(MY_LINE_1))"

SEND_COMMAND dvPanel,"'TEXT4-','Timer 2 Time is ',ITOA(TIMELINE_GET(MY_LINE_2))"

}

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* Pause and restart the timeline at new locations         \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

PUSH\[dvPanel,8\]

{

  TIMELINE_PAUSE(MY_LINE_1)

  TIMELINE_PAUSE(MY_LINE_2)

  TIMELINE_SET(MY_LINE_1,0)

  TIMELINE_SET(MY_LINE_2,0)

  TIMELINE_RESTART(MY_LINE_1)

  TIMELINE_RESTART(MY_LINE_2)

}

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*                     END OF PROGRAM                      \*)

(\*        DO NOT PUT ANY CODE BELOW THIS COMMENT           \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

See Also

- [Timeline Functions](Timeline_Functions.md)

- [TIMELINE IDs](TIMELINE_IDs.md)

- [TIMELINE Keywords](TIMELINE_Keywords.md)

