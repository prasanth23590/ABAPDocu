---
title: "RAP - Behavior Definition Header, Interface BDEF"
source_file: abenbdl_bo_interface_header.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Interface Behavior Definition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Behavior Definition Header, Interface BDEF

## Syntax

``` abap
interface; 
[extensible;] 
[with managed instance filter;] 
[use draft; | use collaborative draft;] 
[use side effects;] 
[with privileged mode;] 
[foreign entity EntityName;] 
 EntityBehaviorDefinition1 [,EntityBehaviorDefinition2] [, ...] 
...  
```

[`interface`](abenbdl_impl_type.md) · [`extensible`](abenbdl_extensible.md) · [`with managed instance filter;`](abenbdl_mngd_instance_check_proj.md) · [`use draft;`](abenbdl_use_projection.md) · [`use collaborative draft;`](abenbdl_use_projection.md) · [`use side effects;`](abenbdl_use_projection.md) · [`with privileged mode;`](abenbdl_privileged_mode.md) · [`foreign entity EntityName`](abenbdl_foreign.md) · [`EntityBehaviorDefinition1`](abenbdl_define_beh_interface.md) · [`EntityBehaviorDefinition2`](abenbdl_define_beh_interface.md)

## Description

The [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) of an [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md) can project certain elements from its base BO. Defining new elements is not possible. All possible elements are listed below. The implementation type is mandatory and all other attributes are optional.

- [`interface`](abenbdl_impl_type.md): An interface BDEF must have the [implementation type](abenbdl_impl_type.md) `interface` and it must be based on a [CDS transactional interface](../../abap-glossary/abencds_projection_view_glosry.md).

- [`extensible`](abenbdl_extensible.md): If specified, [BDEF extensions](abenbdl_extension.md) are allowed. As a prerequisite, the projected BDEF must define at least one entity as [`extensible`](abenbdl_extensible.md).

- [`with managed instance filter`](abenbdl_mngd_instance_check_proj.md): Optional addition. If specified, the `WHERE` condition of the underlying [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) is evaluated when the BDEF is accessed with [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) requests from Web clients. If this addition is not specified, the `WHERE` clause is ignored. For further details, see topic [RAP - `with managed instance filter`](abenbdl_mngd_instance_check_proj.md).

- [`use draft`](abenbdl_use_projection.md): The [draft concept](abenbdl_with_draft.md) can be reused from the base BO.

  - For details on the draft concept, see topic [RAP - `with draft`](abenbdl_with_draft.md).

  - For details on the reuse, see topic [RAP BDL - use](abenbdl_use_projection.md).

- [`use collaborative draft`](abenbdl_use_projection.md): The [draft concept](abenbdl_with_coll_draft.md) can be reused from the base BO.

  - For details on the draft concept, see topic [RAP - with collaborative draft](abenbdl_with_coll_draft.md).

  - For details on the reuse, see topic [RAP BDL - use](abenbdl_use_projection.md).

- [`use side effects`](abenbdl_use_projection.md): [RAP side effects](../../abap-glossary/abenrap_side_effects_glosry.md) can be reused from the base BO.

  - For details on side effects, see topic [RAP - `side effects`](abenbdl_side_effects.md).

  - For details on the reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- [`with privileged mode`](abenbdl_privileged_mode.md): [BDEF privileged mode](../../abap-glossary/abenrap_privileged_mode_glosry.md) can be used. As a prerequisite, it must be specified in the projected BO. For details, see topic [RAP - `with privileged mode`](abenbdl_privileged_mode.md).

- [`foreign entity`](abenbdl_foreign.md): Defines a [RAP foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md), this means, an entity which is not part of the BO structure as component for the response structures, thus enabling message mapping for other BOs.

The behavior definition header is followed by one or more [entity behavior definition(s)](abenbdl_define_beh_interface.md) `EntityBehaviorDefinition1`, `EntityBehaviorDefinition2`, ... that start with `define behavior for`.

## Restrictions

- An [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) must not be specified. The syntax [`implementation in class`](abenbdl_in_class_unique.md) is not supported. An interface BDEF is a BDEF type without runtime handler.

- [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) cannot be defined explicitly. Strict checks are automatically applied.

- [`with cross associations`](abenbdl_with_cross_assoc.md) cannot be defined explicitly. Cross-BO transactional enablement is automatically applied, if specified in the underlying behavior definition.

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
