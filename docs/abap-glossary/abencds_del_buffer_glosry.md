---
title: "CDS delegated buffer"
source_file: abencds_del_buffer_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS delegated buffer

[CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

A [CDS view entity buffer](abencds_entity_buffer_glosry.md) that delegates the buffer usage from one CDS entity to its base entity, which avoids numerous entries of the same data in the memory of the [AS ABAP](abenabap_glossary.md). This can improve performance.

Defined using the syntax [`TYPE DELEGATED`](../abap-core-data-services-abap-cds/abap-cds-tuning-objects/abencds_define_delegated_buffer.md) in the definition of a CDS entity buffer.

[***-\>* More about**](../abap-core-data-services-abap-cds/abap-cds-tuning-objects/abencds_define_delegated_buffer.md)
