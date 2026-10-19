---
title: "AMDP - Implementation of SQLScript Procedures (Client-safe)"
source_file: abenamdp_cs_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Examples > AMDP - Examples (Client-safe)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Implementation of SQLScript Procedures (Client-safe)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how SQLScript procedures are implemented using AMDP. Since they implement a read access and are [client-safe](../../abap-glossary/abenclient_safe_glosry.md) by using the AMDP option [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md), the AMDP class can have the ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md).

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
CLASS cl_demo_amdp_sql_script_cs DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_amdp_sql_script_cs IMPLEMENTATION. 
  METHOD main. 
    NEW cl_demo_amdp_cs( 
      )->get_scarr_cds( IMPORTING carriers = DATA(result_cds) ). 
 
    NEW cl_demo_amdp_cs( 
      )->get_scarr_ddic( IMPORTING carriers = DATA(result_ddic) ). 
 
    SORT result_cds BY carrid. 
    SORT result_ddic BY carrid. 
 
    ASSERT result_cds = result_ddic. 
 
    out->write( result_cds ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Simple [SQLScript procedures](../../abap-glossary/abensql_script_procedure_glosry.md) are implemented in AMDP methods of an AMDP class `CL_DEMO_AMDP_CS`. Client handling is done by the AMDP option [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md). A [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) and a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) are used as sources. The resulting data are filtered implicitly by the current client and are the same for both method calls.

``` abap
METHOD get_scarr_cds BY DATABASE PROCEDURE FOR HDB 
                     LANGUAGE SQLSCRIPT 
                     USING demo_cds_scarr_entity. 
  carriers  = select carrid, carrname, currcode, url 
                     from demo_cds_scarr_entity; 
ENDMETHOD.
```abap
METHOD get_scarr_ddic BY DATABASE PROCEDURE FOR HDB 
                      LANGUAGE SQLSCRIPT 
                      USING scarr. 
  carriers  = select carrid, carrname, currcode, url 
                     from scarr; 
ENDMETHOD.
```

## Hint

This is a syntax example. The same function can be achieved with the same efficiency in ABAP SQL. AMDP is not needed in simple cases like this.
