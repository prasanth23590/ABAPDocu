---
title: "sXML - Exception Classes"
source_file: abenabap_sxml_lib_exceptions.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Classes and Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Exception Classes

The exception classes in the sXML library usually start with the prefix `CX_SXML`. The exceptions of category `CX_DYNAMIC_CHECK` are propagated to the caller and must be handled by the user. The subclass `CX_SXML_INTERNAL_ERROR` of `CX_NO_CHECK` represents internal errors in the library and cannot usually be handled properly in an application program.

``` abap
 
CX_ROOT 
  | 
  |--CX_DYNAMIC_CHECK 
  |    | 
  |    |--CX_ABAP_XML_NAME_ERROR 
  |    | 
  |    |--CX_SXML_ERROR 
  |         | 
  |         |--CX_SXML_ILLEGAL_ARGUMENT_ERROR 
  |         | 
  |         |--CX_SXML_NAME_ERROR 
  |         | 
  |         |--CX_SXML_PARSE_ERROR 
  |         | 
  |         |--CX_SXML_STATE_ERROR 
  | 
  |--CX_NO_CHECK 
       | 
       |--CX_SXML_INTERNAL_ERROR
```
