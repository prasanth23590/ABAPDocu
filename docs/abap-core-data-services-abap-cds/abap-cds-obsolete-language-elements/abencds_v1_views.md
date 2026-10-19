---
title: "ABAP CDS - DDIC-Based Views (Obsolete)"
source_file: abencds_v1_views.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - DDIC-Based Views (Obsolete)

A [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) is defined for existing [DDIC database tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables.md), or other [CDS SQL entities](../../abap-glossary/abencds_sql_entity_glosry.md) using the statement [`DEFINE VIEW`](abencds_define_view_v1.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of [ABAP Core Data Services (CDS)](../abencds.md) in the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a [CDS data definition](../../abap-glossary/abencds_data_definition_glosry.md) in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md).

When a CDS data definition of a CDS DDIC-based view (obsolete) is activated, two artefacts are created:

- a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) is created as a repository object

- a [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) is created in the ABAP Dictionary.

The CDS entity represents the CDS view and the view should be accessed using the name of the CDS entity. The name of the CDS entity is defined after the [`DEFINE VIEW`](abencds_define_view_v1.md) keyword. The definition of the CDS entity occurs only as DDL source code. As a global data type, the CDS entity represents a structured type with the [elements of the CDS view](abencds_select_list_entry_v1.md) as components and can be used like any [CDS entity](../../abap-glossary/abencds_entity_glosry.md).

- In ABAP CDS, the CDS entity can be used as a data source of other CDS entities.

- In ABAP programs, the CDS entity can be used as a data type and in ABAP SQL read statements.

- The CDS entity cannot be used as a data type for definitions of [dictionary objects](../../abap-glossary/abendictionary_object_glosry.md).

The name of this CDS entity is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

The keyword [`KEY`](abencds_select_list_entry_v1.md) can be used to define key elements in CDS views. If the name of the CDS entity is used to access a CDS view in ABAP SQL, this key is used for the syntax check or the extended program check.

The following sections describe client handling and table buffering for CDS DDIC-based views (obsolete) plus the role of a CDS-managed DDIC view (obsolete):

- [Client handling](abencds_view_client_handling_v1.md)

- [Table buffering](abencds_v1_buffering.md)

- [CDS-managed DDIC view (obsolete)](abencds_database_view.md)

## Hints

- The programming of CDS views using the DDL of the Core Data Services is one of the tasks included in the implementation of data models and is not usually the responsibility of regular ABAP application programmers. Once created, CDS views are used in ABAP programs using ABAP SQL read statements and must be stable enough to allow this.

- CDS views can be extended with [CDS view extensions](../../abap-glossary/abencds_view_extend_glosry.md). These extensions are stored in separate entities, so the CDS view itself is not modified.
