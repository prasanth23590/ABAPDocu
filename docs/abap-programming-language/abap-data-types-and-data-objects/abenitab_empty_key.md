---
title: "itab - Empty Table Key"
source_file: abenitab_empty_key.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables > itab - Table Key > itab - Primary Table Key"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Empty Table Key

The [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) of a [standard table](../../abap-glossary/abenstandard_table_glosry.md) can be empty. An empty table key does not contain any key fields.

- [Declaration](abenitab_empty_key.md#declaration)

- [Notes on Use](abenitab_empty_key.md#notes-on-use)

  - [Uncritical Use](abenitab_empty_key.md#uncritical-use)

  - [Critical Use](abenitab_empty_key.md#critical-use)

## Hint

[Sorted keys](../../abap-glossary/abensorted_key_glosry.md) and [hash keys](../../abap-glossary/abenhash_key_glosry.md) are never empty, regardless of whether they are primary or [secondary](../../abap-glossary/abensecondary_key_glosry.md).

## Declaration

An empty primary table key can be created as follows:

- Explicitly, with the addition [`EMPTY KEY`](../abap-declarations/abaptypes_primary_key.md) of the statements [`TYPES`](../abap-declarations/abaptypes_primary_key.md), [`DATA`](../abap-declarations/abapdata_primary_key.md), and so on or in the [ABAP Dictionary](../../abap-dictionary-ddic/ddic-data-types/abenddic_table_types_tech.md).

- Explicitly, using an inline declaration [`INTO TABLE @DATA|@FINAL(itab)`](../abap-database-access/abapinto_clause.md) in the statement `SELECT`

- Implicitly, when using the [standard key](abenitab_standard_key.md) if a structured line type does not contain any non-numeric elementary components or if an unstructured line type is table-like.

## Notes on Use

### Uncritical Use

An empty primary table key can be used to handle a table like an array. This means that filling the table and other accesses take place in such a way that no order is based on key values. An empty internal table key can be used in all statements in which its implicit or explicit specification determines the order in which the internal table is accessed.

### Hints

- Developers should always be aware that they are handling an empty primary table key. This can only be achieved when the empty key is declared explicitly. An implicit declaration using the [standard key](abenitab_standard_key.md), in which the line type determines whether the primary table key is empty or not, is not usually suitable.

- Even with an empty primary key, a standard table has the order specified by the [primary index](../../abap-glossary/abenprimary_table_index_glosry.md), which can be exploited in respective index accesses or loop processing.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A prominent example is the statement [`LOOP AT itab`](../abap-processing-internal-data/abaploop_at_itab.md), where implicit or explicit use (using [`USING primary_key`](../abap-processing-internal-data/abaploop_at_itab_cond.md)) defines the processing order with respect to the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md), but has no other effect.

### Critical Use

In the following statements, which work with the primary table key without specifying the key fields explicitly, the specification of an empty primary table key is critical and generally produces unexpected behavior. An empty table key that is known statically produces a syntax check warning.

- Primary table key specification using a work area:

  - If [`FROM wa`](../abap-processing-internal-data/abapread_table_key.md) is used to specify an empty table key for the statement [`READ TABLE`](../abap-processing-internal-data/abapread_table.md), the first line of the internal table is read.

  - If [`FROM wa`](../abap-processing-internal-data/abapmodify_itab_single.md) is used to specify an empty table key for the statement [`MODIFY`](../abap-processing-internal-data/abapmodify_itab.md), the first line of the internal table is modified.

  - If [`FROM wa`](../abap-processing-internal-data/abapdelete_itab_key.md) is used to specify an empty table key for the statement [`DELETE`](../abap-processing-internal-data/abapdelete_itab.md), the first line of the internal table is deleted.

- If the statement [`SORT itab`](../abap-processing-internal-data/abapsort_itab.md) is executed without the addition `BY` and the primary table key is empty, the statement is ignored, which means no sorting takes place.

- If the statement [`DELETE ADJACENT DUPLICATES`](../abap-processing-internal-data/abapdelete_duplicates.md) contains an empty primary table key, no lines are deleted.

- If the primary table key is empty, the statement [`COLLECT`](../abap-processing-internal-data/abapcollect.md) always compresses the first line of the internal table. In this case, all components of the line type must be numeric.

### Hint

The statements described above can be particularly unpredictable when using the [standard key](abenitab_standard_key.md), which itself can be declared implicitly, to declare an empty internal table key.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a table with an empty table key, in which the order of the lines should not change due to sorting. A `SORT table_of_strings` statement would have no effect.

``` abap
DATA table_of_strings 
  TYPE STANDARD TABLE OF string 
       WITH EMPTY KEY. 
 
APPEND `This should` TO table_of_strings. 
APPEND `stay` TO table_of_strings. 
APPEND `in order` TO table_of_strings. 
 
cl_demo_output=>display( table_of_strings ).
```
