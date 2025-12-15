---
title: Working_With_UniCode
---

# Working With Unicode

Before you begin to work with Unicode, you must enable the UTF-8 Unicode option and the Unicode Compile option in NetLinx Studio.

- The UTF-8 Unicode option directs NetLinx Studio to store your file as UTF-8, which will support Unicode characters.

- The Unicode Compile option directs NetLinx Studio to process the \_WC pre-processor statements to properly handle Unicode embedded in your source files at compile time.

## Enabling UTF-8 in NetLinx Studio:

To enable UTF-8, in NetLinx Studio:

1.  Choose Settings \> Preferences from the menu bar.

2.  Select the Editor tab of the Preferences dialog.

3.  Under Display, check the [Enable UTF-8 format checkbox](javascript:TextPopup(this)).

    ![](Preferences%20dialog%20-%20UTF-8%20option.jpg)

4.  Close the Preferences dialog.

## Enabling Unicode Compiling in NetLinx Studio:

1.  Choose Settings \> Preferences from the menu bar

2.  Select the NetLinx Compiler tab.

3.  Under Options, check the [Enable \_WC Preprocessor checkbox](javascript:TextPopup(this)).

    ![](Preferences%20dialog%20-%20Enable%20_WC%20Preprocessor%20option.jpg)

4.  Close the Preferences dialog.

## Including the Unicode Library

- The Unicode Library is implemented in a NetLinx Include file, UnicodeLib.axi, that must be included in your program in order to access the Unicode functions.  

- The Unicode Library is located in an Include file located in the C:\Program Files\Common Files\AMXShare\AXIs directory.  

Because this location is the default Include search path, you do not need to specify the directory in the include statement.

To include the Unicode Library to your program add these lines to your program:

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\*                   INCLUDE FILES GO BELOW                \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

\#INCLUDE 'UnicodeLib.axi'

## Defining a Unicode String Literal

To enter Unicode characters into your program, enclose the characters in single quotes, like you would any other string, and wrap the string literal in the Unicode macro \_WC.  

Example:

```
\_WC(‘Your string goes here’)

```
Note: All Unicode string literals must be wrapped in the \_WC macro.  Failing to wrap a Unicode string in the \_WC macro will result in a [compiler error](Unicode-Related_Compiler_Errors.md).

## Storing a Unicode String

Unicode strings are stored in WIDECHAR arrays, similar to the way ASCII strings are stored in CHAR arrays.

To define a WIDECHAR constant or variable and initialize it using a Unicode string literal, use the following syntax:

WIDECHAR wcMyString\[\] = \_WC(‘My String’)

Note: The “ wc” prefix is Hungarian notation for WIDECHAR.  This is simply a programming convention and is completely optional.  Hungarian notation helps you better identify your variables while you are programming and is a general recommended standard.  For more information, see Wikipedia’s Hungarian Notation page.

## Character Case Mappings

Converting between upper and lower case is accomplished by using the Unicode.org character database to determine the mapping between upper case and lower case characters.  

Note: Not all Unicode characters have an upper or lower case equivalent; these characters will not be affected by WC_UPPER_STRING and WC_LOWER_STRING.  Only the characters defined by Unicode.org as having an upper or lower case mapping are affected by these functions.  

## Concatenating Strings

Unicode strings and WIDECHAR arrays cannot be concatenated using the same syntax that ASCII strings use.  

In NetLinx, string expressions are enclosed in double quotes and can only contain 8-bit strings.  

To concatenate Unicode strings and WIDECHAR arrays, you must use the WC_CONCAT_STRING function:

wcMyString = WC_CONCAT_STRING(\_WC(‘First name’),\_WC(‘ SurName’))

Note: If you attempt to concatenate Unicode strings or WIDECHAR arrays using NetLinx string expressions, expect data loss.

## Right-to-Left Unicode Strings

Right-to-Left Unicode languages are stored in memory the same way left-to-right language are.  The first memory position of an array contains the first Logical character.  

You can access the right-most character of a Right-to-Left Unicode string using this notation:

wchChar = wcString\[1\]

Right-to-left languages are not stored differently than left-to-right languages, they are simply rendered differently than right to left languages. However, note that the functions WC_LEFT_STRING and WC_RIGHT_STRING remove a number of characters from the start and end of a string respectively.  Using WC_LEFT_STRING on a right-to-left language will return the number of right-most, i.e. first, characters you requested, not the left-most, i.e. end, characters.  

- WC_LEFT_STRING returns the number of characters request from the front of the string.

- WC_RIGHT_STRING return the number of characters requested from the end of the string, regardless of the language’s orientation.

## Sending Strings to a User Interface

Sending a WIDECHAR array to a user interface is  accomplished using WC_TP_ENCODE.  

WC_TP_ENCODE takes a WIDECHAR array and returns a CHAR array formatted for a user interface UNI or BAU command.

cMyString = WC_TP_ENCODE(wcMyString)

SEND_COMMAND dvTP,"'^UNI-1,0,',cMyString "

See Also

- [Reading and Writing to Files](Reading_and_Writing_to_Files.md)

- [Unicode-Related Compiler Errors](Unicode-Related_Compiler_Errors.md)

 

