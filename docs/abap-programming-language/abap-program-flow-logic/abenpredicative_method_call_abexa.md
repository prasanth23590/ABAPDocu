---
title: "rel_exp - Predicative Method Calls"
source_file: abenpredicative_method_call_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicative Method Calls, Data Objects as Relational Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Predicative Method Calls

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [predicative method calls](../../abap-glossary/abenpredicative_method_call_glosry.md).

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
CLASS cl_demo_prdctv_method_call DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_prdctv_method_call IMPLEMENTATION. 
  METHOD main. 
    IF cl_abap_demo_services=>is_production_system( ). 
      out->write( 
         'This demo cannot be executed in a production system' ). 
      RETURN. 
    ENDIF. 
 
    DATA carrier TYPE spfli-carrid VALUE 'LH'. 
    cl_demo_input=>new( )->request( CHANGING field = carrier ). 
 
    out->next_section( 'IF' ). 
    IF cl_demo_spfli=>get_spfli( to_upper( carrier ) ). 
      out->write( 'Filled' ). 
    ELSE. 
      out->write( 'Not filled' ). 
    ENDIF. 
 
    out->next_section( 'COND' 
      )->write( COND string( 
                  WHEN cl_demo_spfli=>get_spfli( to_upper( carrier ) ) 
                    THEN `Filled` 
                  ELSE `Not filled` ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The functional method `IS_PRODUCTION_SYSTEM` of the class `CL_ABAP_DEMO_SERVICES` is called [predicatively](abenpredicative_method_calls.md) in a [control statement](../../abap-glossary/abencontrol_statement_glosry.md) `IF` to ensure that the current system is not a production system. The method called is a [predicate method](../../abap-glossary/abenpredicate_method_glosry.md).

The functional method `GET_SPFLI` of the class `CL_DEMO_SPFLI` is then called [predicatively](abenpredicative_method_calls.md) once in a [control statement](../../abap-glossary/abencontrol_statement_glosry.md) `IF` and once in a [conditional expression](../../abap-glossary/abenconditional_expression_glosry.md) `COND`. In this case, it is not a [predicate method](../../abap-glossary/abenpredicate_method_glosry.md). The relational expressions are true or false, depending on whether the internal table returned is empty or filled.
