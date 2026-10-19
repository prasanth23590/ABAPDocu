---
title: "RAP response parameter"
source_file: abenrap_response_param_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP response parameter

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

Implicit changing parameters of [RAP handler methods](abenabp_handler_method_glosry.md) and [RAP saver methods](abenabp_saver_method_glosry.md) (implicitly) typed with the [BDEF derived type](abenrap_derived_type_glosry.md) [`... TYPE RESPONSE FOR ...`](../abap-rap-business-objects/abap-for-rap-business-objects/abaptype_response_for.md). Depending on the RAP handler or saver method, the signatures of the individual methods can include all of the following three formal parameters `mapped`, `failed` and `reported`, a subset or none of them. The names of the parameters are predefined. They are used to provide a [RAP BO consumer](abenrap_bo_consumer_glosry.md) with information by a [RAP BO provider](abenrap_bo_provider_glosry.md).

Parameters:

- `failed`: Information for identifying the data set for which an error occurred in a RAP operation

- `reported`: Used to exchange messages (for example, error messages) for each entity defined in the BDEF and [not related to a specific entity](../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_other.md).

- `mapped`: Used to provide mapping information on [RAP BO instances](abenrap_bo_instance_glosry.md), for example, which key values were created for given content IDs ([`%cid`](../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_cid.md)).
