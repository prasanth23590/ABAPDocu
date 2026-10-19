---
title: "READ TABLE, table_key"
source_file: abapread_table_key.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > READ TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ TABLE, table_key

## Syntax

``` abap
... { FROM wa [USING KEY keyname] }   
  | { WITH TABLE KEY [keyname COMPONENTS]   
                     {comp_name1|(name1)} = operand1   
                     {comp_name2|(name2)} = operand2   
                     ...                             } ...  
```

[`keyname`](abenkeyname.md) · [`keyname`](abenkeyname.md)

### Alternative

[1. `... FROM wa [USING KEY keyname]`](abapread_table_key.md#alternative-1)

[2. `... WITH TABLE KEY [keyname COMPONENTS] ...`](abapread_table_key.md#alternative-2)

## Overview

### Description

Specifies a table key as a search key. The primary table key or a secondary table key can be specified. The values can be declared either implicitly in a work area `wa` behind `FROM` or explicitly by listing the components of the table key behind `TABLE KEY`.

When the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is used, the table categories are accessed as follows:

- [Standard tables](../../abap-glossary/abenstandard_table_glosry.md) are searched linearly.

- [Sorted tables](../../abap-glossary/abensorted_table_glosry.md) are searched binarily.

- [Hashed tables](../../abap-glossary/abenhashed_table_glosry.md) are searched using the hash algorithm.

When the [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) is used, a binary search is used for a [sorted key](../../abap-glossary/abensorted_key_glosry.md) and a [hash algorithm](../../abap-glossary/abenhash_algorithm_glosry.md) for a [hash key](../../abap-glossary/abenhash_key_glosry.md).

When a line is found, the system field `sy-tabix` is set as specified by the table key used:

- For sorted keys to the number of lines found in the associated table index.

- For hash keys to the value 0.

If no line is found, `sy-tabix` is set to the line number of the entry in the associated table index in the case of a sorted key, in front of which the line searched for would be inserted using `INSERT ... INDEX ...`, to preserve the sort.

### Hint

It should be noted that the system field [`sy-tabix`](abapread_table.md) is always set with reference to the table key used. If the value of the `sy-tabix` is used as an index specification after the `READ` statement is executed in another processing statement for the internal table, the same table key should be used there. It should be noted here that the primary index is always addressed if there is no explicit key specification.

## Alternative 1

`... FROM wa [USING KEY keyname]`

### Description

For `wa`, a work area compatible to the line type of the internal table must be specified. It is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The first line found in the internal table is processed whose values in the columns of the table key used match those of the corresponding components of `wa`.

If the `USING KEY` addition is not specified, the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is used. If the `USING KEY` addition is specified, the table key specified in [`keyname`](abenkeyname.md) is used.

If the [primary table key](../../abap-glossary/abenprimary_key_glosry.md) is used to access a [standard table](../../abap-glossary/abenstandard_table_glosry.md) and the key is [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md), the first line of the internal table is read. If this is known statically, the syntax check produces a warning.

### Hints

- When using the primary table key, it should be noted that this key can also be the [standard key](../../abap-glossary/abenstandard_key_glosry.md), which can have unexpected consequences:

  - For structured line types, the standard key covers all character-like and byte-like components.

  - The standard key of a standard table can be [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of lines of the internal table `spfli_tab` using the primary table key and a secondary key `city_key`. The `READ` statement evaluates the `spfli_key` work area.

``` abap
DATA: 
  spfli_tab TYPE SORTED TABLE OF spfli 
            WITH UNIQUE KEY carrid connid 
            WITH NON-UNIQUE SORTED KEY city_key 
                            COMPONENTS cityfrom cityto, 
  spfli_key LIKE LINE OF spfli_tab. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @spfli_tab. 
 
spfli_key = VALUE #( carrid = 'LH' connid = '0400' ). 
READ TABLE spfli_tab FROM spfli_key 
           ASSIGNING FIELD-SYMBOL(<spfli>). 
IF sy-subrc = 0. 
  ... 
ENDIF. 
 
spfli_key = VALUE #( cityfrom = 'FRANKFURT' cityto = 'BERLIN' ). 
READ TABLE spfli_tab FROM spfli_key USING KEY city_key 
           ASSIGNING <spfli>. 
IF sy-subrc = 0. 
  ... 
ENDIF.
```

## Alternative 2

`... WITH TABLE KEY [keyname COMPONENTS] ...`

### Description

Each component of the table key used must be listed either directly as `comp_name1 comp_name2 ...` or as a parenthesized character-like data object `name1 name2 ...`, which contains the name of the component when the statement is executed. `name` is not case-sensitive. If `name` only contains blanks, this component specification is ignored when the statement is executed. An operand `operand1 operand2 ...` [compatible](../../abap-glossary/abencompatible_glosry.md) with the data type of the component or convertible to it must be assigned to every component. The first line found in the internal table, whose values in the column of the table key used correspond with the values in the operands `operand1 operand2 ...` assigned, is processed. No duplicate or overlapping keys, nor columns that are not components of the table key can be specified.

`operand1 operand2 ...` are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). If necessary, the content of the operands is converted to the data type of the components before the comparison. If a conversion error occurs here, the exception cannot be handled using `CX_SY_CONVERSION_ERROR` and the associated runtime error occurs instead. If an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) is specified, the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is determined from its operands and the data type of the component. If necessary, the result is converted to the data type of the component.

If the addition `COMPONENTS` is not specified, the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is used. If the addition `COMPONENTS` is specified, the table key specified in [`keyname`](abenkeyname.md) is used.

### Hints

- The [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` can be specified as a component for tables with an unstructured line type and for which the entire table line is defined as a table key.

- If `WITH TABLE KEY` is used, it should be noted that the values of incompatible operands `operand1`, `operand2`, ... are converted to the data type of the columns before the comparison, and therefore the [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) do not apply to incompatible data types. If a `WHERE` condition is used in the statements [`LOOP`](abaploop_at_itab_cond.md), [`MODIFY`](abapmodify_itab_multiple.md), and [`DELETE`](abapdelete_itab_lines.md), however, the comparison rules do apply, which can produce different results.

- Due to the conversion before the comparison, [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) can be specified as operands for character-like types of type `c` or `string` and the corresponding special [conversion rules](abenconversion_enumerated.md) apply, which is not possible in a `WHERE` condition. Conversions of this type produce a message from the extended syntax check.

- To avoid unexpected results after a conversion, `operand1`, `operand2`, ... must be compatible with the data type of the component.

- If the line type of the internal table is not known statically, the components of the key can only be specified dynamically and not directly.

- A [customizing include](../../abap-glossary/abencustomizing_include_glosry.md) must not be specified as a component if it is empty.

- Using the variant [`WITH KEY keyname COMPONENTS`](abapread_table_free.md) with specifying all key fields has the same effect as using `WITH TABLE KEY keyname`. In the latter variant it is ensured syntactically that all key fields are specified.

- [Table expressions](../../abap-glossary/abentable_expression_glosry.md) allow corresponding reads to also be performed in operand positions. The syntax shown here can be mapped to a [line specification](abentable_exp_itab_line.md) in a table expression.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of lines of the internal table `spfli_tab` using the primary key and a secondary table key `city_key`. The components of the table keys are specified explicitly in the `READ` statement.

``` abap
DATA: 
  spfli_tab TYPE SORTED TABLE OF spfli 
            WITH UNIQUE KEY carrid connid 
            WITH NON-UNIQUE SORTED KEY city_key 
                            COMPONENTS cityfrom cityto, 
  spfli_key LIKE LINE OF spfli_tab. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @spfli_tab. 
 
READ TABLE spfli_tab 
           WITH TABLE KEY primary_key 
                COMPONENTS carrid = 'LH' connid = '400' 
           ASSIGNING FIELD-SYMBOL(<spfli>). 
IF sy-subrc = 0. 
  ... 
ENDIF. 
 
READ TABLE spfli_tab 
           WITH TABLE KEY city_key 
                COMPONENTS cityfrom = 'FRANKFURT' cityto = 'BERLIN' 
           ASSIGNING <spfli>. 
IF sy-subrc = 0. 
  ... 
ENDIF.
```

### Executable Example

[Key Accesses](abenread_itab_using_key_abexa.md)
