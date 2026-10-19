---
title: "CORRESPONDING, Lookup Table"
source_file: abencorresponding_constr_using.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > CORRESPONDING, Component Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CORRESPONDING, Lookup Table

## Syntax

``` abap
... CORRESPONDING dtype|#( itab FROM lookup_tab 
                                USING [KEY key_name] s1 = t1 s2 = t2 ... 
                                [mapping]  ) ...  
```

[`mapping`](abencorresponding_constr_mapping.md)

## Description

This variant of the component operator [`CORRESPONDING`](abenconstructor_expr_corresponding.md) can only be used for internal tables. The expression constructs an internal table from the components of the internal table `itab` and a lookup table `lookup_tab`. The lines of the internal table result from a comparison of `itab` and `lookup_tab`. The target type specified using `dtype` or `#` must be a table type. The parameters `itab` and `lookup_tab` expect internal tables whose line type must be structured. In addition, `itab` must be convertible to the target type. `itab` and `lookup_tab` are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md).

The result of the expression is created in the following steps:

- First, an interim result of the type of the internal table `itab` is constructed as follows: For each line in `itab`, the lookup table `lookup_tab` searches for a line that has the same content in the columns `s1`, `s2`, ... as the columns `t1`, `t2`, ... of the line in `itab`. The search must be performed using a sorted table key or a hash key (see below). If the key is not unique, the first line found is used.

  - If no line like this is found, a line with the unchanged content of the line in `itab` is inserted into the interim result.

  - If such a line is found, a line is inserted into the interim result that is the result of an assignment of the line found in `itab` to the current line in `lookup_tab`. By default, the assignment is made in accordance with the rules of [`MOVE-CORRESPONDING` for structures](abapmove-corresponding.md) with the addition `EXPANDING NESTED TABLES`, with the exception that the components used for searches are not assigned by default: The components `s1`, `s2`, ... of `lookup_tab` used for the search are by default not assigned to the identically named components of `itab` and the components `t1`, `t2`, ... of `itab` used for searches are not assigned the identically named components of `lookup_tab`.

- The interim result of the type of the table `itab` is assigned to the result of the expression in accordance with the regular [assignment rules](abenconversion_rules.md) for internal tables and, if necessary, converted to the target type.

This means that the component by component assignment takes place between the lookup table `lookup_tab` as the source table and an interim result with the type of `itab` as the target table. A mapping rule [`mapping`](abencorresponding_constr_mapping.md) can be used to override the default assignment of identically named components and the default exclusion of the components `s1`, `s2`, ... and `t1`, `t2`, ... The same internal table can only be specified for `itab` and `lookup_tab` if this is known statically. If it is only known at runtime, the expression cannot be evaluated and the runtime error `CORRESPONDING_SELF` occurs.

The search for the line in `lookup_tab` must take place using a sorted table key or a hash key:

- If the addition `KEY` is not specified, a sorted table or a hashed table must be specified for `lookup_tab`.

- If the addition `KEY` is specified, the key `key_name` specified after it is used. The following can be specified for `key_name`:

  - A [secondary key](../../abap-glossary/abensecondary_key_glosry.md) using its name

  - The primary key using its predefined name `primary_key` or an alias. If the primary key is specified, `lookup_tab` must be a sorted table or a hashed table.

The comparison fields `s1`, `s2`, ... must completely cover the used table key.

## Hints

- Unlike the [basic form](abencorresponding_constr_arg_type.md), this variant does not have the addition `DEEP`. Instead, it always behaves as if `DEEP` were specified. The addition `BASE` cannot be specified either.

- Generally, the type of `itab` and the target type should be identical.

- In a common use case, an existing internal table `itab` is enriched with information from the lookup table `lookup_tab`. Here, the constructor expression is assigned to the same internal table as specified for `itab`. In this case, the expression is optimized internally to work directly with `itab` without creating an interim result.

- If the constructor expression is not assigned to the internal table specified for `itab` or if this table is not known statically, the temporary interim result with the type `itab` must be created completely. This produces a syntax check warning that can be hidden by a pragma.

- If the same table is specified for `itab` and `lookup_tab`, a temporary copy of the table must be created as a target table of the assignment. If this is detected by the syntax check, a warning occurs that can be hidden by a pragma. If this is not detected until runtime, the information needed to create the necessary temporary copy of the target object is missing and runtime error `CORRESPONDING_SELF` occurs.

- The variant should not be used with the addition `EXACT` which produces a syntax warning.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Lines of internal table `itab1` that exist in internal table `itab2` are passed to `itab1`.

``` abap
TYPES: 
  BEGIN OF line, 
    value   TYPE i, 
    comment TYPE string, 
  END OF line, 
  itab1 type STANDARD TABLE OF line WITH EMPTY KEY, 
  itab2 TYPE HASHED TABLE OF line WITH UNIQUE KEY value. 
 
DATA(itab1) =  VALUE itab1( for i = 1 UNTIL i >= 10 ( value = i ) ). 
FINAL(itab2) = VALUE itab2( ( value = 2 comment = `...` ) 
                            ( value = 3 comment = `...` ) 
                            ( value = 5 comment = `...` ) 
                            ( value = 8 comment = `...` ) ). 
 
itab1 = CORRESPONDING itab1( itab1 FROM itab2 USING value = value ). 
 
cl_demo_output=>display( itab1 ).
```

## Executable Examples

- [Component operator, lookup table](abencorresponding_using_abexa.md)

- [Component Operator, Reflexive Assignment](abencorresponding_using_self_abexa.md)
