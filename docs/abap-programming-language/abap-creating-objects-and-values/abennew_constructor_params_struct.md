---
title: "NEW, Structures"
source_file: abennew_constructor_params_struct.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > NEW, Instance Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# NEW, Structures

## Syntax

``` abap
... NEW dtype|#( [let_exp] 
                 [BASE dobj] 
                 comp1 = dobj1 comp2 = dobj2 ... ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md)

## Description

If `dtype` is a structured data type or `#` stands for such a type, the individual components can be specified as `comp1`, `comp2`, ... Each component of the created anonymous data object can be assigned a data object with the same data type as the component, or can be converted to it. The assignment is made for all data types in accordance with the corresponding [assignment rules](../abap-processing-internal-data/abenconversion_rules.md).

An addition `BASE` can be specified in front of the individual component assignments, followed by a data object `dobj`. `dobj` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The type of `dobj` must be convertible to the type of the anonymous data object. If `BASE` is specified, the content of `dobj` is assigned to the anonymous data object before the individual components are assigned. If the character `#` is specified for the type of the anonymous data object and the type cannot be determined from the operand position of the `VALUE` expression, the type of `dobj` is used for this expression if it is known and structured.

`dobj1`, `dobj2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). Optionally, a `LET` expression [`let_exp`](../abap-declarations/abaplet.md) can be specified in front of the assignments to define local helper fields that can be used on the right side of the assignments.

If a component is structured itself, either a suitable data object can be assigned to the entire substructure or its components can be specified using the structure component selector (`-`). Non-specified components are ignored and keep their type-specific initial value, or the value assigned using `BASE`. If the addition `BASE` is used, at least one component must also be specified.

It is not allowed to assign multiple values to a component.

- It leads to a syntax error, if the name of a component appears more than once on the left side of an assignment.

- A syntax warning occurs, if structures are involved that contain [component groups](../../abap-glossary/abencomponent_group_glosry.md). Then, the respective components can be addressed as usual as components of the including structures or by using the name of the component group. In that case, a component might be assigned more than one value and the latest assignment is considered.

## Hints

- The assignments can be specified in any order in parentheses.

- If a component with a complex data type is to be constructed in an operand position, the value operator [`VALUE`](abenconstructor_expression_value.md) can be used. This affects tabular components, for example. This is also possible for structured components but is not necessary since the subcomponents can be addressed using the structure component selector.

- When a constructor expression is assigned to a reference variable using `NEW`, the original reference is available in the entire expression in the target variable. The target variable is not overwritten until the expression is completed. In the case of the value operator [`VALUE`](abenvalue_constructor_params_struc.md), however, the target variable can only be assigned to a helper variable using `LET` and is then no longer available.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an anonymous data object with a nested structure type and tabular components. The subcomponents of `col2` are addressed directly using the structure component selector. [`VALUE`](abenconstructor_expression_value.md) must be used to construct the tabular component `col3` because the [syntax](abennew_constructor_params_itab.md) for constructing internal tables cannot be specified directly as an operand.

``` abap
TYPES: t_itab TYPE TABLE OF i WITH EMPTY KEY, 
       BEGIN OF t_struct, 
         col1 TYPE i, 
         BEGIN OF col2, 
           col1 TYPE i, 
           col2 TYPE t_itab, 
         END OF col2, 
         col3 TYPE t_itab, 
       END OF t_struct. 
 
DATA itab TYPE t_itab. 
 
DATA dref TYPE REF TO data. 
 
dref = NEW t_struct( col1 = 1 
                     col2-col1 = 2 
                     col2-col2 = itab 
                     col3 = VALUE #( ( 1 ) 
                                     ( 2 ) 
                                     ( 3 ) ) ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of `BASE`. The type of the return value of `base1` is transferred in the construction of `ref1`. This is not possible in the construction of `ref2`, since `base2` is not structured. In both results, `col1` and `col3` have the values `xx` or `zz` assigned using `BASE`, whereas `col2` has the directly assigned value *BB*.

``` abap
TYPES: 
  BEGIN OF struct, 
    col1 TYPE c LENGTH 2, 
    col2 TYPE c LENGTH 2, 
    col3 TYPE c LENGTH 2, 
  END OF struct. 
 
FINAL(base1) = VALUE struct( col1 = 'xx' col2 = 'yy' col3 = 'zz' ). 
FINAL(ref1)  = NEW #( BASE base1 col2 = 'BB' ). 
 
FINAL(base2)   = `xxyyzz`. 
FINAL(ref2)  = NEW struct( BASE base2 col2 = 'BB' ). 
 
cl_demo_output=>write(   ref1->* ). 
cl_demo_output=>display( ref2->* ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See also the examples for the value operator [`VALUE`](abenvalue_constructor_params_struc.md).
