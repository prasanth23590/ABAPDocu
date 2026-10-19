---
title: "AMDP - SQLScript with Tabular CHANGING Parameter (Client-safe)"
source_file: abenamdp_changing_cs_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Examples > AMDP - Examples (Client-safe)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - SQLScript with Tabular CHANGING Parameter (Client-safe)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how an SQLScript procedure is implemented using AMDP with a tabular `CHANGING` parameter. Since the AMDP option [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md) is used for the AMDP methods, they are [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

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
CLASS cl_demo_amdp_changing_para_cs DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_amdp_changing_para_cs IMPLEMENTATION. 
  METHOD main. 
    DATA lower TYPE scarr-carrid VALUE 'AA'. 
    DATA upper TYPE scarr-carrid VALUE 'BA'. 
    DATA call_flag TYPE abap_boolean. 
    cl_demo_input=>new( 
       )->add_field( CHANGING field = lower 
       )->add_field( CHANGING field = upper 
       )->add_line( 
       )->add_field( EXPORTING text = 'Indirect call' 
                               as_checkbox = abap_true 
                     CHANGING  field = call_flag 
       )->request( ). 
 
    DATA carriers TYPE cl_demo_amdp_changing_cs=>t_carriers. 
    SELECT mandt, carrid 
           FROM scarr 
           WHERE carrid BETWEEN @lower AND @upper 
           ORDER BY mandt, carrid 
           INTO CORRESPONDING FIELDS OF TABLE @carriers. 
    out->write( carriers ). 
 
    TRY. 
        IF call_flag IS INITIAL. 
          NEW cl_demo_amdp_changing_cs( 
            )->get_carriers( CHANGING carriers = carriers ). 
        ELSE. 
          NEW cl_demo_amdp_changing_cs( 
            )->call_get_carriers( CHANGING carriers = carriers ). 
        ENDIF. 
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

The following [SQLScript procedure](../../abap-glossary/abensql_script_procedure_glosry.md) is implemented in the AMDP method `GET_CARRIERS` of the AMDP class `CL_DEMO_AMDP_CHANGING_CS`:

``` abap
METHOD get_carriers BY DATABASE PROCEDURE FOR HDB 
                       LANGUAGE SQLSCRIPT 
                    USING demo_cds_scarr_entity. 
  carriers  = select s.* 
                   from demo_cds_scarr_entity as s 
                   inner join :carriers as c 
                     on s.mandt  = c.mandt and 
                        s.carrid = c.carrid; 
ENDMETHOD.
```

The tabular `CHANGING` parameter `carriers` can be used in the procedure in read positions and write positions. Internally, the database procedure uses an identically named output parameter to which the initial value of the `CHANGING` parameter is assigned at the beginning of the execution of the procedure using the invisible `IN` parameter `carriers__in__` (see [SQLScript for the SAP HANA Database](abenamdp_hdb_sqlscript.md)).

A further method `CALL_GET_CARRIERS` demonstrates how the SQLScript procedure implemented in `GET_CARRIERS` is called from a different SQLScript procedure.

``` abap
METHOD call_get_carriers BY DATABASE PROCEDURE FOR HDB 
                            LANGUAGE SQLSCRIPT 
                         USING cl_demo_amdp_changing_cs=>get_carriers. 
  call "CL_DEMO_AMDP_CHANGING_CS=>GET_CARRIERS"( 
    CARRIERS__IN__  => :CARRIERS, 
    CARRIERS        => :CARRIERS ); 
ENDMETHOD.
```

In this case, the implicit `IN` parameter `carriers__in__` must be filled explicitly with the actual parameter to be modified.

## Hint

This is a syntax example. The same function can be achieved with the same efficiency in ABAP SQL. AMDP is not needed in simple cases like this.
