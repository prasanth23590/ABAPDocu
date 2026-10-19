---
title: "RAP persistent table"
source_file: abenrap_persistent_table_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP persistent table

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

The [DDIC database table](abenddic_db_table_glosry.md) a [RAP BO](abenrap_bo_glosry.md) is based on. For transactional changes of RAP persistent table data, the data is loaded into the [transactional buffer](abentransactional_buffer_glosry.md). At the end of a [RAP transaction](abenrap_luw_glosry.md), changes in the transactional buffer are either written back to the persistent table (commit) or discarded (rollback).

[***-\>* More about**](../abap-rap-business-objects/rap-behavior-definitions/abenbdl_persistent_table.md)
