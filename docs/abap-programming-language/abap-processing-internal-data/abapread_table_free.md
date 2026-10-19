---
title: "READ TABLE, free_key"
source_file: abapread_table_free.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > READ TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ TABLE, free_key

## Syntax

``` abap
 ... WITH KEY { comp1 = operand1 comp2 = operand2 ... [BINARY SEARCH] }   
           | { keyname COMPONENTS comp1 = operand1 comp2 = operand2 ... } ...  
```

[`comp1`](abenitab_components.md) · [`comp2`](abenitab_components.md) · [`keyname`](abenkeyname.md) · [`comp1`](abenitab_components.md) · [`comp2`](abenitab_components.md)

### Variant

[1. `... WITH KEY comp1 = operand1 comp2 = operand2 ... [BINARY SEARCH] ...`](abapread_table_free.md#variant-1)

[2. `... WITH KEY keyname COMPONENTS comp1 = operand1 comp2 = operand2 ... .`](abapread_table_free.md#variant-2)

## Overview

### Description

Specifies a free search key. The free search key can be defined freely or linked to the specification of a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) in [`keyname`](abenkeyname.md).

### Hints

- [Table expressions](../../abap-glossary/abentable_expression_glosry.md) allow corresponding reads to also be performed in operand positions. All syntax variants shown here can be mapped to [line specifications](abentable_exp_itab_line.md) in table expressions.

## Variant 1

`... WITH KEY comp1 = operand1 comp2 = operand2 ... [BINARY SEARCH] ...`

### Addition

[`... BINARY SEARCH`](abapread_table_free.md#addition)

### Description

After the addition `WITH KEY`, components `comp1 comp2 ...` can be specified as search keys, in accordance with the rules [here](abenitab_components.md). An operand `operand1 operand2 ...` is assigned to each of these search keys and must be [compatible](../../abap-glossary/abencompatible_glosry.md) with the data type of the component or convertible to it. No duplicate or overlapping keys may be specified.

`operand1 operand2 ...` are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). If necessary, the content of the operands is converted to the data type of the components before the comparison. If an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) is specified, the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is determined from its operands and the data type of the component. If necessary, the result is converted to the data type of the component.

The system searches for the first line of the internal table whose values in the specified components or their subareas or attributes match the values in the assigned operands `operand1 operand2 ...`

The search is performed as follows for the individual table categories if `BINARY SEARCH` is not specified:

- [Standard tables](../../abap-glossary/abenstandard_table_glosry.md) are searched linearly.

- [Sorted tables](../../abap-glossary/abensorted_table_glosry.md) are searched binarily if the specified search key is an initial part of the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) or includes this key, Otherwise the search is linear.

- [Hashed tables](../../abap-glossary/abenhashed_table_glosry.md) are searched using the hash algorithm if the specified search key completely covers the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md). Otherwise the search is linear.

If the [`name`](abenitab_components.md) field of a component `comp` is initial, the first line that matches the remaining search key is read. If all `name` fields are initial, the first line of the internal table is read.

When a line is found, the system field `sy-tabix` is set according to the table category:

- For index tables to the number of lines found in the primary table index

- For hashed tables to the value 0.

If no line is found, `sy-tabix` is undefined (-1), except if the complete table key or the addition `BINARY SEARCH` was specified in a sorted table. In this case, `sy-tabix` is set to the line number of the entry in the primary table index in front of which the line would be inserted using `INSERT ... INDEX ...`, to preserve the sort.

### Hints

- If the line type of the internal table is not known statically, the components of the search key can only be specified dynamically and not directly.

- If the search key includes components that supply a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) of the internal table without the key being specified in `keyname`, a warning is raised by the syntax check.

- If the `BINARY SEARCH` addition is used, and there are multiple hits, either due to an incompletely specified search key or duplicate table entries, the first hit based on the sequence of lines is the primary index, that is, the line with the lowest line number, is always returned.

- If `WITH KEY` is used, it should be noted that the values of incompatible operands `operand1 operand2 ...` are converted to the data type of the columns before the comparison. This means that the [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) do not apply to incompatible data types. If a `WHERE` condition is used in the statements [`LOOP`](abaploop_at_itab_cond.md), [`MODIFY`](abapmodify_itab_multiple.md), and [`DELETE`](abapdelete_itab_lines.md), however, the comparison rules apply, which can produce different results.

- Due to the conversion before the comparison, [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) can be specified as operands for character-like types of type `c` or `string` and the corresponding special [conversion rules](abenconversion_enumerated.md) apply, which is not possible in a `WHERE` condition. This type of conversion produces a message from the extended syntax check.

- To avoid unexpected results after a conversion, `operand1`, `operand2`, ... must be compatible with the data type of the component.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The internal table `html_viewer_tab` contains references to HTML controls. The `READ` statement reads the reference that points to a HTML control in a specific container control.

``` abap
DATA: container   TYPE REF TO cl_gui_container, 
      html_viewer TYPE REF TO cl_gui_html_viewer. 
 
DATA html_viewer_tab LIKE TABLE OF html_viewer WITH EMPTY KEY. 
 
... 
 
CREATE OBJECT html_viewer EXPORTING parent = container. 
APPEND html_viewer TO html_viewer_tab. 
 
... 
 
READ TABLE html_viewer_tab 
           WITH KEY table_line->parent = container 
           INTO html_viewer. 
 
...
```

## Addition

`... BINARY SEARCH`

