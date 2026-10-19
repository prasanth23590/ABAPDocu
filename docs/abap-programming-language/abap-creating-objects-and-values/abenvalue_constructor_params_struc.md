---
title: "VALUE, Structures"
source_file: abenvalue_constructor_params_struc.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > VALUE, Value Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# VALUE, Structures

## Syntax

``` abap
... VALUE dtype|#( [let_exp] 
                   [BASE dobj] 
                   comp1 = dobj1 comp2 = dobj2 ... ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md)

## Description

If `dtype` is a structured data type or `#` stands for a type like this, the individual components can be specified as named arguments `comp1`, `comp2`, ... Each component of the return value can be assigned a data object that has the same data type as the component, or whose data type can be converted to this data type. This assignment is made for all data types in accordance with the corresponding [assignment rules](../abap-processing-internal-data/abenconversion_rules.md).

An addition `BASE` can be specified in front of the individual component assignments, followed by a data object `dobj`. `dobj` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The type of `dobj` must be convertible to the type of the return value. If `BASE` is specified, the content of `dobj` is assigned to the return value before the individual components are assigned. If the character `#` is specified for the type of the return value and the type cannot be determined from the operand position of the `VALUE` expression, the type of `dobj` is used for this expression if it is known and structured.

`dobj1`, `dobj2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). An optional `LET` expression [`let_exp`](../abap-declarations/abaplet.md) can be specified in front of the assignments to define local helper fields that can be used on the right side of the assignments.

If a component is structured itself, either a suitable data object can be assigned to the entire substructure or its components can be listed individually using the structure component selector (`-`). Non-specified components are ignored and keep their type-specific initial value or the value assigned using `BASE`. If the addition `BASE` is used, at least one component must also be specified.

If the `VALUE` operator is used as the source of an assignment to a structure, this structure is first initialized after any [`LET`](../abap-declarations/abaplet.md) expressions are evaluated or the structure is first assigned the data object `dobj` after `BASE`. The assignments are then executed directly in the parentheses, with the structure components as target fields.

It is not allowed to assign multiple values to a component.

- It leads to a syntax error, if the name of a component appears more than once on the left side of an assignment.

- A syntax warning occurs, if structures are involved that contain [component groups](../../abap-glossary/abencomponent_group_glosry.md). Then, the respective components can be addressed as usual as components of the including structures or by using the name of the component group. In that case, a component might be assigned more than one value and the latest assignment is considered.

## Hints

- The assignments can be specified in any order in the parentheses after the optional additions `LET ... IN` and `BASE`, in any order.

- If a component with a complex data type is to be constructed in an operand position, the value operator `VALUE` can be used again. Tabular components, for example, are affected by this. This is also possible for structured components, but not necessary since the subcomponents can be addressed using the structure component selector.

- The rule that a target structure of an assignment is first completely overwritten and then processed directly can produce surprising results if structure components on the left side are specified as data objects to be assigned on the right side. The assignments on the right are not evaluated and assigned first, but the current value is used for each assignment. If the entire structure or structure components on the left side are needed on the right side, however, they can be saved in local helper variables using a [`LET`](../abap-declarations/abaplet.md) expression, since this expression is evaluated first.

- If the target table is specified as `dobj` after `BASE` in an assignment to an existing structure, no assignment takes place before the component assignments are evaluated, and the target structure just keeps its value instead.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Three different ways of filling a nested structure `struct` with values. The structure is given the same values each time.

``` abap
TYPES:  BEGIN OF t_col2, 
           col1 TYPE i, 
           col2 TYPE i, 
        END OF t_col2. 
 
TYPES: BEGIN OF t_struct, 
         col1 TYPE i, 
         col2 TYPE t_col2, 
       END OF t_struct. 
 
DATA: struct TYPE t_struct, 
      col2 TYPE t_col2. 
 
struct = VALUE t_struct( col1 = 1 
                         col2-col1 = 1 
                         col2-col2 = 2 ). 
 
col2   = VALUE   t_col2( col1 = 1 
                         col2 = 2 ). 
struct = VALUE t_struct( col1 = 1 
                         col2 = col2 ). 
 
