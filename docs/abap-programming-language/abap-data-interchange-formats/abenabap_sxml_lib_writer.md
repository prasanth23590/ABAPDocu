---
title: "sXML - XML Writer"
source_file: abenabap_sxml_lib_writer.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Classes and Interfaces > sXML - XML Reader and XML Writer"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - XML Writer

The interfaces and classes of sXML library for the [XML writer](abenabap_sxml_lib_render.md) are:

``` abap
 
IF_SXML   IF_SXML_NSURI_HELPER 
  |         | 
  |---------| 
  | 
  |--IF_SXML_WRITER 
       | 
       |--CL_SXML_WRITER 
            | 
            |-------CL_SXML_STRING_WRITER 
            | 
            |-------CL_SXML_TABLE_WRITER 
            | 
            |-------CL_SXML_DATASET_WRITER 
            | 
            |-------CL_SXML_HTTP_WRITER 
            | 
            |  IF_SXML_XOP 
            |    | 
            |----|--CL_SXML_XOP_WRITER
```

The interface `IF_SXML_WRITER` contains the components that are required for every XML writer. The abstract class `CL_SXML_WRITER` implements all the general methods of an XML writer. The subclasses of these classes are specializations for different repositories of XML data and provide a factory method for creating the associated XML writer.

The higher-level interfaces contain components for XML reader and XML writer:

- `IF_SXML` contains constants for the supported XML format.

- `IF_SXML_NSURI_HELPER` contains methods for namespaces.
