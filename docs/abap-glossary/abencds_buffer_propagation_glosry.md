---
title: "CDS buffer propagation"
source_file: abencds_buffer_propagation_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS buffer propagation

[CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

Buffer propagation means that the joins defined by a [CDS association](abencds_association_glosry.md) are processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng_glosry.md) on data stored in the [table buffer](abentable_buffer_glosry.md). Instead of using joins instantiated on the [SAP HANA database](abenhana_database_glosry.md), temporary joins for processing the table buffer are established on the [AS ABAP](abenas_abap_glosry.md). This can lead to performance gains.

[***-\>* More about**](../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_propagate_buffer.md)
