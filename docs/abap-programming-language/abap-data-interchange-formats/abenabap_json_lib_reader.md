---
title: "JSON - JSON Reader"
source_file: abenabap_json_lib_reader.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON Library > JSON - Classes and Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - JSON Reader

The classes and interfaces of the JSON reader are:

``` abap
 
IF_JSON_READER 
  | 
  |--CL_JSON_READER 
       | 
       |--CL_JSON_STRING_READER 
       | 
       |--CL_JSON_XSTRING_READER
```

The interface `IF_JSON_READER` contains the components that are required for every JSON reader. The abstract class `CL_JSON_READER` implements all general methods of a JSON reader.
