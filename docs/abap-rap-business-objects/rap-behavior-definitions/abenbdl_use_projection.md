---
title: "RAP - use, Projection and Interface BDEF"
source_file: abenbdl_use_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - use, Projection and Interface BDEF

## Syntax

``` abap
... use create [(augment[, precheck])] 
  | use update [(augment[, precheck])] 
  | use delete [(precheck)] 
  | use association _Assoc { create [(augment[, precheck])]; 
                            [with draft]|[with dependent draft;]} 
  | use action [(precheck)] ActionName 
               [RedefinedParameter] 
               [result entity ProjResultEntity] 
               [as ProjAction] 
               [external 'ExtName'] 
               [result external 'ExtResultName'] 
  | use function FunctionName 
               [RedefinedParameter] 
               [result entity ProjResultEntity] 
               [as AliasName] 
               [external ExtName] 
               [result external ExtResultName] 
  | use draft 
  | use collaborative draft 
  | use draft as dependent 
  | use etag 
  | use event EventName [RedefinedParameter] [as AliasName] 
  | use side effects 
  | use key KeyName [as AliasName] 
  | use DefaultValuesFunction ... 
  | use recommendations  
```

[`augment`](abenbdl_augment_projection.md) · [`precheck`](abenbdl_precheck.md) · [`augment`](abenbdl_augment_projection.md) · [`precheck`](abenbdl_precheck.md) · [`precheck`](abenbdl_precheck.md) · [`augment`](abenbdl_augment_projection.md) · [`precheck`](abenbdl_precheck.md) · [`with draft`](abenbdl_association.md) · [`with dependent draft`](abenbdl_association.md) · [`precheck`](abenbdl_precheck.md) · [`RedefinedParameter`](abenbdl_redefine_param.md) · [`external`](abenbdl_external.md) · [`external`](abenbdl_external.md) · [`RedefinedParameter`](abenbdl_redefine_param.md) · [`external`](abenbdl_external.md) · [`RedefinedParameter`](abenbdl_redefine_param.md) · [`use DefaultValuesFunction`](abenbdl_use_default_function.md)

### Variant

