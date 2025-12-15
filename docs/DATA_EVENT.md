# DATA_EVENT

This keyword defines a data event handler.

- This type of handler processes [COMMAND](COMMAND.md), [STRING](STRING.md), [ONLINE](ONLINE.md), [OFFLINE](OFFLINE.md) and [ONERROR](ONERROR.md) events.

-  It can only be used in the [DEFINE_EVENT](DEFINE_EVENT.md) section of the program.

Example:

```
DATA_EVENT\[DEVICE\]

{

   [COMMAND](COMMAND.md):

  {

        // Command processing goes here

  }

   [STRING](STRING.md):

  {

        // String processing goes here

  }

   [ONLINE](ONLINE.md):

  {

        // OnLine processing goes here

  }

   [OFFLINE](OFFLINE.md):

  {

        // Offline processing goes here

  }

   [ONERROR](ONERROR.md):

  {

        // OnError processing goes here

  }

   [STANDBY](STANDBY.md):

  {

       // Standby processing goes here

  }

   [AWAKE](AWAKE.md):

  {

       // Awake processing goes here

 }

}

```
DEVICE refers to:

- Device – a single device number constant.

- D:P:S – a constant device specification such as TP:1:0.

See Also

- [Event Handlers](Event_Handlers.md)

- [Event Parameters](Event_Parameters.md)

- [Data Events](Data_Events.md)

