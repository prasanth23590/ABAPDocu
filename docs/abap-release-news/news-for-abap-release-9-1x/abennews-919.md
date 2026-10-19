---
title: "News for ABAP Release 9.19"
source_file: abennews-919.html
section: "ABAP Release News > News for ABAP Release 9.1x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 9.19

The kernel release for ABAP release 9.19 is 9.19.

## Data Types

| Modification                       | Description                                                                                                                                                                               |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Recursive Structure References** | [Recursive structure references](../../abap-programming-language/abap-declarations/abaprecursive_struc_references.md) are components of a structured type that represent data references to the same structure in which they are defined. |

## Expressions

| Modification                               | Description                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Data Objects as Relational Expressions** | Individual data objects can now represent [relational expressions](../../abap-glossary/abenrelational_expression_glosry.md), returning a truth value. The expression evaluates to true if the operand's content is not initial. It evaluates to false if it is initial. The concrete type of the operand is arbitrary, as the type-specific initial value is checked. |

## Internal Tables

| Modification                     | Description                                                                                                                                                                                                                    |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`DELETE DUPLICATES FROM ...`** | The syntax [`DELETE DUPLICATES FROM itab`](../../abap-programming-language/abap-processing-internal-data/abapdelete_duplicates.md) removes duplicates from an internal table, similar to the statement `DELETE ADJACENT DUPLICATES FROM itab`, however, without requiring a prior sorting. |

## ABAP SQL

| Modification                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Method for Preventing Commits with `IF_ABAP_SQL_CONNECTION`** | An [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) implementing the interface [`IF_ABAP_SQL_CONNECTION`](../../abap-programming-language/abap-database-access/abenif_abap_sql_connection.md) represents a [database connection](../../abap-glossary/abendatabase_connection_glosry.md) that can be used behind the `CONNECTION` addition of ABAP SQL statements. The interface now includes the new `SET_BLOCK_COMMIT` method that prevents implicit and explicit commits. |
