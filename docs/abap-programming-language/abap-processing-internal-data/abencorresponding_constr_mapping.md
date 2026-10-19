---
title: "CORRESPONDING, mapping"
source_file: abencorresponding_constr_mapping.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > CORRESPONDING, Component Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CORRESPONDING, mapping

## Syntax

``` abap
... [ MAPPING {t1 = s1 [duplicates]} | 
                 ( t1 = s1 [duplicates] [MAPPING ...] [EXCEPT ...] ) | 
                 {t1 = [s1] DEFAULT expr} 
              {t2 = s2 [duplicates]} | 
                 ( t2 = s2 [duplicates] [MAPPING ...] [EXCEPT ...] ) | 
                 {t2 = [s2] DEFAULT expr} 
              ...  ] 
    [ EXCEPT {ti tj ...}|* ] ...  
```

[`duplicates`](abencorresponding_constr_dupl.md) · [`duplicates`](abencorresponding_constr_dupl.md) · [`duplicates`](abencorresponding_constr_dupl.md) · [`duplicates`](abencorresponding_constr_dupl.md)

### Addition

[1. `... MAPPING t1 = s1 [duplicates] t2 = s2 [duplicates] ...`](abencorresponding_constr_mapping.md#addition-1)

[2. `... t1 = [s1] DEFAULT expr ...`](abencorresponding_constr_mapping.md#addition-2)

[3. `... EXCEPT {t1 t2 ...}|*`](abencorresponding_constr_mapping.md#addition-3)

## Overview

### Description

Mapping rule for the component operator [`CORRESPONDING`](abenconstructor_expr_corresponding.md). The optional mapping rule overrides the default assignment of identically named components only. The additions `MAPPING` and `EXCEPT` can be used individually or together. `EXCEPT` must always be specified behind `MAPPING`.

### Hints

- The system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md) is used for assignments between structures or internal tables with a dynamic mapping rule.

- It is best to use the component operator for mapping tasks that can be solved using either the component operator or [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md).

## Addition 1

`... MAPPING t1 = s1 [duplicates] t2 = s2 [duplicates] ...`

### Description

Behind `MAPPING`, the components `s1`, `s2`,... of a source structure or source table are assigned to the components of a target structure or target table `t1`, `t2`, .... in mapping relationships.

If the components specified on the left and right of an equal sign of a mapping relationship are themselves structured or tabular with a structured line type, a separate mapping rule can be nested for them. Here, the mapping relationship is set in parentheses `( ... )` and a further mapping rule `MAPPING ...` and/or `EXCEPT ...` is specified behind the mapping relationship in accordance with the same rules as on the top level. The parentheses are not allowed if a nested mapping rule is not used.

If the components specified to the left and right of an equal sign of a mapping relationship are tabular, the addition [`duplicates`](abencorresponding_constr_dupl.md) can be used to control the behavior used when duplicate lines appear in target tables with unique table keys.

A component of a target object cannot occur more than once in a list behind `MAPPING`. The structure component selector cannot be used to access subcomponents. Components can only be mapped that are on the same nesting level. **Note:** When using the component selector (even though it is not allowed), a syntax warning indicating that the result is undefined or an error will be displayed.

If `MAPPING` is used, the table types involved must also have structured line types in the [basic form](abencorresponding_constr_arg_type.md) and the addition `DEEP` is set implicitly.

- In the [basic form](abencorresponding_constr_arg_type.md), `t1`, `t2`, ... are components of the target type and `s1`, `s2`, ... are components of the parameter `struct` or `itab`.

- In the [variant with lookup table](abencorresponding_constr_using.md), `t1`, `t2`, ... are columns of the parameter `itab` and `s1`, `s2`, ... are columns of the parameter `lookup_tab`.

The content of the component specified on the right side of an equal sign in a mapping relationship is assigned to each component specified on the left side. If there is an identically named component in the target structure for a component specified on the right side, it is also assigned content, unless it is listed on the left side of a mapping relationship itself. In elementary components, the assignment is made in accordance with the associated [assignment rules](abenconversion_rules.md). In structured and tabular components, the assignment is made in accordance with the rules of [`MOVE-CORRESPONDING`](abapmove-corresponding.md) with the addition `EXPANDING NESTED TABLES`.

Identically named components can also be listed on the right and left side of the equal sign of a mapping relationship. This is a good idea in the following cases:

- If the [variant with lookup table](abencorresponding_constr_using.md) are used, identically named components in a mapping relationship override the rule that the components `s1`, `s2`, ... and `t1`, `t2`, ... used for searches are not assigned by default.

- Identically named components must be listed in a mapping relationship if a nested mapping rule is to be specified for these components.

- Identically named tabular components can be listed in a mapping relationship to control the behavior of duplicate lines using [`duplicates`](abencorresponding_constr_dupl.md).

If the line type of a source table is elementary, the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` can be specified as a component on the right of an equal sign of a mapping relationship and the entire table line is mapped to the target component. In all other cases, the behavior is undefined when the pseudo component `table_line` is specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of the components of the structure `struct1` to the components of the structure `struct2` using mapping rules for the components at the top level and the components of the substructure.

``` abap
DATA: BEGIN OF struct1, 
        mcomp1 TYPE i VALUE 1, 
        mcomp2 TYPE i VALUE 2, 
        BEGIN OF substruc, 
          subcomp1 TYPE i VALUE 1, 
          subcomp2 TYPE i VALUE 2, 
          subcomp3 TYPE i VALUE 3, 
        END OF substruc, 
      END OF struct1. 
 
DATA: BEGIN OF struct2, 
        comp2 TYPE i, 
        comp1 TYPE i, 
        BEGIN OF substruc, 
          comp3 TYPE i, 
          comp2 TYPE i, 
          comp1 TYPE i, 
        END OF substruc, 
      END OF struct2. 
 
struct2 = 
  CORRESPONDING #( 
    struct1 MAPPING comp1    = mcomp1 
                    comp2    = mcomp2 
                  ( substruc = substruc MAPPING comp1 = subcomp1 
                                                comp2 = subcomp2 
                                                comp3 = subcomp3 ) ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` as the right side of a mapping rule. The content of the table lines of an internal table of type `itab1` is copied to column `col1` of an internal table of type `itab2`.

``` abap
TYPES: 
  itab1 TYPE STANDARD TABLE OF i WITH EMPTY KEY, 
  BEGIN OF struct, 
    col1 TYPE i, 
    col2 TYPE string, 
  END OF struct, 
  itab2 TYPE STANDARD TABLE OF struct WITH EMPTY KEY. 
 
cl_demo_output=>display( 
  CORRESPONDING itab2( VALUE itab1( ( 1 ) ( 2 ) ( 3 ) ) 
                       MAPPING col1 = table_line ) ).
```

## Executable Examples

- [Component Operator, Mapping Rule](abencorresponding_mapping_abexa.md)

- [Component Operator, Nested Mapping Rule](abencorresponding_deep_mapp_abexa.md)

## Addition 2

`... t1 = [s1] DEFAULT expr ...`

### Description

The addition `DEFAULT` allows the assignment of values for a target component based on an [expression](../../abap-glossary/abenexpression_glosry.md) `expr`. The expression is evaluated before the `CORRESPONDING` expression.

``` abap
... MAPPING a1 = a2 
            b1 = DEFAULT expr1 
            c1 = DEFAULT expr2 ...
```

On the right-hand side of the assignment, `DEFAULT` can be preceded by the source component. In this case, the source component's value is assigned to the left-hand side only if the source component is not initial. If it is initial, the value of the expression `expr` following the `DEFAULT` addition is assigned.

``` abap
... MAPPING a1 = a2 
            b1 = b2 DEFAULT expr1 
            c1 = c2 DEFAULT expr2 ...
```

### Executable Example

[`CORRESPONDING` Operator Using the Additions `MAPPING` and `DEFAULT`](abencorresp_mapping_default_abexa.md)

## Addition 3

`... EXCEPT {t1 t2 ...}|*`

### Description

Behind `EXCEPT`, components `t1`, `t2`, ... of the target structure or target table that are not listed in a preceding mapping relationship or an asterisk, `*`, can be specified:

- If explicit components `t1`, `t2`, ... are listed, these components of the result are not assigned content and remain initial.

- If an asterisk, `*`, is specified, all components of the result remain initial that are not specified explicitly in a preceding mapping relationship.

Access to subcomponents of components of the target object using the structure component selector is also not allowed in the list behind `EXCEPT` either.

If components of the target structure are included using [`INCLUDE TYPE|STRUCTURE`](../abap-declarations/abapinclude_type.md) and these components are assigned a name using [`AS`](../abap-declarations/abapinclude_type.md), this name can be specified behind `EXCEPT`. In that case, all the components of the included structure are handled as if they had been specified explicitly in the `EXCEPT` list and are not assigned content.

### Hints

- If there are identically named components in the source and target object that are not compatible or convertible, they can be excluded from the assignment using `EXCEPT`. This avoids syntax errors or runtime errors.

- If `EXCEPT *` is specified without preceding mapping relationships, all components of the result remain initial.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Effect of the addition `EXCEPT`. In `struct3`, the components `col2` and `col3` remain initial.

``` abap
DATA: 
  BEGIN OF struct1, 
    col1 TYPE string VALUE `COL1`, 
    col2 TYPE string VALUE `COL2`, 
    col3 TYPE string VALUE `COL3`, 
    col4 TYPE string VALUE `COL4`, 
  END OF struct1, 
  BEGIN OF struct2, 
    col4 TYPE string, 
    col3 TYPE string, 
    col2 TYPE string, 
    col1 TYPE string, 
  END OF struct2, 
  struct3 LIKE struct2. 
 
 struct2 = CORRESPONDING #( struct1 ). 
 struct3 = CORRESPONDING #( struct1 EXCEPT col2 col3 ) 
           ##OPERATOR[STRUCT1]. 
 
  cl_demo_output=>new( 
    )->write(   struct1 
    )->write(   struct2 
    )->display( struct3 ).
```

## Executable Examples

- [Component Operator, Mapping Rule](abencorresponding_mapping_abexa.md)

- [Component Operator, Nested Mapping Rule](abencorresponding_deep_mapp_abexa.md)
