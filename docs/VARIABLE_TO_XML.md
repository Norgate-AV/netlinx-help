# VARIABLE_TO_XML

**Syntax:**

```netlinx
SINTEGER VARIABLE_TO_XML(CONSTANT VARIANTARRAY A, CHAR B[], LONG C, LONG D)
```

**Parameters:**

- **A** is the variable (any type) to be encoded
- **B** is the CHAR array to hold the resulting XML
- **C** is the beginning encoding position. Encoding will start as B[C]
- **D** is the encoding flag. These can be used together
  - Value $01 is "Encode with Types". If the bit is set, types will be included for every variable being encoded. The default is to not include types. The constant XML_ENCODE_TYPES can be used to specify this flag.
  - Value $10 is "Encoded CHAR arrays as using data list". The constant XML_ENCODE_CHAR_AS_LIST can be used to specify this flag. See the Encoding and Decoding: Binary and XML section on page 175.
  - Value $20 is "Array Encoding is Little-Ending". The constant XML_ENCODE_LE can be used to specify this flag.

**Return:**

- 3 = XML decode data type mismatch
- 2 = XML decode data too small, more members in structure
- 1 = structure too small, more members in XML decode string
- 0 = decoded OK
- -1 = decode variable type mismatch
- -2 = decode data too small, decoder ran out of data. Most likely poorly formed XML
- -3 = output character buffer was too small

**Example:**

```netlinx
DEFINE_TYPE

STRUCTURE _AlbumStruct
{
    LONG lTitleID
    CHAR sArtist[100]
    CHAR sTitle[100]
}

DEFINE_VARIABLE

_AlbumStruct MyAlbumStruct[3]
LONG  lPos
SLONG  slReturn
SLONG  slFile
SLONG  slResult
CHAR  sBinaryString[10000]
CHAR  sXMLString[50000]

DEFINE_START

MyAlbumStruct[1].lTitleID = 11101000
MyAlbumStruct[1].sArtist = 'Buffet, Jimmy'
MyAlbumStruct[1].sTitle = 'Living & Dying in ¾ Time'

MyAlbumStruct[2].lTitleID = 11101012
MyAlbumStruct[2].sArtist = 'Sinatra, Frank'
MyAlbumStruct[2].sTitle = 'Come Fly With Me'

MyAlbumStruct[3].lTitleID = 33101000
MyAlbumStruct[3].sArtist = 'Holiday, Billie'
MyAlbumStruct[3].sTitle = 'Lady in satin'

DEFINE_EVENT

BUTTON_EVENT[TP,1]  // Convert And Save
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
        SEND_STRING 0,"'POSITION=',ITOA(lPos),' – Result = ',ITOA(slReturn)"
        
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

BUTTON_EVENT[TP,2]  // Read and Decode
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
```

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
- [STRING_TO_VARIABLE](STRING_TO_VARIABLE.md)
- [VARIABLE_TO_STRING](VARIABLE_TO_STRING.md)
- [LENGTH_VARIABLE_TO_STRING](LENGTH_VARIABLE_TO_STRING.md)
- [LENGTH_VARIABLE_TO_XML](LENGTH_VARIABLE_TO_XML.md)
- [XML_TO_VARIABLE](XML_TO_VARIABLE.md)
- [FORMAT](FORMAT.md)
- [Intrinsic Data Types](Intrinsic_Data_Types.md)

