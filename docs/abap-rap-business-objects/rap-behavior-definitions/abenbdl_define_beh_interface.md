---
title: "RAP - EntityBehaviorDefinition, Interface BDEF"
source_file: abenbdl_define_beh_interface.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Interface Behavior Definition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - EntityBehaviorDefinition, Interface BDEF

## Syntax

``` abap
define behavior for ProjectedEntity [alias AliasName] [ external ExternalName] 
[use etag] 
{ 
  EntityBehaviorBody 
} 
 
[behavior for ChildEntity1][, behavior for ChildEntity2][, ... 
]  
```

[`external`](abenbdl_external.md) · [`use etag`](abenbdl_use_projection.md) · [`EntityBehaviorBody`](abenbdl_body_interface.md)

## Description

Defines the behavior for a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md) in the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md). An interface behavior definition can project a subset or all of the nodes of its underlying [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md). The [root entity](../../abap-glossary/abenroot_entity_glosry.md) `ProjectedEntity` must be a [CDS transactional interface](../../abap-glossary/abencds_projection_view_glosry.md).

Syntax additions and components:

- An alias name should be specified using the keyword `alias`. This name can be clearer than the entity name itself, since it does not need to be uniquely global in [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md). The length of an alias name `AliasName` is restricted to 30 characters. If no alias name is specified, a syntax check warning occurs.

- The optional addition [`external`](abenbdl_external.md) can be used to provide an alias name for external usage. This external name can be used, for example, if another projection layer is built on top of the interface BDEF. It can be much longer than the alias name.

- Only one [entity behavior characteristic](../../abap-glossary/abencds_entity_properties_glosry.md) is available, namely [`use etag`](abenbdl_use_projection.md). An ETag field for [optimistic concurrency control](../../abap-glossary/abenoptimistic_conc_control_glosry.md) can be reused if it is specified in the base BO.

  - For details on optimistic concurrency control, see topic [RAP BDL - ETag](abenbdl_etag.md).

  - For details on reuse, see topic [RAP BDL - use](abenbdl_use_projection.md).

- The [entity behavior body](abenbdl_body_interface.md) `EntityBehaviorBody` can expose a subset of the transactional behavior or the base BDEF, for example, [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md).

## Hint

The following entity behavior characteristics are reused automatically, if applicable, and therefore must not be defined again in an interface:

- [RAP authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) for [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md).

- [RAP persistent table](../../abap-glossary/abenrap_persistent_table_glosry.md)

- [RAP draft table](../../abap-glossary/abendraft_table_glosry.md)

- [`SavingOptions`](abenbdl_saving.md)

- [RAP locking](../../abap-glossary/abenrap_locking_glosry.md): Interfaces inherit the lock master and lock dependent relations. Upon each modify operation on an interface instance, the method [`FOR LOCK`](../abap-for-rap-business-objects/abaphandler_meth_lock.md) is called and the respective entities are locked.

- [RAP change documents](../../abap-glossary/abenrap_change_documents_glosry.md)

- [RAP early numbering](../../abap-glossary/abenrap_early_numbering_glosry.md)

- [RAP late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an interface BDEF. The projected BO is `DEMO_RAP_UNMANAGED_DRAFT_ROOT`. The interface BDEF reuses draft handling and standard operations from the underlying BO. It also defines a foreign entity and excludes a field from the BDEF derived types.

``` abap
interface;
use draft;
foreign entity demo_cds_validation;
define behavior for DEMO_RAP_INTERFACE_DRAFT alias Root
use etag
{
  use create;
  use update;
  use delete;

  use action Activate;
  use action Discard;
  use action Edit;
  use action Resume;
  use action Prepare;

  field(suppress) DataFieldRoot;

}
```
