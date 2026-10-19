---
title: "NEW, Internal Tables"
source_file: abennew_constructor_params_itab.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > NEW, Instance Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# NEW, Internal Tables

## Syntax

``` abap
... NEW dtype|#( [let_exp] 
                 [BASE itab] 
                 [FOR for_exp1 
                  FOR for_exp2 
                  ... ] 
                 ( line_spec1 ) 
                 ( line_spec2 ) 
                   ... ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md) · [`FOR for_exp1`](../abap-program-flow-logic/abenfor.md) · [`FOR for_exp2`](../abap-program-flow-logic/abenfor.md) · [`line_spec1`](abennew_constructor_params_lspc.md) · [`line_spec2`](abennew_constructor_params_lspc.md)

### Addition

[1. `... BASE itab`](abennew_constructor_params_itab.md#addition-1)

[2. `... FOR for_exp`](abennew_constructor_params_itab.md#addition-2)

## Overview

### Description

If `dtype` is a tabular data type or `#` stands for such a type, the table lines of the constructed table are created as follows:

- The first option is to list a `LET` expression [`let_exp`](../abap-declarations/abaplet.md) to define local helper fields whose values can be used to construct the table lines.

- An optional start value for the content can then be specified for the content of the internal table after `BASE` (see below).

- One or more optional consecutive [iteration expressions](../../abap-glossary/abeniteration_expression_glosry.md) can then be specified using [`FOR`](../abap-program-flow-logic/abenfor.md) (see below).

- The table lines are then constructed in one or more sets of internal parentheses by specifying [`line_spec`](abennew_constructor_params_lspc.md). Each set of inner parentheses constructs one or more lines in accordance with the information in `line_spec` and inserts them into the new internal table according to the rules for the statement [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md) ... [`INTO TABLE`](../abap-processing-internal-data/abapinsert_itab_position.md). The object is inserted in the order of the parentheses.

The constructed lines must meet the requirements of the statement [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md) for inserting work areas using table keys and therefore be compatible with the line type, with one exception: when constructing a [standard table](../../abap-glossary/abenstandard_table_glosry.md) where the lines are only appended anyway, the value can be shorter than the line length for line types `c` and `x` and then padded on the right with blanks or hexadecimal 0.

### Hints

- When a constructor expression is assigned to a reference variable using `NEW`, the original reference is available in the entire expression in the target variable. The target variable is not overwritten until the expression is completed. In the case of the value operator [`VALUE`](abenvalue_constructor_params_itab.md), however, the target variable can only be assigned to a helper variable using `LET` and is then no longer available.

- The operand type for [`line_spec`](abennew_constructor_params_lspc.md) in the inner parentheses is the line type of the table type specified using `dtype` or `#` and is always uniquely identifiable. Constructor expressions at this position can therefore always derive the required data type using `#`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an anonymous internal table with a structured line type with substructures and tabular components.

``` abap
TYPES: BEGIN OF t_struct1, 
         col1 TYPE i, 
         col2 TYPE i, 
       END OF t_struct1, 
       BEGIN OF t_struct2, 
         col1 TYPE i, 
         col2 TYPE t_struct1, 
         col3 TYPE TABLE OF t_struct1 WITH EMPTY KEY, 
       END OF t_struct2, 
       t_itab TYPE TABLE OF t_struct2 WITH EMPTY KEY. 
 
DATA dref TYPE REF TO data. 
 
dref = NEW t_itab( ( col1 = 1 
                     col2-col1 = 1 
                     col2-col2 = 2 
                     col3 = VALUE #( ( col1 = 1 col2 = 2 ) 
                                     ( col1 = 3 col2 = 4 ) ) ) 
                   ( col1 = 2 
                     col2-col1 = 2 
                     col2-col2 = 4 
                     col3 = VALUE #( ( col1 = 2 col2 = 4 ) 
                                     ( col1 = 6 col2 = 8 ) ) ) ).
```

## Addition 1

`... BASE itab`

### Description

An addition, `BASE`, followed by an internal table, `itab`, can be specified in front of the specification of lines to be inserted. `itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The line type of `itab` must be convertible to the line type of the return value. If `BASE` is specified, the content of `itab` is assigned to the return value before the individual lines are inserted. If the character `#` is specified for the type of the return value and the type cannot be determined from the operand position of the constructor expression, the type of `itab` is used for this expression if it is known.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of three anonymous internal tables with an elementary line type. The first table is filled with three lines, whereby the second inserted line is initial. The second and third tables are filled with the lines of the first table and three further lines. Using `BASE` and [`LINES OF`](abennew_constructor_params_lspc.md) has the same effect here.

``` abap
TYPES t_itab TYPE TABLE OF i WITH EMPTY KEY. 
 
FINAL(dref1) = NEW t_itab( ( 1 ) (  ) ( 3 ) ). 
 
FINAL(dref2) = NEW t_itab( BASE dref1->* 
                          (   ) ( 5 ) (  ) ). 
 
FINAL(dref3) = NEW t_itab( ( LINES OF dref1->* ) 
                          (   ) ( 5 ) (  ) ). 
 
cl_demo_output=>write(   dref1->* ). 
cl_demo_output=>write(   dref2->* ). 
cl_demo_output=>display( dref3->* ).
```

## Addition 2

`... FOR for_exp`

### Description

If one or more [iteration expressions](../../abap-glossary/abeniteration_expression_glosry.md) are specified consecutively using [`FOR`](../abap-program-flow-logic/abenfor.md), the lines constructed in [`line_spec`](abennew_constructor_params_lspc.md) for each iteration of the last `FOR` expression are inserted into the target table. When constructing table lines in [`line_spec`](abennew_constructor_params_lspc.md), the visible local work areas and field symbols of the iteration expressions can be used to construct table lines.

- If [conditional iterations](../abap-program-flow-logic/abenfor_conditional.md) are used, the new table lines are created in freely definable iteration steps.

- If [table iterations](../abap-processing-internal-data/abenfor_itab.md) are used, the lines of existing internal tables are evaluated. In this case, these are known as [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md), since new table lines are constructed from the lines of existing internal tables.

### Hints

- The term *table comprehension* is derived from similar concepts used in many other languages, where it is also referred to as *list comprehension*.

- Conditional iterations and table comprehensions are also possible with [`FOR` expressions](../abap-processing-internal-data/abenmesh_for.md) for [mesh paths](../../abap-glossary/abenmesh_path_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an anonymous internal table with an elementary line type and filling it with square numbers using an iteration expression.

``` abap
TYPES t_itab TYPE TABLE OF i WITH EMPTY KEY. 
 
FINAL(dref) = NEW t_itab( FOR i = 1 UNTIL i > 10 
                         ( ipow( base = i exp = 2 ) ) ). 
 
cl_demo_output=>display( dref->* ).
```

## Executable Examples

[Examples of Table Comprehensions](../abap-processing-internal-data/abentable_comprehensions_abexas.md)
