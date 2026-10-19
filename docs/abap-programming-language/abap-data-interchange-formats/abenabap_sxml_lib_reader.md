---
title: "sXML - XML Reader"
source_file: abenabap_sxml_lib_reader.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Classes and Interfaces > sXML - XML Reader and XML Writer"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - XML Reader

The interfaces and classes of sXML library for the [XML reader](abenabap_sxml_lib_parse.md) are:

``` abap
 
IF_SXML   IF_SXML_NSURI_HELPER 
  |         | 
  |---------| 
  | 
  |--IF_SXML_READER 
       | 
       |--CL_SXML_READER 
            | 
            |--CL_SXML_STRING_READER 
            | 
            |--CL_SXML_TABLE_READER 
            | 
            |--CL_SXML_DATASET_READER 
            | 
            |--CL_SXML_HTTP_READER 
            | 
            |--CL_SXML_XOP_READER
```

The interface `IF_SXML_READER` contains the components that are required for every XML reader. The abstract class `CL_SXML_READER` implements all general methods of an XML reader. The subclasses of these classes are specializations for different sources of XML data and provide a factory method for creating the associated XML reader.

The higher-level interfaces contain components for XML reader and XML writer:

- `IF_SXML` contains constants for the supported XML format.

- `IF_SXML_NSURI_HELPER` contains methods for namespaces.
