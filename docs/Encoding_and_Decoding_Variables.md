---
title: Encoding_and_Decoding_Variables
---

# Encoding and Decoding Variables

There are six functions used to encode and decode variables in NetLinx. This
encoding process takes a NetLinx variable, no matter how complex, and converts
it into a string. The decode process will take this string and copy the contents
back into a variable.

These functions can be used to take the contents of NetLinx variables and
convert them to string. Once the variable exists in string form, it can then be
sent across an RS-232 connection, sent over and IP socket or saved to the
NetLinx master's file system (disc on chip). Once the string is retrieved,
either from a data event or by reading the information from the NetLinx master's
file system, the data can be converted back to a variable.

There are two version of this encoding and decoding: Binary and XML.

The Binary conversion routines are:

- [STRING_TO_VARIABLE](STRING_TO_VARIABLE.md),
- [VARIABLE_TO_STRING](VARIABLE_TO_STRING.md) and
- [LENGTH\_ VARIABLE_TO_STRING](LENGTH_VARIABLE_TO_STRING.md).

The XML routines are:

- [XML_TO_VARIABLE](XML_TO_VARIABLE.md),
- [VARIABLE_TO_XML](VARIABLE_TO_XML.md) and
- [LENGTH\_ VARIABLE_TO_XML](LENGTH_VARIABLE_TO_XML.md).

Both sets of routines accomplish the same function but the encoded string
differs in protocol. The binary conversion routines uses a compact binary
representation of the variable while the XML represents the variable as a ASCII
text only XML document.

The binary routines are ideal when sending data from one NetLinx system to
another NetLinx system over RS-232 or IP since the variable will be as compact
as possible. It is also ideal for saving a file to the NetLinx master's file
system if you do not intend to edit the file later. The binary routines encode
and decode a variable sequentially meaning that the order and type of the
variables must match on both the encoding and decoding side.

The XML routines are ideal when sending data from one NetLinx system to another
type of system over RS232 or IP, since XML is more universally accepted by other
types of computer systems. XML is also ideal for saving a file to the NetLinx
master's file system if you intend to edit the file later since it is entirely
ASCII text. It should be noted that while the XML is more universal, is not very
compact. The XML routines encode and decode a variable non-sequentially, meaning
that the order and type of variables do not need to match on both the encoding
and decoding side.

Below are some examples of how to use these encoding routines:

PROGRAM_NAME='ConversionExample'

