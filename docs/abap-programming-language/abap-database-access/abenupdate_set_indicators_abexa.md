---
title: "UPDATE, SET INDICATORS"
source_file: abenupdate_set_indicators_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > UPDATE writable_obj > UPDATE writable_obj, source > UPDATE writable_obj, set indicators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UPDATE, SET INDICATORS

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how the addition [`SET INDICATORS`](abapupdate_set_indicator.md) of the statement `UPDATE` is used.

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
CLASS cl_demo_update_set_indicator DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_update_set_indicator IMPLEMENTATION. 
  METHOD main. 
    DELETE FROM demo_update.                            "#EC CI_NOWHERE 
    INSERT demo_update FROM TABLE @( 
        VALUE #( ( id = 'A' col1 = '1' col2 = '10'   col3 = '100' ) 
                 ( id = 'B' col1 = '2' col2 = '20'   col3 = '200' ) 
                 ( id = 'C' col1 = '3' col2 = '30'   col3 = '300' ) 
                 ( id = 'D' col1 = '4' col2 = '40'   col3 = '400' ) 
                 ( id = 'E' col1 = '5' col2 = '50'   col3 = '500' ) 
                 ( id = 'F' col1 = '6' col2 = '60'   col3 = '600' ) ) ). 
 
    TYPES ind_wa TYPE demo_update WITH INDICATORS col_ind 
                 TYPE abap_boolean. 
    DATA ind_tab TYPE TABLE OF ind_wa. 
 
    ind_tab = VALUE #( 
           ( id = 'D' col4 = 4000 col_ind-col4 = abap_true ) 
           ( id = 'E' col4 = 5000 col_ind-col4 = abap_true ) 
           ( id = 'F' col4 = 6000 col_ind-col4 = abap_true ) ). 
 
    UPDATE demo_update FROM TABLE @ind_tab 
                       INDICATORS SET STRUCTURE col_ind. 
 
    SELECT * FROM demo_update 
             ORDER BY id 
             INTO TABLE @FINAL(result1). 
 
    out->write( result1 ). 
 
    UPDATE demo_update FROM TABLE @ind_tab. 
 
    SELECT * FROM demo_update 
             ORDER BY id 
             INTO TABLE @FINAL(result2). 
 
    out->write( result2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

It modifies the content of three fields of the CDS table entity `DEMO_CDS_UPDATE_TE`:

- The rows with the `ID` values D, E, and F are selected.

- Within these rows, the column `COL4` is indicated for change.

As a result, only these three fields are updated with new values.
