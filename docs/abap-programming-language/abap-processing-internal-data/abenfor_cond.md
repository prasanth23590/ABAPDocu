---
title: "FOR, cond"
source_file: abenfor_cond.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR, cond

## Syntax

``` abap
 ... [USING KEY keyname] 
    [FROM idx1] [TO idx2] [STEP n] 
    [WHERE ( log_exp )|(cond_syntax)] ...  
```

[`keyname`](abenkeyname.md) · [`log_exp`](../abap-program-flow-logic/abenlogexp.md)

## Description

As with [`LOOP AT itab`](abaploop_at_itab_cond.md), the following is possible for each expression [`FOR ... IN itab`](abenfor_in_itab.md) and [`FOR GROUPS ... OF`](abenfor_groups_of.md) of a constructor expression:

- `USING KEY` can be used to specify the table key with which the table is evaluated.

- `FROM` and `TO` can be used as upper and lower limits to restrict the lines in the table index used.

- `STEP` can be used to define the step size and loop order for processing the internal table.

- `WHERE` can be used to specify static or dynamic conditions for column content.

The syntax and semantics are exactly the same as in [`LOOP AT itab`](abaploop_at_itab_cond.md), apart from the fact that a statically specified logical expression `log_exp` in the `WHERE` condition must always be placed in parentheses. This also applies to dynamically specified, parenthesized standard tables with a character-like line type, such as `... WHERE ( (dyn_tab) ) ...`. However, dynamically specified character-like data objects are specified without the extra pair of parentheses, for example, `... WHERE (dyn_spec) ...`.

In the expression [`FOR ... IN GROUP group`](abenfor_in_group.md), only static `WHERE` conditions can be specified for `cond`.

## Hints

- The local auxiliary variables of the expression visible in this position can be used for `idx1`, `idx2`, and in the logical expression of the `WHERE` condition.

- The [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` can be used in the logical expression of the `WHERE` condition.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows how the same result can be achieved with a `WHERE` condition in an iteration expression and the filter operator [`FILTER`](abenconstructor_expression_filter.md). The shorter filter expression is usually more suitable in this case.

``` abap
DATA messages TYPE SORTED TABLE OF t100 WITH NON-UNIQUE KEY sprsl msgnr. 
SELECT * 
       FROM t100 
       WHERE arbgb = 'SABAPDEMOS' 
       INTO TABLE @messages. 
 
DATA value_tab LIKE messages. 
value_tab = VALUE #( FOR wa IN messages WHERE ( sprsl = 'E' ) ( wa ) ). 
 
ASSERT value_tab = FILTER #( messages WHERE sprsl = 'E' ).
```
