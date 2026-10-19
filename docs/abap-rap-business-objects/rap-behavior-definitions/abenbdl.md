---
title: "RAP - BDL for Behavior Definitions"
source_file: abenbdl.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - BDL for Behavior Definitions

[RAP behavior definitions](../../abap-glossary/abencds_behavior_definition_glosry.md) are created using the behavior definition language [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) in [BDL source code](../../abap-glossary/abenbdl_source_code_glosry.md).

The general syntax rules for the RAP BDL are described in the topic [RAP BDL - General Syntax Rules](abenbdl_general_syntax_rules.md).

A list of all available BDL language elements can be found in topic [RAP BDL - Feature Tables](abenrap_feature_table.md).

RAP BDL offers the following statements for different [implementation types](../../abap-glossary/abencds_bdef_impl_type_glosry.md):

- `managed`

  The [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) and the [standard BO operations](abenbdl_standard_operations.md) are handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). In a managed RAP BO, a ready-to-run business object can work without [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). As soon as [non-standard operations](abenbdl_nonstandard.md), [validations](abenbdl_validations.md), [determinations](abenbdl_determinations.md), or other implementation-relevant syntax elements are added, an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is necessary. Recommended for development scenarios in which all essential parts are developed from scratch, without a large amount of existing code (so-called *greenfield* development) with standard implementation. See also: [managed RAP business object](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- `unmanaged`

  The [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) and the [standard BO operations](abenbdl_standard_operations.md) must be implemented in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). Recommended for development scenarios in which business logic already exists and is intended to be reused (so-called *brownfield* development). See also: [unmanaged RAP business object](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- `interface`

  Defines the behavior of a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), which serves as interface for stable consumption and is typically released as [released API](../../abap-glossary/abenreleased_api_glosry.md). See also: [RAP interface behavior definition](../../abap-glossary/abencds_interface_bdef_glosry.md).

- `projection`

  A RAP projection behavior definition is based on a [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) or [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) and represents a direct projection of its base behavior definition. It exposes a subset of the [base behavior definition's](../../abap-glossary/abenrap_base_bdef_glosry.md) operations and characteristics. In a business application, a projection BDEF provides means to define service-specific behavior for a BO projection. See also: [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md)

- `abstract`

  A RAP abstract behavior definition mainly serves as typing mechanism for deep action or function parameters. Only a limited range of syntax elements is available, such as associations and type mapping. It is not possible to define any transactional behavior in an abstract behavior definition. See also: [RAP abstract behavior definition](../../abap-glossary/abencds_abstract_bdef_glosry.md)

Managed and unmanaged RAP BOs share a common set of keywords. These keywords are listed in section [RAP BDL - managed and unmanaged behavior definitions](abenbdl_rap_bo.md).

RAP projection behavior definitions reuse elements of the underlying base BDEF. Section [RAP BDL - RAP projection behavior definitions](abenbdl_projection_bo.md) explains which elements, such as characteristics and operations, can be reused under which conditions and which characteristics and operations can be newly added to RAP projection behavior definitions.

RAP abstract behavior definitions offer only a limited range of behavior definition elements, such as associations and type mapping. It is not possible to define any transactional behavior in an abstract behavior definition. Section [RAP BDL - RAP abstract behavior definitions](abenbdl_abstract.md) explains which elements are available in abstract BDEFs.

RAP BOs can be extended using [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md). The rules for BDEF extensions are described in the topic [RAP - BDEF Extension](abenbdl_extension.md).
