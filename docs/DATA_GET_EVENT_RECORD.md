---
title: DATA_GET_EVENT_RECORD
---

# DATA_GET_EVENT_RECORD

*Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5 Instruction Manual** for a detailed description of format and usage of the Listview data feed functions.*

The DATA_GET_EVENT_RECORD function retrieves data feed event record values from a data feed custom event.

Syntax:

```c linenums="1"
SINTEGER DATA_GET_EVENT_RECORD (DEV device, LONG payloadID, char fields\[\]\[\], DATA_RECORD rec)

```
Parameters:

- device : NetLinx device event is coming from
- payloadID : Payload identifier supplied in custom event value1
- fields : array of strings specifying what fields from the record to return
- rec : [DATA_RECORD](DATA_RECORD.md) structure containing the desired field values from the data feed event

Result:

1 = Record values retrieved

-1 = Failed to retrieve values due to invalid parameter

Example:

```c linenums="1"
CUSTOM_EVENT\[dvTP,btnListview,LISTVIEW_ON_ROW_SELECT_EVENT\]

{

```
SLONG payloadID

SLONG payloadType

CHAR fields\[2\]\[16\]

CHAR name\[DATA_MAX_VALUE_LENGTH\]

CHAR number\[DATA_MAX_VALUE_LENGTH\]

DATA_RECORD record

// Get the data access ID from the custom event

payloadID = custom.value1

// Get the data type from the custom event

payloadType = custom.value2

Listview Buttons & Dynamic Data

108 TPDesign5 - G5 Touch Panel Design/Programming

if (payloadID \> 0 && payloadType == DATA_STRUCTURE_DATARECORD)

{

  // Specify which fields we want to retrieve from the payload

  fields\[1\] = 'name'

  fields\[2\] = 'number'

  // Populate a record with the requested fields from the event

  if (DATA_GET_EVENT_RECORD(dvTP, payloadID, fields, record) \> 0)

  {

    // All is well so far so retrieve the values that we are

    // interested in from the selection that the user made on

    // the panel.

    name = record.content\[1\].value

    number = record.content\[2\].value

    // Put the name and number that was selected on a popup and

    // show the popup

    SEND_COMMAND dvTP,"'^TXT-50,0,',name"

    SEND_COMMAND dvTP,"'^TXT-51,0,',number"

    SEND_COMMAND dvTP,"'^PPN-Calling'"

   }

  }

}

See Also

- [DATA_RECORD](DATA_RECORD.md)
- [DATA_ADD_RECORD](DATA_ADD_RECORD.md)
- [WC_DATA_RECORD](WC_DATA_RECORD.md)
- \_[WC_DATA_ADD_RECORD](WC_DATA_ADD_RECORD.md)
- \_[WC_DATA_GET_EVENT_RECORD](WC_DATA_GET_EVENT_RECORD.md)
