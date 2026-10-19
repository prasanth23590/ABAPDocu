---
title: "asXML - Mapping of Structures"
source_file: abenasxml_structure_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Examples of Mappings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the mapping of structures.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_asxml_structure DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asxml_structure IMPLEMENTATION. 
  METHOD main. 
    DATA: BEGIN OF struct, 
            num TYPE i VALUE 20, 
            dat TYPE d VALUE '20060627', 
          END OF struct, 
          xmlstr TYPE xstring. 
 
    CALL TRANSFORMATION id 
                        SOURCE structure = struct 
                        RESULT XML xmlstr. 
 
    out->write_xml( xmlstr ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The structure `struct` is mapped as a superordinate XML element for its components.
