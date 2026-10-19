---
title: "News for ABAP Release 9.18"
source_file: abennews-918.html
section: "ABAP Release News > News for ABAP Release 9.1x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 9.18

The kernel release for ABAP release 9.18 is 9.18.

## ABAP CDS

| Modification                            | Description                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CDS Propagated Buffers Are Obsolete** | [CDS propagated buffer](../../abap-glossary/abencds_prop_buffer_glosry.md), defined using the statement [`PROPAGATE VIEW ENTITY BUFFER ON`](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_propagate_buffer.md), are obsolete. When creating new data models, it is no longer the case that performance gains are to be gained by using propagated buffers, so they can be left out of future models. |

## ABAP SQL

| Modification            | Description                                                                                                                                                                                    |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New Keyword `MERGE`** | The [`MERGE`](../../abap-programming-language/abap-database-access/abapmerge_dbtab.md) keyword is now available in ABAP SQL. Using `MERGE`, insert, update, and delete operations can be done on a data source by evaluating another data source. |

## ABAP RESTful Application Programming Model

In release 9.18, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RAP Recommendations** | [RAP recommendations](../../abap-glossary/abenrecommendation_glosry.md) are an enhancement to value helps, adding context-aware suggestions through a deterministic approach or leveraging artificial intelligence. In the [behavior definition](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl.md), a source and a target field need to be defined. To define the RAP recommendation itself, the function must be embedded in a [side effect](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_side_effects.md). The recommended values can then be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). |

## ABAP Doc

| Modification                                  | Description                                                                                                        |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **ABAP Doc Comments for Inline Declarations** | It is now possible to add [ABAP Doc comments](../../abap-programming-language/abap-syntax-elements-of-an-abap-program/abendoccomment.md) to inline declarations with `DATA` and `FINAL`. |

## System Classes

| Modification                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System Class for Weak References** | The `CL_ABAP_WEAK_OBJECT_REFERENCE` system class enables the use of weak references in ABAP Cloud. Objects of the `CL_ABAP_WEAK_OBJECT_REFERENCE` class represent weak references to an object. Unlike regular object references, weak references do not keep the referenced object alive. If the Garbage Collector is running and the referenced object is accessible only through a weak reference, the object is released. |
