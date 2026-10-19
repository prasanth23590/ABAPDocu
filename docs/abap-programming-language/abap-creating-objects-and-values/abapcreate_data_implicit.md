---
title: "CREATE DATA dref"
source_file: abapcreate_data_implicit.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE DATA dref

## Syntax

``` abap
CREATE DATA dref.  
```

## Description

Creation of an anonymous data object with an implicit type. If neither of the additions `TYPE` or `LIKE` are specified, the data reference variable `dref` must be completely typed. The data object is then created with the static data type of the data reference variable.

## Hint

When the character `#` is used in an operand position with the operand type of a data reference variable, the [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abenconstructor_expression_new.md) works like the statement `CREATE DATA dref`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an anonymous data object of the type `SCARR` from the ABAP Dictionary. The type is implicitly determined using the static data type of the data reference variable.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA dref TYPE REF TO scarr. 
 
CREATE DATA dref. 
 
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = 'LH' 
       INTO @dref->*. 
 
out->write( |{ dref->carrid }, { dref->carrname }| ). 
 
out->display( ).
```

## Executable Example

[Creating Data Objects with Implicit Type](abencreate_data_implicit_abexa.md)
