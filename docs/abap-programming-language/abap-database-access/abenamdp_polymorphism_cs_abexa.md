---
title: "AMDP - AMDP Methods in Interfaces and Superclasses (Client-safe)"
source_file: abenamdp_polymorphism_cs_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Examples > AMDP - Examples (Client-safe)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - AMDP Methods in Interfaces and Superclasses (Client-safe)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how AMDP methods are implemented from interfaces and superclasses. The AMDP methods use the AMDP option [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md) and thus are [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

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
CLASS cl_demo_amdp_polymorphism_cs DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_amdp_polymorphism_cs IMPLEMENTATION. 
  METHOD main. 
    DATA: iref TYPE REF TO if_demo_amdp_interface_cs, 
          cref TYPE REF TO cl_demo_amdp_superclass_cs. 
 
    cref = NEW cl_demo_amdp_subclass_hdb_cs( ). 
    iref = NEW cl_demo_amdp_implement_hdb_cs( ). 
 
    TRY. 
        iref->get_scarr( IMPORTING carriers = FINAL(result1) ). 
        cref->get_scarr( IMPORTING carriers = FINAL(result2) ). 
      CATCH cx_amdp_execution_error cx_amdp_version_error 
            cx_amdp_creation_error INTO FINAL(amdp_error). 
        out->write( amdp_error->get_text( ) ). 
        RETURN. 
    ENDTRY. 
 
    ASSERT result1 = result2. 
 
    out->write( name = 'Result' 
                data = result1 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An interface `IF_DEMO_AMDP_INTERFACE_CS` and an abstract superclass `CL_DEMO_AMDP_SUPERCLASS_CS` implement the tag interface `IF_AMDP_MARKER_HDB` and contain the method `GET_SCARR`, which meets the prerequisites of an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md).

The interface method is implemented as an AMDP method in the class `CL_DEMO_AMDP_IMPLEMENT_HDB_CS`. In the same way, the method of the abstract superclass is redefined in the concrete subclass `CL_DEMO_AMDP_SUBCLASS_HDB_CS`.
