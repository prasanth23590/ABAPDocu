---
title: "itab - Optimizing the WHERE Condition"
source_file: abenitab_where_optimization.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Performance Notes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Optimizing the WHERE Condition

Using the statements [`LOOP AT`](abaploop_at_itab.md), [`READ TABLE`](abapread_table.md), [`DELETE`](abapdelete_itab.md), and [`MODIFY`](abapmodify_itab.md) a `WHERE` condition can be specified to select specific lines of the internal table. While the search across a [standard table](../../abap-glossary/abenstandard_table_glosry.md) is always linear and cannot be optimized when using the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md), the compiler tries to optimize the search when the statement is processed by using a [sorted key](../../abap-glossary/abensorted_key_glosry.md) or a [hash key](../../abap-glossary/abenhash_key_glosry.md). This is the case, when

- accessing a [sorted table](../../abap-glossary/abensorted_table_glosry.md) using its primary key,

- accessing a [hashed table](../../abap-glossary/abenhashed_table_glosry.md) using its primary key,

- accessing a table of any table type using a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) specified by `USING KEY`.

For the optimization, the compiler tries to transform the [relational expressions](../../abap-glossary/abenrelational_expression_glosry.md) of the given `WHERE` condition into an equivalent `WHERE` condition that starts with comparisons between key fields and values combined by `AND`. These key/value pairs are then used as a key specification for an optimized key access (binary search or hash algorithm as in the statement [`READ TABLE`](abapread_table.md) or a [table expression](abentable_expressions.md)), to find one or more lines. The found line or lines are then further checked using the remaining relational expressions from the `WHERE` condition that could not be extracted as key/value pairs.

Prerequisites for the optimization are therefore:

- The relational expressions of the `WHERE` condition can be transformed to sufficient key/value pairs.

- The corresponding key access returns the same results as the evaluation of respective part of the logical expression would. This is guaranteed only for compatible data types, since in the case of incompatible data types:

  - The content of the specified data objects is converted to the data type of the columns before the evaluation in the case of key accesses.

  - The [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) for incompatible data types apply when evaluating a [comparison expression](../../abap-glossary/abencomparison_expression_glosry.md). Here, all the data types involved play a part in determining which operand is converted into which comparison type.

If there are no or insufficient relational expressions to meet both of these prerequisites, no optimization is possible and the behavior is as follows:

- If a sorted table or a hashed table is accessed using the primary table key, all lines of the internal table are checked as in a standard table.

- If the table is read using a secondary table key, that is, if said key is specified after `USING KEY`, a syntax error or syntax check warning, or an exception is raised. Access using a secondary table key must always be executed in an optimized way.

The following sections describe when an access can be optimized.

