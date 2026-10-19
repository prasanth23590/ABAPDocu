---
title: "RAP business object"
source_file: abenrap_bo_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP business object

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

RAP BO for short. A [business object](abenbusiness_object_glosry.md) in the context of [ABAP RAP](abenabap_rap_glosry.md). A RAP BO is mainly described by a [RAP behavior definition](abencds_behavior_definition_glosry.md) that defines the [RAP business object behavior](abenrap_bo_behavior_glosry.md) for a set of special hierarchical [CDS entities](abencds_entity_glosry.md) in form of RAP behavior operations and behavior characteristics. A RAP BO has [RAP BO operations](abenrap_bo_operation_glosry.md) to handle its data that is available in a [transactional buffer](abentransactional_buffer_glosry.md). There are two kinds of RAP BOs:

- [Managed RAP BOs](abenmanaged_rap_bo_glosry.md) that are fully or partly provided by the [managed RAP BO provider](abenmanaged_rap_bo_prov_glosry.md)

- [Unmanaged RAP BOs](abenunmanaged_rap_bo_glosry.md) that are provided by the [unmanaged RAP BO provider](abenunmanaged_rap_bo_prov_glosry.md) that is implemented in an [ABAP behavior implementation](abenbehavior_implement_glosry.md).

- [BOPF-based RAP business objects](abenrap_bopf_bo_glosry.md) that are provided by the [BOPF-managed RAP BO provider](abenbopf_man_rap_bo_prov_glosry.md).

A RAP BO can be exposed as a [RAP business service](abenbusiness_service_glosry.md) for access from outside [AS ABAP](abenas_abap_glosry.md) and is consumed by the [RAP transactional engine](abenrap_transac_engine_glosry.md) then. For access to RAP BOs from inside AS ABAP, ABAP contains a subset called [ABAP Entity Manipulation Language (EML)](abenaeml_glosry.md).
