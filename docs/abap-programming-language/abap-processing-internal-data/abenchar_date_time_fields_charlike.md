---
title: "Character-Like Access to Date Fields and Time Fields"
source_file: abenchar_date_time_fields_charlike.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Date Fields and Time Fields > Access to Date Fields and Time Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Character-Like Access to Date Fields and Time Fields

Character-like access to character-like content of date fields and time fields is evaluated in a character-like way. The character-like nature of date fields and time fields can be exploited, for example, to access detailed information. To avoid unexpected results from this type of access, the [validity](abenchar_date_time_fields_validity.md) of the content of the date or time fields must be ensured. Most [statements](abenstring_processing_statements.md) and [functions](abenstring_functions.md) used in [character string processing](abenabap_data_string.md) are not suitable for processing date fields and time fields because they generally produce invalid content.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates how [substring functions](abensubstring_functions.md) can be used to extract the components year, month, day, hour, minute, and second from date fields and time fields.

``` abap
DATA: date TYPE d, 
      time TYPE t. 
 
DATA: year   TYPE i, 
      month  TYPE i, 
      day    TYPE i, 
      hour   TYPE i, 
      minute TYPE i, 
      second TYPE i. 
 
date = cl_demo_date_time=>get_user_date( ). 
time = cl_demo_date_time=>get_user_time( ). 
 
year   = substring( val = date off = 0 len = 4 ). 
month  = substring( val = date off = 4 len = 2 ). 
day    = substring( val = date off = 6 len = 2 ). 
hour   = substring( val = time off = 0 len = 2 ). 
minute = substring( val = time off = 2 len = 2 ). 
second = substring( val = time off = 4 len = 2 ).
```