struct = VALUE t_struct( col1 = 1 
                         col2 = VALUE #( col1 = 1 
                                         col2 = 2 ) ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example shows the effects that occur when components of a target structure are used as assignment sources. After the assignment to `struct1`, `col1` and `col2` have the value 0 and `col3` and `col4` have the value 5. The original values of `col1` and `col2` are not switched and `col3` is not given the original value of `col4`. The assignment to `struct2` demonstrates how the behavior can be changed by saving the target object to a helper variable `x` and using it. In `struct2`, the original values of `col1` and `col2` are switched and `col3` is given the original value of `col4`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  BEGIN OF struct, 
    col1 TYPE i VALUE 1, 
    col2 TYPE i VALUE 2, 
    col3 TYPE i VALUE 3, 
    col4 TYPE i VALUE 4, 
  END OF struct, 
  struct1 LIKE struct, 
  struct2 LIKE struct. 
 
struct1 = struct2 = struct. 
 
struct1 = VALUE #( col1 = struct1-col2 
                   col2 = struct1-col1 
                   col4 = 5 
                   col3 = struct1-col4 ). 
 
out->write( struct1 ). 
 
struct2 = VALUE #( LET x = struct2 IN 
                   col1 = x-col2 
                   col2 = x-col1 
                   col4 = 5 
                   col3 = x-col4 ). 
 
out->write( struct2 ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of `BASE`. The type of the return value of `base1` is transferred in the construction of `struct1`. This is not possible in the construction of `struct2`, since `base2` is not structured. In both results, `col1` and `col3` have the values `xx` or `zz` assigned using `BASE`, whereas `col2` has the directly assigned value *BB*.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF struct, 
    col1 TYPE c LENGTH 2, 
    col2 TYPE c LENGTH 2, 
    col3 TYPE c LENGTH 2, 
  END OF struct. 
 
FINAL(base1)   = VALUE struct( col1 = 'xx' col2 = 'yy' col3 = 'zz' ). 
FINAL(struct1) = VALUE #( BASE base1 col2 = 'BB' ). 
 
FINAL(base2)   = `xxyyzz`. 
FINAL(struct2) = VALUE struct( BASE base2 col2 = 'BB' ). 
 
out->write( struct1 ). 
out->write( struct2 ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of `BASE` with a [`CORRESPONDING` expression](../abap-processing-internal-data/abenconstructor_expr_corresponding.md) for an assignment between two incompatible structures. `struct1` is first assigned only the identically named components of `struct2` and then the remaining components are explicitly supplied. The same can be done for the columns of an internal table by performing an appropriate assignment within an iteration using [`FOR`](../abap-processing-internal-data/abenfor_itab.md).

``` abap
DATA: 
  BEGIN OF struct1, 
    col1 TYPE i, 
    col2 TYPE i, 
    col3 TYPE i, 
    col4 TYPE i, 
    col5 TYPE i, 
  END OF struct1, 
  BEGIN OF struct2, 
    col1 TYPE i VALUE 1, 
    col2 TYPE i VALUE 2, 
    col3 TYPE i VALUE 3, 
  END OF struct2. 
 
struct1 = VALUE #( BASE CORRESPONDING #( struct2 ) col4 = 4 col5 = 5 ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Constructing a structure with [component groups](../../abap-glossary/abencomponent_group_glosry.md). All `VALUE` operators have the same effect.

``` abap
TYPES: 
  BEGIN OF struc1, 
    col1 TYPE i, 
    col2 TYPE i, 
  END OF struc1. 
 
TYPES: 
  BEGIN OF struc2, 
    col3 TYPE i, 
    col4 TYPE i, 
  END OF struc2. 
 
TYPES 
  BEGIN OF struct. 
INCLUDE TYPE struc1 AS name1. 
INCLUDE TYPE struc2 AS name2. 
TYPES 
  END OF struct. 
 
 
FINAL(struct1) = VALUE struct( col1 = 1 col2 = 2 
                              col3 = 3 col4 = 4 ). 
 
FINAL(struct2) = VALUE struct( name1-col1 = 1 name1-col2 = 2 
                              name2-col3 = 3 name2-col4 = 4  ). 
 
FINAL(struct3) = VALUE struct( name1 = VALUE #( col1 = 1 col2 = 2 ) 
                              name2 = VALUE #( col3 = 3 col4 = 4 ) ). 
 
ASSERT struct1 = struct2. 
ASSERT struct2 = struct3.
```
