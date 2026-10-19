---
title: "dynamic external entity"
source_file: abencds_dynamic_ee_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# dynamic external entity

[CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

A [CDS external entity](abencds_external_entity_glosry.md) that does not specify a [logical external schema](abencds_logical_schema_glosry.md) in its [data definition](abencds_data_definition_glosry.md), but instead uses the addition [`PROVIDED AT RUNTIME`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_external_entity.md). The logical external schema for a dynamic external entity must be provided as a part of the [ABAP SQL](abenabap_sql_glosry.md) `SELECT` statement when accessing the external entity, using a `PROVIDED BY` clause. Dynamic external entities can only be accessed by ABAP SQL; they cannot be used as a data source for other [CDS entities](abencds_entity_glosry.md).

[***-\>* More about**](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_external_entity.md)
