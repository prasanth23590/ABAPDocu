---
title: "transactional contract"
source_file: abentransactional_contract_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# transactional contract

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Specifies which ABAP statements and operations are allowed and which are not allowed in a [transactional phase](abentr_phase_glosry.md). The following transactional contracts are available, each of which specifies restrictions to ensure transactional consistency: `SAVE`, `MODIFY`, `FUNCTIONAL`, `SURFACE`, `READ`, `COMPLETE`. The `SAVE` and `MODIFY` contracts are implicitly enabled in both transactional phases.

The transactional contracts can be set explicitly by [API classifications](../abap-programming-language/abap-database-access/abapapi_classification.md) (starting with `IF_ABAP_TX...`, for example, `IF_ABAP_TX_SAVE`). In the [controlled SAP LUW](abencontrolled_sap_luw_glosry.md) and when in a transactional context, transactional contracts are checked.

For example, an API contains database changes and has the classification `IF_ABAP_TX_SAVE`. The classification ensures that the API is not called in the modify [transactional phase](abentr_phase_glosry.md) by causing a violation that is either logged or results in a [runtime error](abenruntime_error_glosry.md).
