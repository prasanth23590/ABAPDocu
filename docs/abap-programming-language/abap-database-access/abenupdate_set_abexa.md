---
title: "UPDATE, Use of SET"
source_file: abenupdate_set_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > UPDATE writable_obj > UPDATE writable_obj, source > UPDATE writable_obj, set_expression"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UPDATE, Use of SET

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how the addition `SET` of the statement `UPDATE` is used.

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
CLASS cl_demo_update DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_update IMPLEMENTATION. 
  METHOD main. 
    CONSTANTS id TYPE demo_cds_update_te-id VALUE 'X'. 
 
    DELETE FROM demo_cds_update_te WHERE id = @id. 
    INSERT demo_cds_update_te FROM @( VALUE demo_cds_update_te( 
      id   = id 
      col1 = 100 
      col2 = 100 
      col3 = 100 
      col4 = 100 ) ). 
 
    FINAL(num)   = 200. 
    FINAL(diff)  = 10. 
    FINAL(token) = `col4 = col4 - demo_cds_update_te~col1`. 
    UPDATE demo_cds_update_te 
           SET col1 = @num, 
               col2 = col2 + @diff, 
               col3 = col3 - @diff, 
              (token) 
           WHERE id = @id. 
 
    SELECT SINGLE * 
           FROM demo_cds_update_te 
           WHERE id = @id 
           INTO @FINAL(wa). 
    out->write( wa ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

It modifies the content of four columns of a row of the CDS table entity `DEMO_CDS_UPDATE_TE`:

- The column `COL1` is assigned the value 200.

- The value of the column `COL2` is raised by 10.

- The value of the column `COL3` is reduced by 10.

- The value of the column `COL4` is reduced dynamically by the value of the column `COL1` as it was before the execution of the statement.
