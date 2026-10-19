---
title: "News for ABAP Release 9.17"
source_file: abennews-917.html
section: "ABAP Release News > News for ABAP Release 9.1x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 9.17

The kernel release for ABAP release 9.17 is 9.17.

## ABAP SQL

| Modification                                    | Description                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **INDICATORS Addition for Setting Null Values** | The addition `INDICATORS` can be used for [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md), [`UPDATE`](../../abap-programming-language/abap-database-access/abapupdate.md) to specify [null indicators](../../abap-glossary/abennull_indicator_glosry.md). It describes whether individual fields contain a [null value.](../../abap-programming-language/abap-database-access/abenabap_sql_null_values.md) |

## System Classes

| Modification                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System Class for Writing CSV**        | The `CL_CSV_FACTORY` system class enables the creation of instances for CSV writers. Instance methods of the CSV writer implementing the `IF_CSV_WRITER` interface allow settings to be applied and internal table content to be converted into CSV format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **System Class for Garbage Collection** | The `CL_ABAP_GARBAGE_COLLECTOR` class provides the `COLLECT` method. Calling this method manually triggers garbage collection, regardless of the current memory consumption or the garbage collector's state. Since the ABAP runtime framework periodically invokes the garbage collector, it is generally unnecessary to trigger clearing explicitly. However, it can be beneficial in exceptional cases, such as when very large, unneeded objects consume a significant amount of memory, or when explicitly releasing memory in resource-constrained environments is required. It can also aid in analyzing memory consumption and ensuring proper memory release, or when large objects are created repeatedly in a short period. |

## ABAP RESTful Application Programming Model

In release 9.17, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### ABAP EML

| Modification                                              | Description                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`WITH CHANGES` Addition to ABAP EML `READ` Statements** | The [`WITH CHANGES`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_read_with_changes.md) addition to ABAP EML `READ` statements enables access to accumulated change operation information for [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) within a [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). |

### RAP BDL

| Modification                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RAP Global Side Effects** | [RAP side effects](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_side_effects.md) are an optional part of a [RAP behavior definition](../../abap-glossary/abenrap_behavior_glosry.md) that define interdependencies among BO properties that trigger a reload of the affected properties on the user interface. Global side effects are invoked by an end user with a dedicated key stroke. It is defined using the following syntax: `side effects { determine action MyDetermineAction executed on global affects field MyField; }` |
