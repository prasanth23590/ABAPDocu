---
title: "COLLECT"
source_file: abapcollect.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COLLECT

## Syntax

``` abap
COLLECT wa INTO itab [result].  
```

[`result`](abapcollect_itab_result.md)

## Description

This statement inserts the content of a work area `wa` either as a single line in an internal table `itab` or adds the values of its numeric components to the corresponding values of existing lines with the same [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md). `wa` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

[`result`](abapcollect_itab_result.md) can be used to set a reference to the inserted or changed line in the form of a field symbol or data reference.

Prerequisite for the use of this statement is that `wa` is [compatible](../../abap-glossary/abencompatible_glosry.md) with the line type of `itab`. All components that are not part of the primary table key must have a [numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md).

The table is searched for a line with the same primary key as follows:

- In [standard tables](../../abap-glossary/abenstandard_table_glosry.md) that are filled using `COLLECT` only, the entry is determined by temporary hash administration. The workload is independent of the number of entries in the table. The hash administration is temporary and is generally invalidated by writes to the table. If `COLLECT` statements are specified after an invalidation, a linear search of all table lines is performed. The workload for this search increases linearly in relation to the number of entries.

- In [sorted tables](../../abap-glossary/abensorted_table_glosry.md), the entry is determined using a binary search. The workload depends logarithmically on the number of entries in the table.

- In [hashed tables](../../abap-glossary/abenhashed_table_glosry.md), the entry is determined using the hash administration of the table and is always independent of the number of table entries.

If no line is found with an identical primary key, a line is inserted as follows and filled with the content of `wa`:

- In standard tables, the line is appended as the last line of the primary table index.

- In sorted tables, the new line is inserted in the sort order of the internal table in accordance with its key values, and the primary table index of the subsequent lines is increased by 1.

- In hashed tables, the new line is inserted into the internal table by the hash administration, in accordance with its key values.

If the internal table already contains one or more lines with an identical primary key, those values of the components of work area `wa` that are not part of the key are added to the corresponding components of the highest existing line (in the case of index tables, this is the line with the lowest primary table index).

An uncatchable exception is raised if a duplicate entry in a unique [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) were to be produced when the statement `COLLECT` is executed.

If the primary table key of a standard table is [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md), all components of the line type must be numeric and the first line of the internal table is always compressed. If this is known, a syntax check warning occurs that can be hidden using a [pragma](../../abap-glossary/abenpragma_glosry.md).

## System Fields

The statement `COLLECT` sets `sy-tabix` for [standard tables](../../abap-glossary/abenstandard_table_glosry.md) and [sorted tables](../../abap-glossary/abensorted_table_glosry.md) to the line number of the inserted or existing line in the primary table index, and for [hashed tables](../../abap-glossary/abenhashed_table_glosry.md) to the value 0.

## Hints

- `COLLECT` should only be used if internal tables are to be created that are genuinely unique or compressed. In this case, `COLLECT` can greatly benefit performance. If uniqueness or compression are not required, or if uniqueness is guaranteed for other reasons, the statement [`INSERT`](abapinsert_itab.md) should be used instead.

- The statement `COLLECT` is not suitable for standard tables and should no longer be used for them. `COLLECT` can be used for sorted tables and hashed tables without any problems since these, unlike standard tables, always have their own stable key administration that can be exploited by `COLLECT`. When used for sorted tables, they should have a unique primary key or the table should be filled with `COLLECT` only. For hashed tables, all prerequisites are fulfilled automatically.

- If a standard table is still filled using `COLLECT`, it should not be processed using any other statement than [`MODIFY`](abapmodify_itab.md). In the latter case, the addition `TRANSPORTING` ensures that no primary key fields can be changed. This is the only way to ensure that the table entries are always unique and compressed and that the statement `COLLECT` runs efficiently. The function module `ABL_TABLE_HASH_STATE` can be used to check whether a standard table is suitable for processing using `COLLECT`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Compressed insertion of data from the DDIC database table `SFLIGHT` into the internal table `seats_tab`. The lines in which the primary key components `carrid` and `connid` are identical are compressed by adding the number of occupied seats to the numeric component `seatsocc`.

``` abap
DATA: BEGIN OF seats, 
        carrid   TYPE sflight-carrid, 
        connid   TYPE sflight-connid, 
        seatsocc TYPE sflight-seatsocc, 
      END OF seats. 
 
DATA seats_tab LIKE HASHED TABLE OF seats 
               WITH UNIQUE KEY carrid connid. 
 
SELECT carrid, connid, seatsocc 
       FROM sflight 
       INTO @seats. 
  COLLECT seats INTO seats_tab. 
ENDSELECT.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ARITHMETIC_OVERFLOW`

- *Cause:* Overflow in integer field when creating totals

  *Runtime error:* `COLLECT_OVERFLOW`

- *Cause:* Overflow in type `p` field when creating totals

  *Runtime error:* `COLLECT_OVERFLOW_TYPE_P`
