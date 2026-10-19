---
title: "Streaming for Internal Tables"
source_file: abenitab_streams.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Streaming > Streaming for Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Streaming for Internal Tables

The specific classes for [streaming](../../abap-glossary/abenstreaming_glosry.md) for internal tables are:

- `CL_ABAP_ITAB_C_READER`

- `CL_ABAP_ITAB_C_WRITER`

- `CL_ABAP_ITAB_X_READER`

- `CL_ABAP_ITAB_X_WRITER`

These classes are subclasses of the abstract superclasses [`CL_ABAP_MEMORY_...`](abendata_objects_streams.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of an internal table using a reader stream.

``` abap
DATA itab TYPE TABLE OF string WITH EMPTY KEY. 
 
itab = VALUE #( ( `abc` ) ( `def` ) ( `ghi` ) ). 
 
FINAL(itab_reader) = NEW cl_abap_itab_c_reader( itab ). 
 
WHILE itab_reader->data_available( ) = 'X'. 
  cl_demo_output=>write_text( itab_reader->read( 3 ) ). 
ENDWHILE. 
itab_reader->close( ). 
 
cl_demo_output=>display( ).
```
