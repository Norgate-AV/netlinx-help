---
title: LISTVIEW_ON_ROW_SELECT_EVENT
---

# LISTVIEW_ON_ROW_SELECT_EVENT

LISTVIEW_ON_ROW_SELECT_EVENT is a Custom Event that is raised in response to a user selection of an item in a Listview button.

When the user selects an item on the Listview button, a LISTVIEW_ON_ROW_SELECT_EVENT is raised and the entire data feed record for that selection is sent to the master. The user can then use DATA_GET_EVENT_RECORD to retrieve the specific values of interest.

Note: "payloadId" specifies the data access identifier to be retrieved from the custom event object, and is predefined as "custom.value1". “payloadType” specifies the dataType to be retrieved from the custom event object and is predefined as “custom.value2”. 

The following code example illustrates how the LISTVIEW_ON_ROW_SELECT_EVENT Custom Event is used to retrieve two data fields ('name' and 'number') when a listview item is selected.

// The custom event that is raised whenever a listview item is selected on the panel

CUSTOM_EVENT\[dvTP,btnListview,LISTVIEW_ON_ROW_SELECT_EVENT\]

{

   SLONG payloadId

   SLONG payloadType

   //just a char array to hold the data we want to use in the custom event.

   CHAR fields\[2\]\[16\]

   //char variables to hold our data for "name" & "number"

   CHAR name\[DATA_MAX_VALUE_LENGTH\]

   CHAR number\[DATA_MAX_VALUE_LENGTH\]

 

   //variable record, of type DATA_RECORD, to hold the record we retrieve from the custom event

   DATA_RECORD record

   // Get the data access ID from the custom event

   // variable is payloadID - custom.value1 is predefined

   payloadId = custom.value1

   // Get the data type from the custom event

   // variable is payloadType - custom.value2 is predefined

   payloadType = custom.value2

 

   if (payloadId \> 0 && payloadType == DATA_STRUCTURE_DATARECORD)

   {

   // Specify which fields we want to retrieve from the payload

   // (these are the IDs we defined earlier)

   fields\[1\] = 'name'

   fields\[2\] = 'number'

   // Retrieve the record and get our requested fields

   if (DATA_GET_EVENT_RECORD(dvTP, payloadId, fields, record) \> 0)

   {

      // The record existed and contained our fields

      // let's retrieve the values that we are interested in

      name = record.content\[1\].value

      number = record.content\[2\].value

      // Send the name & number that was retrieved to the appropriate buttons & show the popup

      SEND_COMMAND dvTP,"'^TXT-50,0,',name"

      SEND_COMMAND dvTP,"'^TXT-51,0,',number"

      SEND_COMMAND dvTP,"'^PPN-Calling'"

      }

   }

}

See Also

- [DATA_RECORD](DATA_RECORD.md)
- [DATA_GET_EVENT_RECORD](DATA_GET_EVENT_RECORD.md)

