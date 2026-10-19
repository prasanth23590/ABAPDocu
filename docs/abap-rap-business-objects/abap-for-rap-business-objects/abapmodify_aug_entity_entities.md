---
title: "ABAP EML - MODIFY AUGMENTING ENTITY, ENTITIES"
source_file: abapmodify_aug_entity_entities.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP EML - Providing RAP BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - MODIFY AUGMENTING ENTITY, ENTITIES

## Syntax

``` abap
MODIFY AUGMENTING { ENTITY bdef 
                      operations [RELATING TO orig BY rela] } 
                | { ENTITIES OF bdef 
                      ENTITY bdef1 operations [RELATING TO orig BY rela] 
                     [ENTITY bdef2 operations [RELATING TO orig BY rela]] 
                     [...] }.  
```

[`operations`](abapmodify_entity_entities_op.md) · [`operations`](abapmodify_entity_entities_op.md) · [`operations`](abapmodify_entity_entities_op.md)

### Alternative

[1. `MODIFY AUGMENTING ENTITY ...`](abapmodify_aug_entity_entities.md#alternative-1)

[2. `MODIFY AUGMENTING ENTITIES OF ...`](abapmodify_aug_entity_entities.md#alternative-2)

### Addition

[`... RELATING TO orig BY rela`](abapmodify_aug_entity_entities.md#addition)

## Overview

### Description

A special variant of [`MODIFY ENTITY, ENTITIES`](abapmodify_entity_entities.md) that is only possible in the context of [projections](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_view_as_projection.md). The variant can only be used by a [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) and is used to manipulate the request for the [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md) in the handler implementation. Only entities of the base BO can be modified by this statement. All [standard operations](../../abap-glossary/abencrud_glosry.md) are allowed including actions.

### Hints

- For the statements, no [`response parameters`](abapeml_response.md) can be specified, i.e. the additions `FAILED`, `MAPPED` or `REPORTED` cannot be used.

- An ABAP EML `MODIFY` statement using the addition `AUGMENTING` must not overwrite fields of the original request, i. e. there must not be a flag in `%control` which is set for the same instance and field both in the original and in the augmenting operation. An ABAP EML `MODIFY` statement using the addition `AUGMENTING` containing operations on instances which are not contained in the original request should relate these instances to instances of the original request by use of the `RELATING` clause so that responses can be associated.

## More Information

- [RAP BDL - `augment`, projection BDEF](../rap-behavior-definitions/abenbdl_augment_projection.md)

- Development guide for the ABAP RESTful Application Programming Model, section [Operation Augmentation](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/346c2b7516ce4176bbb4daebaa80c2ca?version=sap_cross_product_abap).

## Alternative 1

`MODIFY AUGMENTING ENTITY ...`

### Description

Short form. Used to manipulate the request for the [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md) in the handler implementation. `bdef` must be the full name, i. e. not the alias name, of the projected root BO. Multiple operations can be specified for [operations](abapmodify_entity_entities_op.md) within a single `MODIFY` statement. However, in this case, it must be ensured that the importing parameters for the corresponding methods are available.

## Alternative 2

`MODIFY AUGMENTING ENTITIES ...`

### Description

Long form. Used to manipulate the request for the base BO in the handler implementation including one or more RAP BO entities. `bdef` must be the full name, i. e. not the alias name, of the projected root BO.

`bdef` must be the full name, i. e. not the alias name, of the projected root BO followed by a list of operations grouped by individual entities. `bdef1`, `bdef2`, and so on, must be entities contained in the [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) of the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md) `bdef`. The root entity itself can also be inserted in the position of `bdef1`, for example. Each part of the list of operations specified after `MODIFY AUGMENTING ENTITIES OF bdef` has the same syntax as the short form. At least one entry (`ENTITY bdef/bdef1/...` with an operation) must be specified. The same entity can be specified after `ENTITY` repeatedly, however, the same operation in that combination is allowed only once. `operations` must be specified as outlined in the topic [`operations`](abapmodify_entity_entities_op.md).

## Addition

`... RELATING TO orig BY rela`

### Description

Used to relate augment instances to original instances. When the augmented request is passed to the base handler, it may return `FAILED` instances. If this happens for new instances that are not contained in the original request but added by the augment exit, it may be problematic for the consumer to relate these responses to the actual request. The runtime uses this information to transform `FAILED` keys of new instances back to the keys of the related original instances which the consumer can be expected to handle.

Each operation can be followed by this clause. If the reference to instances from the original request is given through identical keys or `%cid_ref`, an explicit specification of the `RELATING` addition is not required.

In the example code below, `orig1` (the same is true for `orig2`) is an original instance table (i. e. the input for the augment exit), and `rela1` is a variable of type `ABP_BEHV_RELATING_TAB` that is a standard table of integers. The number of lines in `augm1` and `rela1` must be equal. All entries in `rela1` must be integers between *0* and `lines( orig1 )`. A violation of these conditions leads to a runtime error. If the entry in `rela1` is an integer greater than *0*, for example, *2*, it means that the second entry in `augm1` is related to the second entry in `orig1`. If the entry is *0*, it means that an entry in `augm1` is not related to an entry in `orig1`, for example, because it is an original instance. It is possible that many augment instances are related in this way to the same original instance.

If augmentations are needed with the same operation, for example `CREATE`, but with instances relating to different original tables, it can be achieved by splitting the augmentation in several `MODIFY AUGMENTING` statements. If an instance from `augm1` fails, for example when trying to lock it or when processing the base handler, the related `orig1` instance is included in the `FAILED` response of the overall request. If the failure occurs when locking, the related `orig1` instance is not passed to the base handler.

### Hint

Create requests on the projection layer, augmented by a create or create-by-association operation, only include the [`%cid`](abapderived_types_cid.md) values from the original create request in the [`mapped` response](abapeml_response.md). `%cid` values generated from the augmentations are not included in the `mapped` response of the original request.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following statement shows the pattern of an ABAP EML `MODIFY` statement with the `AUGMENTING` and `RELATING` additions.

``` abap
MODIFY AUGMENTING ENTITY ... 
  CREATE FROM augm1 RELATING TO orig1 BY rela1 
  UPDATE FROM augm2 RELATING TO orig2 BY rela2 ...
```

## Executable Examples

- The example [ABAP EML - `MODIFY ENTITY AUGMENTING`](abeneml_modify_augmenting_abexa.md) demonstrates the addition `AUGMENTING` with a RAP projection business object.

- The example [ABAP EML - `MODIFY AUGMENTING`, `RELATING TO`](abeneml_modify_augm_relating_abexa.md) demonstrates the `RELATING TO` addition.
