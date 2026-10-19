---
title: "ABAP CDS - CDS-managed DDIC Views"
source_file: abencds_database_view.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - CDS-managed DDIC Views

For [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) defined using the statement [`DEFINE VIEW`](abencds_define_view_v1.md) without the addition [`ENTITY`](../abap-cds-data-definitions/abencds_define_view_entity.md), a [CDS-managed DDIC view](../../abap-glossary/abencds_mngdddic_view_glosry.md) is created alongside the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) when the CDS view is activated. The CDS entity represents the actual CDS view. Properties, such as [access controls](../../abap-glossary/abencds_access_control_glosry.md) defined in CDS, can be defined for the CDS entity only. The CDS-managed DDIC view is used as a technical foundation for CDS DDIC-based views (obsolete). It is a read-only [DDIC database view](../../abap-glossary/abendatabase_view_glosry.md) in ABAP Dictionary.

The name `CDS_DB_VIEW` of the DDIC database view is defined in the [definition](abencds_define_view_v1.md) of a CDS DDIC-based view (obsolete) with the [CDS annotation](../../abap-glossary/abencds_annotation_glosry.md) `@AbapCatalog.sqlViewName`, and is located in the same namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. When the CDS view is activated, the corresponding [SQL view](../../abap-glossary/abensql_view_glosry.md) is created with the same name.

As a data type in ABAP Dictionary, the CDS-managed DDIC view represents like all DDIC database views a flat [DDIC structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md) with the [elements of the CDS](abencds_select_list_entry_v1.md) view as components. The CDS-managed DDIC view of a [client-dependent](abencds_view_client_handling_v1.md) CDS view always has a client column, unlike the CDS entity.

- In ABAP Dictionary, the CDS-managed DDIC view can be used like any [DDIC structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md), such as the type of a substructure, as an include structure, or as the row type of a table type.

- The CDS-managed DDIC view should not, however, be used in ABAP.

- In CDS DDL too, only the CDS entity should be accessed using its name `ddic_based_view` and not the CDS-managed DDIC view using the name `CDS_DB_VIEW`.

## Hints

- Accessing a CDS-managed DDIC view is [obsolete](abencds_access_obsolete.md). Instead, the CDS entity should be accessed directly.
