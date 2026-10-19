---
title: "AMDP - Access to ABAP Types (Client-safe)"
source_file: abenamdp_abap_types_cs_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Examples > AMDP - Examples (Client-safe)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Access to ABAP Types (Client-safe)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how to access ABAP types using the [AMDP macro](../../abap-glossary/abenamdp_macro_glosry.md) [`$ABAP.type`](abenamdp_abap_types.md). The AMDP method uses the AMDP option [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md) and is [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

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
CLASS cl_demo_amdp_abap_types_acc_cs DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_amdp_abap_types_acc_cs IMPLEMENTATION. 
  METHOD main. 
    DATA itab TYPE cl_demo_amdp_abap_types_cs=>itab. 
 
    cl_demo_amdp_abap_types_cs=>demo_abap_types( 
      IMPORTING itab = itab ). 
 
    out->write( itab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example calls the following [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) of the class `CL_DEMO_AMDP_ABAP_TYPES_CS`:

``` abap
METHOD demo_abap_types BY DATABASE PROCEDURE 
                       FOR HDB LANGUAGE SQLSCRIPT. 
 
  DECLARE mytab table( mandt  "$ABAP.type( mandt )", 
                       uname  "$ABAP.type( syst_uname )", 
                       langu  "$ABAP.type( syst_langu )", 
                       datum  "$ABAP.type( syst_datum )", 
                       text   "$ABAP.type( line-text )", 
                       number "$ABAP.type( f )" ); 
 
  mytab.mandt[1]  := session_context('CLIENT'); 
  mytab.uname[1]  := session_context('APPLICATIONUSER'); 
  mytab.langu[1]  := session_context('LOCALE_SAP'); 
  mytab.datum[1]  := session_context('SAP_SYSTEM_DATE'); 
  mytab.text[1]   := cast( 0123456789 as "$ABAP.type( line-text )" ); 
  mytab.number[1] := 333 ; 
 
  itab = select * from :mytab; 
ENDMETHOD.
```

In the method, a local table variable `mytab` is declared using `DECLARE` in [SQLScript](../../abap-glossary/abensql_script_glosry.md). All columns of the table variable are declared using the [`AMDP`](../../abap-glossary/abenamdp_macro_glosry.md) macro [`$ABAP.type`](abenamdp_abap_types.md) with reference to ABAP types. The first four ABAP types, `MANDT`, `SYST_UNAME`, `SYST_LANGU`, and `SYST_DATUM`, are defined in the ABAP Dictionary. Type `line_text` comes from a `TYPES` statement of its own class. `f` stands for the built-in numeric ABAP type.

The table variable is filled using assignments to columns with one row, where the specification of the AMDP macro `$ABAP.type` is also shown in a `CAST` expression. Finally, the content of the table variable is imported into the tabular output parameter `itab`, whose row type is made up of components of the same ABAP types, which are used to define the table variable.
