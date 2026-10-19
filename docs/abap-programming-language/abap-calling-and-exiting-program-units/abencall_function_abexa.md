---
title: "Calling Function Modules"
source_file: abencall_function_abexa.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > CALL FUNCTION > CALL FUNCTION func"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Calling Function Modules

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how function modules are called.

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
CLASS cl_demo_call_function DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_call_function IMPLEMENTATION. 
  METHOD main. 
    DATA: itab TYPE spfli_tab, 
          jtab TYPE spfli_tab. 
 
    DATA carrier TYPE s_carr_id VALUE 'LH'. 
    cl_demo_input=>new( )->request( CHANGING field = carrier ). 
 
    CALL FUNCTION 'READ_SPFLI_INTO_TABLE' 
      EXPORTING 
        id        = carrier 
      IMPORTING 
        itab      = itab 
      EXCEPTIONS 
        not_found = 4. 
    IF sy-subrc <> 0. 
      MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno 
              INTO FINAL(msg). 
      out->write( msg ). 
    ENDIF. 
 
    TRY. 
        CALL FUNCTION 'READ_SPFLI_INTO_TABLE_NEW' 
          EXPORTING 
            id   = carrier 
          IMPORTING 
            itab = jtab. 
      CATCH cx_no_flight_found INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    ASSERT itab = jtab. 
    out->write( itab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The function modules `READ_SPFLI_INTO_TABLE` and `READ_SPFLI_INTO_TABLE_NEW` read all data from the database table `SPFLI` where the key field `CARRID` matches the import parameter `id` into the internal tables `itab` or `jtab`. If no suitable data can be found, exceptions are raised.

- In `READ_SPFLI_INTO_TABLE`, the non-class-based exception `NOT_FOUND` is raised by [`MESSAGE ... RAISING`](../abap-program-flow-logic/abapmessage_raising.md).

- In `READ_SPFLI_INTO_TABLE_NEW`, the class-based exception is raised `CX_NO_FLIGHT_FOUND` by [`RAISE EXCEPTION ... MESSAGE`](../abap-program-flow-logic/abapraise_exception.md). `CX_NO_FLIGHT_FOUND` implements the interface `IF_T100_DYN_MSG`.

Otherwise, the table is passed to the caller as an export parameter.

The actual parameters `carrier` and `itab` or `itab` have the same data types as the corresponding interface parameters of the function module. The exceptions are handled. The relevant exception text is accessed in different ways.

- In non-class-based exceptions, it is implicitly available via system fields.

- In class-based exceptions, it is specified by attributes of the exception object.
