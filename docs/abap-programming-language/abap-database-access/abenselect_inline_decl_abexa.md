---
title: "SELECT, Inline Declarations"
source_file: abenselect_inline_decl_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, INTO, APPENDING > SELECT, INTO target"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Inline Declarations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates inline declarations in the statement `SELECT`.

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
CLASS cl_demo_select_inline_dclrtn DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_inline_dclrtn IMPLEMENTATION. 
  METHOD main. 
 
    DATA carrier TYPE scarr-carrid VALUE 'LH'. 
    cl_demo_input=>new( )->request( CHANGING field = carrier ). 
 
    SELECT * 
       FROM scarr INNER JOIN spfli ON scarr~carrid = spfli~carrid 
       WHERE scarr~carrid = @carrier 
       ORDER BY scarr~carrid 
       INTO TABLE @FINAL(result1). 
 
    SELECT scarr~*, spfli~* 
       FROM scarr INNER JOIN spfli ON scarr~carrid = spfli~carrid 
       WHERE scarr~carrid = @carrier 
       ORDER BY scarr~carrid 
       INTO TABLE @FINAL(result2). 
 
    ASSERT result1 = result2. 
 
    out->write( result1 ). 
 
    SELECT scarr~carrname, 
           spfli~connid, spfli~cityfrom, spfli~cityto 
       FROM scarr INNER JOIN spfli ON scarr~carrid = spfli~carrid 
       WHERE scarr~carrid = @carrier 
       ORDER BY scarr~carrid 
       INTO TABLE @FINAL(result3). 
 
    out->write( result3 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The inline declarations of the first two `SELECT` statements create the same internal tables. The row type of the internal tables is a structure with the two substructures `scarr` and `spfli` that each have the columns of the two joined DDIC database tables as components. The substructures are resolved in a table comprehension in the output.

The inline declaration of the third `SELECT` statement creates an internal table with a non-nested row structure. The components of the row are determined directly using the columns specified in the `SELECT` list.
