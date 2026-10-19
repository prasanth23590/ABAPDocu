---
title: "response_param, Dynamic Forms of ABAP EML Statements"
source_file: abapeml_responses_dyn.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands > ABAP EML - response_param"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# response_param, Dynamic Forms of ABAP EML Statements

## Syntax

``` abap
... [FAILED failed_resp] 
    [MAPPED mapped_resp] 
    [REPORTED reported_resp] ...  
```

## Description

Used for [RAP responses](../../abap-glossary/abenrap_response_glosry.md) in the context of dynamic forms of ABAP EML statements. The operands `failed_resp`, `mapped_resp` and `reported_resp` after the respective ABAP word must be internal tables typed with `ABP_BEHV_RESPONSE_TAB`. All variants can be used together where possible.

They can be specified for the following dynamic ABAP EML statements:

- [`MODIFY ENTITIES OPERATIONS`](abapmodify_entities_operations_dyn.md)

- [`READ ENTITIES OPERATIONS`](abapread_entities_operations.md)

- [`COMMIT ENTITIES RESPONSES OF`](abapemlcommit_entities_dyn.md)

- [`GET PERMISSIONS OPERATIONS`](abapget_permissions_dyn.md)

- [`SET LOCKS lock_tab`](abapset_locks_dyn.md)

The internal table can be constructed inline using the declaration operators [`DATA`](../../abap-programming-language/abap-declarations/abendata_inline.md) and [`FINAL`](../../abap-programming-language/abap-declarations/abenfinal_inline.md). It contains deep structures of type `ABP_BEHV_RESPONSE` for each entity for which entries are available in the response. These structures include the following components:

| **Component** | **Details**                                                                                                                                                   | **Type**               |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `root_name`   | Specifies the name of the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md) of entity `entity_name` for which entries are available in the response.   | `ABP_ROOT_ENTITY_NAME` |
| `entity_name` | Specifies the entity's name for which entries are available in the response. This can be the root entity or associated and child entities of the root entity. | `ABP_ENTITY_NAME`      |
| `entries`     | Internal table containing the entries for which information is available.                                                                                     | `REF TO DATA`          |

## More Information

See further information and rules on response parameters in implementations of the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) in the Development guide for the ABAP RESTful Application Programming Model, section [General RAP BO Implementation Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/1040b81372d44ed38b07a409fa0e1769?version=sap_cross_product_abap).

## Executable Example

The example [ABAP EML - Responses (Dynamic Forms of ABAP EML Statements](abeneml_responses_dyn_abexa.md) demonstrates the response parameters with the dynamic forms of read and modify operations in the context of a simple managed RAP BO.
