---
title: "NEW, Single Value for All Data Types"
source_file: abennew_constructor_params_single.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > NEW, Instance Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# NEW, Single Value for All Data Types

## Syntax

``` abap
... NEW dtype|#( [let_exp] dobj ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md)

## Description

If `dtype` is a non-generic elementary data type, a structured type, a table type, or a reference type or `#` is used for a type like this, a single data object `dobj` can be specified as a single operand `dobj` that is convertible to or from data type `dtype`. `dobj` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). The value of `dobj` is assigned to the created anonymous data object. The assignment is made in accordance with the applicable [assignment rules](../abap-processing-internal-data/abenconversion_rules.md). Optionally, a `LET` expression [`let_exp`](../abap-declarations/abaplet.md) can be specified in front of the data object to define local helper fields.

## Hints

- In particular, an expression specified for `dobj` can be a constructor expression itself or contain a constructor expression.

- When a constructor expression is assigned to a reference variable using `NEW`, the original reference is available in the entire expression in the target variable. The target variable is not overwritten until the expression is completed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an anonymous data object of the type `string`, whose value is determined using a string expression.

``` abap
DATA input TYPE c LENGTH 10 VALUE 'World'. 
cl_demo_input=>request( CHANGING field = input ). 
 
DATA dref TYPE REF TO string. 
dref =  NEW string( `Hello ` && input && `!` ). 
 
cl_demo_output=>display( dref->* ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

For each line read, a structured anonymous data object is created in a `SELECT` loop, to which the content of the line is assigned. The object is created in the general expression position of the statement `APPEND` and the created data reference is appended directly to an internal table with the appropriate line type. The result is a table that references all new anonymous data objects.

``` abap
DATA dref_tab TYPE TABLE OF REF TO t100 WITH EMPTY KEY. 
 
DATA wa TYPE t100. 
 
SELECT * 
       FROM t100 
       WHERE sprsl = @sy-langu 
       INTO @wa. 
  APPEND NEW #( wa ) TO dref_tab. 
ENDSELECT.
```
