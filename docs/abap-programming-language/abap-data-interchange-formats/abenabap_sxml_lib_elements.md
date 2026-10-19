---
title: "sXML - Named Entities"
source_file: abenabap_sxml_lib_elements.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Classes and Interfaces > sXML - Entities of XML Data"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Named Entities

The classes and interfaces in sXML Library used for object-oriented access to elements and attributes are:

``` abap
 
IF_SXML_NAMED 
  | 
  |  IF_SXML_NODE 
  |    | 
  |----|--IF_SXML_OPEN_ELEMENT---| 
  |                              | 
  |-------CL_SXML_NAMED----------| 
  |                              | 
  |                              |-- CL_SXML_OPEN_ELEMENT 
  | 
  |  IF_SXML_VALUE 
  |    | 
  |----|--IF_SXML_ATTRIBUTE------| 
  |                              | 
  |-------CL_SXML_NAMED----------| 
  |                              | 
  |                              |-- CL_SXML_ATTRIBUTE 
  | 
  |  IF_SXML_NODE 
  |    | 
  |----|--IF_SXML_CLOSE_ELEMENT--| 
  |                              | 
  |-------CL_SXML_NAMED----------| 
                                 | 
                                 |-- CL_SXML_CLOSE_ELEMENT
```
