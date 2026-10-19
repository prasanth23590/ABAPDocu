---
title: "AMDP - Calling an AMDP Procedure from SQLScript (Client-safe)"
source_file: abenamdp_call_amdp_cs_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Examples > AMDP - Examples (Client-safe)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Calling an AMDP Procedure from SQLScript (Client-safe)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how am AMDP procedure is called from an AMDP procedure. The AMDP methods involved use the AMDP options [`READ-ONLY`](abapmethods_amdp_options.md) and [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md) and are [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

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
CLASS cl_demo_amdp_call_amdp_prcd_cs DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_amdp_call_amdp_prcd_cs IMPLEMENTATION. 
  METHOD main. 
 
    TRY. 
        cl_demo_amdp_call_amdp_cs=>get_scarr( 
          IMPORTING carriers = FINAL(carriers) ). 
      CATCH cx_amdp_execution_error cx_amdp_version_error 
            cx_amdp_creation_error INTO FINAL(amdp_error). 
        out->write( amdp_error->get_text( ) ). 
        RETURN. 
    ENDTRY. 
 
    out->write( carriers ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The [SQLScript procedure](../../abap-glossary/abensql_script_procedure_glosry.md) of the AMDP method `GET_SCARR` of the AMDP class `CL_DEMO_AMDP_CALL_AMDP_CS` calls a different AMDP procedure that is implemented in the private AMDP method `GET_SCARR_AMDP` of the same class:

``` abap
METHOD get_scarr BY DATABASE PROCEDURE 
                      FOR HDB LANGUAGE SQLSCRIPT 
                      USING cl_demo_amdp_call_amdp_cs=>get_scarr_amdp. 
  call "CL_DEMO_AMDP_CALL_AMDP_CS=>GET_SCARR_AMDP"( :carriers ); 
ENDMETHOD.
```abap
METHOD get_scarr_amdp BY DATABASE PROCEDURE 
                           FOR HDB LANGUAGE SQLSCRIPT 
                           USING demo_cds_scarr_entity. 
  carriers  = select carrid, carrname, currcode, url 
                     from demo_cds_scarr_entity; 
ENDMETHOD.
```

The called database procedure must be specified after the addition [`USING`](abapmethod_by_db_proc.md) of the statement `METHOD`.