- [Prerequisites for the Optimization of Hash Keys](abenitab_where_optimization.md#prerequisites-for-the-optimization-of-hash-keys)

- [Prerequisites for the Optimization of Sorted Keys](abenitab_where_optimization.md#prerequisites-for-the-optimization-of-sorted-keys)

- [Prerequisites for the Operands](abenitab_where_optimization.md#prerequisites-for-the-operands)

## Hints

- By specifying a key with `USING KEY`, it can be checked, whether an optimization is possible for a `WHERE` condition. The long texts of the syntax errors and warnings provide detailed information for dedicated situations.

- If the lines selected using `WHERE` are modified or deleted using [`MODIFY`](abapmodify_itab.md) or [`DELETE`](abapdelete_itab.md) and not just read using [`LOOP AT`](abaploop_at_itab.md), further update costs are incurred in addition to the search for the lines. When deleting lines from standard tables, it should be noted that searches using a secondary key optimize the selection of lines to be deleted, but not the update required for the primary key, which is usually performed using a linear search.

## Prerequisites for the Optimization of Hash Keys

In the case of a [hash key](../../abap-glossary/abenhash_key_glosry.md) access, it must be possible to transform the `WHERE` condition fully or partly to a set of comparisons on equality combined by `AND` that cover all components of the key. The operands must meet the prerequisites described below.

The operands of these relational expressions are then used as the key/value pairs for the key access. The remainder of the logical expression can contain any number of relational expressions combined using `AND`. Key components may be used in the relational expressions not used for the key access but not for comparisons on equality.

Comparisons specified by the tabular comparison operator [`IN range_tab`](../abap-program-flow-logic/abenlogexp_select_option.md) are ignored by the optimization. They are never part of the key access but are always applied to the lines found by the key access.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example:

- The first `WHERE` condition can be optimized. It is already written in an optimized form, where the three key fields are compared for equality and combined by `AND`. A comparison for a further column is also appended by `AND`.

- The second `WHERE` condition can be optimized. The compiler can transform it to the first `WHERE` condition by removing the double negation with `NOT` and by replacing `IS INITIAL` with a comparison for equality.

- The third `WHERE` condition can be optimized. The compiler can transform the comparisons combined by `OR` into comparisons combined by `AND` using De Morgan's Laws. Also the double negation with `NOT` for `IS INITIAL` is identified and removed.

- The fourth `WHERE` condition cannot be optimized because a comparison for a further column is appended by `OR`.

- The fifth `WHERE` condition cannot be optimized because there is a duplicate comparison for equality for a key field.

``` abap
TYPES: 
  BEGIN OF line, 
    a TYPE i, 
    b TYPE i, 
    c TYPE i, 
    d TYPE i, 
  END OF line. 
 
DATA itab TYPE STANDARD TABLE OF line 
               WITH UNIQUE HASHED KEY key COMPONENTS a b c. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs1>) 
             WHERE a = 3 AND b = 3 AND c = 0 AND d > 1. 
  ... 
ENDLOOP. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs2>) 
             WHERE d > 1 AND 
                   NOT ( NOT ( a = 3 AND b = 3 ) ) AND 
                   c IS INITIAL. 
  ... 
ENDLOOP. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs3>) 
             WHERE NOT ( NOT a = 3 OR NOT b = 3 ) AND 
                   d > 1 AND 
                   NOT c IS NOT INITIAL. 
  ... 
ENDLOOP. 
 
*LOOP AT itab USING KEY key "Syntax error 
*             ASSIGNING FIELD-SYMBOL(<fs4>) 
*             WHERE a = 3 AND b = 3 AND c = 0 OR d > 1. 
*  ... 
*ENDLOOP. 
 
*LOOP AT itab USING KEY key "Syntax error 
*             ASSIGNING FIELD-SYMBOL(<fs5>) 
*             WHERE a = 3 AND b = 3 AND c = 0 AND a = 1. 
*  ... 
*ENDLOOP.
```

## Prerequisites for the Optimization of Sorted Keys

In the case of a [sorted key](../../abap-glossary/abensorted_key_glosry.md) access, it must be possible to transform the `WHERE` condition fully or a partly to a set of comparisons with any [binary comparison operators](../abap-program-flow-logic/abenlogexp_any_operand.md) or with [`BETWEEN`](../abap-program-flow-logic/abenlogexp_between.md) combined by `AND` that cover an initial section of the key consisting of at least one component. The operands must meet the prerequisites described below.

The operands of these relational expressions are then used as the key/value pairs for the key access. The remainder of the logical expression can contain any number of relational expressions combined using `AND`. Key components may be used in the relational expressions not used for the key access but not for comparisons on equality. Nevertheless, the duplicate use of key fields in comparisons leads to a syntax warning.

The access to the internal table is partially sequential. For a forward loop, the starting point for processing is determined by a binary search with the extracted key/value pairs for relations `=`, `>=`, `>`, and `BETWEEN` (first operand) that cover the table key completely or partially. From the starting point on, the table is only processed as long as subconditions for pairs with relations `=`, `<=`, `<`, and `BETWEEN` (second operand) remain fulfilled. For a backward loop (see [`STEP`](abaploop_at_itab_cond.md)), the starting point is determined by pairs with relations `=`, `<=`, `<`, and `BETWEEN` (second operand) and the processing is stopped when subconditions for pairs with `=`, `>=`, `>`, and `BETWEEN` (first operand) are not fulfilled any more.

Comparisons specified by a tabular comparison operator [`IN range_tab`](../abap-program-flow-logic/abenlogexp_select_option.md) appended with `AND` are ignored by the optimization. They are never part of the key access but always applied to the lines found by the key access.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example:

- The first `WHERE` condition can be optimized. It is already written in an optimized form, where the three key fields are compared with different operators combined by `AND`. A comparison for a further column is also appended by `AND`.

- The second `WHERE` condition can be optimized. It is already written in an optimized form, where the first two key fields are compared.

- The third `WHERE` condition can be optimized. The first two key fields are extracted for the key access and the condition for the third key field is evaluated together with the additional condition on the resulting lines.

- The fourth `WHERE` condition can be optimized. The compiler can use De Morgan's Laws to transform the condition to comparisons combined by `AND`.

- The fifth `WHERE` condition can be optimized because it uses `BETWEEN` for the first key field.

- The sixth `WHERE` condition cannot be optimized because the additional condition is combined by `OR`.

- The seventh `WHERE` condition cannot be optimized because a key field is used two times in comparisons on equality.

- The eighth `WHERE` condition can be optimized but produces a syntax warning, suppressed by a pragma here, because a field is used twice.

``` abap
TYPES: 
  BEGIN OF line, 
    a TYPE i, 
    b TYPE i, 
    c TYPE i, 
    d TYPE i, 
  END OF line. 
 
DATA itab TYPE STANDARD TABLE OF line 
               WITH UNIQUE SORTED KEY key COMPONENTS a b c. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs1>) 
             WHERE a = 3 AND b >= 3 AND c < 0 AND d > 1. 
  ... 
ENDLOOP. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs2>) 
             WHERE a = 3 AND b < 3 AND d > 1. 
  ... 
ENDLOOP. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs3>) 
             WHERE a = 3 AND b = 3 AND NOT c = 1 AND d > 1. 
  ... 
ENDLOOP. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs4>) 
             WHERE NOT ( NOT a = 3 OR NOT b = 3 ). 
  ... 
ENDLOOP. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs5>) 
             WHERE a BETWEEN 1 AND 3. 
  ... 
ENDLOOP. 
 
*LOOP AT itab USING KEY key "Syntax error 
*             ASSIGNING FIELD-SYMBOL(<fs6>) 
*             WHERE a = 3 AND b = 3 OR d > 1. 
*  ... 
*ENDLOOP. 
 
*LOOP AT itab USING KEY key "Syntax error 
*             ASSIGNING FIELD-SYMBOL(<fs7>) 
*             WHERE a = 3 AND b = 3 AND a = 1. 
*  ... 
*ENDLOOP. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs8>) 
             WHERE a = 3 AND b = 3 AND a > 1 ##ITAB_DUP_IN_WHERE[A]. 
  ... 
ENDLOOP.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, the partially sequential access to the internal table is as follows:

- The first loop is a forward loop.

  - The starting point is determined by key/value pairs of relations `a =0`, `b >= 0`, `c > 2`.

  - The table is processed as long as subconditions for the pairs `a = 0`, `b < 5` are fulfilled.

- The second loop is a backward loop.

  - The starting point is determined by the pairs `a <= 1`, `b < 5`.

  - The table is processed as long as subconditions for the pairs `a >= -1`, `b >= 0`, `c > 2` are fulfilled.

- The third loop is a forward loop and the fourth loop is a backward loop. Since for both loops there is no relation for key field `a`:

  - No starting point can be determined.

  - No subconditions can be determined.

    An optimization is not possible

``` abap
TYPES: 
  BEGIN OF line, 
    a TYPE i, 
    b TYPE i, 
    c TYPE i, 
    d TYPE i, 
  END OF line. 
 
DATA itab TYPE STANDARD TABLE OF line 
               WITH UNIQUE SORTED KEY key COMPONENTS a b c. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs1>) 
             WHERE a = 0 AND b >= 0 AND b < 5 AND c > 2. 
  ... 
ENDLOOP. 
 
LOOP AT itab USING KEY key 
             ASSIGNING FIELD-SYMBOL(<fs2>) 
             STEP -1 
             WHERE a BETWEEN -1 AND 1 AND b >= 0 AND b < 5 AND c > 2. 
  ... 
ENDLOOP. 
 
*LOOP AT itab USING KEY key "Syntax error 
*             ASSIGNING FIELD-SYMBOL(<fs3>) 
*             WHERE b >= 0 AND b < 5 AND c > 2. 
*  ... 
*ENDLOOP. 
 
*LOOP AT itab USING KEY key "Syntax error 
*             ASSIGNING FIELD-SYMBOL(<fs4>) 
*             STEP -1 
*             WHERE b >= 0 AND b < 5 AND c > 2. 
*  ... 
*ENDLOOP.
```

## Prerequisites for the Operands

The part of the logical expression that can be mapped to a key access must select the same lines as a statement [`READ TABLE`](abapread_table.md) or a corresponding [table expression](abentable_expressions.md) that specifies the corresponding components as keys.

- In the `WHERE` condition, the [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) for incompatible data types apply when comparing incompatible data objects, where it depends on the data types involved which operand is converted to which comparison type.

- If the additions [`WITH TABLE KEY`](abapread_table_key.md) and [`WITH KEY`](abapread_table_free.md) of the statement `READ` or [`KEY`](abentable_exp_itab_line.md) in a table expression are used, however, the content of the specified data objects is always converted to the data type of the columns before the comparison.

If this leads to different results, an optimization is not possible. Because of the complexity of the comparison rules, especially for [elementary data types](../abap-program-flow-logic/abenlogexp_rules_operands.md), it is not useful to set up a detailed set of rules when the comparison type exactly matches the data type of the left operand. Generally speaking,

- only fully compatible operands are optimizable,

- in some cases, operands with different elementary data types can be optimized, if the value ranges or lengths are suitable. For example, a comparison of a column with the type of a floating point number with an operand of type integer or of a column of `c` with a similar operand, if its length is less than the length of the column.

For this reason, it is advisable to use only pairs of [compatible](../../abap-glossary/abencompatible_glosry.md) operands in the `WHERE` condition. This guarantees that the differences in behavior of the `WHERE` condition and the specified key do not affect the result.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example is similar to the example in the section `WHERE log_exp` in [`LOOP AT itab`](abaploop_at_itab_cond.md).

- There, the access is done via the primary table key. No optimization takes place, but there is no warning from the syntax check.

- Here, the access is done via a secondary table key, resulting in a warning from the syntax check and a possible exception during program execution. Whether the exception is raised depends on the number of lines in the internal table.

``` abap
DATA text_short TYPE c LENGTH 2. 
DATA text_long  TYPE c LENGTH 4. 
 
DATA itab LIKE TABLE OF text_short 
          WITH UNIQUE HASHED KEY key COMPONENTS table_line. 
 
itab = VALUE #( ( 'AA' ) 
                ( 'BB' ) 
                ( 'CC' ) 
                ( 'DD' ) 
                ( 'EE' ) 
                ( 'FF' ) 
                ( 'GG' ) 
                ( 'HH' ) 
                ( 'II' ) 
                ( 'JJ' ) 
                ( 'KK' ) 
                ( 'LL' ) 
                ( 'MM' ) ). 
 
text_short = 'AA'. 
text_long  = 'AAXX'. 
 
LOOP AT itab INTO text_short USING KEY key 
             WHERE table_line = text_long. 
ENDLOOP. 
cl_demo_output=>write( |LOOP: { sy-subrc }| ). 
 
"Statement 
READ TABLE itab INTO text_short WITH TABLE KEY key 
                                COMPONENTS table_line = text_long. 
cl_demo_output=>write( |READ: { sy-subrc }| ). 
 
"Expression 
TRY. 
    text_short = itab[ KEY key COMPONENTS table_line = text_long ]. 
  CATCH cx_sy_itab_line_not_found. 
    ... 
ENDTRY. 
cl_demo_output=>display( |Expression: { text_short }| ).
```
