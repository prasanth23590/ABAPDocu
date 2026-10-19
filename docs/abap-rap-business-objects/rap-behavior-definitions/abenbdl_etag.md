---
title: "RAP - etag"
source_file: abenbdl_etag.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - etag

## Syntax Forms

**ETag for Active Data**

``` abap
        etag master MasterField 
| etag dependent by _Assoc 
```

**ETag for Draft Data**

``` abap
       total etag TotalEtagField
```

### Variant

[1. `... etag master MasterField`](abenbdl_etag.md#variant-1)

[2. `... etag dependent by _Assoc`](abenbdl_etag.md#variant-2)

[3. `... total etag TotalEtagField`](abenbdl_etag.md#variant-3)

## Overview

### Description

Defines a field as entity tag ([ETag](../../abap-glossary/abenrap_etag_glosry.md)) field for [optimistic concurrency control](../../abap-glossary/abenoptimistic_conc_control_glosry.md). A field flagged as ETag field is used to describe, uniquely, the state of a requested resource (for example a specific [entity instance](../../abap-glossary/abenrap_bo_entity_inst_glosry.md)). Any changes made to the requested resource update the ETag field. On each change request, the value of the ETag field is compared to the value the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) sends with the request and only if these values match is the change request accepted. This way, inconsistencies and unintentional changes of data are prevented when multiple users work on the same data.

- `etag master` and `etag dependent` can optionally be used for the [persistent data](../../abap-glossary/abenrap_persistent_data_glosry.md) of a business object. They are defined at entity-level in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) for each [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) separately. If an entity is an [ETag master entity](../../abap-glossary/abenrap_etag_ma_ent_glosry.md), it has its own ETag field. An [ETag dependent entity](../../abap-glossary/abenrap_etag_dep_ent_glosry.md) uses the ETag field of another entity for optimistic concurrency control.

- `total etag` is available for [draft-enabled business objects](abenbdl_with_draft.md) only and for these, it is mandatory. It manages the transitions from active data to draft data and vice versa.

In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), optimistic concurrency control with ETag fields can be handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md), so that no implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required. This is only possible if the following prerequisites are met:

- The ETag field must be updated reliably with every change on the [RAP BO entity instance](../../abap-glossary/abenrap_bo_entity_inst_glosry.md).

- The read access to the ETag master field from every entity that uses this particular ETag field must be guaranteed.

In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), the handling of the ETag fields must be implemented in the ABAP behavior pool.

## Availability

- Managed RAP BO

- Unmanaged RAP BO

- `total ETag` is available in draft-enabled RAP BOs only and for these, it is mandatory.

- In a [projection](../../abap-glossary/abencds_proj_bdef_glosry.md) or [interface](../../abap-glossary/abencds_interface_bdef_glosry.md) BDEF, the optimistic concurrency control functionality can be reused with the keyword `use etag`. For details, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

### Hints

- In draft-enabled RAP BOs, [total ETag](../../abap-glossary/abenrap_total_etag_glosry.md) and `ETag master/dependent` complement each other and it is recommended that both are used together. Depending on the use case, separate fields or identical fields can be used as total ETag field and ETag master field.

- The RAP framework offers reuse data elements that can be used as ETag and total ETag fields. For more information, see [RAP Reuse Data Elements](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/84bd58e2b9354be4a7a1c91cb687815c?version=sap_cross_product_abap).

- In scenarios where the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md) handles the ETag fields, it is recommended that you specify the respective fields as read-only using the field characteristic [`readonly`](abenbdl_field_char.md).

- In an [unmanaged RAP business object](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), it is recommended that the ETag fields are handled during the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Optimistic Concurrency Control](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/41d72e9f31964082a7e7189f832010c3?version=sap_cross_product_abap).

## Variant 1

`... etag master MasterField`

### Description

Defines an entity as [RAP ETag master entity](../../abap-glossary/abenrap_etag_ma_ent_glosry.md) and assigns a field `MasterField` for change logging. The following rules apply:

- An ETag master field is optional.

