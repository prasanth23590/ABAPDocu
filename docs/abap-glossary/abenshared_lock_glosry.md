---
title: "shared lock"
source_file: abenshared_lock_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# shared lock

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

[Lock](abenlock_glosry.md) that allows other users to set further shared locks but no simultaneous [exclusive locks](abenexclusive_lock_glosry.md) for the locked data. The [ABAP SQL](abenabap_sql_glosry.md) statement [`SELECT`](../abap-programming-language/abap-database-access/abapselect.md) without the addition [`FOR UPDATE`](../abap-programming-language/abap-database-access/abapselect_single.md) do not set such a [database lock](abendatabase_lock_glosry.md) for the addressed lines by default.