(\*{{PS_SOURCE_INFO(PROGRAM STATS) \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* FILE CREATED ON: 05/22/2001 AT: 11:09:27 \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* FILE_LAST_MODIFIED_ON: 05/22/2001 AT: 11:26:44 \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* ORPHAN_FILE_PLATFORM: 1 \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*!!FILE REVISION: \*)

(\* REVISION DATE: 05/22/2001 \*)

(\* \*)

(\* COMMENTS: \*)

(\* \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* PS_SOURCE_INFO \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* System Type : NetLinx \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* REV HISTORY: \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* DEVICE NUMBER DEFINITIONS GO BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_DEVICE

dvTP = 128:1:0

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* CONSTANT DEFINITIONS GO BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_CONSTANT

nFileRead = 1

nFileWrite = 2

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* DATA TYPE DEFINITIONS GO BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_TYPE

STRUCTURE \_AlbumStruct

{

LONG lTitleID

CHAR sArtist\[100\]

CHAR sTitle\[100\]

CHAR sCopyright\[100\]

CHAR sLabel\[100\]

CHAR sReleaseDate\[100\]

INTEGER nNumTracks

CHAR sCode\[100\]

INTEGER nDiscNumber

}

STRUCTURE \_AlbumStruct2

{

CHAR sArtist\[100\]

CHAR sTitle\[100\]

INTEGER nNumTracks

}

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* VARIABLE DEFINITIONS GO BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_VARIABLE

VOLATILE \_AlbumStruct AlbumStruct\[3\]

VOLATILE \_AlbumStruct2 AlbumStruct2\[3\]

VOLATILE CHAR sBinaryString\[10000\]

VOLATILE CHAR sXMLString\[50000\]

VOLATILE LONG lPos

VOLATILE SLONG slFile

VOLATILE SLONG slReturn

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* STARTUP CODE GOES BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_START

(\* assign some values \*)

AlbumStruct\[1\].lTitleID = 11101000

AlbumStruct\[1\].sArtist = 'Buffet, Jimmy'

AlbumStruct\[1\].sTitle = 'Living & Dying in 3/4 Time'

AlbumStruct\[1\].sCopyright = 'MCA'

AlbumStruct\[1\].sLabel = 'MCA'

AlbumStruct\[1\].sReleaseDate = '1974'

AlbumStruct\[1\].nNumTracks = 11

AlbumStruct\[1\].sCode = '3132333435'

AlbumStruct\[1\].nDiscNumber = 91

AlbumStruct\[2\].lTitleID = 17248229

AlbumStruct\[2\].sArtist = 'Buffet, Jimmy'

AlbumStruct\[2\].sTitle = 'Off to See the Lizard'

AlbumStruct\[2\].sCopyright = 'MCA'

AlbumStruct\[2\].sLabel = 'MCA'

AlbumStruct\[2\].sReleaseDate = '1989'

AlbumStruct\[2\].nNumTracks = 11

AlbumStruct\[2\].sCode = '3132333436'

AlbumStruct\[2\].nDiscNumber = 105

AlbumStruct\[3\].lTitleID = 12328612

AlbumStruct\[3\].sArtist = 'Buffet, Jimmy'

AlbumStruct\[3\].sTitle = 'A-1-A'

AlbumStruct\[3\].sCopyright = 'MCA'

AlbumStruct\[3\].sLabel = 'MCA'

AlbumStruct\[3\].sReleaseDate = '1974'

AlbumStruct\[3\].nNumTracks = 11

AlbumStruct\[3\].sCode = '3132333437'

AlbumStruct\[3\].nDiscNumber = 189

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* THE EVENTS GOES BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_EVENT

(\* CONVERT AND SAVE \*)

BUTTON_EVENT\[dvTP,1\]

{

PUSH:

{

(\* CONVERT TO BINARY \*)

lPos = 1

slReturn = VARIABLE_TO_STRING (AlbumStruct,sBinaryString,lPos)

SEND_STRING 0,"'POSITION=',ITOA(lPos),'; RETURN=',ITOA(slReturn)"

(\* CONVERT TO XML \*)

lPos = 1

slReturn = VARIABLE_TO_XML (AlbumStruct,sXMLString,lPos,0)

SEND_STRING 0,"'POSITION=',ITOA(lPos),'; RETURN=',ITOA(slReturn)"

(\* NOW WE CAN SAVE THESE BOTH TO DICS \*)

slFile = FILE_OPEN('BinaryEncode.xml',nFileWrite)

IF (slFile \> 0)

{

slReturn = FILE_WRITE(slFile,sBinaryString,LENGTH_STRING(sBinaryString))

IF (slReturn \< 0) SEND_STRING 0,"'FILE WRITE FAIL RETURN=',ITOA(slReturn)"

slReturn = FILE_CLOSE(slFile)

IF (slReturn \< 0) SEND_STRING 0,"'FILE CLOSE FAIL RETURN=',ITOA(slReturn)"

}

slFile = FILE_OPEN('XMLEncode.xml',nFileWrite)

IF (slFile \> 0)

{

slReturn = FILE_WRITE(slFile,sXMLString,LENGTH_STRING(sXMLString))

IF (slReturn \< 0) SEND_STRING 0,"'FILE WRITE FAIL RETURN=',ITOA(slReturn)"

slReturn = FILE_CLOSE(slFile)

IF (slReturn \< 0) SEND_STRING 0,"'FILE CLOSE FAIL RETURN=',ITOA(slReturn)"

}

(\* Clear string \*)

sBinaryString = ""

sXMLString = ""

}

}

(\* READ AND DECODE \*)

BUTTON_EVENT\[dvTP,2\]

{

PUSH:

{

(\* NOW WE CAN SAVE THESE BOTH TO DICS \*)

slFile = FILE_OPEN('BinaryEncode.xml',nFileRead)

IF (slFile \> 0)

{

slReturn = FILE_READ(slFile,sBinaryString,MAX_LENGTH_STRING(sBinaryString))

IF (slReturn \< 0) SEND_STRING 0,"'FILE WRITE FAIL RETURN=',ITOA(slReturn)"

slReturn = FILE_CLOSE(slFile)

IF (slReturn \< 0) SEND_STRING 0,"'FILE CLOSE FAIL RETURN=',ITOA(slReturn)"

}

slFile = FILE_OPEN('XMLEncode.xml',nFileRead)

IF (slFile \> 0)

{

slReturn = FILE_READ(slFile,sXMLString,MAX_LENGTH_STRING(sXMLString))

IF (slReturn \< 0) SEND_STRING 0,"'FILE WRITE FAIL RETURN=',ITOA(slReturn)"

slReturn = FILE_CLOSE(slFile)

IF (slReturn \< 0) SEND_STRING 0,"'FILE CLOSE FAIL RETURN=',ITOA(slReturn)"

}

(\* CONVERT TO BINARY \*)

lPos = 1

slReturn = STRING_TO_VARIABLE (AlbumStruct,sBinaryString,lPos)

SEND_STRING 0,"'POSITION=',ITOA(lPos),'; RETURN=',ITOA(slReturn)"

(\* CONVERT TO XML \*)

lPos = 1

slReturn = XML_TO_VARIABLE (AlbumStruct,sXMLString,lPos,0)

SEND_STRING 0,"'POSITION=',ITOA(lPos),'; RETURN=',ITOA(slReturn)"

}

}

(\* READ AND DECODE \*)

(\* THE BINARY WILL FAIL SINCE THE DECODE TYPE DOES NOT MATCH THE ENCODE TYPE
\*)

(\* THE XML WILL NOT FAIL SINCE IT DOES NOT REQUIRE DATA TO BE THE SEQUENTIAL
\*)

BUTTON_EVENT\[dvTP,3\]

{

PUSH:

{

(\* NOW WE CAN SAVE THESE BOTH TO DISC \*)

slFile = FILE_OPEN('BinaryEncode.xml',nFileRead)

IF (slFile \> 0)

{

slReturn = FILE_READ(slFile,sBinaryString,MAX_LENGTH_STRING(sBinaryString))

IF (slReturn \< 0) SEND_STRING 0,"'FILE WRITE FAIL RETURN=', ITOA(slReturn)"

slReturn = FILE_CLOSE(slFile)

IF (slReturn \< 0) SEND_STRING 0,"'FILE CLOSE FAIL RETURN=', ITOA(slReturn)"

}

slFile = FILE_OPEN('XMLEncode.xml',nFileRead)

IF (slFile \> 0)

{

slReturn = FILE_READ(slFile,sXMLString,MAX_LENGTH_STRING(sXMLString))

IF (slReturn \< 0) SEND_STRING 0,"'FILE WRITE FAIL RETURN=',ITOA(slReturn)"

slReturn = FILE_CLOSE(slFile)

IF (slReturn \< 0) SEND_STRING 0,"'FILE CLOSE FAIL RETURN=',ITOA(slReturn)"

}

(\* CONVERT TO BINARY \*)

lPos = 1

slReturn = STRING_TO_VARIABLE (AlbumStruct2,sBinaryString,lPos)

SEND_STRING 0,"'POSITION=',ITOA(lPos),'; RETURN=',ITOA(slReturn)"

(\* CONVERT TO XML \*)

lPos = 1

slReturn = XML_TO_VARIABLE (AlbumStruct2,sXMLString,lPos,0)

SEND_STRING 0,"'POSITION=',ITOA(lPos),'; RETURN=',ITOA(slReturn)"

}

}

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* THE ACTUAL PROGRAM GOES BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_PROGRAM

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* END OF PROGRAM \*)

(\* DO NOT PUT ANY CODE BELOW THIS COMMENT \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

See Also

- [STRING_TO_VARIABLE](STRING_TO_VARIABLE.md)
- [VARIABLE_TO_STRING](VARIABLE_TO_STRING.md)
- [LENGTH_VARIABLE_TO_STRING](LENGTH_VARIABLE_TO_STRING.md)
- [XML_TO_VARIABLE](XML_TO_VARIABLE.md)
- [VARIABLE_TO_XML](VARIABLE_TO_XML.md)
- [LENGTH_VARIABLE_TO_XML](LENGTH_VARIABLE_TO_XML.md)
