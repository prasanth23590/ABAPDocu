---
title: "exclusive lock"
source_file: abenexclusive_lock_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# exclusive lock

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

[Lock](abenlock_glosry.md) that does not allow other users to set simultaneous locks for the exclusively locked data. The [ABAP SQL](abenabap_sql_glosry.md) statements [`INSERT`](../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`DELETE`](../abap-programming-language/abap-database-access/abapdelete_dbtab.md), [`MODIFY`](../abap-programming-language/abap-database-access/abapmodify_dbtab.md), and [`UPDATE`](../abap-programming-language/abap-database-access/abapupdate.md), [`SELECT`](../abap-programming-language/abap-database-access/abapselect.md) with the addition [`FOR UPDATE`](../abap-programming-language/abap-database-access/abapselect_single.md), and all corresponding statements in [AMDP methods](abenamdp_method_glosry.md) set corresponding [database locks](abendatabase_lock_glosry.md) on the rows they address.
