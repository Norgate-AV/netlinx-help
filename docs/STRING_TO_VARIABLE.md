---
title: STRING_TO_VARIABLE
---

# STRING_TO_VARIABLE

This routine takes the Encode data from buffer and loads the values into the Decode variable.

The Decode variable must match the type of the encoded variable. In the case where the Encode variable was a structure then the Decode variable members must match in type and order. However if the number of members of the structures do not match, then the routine will fill all it can or skip any unused data members.

Syntax:

```c linenums="1"
SINTEGER STRING_TO_VARIABLE (DECODE, CHAR BUFFER[], LONG POSITION
```

Note: The "S" in SINTEGER allows a negative value to be returned.

Parameters:

- Decode - any type of variable. This is the variable to be decoded into.
- Buffer - Must of char array type. This is where the decode data is found.
- Position - This is where the first byte of the decode data. Is it also modified to point to the next location after the last decoded byte. That means that successive calls to this function can be made without modifying position. Position should be set to one on the first call.

Result:

- 2 = Decode data to small, more members in structure
- 1 = Structure to small, more members in decode string
- 0 = Decoded OK
- -1 = Decode variable type mismatch
- -2 = Decode data too small, decoder ran out of data

Example:

```c linenums="1"
DEFINE_TYPE
```

STRUCTURE \_AlbumStruct

{

LONG lTitleID

CHAR sArtist\[100\]

CHAR sTitle\[100\]

}

DEFINE_VARIABLE

\_AlbumStruct MyAlbumStruct\[3\]

LONG  lPos

SLONG  slReturn

SLONG  slFile

CHAR  sBinaryString\[10000\]

CHAR  sXMLString\[50000\]

DEFINE_START

MyAlbumStruct\[1\].lTitleID = 11101000

MyAlbumStruct\[1\].sArtist = 'Buffet, Jimmy'

MyAlbumStruct\[1\].sTitle = 'Living & Dying in ¾ Time'

MyAlbumStruct\[2\].lTitleID = 11101012

MyAlbumStruct\[2\].sArtist = 'Sinatra, Frank'

MyAlbumStruct\[2\].sTitle = 'Come Fly With Me'

MyAlbumStruct\[3\].lTitleID = 33101000

MyAlbumStruct\[3\].sArtist = 'Holiday, Billie'

MyAlbumStruct\[3\].sTitle = 'Lady in Satin'

DEFINE_EVENT

BUTTON_EVENT\[TP,1\]  / /Convert And Save

{

PUSH:

{

 // Convert To Binary

lPos = 1

slReturn = VARIABLE_TO_STRING(MyAlbumStruct, sBinaryString, lPos)

SEND_STRING 0,"'POSITION=',ITOA(lPos),' – Result = ',ITOA(slReturn)"

// Convert To XML

lPos = 1

slReturn = VARIABLE_TO_XML(MyAlbumStruct, sXMLString, lPos, 0)

SEND_STRING 0,"'POSITION=’,ITOA(lPos),' – Result = ',ITOA(slReturn)"

// Save Structure to Disk - Binary

slFile = FILE_OPEN('BinaryEncode.xml', 2)

slReturn = FILE_WRITE(slFile, sBinaryString, LENGTH_STRING(sBinaryString))

slReturn = FILE_CLOSE(slFile)

// Save Structure To Disk – XML

slFile = FILE_OPEN('xmlEncode.xml', 2)

slReturn = FILE_WRITE(slFile, sXMLString, LENGTH_STRING(sXMLString))

slReturn = FILE_CLOSE(slFile)

}

RELEASE:

{

}

}

  BUTTON_EVENT\[TP,2\]  // Read and Decode

{

PUSH:

{

// Read Binary File

slFile = FILE_OPEN('BinaryEncode.xml',1)

slResult = FILE_READ(slFile, sBinaryString, MAX_LENGTH_STRING(sBinaryString)

slResult = FILE_CLOSE (slFile)

// Read XML File

slFile = FILE_OPEN('XMLEncode.xml',1)

slResult = FILE_READ(slFile, sXMLString, MAX_LENGTH_STRING(sXMLString))

slResult = FILE_CLOSE (slFile)

// Convert To Binary

lPos = 1

slReturn = STRING_TO_VARIABLE(MyAlbumStruct, sBinaryString, slPos)

// OR Convert To XML

slPos = 1

slReturn = XML_TO_VARIABLE (MyAlbumStruct, sXMLString, slPos, 0)

}

RELEASE:

{

}

}

See Also

- [ATOI](ATOI.md)
- [ATOL](ATOL.md)
- [ITOA](ITOA.md)
- [ATOF](ATOF.md)
- [FTOA](FTOA.md)
- [ITOHEX](ITOHEX.md)
- [HEXTOI](HEXTOI.md)
- [CH_TO_WC](CH_TO_WC.md)
- [WC_TO_CH](WC_TO_CH.md)
- [RAW_BE](RAW_BE.md)
- [RAW_LE](RAW_LE.md)
- [VARIABLE_TO_STRING](VARIABLE_TO_STRING.md)
- [LENGTH_VARIABLE_TO_STRING](LENGTH_VARIABLE_TO_STRING.md)
- [LENGTH_VARIABLE_TO_XML](LENGTH_VARIABLE_TO_XML.md)
- [XML_TO_VARIABLE](XML_TO_VARIABLE.md)
- [VARIABLE_TO_XML](VARIABLE_TO_XML.md)
- [FORMAT](FORMAT.md)
- [Intrinsic Data Types](Intrinsic_Data_Types.md)
