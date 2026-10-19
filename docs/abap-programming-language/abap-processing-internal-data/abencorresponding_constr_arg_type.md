---
title: "CORRESPONDING, Basic Form"
source_file: abencorresponding_constr_arg_type.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > CORRESPONDING, Component Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CORRESPONDING, Basic Form

## Syntax

``` abap
... { CORRESPONDING {dtype|#}( [EXACT] [DEEP] 
                               struct|{itab [duplicates]} ) } 
  | { CORRESPONDING {dtype|#}( [DEEP] 
                               [[APPENDING] BASE ( base )] 
                               struct|{itab [duplicates]} ) } 
  | { CORRESPONDING {dtype|#}( [[APPENDING] BASE ( base )] 
                               struct|{itab [duplicates]} 
                               mapping ) } ...  
```

[`duplicates`](abencorresponding_constr_dupl.md) · [`duplicates`](abencorresponding_constr_dupl.md) · [`duplicates`](abencorresponding_constr_dupl.md) · [`mapping`](abencorresponding_constr_mapping.md)

### Addition

[1. `... EXACT ...`](abencorresponding_constr_arg_type.md#addition-1)

[2. `... DEEP ...`](abencorresponding_constr_arg_type.md#addition-2)

[3. `... BASE ( base ) ...`](abencorresponding_constr_arg_type.md#addition-3)

[4. `... APPENDING ( base )`](abencorresponding_constr_arg_type.md#addition-4)

[5. `... DEEP APPENDING ( base )`](abencorresponding_constr_arg_type.md#addition-5)

## Overview

### Description

This variant of the component operator [`CORRESPONDING`](abenconstructor_expr_corresponding.md) constructs a result with the target type specified using `dtype` or `#` from the components of a parameter `struct` or `itab`. `struct` and `itab` are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md).

- If the target type is a structured type, a structure `struct` must be used as a parameter. The expression creates a structure of the target type. The target structure is either initial or is assigned the value of `base` after the optional addition `BASE` as a start value. The target structure is then by default assigned the identically named components of `struct` in accordance with the rules of [`MOVE-CORRESPONDING` for structures](abapmove-corresponding.md).

- If the target type is a table type, an internal table `itab` must be used as a parameter. The expression creates an internal table of the target type. The target table is either initial or is assigned the value of `base` after the optional addition `BASE` as a start value. The target table is then by default assigned the identically named columns of `itab` in accordance with the rules of [`MOVE-CORRESPONDING` for internal tables](abapmove-corresponding.md) using the addition `KEEPING TARGET LINES`. Here, the addition [`duplicates`](abencorresponding_constr_dupl.md) can be used to control the behavior with respect to duplicate lines occurring in a target table with unique table keys.

### Hints

- An assignment of structures

  `struct2 = CORRESPONDING #( struct1 ).` without the addition `BASE` is not the same as an assignment `MOVE-CORRESPONDING struct1 TO struct2.` In `MOVE-CORRESPONDING`, all not identically named components in `struct2` keep their value. When the result of the constructor expression is assigned, however, they are assigned the value from there, which is initial for ignored components. This behavior can be overridden using the addition `BASE`.

- In the case of an assignment of a parameter to the target type and its assignment to a data object

  `dobj = CORRESPONDING type( ... ).` the target object is used directly for optimization reasons and then assigned. A temporary version of the expression is not created. This is not possible when the target object and parameter are identical, and a mapping rule is used, which enables, for example, the swapping of the content of two components. In cases like this, a temporary copy of the target object must be created, which is then used and a corresponding syntax warning is produced. This warning can be hidden using a pragma. If this is not detected until runtime, the information needed to create the necessary temporary copy of the target object is missing and the runtime error `CORRESPONDING_SELF` occurs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of four identically named components of standard table `spfli_tab` to a temporarily sorted table of type `flights` in an operand position.

``` abap
TYPES: 
  BEGIN OF flight, 
    carrid   TYPE spfli-carrid, 
    connid   TYPE spfli-connid, 
    cityfrom TYPE spfli-cityfrom, 
    cityto   TYPE spfli-cityto, 
  END OF flight. 
TYPES 
  flights TYPE SORTED TABLE OF flight WITH UNIQUE KEY carrid connid. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @FINAL(spfli_tab). 
 
cl_demo_output=>display( CORRESPONDING flights( spfli_tab ) ).
```

## Addition 1

`... EXACT ...`

### Description

If the addition `EXACT` is specified for a structure `struct`, the assignment is made as with the addition [`EXACT`](abapmove-corresponding.md) of the statement `MOVE-CORRESPONDING` for structures. If the addition `EXACT` is specified for an internal table `itab`, the assignment is made in accordance with the rules outlined for the statement [`MOVE-CORRESPONDING` for internal tables](abapmove-corresponding.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of results of the component operator without and with addition `EXACT` to existing structures of the same content. The example with `EXACT` demonstrates that, if an exception is raised, all components are assigned up to the component that raised the exception. This component, and all following components, are not assigned.

``` abap
DATA: 
  BEGIN OF src, 
    a TYPE string VALUE `AAA`, 
    b TYPE string VALUE `BBB`, 
    c TYPE string VALUE `CCC`, 
  END OF src, 
  BEGIN OF target1, 
    a TYPE string, 
    b TYPE c LENGTH 1, 
    c TYPE string, 
    d TYPE i, 
  END OF target1. 
DATA(target2) = target1. 
target1 = CORRESPONDING #( src ). 
 
TRY. 
    target2 = CORRESPONDING #( EXACT src ). 
  CATCH cx_root INTO FINAL(error). 
ENDTRY. 
 
cl_demo_output=>new( )->write( target1 )->display( target2 ).
```

## Addition 2

`... DEEP ...`

### Description

If the addition `DEEP` is specified, the assignment is made as with the addition [`EXPANDING NESTED TABLES`](abapmove-corresponding.md) of the statement `MOVE-CORRESPONDING`. A mapping rule [`mapping`](abencorresponding_constr_mapping.md) can be used to override the matching name assignment rule of `MOVE-CORRESPONDING`. If a mapping rule is specified, the addition `DEEP` is set implicitly and cannot be specified explicitly.

### Hint

If the additions [`EXACT`](abencorresponding_constr_arg_type.md) and `DEEP` are specified, the order of the additions is irrelevant, i. e. both `... EXACT DEEP ...` and `... DEEP EXACT ...` are possible. Furthermore, the only syntax option using both `DEEP` and `EXACT` with more additions is `DISCARDING DUPLICATES`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of results of the component operator with the additions `DEEP` and `EXACT DEEP` to existing [deep structures](../../abap-glossary/abendeep_structure_glosry.md) of the same content.

``` abap
DATA: 
  BEGIN OF struc1, 
    a TYPE string, 
    b TYPE string, 
    c TYPE i, 
  END OF struc1, 
  BEGIN OF struc2, 
    a TYPE string, 
    b TYPE c LENGTH 1, 
    c TYPE i, 
  END OF struc2, 
  BEGIN OF str_deep1, 
    comp TYPE string VALUE `ZZZ`, 
    itab LIKE TABLE OF struc1 WITH EMPTY KEY, 
  END OF str_deep1, 
  BEGIN OF str_deep2, 
    comp TYPE string, 
    itab LIKE TABLE OF struc2 WITH EMPTY KEY, 
  END OF str_deep2. 
 
str_deep1-itab = VALUE #( ( a = `AAA` b = `BBB` c = 111  ) ). 
DATA(str_deep3) = str_deep2. 
 
str_deep2 = CORRESPONDING #( DEEP str_deep1 ). 
 
TRY. 
    str_deep3 = CORRESPONDING #( EXACT DEEP str_deep1 ). 
  CATCH cx_root INTO FINAL(error). 
ENDTRY. 
 
cl_demo_output=>new( )->write( str_deep2 )->display( str_deep3 ).
```

## Addition 3

`... BASE ( base ) ...`

### Description

The addition `BASE` can be used to specify a start value `base` for the created structure or internal table. `base` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md) in which a database convertible to the target type can be specified.

If the addition `BASE` is specified, the value of `base` is assigned to the target structure or target table in accordance with the general [assignment rules](abenconversion_rules.md) before the remainder of the expression is evaluated. Here, the addition [`duplicates`](abencorresponding_constr_dupl.md) after `itab` can be used to affect the behavior with respect to duplicate lines occurring in a target table.

### Hints

- Unlike the operators `NEW` and `VALUE`, parentheses must be set around `base` in `CORRESPONDING`.

- Unlike the operators `NEW` and `VALUE`, the data type of `base` is not used in `CORRESPONDING` to determine a result type specified using `#`.

- The addition `BASE` can be used with the component operator to replace the statement [`MOVE-CORRESPONDING`](abapmove-corresponding.md) as follows:

  - An assignment of structures

    `struct2 = CORRESPONDING #( BASE ( struct2 ) struct1 ).`

is the same as an assignment

`MOVE-CORRESPONDING struct1 TO struct2.` - An assignment of internal tables

`itab2 = CORRESPONDING #( BASE ( itab2 ) itab1 ).`

is the same as an assignment

`MOVE-CORRESPONDING itab1 TO itab2 KEEPING TARGET LINES.`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of results of the component operator without and with addition `BASE` to existing structures of the same content. The value of the component that does not exist in the source structure is only preserved if `BASE` is used.

``` abap
DATA: 
  BEGIN OF src, 
    a TYPE i VALUE 1, 
    b TYPE i VALUE 2, 
  END OF src, 
  BEGIN OF target1, 
    b TYPE i VALUE 11, 
    c TYPE i VALUE 12, 
  END OF target1. 
DATA(target2) = target1. 
 
target1 = CORRESPONDING #( src ). 
target2 = CORRESPONDING #( BASE ( target2 ) src ). 
 
cl_demo_output=>new( )->write( target1 )->display( target2 ).
```

## Addition 4

`... APPENDING ( base ) ...`

### Description

This addition affects two identically named deep components that are both internal tables. It ensures that the nested target tables are not deleted. Furthermore, it appends the lines of the nested source tables. The value assignment applied to the added lines is performed in the same way as using the `CORRESPONDING` operator without addition.

**Note:** The entire table bodies of the nested source tables are assigned in accordance with the [conversion rules for internal tables](abenconversion_itab.md).

### Hint

The addition `APPENDING` appends the lines of a nested table and keeps the original lines. The explicit specification of the addition `BASE` is possible here but not necessary. That means, the following syntax has the same effect:

``` abap
struc2 = CORRESPONDING #( APPENDING ( struc2 ) struc1 ). 
struc2 = CORRESPONDING #( APPENDING BASE ( struc2 ) struc1 ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_CRRSPNDNG_VARIANTS_ST` demonstrates the variant with deep structures containing internal tables as components.

deep_struc2 = CORRESPONDING \#( APPENDING ( deep_struc2 ) deep_struc1 ).

## Addition 5

`... DEEP APPENDING ( base ) ...`

### Description

This combination affects two identically named components that are both internal tables. It ensures that the nested target tables are not deleted. Furthermore, it appends the lines of the nested source tables. The value assignment applied to the added lines is performed in the same way as using the `CORRESPONDING` operator with the addition `DEEP`. That is, the value assignment is only carried out for identically named components in the nested table.

### Hint

The addition `APPENDING` appends the lines of a nested table and keeps the original lines. The explicit specification of the addition `BASE` is possible here but not necessary. That means, the following syntax has the same effect:

``` abap
struc2 = CORRESPONDING #( DEEP APPENDING ( struc2 ) struc1 ). 
struc2 = CORRESPONDING #( DEEP APPENDING BASE ( struc2 ) struc1 ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_CRRSPNDNG_VARIANTS_ST` demonstrates the variant with deep structures containing internal tables as components.

deep_struc2 = CORRESPONDING \#( DEEP APPENDING ( deep_struc2 ) deep_struc1 ).

## Executable Examples

- [Component Operator for Structures](abencorresponding_struct_abexa.md)

- [Component Operator for Internal Tables](abencorresponding_itab_abexa.md)

- [Component Operator for Table Expression](abencorresponding_table_exp_abexa.md)

- [Variants of `MOVE-CORRESPONDING` and the `CORRESPONDING` operator using deep structures](abencorresponding_variants_s_abexa.md)
