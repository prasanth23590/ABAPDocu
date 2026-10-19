---
title: "ABAP CDS - Type Definitions"
source_file: abencds_tdl.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Type Definitions

[CDS type definitions](../../abap-glossary/abencds_type_definition_glosry.md) are defined in the CDS data definition language ([CDS DDL](../../abap-glossary/abencds_ddl_glosry.md)) of [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) using the statement [`DEFINE TYPE`](abencds_define_type.md). The following [CDS user-defined types](../../abap-glossary/abencds_user_defined_type_glosry.md) are available:

- [CDS simple types](../../abap-glossary/abencds_simple_type_glosry.md) for defining [elementary data types](../../abap-glossary/abenelementary_data_type_glosry.md).

- [CDS enumerated types](../../abap-glossary/abencds_enum_type_glosry.md) for defining [enumerated types](../../abap-glossary/abenenum_type_glosry.md).

When source code with a CDS type definition is activated, the CDS type is created in form of a metadata representation in system tables. The CDS types themselves are not transported. Instead they are created after the transport of a DDL source code when this code is activated in the target system. Each CDS type is defined in a separate piece of DDL source code in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md). In the development tools, CDS types are only visible as CDS definitions in their DDL source code. The [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) and other frameworks access the internal metadata of CDS types. For example, the ABAP runtime framework recognizes a CDS type as a [global type](../../abap-glossary/abenglobal_type_glosry.md). Therefore, the name of a CDS type must be unique.

CDS types can be enriched with metadata using [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md).

CDS types can be released as stable APIs under the following release contracts:

- [C1 contract, system internal use](../../abap-glossary/abenc1_contract_glosry.md)

- [C2 contract, use as remote API](../../abap-glossary/abenc2_contract_glosry.md)

For details, see the topic [Contract Checks for Released APIs](../../abap-apis/release-contracts/abenrestricted_apis_atc_checks.md).

The following sections describe the possible CDS types and the associated syntax:

- [CDS simple types](abencds_simple_types.md)

- [CDS enumerated types](abencds_enumeration_types.md)

## Hints

- CDS types are in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

- Once a CDS type has been activated, its name is stable and cannot be changed.

- The source code of a type definition for a CDS type is edited in a different editor than the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a [CDS data definition](../../abap-glossary/abencds_data_definition_glosry.md), the [DDLA source code](../../abap-glossary/abenddla_source_code_glosry.md) of a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md), the [DDLX source code](../../abap-glossary/abenddlx_source_code_glosry.md) of a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md), and the [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md) of a [CDS role](../../abap-glossary/abencds_role_glosry.md) for [CDS access control](../../abap-glossary/abencds_access_control_glosry.md). The [ADT](../../abap-glossary/abenadt_glosry.md) documentation describes how to create the different types of source code.

- [CDS metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md) are not supported for CDS types. If required, metadata extensions can be added to a CDS type when the simple type is used in another CDS object, such as a CDS view entity.
