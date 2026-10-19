---
title: "CDS DDL - DEFINE TYPE simple_type"
source_file: abencds_define_simple_type.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE > ABAP CDS - Simple Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TYPE simple_type

## Syntax

``` abap
[@type_annot1] 
[@type_annot2] 
... 
DEFINE TYPE simple_type : dtype 
                        | data_element 
                        | simple_type  
```

[`@type_annot1`](abencds_simple_type_anno.md) · [`@type_annot2`](abencds_simple_type_anno.md) · [`dtype`](../abap-cds-data-types/abencds_overview_builtin_types.md) · [`data_element`](abencds_dtel.md) · [`simple_type`](abencds_simple_type.md)

## Description

Defines a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md). A CDS simple type defines an [elementary data type](../../abap-glossary/abenelementary_data_type_glosry.md) natively in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md).

A CDS simple type can be enriched with [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md) [`type_annot`](abencds_simple_type_anno.md). All annotations are optional and a simple type can also be created without any annotations. If specified, the type annotations must be defined in front of the statement `DEFINE TYPE`.

The name `simple_type` of the CDS simple type is defined after the `DEFINE TYPE` statement. It is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. The general rules for CDS object names described in topic [ABAP CDS - General Syntax Rules](../abap-cds-syntax/abencds_general_syntax_rules.md) apply. The name of the CDS simple type must be the same as the name of the source code.

**Typing**

A simple type can be typed as follows:

- Using a built-in ABAP Dictionary data type [`dtype`](../abap-cds-data-types/abencds_overview_builtin_types.md). All possible types and rules are described in the topic [ABAP CDS - Built-In Data Types](../abap-cds-data-types/abencds_overview_builtin_types.md).

- Using a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) [`data_element`](abencds_dtel.md). The rules, including inheritance rules, are described in topic [CDS Simple Type, `data_element`](abencds_dtel.md).

- Using another CDS simple type [`simple_type`](abencds_simple_type.md). The rules are described in topic [CDS Simple Type, `simple_type`](abencds_simple_type.md).

## Use

CDS simple types can be used in the following places:

- To type another CDS simple type.

  **Note:** The maximum nesting depth is five. This means that a stack of simple types can have a maximum of five layers, from base to top-most.

- In [cast expressions in CDS view entities](abencds_cast_expression_v2.md).

- In [cast expressions in CDS projection views](abencds_proj_view_element.md).

  **Note:** Remember that casting in CDS projection views is only possible with the addition `PRESERVING TYPE`. **Example**: `cast(ProjField as MySimpleType preserving type) as NewProjField`

- For [typing](abencds_typing.md) of elements in [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md) and in [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md).

- For [typing](abencds_typing.md) of parameters in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS analytical projection views](../../abap-glossary/abencds_analytical_pv_glosry.md), CDS custom entities, CDS abstract entities, and [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md).

- For typing of [CDS virtual elements](../../abap-glossary/abencds_virtual_element_glosry.md) in [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md).

- For [typing](abencds_scalar_typing.md) the input parameters or the return parameter of [SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md).

- In ABAP for typing data objects with the statement `TYPE`.

## Restrictions

- CDS simple types cannot be used in [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- CDS simple types cannot be used for typing in DDIC objects such as [DDIC data types](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_types.md), DDIC views, and [DDIC extensions](../../abap-glossary/abenddic_extension_glosry.md).

- Unlike DDIC data elements, there is no [search help assignment](../../abap-glossary/abensearch_help_glosry.md) available for CDS simple types.

- CDS simple types cannot be used in [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md).

## Hint

If a CDS DDIC-based views (obsolete) selects from a view entity that is typed with a simple type, then the simple type information is available in the metadata of the CDS entity, but not in the metadata of the [CDS-managed DDIC view](../../abap-glossary/abencds_mngdddic_view_glosry.md).
