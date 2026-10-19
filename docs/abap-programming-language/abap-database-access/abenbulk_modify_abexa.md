---
title: "MODIFY, FROM TABLE"
source_file: abenbulk_modify_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > MODIFY writable_obj"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY, FROM TABLE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the statement [`MODIFY`](abapmodify_dbtab.md) `...` [`FROM TABLE`](abapmodify_source.md).

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
CLASS cl_demo_bulk_modify DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_bulk_modify IMPLEMENTATION. 
  METHOD main. 
    "has a unique secondary index k1, v1 
    DELETE FROM demo_bulk_modify.                       "#EC CI_NOWHERE 
    "has a unique secondary index k1, v1 
    INSERT demo_bulk_modify FROM @( VALUE #( k1 = 1 k2 = 1 v1 = 1 ) ). 
 
    DATA itab TYPE STANDARD TABLE OF demo_bulk_modify WITH EMPTY KEY. 
    itab = VALUE #( ( k1 = 1 k2 = 2 v1 = 1 ) 
                    ( k1 = 1 k2 = 1 v1 = 2 ) ). 
 
    MODIFY demo_bulk_modify FROM TABLE @itab. "platform dependent! 
 
    SELECT * 
           FROM demo_bulk_modify 
           INTO TABLE @FINAL(result). 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The DDIC database table `DEMO_BULK_MODIFY` has two key fields, `K1` and `K2`, and a regular field `V1`. A unique secondary index `IDX` comprises the fields `K1` and `V1`. The DDIC database table is filled with a row 1, 1, 1, and then the statement `MODIFY ... FROM TABLE` is used with an internal table with the rows 1, 2, 1 and 1, 1, 2. The result is platform-dependent:

- In database systems with row-by-row `MODIFY`, like the SAP HANA database, the first row of the internal table cannot be inserted because of the unique secondary index. The second row of the internal table overwrites the existing row and the result is a row with the content 1, 1, 2.

- In database systems with row-by-row `MODIFY` and termination after a failed insert, such as SAP MaxDB, no change is made and the result is a row with the content 1, 1, 1.

- In database systems with block-by-block `UPDATE` and `INSERT`, such as ORACLE DB, the existing row is overwritten with the second row of the internal table and then the first row of the internal table is inserted. The result is two rows 1, 1, 2 and 1, 2, 1.
