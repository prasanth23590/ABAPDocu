---
title: "database commit"
source_file: abendatabase_commit_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# database commit

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

End of a [database LUW](abendatabase_luw_glosry.md), in which changed data records are written to the [database](abendatabase_glosry.md). All changes are temporary until they have been written using a database commit. Changes are always directly visible to the executing program. The [database system](abendatabase_system_glosry.md) that is used determines whether other users can see the database changes immediately or only after the database commit. In [AS ABAP](abenas_abap_glosry.md), database commits are triggered implicitly, as well as by explicit requests.

[***-\>* More about**](../abap-programming-language/abap-database-access/abendb_commit.md)
