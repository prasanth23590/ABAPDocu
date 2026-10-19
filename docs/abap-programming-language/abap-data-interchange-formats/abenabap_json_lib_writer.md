---
title: "JSON - JSON Writer"
source_file: abenabap_json_lib_writer.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON Library > JSON - Classes and Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - JSON Writer

The classes and interfaces of the JSON writer are:

``` abap
 
IF_JSON_WRITER 
  | 
  |--CL_JSON_WRITER 
       | 
       |--CL_JSON_STRING_WRITER 
       | 
       |--CL_JSON_XSTRING_WRITER
```

The interface `IF_JSON_WRITER` contains the components that are required for every JSON writer. The abstract class `CL_JSON_WRITER` implements all general methods of a JSON writer.
