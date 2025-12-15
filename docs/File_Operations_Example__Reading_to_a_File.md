---
title: File_Operations_Example__Reading_to_a_File
---

# File Operations Example: Reading to a File

The code example below shows a framework for using the file operations to read the contents of a file.  

- Nothing is said about parsing the actual file contents, as this is completely dependent on the information contained in the file.  
- Similar to serial or IP communications, the ability to interpret the data is all about knowing the format in which it is provided.

Note: This example assumes that the data in the file is text that is broken up in to a number of lines (such as a CSV file).  For files that are not separated in to lines, [FILE_READ](FILE_READ.md) is a better candidate.

DEFINE_FUNCTION readStuffFromFile(CHAR cFileName\[\])

{

   STACK_VAR SLONG slFileHandle     // stores the tag that represents the file (or and error code)

   LOCAL_VAR SLONG slResult         // stores the number of bytes read (or an error code)

   STACK_VAR CHAR  oneline\[2000\]    // a buffer for reading one line.  Must be as big or bigger than the biggest line

   STACK_VAR INTEGER INC

   slFileHandle = [FILE_OPEN](FILE_OPEN.md)(cFileName,FILE_READ_ONLY) // OPEN FILE FROM THE BEGINNING

    

   IF(slFileHandle\>0)               // A POSITIVE NUMBER IS RETURNED IF SUCCESSFUL

      {

         slResult = 1               // seed with a good number so the loop runs at least once

         WHILE(slResult\>0)

         {

            slResult = [FILE_READ_LINE](FILE_READ_LINE.md)(slFileHandle,oneline,MAX_LENGTH_STRING(oneline)) // grab one line  
                                                                                         from the file

            parseLineFromFile(oneline)

         }

           [FILE_CLOSE](FILE_CLOSE.md)(slFileHandle)   // CLOSE THE LOG FILE

      }           

      ELSE

         {

             SEND_STRING 0,"'FILE OPEN ERROR:',ITOA(slFileHandle)"  // IF THE LOG FILE COULD NOT BE  
                                                                      CREATED

         }

      }

DEFINE_FUNCTION parseLineFromFile(CHAR aLine\[\])

{

      /// normal string parsing here...

}

See Also

- [File Operations Example: Writing to a File](File_Operations_Example__Writing_to_a_File.md)
- [File Operation Keywords](File_Operation_Keywords.md)

