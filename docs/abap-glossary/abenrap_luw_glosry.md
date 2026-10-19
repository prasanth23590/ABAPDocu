---
title: "RAP transaction"
source_file: abenrap_luw_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP transaction

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A RAP transaction ...

- is the sum of all operations and workflows that are used to transfer data from one consistent state to another.

- begins with creating new data on the [RAP transactional buffer](abentransactional_buffer_glosry.md) or by retrieving data from the database to the transactional buffer.

- is terminated with [`COMMIT ENTITIES`](../abap-rap-business-objects/abap-for-rap-business-objects/abapcommit_entities.md) or [`ROLLBACK ENTITIES`](../abap-rap-business-objects/abap-for-rap-business-objects/abaprollback_entities.md).
