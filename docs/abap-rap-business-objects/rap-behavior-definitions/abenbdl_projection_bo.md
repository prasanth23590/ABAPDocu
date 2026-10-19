---
title: "RAP - Projection Behavior Definitions"
source_file: abenbdl_projection_bo.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Projection Behavior Definitions

[RAP projection behavior definitions](../../abap-glossary/abencds_proj_bdef_glosry.md) are created using the behavior definition language [RAP BDL](../../abap-glossary/abencds_ddl_glosry.md) in [BDL source code](../../abap-glossary/abenbdl_source_code_glosry.md).

A [RAP projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md) prepares a business object for a specific business service. The projection enables flexible service consumption as well as role-based service design. In RAP, a projection BO consists of CDS projection views, [RAP projection behavior definitions](../../abap-glossary/abencds_proj_bdef_glosry.md), and, if needed, additional or consumption-specific implementations.

To obtain a RAP projection business object, a projection layer must be created for some or all of the nodes of the CDS view model. Afterwards, a projection behavior definition can be created for the CDS root projection view. This projection behavior definition represents a projection of the underlying base BDEF of type [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) or [unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md). It exposes a subset of the base BO's elements.

The following image shows the role of RAP projection behavior definitions for a [business service](../../abap-glossary/abenbusiness_service_glosry.md). ![figure](images_projection_bdef.jpg)

## Hint

A RAP projection behavior definition can also be built on top of a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md). See the topic [RAP - Interface Behavior Definition](abenbdl_rap_bo_interface.md) for further details.
