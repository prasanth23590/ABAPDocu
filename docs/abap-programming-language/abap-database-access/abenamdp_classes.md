---
title: "AMDP - Classes"
source_file: abenamdp_classes.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Classes

An AMDP class is a global class in the [class library](../../abap-glossary/abenclass_library_glosry.md) that implements the following [tag interface](../../abap-glossary/abentag_interface_glosry.md):

- `IF_AMDP_MARKER_HDB` for the SAP HANA database.

The suffix `_HDB` stands for the SAP HANA database and it is currently the only database system for which the ABAP Managed Database Procedures can be implemented in AMDP methods of the class.

An AMDP class can contain both regular methods and [AMDP methods](abenamdp_methods.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Simple example for an AMDP class. The class `CL_DEMO_AMDP_SCARR` implements the interface `IF_AMDP_MARKER_HDB` and contains an AMDP method `SELECT_SCARR` that reads data from the [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) `DEMO_CDS_SCARR_ENTITY`:

``` abap
METHOD select_scarr 
       BY DATABASE PROCEDURE FOR HDB 
       LANGUAGE SQLSCRIPT 
       OPTIONS READ-ONLY 
       USING demo_cds_scarr_entity. 
  scarr_tab = 
  SELECT * 
         FROM "DEMO_CDS_SCARR_ENTITY" 
         WHERE mandt = clnt 
         ORDER BY carrid; 
ENDMETHOD.
```

The following program section calls the method and displays the result.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA result TYPE cl_demo_amdp_scarr=>scarr_tab. 
 
NEW cl_demo_amdp_scarr( )->select_scarr( 
  EXPORTING clnt = sy-mandt 
  IMPORTING scarr_tab = result ). 
 
out->write( result ). 
 
out->display( ).
```