### Description

The addition `BINARY SEARCH` searches the table binarily instead of linearly. For larger tables (from approximately 100 entries), this can significantly reduce runtime. The table must, however, be sorted in ascending order by the components specified in the search key. The priority of the sort order must match exactly the order of the components in the search key. If this requirement is not met, the correct line is not usually found.

- The addition `BINARY SEARCH` is recommended for standard tables where no appropriate [sorted](../../abap-glossary/abensorted_key_glosry.md) [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) is defined.

- The addition `BINARY SEARCH` can only be specified for [sorted tables](../../abap-glossary/abensorted_table_glosry.md) if the specified search key is in the correct order and is an initial part of the table key, or includes the key. It has no special effect in this situation.

- The addition `BINARY SEARCH` cannot be specified for [hashed tables](../../abap-glossary/abenhashed_table_glosry.md).

### Hints

- If the addition `BINARY SEARCH` is used, the statement `READ` always performs an index access, and can therefore only be used for tables with the appropriate type. [Formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) or a [field symbol](../../abap-glossary/abenfield_symbol_glosry.md) must have at least the generic type `INDEX TABLE`.

- The addition `BINARY SEARCH` is based on standard sorting according to the size of the components. Text sorting with the addition `AS TEXT` of the statement [`SORT`](abapsort_itab.md) can produce unexpected results, since the result for text-like components no longer depends on the binary representation, but on the [locale](../../abap-glossary/abenlocale_glosry.md) of the current [text environment](../../abap-glossary/abentext_environment_glosry.md).

- The method `READ_BINARY_SEARCH_CHECK` of the class `CL_ABAP_ITAB_UTILITIES` can be used to check whether the required sorting exists for the addition `BINARY SEARCH`.

- When the addition `BINARY SEARCH` is used, if there are multiple hits due to an incomplete search key or duplicate entries in the table, the first hit according to the order of the lines in the primary index is returned. This is the line with the lowest line number.

- Instead of using the addition `BINARY SEARCH`, it is recommended that work is done either with [sorted tables](../../abap-glossary/abensorted_table_glosry.md) or with [sorted](../../abap-glossary/abensorted_key_glosry.md) [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a table line with `BINARY SEARCH` after the table has been sorted accordingly. However, if possible `sflight_tab` should be created as a sorted table or given a sorted secondary key afterwards (see example below).

``` abap
DATA sflight_tab TYPE STANDARD TABLE OF sflight WITH EMPTY KEY. 
 
... 
 
SORT sflight_tab BY carrid connid fldate. 
 
READ TABLE sflight_tab 
     WITH KEY carrid = 'LH' connid = '400' fldate = '20240627' 
     BINARY SEARCH 
     ASSIGNING FIELD-SYMBOL(<flight>).
```

## Variant 2

`... WITH KEY keyname COMPONENTS comp1 = operand1 comp2 = operand2 ...`

### Description

[`keyname`](abenkeyname.md) can be used to specify a [table key](../../abap-glossary/abentable_key_glosry.md). The same applies when specifying the components as in the variant without key specifications.

If a [secondary table key](../../abap-glossary/abensecondary_table_index_glosry.md) is specified in `keyname`, the behavior is as follows:

- If a [sorted key](../../abap-glossary/abensorted_key_glosry.md) is specified, the specified search key must be an initial part of the secondary table key or include it. The associated [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) is then searched binarily. If multiple entries are found when using a non-unique search key, the first hit, that is, the line with the lowest line number, is read in the secondary index. Additional search criteria can also be specified that are also evaluated.

- If a [hash key](../../abap-glossary/abenhash_key_glosry.md) is specified, the specified search key must include the secondary table key and the hash algorithm is used. Additional search criteria can also be specified that are also evaluated.

When a line is found, the system field `sy-tabix` is set with respect to the specified secondary table key:

- For sorted secondary keys to the number of the found line in the associated secondary table index

- For hash keys to the value 0.

If no line is found, `sy-tabix` is undefined (-1), except when it is covered completely by a sorted secondary key. In this case, `sy-tabix` is set to the line number of the entry in the secondary table index in front of which the line would be inserted using `INSERT ... INDEX ...`, to preserve the sort.

If the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified in `keyname` using its name `primary_key`, the behavior is the same as in the variant without key specifications.

### Hints

- The specification of free keys differs when a secondary key is used from the [`table_key`](abapread_table_key.md) variant for specifying the table key in that additional conditions can be specified in the search key. These conditions can also be evaluated and reduce the length of the hit list. For secondary sorted keys, however, free search keys make it possible to specify an incomplete search key, which can make the hit list longer.

- If a secondary table key is used, when the value of `sy-tabix` is used subsequently as an index specification in other processing statements for the internal table, it must be ensured that the same table key is used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a table line using the sorted secondary table key `dbkey`. The read is now performed automatically using a binary search, as in the example above where `BINARY SEARCH` is specified explicitly, and an explicit sort is not necessary.

``` abap
DATA sflight_tab TYPE STANDARD TABLE OF sflight WITH EMPTY KEY 
                 WITH UNIQUE SORTED KEY dbkey 
                      COMPONENTS carrid connid fldate. 
 
... 
 
READ TABLE sflight_tab WITH KEY dbkey 
     COMPONENTS carrid = 'LH' connid = '400' fldate = '20240916' 
     ASSIGNING FIELD-SYMBOL(<flight>).
```
