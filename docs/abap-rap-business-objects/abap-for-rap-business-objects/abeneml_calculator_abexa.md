---
title: "ABAP EML - RAP Calculator"
source_file: abeneml_calculator_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES > Examples for ABAP EML MODIFY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - RAP Calculator

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a calculator that is implemented in a RAP context using a simple managed RAP BO. The calculator uses a create operation with an ABAP EML `MODIFY ENTITY` statement to perform calculations based on user input, which includes numbers and an arithmetic operator. The RAP BO is draft-enabled, but it does not play a role in this particular example. For more information refer to the related example [ABAP EML in Use: Managed, Draft-Enabled RAP BO with Late Numbering](abensheet_rap_calc_dr_ln_m_abexa.md).

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
CLASS cl_demo_rap_eml_u_calculator DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      num1      TYPE c LENGTH 7, 
      num2      TYPE c LENGTH 7, 
      arithm_op TYPE c LENGTH 1. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_u_calculator IMPLEMENTATION. 
  METHOD main. 
 
    cl_demo_input=>new( 
     )->add_text( `RAP Calculator with a managed RAP BO` 
     )->add_text( `Please enter numbers and an operand ` && 
                  `(+ - * P) for the calculation:` 
     )->add_field( CHANGING field = num1 
     )->add_line( 
     )->add_field( CHANGING field = arithm_op 
     )->add_line( 
     )->add_field( CHANGING field = num2 
     )->request( ). 
 
    out->begin_section( `RAP Calculator with a managed RAP BO` ). 
 
    TRY. 
        MODIFY ENTITY demo_cs_rap_draft_m 
         CREATE AUTO FILL CID 
         FIELDS ( num1 num2 arithm_op ) WITH VALUE #( 
          ( num1 =  num1 
            num2 = num2 
            arithm_op = arithm_op ) ). 
      CATCH cx_root INTO FINAL(err). 
    ENDTRY. 
 
    IF err IS NOT INITIAL. 
      out->write( err->get_text( ) ). 
    ENDIF. 
 
    COMMIT ENTITIES RESPONSE OF demo_cs_rap_draft_m REPORTED DATA(rep). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    IF rep-calc IS NOT INITIAL. 
      out->write_html( '<b>The calculation cannot be executed:</b>' ). 
      LOOP AT rep-calc 
         ASSIGNING FIELD-SYMBOL(<reported>). 
        out->write( <reported>-%msg->if_message~get_text( ) ). 
      ENDLOOP. 
    ENDIF. 
 
    SELECT SINGLE num1, arithm_op, num2, calc_result 
     FROM demo_cs_tab_calc INTO @FINAL(calculation). 
 
    IF calculation IS NOT INITIAL. 
      out->write_html( 
             '<b>Calculation result</b>' 
            )->write( calculation ). 
    ENDIF. 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_cs_tab_calc. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class.
