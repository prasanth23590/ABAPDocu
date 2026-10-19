---
title: "COMMIT ENTITIES, IN SIMULATION MODE"
source_file: abapcommit_entities_simulation.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > COMMIT ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COMMIT ENTITIES, IN SIMULATION MODE

## Syntax

``` abap
COMMIT ENTITIES ... IN SIMULATION MODE ...  
```

## Description

Optional addition of [`COMMIT ENTITIES`](abapcommit_entities.md) statements that allows a RAP transaction to be checked. It processes the [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md) only and without actually saving data. A final [`COMMIT WORK`](../../abap-programming-language/abap-database-access/abapcommit.md) is not implicitly included with this variant. The consistency of the transaction can be checked by evaluating the value of `sy-subrc` as a result of executing the commit in simulation mode.

**Use Case**

A use case of COMMIT ENTITIES statements with the addition IN SIMULATION MODE might be as follows:

- A non-RAP application modifies data. It needs to persist the data and has its own save logic. Furthermore, it is responsible for the final saving of data from within an [SAP LUW](../../abap-glossary/abenluw_glosry.md), i. e. once the SAP LUW is finalized with [`COMMIT WORK`](../../abap-programming-language/abap-database-access/abapcommit.md).

- If other RAP implementations are involved and part of the SAP LUW before this `COMMIT WORK`, for example, due to new features added or due to a redesign or refactoring, it must be ensured that the overall SAP LUW is consistent with regards to saving.

- RAP implementations whose save sequence is usually triggered with a `COMMIT ENTITIES` statement, i. e. without the addition `IN SIMULATION MODE`, process the complete save sequence automatically including the actual saving. This might lead to inconsistencies because of a potentially incomplete execution of `COMMIT WORK` while the RAP BOs are already saved with a `COMMIT ENTITIES` statement.

- Similarly, inconsistencies can occur if data gets saved from a non-RAP application first and then RAP BOs cannot be saved due to issues. A complete checking of all involved data is not possible.

- To overcome these potential inconsistencies, the addition `IN SIMULATION MODE` of the `COMMIT ENTITIES` statement simulates the saving of the RAP BOs to check the consistency and whether issues occur.

- If there are no issues with saving the RAP BOs (indicated by the value 0 of `sy-subrc` following the statement), the saving of all involved (RAP and non-RAP) components from within the SAP LUW can be executed using `COMMIT WORK` that is triggered by the non-RAP application.

- If problems show up following the consistency check (indicated by a value other than 0 of `sy-subrc` following the statement), the overall implementation can react and avoid the final saving of data at the end of the SAP LUW with `COMMIT WORK`.

For general hints on using the statement see the topic [`COMMIT ENTITIES`](abapcommit_entities.md).
