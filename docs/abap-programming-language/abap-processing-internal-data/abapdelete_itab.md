---
title: "DELETE itab"
source_file: abapdelete_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DELETE itab

## Syntax

``` abap
DELETE { itab_line | itab_lines | duplicates }.  
```

[`itab_line`](abapdelete_itab_line.md) · [`itab_lines`](abapdelete_itab_lines.md) · [`duplicates`](abapdelete_duplicates.md)

## Description

This statement either deletes a line [`itab_line`](abapdelete_itab_line.md) or multiple lines [`itab_lines`](abapdelete_itab_lines.md), which can be specified using a table key or a table index, or it deletes adjacent duplicate lines [`duplicates`](abapdelete_duplicates.md).

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | At least one line was deleted.                                                                                                                                                                                                                                                     |
| 4              | No lines were deleted, since no appropriate line was found when deleting using a table key or when specifying a logical expression, the index specified when deleting using a table index was greater than the current number of lines, or no duplicate adjacent lines were found. |

The system field `sy-tabix` is not set.

## Hints

- If `DELETE` is used to delete the current line inside a [`LOOP AT itab`](abaploop_at_itab.md) loop, a field symbol or reference variable assigned with [`ASSIGNING`](abaploop_at_itab_result.md) or [`REFERENCE INTO`](abaploop_at_itab_result.md) becomes unassigned or unbound and should not be used after the `DELETE` statement any more.

- Deleting lines of internal tables using `DELETE` does not usually release any memory in the internal table. Statements such as [`CLEAR`](abapclear.md) or [`FREE`](abapfree_dataobject.md) must be used to release this memory.

- An internal table in which all lines have been deleted with `DELETE` is empty and the relational expression [`IS INITIAL`](../abap-program-flow-logic/abenlogexp_initial.md) is true. Nevertheless, the internal table usually still occupies memory and therefore is not in the same state as an initial table after its declaration.

- When deleting lines in an internal table, costs are incurred for updating all existing [table keys](../../abap-glossary/abentable_key_glosry.md) and [table indexes](../../abap-glossary/abentable_key_glosry.md). The [primary key](../../abap-glossary/abenprimary_table_key_glosry.md) and all unique [secondary keys](../../abap-glossary/abensecondary_table_key_glosry.md) are updated directly, whereas non-unique secondary keys are only updated if the lines to be deleted are contained within an updated part of a relevant index ([lazy update](../../abap-glossary/abenlazy_update_glosry.md)). When deleting a line from a standard table and the line is found using a secondary key, the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md) in particular must be updated, which usually requires a linear search.

- There is no implicit selection of a suitable key or index. The used table key or table index is always specified uniquely. A syntax check warning occurs if there is a suitable [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) available but not used. This warning should be removed by using the key. However, in exceptional cases, it can also be bypassed using a [pragma](../../abap-glossary/abenpragma_glosry.md).

- A special variant [`DELETE mesh_path`](abenmesh_delete.md) can be used to delete lines from the last path node of a [mesh path](../../abap-glossary/abenmesh_path_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of all initial lines of an internal table.

``` abap
DATA itab TYPE HASHED TABLE OF scarr WITH UNIQUE KEY carrid. 
 
... 
 
DELETE itab WHERE table_line IS INITIAL.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ITAB_DYN_LOOP`

- *Cause:* Error in a dynamic `WHERE` condition

  *Runtime error:* `DYN_WHERE_PARSE_ERROR`
