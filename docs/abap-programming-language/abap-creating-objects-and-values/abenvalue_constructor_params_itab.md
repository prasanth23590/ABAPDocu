---
title: "VALUE, Internal Tables"
source_file: abenvalue_constructor_params_itab.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > VALUE, Value Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# VALUE, Internal Tables

## Syntax

``` abap
... VALUE dtype|#( [let_exp] 
                   [BASE itab] 
                   [FOR for_exp1 
                    FOR for_exp2 
                    ... ] 
                   ( line_spec1 ) 
                   ( line_spec2 ) 
                     ... ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md) · [`FOR for_exp1`](../abap-program-flow-logic/abenfor.md) · [`FOR for_exp2`](../abap-program-flow-logic/abenfor.md) · [`line_spec1`](abenvalue_constructor_params_lspc.md) · [`line_spec2`](abenvalue_constructor_params_lspc.md)

### Addition

[1. `... BASE itab`](abenvalue_constructor_params_itab.md#addition-1)

[2. `... FOR for_exp`](abenvalue_constructor_params_itab.md#addition-2)

## Overview

### Description

If `dtype` is a tabular data type or `#` stands for such a type, the table lines of the constructed table are created as follows:

- The first option is to list a `LET` expression [`let_exp`](../abap-declarations/abaplet.md) to define local helper fields whose values can be used to construct the table lines.

- An optional start value for the content can then be specified for the content of the internal table after `BASE` (see below).

- One or more optional consecutive [iteration expressions](../../abap-glossary/abeniteration_expression_glosry.md) can then be specified using [`FOR`](../abap-program-flow-logic/abenfor.md) (see below).

- The table lines are then constructed in one or more sets of internal parentheses by specifying [`line_spec`](abenvalue_constructor_params_lspc.md). Each set of inner parentheses constructs one or more lines in accordance with the information in `line_spec` and inserts them into the created internal table in accordance with the rules for the statement [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md) ... [`INTO TABLE`](../abap-processing-internal-data/abapinsert_itab_position.md), with one difference: Any conflicts with an existing unique primary table key raise an exception of the class `CX_SY_ITAB_DUPLICATE_KEY`. The object is inserted in the order of the parentheses.

The constructed lines must meet the requirements of the statement [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md) for inserting work areas using table keys and therefore be compatible with the line type, with one exception: when constructing a [standard table](../../abap-glossary/abenstandard_table_glosry.md) where the lines are only appended anyway, the value can be shorter than the line length for line types `c` and `x` and then padded on the right with blanks or hexadecimal 0.

If the `VALUE` operator is used as the source of an assignment to an internal table, it is first initialized after the evaluation of a possible [`LET`](../abap-declarations/abaplet.md) expression or is assigned the content of `itab`. Then, [`line_spec`](abenvalue_constructor_params_lspc.md) data is then evaluated and inserted directly into the target table.

### Hints

- In assignments of constructor expressions to an internal table, its existing lines cannot be used directly as an operand in [`line_spec`](abenvalue_constructor_params_lspc.md). This is because this table is deleted before `line_spec` is evaluated or overwritten by the content of `itab`. If the entire internal table or lines from the left side are needed on the right side, however, they can be saved in local helper variables using a [`LET`](../abap-declarations/abaplet.md) expression, since this expression is evaluated first.

- The operand type for [`line_spec`](abenvalue_constructor_params_lspc.md) in the inner parentheses is the line type of the table type specified using `dtype` or `#`, which means it is always uniquely identifiable. Constructor expressions at this position can therefore always derive the required data type using `#`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an internal table with a structured line type and filling it with two lines. The structures are filled with values component by component.

``` abap
TYPES: BEGIN OF t_struct, 
         col1 TYPE i, 
         col2 TYPE i, 
       END OF t_struct, 
       t_itab TYPE TABLE OF t_struct WITH EMPTY KEY. 
 
DATA itab TYPE t_itab. 
 
itab = VALUE #( ( col1 = 1 col2 = 2 ) 
                ( col1 = 3 col2 = 4 ) ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an internal table with a tabular line type and filling it with two lines. The first line is assigned a table that is already filled. The second line is constructed using `VALUE`.

``` abap
TYPES: t_itab1 TYPE TABLE OF i       WITH EMPTY KEY, 
       t_itab2 TYPE TABLE OF t_itab1 WITH EMPTY KEY. 
 
DATA itab1 TYPE t_itab1. 
DATA itab2 TYPE t_itab2. 
 
itab1 = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
itab2 = VALUE #( ( itab1 ) 
                 ( VALUE t_itab1( ( 4 ) ( 5 ) ( 6 ) ) ) ).
```

## Executable Examples

- [`VALUE` - Operator for Internal Tables](abenvalue_itab_abexa.md)

- [`VALUE` Operator with `LET` for Internal Tables](abenvalue_itab_let_abexa.md)

## Addition 1

`... BASE itab`

### Description

An addition, `BASE`, followed by an internal table, `itab`, can be specified in front of the specification of lines to be inserted. `itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The line type of `itab` must be convertible to the line type of the return value. If `BASE` is specified, the content of `itab` is assigned to the return value before the individual lines are inserted. If the character `#` is specified for the type of the return value and the type cannot be determined from the operand position of the constructor expression, the type of `itab` is used for this expression if it is known.

### Hints

- Without the addition `BASE`, the content of tables can only be newly constructed using the value operator, but not extended. If the same table is specified after `BASE` to which the constructor expression is assigned, further lines can be inserted in this table.

