---
title: "READ TABLE, where_cond"
source_file: abapread_table_where.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > READ TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ TABLE, where_cond

## Syntax

``` abap
... [USING KEY keyname] WHERE log_exp|(cond_syntax) ...  
```

[`keyname`](abenkeyname.md) · [`log_exp`](../abap-program-flow-logic/abenlogexp.md)

### Variant

[1. `... WHERE log_exp`](abapread_table_where.md#variant-1)

[2. `... WHERE (cond_syntax)`](abapread_table_where.md#variant-2)

### Addition

[`... USING KEY keyname`](abapread_table_where.md#addition)

## Overview

### Description

Static or dynamic `WHERE` condition. The internal table is searched for the first line whose values match the `WHERE` condition.

## Restrictions

A `WHERE` condition cannot be used together with the following transport options:

- [`COMPARING`](abapread_table_transport_options.md)

- [`TRANSPORTING {comp1 comp2 ...}|{ALL FIELDS}`](abapread_table_transport_options.md)

**Note:** The transport option [`TRANSPORTING NO FIELDS`](abapread_table_transport_options.md) can be used together with a `WHERE` condition.

### Hints

- When a `WHERE` condition is used, `sy-subrc` can have the values 0 and 4 only.

- The statement

  `READ TABLE itab ... [USING KEY ...] WHERE log_exp|(cond_syntax).` works almost exactly in the same way as [`LOOP AT itab`](abaploop_at_itab.md) ... [`[USING KEY ...] WHERE log_exp|(cond_syntax)`](abaploop_at_itab_cond.md). [`EXIT`](../abap-calling-and-exiting-program-units/abapexit_loop.md). [`ENDLOOP`](abapendloop.md). There is a difference between the above `LOOP` pattern and the `READ` statement regarding `sy-tabix`:

  - If a table key connected to a table index is used, `sy-tabix` is set to the current line in that index and to *0* for a hash key behind the `LOOP` statement but not behind the `ENDLOOP` statement. If the line number is needed after the loop, a helper variable must be used.

  - After `READ`, `sy-tabix` is set to the line number in an table index or *0* for a hash key if a line is found.

    **Note:** There is no performance gain in using `READ WHERE` versus `LOOP WHERE`. `READ WHERE` simply provides an easier to use syntax.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `READ` statement determines the first line of an internal table where the flight time exceeds a given value.

``` abap
DATA itab TYPE SORTED TABLE OF spfli 
          WITH UNIQUE KEY fltime carrid connid. 
 
SELECT * 
       FROM spfli 
       ORDER BY fltime, carrid, connid 
       INTO TABLE @itab. 
 
READ TABLE itab 
     TRANSPORTING NO FIELDS 
     WHERE fltime > 600. 
 
IF sy-subrc = 0. 
  FINAL(idx) = sy-tabix. 
ENDIF.
```

## Variant 1

`... WHERE log_exp`

### Description

Static `WHERE` condition. The first line is searched for which the condition after `WHERE` is met. If a static `WHERE` condition is specified, the line type of the internal table must be known statically. `WHERE` can be specified for all table categories.

A [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) [`log_exp`](../abap-program-flow-logic/abenlogexp.md) can be specified after `WHERE`, in which the first operand of each [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) is a [component](abenitab_components.md) of the internal table. The following can be specified as relational expressions:

- All [comparison expressions](../abap-program-flow-logic/abenlogexp_comp.md)

- The following [predicate expressions](../../abap-glossary/abenpredicate_expression_glosry.md):

  - [`IS [NOT] INITIAL`](../abap-program-flow-logic/abenlogexp_initial.md)

  - [`IS [NOT] BOUND`](../abap-program-flow-logic/abenlogexp_bound.md)

  - [`IS [NOT] INSTANCE OF`](../abap-program-flow-logic/abenlogexp_instance_of.md)

No other [predicates](../abap-program-flow-logic/abenpredicate.md) can be specified. The components of the internal table must be specified as individual operands and not as part of an expression. Parenthesized character-like data objects cannot be used to specify a component dynamically here. The remaining operands of a relational expression are [general expression positions](../abap-syntax-elements-of-an-abap-program/abengeneral_expression_positions.md) at which any [suitable](../abap-program-flow-logic/abenlogexp_rules.md) individual operands or [expressions](../../abap-glossary/abenexpression_glosry.md) can be specified, but no components of the internal table. The specified components can have any data type. The corresponding [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) apply to the evaluation, whereby a different [rule](../abap-program-flow-logic/abenlogexp_rules_expr_char.md) applies to a string expression on the right side than to general logical expressions.

The evaluation of the `WHERE` condition depends on the [table category](../../abap-glossary/abentable_category_glosry.md) and the [table key](../../abap-glossary/abentable_key_glosry.md) used as follows:

- When [standard tables](../../abap-glossary/abenstandard_table_glosry.md) are accessed without a secondary key specification, the search is not optimized. This means that the logical expression of the `WHERE` addition is applied to each line of the internal table that is relevant for the current statement.

- When using a [sorted key](../../abap-glossary/abensorted_key_glosry.md) or a [hash key](../../abap-glossary/abenhash_key_glosry.md), that is, when accessing a [sorted table](../../abap-glossary/abensorted_table_glosry.md), a [hashed table](../../abap-glossary/abenhashed_table_glosry.md), or a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md), the compiler tries to optimize the search as described under [Optimization of the `WHERE` Condition](abenitab_where_optimization.md). The prerequisites are:

  - The entire logical expression or a part of it can be transformed into a key access.

  - The transformable part of the logical expression has the same result as the resulting key access.

    If an optimization is not possible, the behavior is as follows:

  - If a sorted table or a hashed table is accessed using the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md), the full `WHERE` condition is applied to each line of the table that is relevant for the current statement.

  - If the table is accessed using a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md), a syntax error or an exception is raised.

