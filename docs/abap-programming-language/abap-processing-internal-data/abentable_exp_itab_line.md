---
title: "table_exp - itab_line"
source_file: abentable_exp_itab_line.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - itab_line

## Syntax

``` abap
... { [KEY keyname INDEX] idx }   
  | { [KEY keyname [COMPONENTS]] comp1 = operand1 
                                 comp2 = operand2 
                                 ...  }   
  | { TABLE KEY keyname [COMPONENTS] {comp_name1|(name1)} = operand1 
                                     {comp_name2|(name2)} = operand2 
                                      ... } ...  
```

[`keyname`](abenkeyname.md) · [`keyname`](abenkeyname.md) · [`comp1`](abenitab_components.md) · [`comp2`](abenitab_components.md) · [`keyname`](abenkeyname.md)

### Alternative

[1. `... [KEY keyname INDEX] idx`](abentable_exp_itab_line.md#alternative-1)

[2. `... [KEY keyname [COMPONENTS]] comp1 = operand1 comp2 = operand2 ...`](abentable_exp_itab_line.html#alternative-2)

[3. `... TABLE KEY keyname [COMPONENTS] ...`](abentable_exp_itab_line.md#alternative-3)

## Overview

### Description

Specifies a table line in the square brackets of a [table expression](abentable_expressions.md). The following reads are possible:

- Index read

- Read using a free key or a table key

- Read using a table key

### Executable Example

[`table_exp` - Line Specification](abentable_exp_itab_line_abexa.md)

## Alternative 1

`... [KEY keyname INDEX] idx`

### Description

The table expression reads the line with the line number specified in `idx` with respect to a table index. The line is read in exactly the same way as when specifying an index

[`... INDEX idx [USING KEY keyname]`](abapread_table_index.md)

in the statement [`READ TABLE`](abapread_table.md). Similarly, `idx` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) and the optional KEY [`keyname`](abenkeyname.md) INDEX is equivalent to the USING KEY [`keyname`](abenkeyname.md) specified here. If the optional addition is not used, `itab` must be an [index table](../../abap-glossary/abenindex_table_glosry.md). If the addition is used, the secondary table index of a sorted secondary key can be specified statically or dynamically.

If no line exists for the specified index, the catchable exception `CX_SY_ITAB_LINE_NOT_FOUND` is usually raised. The attributes `KEY_NAME` and `KEY_COMP_VALUES` are not filled here. Exceptions to this rule are when a [start value](abentable_exp_optional_default.md) is specified, uses in the statement [`ASSIGN`](abapassign_mem_area_writable_exp.md), in the predicate function [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md), and in the table function [`line_index`](abenline_index_function.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the line with the line number 1 once using the secondary table key `skey` and twice using the primary table key. It is the third line once and the first line twice.

``` abap
DATA itab TYPE TABLE OF i 
          WITH NON-UNIQUE KEY primary_key COMPONENTS table_line 
          WITH NON-UNIQUE SORTED KEY skey COMPONENTS table_line. 
 
itab = VALUE #( ( 3 ) ( 2 ) ( 1 ) ). 
 
cl_demo_output=>new( 
  )->write( itab[ KEY skey INDEX 1 ] 
  )->write( itab[ KEY primary_key INDEX 1 ] 
  )->write( itab[ 1 ] 
  )->display( ).
```

## Alternative 2

`... [KEY keyname [COMPONENTS]] comp1 = operand1 comp2 = operand2 ...`

### Description

The table expression reads the line in accordance with the specified free search key.

- If `KEY keyname [COMPONENTS]` is not specified, the search is performed in exactly the same way as for the statement [`READ TABLE`](abapread_table.md) when specifying the free search key:

  [`... WITH KEY comp1 = operand1 comp2 = operand2 ...`](abapread_table_free.md) If the free key overlaps with some or all of the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md), the optimizations described under [`READ TABLE`](abapread_table_free.md) are performed when sorted tables and hashed tables are read. Unlike the statement [`READ TABLE`](abapread_table.md), no binary searches can be forced for a table expression.

- If `KEY keyname [COMPONENTS]` is specified, an optimized search is performed in exactly the same way as for he statement [`READ TABLE`](abapread_table.md) when specifying the free search key with the name of a table key:

  [`... WITH KEY keyname COMPONENTS comp1 = operand1 comp2 = operand2 ...`](abapread_table_free.md) A sorted table key `keyname` does not have to be covered completely by components. For sorted as well as secondary keys, components can be specified that are not part of the table key. Unlike than in the statement `READ TABLE`, the addition `COMPONENTS` can be omitted in table expressions.

The components `comp1 comp2 ...` can be specified exactly as in the `READ` statement in accordance with the rules from the section [Specifying Components](abenitab_components.md) and compatible or convertible operands `operand1 operand2 ...` must be specified that are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). The same syntax warnings can occur as for the respective `READ TABLE` statements.

If no line is found for the specified free key, the catchable exception `CX_SY_ITAB_LINE_NOT_FOUND` is usually raised. The attributes `KEY_NAME` and `KEY_COMP_VALUES` are not filled here. Exceptions to this rule are when a [start value](abentable_exp_optional_default.md) is specified, uses in the statement [`ASSIGN`](abapassign_mem_area_writable_exp.md), in the predicate function [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md), and in the table function [`line_index`](abenline_index_function.md).

### Hints

- In order to use the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) explicitly, the key must be specified using its predefined name `primary_key` or an alias name.

