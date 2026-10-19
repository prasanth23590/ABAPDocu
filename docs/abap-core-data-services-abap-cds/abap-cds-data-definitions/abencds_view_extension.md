---
title: "ABAP CDS - CDS Entity Extension"
source_file: abencds_view_extension.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - CDS Entity Extension

A [CDS entity extension](../../abap-glossary/abencds_entity_extend_glosry.md) is a transportable extension of a CDS entity. A CDS entity extension can make additions to the original entity, but it cannot modify, overwrite, or delete elements from the original entity. There are currently four different statements that can be used to extend a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md):

- [`EXTEND VIEW ENTITY`](abencds_extend_view_entity.md)

  - This variant is used to define a [CDS view entity extension](../../abap-glossary/abencds_view_entity_extend_glosry.md) for a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md).

  - Available since release 7.78.

- [`EXTEND CUSTOM ENTITY`](abencds_extend_custom_entity.md)

  - This variant is used to define a [CDS custom entity extension](../../abap-glossary/abencds_cus_entity_extend_glosry.md) for a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md).

  - Available since release 7.89.

- [`EXTEND ABSTRACT ENTITY`](abencds_extend_abstract_entity.md)

  - This variant is used to define a [CDS abstract entity extension](../../abap-glossary/abencds_abs_entity_extend_glosry.md) for a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md).

  - Available since release 7.84.

- [`EXTEND VIEW`](abencds_extend_view.md)

  - This variant is used to define a [CDS view extension](../../abap-glossary/abencds_view_extend_glosry.md) that is also linked with a [DDIC append view](../../abap-glossary/abenddic_append_view_glosry.md) in [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md).

  - Available since release 7.40, SP08.

  - Recommended for extending [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), defined using the statement [`DEFINE VIEW`](../abap-cds-obsolete-language-elements/abencds_define_view_v1.md).

When working in a [restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md), extensions are possible only to [released APIs](../../abap-glossary/abenreleased_api_glosry.md) that are released under the [C0 stability contract for extensions](../../abap-glossary/abenc0_contract_glosry.md).

## Hints

- Since release 7.78, there are two different statements available that can be used to extend a [CDS view](../../abap-glossary/abencds_view_glosry.md), namely `EXTEND VIEW` and `EXTEND VIEW ENTITY`. The differences and when to use what is explained in topic [ABAP CDS - Extending CDS views](abencds_view_extend.md).

- Every CDS entity extension has its own [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md). The DDL source code in a CDS entity extension is edited in a different editor from the DDL source code of the base entity. The ADT documentation describes how these types of source code are created.
