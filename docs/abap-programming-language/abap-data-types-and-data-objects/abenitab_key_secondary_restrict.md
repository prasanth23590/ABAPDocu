---
title: "itab - Restrictions for Secondary Keys"
source_file: abenitab_key_secondary_restrict.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables > itab - Table Key > itab - Secondary Table Key"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Restrictions for Secondary Keys

Internal tables with secondary keys can be used in all [processing statements for internal tables](../abap-processing-internal-data/abentable_processing_statements.md) and other statements that work with internal tables. However, there are also operand positions for internal tables where the use of secondary keys does not make sense and is therefore not supported there.

The use of tables with secondary keys causes syntax or runtime errors for the following operand positions:

- Only standard tables without secondary keys are possible for the following:

  - `rspar` in `SUBMIT WITH rspar` and `range_tab` in `SUBMIT WITH sel IN range_tab`

  - `itab` in [`FIND IN TABLE itab`](../abap-processing-internal-data/abapfind_itab.md) and [`REPLACE IN TABLE itab`](../abap-processing-internal-data/abapreplace_itab.md)

  - `result_tab` in [`SPLIT INTO TABLE result_tab`](../abap-processing-internal-data/abapsplit.md)

  - `column_syntax` in the [`SELECT` list](../abap-database-access/abapselect_list.md), in [`GROUP BY`](../abap-database-access/abapgroupby_clause.md), and in [`ORDER BY`](../abap-database-access/abaporderby_clause.md)

  - `cond_syntax` in [`WHERE`](../abap-database-access/abenwhere_logexp_dynamic.md)

  - `source_syntax` in [`SELECT`](../abap-database-access/abapfrom_clause.md)

  - `target_syntax` in [`INSERT`](../abap-database-access/abapiumd_target.md), [`UPDATE`](../abap-database-access/abapiumd_target.md), [`MODIFY`](../abap-database-access/abapiumd_target.md), and [`DELETE`](../abap-database-access/abapiumd_target.md)

  - `expr_syntax` in [`UPDATE`](../abap-database-access/abapupdate_set_expression.md)

  - `IN`, `OUT`, `INOUT` parameters in `EXEC SQL - EXECUTE`

  - `itab` in [`EXPORT TO INTERNAL TABLE itab`](../abap-data-cluster/abapexport_data_cluster_medium.md) and [`IMPORT FROM INTERNAL TABLE itab`](../abap-data-cluster/abapimport_medium.md)

  - `itab` in `GENERATE SUBROUTINE POOL itab`, `READ REPORT INTO itab`, `INSERT REPORT FROM itab`, and `SYNTAX-CHECK FOR itab`.

  - `itab` in `EDITOR-CALL FOR itab`

  - `itab` in `WRITE TO itab`
