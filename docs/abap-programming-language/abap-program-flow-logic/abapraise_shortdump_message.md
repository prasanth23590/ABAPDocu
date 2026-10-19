---
title: "RAISE SHORTDUMP, message"
source_file: abapraise_shortdump_message.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Runtime Errors > RAISE SHORTDUMP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAISE SHORTDUMP, message

## Syntax

``` abap
... { MESSAGE tn(id) 
            | { ID mid TYPE mtype NUMBER num } 
              [WITH dobj1 ... dobj4] } 
  | { USING MESSAGE } ...  
```

[`MESSAGE`](abapraise_exception_message.md) · [`USING MESSAGE`](abapraise_exception_message.md)

## Description

The addition `MESSAGE` of the statement [`RAISE SHORTDUMP`](abapraise_shortdump.md) and of the addition [`THROW SHORTDUMP`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md) passes the specification of a [message](../../abap-glossary/abenmessage_glosry.md) to the exception object. Syntax and semantics are the same as in the addition [`MESSAGE`](abapraise_exception_message.md) of the statement [`RAISE EXCEPTION`](abapraise_exception_class.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of a runtime error with an exception object of the exception class `CX_DEMO_DYN_T100`, which implements the interface [`IF_T100_DYN_MSG`](../abap-text-repositories/abenif_t100_dyn_msg.md). The addition `MESSAGE` is used to pass the properties of a message that determines the exception text.

``` abap
RAISE SHORTDUMP TYPE cx_demo_dyn_t100 
  MESSAGE ID 'SABAPDEMOS' 
          TYPE 'I' 
          NUMBER '888' 
          WITH 'I' 'need' 'a' 'break!'.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of a runtime error with an exception object of the exception class `CX_DEMO_T100`, which implements the interface [`IF_T100_MESSAGE`](../abap-text-repositories/abenif_t100_message.md). The additions `MESSAGE` and `EXPORTING` are used to pass the properties of a message that determines the exception text.

``` abap
RAISE SHORTDUMP TYPE cx_demo_t100 
                MESSAGE ID 'SABAPDEMOS' 
                        NUMBER '888' 
                EXPORTING text1 = 'I' 
                          text2 = 'need' 
                          text3 = 'a' 
                          text4 = 'break!'.
```
