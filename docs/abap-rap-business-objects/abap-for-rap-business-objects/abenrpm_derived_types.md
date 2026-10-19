---
title: "BDEF Derived Types"
source_file: abenrpm_derived_types.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# BDEF Derived Types

[BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) are special data types within the RAP context. The types are derived by the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) from [CDS entities](../../abap-glossary/abencds_entity_glosry.md) and their behavior definition in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). In ABAP, BDEF derived types are used to provide type-safe access to RAP BOs. As an essential part of RAP, internal tables and structures that are typed with BDEF derived types are used for the communication and to exchange data between [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) and [RAP BO providers](../../abap-glossary/abenrap_bo_provider_glosry.md), thus, enabling mass processing of data.

Each BDEF derived type can be categorized as input or output (result) derived type according to its use as import or export parameter in methods of [RAP BO providers](../../abap-glossary/abenrap_bo_provider_glosry.md). For example, the types `... FOR CREATE ...` or `... FOR UPDATE ...` are used for providing input; `... FOR READ RESULT ...`, `... FOR ACTION RESULT ...` or `... FOR FAILED ...` are used to return a result.

Internal tables and structures that are typed with BDEF derived types contain components of CDS entities like key and data fields that retain their original data type. Yet, BDEF derived types also contain additional RAP components that do not derive their data type from the entity. They have special, tailor-made types that provide additional information required in the context of transactional processing. The names of those RAP components begin with `%` to avoid naming conflicts with components of the CDS entities. Among the components, there are [component groups](../../abap-glossary/abencomponent_group_glosry.md) available summarizing groups of table columns under a single name. In doing so, they simplify the handling of derived types for developers. For example, `%key` summarizes all primary keys. For details on the components, see the topic [Components of BDEF Derived Types](abapderived_types_comp.md).

The parameters of [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md) are mainly typed with BDEF derived types. Derived types can also be used outside of those operations in ABAP programs using [ABAP EML](../../abap-glossary/abenaeml_glosry.md). They can be [explicitly declared](abapderived_types_declaration.md) using a variable, for example, with the statements `TYPES`, `DATA` and `CREATE`.

Derived types can be declared using the following variants:

- [`TYPE TABLE FOR`](abaptype_table_for.md)

- [`TYPE STRUCTURE FOR`](abaptype_structure_for.md)

- [`TYPE REQUEST FOR`](abaptype_request_for.md)

- [`TYPE RESPONSE FOR`](abaptype_response_for.md)

## Hint

BDEF derived types are created automatically and are known only to the ABAP compiler. For example, the element information for a variable typed with a BDEF derived type can be called by choosing F2 in ADT to display the components.
