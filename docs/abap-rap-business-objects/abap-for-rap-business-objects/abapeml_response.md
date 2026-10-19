---
title: "ABAP EML - response_param"
source_file: abapeml_response.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - response_param

## Syntax

``` abap
... [FAILED failed_resp] 
    [MAPPED mapped_resp] 
    [REPORTED reported_resp] ...  
```

## Description

Used as part of ABAP EML statements to retrieve information on the following:

- Failures, i. e. operations that could not get processed (`FAILED failed_resp`)

- Key mapping information (`MAPPED mapped_resp`)

- Returned error messages (`REPORTED reported_resp`)

The following table shows which responses are possible for the respective ABAP EML statements:

| **EML statement**                                            | `FAILED` | `MAPPED` | `REPORTED` |
|--------------------------------------------------------------|----------|----------|------------|
| [`MODIFY ENTITY, ENTITIES`](abapmodify_entity_entities.md) | X        | X        | X          |
| [`READ ENTITY, ENTITIES`](abapread_entity_entities.md)     | X        |          | X          |
| [`COMMIT ENTITIES`](abapcommit_entities.md)                | X        |          | X          |
| [`GET PERMISSIONS`](abapget_permissions.md)                | X        |          | X          |
| [`SET LOCKS`](abapset_locks_entity.md)                     | X        |          | X          |

The specification of the operands `failed_resp`, `mapped_resp`, and `reported_resp` after the respective keyword depends on the context, i. e. which forms of the ABAP EML statements are used:

- [`response_param`, Nondynamic Forms of ABAP EML Statements](abapeml_responses.md).

  Use of the response parameters with nondynamic (i. e. short or long) forms of ABAP EML statements, for example, [`MODIFY ENTITY`](abapmodify_entity_short.md) or [`MODIFY ENTITIES`](abapmodify_entities_long.md).

## Hints

- The operands `failed_resp` etc. can be constructed inline using the declaration operators [`DATA`](../../abap-programming-language/abap-declarations/abendata_inline.md) and [`FINAL`](../../abap-programming-language/abap-declarations/abenfinal_inline.md).

- If there is no response returned, for example, an operation is successful, there are no entries in the `failed_resp` parameter.

- The `reported_resp` operand contains the component [`%msg`](abapderived_types_msg.md). It is of type `REF TO if_abap_behv_message` (which contains `if_t100_dyn_msg`). If no custom implementation of this interface is required, the inherited method `new_message` (or `new_message_with_text`) can be used as a standard implementation.

- The specification of an operand for `MAPPED` is required for create operations including [UUID](../../abap-glossary/abenuuid_glosry.md) and in case of early internal numbering. It cannot be specified in external numbering scenarios. In late numbering scenarios, the [`CONVERT KEY`](abapemlcommit_entities_late.md) statement can be used. For further information, see the Development Guide for the ABAP RESTful Application Programming Model, section [Numbering](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/d85aec25222145f0b0cbbe8b02db51f0?version=sap_cross_product_abap).

- For `MODIFY` statements with the addition [`AUGMENTING`](abapmodify_aug_entity_entities.md), the additions `FAILED`, `MAPPED` or `REPORTED` cannot be used.

- When specifying the `REPORTED` response parameter for an ABAP EML `READ` request, the related [RAP state messages](../../abap-glossary/abenrap_state_mes_glosry.md) of the instances and child entities of a [CDS composition](../../abap-glossary/abencds_composition_glosry.md) are returned for the instances with the keys specified. This leads to increased runtime and, usually, retrieving the messages of the `REPORTED` response parameter for read requests is not required. If the read request is triggered by a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) and an entity instance contains a state message, the component [`%state_area`](abapderived_types_state_area.md) of the `REPORTED` response contains `%STATE` as an indicator for state messages. When using ABAP EML `READ` statements with the addition `IN LOCAL MODE` in behavior implementations, the original value of `%state_area` can be retrieved. See the example [RAP Messages: Transition and State Messages](abenrap_messages_abexa.md).

- In case of a non-dynamic ABAP EML `MODIFY` statement without the addition `IN LOCAL MODE` and without specifying the `FAILED` response parameter, it is recommended that the `FAILED` response parameter is specified and that proper error handling on the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) side is implemented. Otherwise, a syntax warning occurs, which can be suppressed using the pragma `##EML_FAILED_MISSING_OK`.

## More Information

See further information and rules on response parameters in implementations of the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) in the Development guide for the ABAP RESTful Application Programming Model, section [General RAP BO Implementation Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/1040b81372d44ed38b07a409fa0e1769?version=sap_cross_product_abap).

## Executable Example

- The example [ABAP EML - Responses](abeneml_responses_abexa.md) demonstrates response parameters using modify operations to change a simple managed RAP BO.
