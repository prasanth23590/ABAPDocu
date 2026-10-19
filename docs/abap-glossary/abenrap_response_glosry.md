---
title: "RAP response"
source_file: abenrap_response_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP response

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

Information a [RAP BO consumer](abenrap_bo_consumer_glosry.md) is provided with by a [RAP BO provider](abenrap_bo_provider_glosry.md) via the [RAP response parameters](abenrap_response_param_glosry.md) `mapped`, `failed` and `reported` of individual [RAP handler methods](abenabp_handler_method_glosry.md) and [RAP saver methods](abenabp_saver_method_glosry.md).

Depending on the availability of these response parameters in the said methods, the information that is provided can comprise the following:

- `mapped`: Used to provided mapping information on [RAP BO instances](abenrap_bo_instance_glosry.md), for example, which key values were created for given content IDs ([`%cid`](../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_cid.md)).

- `failed`: Information for identifying the data set for which an error occurred in a RAP operation.

- `reported`: Used to exchange error messages for each entity defined in the BDEF and [not related to a specific entity](../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_other.md).
