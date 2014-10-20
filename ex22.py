print: prints a message in the console.
#: is used to comment things
+: add operation, concatenate strings
-: subtract operation
*: multiply operation
/: divide operation
<: less than
>: greater than
": used to define the start and end of a string
': used to define the start and end of a string
,: used to separate strings in a print, separate arguments when defining or calling a function. It can also be used to unpack argv into various variables.
=: used to assign values to a variable
%: used to give a format to a substitution in a print. %d integer, %s string, %r raw format. It is also used after the string to asign the substitute value.
(): used to pass arguments to a function or to define the arguments that it needs.
\:used to define escape special characters and to escape special characters.
""": can be used to define a block of text to print.
\n: new line
\t: tab
argv: contains parameters given when calling a python script.
raw_input(): used to get an input from a user typing in the console. Can be given a string as a parameter that can be used as a prompt. Regular input has a security bug.
open(file, permissions): opens a file, returning a file descriptor. Can be given the open mode (r, r+w, w...).
file.read(): returns the content of a file.
file.close(): closes the file descriptor
file.write(data): writes a string to the file
len(data): length in bytes
exists(file): returns true if a file exists
def function(parameter, ...):: defines a function
file.seek(byte): sets the current reading line to a byte offset.
file.tell(): tells you the next byte to read.
return: returns a value after the execution of a function