- One or more RAP BO entities can be defined as ETag master entities and have an ETag master field assigned. RAP BO entities on each level of the CDS composition tree can be ETag master entities.

- `MasterField` can have any data type that can be converted into the data type [`string`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) (see the topic [Assignment and Conversion Rules](../../abap-programming-language/abap-processing-internal-data/abenconversion_rules.md) for details).

- In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), a value for the total ETag field can be provided automatically if the following conditions are met:

  - The ETag master field `MasterField` must be annotated in CDS with the annotation [`@Semantics.systemDateTime.localInstanceLastChangedAt: true`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_425922347-_anno.md)

  - The data type must be [`utclong`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), `TIMESTAMP`, or `TIMESTAMPL`.

- In [unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), the application developer must ensure that a value is provided for the ETag master field.

### Hints

- The same field can be used as ETag master field `MasterField` and as total ETag field `TotalEtagField`.

- In an [unmanaged RAP business object](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), it is recommended that the ETag fields are handled during the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md).

## Variant 2

`... etag dependent by _Assoc`

### Description

Defines an entity as [RAP ETag dependent entity](../../abap-glossary/abenrap_etag_dep_ent_glosry.md). This means that this entity does not have its own ETag field and uses the ETag field of the ETag master entity. The following rules apply to ETag dependent entities:

- The association `_Assoc` to the ETag master entity must be explicitly read-enabled in the entity behavior body using the syntax:

  `association _Assoc { }`

  This association must also be defined in the underlying CDS data model.

- The ETag master entity must be higher in the [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) than its dependent entities.

### Hint

The following syntax short form is available to summarize lock dependent, ETag dependent, and authorization dependent:

`([lock][, authorization][, etag]) dependent by _Assoc`

For details, see the topic [RAP - `SyntaxShortForm`](abenbdl_short_syntax.md).

## Variant 3

`... total etag TotalEtagField`

### Description

Defines a field `TotalEtagField` as [total ETag field](../../abap-glossary/abenrap_total_etag_glosry.md) for [draft-enabled scenarios](abenbdl_with_draft.md) to enable optimistic concurrency checks during the transition from draft to persistent data. If a user edits data in draft mode and returns after the exclusive lock of their editing session has expired, the total ETag checks whether the persistent data has been changed during the period of absence. Each time the persistent state is changed, the total ETag field is updated. To resume a draft version, the infrastructure first compares the total ETag of the persistent and the draft version and only if both values are identical the draft can be resumed.

The following rules apply:

- A total ETag field is mandatory for [draft-enabled RAP BOs](../../abap-glossary/abendraft_rap_bo_glosry.md).

- The total ETag field must be defined directly after the lock master entity [`lock master`](abenbdl_locking.md).

- The total ETag field is defined in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) of the [lock master entity](../../abap-glossary/abenrap_lock_ma_ent_glosry.md) and it controls all RAP BO entities of the current RAP BO.

- `TotalEtagField` can have any data type that can be converted into the data type [`string`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) (see the topic [Assignment and Conversion Rules](../../abap-programming-language/abap-processing-internal-data/abenconversion_rules.md) for details). Additionally, it can have a length of maximally 40 characters.

- In a managed RAP BO, a value for the total ETag field can be provided automatically if the following conditions are met:

  - The field `TotalEtagField` must be annotated in CDS with the annotation [`@Semantics.systemDateTime.lastChangedAt: true`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_1631854850-_anno.md)

  - The data type must be [`utclong`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), `TIMESTAMP`, or `TIMESTAMPL`.

- In unmanaged RAP BOs, the application developer must ensure that a value is provided for the total ETag field `TotalEtagField`.

### Hints

- The same field can be used as ETag master field `MasterField` and as total ETag field `TotalEtagField`.

- In an [unmanaged RAP business object](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), it is recommended that the total ETag field is handled during the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md).

## More Information

For further details, see topic [Total ETag](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/f5e8548c241b43ab82bceec030b5dc9a?version=sap_cross_product_abap) in the development guide for the ABAP RESTful Application Programming Model.
