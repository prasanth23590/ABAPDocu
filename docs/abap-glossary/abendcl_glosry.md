---
title: "DCL"
source_file: abendcl_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DCL

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md) [CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

Short for Data Control Language. A subset of [SQL](abensql_glosry.md). The statements of the DCL perform authorization and consistency checks on [relational databases](abenrelational_database_glosry.md).

- [ABAP SQL](abenabap_sql_glosry.md) does not support DCL. On an Application Server ABAP, the functionality of the [DCL](abencds_dcl_glosry.md) is implemented using [authorization objects](abenauthorization_object_glosry.md) and SAP locks.

- [ABAP CDS](abenabap_cds_glosry.md) provides a [DCL](abencds_dcl_glosry.md) that implements an [access control](abencds_access_control_glosry.md), where database objects can be linked to authorization objects of AS ABAP.
