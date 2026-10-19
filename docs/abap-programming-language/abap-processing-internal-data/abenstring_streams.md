---
title: "Streaming for Strings"
source_file: abenstring_streams.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Streaming > Streaming for Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Streaming for Strings

The specific classes for [streaming](../../abap-glossary/abenstreaming_glosry.md) for strings are:

- `CL_ABAP_STRING_C_READER`

- `CL_ABAP_STRING_C_WRITER`

- `CL_ABAP_STRING_X_READER`

- `CL_ABAP_STRING_X_WRITER`

These classes are subclasses of the abstract superclasses [`CL_ABAP_MEMORY_...`](abendata_objects_streams.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A writer stream is used to fill a string and then pass it to a reader stream. The reader stream skips three characters and then reads the remaining characters.

``` abap
FINAL(string_writer) = NEW cl_abap_string_c_writer( ). 
 
DO 10 TIMES. 
  string_writer->write( |{ sy-index - 1 }| ). 
ENDDO. 
string_writer->close( ). 
 
FINAL(string_reader) = 
  NEW cl_abap_string_c_reader( string_writer->get_result_string( ) ). 
 
string_reader->skip( 3 ). 
WHILE string_reader->data_available( ) = 'X'. 
  cl_demo_output=>write( string_reader->read( 1 ) ). 
ENDWHILE. 
string_reader->close( ). 
 
cl_demo_output=>display( ).
```
