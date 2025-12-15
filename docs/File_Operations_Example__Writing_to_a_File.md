# File Operations Example: Writing to a File

The following example code demonstrates writing to a file (typical usage):

DEFINE_FUNCTION appendToFile (CHAR cFileName\[\],CHAR cLogString\[\])

{

   STACK_VAR SLONG slFileHandle     // stores the tag that represents the file (or and error code)

   LOCAL_VAR SLONG slResult         // stores the number of bytes written (or an error code)

   slFileHandle = [FILE_OPEN](FILE_OPEN.md)(cFileName,FILE_RW_APPEND) // OPEN OLD FILE (OR CREATE NEW ONE)    

   IF(slFileHandle\>0)               // A POSITIVE NUMBER IS RETURNED IF SUCCESSFUL

         {

         slResult = [FILE_WRITE_LINE](FILE_WRITE_LINE.md)(slFileHandle,cLogString,LENGTH_STRING(cLogString)) // WRITE THE NEW  
                                                                                         INFO

          [FILE_CLOSE](FILE_CLOSE.md)(slFileHandle)   // CLOSE THE LOG FILE

         }           

      ELSE

         {

         SEND_STRING 0,"'FILE OPEN ERROR:',ITOA(slFileHandle)" // IF THE LOG FILE COULD NOT BE CREATED

         }

}

 

Which would be called like this:

appendToFile(‘log.txt’,’Something happened…’)

 when an entry to this file needed to be written.

See Also

- [File Operations Example: Reading to a File](File_Operations_Example__Reading_to_a_File.md)

- [File Operation Keywords](File_Operation_Keywords.md)

