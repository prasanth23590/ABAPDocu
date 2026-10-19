---
title: "fast data access"
source_file: abenfast_data_access_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# fast data access

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md) [ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

FDA for short. Protocol that allows the content of [internal tables](abeninternal_table_glosry.md) to be passed between the [Application Server ABAP](abenas_abap_glosry.md) and a [database system](abendatabase_system_glosry.md). FDA is supported by the [SAP HANA database](abenhana_database_glosry.md) and some other platforms. FDA can be switched on and off with database parameters and [database hints](abendatabase_hint_glosry.md). FDA write access is the prerequisite for [`SELECT, FROM @itab`](../abap-programming-language/abap-database-access/abapselect_itab.md) in [ABAP SQL](abenabap_sql_glosry.md). Depending on settings, FDA is also used for [`SELECT, FOR ALL ENTRIES`](../abap-programming-language/abap-database-access/abenwhere_all_entries.md).

[***-\>* More about**](https://launchpad.support.sap.com/#/notes/0002399993).