- If the target table is specified as `itab` after `BASE` in an assignment to an existing internal table, there is no assignment before [`line_spec`](abenvalue_constructor_params_lspc.md) is evaluated, but the target table simply keeps its value instead.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of `BASE`. The table type of `base1` or `base2` is transferred in the construction of `tab1` and `tab2`. This is not possible in the construction of `tab3` since the line type of `base2` is not structured and hence does not match the specification of individual components in the following parentheses. The type `itab2` is specified explicitly for `tab3`. This is possible since the line type of `base2` can be converted into this line type. Since sorted tables are constructed, the lines in the results are also sorted.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  itab1 TYPE SORTED TABLE OF string WITH UNIQUE KEY table_line, 
  BEGIN OF struct, 
    col1 TYPE c LENGTH 2, 
    col2 TYPE c LENGTH 2, 
    col3 TYPE c LENGTH 2, 
  END OF struct, 
  itab2 TYPE SORTED TABLE OF struct WITH UNIQUE KEY col1 col2 col3. 
 
FINAL(base1) = VALUE itab1( 
                ( `x1y1z1` ) 
                ( `x2y2z2` ) 
                ( `x3y3z3` ) ). 
FINAL(base2) = VALUE itab2( 
                ( col1 = 'x1' col2 = 'y1' col3 = 'z1' ) 
                ( col1 = 'x2' col2 = 'y2' col3 = 'z2' ) 
                ( col1 = 'x3' col2 = 'y3' col3 = 'z3' ) ). 
 
FINAL(tab1) = VALUE #( BASE base1 
               ( `A1B1B1` ) 
               ( `A2B2B2` ) ). 
 
FINAL(tab2)  = VALUE #( 
                BASE base2 
                ( col1 = 'A1' col2 = 'B1' col3 = 'C1' ) 
                ( col1 = 'A2' col2 = 'B2' col3 = 'C2' ) ). 
 
FINAL(tab3) = VALUE itab2( BASE base1 
               ( col1 = 'A1' col2 = 'B1' col3 = 'C1' ) 
               ( col1 = 'A2' col2 = 'B2' col3 = 'C2' ) ). 
 
out->write( tab1  ). 
out->write( tab2 ). 
out->write( tab3 ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of `BASE` to append lines to existing lines in an internal table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES itab TYPE TABLE OF string WITH EMPTY KEY. 
 
DATA(itab) = 
  VALUE itab( 
    ( `a` ) ( `b` ) ( `c` ) ). 
 
... 
 
itab = 
  VALUE #( 
    BASE itab 
    ( `d` ) ( `e` ) ( `f` ) ). 
 
out->write( itab ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of `BASE` to append lines to an internal table in a loop. After the output, it is shown how the same function can be applied using an iteration expression with [`FOR`](../abap-program-flow-logic/abenfor_conditional.md).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
 
DO 10 TIMES. 
  itab = VALUE #( BASE itab ( ipow( base = sy-index exp = 2 ) ) ). 
ENDDO. 
 
out->write( itab ). 
 
DATA jtab LIKE itab. 
jtab = VALUE #( FOR j = 1 UNTIL j > 10 
                ( ipow( base = j exp = 2 ) ) ). 
ASSERT jtab = itab. 
 
out->display( ).
```

### Executable Example

[`VALUE` - Addition `BASE` for Internal Tables](abenvalue_itab_base_abexa.md)

## Addition 2

`... FOR for_exp`

### Description

The specification of one or more consecutive [iteration expressions](../../abap-glossary/abeniteration_expression_glosry.md) using [`FOR`](../abap-program-flow-logic/abenfor.md), this means that the lines constructed in [`line_spec`](abenvalue_constructor_params_lspc.md) for each iteration of the last `FOR` expression are inserted into the target table. When constructing table lines in [`line_spec`](abenvalue_constructor_params_lspc.md), the visible local work areas and field symbols of the iteration expressions can be used to construct the table lines.

- If [conditional iterations](../abap-program-flow-logic/abenfor_conditional.md) are used, the new table lines are created in freely definable iteration steps.

- If [table iterations](../abap-processing-internal-data/abenfor_itab.md) are used, the lines of existing internal tables are evaluated. In this case, these are known as [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md), since new table lines are constructed from the lines of existing internal tables.

### Hints

- The term *table comprehension* is derived from similar concepts used in many other languages, where it is also referred to as *list comprehension*.

- Conditional iterations and table comprehensions are also possible with [`FOR` expressions](../abap-processing-internal-data/abenmesh_for.md) for [mesh paths](../../abap-glossary/abenmesh_path_glosry.md).

- For tasks that can be solved using both table comprehensions and [special assignments](../abap-processing-internal-data/abencorresponding.md) for components, in particular the component operator [`CORRESPONDING`](../abap-processing-internal-data/abenconstructor_expr_corresponding.md), it is best to use assignments (see the [executable example](../abap-processing-internal-data/abencorresponding_vs_for_abexa.md)).

- If the `VALUE` operator is used, it should be noted that assignments to internal tables are also initialized or assigned the content of `itab` after `BASE` even in the case of table comprehensions after the evaluation of a [`LET`](../abap-declarations/abaplet.md) expressions and the target table is then used directly. The original table can therefore not be used directly in the `FOR` expressions, unless it is assigned to a helper variable after `LET`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of a temporary internal table with an elementary line type and filling it with square numbers using an iteration expression.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES t_itab TYPE TABLE OF i WITH EMPTY KEY. 
 
out->write( 
  VALUE t_itab( FOR i = 1 UNTIL i > 10 
                ( ipow( base = i exp = 2 ) ) ) ). 
 
out->display( ).
```

## Executable Examples

- [Examples of Table Comprehensions](../abap-processing-internal-data/abentable_comprehensions_abexas.md)
