---
title: "MERGE writable_obj"
source_file: abapmerge_dbtab.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MERGE writable_obj

## Syntax Forms

**Static Form**

``` abap
MERGE INTO target [AS target_alias] 
      USING { source [AS source_alias] | @itab AS itab_alias [DECLARE CLIENT clnt] } ON join_condition 
      WHEN MATCHED [AND match_condition1 [AND match_condition2 ... ] ] THEN 
        { UPDATE { ALL | SET set_condition } | DELETE } 
      WHEN NOT MATCHED [AND match_condition [AND match_condition2 ... ]] THEN INSERT { ALL | ( columns_list ) VALUES ( values_expressions ) } 
      [%_HINTS hints] [OPTIONS PRIVILEGED ACCESS].
```

**Dynamic Form**

``` abap
MERGE (dynamic_syntax).
```

[`%_HINTS hints`](abenabap_sql_db_hints.md) · [`OPTIONS`](abapiumd_options.md) · [`PRIVILEGED ACCESS`](abapselect_privileged_access.md)

## Description

The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement `MERGE` allows modification operations on a data source `target` by evaluating another data source `source`. It combines the logic of insert, update, and delete operations into a single statement, based on matching datasets using join conditions. Modifications can be made by specifying whether the datasets in `source` and `target` match or do not match.

`MERGE` statements perform a [right outer join](../../abap-glossary/abenright_outer_join_glosry.md).

Notes on the syntax:

- `USING` clause:

  - For `target`, [writable database objects](../../abap-glossary/abenwritable_db_obj_glosry.md) can be specified. `source` is a read position. You can specify writable database objects, read-only data sources, and internal tables.

  - Alias names can be optionally specified for `target` and `source`. When specifying an internal table as `source`, an alias name must be specified, and the internal table `itab` must be escaped using `@`. Optionally and if available, the client field can be specified for an internal table using `DECLARE CLIENT` and the field name `clnt`.

  - `join_condition`: The same conditions apply as explained in [`SELECT`, `FROM JOIN`](abapselect_join.md).

- The syntax allows specifying either a `WHEN MATCHED` clause, a `WHEN NOT MATCHED` clause, or both of them. When both are specified, the `WHEN MATCHED` clause must precede the `WHEN NOT MATCHED` clause.

- `WHEN MATCHED` clause:

  - Can be optionally enhanced with additional match conditions ([`match_condition1`](abenabap_sql_stmt_logexp.md), and so on). Conditions can be specified using both `source` and `target` components.

  - Allows an update or delete operation when the datasets match.

  - `UPDATE`: Updates the `target` with `source` content based on match conditions. Specifying `ALL` means that all `source` fields are respected for the update operation. `SET` allows specifying set conditions (`set_condition`) to perform conditional update operations. The values specified for the conditions can be represented by expressions, for example, using [ABAP SQL functions](abensql_builtin_func.md).

  - `DELETE`: Deletes datasets in `target` when matching datasets are found in `source`.

- `WHEN NOT MATCHED` clause:

  - Allows an insert operation when the datasets do not match.

  - Can be optionally enhanced with additional match conditions ([`match_condition1`](abenabap_sql_stmt_logexp.md), and so on). Conditions can be specified using both `source` and `target` components. Note that due to the [right outer join](../../abap-glossary/abenright_outer_join_glosry.md) performed, the values in the target table are null values.

  - `ALL` specifies that all not matching datasets in `source` are inserted into `target`. The amount of columns must be the same for `target` and `source`.

  - The `VALUES` addition allows specifying concrete columns and values to insert. `VALUES` is preceded by a parenthesized and comma-separated list of column names (`columns_list`). It is possible to specify a single column name. Column names can only be specified once in the list. `VALUES` is followed by a parenthesized and comma-separated list of values that should be added for the specified columns (`values_expressions`). The values specified can be represented by expressions, for example, using [ABAP SQL functions](abensql_builtin_func.md). The number of values must match the number of column names specified for `columns_list`.

- Further syntax options:

  - [`%_HINTS`](abenabap_sql_db_hints.md): Specifies [database hints](../../abap-glossary/abendatabase_hint_glosry.md).

  - [`OPTIONS PRIVILEGED ACCESS`](abapselect_privileged_access.md): Disables [CDS access control](../../abap-glossary/abencds_access_control_glosry.md).

The dynamic form of the `MERGE` statement expects a parenthesized data object `dynamic_syntax`. `dynamic_syntax` can be a character-like data object or an internal table with character-like line type holding syntax of static form starting with `INTO`.

## Hints

- `MERGE` statements set system variables as follows:

  - `sy-subrc`: 0 if at least one entry in the target was updated, inserted or deleted; otherwise, the value is 4.

  - `sy-dbcnt`: The sum of all entries updated, inserted and/or deleted in the target.

- For certain column specifications and join conditions, null values can be produced. If detected by the compiler, a syntax warning occurs. In such cases, the `coalesce` function can be specified.

- Note that insert operations can lead to duplicate entries.

- The number of columns in `target` and `source` must match.

- The column names in `target` and `source` do not have to match, but the columns' types must be compatible.

- The merging process involves the following steps:

  - First, the `ON` condition is applied, which generates an implicit result set.

  - Since the `ON` condition triggers a right outer join, an entry from the source table may not have a corresponding entry in the target table.

  - If there is a match, that is, an entry exists in the target table, the `WHEN MATCHED` clause is processed. Conversely, if there is no match, that is, the entry is not available in the target table, the `WHEN NOT MATCHED` clause is processed. This evaluation occurs for each dataset returned by the `ON` condition.

  - When there is a match and `WHEN MATCHED` is processed, the optional additional conditions specified with `AND` (`match_condition1`, and so on) are evaluated. If these conditions evaluate to true, the `THEN` clause is executed (resulting in an update or delete operation). If the evaluation is false, the `THEN` clause is skipped. Note that if the `AND` condition returns false, the `WHEN NOT MATCHED` clause is not triggered for the specific result set entry.

  - The same logic applies to the `WHEN NOT MATCHED` clause. If there is no match and the additional condition with `AND` evaluates to false, the `THEN` clause (and any insert operation) is not executed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_SQL_MERGE` demonstrates a `MERGE` statement combining update and insert logic.

``` abap
MERGE INTO demo_tab_root_5 AS a USING demo_tab_root_7 AS b 
    ON a~key_field = b~key_field AND b~key_field > 0 
    WHEN MATCHED THEN UPDATE SET field1 = '#' 
    WHEN NOT MATCHED THEN INSERT ALL.
```

## Executable Example

The executable class `CL_DEMO_SQL_MERGE` shows multiple `MERGE` statements. Demo tables are populated, and the result of the individual `MERGE` operations is displayed by selecting from the database table.
