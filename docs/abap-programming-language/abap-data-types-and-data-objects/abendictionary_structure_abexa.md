---
title: "Structure from ABAP Dictionary"
source_file: abendictionary_structure_abexa.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Structures > Examples of Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Structure from ABAP Dictionary

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a structure from the ABAP Dictionary and its use.

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
CLASS cl_demo_dictionary_structure DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_dictionary_structure IMPLEMENTATION. 
  METHOD main. 
    DATA carrier TYPE scarr. 
    carrier-carrid = 'UA'. 
    cl_demo_input=>new( )->request( CHANGING field = carrier-carrid ). 
    SELECT SINGLE * 
           FROM scarr 
           WHERE carrid = @carrier-carrid 
           INTO @carrier. 
    out->write( carrier ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Structure types of the ABAP Dictionary are typically used in ABAP programs to define structures or internal tables with a structured line type to process data that is imported from the database. The example shows how a structure `carrier` local to a method is declared by reference to a database table `SCARR` defined in the ABAP Dictionary, and used as the target area of a [`SELECT`](../abap-database-access/abapselect.md) statement.
