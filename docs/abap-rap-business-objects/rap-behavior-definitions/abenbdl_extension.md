---
title: "RAP - BDEF Extension"
source_file: abenbdl_extension.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - BDEF Extension

A [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md) is a transportable extension of a [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md). BDEF extensions can be added to the [BDEF implementation types](../../abap-glossary/abencds_bdef_impl_type_glosry.md) [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md), [unmanaged](../../abap-glossary/abenmanaged_rap_bo_glosry.md), [projection](../../abap-glossary/abencds_proj_bdef_glosry.md), and [abstract](../../abap-glossary/abencds_abstract_bdef_glosry.md). A BDEF extension itself can be extended. This is referred to as [extension layering](../../abap-glossary/abenrap_ext_layering_glosry.md).

A BDEF extension can make additions to the original BDEF, but it cannot modify, overwrite, or delete elements from it. The following extensions are possible: field extensibility, [behavior extensibility](../../abap-glossary/abenrap_behavior_extension_glosry.md), [node extensibility](../../abap-glossary/abenrap_ext_entity_behavior_glosry.md).

- Section [Extensibility Enablement](abenbdl_extensibility_enabling.md): As a prerequisite for BDEF extensions, the behavior definition or BDEF extension to be extended must be explicitly enabled for RAP extensibility.

- Section [Base BDEF Extension](abenbdl_extensibility_managed_unm.md): All available extension features for RAP BOs of type managed and unmanaged are described.

- Section [BDEF Projection Extension](abenbdl_extensibility_projection.md): All available extension features for BDEF projections are described.

- Section [Abstract BDEF Extension](abenbdl_extensibility_abstract.md): All available extension features for abstract BDEFs are described.

A note on the terminology: the following topics use the terms *base RAP BO* and *base BDEF* to refer to RAP behavior definitions of type `managed` and `unmanaged`. A base BDEF extension is a BDEF extension that extends a RAP behavior definition of type `managed` or `unmanaged`.

*Original* is used as synonym for *extended* or to refer to BDEF components that belong to the extended RAP BO. For example, *original field* and *original operation* refers to fields and operations from the extended RAP BO. The term *original* can refer to BDEFs of any type or layer. It focuses on the contrast between *extended object* and *extension*.

Each BDEF extension automatically inherits the [release contract](../../abap-glossary/abenrelease_contract_glosry.md) of the original RAP BO. Therefore, BDEF extensions must also meet the specifications of the release contract and need to be kept stable.

## Hints

- BDEF extensions themselves and each single extension element should use a separate [namespace](../../abap-glossary/abennamespace_glosry.md) to avoid naming conflicts with extended elements. BDEF extensions created in non-SAP and non-partner development systems should use the [customer namespace](../../abap-glossary/abencustomer_namespace_glosry.md) prefix `Z` or `ZZ`.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Extend](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/492d88ed89f640e5b18dd1c57f6817b1?version=sap_cross_product_abap).

- [ABAP CDS - CDS Entity Extension](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_view_extension.md)

- CDS Service Definition Extensions ([`EXTEND SERVICE`](../../abap-core-data-services-abap-cds/abap-cds-service-definitions/abensrvd_extend_service.md)).
