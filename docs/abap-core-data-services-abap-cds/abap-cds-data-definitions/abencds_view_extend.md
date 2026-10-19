---
title: "ABAP CDS - Extending CDS Views"
source_file: abencds_view_extend.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entity Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Extending CDS Views

There are currently two different statements that can be used to extend a [CDS view](../../abap-glossary/abencds_view_glosry.md) in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md):

- [`EXTEND VIEW ENTITY`](abencds_extend_view_entity.md)

  - This variant is used to define a [CDS view entity extension](../../abap-glossary/abencds_view_entity_extend_glosry.md) for a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md).

  - Available since release 7.78.

- [`EXTEND VIEW`](abencds_extend_view.md)

  - This variant is used to define a [CDS view extension](../../abap-glossary/abencds_view_extend_glosry.md) that is also linked with a [DDIC append view](../../abap-glossary/abenddic_append_view_glosry.md) in [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md).

  - Available since release 7.40, SP08.

  - Recommended for extending [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), defined using the statement [`DEFINE VIEW`](../abap-cds-obsolete-language-elements/abencds_define_view_v1.md).

**Differences Between View Extensions and View Entity Extensions**

- A view entity extension does not have a DDIC append view.

- For a view entity extension, no name is specified after `WITH`. A view entity extension has only one name, which is the name of the [repository object](../../abap-glossary/abenrepository_object_glosry.md). This name is assigned in the wizard for creating a new repository object.

- In view entity extensions, no [header annotations](abencds_f1_entity_annotations.md) are allowed. That means that no annotations are allowed in front of the statement `EXTEND VIEW ENTITY`.

- View entity extensions were developed for CDS view entities and they have the same advantages, for example, a better performance during activation. The advantages of CDS view entities over DDIC-based views is explained in topic [ABAP CDS - DDIC-Based Entities](../abap-cds-obsolete-language-elements/abencds_ddic_entity.md).

## Hints

- For compatibility and migration reasons, `EXTEND VIEW` can also be used to extend CDS view entities and CDS projection views. Activation is possible without errors. However, the syntax elements specific to CDS view entities and CDS projection views are not supported in this variant of view extensions. It is recommended that the statement `EXTEND VIEW ENTITY` is used for CDS view entities and CDS projection views.

- CDS DDIC-based views (obsolete) are [obsolete](../abap-cds-obsolete-language-elements/abencds_ddic_entity.md). If new CDS views are required, CDS view entities should be used.
