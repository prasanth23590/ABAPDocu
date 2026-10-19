---
title: "destination1 = destination2 = ..."
source_file: abapmove_multiples.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Special Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# destination1 = destination2 = ...

## Syntax

``` abap
destination1 = destination2 = ... = destination = rhs.  
```

## Description

The [assignment operator `=`](abenequals_operator.md) can be used to perform multiple assignments at once within a single statement. This statement is the same as:

``` abap
`destination  = rhs` 
`         ... = destination` 
`destination2 = ...` 
`destination1 = destination2.`
```

The same settings can be specified for `rhs` as for the simple [assignment](abenequals_operator.md). Only existing variables can be specified for `destination`, `destination1`, `destination2`, but no [inline declarations](../abap-declarations/abeninline_declarations.md).

## Hint

Any conversions are performed for each assignment, which means that a value assigned to a data object on the left side may be converted multiple times if the operands have different data types. To assign the value of `lhs` to different data objects with one conversion each, multiple statements are needed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the assignments, all involved data objects are given the name`Hugo`.

``` abap
DATA: name  TYPE string, 
      name1 TYPE string, 
      name2 TYPE string, 
      name3 TYPE string. 
 
name = `Hugo`. 
 
name3 = name2 = name1 = name.
```