- The main purpose of using a part of a sorted table key is to determine the existence of a specified line that is not necessarily specified completely or, for example, a line number as the starting point of a subsequent sequential read using [`LOOP ... FROM`](abaploop_at_itab_cond.md) as efficiently as possible.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading a line from an internal table specifying a free key without key name. The search is and cannot be not optimized, because the search fields are not part of the primary key of the sorted table and there is no appropriate secondary key.

``` abap
DATA itab TYPE SORTED TABLE OF spfli 
          WITH UNIQUE KEY carrid connid. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @itab. 
 
TRY. 
    cl_demo_output=>display( itab[ cityfrom = 'FRANKFURT' ]  ). 
  CATCH cx_sy_itab_line_not_found. 
    ... 
ENDTRY.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading a line from an internal table specifying a free key without key name. The search is not optimized, because the search fields are not part of the primary key of the sorted table. Since there is an appropriate secondary key available, it could be optimized and therefore, a syntax warning occurs that is suppressed by a pragma here.

``` abap
DATA itab TYPE SORTED TABLE OF spfli 
          WITH UNIQUE KEY carrid connid 
          WITH NON-UNIQUE SORTED KEY cities COMPONENTS cityfrom cityto. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @itab. 
 
TRY. 
    cl_demo_output=>display( 
      itab[ cityfrom = 'FRANKFURT' ] ) ##primkey[cities]. 
  CATCH cx_sy_itab_line_not_found. 
    ... 
ENDTRY.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading a line from an internal table by specifying a free key by naming an appropriate secondary key and specifying a part of the key fields. The search is partly optimized.

``` abap
DATA itab TYPE SORTED TABLE OF spfli 
          WITH UNIQUE KEY carrid connid 
          WITH NON-UNIQUE SORTED KEY cities COMPONENTS cityfrom cityto. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @itab. 
 
TRY. 
    cl_demo_output=>display( 
      itab[ KEY cities cityfrom = 'FRANKFURT' ] ). 
  CATCH cx_sy_itab_line_not_found. 
    ... 
ENDTRY.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading a line from a standard table specifying a free key by naming a secondary table key and all key fields. The search is fully optimized.

``` abap
DATA itab TYPE SORTED TABLE OF spfli 
          WITH UNIQUE KEY carrid connid 
          WITH NON-UNIQUE SORTED KEY cities COMPONENTS cityfrom cityto. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @itab. 
 
TRY. 
    cl_demo_output=>display( itab[ KEY cities COMPONENTS 
                                       cityfrom = 'FRANKFURT' 
                                       cityto   = 'SINGAPORE' ] ). 
  CATCH cx_sy_itab_line_not_found. 
    ... 
ENDTRY.
```

## Alternative 3

`... TABLE KEY keyname [COMPONENTS] ...`

### Description

The table expression reads the line in accordance with an explicitly specified [table key](../../abap-glossary/abentable_key_glosry.md). The search is performed in exactly the same way as when specifying the table key

[`... WITH TABLE KEY [keyname COMPONENTS] ...`](abapread_table_key.md)

in the statement [`READ TABLE`](abapread_table.md). The table key must be covered completely by specifying components and no components can be specified that are not part of the table key.

Unlike the statement `READ TABLE`, a table expression must specify the name of the table key and the addition `COMPONENTS` can be omitted. Like the statement `READ TABLE`, the table key `keyname` and the key components can be specified statically or dynamically. The operands `operand1 operand2 ...` are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md).

If no line is found for the specified table key, the catchable exception `CX_SY_ITAB_LINE_NOT_FOUND` is usually raised and its attributes `KEY_NAME` and, if the table is not empty, `KEY_COMP_VALUES` are filled. Exceptions to this rule are when a [start value](abentable_exp_optional_default.md) is specified, uses in the statement [`ASSIGN`](abapassign_mem_area_writable_exp.md), in the predicate function [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md), and in the built-in function [`line_index`](abenline_index_function.md).

### Hints

- Searches using the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) do not have to specify it explicitly. Instead, the variants with a free search key can be used. If this covers the primary table key, it is used for optimized reads on sorted tables and hashed tables.

- In order to use the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) in this variant explicitly, the key must be specified using its predefined name `primary_key` or an alias name.

- The main purpose of an explicitly specified table key is to read exactly one completely specified line.

- Using the variant `KEY keyname` and specifying all key fields has the same effect as using `TABLE KEY keyname`. In the latter variant it is ensured syntactically that all key fields are specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading a line from an internal table by specifying the full primary table key. The search is fully optimized.

``` abap
DATA itab TYPE SORTED TABLE OF spfli 
          WITH UNIQUE KEY carrid connid. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @itab. 
 
TRY. 
    cl_demo_output=>display( itab[ TABLE KEY primary_key 
                                             carrid = 'LH' 
                                             connid = '400' ]  ). 
  CATCH cx_sy_itab_line_not_found. 
    ... 
ENDTRY.
```
