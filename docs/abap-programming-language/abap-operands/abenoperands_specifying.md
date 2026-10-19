---
title: "Specifying Individual Operands"
source_file: abenoperands_specifying.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Specifying Individual Operands

There are three ways to specify the [names of operands](abenoperands_names.md):

- [Static Specification](abenoperands_specifying.md#static-specification)

- [Dynamic Specification in Parentheses](abenoperands_specifying.md#dynamic-specification-in-parentheses)

- [Dynamic Specification](abenoperands_specifying.md#dynamic-specification)

## Static Specification

The name of the operand must be specified directly. If the name of a data object is specified, the specified name is used and not the content of the data object.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Static method call as example for a direct operand specification.

``` abap
cl_demo_spfli=>get_spfli( ).
```

## Dynamic Specification in Parentheses

For some statements that normally expect a static specification, there is a syntactic form that allows the name of a character-like data object to be specified in parentheses at the operand position. At the time of execution, the data object must contain the actual name of the operand. It depends on the operand position, whether the name must be specified in upper case letters or is case-insensitive.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic method call as example for a dynamic operand specification.

``` abap
DATA(meth) = 'GET_SPFLI'. 
 
CALL METHOD cl_demo_spfli=>(meth).
```

For statements that contain lists of operands or full parts of statements, an internal table with a character-like line type can often be specified in parentheses. The table lines must then contain the tokens or the names of the individual operands.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Internal table used for dynamic token specification in ABAP SQL.

``` abap
DATA itab TYPE TABLE OF string WITH EMPTY KEY. 
 
itab = VALUE #( ( `carrid = 'LH' AND ` ) 
                ( `connid = '400' `    ) ). 
 
SELECT * 
       FROM spfli 
       WHERE (itab) 
       INTO TABLE @FINAL(result).
```

## Dynamic Specification

At many operand positions, the system expects character-like data objects that contain the actual names of the individual operands at the time of execution. To enable the static specification of these operands, literals must be used. It depends on the operand position, whether the name must be specified in upper case letters or is case-insensitive.

### Hint

In some rare cases, there may be exceptions to these rules, where operands must be set directly in parentheses or quotation marks as literals, but no data objects can be specified. This is noted in the corresponding syntax descriptions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The content of data object `dobj` specifies the function module to be called.

CALL FUNCTION dobj.
