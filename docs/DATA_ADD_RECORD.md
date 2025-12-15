---
title: DATA_ADD_RECORD
---

# DATA_ADD_RECORD

*Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5 Instruction Manual** for a detailed description of format and usage of the Listview data feed functions.*

The DATA_ADD_RECORD function adds a new record to a data feed.

Syntax:

```c linenums="1"
SINTEGER DATA_ADD_RECORD (CHAR FEED\[\], CHAR \[\] RECORDSET_ID, DATA_RECORD REC)

```
Parameters:

- FEED : A string containing the name of the data feed to add the record to
- RECORDSET_ID : A string containing the name of the record set the record belongs to
- REC : A [DATA_RECORD](DATA_RECORD.md) containing the record values to add to the data feed

Result:

1 = Record added

-1 = Record failed to add due to invalid parameter

Example:

```c linenums="1"
STACK_VAR DATA_RECORD record

 

// Records can have metadata fields and content fields. In this

// example we won't use any metadata

```
SET_LENGTH_ARRAY(record.metadata, 0)

// We will have 3 content fields per record: photo, name and phone number

SET_LENGTH_ARRAY(record.content, 3)

// Initialize the field attributes that will be the same for every record

// the first field in a record will be the image

record.content\[1\].id = 'photo';

record.content\[1\].type = DATA_TYPE_IMAGE;

record.content\[1\].format = DATA_FORMAT_URL;

// The label can be something different from the id but in our case we'll

// keep them the same

record.content\[1\].label = 'photo';

// The second field in a record will be the name

record.content\[2\].id = 'name';

record.content\[2\].type = DATA_TYPE_STRING;

record.content\[2\].format = '';

record.content\[2\].label = 'name';

// The third field will be the phone number

record.content\[3\].id = 'number';

record.content\[3\].type = DATA_TYPE_STRING;

record.content\[3\].format = DATA_FORMAT_PHONE;

record.content\[3\].label = 'number';

// The next step is to put in the actual values for the 3 fields

// Do this for the first record

record.content\[1\].value = 'http://192.168.222.333/FTP/Listview/hunter.jpg'

record.content\[2\].value = 'Hunter Pence'

record.content\[3\].value = '888-555-1111'

// Add the record to the feed phonelist data feed

DATA_ADD_RECORD('phonelist', 'phonelist', record)

See Also

- [DATA_RECORD](DATA_RECORD.md)
- [DATA_GET_EVENT_RECORD](DATA_GET_EVENT_RECORD.md)
- [WC_DATA_RECORD](WC_DATA_RECORD.md)
- \_[WC_DATA_ADD_RECORD](WC_DATA_ADD_RECORD.md)
- \_[WC_DATA_GET_EVENT_RECORD](WC_DATA_GET_EVENT_RECORD.md)

