---
title: "data federation"
source_file: abendata_federation_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# data federation

[General](abenabap_glossary.md)

## Definition

An approach to [data integration](abendata_integration_glosry.md) where data in a source system is accessed from consumer systems or applications in real-time. Data is not moved or copied to a centralized repository. Data remains in its source system and all requests are forwarded and run on the original data. Data federation is used in scenarios where live access to the source system is required, for example, when access to the most recent data is needed.

The [SAP HANA database](abenhana_database_glosry.md) uses data federation as a part of its [SAP HANA Smart Data Access](abensap_hana_sda_glosry.md) technology to access and query data from other (remote) enterprise data stores.

In ABAP CDS, access to the federated data of an external system is supported by [CDS external entities](abencds_external_entity_glosry.md).

See also: [Data replication](abendata_replication_glosry.md)