[1. `... use create ...`](abenbdl_use_projection.md#variant-1)

[2. `... use update ...`](abenbdl_use_projection.md#variant-2)

[3. `... use delete ...`](abenbdl_use_projection.md#variant-3)

[4. `... use association ...`](abenbdl_use_projection.md#variant-4)

[5. `... use action ...`](abenbdl_use_projection.md#variant-5)

[6. `... use function ...`](abenbdl_use_projection.md#variant-6)

[7. `... use draft ...`](abenbdl_use_projection.md#variant-7)

[8. `... use draft as dependent...`](abenbdl_use_projection.md#variant-8)

[9. `... use collaborative draft ...`](abenbdl_use_projection.md#variant-9)

[10. `... use etag ...`](abenbdl_use_projection.md#variant-10)

[11. `... use event ...`](abenbdl_use_projection.md#variant-11)

[12. `... use side effects ...`](abenbdl_use_projection.md#variant-12)

[13. `... use key ...`](abenbdl_use_projection.md#variant-13)

[14. `... use DefaultValuesFunction ...`](abenbdl_use_projection.md#variant-14)

[15. `... use recommendations ...`](abenbdl_use_projection.md#variant-15)

## Overview

### Description

The keyword `use` allows the reuse of [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md), [draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md), [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md), [RAP side effects](../../abap-glossary/abenrap_side_effects_glosry.md), [RAP alternative keys](../../abap-glossary/abenrap_alternative_key_glosry.md), [RAP default values functions](../../abap-glossary/abenrap_bo_defaulting_glosry.md), and [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md) from the base BDEF in a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) or [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md).

The following operations and characteristics can be reused:

- [standard operations](abenbdl_standard_operations.md)

- [operations for associations](abenbdl_association.md)

- [actions](abenbdl_action.md)

- [functions](abenbdl_function.md)

- [ETag](abenbdl_etag.md)

- [draft handling](abenbdl_with_draft.md), including [draft actions](abenbdl_draft_action.md)

- [events](abenbdl_event.md)

- [side effects](abenbdl_side_effects.md)

- [BDEF alternative keys](abenbdl_define_key.md)

- [default values functions](abenbdl_default_function.md)

A prerequisite for reuse is that the respective elements were defined in the underlying behavior definition. The behavior is realized by mapping it to the underlying behavior; no implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

Reused behavior can be enhanced. The following optional additions are available for the reused behavior: `precheck` and `augment`. Both of them require an implementation in the ABAP behavior pool. They are available only in projection BDEFs, not in interface BDEFs. These additions are documented in the following topics:

- [`precheck`](abenbdl_precheck.md)

- [`augment`](abenbdl_augment_projection.md)

For the operations and characteristics listed in this topic, no automatic inheritance takes place. They must be explicitly specified in the projection or interface BDEF. Otherwise, the respective feature is not available in the projection or interface.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF that reuses standard operations and operations for associations from its underlying base BDEF. The base BDEF is `DEMO_SALES_CDS_BUPA_2`.

``` abap
projection;
strict(2);

define behavior for DEMO_RAP_PROJECTION_CRUD
{
  use create;
  use update;
  use delete;

  use association _BuPa { create; }
}

define behavior for DEMO_RAP_PROJ_CRUD_CHILD
{
  use update;
  use delete;

  use association _Address;
}
```

The ABAP class `CL_DEMO_RAP_PROJECTION_CRUD` uses [EML](../../abap-glossary/abeneml_glosry.md) to access a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). It creates, updates, and deletes BO instances.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Projection Behavior Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/75a43d0b332a45d2a90371290488a26a?version=sap_cross_product_abap)

## Variant 1

`... use create ...`

### Description

The [standard operation `create`](abenbdl_standard_operations.md) can be reused in a projection or interface BDEF.

In a projection BDEF, the following additions can be added. Both of them require an implementation in an ABAP behavior pool.

- [`augment`](abenbdl_augment_projection.md)

- [`precheck`](abenbdl_precheck.md)

Example: see above, projection BDEF `DEMO_RAP_PROJECTION_CRUD`.

## Variant 2

`... use update ...`

### Description

The [standard operation `update`](abenbdl_standard_operations.md) can be reused in a projection or interface BDEF.

In a projection BDEF, the following additions can be added. Both of them require an implementation in an ABAP behavior pool.

- [`augment`](abenbdl_augment_projection.md)

- [`precheck`](abenbdl_precheck.md)

Example: see above, projection BDEF `DEMO_RAP_PROJECTION_CRUD`.

## Variant 3

`... use delete ...`

### Description

The [standard operation `delete`](abenbdl_standard_operations.md) can be reused in a projection or interface BDEF.

In a projection BDEF, the following addition can be added. It requires an implementation in an ABAP behavior pool.

- [`precheck`](abenbdl_precheck.md)

Example: see above, projection BDEF `DEMO_RAP_PROJECTION_CRUD`.

## Variant 4

`... use association ...`

### Description

``` abap
The transactional enabling of associations can be reused in a  projection or interface BDEF\. 
When using the statement `use association`, the read\-by\-association is implicitly enabled\. For details, refer to RAP \- Operations for Associations\.
```

Additions:

- `create`:

  Must be annotated to activate [create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) operations.

  For details refer to [RAP - Operations for Associations](abenbdl_association.md).

  Example: `use association _assoc { create; }`

  In projection BDEFs, the following additions can be added. Both of them require an implementation in an ABAP behavior pool.

  - use association \_assoc { create [`augment`](abenbdl_augment_projection.md); }

  - use association \_assoc { create [`precheck`](abenbdl_precheck.md); }

    Example: see above, projection BDEF `DEMO_RAP_PROJECTION_CRUD`.

- `with draft`:

  If [RAP draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md) is enabled in the projection or interface BDEF, associations must be draft enabled using the syntax addition `with draft`.

  Example: `use association _assoc { with draft; }`

  For details refer to [RAP - Operations for Associations](abenbdl_association.md).

- `with dependent draft`:

  The addition `with dependent draft` is used in the [principal draft BO](../../abap-glossary/abenrap_principal_draft_bo_glosry.md) of a [cross-BO association](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) scenario. The principal draft BO controls the draft functionalities of the associated [dependent draft BO](../../abap-glossary/abenrap_dependent_draft_bo_glosry.md). When the principal draft BO is set to [draft mode](../../abap-glossary/abenrap_draft_handling_glosry.md), all associated [instances](../../abap-glossary/abeninstance_glosry.md) are also set to draft. When the principal draft BO is activated, all associated instances are also activated. Prerequisites:

  - The dependent draft BO must have the statement [`use draft as dependent`](abenbdl_use_projection.md) in its [projection view](../../abap-glossary/abencds_projection_view_glosry.md) header.

  - Both BOs must be draft-enabled.

    Example: `use association _assoc { with dependent draft; }` For a complete example, see: [RAP - Dependent Draft](abenbdl_dependent_draft_abexa.md).

## Variant 5

`... use action ...`

### Description

The syntax element `use action` can be used in a projection or interface BDEF to project [actions](abenbdl_action.md), [draft actions](abenbdl_draft_action.md), [determine actions](abenbdl_determine_action.md), [copy actions](abenbdl_copy_action.md), and [reorder actions](abenbdl_reorder_action.md) from the underlying base BDEF. As a prerequisite for reuse, the respective actions, draft actions, and determine actions must be defined in the underlying behavior definition. If an [authorization concept](abenbdl_authorization.md) or [feature control](abenbdl_actions_fc.md) is specified for an action, this is automatically passed on to the projection or interface.

Additions:

- [`precheck`](abenbdl_precheck.md): A precheck can newly be added in the projection layer. An implementation in an ABAP behavior pool is required.

- [`RedefinedParameter`](abenbdl_redefine_param.md): The input or the output parameter of an action can be redefined in a projection or interface BDEF. For details, see [RAP - `RedefinedParameter`](abenbdl_redefine_param.md).

- `result entity`: If the base BDEF specifies an output parameter entity [`OutputParameter`](abenbdl_action_output_para.md) using the keyword `result entity`, the projection BDEF must specify the projection of the result entity with the syntax `result entity ProjResultEntity`. Otherwise, it may happen that the action is no longer exposed if the result entity is not included in the service.

- `as`: An action can be given a new [alias name](../../abap-glossary/abenalias_glosry.md) in the projection layer using the keyword `as`.

- [`external`](abenbdl_external.md): A new alias name for external usage in OData can be provided in the projection layer. This external name can be much longer than the alias name in ABAP and needs to be used when defining the corresponding UI annotations.

- `result external`: A new alias name for the result entity can be provided in the projection layer. This new name is exposed in the OData metadata.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF that reuses the two actions `Approve_Order` and `Reject_Order` from the underlying base BDEF. The underlying base BDEF is `DEMO_CDS_PURCH_DOC_M`.

For a detailed description of the definition and implementation of the base BO, see topic [RAP - Action](abenbdl_action1_abexa.md).

``` abap
projection;
strict(2);

define behavior for DEMO_RAP_PROJ_ACTION
{
  use create;
  use update;
  use delete;

  use action Approve_Order as Approve;

  use action Reject_Order as Reject;
}
```

The ABAP class `CL_DEMO_RAP_PROJ_ACTION` uses [EML](../../abap-glossary/abeneml_glosry.md) to access a RAP business object. It performs the action `Reject` on one entity instance.

Result: column `Status` of the respective instance is filled with `R` for `Rejected`. ![figure](images_abdoc_rejected.jpg)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An example for reusing draft actions is shown under Variant 7, `use draft`.

## Variant 6

`... use function ...`

### Description

The syntax element `use function` can be used in a projection or interface BDEF to reuse [functions](abenbdl_function.md) from the underlying base BDEF. As a prerequisite for reuse, the respective functions must be specified in the underlying behavior definition.

Additions:

- [`RedefinedParameter`](abenbdl_redefine_param.md): The input or the output parameter of a function can be redefined in a projection or interface BDEF. For details, see [RAP - `RedefinedParameter`](abenbdl_redefine_param.md).

- `result entity`: If the base BDEF specifies an output parameter entity [`OutputParameter`](abenbdl_action_output_para.md) using the keyword `result entity`, the projection BDEF must specify the projection of the result entity with the syntax `result entity ProjResultEntity`. Otherwise, it may happen that the function is no longer exposed if the result entity is not included in the service.

- `as`: A function can be given a new [alias name](../../abap-glossary/abenalias_glosry.md) in the projection layer using the keyword `as`.

- [`external`](abenbdl_external.md): A new alias name for external usage in OData can be provided in the projection layer. This external name can be much longer than the alias name in ABAP and needs to be used when defining the corresponding UI annotations.

- `result external`: A new alias name for the result entity can be provided in the projection layer. This new name is exposed in the OData metadata.

The following special rules apply to [RAP key functions](../../abap-glossary/abenrap_key_function_glosry.md):

- Reuse is possible in interface and projection BDEFs.

- As a prerequisite for reusing a key function, the [alternative key](../../abap-glossary/abenrap_alternative_key_glosry.md) it refers to must be reused using the syntax `use key KeyName`.

- Key functions are reused using the syntax `use function Name`. An alias name can be defined using `as` and an external name can be defined using `external`. No other additions are possible.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF that reuses the functions `getDetails`, `calculateTotal`, and ` calculateDiscount` from the underlying base BDEF. The underlying base BDEF is `DEMO_RAP_PROJ_FUNCTION`.

For a detailed description of the definition and implementation of the base BO, see topic [RAP - `function`](abenbdl_function_abexa.md).

``` abap
projection;
strict(2);

define behavior for DEMO_RAP_PROJ_FUNCTION
{
  use create;
  use update;
  use delete;

  use function getDetails;
  use function calculateTotal;
  use function calculateDiscount;
}
```

The ABAP class `CL_DEMO_RAP_PROJ_FUNCTION` uses [EML](../../abap-glossary/abeneml_glosry.md) to access a RAP business object. It executes all three functions and displays the content of their result structures. No [modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md) are carried out, the functions merely deliver information in their result structure without changing database entries.

Result: ![figure](images_abdoc_function.png)

## Variant 7

`... use draft ...`

### Description

[RAP draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md) can be reused with the syntax element `use draft`. As a prerequisite, the underlying RAP BO must be draft-enabled. The [draft tables](../../abap-glossary/abendraft_table_glosry.md), [draft query views](../../abap-glossary/abendraft_query_view_glosry.md) (if specified), and the [total ETag](../../abap-glossary/abenrap_total_etag_glosry.md) field are implementation details that are automatically reused and do not have to be explicitly specified in projection BDEFs and interface BDEFs. For details on RAP draft handling, see topic [RAP BDL - with draft](abenbdl_with_draft.md).

If RAP draft handling is reused, it is mandatory to explicitly reuse the draft actions using the syntax `use action` in projections BDEFs and RAP BO interfaces.

Reused associations should be explicitly draft-enabled using the syntax element `with draft`.

Example: `use association _assoc { create; with draft; }`

For further details on draft-enabled associations, see the topic [RAP BDL - operations for associations](abenbdl_association.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF that is based on the unmanaged, draft-enabled BDEF `DEMO_RAP_UNMANAGED_DRAFT_ROOT`. It reuses the RAP draft handling.

For a detailed description of the definition and implementation of the base BO, see the topic [RAP BDL - with draft](abenbdl_with_draft.md).

``` abap
projection;
strict(2);
use draft;

define behavior for DEMO_RAP_PROJECTION_DRAFT
{
  use create;
  use update;
  use delete;

  use association _child { create; with draft; }

  use action Edit;
  use action Activate;
  use action Discard;
  use action Prepare;
  use action Resume;
}

define behavior for DEMO_RAP_PROJECTION_DRAFT_CHIL
{
  use update;

  use association _parent { with draft; }
}
```

The implementation is automatically reused from the base BO.

The ABAP class `CL_DEMO_RAP_PROJECTION_DRAFT` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md) and performs the following steps:

- It creates two new draft instances of the parent entity and two new draft instances of the child entity and displays the content of the draft tables.

- Then it activates the draft entities using the draft action `Activate`. The content of the draft tables is written to the [persistent tables](../../abap-glossary/abenrap_persistent_table_glosry.md) and the draft tables are emptied.

## Variant 8

`... use draft as dependent...`

### Description

Using the statement `use draft as dependent` in a [cross-BO scenario](../../abap-glossary/abencds_cross_bo_assoc_glosry.md), [RAP draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md) can be delegated to a [principal draft BO](../../abap-glossary/abenrap_principal_draft_bo_glosry.md). This turns the respective BO into a [dependent draft BO](../../abap-glossary/abenrap_dependent_draft_bo_glosry.md). When the principal draft BO is set to draft mode, all associated instances of the dependent draft BO are also set to draft. When the principal draft BO is activated, all associated instances of the dependent draft BO are also activated.

Prerequisites:

- The [association](../../abap-glossary/abenassociation_glosry.md) to the dependent draft BO in the principal draft BO behavior definition must have the addition [`with dependent draft`](abenbdl_use_projection.md) in its declaration.

- Both BOs must be draft-enabled.

## Variant 9

`... use collaborative draft ...`

### Description

[RAP draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md) can be reused with the syntax element `use collaborative draft`. As a prerequisite, the underlying RAP BO must be enabled with [collaborative draft](../../abap-glossary/abenrap_collaborative_draft_glosry.md) capabilities. The [draft tables](../../abap-glossary/abendraft_table_glosry.md), and the [total ETag](../../abap-glossary/abenrap_total_etag_glosry.md) field are implementation details that are automatically reused and do not have to be explicitly specified in projection BDEFs and interface BDEFs. For details on RAP collaborative draft handling, see topic [RAP - with collaborative draft](abenbdl_with_coll_draft.md).

If RAP draft handling is reused, it is mandatory to explicitly reuse the draft actions using the syntax `use action` including the collaborative draft specific [draft action](abenbdl_draft_action.md) `Share` in projection BDEFs and RAP BO interfaces.

Reused associations should be explicitly draft-enabled using the syntax element `with draft`.

Example: `use association _assoc { create; with draft; }`

For further details on draft-enabled associations, see the topic [RAP BDL - operations for associations](abenbdl_association.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Collaborative Draft Handling](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/18d41e2a7be24ff99b43c4c88711e86c?version=sap_cross_product_abap).

## Variant 10

`... use etag ...`

### Description

If the base BO specifies [RAP ETag](../../abap-glossary/abenrap_etag_glosry.md) fields, these fields can be reused. The keyword `use etag` must be specified for each entity in the projection or interface BDEF individually. If it is not specified explicitly in the projection or interface BDEF, the [optimistic concurrency control](../../abap-glossary/abenoptimistic_conc_control_glosry.md) functionality is lost.

### Hint

Even in projection BDEFs without the syntax `use etag`, the value of the ETag field is updated during each modify operation. However, the syntax `use etag` enables an optimistic lock phase in an OData service. During the optimistic lock phase, on each modify request, the value of the ETag field is checked and if an OData client detects any changes in the ETag value, no data changes are possible. Any attempt to save data fails.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Optimistic Concurrency Control](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/41d72e9f31964082a7e7189f832010c3?version=sap_cross_product_abap).

## Variant 11

`... use event ...`

### Description

[RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md) can be reused in an interface BDEF.

**Caution**

Reuse is possible in interface BDEFs only. It is not possible to reuse a business event in a projection BDEF.

Additions:

- [`RedefinedParameter`](abenbdl_redefine_param.md): The input parameter of an event can be redefined in the interface BDEF. For details, see [RAP - `RedefinedParameter`](abenbdl_redefine_param.md).

- The optional addition `as` can be used to assign an [alias name](../../abap-glossary/abenalias_glosry.md) to the business event in question.

[RAP business events for side effects](../../abap-glossary/abenrap_side_effct_event_glosry.md) that are defined using the keyword [`for side effect`](abenbdl_event_side_effect.md) in the base BDEF can be reused in interface BDEFs and in projection BDEFs using the statement `use event EventName`. The optional addition `as` can be used, but no other addition.

## Variant 12

`... use side effects ...`

### Description

[RAP side effects](../../abap-glossary/abenrap_side_effects_glosry.md) can be reused in a projection BDEF and in an interface BDEF.

The syntax `use side effects` is specified in the [behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) and all side effects from all RAP BO entities of the underlying RAP BO are reused. However, if side effects are defined for BO properties, such as fields or actions, that do not appear in the projection at all, these side effects are filtered out and do not have any effect in the projection.

**Note:** If a base BO is defined as [`extensible`](abenbdl_extensible.md), the syntax `use side effects` *must* be specified in the behavior definition header of an interface BDEF or of a projection BDEF to ensure that side effects are reused, even if they are specified in an extension. Otherwise, a syntax check warning occurs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an interface BDEF that reuses the side effects from its underlying base BDEF. The base BDEF is `DEMO_RAP_SIDE_EFFECTS`.

``` abap
interface;
use draft;
use side effects;

define behavior for DEMO_RAP_SIDE_EFFECTS_I alias Root
{
  use create;
  use update;
  use delete;

  use action MyActionFC;
  use action MyAction;
  use action someDetermineAction;

  use action Edit;
  use action Activate;
  use action Discard;
  use action Resume;
  use action Prepare;
}
```

## Variant 13

`... use key ...`

### Description

[BDEF alternative keys](../../abap-glossary/abenrap_alternative_key_glosry.md) can be reused in a projection or interface BDEF. Optionally, an alias name `AliasName` can be specified using the addition `as`. The reused alternative key can then be used to define a new [key function](../../abap-glossary/abenrap_key_function_glosry.md) in a projection BDEF or for accessing an internal table using this alternative key.

## Variant 14

`... use DefaultValuesFunction ...`

### Description

[Default values functions](../../abap-glossary/abenrap_bo_defaulting_glosry.md) can be reused in a projection BDEF or in an interface BDEF. Both the operation in question and the default values function must be reused separately. For details, see the topic [RAP - `use DefaultValuesFunction`](abenbdl_use_default_function.md).

## Variant 15

`... use recommendations ...`

### Description

The syntax element `use recommendations` can be used in a projection BDEF to reuse [RAP recommendations](../../abap-glossary/abenrecommendation_glosry.md) from the underlying base BDEF.

The syntax `use recommendations` is specified in the [behavior definition header](abenbdl_bdef_projection_header.md) of the projection BDEF.

### Hint

A [RAP recommendation function](abenbdl_recommendations.md) is triggered by a side effect. To make the RAP recommendation work, side effects must also be reused in the projection BDEF.

## More Information

[*Adding RAP Recommendations*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/9d9cc97cab9d48fdaa35d5c333526ba0) in the development guide for the ABAP RESTful Application Programming Model