### Hints

- When using a `WHERE` condition, it should be noted that the [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) for incompatible data types apply when comparing incompatible data objects. Here, the data types involved determine which operand is converted. If the additions [`WITH TABLE KEY`](abapread_table_key.md) and [`WITH KEY`](abapread_table_free.md) of the statement `READ` are used or if the corresponding [keys are specified](abentable_exp_itab_line.md) in [table expressions](abentable_expressions.md), however, the content of the specified data objects is always converted to the data type of the columns before the comparison, which can produce varying results.

- The difference between comparison rules in a `WHERE` condition and conversion rules when reading individual lines is particularly significant for [enumerated types](../../abap-glossary/abenenum_type_glosry.md) for which the comparison rules are more restrictive than conversion rules. [Conversions](abenconversion_enumerated.md) of an enumerated object to a character-like type produce a message from the extended program check.

- If possible, all operands of the logical expression should be in [compatible](../../abap-glossary/abencompatible_glosry.md) pairs, so that the [`WHERE` condition can be optimized](abenitab_where_optimization.md).

- If a comparison expression with a [ranges table](../../abap-glossary/abenranges_table_glosry.md) is specified after [`IN`](../abap-program-flow-logic/abenlogexp_select_option.md) as a logical expression, the expression for the initial table is always true and then all lines are found.

- For a `WHERE` condition that could also be expressed by [`WITH KEY`](abapread_table_free.md), the latter has a better performance. If such a `WHERE` condition is used, a syntax warning occurs that can be suppressed by the [pragma](../../abap-glossary/abenpragma_glosry.md) `##read_where_ok`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the differences in behavior of a `WHERE` condition and a key access with `WITH TABLE KEY`. In `READ WHERE`, the rule for the [comparison of character-like data types](../abap-program-flow-logic/abenlogexp_character.md) applies. The short column content *AA* is first padded with blanks to increase the length to 4 and then compared with *AAXX*. No matching line is found. Using `READ TABLE itab WITH TABLE KEY`, the content of `text_long` is [converted](abenconversion_type_c.md) to the value *AA* before the comparison, by cutting off two characters, and then compared with the column content. The read is therefore successful.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA text_short TYPE c LENGTH 2. 
DATA text_long  TYPE c LENGTH 4. 
 
DATA itab LIKE TABLE OF text_short WITH NON-UNIQUE KEY table_line. 
 
text_short = 'AA'. 
text_long  = 'AAXX'. 
 
itab = VALUE #( ( text_short ) ). 
 
READ TABLE itab INTO text_short 
          WHERE table_line = text_long ##READ_WHERE_OK. 
out->write( |READ WHERE: { sy-subrc }| ). 
 
READ TABLE itab INTO text_short 
           WITH TABLE KEY table_line = text_long. 
out->write( |READ WITH TABLE KEY: { sy-subrc }| 
  )->display( ).
