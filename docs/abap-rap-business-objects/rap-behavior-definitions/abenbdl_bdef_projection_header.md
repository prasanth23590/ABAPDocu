---
title: "RAP - BehaviorDefinitionHeader, Projection BDEF"
source_file: abenbdl_bdef_projection_header.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - BehaviorDefinitionHeader, Projection BDEF

## Syntax

``` abap
projection [implementation in class ClassName unique]; 
[strict[(version)];] 
[extensible;] 
[with managed instance filter;] 
[use draft;] 
[use side effects;] 
[use recommendations;] 
[with privileged mode disabling base context;] 
[foreign entity EntityName;] 
 EntityBehaviorDefinition1[,EntityBehaviorDefinition2][, ...] 
[AuthorizationContext1][, AuthorizationContext2][, ... ] 
...  
```

[`projection`](abenbdl_impl_type.md) · [`implementation in class ClassName unique`](abenbdl_in_class_unique.md) · [`strict[(version)];`](abenbdl_strict.md) · [`extensible;`](abenbdl_extensible.md) · [`with managed instance filter;`](abenbdl_mngd_instance_check_proj.md) · [`use draft;`](abenbdl_use_projection.md) · [`use side effects;`](abenbdl_use_projection.md) · [`use recommendations;`](abenbdl_use_projection.md) · [`with privileged mode disabling base context;`](abenbdl_privileged_mode.md) · [`foreign entity EntityName`](abenbdl_foreign.md) · [`EntityBehaviorDefinition1`](abenbdl_define_beh_projection.md) · [`EntityBehaviorDefinition2`](abenbdl_define_beh_projection.md) · [`AuthorizationContext1`](abenbdl_authorization_context.md) · [`AuthorizationContext2`](abenbdl_authorization_context.md)

## Description

The [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) of a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) can consist of one or more of the elements listed below. The implementation type is mandatory and all other attributes are optional.

Elements that must be specified explicitly, if required:

- [`projection`](abenbdl_impl_type.md): A projection BDEF must start with the keyword `projection` and it must be based on a [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md).

- [`implementation in class ClassName unique`](abenbdl_in_class_unique.md): In a projection behavior definition, an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is not mandatory but possible:

  - Functionality that is reused from the [projected BO](../../abap-glossary/abenrap_projection_bo_glosry.md) does not require its own implementation. The implementation from the projected BO is reused.

  - If the projection BDEF defines [new actions or functions](abenbdl_nonstandard_projection.md), an ABAP behavior pool is required.

- [`strict[(version)]`](abenbdl_strict.md): [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) can be used. As a prerequisite, it must be specified in the projected BO. The projected BO and the projection must use the same version of strict mode.

- [`extensible`](abenbdl_extensible.md): if specified, [BDEF extensions](abenbdl_extension.md) are allowed. As a prerequisite, [BDEF strict mode](abenbdl_strict.md) must be switched on. In projection BDEFs, only the keyword `extensible` is possible, without the additions described in topic [`extensible`](abenbdl_extensible.md).

- [`use draft`](abenbdl_use_projection.md): The [draft concept](abenbdl_with_draft.md) can be reused from the base BO.

  - For details on the draft concept, see topic [RAP - `with draft`](abenbdl_with_draft.md).

  - For details on the reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- [`with managed instance filter`](abenbdl_mngd_instance_check_proj.md): Optional addition for [projection BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md) and [interface BDEFs](../../abap-glossary/abencds_interface_bdef_glosry.md). If specified, the `WHERE` condition of the underlying [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) or [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) is evaluated when the BDEF is accessed with [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) requests from Web clients. If this addition is not specified, the `WHERE` clause is ignored. For further details, see topic [RAP - `with managed instance filter`](abenbdl_mngd_instance_check_proj.md).

- [`use side effects`](abenbdl_use_projection.md): [RAP side effects](../../abap-glossary/abenrap_side_effects_glosry.md) can be reused from the base BO.

  - For details on RAP side effects, see topic [RAP - `side effects`](abenbdl_side_effects.md).

  - For details on the reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- [`use recommendations`](abenbdl_use_projection.md): [RAP recommendations](../../abap-glossary/abenrecommendation_glosry.md) can be reused from the base BO.

- [`with privileged mode disabling base context`](abenbdl_privileged_mode.md): [BDEF privileged mode](../../abap-glossary/abenrap_privileged_mode_glosry.md) can be used. As a prerequisite, it must be specified in the projected BO. For details, see topic [RAP - `with privileged mode`](abenbdl_privileged_mode.md).

- [`foreign entity`](abenbdl_foreign.md): Defines a [RAP foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md), that is, an entity which is not part of the BO structure as component for the response structures, thus enabling message mapping for other BOs.

Elements that are automatically reused:

- [`with cross associations`](abenbdl_with_cross_assoc.md): Cross-BO transactional enablement is automatically reused, if specified in the underlying behavior definition.

The behavior definition header is followed by

- one or more [entity behavior definition(s)](abenbdl_define_beh_projection.md) that start with `define behavior for`

- or by the definition of one or more [authorization contexts](../../abap-glossary/abencds_auth_context_glosry.md) that start with [`define [own] authorization context`](abenbdl_authorization_context.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF based on the projected BO `DEMO_SALES_CDS_BUPA_2`. It defines the managed BDEF `DEMO_CDS_VALIDATION` as foreign entity and exposes the standard operations and associations of the underlying BO.

``` abap
projection;
strict(2);
foreign entity demo_cds_validation;
define behavior for DEMO_RAP_PROJECTION_1 alias Parent
{
  use create;
  use update;
  use delete;

  use association _BuPa { create; }
}

define behavior for DEMO_RAP_PROJECTION_1_CHILD alias Child
{
  use update;
  use delete;

  use association _Address;
}
```

Like in a RAP BO of type managed or unmanaged, the foreign entity is included in the `reported` structure: ![figure](images_foreign_in_projection.jpg)
