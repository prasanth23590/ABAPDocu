---
title: "release contract"
source_file: abenrelease_contract_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# release contract

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

Classification of a [repository object](abenrepository_object_glosry.md) that is a prerequisite for its usability as an [released API](abenreleased_api_glosry.md). A release contract ensures a certain stability regarding consistency and compatibility of released APIs.

There are currently the following release contracts:

- [C0 contract, release](abenc0_contract_glosry.md), which allows enhancement fields to be added at specified extension options.

- [C1 contract, use system-internally](abenc1_contract_glosry.md), which guarantees a stable interface for use within the [AS ABAP](abenas_abap_glosry.md)

- [C2 contract, use as remote API](abenc2_contract_glosry.md), which also guarantees a stable interface for use outside the AS ABAP.

- [C3 contract, manage configuration content](abenc3_contract_glosry.md), which ensures a stable persistence for configuration content.

- [C4 contract, use in ABAP-Managed Database Procedures](abenc4_contract_glosry.md), which guarantees a stable interface of [AMDP methods](abenamdp_method_glosry.md) for use in other AMDP methods.

Objects are classified in [ADT](abenadt_glosry.md) or using special transactions.

[***-\>* More about**](../abap-apis/release-contracts/abenabap_release_contracts.md)