```

### Executable Example

For a comparison between `WHERE` and `WITH KEY`, refer to [itab - `READ WHERE` Versus `WITH KEY`](abenread_itab_where_key_abexa.md).

## Variant 2

`... WHERE (cond_syntax)`

### Description

Dynamic `WHERE` condition. For `cond_syntax` any character-like data object or [standard table](../../abap-glossary/abenstandard_table_glosry.md) with character-like line type can be specified that, when the statement is executed and with the following exceptions, contains the syntax of a logical expression in accordance with the rules of the static `WHERE` condition or is initial. The following are not supported in a dynamic `WHERE` condition:

- [String expressions](../../abap-glossary/abenstring_expression_glosry.md) and [bit expressions](../../abap-glossary/abenbit_expression_glosry.md)

- [String functions](../../abap-glossary/abenstring_function_glosry.md)

- [Time stamp functions](../../abap-glossary/abentimestamp_function_glosry.md) with the exception of `utclong_current`

- [Constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md)

- [Table expressions](../../abap-glossary/abentable_expression_glosry.md)

The syntax in `cond_syntax` is not case-sensitive as in the static syntax. When an internal table is specified, the syntax can be distributed across multiple lines. If `cond_syntax` is initial when the statement is executed, the logical expression is true. Invalid logical expressions raise an exception from the class `CX_SY_ITAB_DYN_LOOP`.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](abenescape_functions.md).

### Hint

The dynamic `WHERE` condition is not evaluated for an empty table for optimization reasons. Therefore, if an internal table is empty, and a logical expression has errors, no exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example allows entering freely a `WHERE` condition. The first line of an internal table that matches the condition is displayed.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(where_cond) = `url NS '.com'`. 
cl_demo_input=>request( CHANGING field = where_cond ). 
 
SELECT * 
       FROM scarr 
       ORDER BY PRIMARY KEY 
       INTO TABLE @FINAL(itab). 
 
TRY. 
    READ TABLE itab INTO DATA(wa) 
                     WHERE (where_cond). 
    FINAL(idx) = sy-tabix. 
  CATCH cx_sy_itab_dyn_loop INTO FINAL(exc). 
    out->display( exc->get_text( ) ). 
    RETURN. 
ENDTRY. 
 
out->write( itab ). 
 
IF sy-subrc = 0. 
  out->write( idx )->display( wa ). 
ELSE. 
  out->display( 'Not found' ). 
ENDIF.
```

## Addition

`... USING KEY keyname`

### Description

The addition `USING KEY` can be used to specify a table key in [`keyname`](abenkeyname.md) with which the search is executed. The specified table key affects the evaluation of the `WHERE` condition as described above and the table index to which the system field `sy-tabix` is related.

Furthermore, the table key affects the order in which the table lines are accessed in the same way as for [`LOOP AT itab`](abaploop_at_itab_cond.md) and thus can affect which line is found first.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first two `READ` statements return different values for `sy-tabix` for the same `WHERE` condition. The first statement uses the primary table key and thus the primary table index. It finds the second line with the value *9* of the internal table. The second statement uses a sorted secondary table key and its secondary table index. It finds the fourth line according to that index with the value *8* which is the fifth line according to the primary index, as shown in the third `READ` statement.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE TABLE OF i 
     WITH NON-UNIQUE SORTED KEY skey COMPONENTS table_line. 
 
itab = VALUE #( ( 3 ) ( 9 ) ( 1 ) ( 6 ) ( 8 ) ). 
 
READ TABLE itab 
     ASSIGNING FIELD-SYMBOL(<fs1>) 
     WHERE table_line > 6 ##PRIMKEY[SKEY]. 
FINAL(idx1) = sy-tabix. 
out->write( |{ idx1 }: { <fs1> }| ). 
 
READ TABLE itab 
     ASSIGNING FIELD-SYMBOL(<fs2>) 
     USING KEY skey 
     WHERE table_line > 6. 
FINAL(idx2) = sy-tabix. 
out->write( |{ idx2 }: { <fs2> }| ). 
 
READ TABLE itab 
     ASSIGNING FIELD-SYMBOL(<fs3>) 
     WHERE table_line = 8 ##PRIMKEY[SKEY] ##READ_WHERE_OK. 
FINAL(idx3) = sy-tabix. 
out->write( |{ idx3 }: { <fs3> }| )->display( ).
```

For a better understanding, the following tables show the relations between the index an line values in different sort orders

| **Primary Index** | **Secondary Index** | **Table Line** |
|-------------------|---------------------|----------------|
| *1*               | *2*                 | *3*            |
| *2*               | *5*                 | *9*            |
| *3*               | *1*                 | *1*            |
| *4*               | *3*                 | *6*            |
| *5*               | *4*                 | *8*            |

| **Primary Index** | **Secondary Index** | **Table Line** |
|-------------------|---------------------|----------------|
| *3*               | *1*                 | *1*            |
| *1*               | *2*                 | *3*            |
| *4*               | *3*                 | *6*            |
| *5*               | *4*                 | *8*            |
| *2*               | *5*                 | *9*            |
