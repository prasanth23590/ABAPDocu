---
title: "ABAP for RAP Business Objects"
source_file: abenabap_for_rap_bos.html
section: "ABAP RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP for RAP Business Objects

This section describes the ABAP language elements for providing and consuming [RAP business objects (RAP BOs)](../../abap-glossary/abenrap_bo_glosry.md). A RAP BO is mainly defined by a [RAP behavior definition (BDEF)](../../abap-glossary/abencds_behavior_definition_glosry.md). The Behavior Definition defines:

- The [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md), which can consist of [CRUD](../../abap-glossary/abencrud_glosry.md) operations and other actions.

- The provisioning type of the RAP BO that can be [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) or [unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md).

The data content of a RAP BO is stored in a [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md). The RAP BO operations work with the transactional buffer and must follow the [REST](../../abap-glossary/abenrest_glosry.md) paradigm.

- For managed RAP BOs, the transactional buffer is provided and handled as a [managed transactional buffer](../../abap-glossary/abenmanaged_trans_buff_glosry.md) by the RAP BO provider. In non-standard operations of a managed RAP BO, the managed transactional buffer can be accessed by [EML](../../abap-glossary/abeneml_glosry.md) statements.

- For unmanaged RAP BOs, the transactional buffer as well as the operations of a RAP BO must be provided by [ABAP behavior implementations](../../abap-glossary/abenbehavior_implement_glosry.md) as an [unmanaged transactional buffer](../../abap-glossary/abenunmanaged_trans_buff_glosry.md). There are no syntactical constraints on how an unmanaged transactional buffer is provided or handled, but it should fulfill the expectations of the [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md).

[RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) trigger the RAP BO operations. A RAP BO consumer is either the [RAP runtime framework](../../abap-glossary/abenrap_runt_framework_glosry.md) that handles requests from outside the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) or an ABAP program using [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md).

ABAP language contains elements for providing RAP BOs and for consuming RAP BOs:

- The language elements for providing RAP BOs are necessary for [ABAP behavior implementations](../../abap-glossary/abenbehavior_implement_glosry.md):

  - [ABAP Behavior Pools (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) are special class pools for implementing the non-standard RAP BO operations. Classes of an ABP access the transactional buffer of the RAP BO, which is either managed or unmanaged.

  - In case of a managed transactional buffer, ABAP EML must be used in the behavior implementation for accessing it. There are special EML variants that can be used in behavior implementations only.

- The language elements for accessing RAP BOs from any ABAP program are provided by the [ABAP Entity Manipulation Language (EML)](../../abap-glossary/abenaeml_glosry.md). ABAP EML statements call the operations of a RAP BO that work with the transactional buffer. The operations can be implemented by the managed RAP BO provider or in ABAP behavior implementations (unmanaged).

The following topics document the ABAP language elements for consuming and providing RAP BOs:

- [ABAP for Providing RAP Business Objects](abenabap_provide_rap_bos.md)

- [ABAP for Consuming RAP Business Objects](abenabap_consume_rap_bos.md)

- [BDEF Derived Types](abenrpm_derived_types.md)

- [ABAP for RAP Business Events](abenrap_events.md)

- [Other RAP-Related ABAP Language Elements and Topics](abenabap_rap_other.md)
