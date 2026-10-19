---
title: "controlled SAP LUW"
source_file: abencontrolled_sap_luw_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# controlled SAP LUW

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md) [RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

An extension of the [SAP LUW](abensap_luw_glosry.md) concept. The controlled SAP LUW introduces a checking mechanism to detect transactional consistency violations. The controlled SAP LUW is automatically and implicitly supported by newer ABAP concepts such as [RAP](abenrap_glosry.md). In non-RAP transactions, the controlled SAP LUW can be used by explicitly setting transactional phases using the static methods of the [`CL_ABAP_TX`](../abap-programming-language/abap-database-access/abaprap_cl_abap_tx.md) class. In addition, [released APIs](abenreleased_api_glosry.md) can have special classifications (starting with [`IF_ABAP_TX...`](../abap-programming-language/abap-database-access/abapapi_classification.md)) that enable specific transactional contracts that are checked in the [transactional phases](abentr_phase_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-database-access/abencontrolling_sap_luw.md)
