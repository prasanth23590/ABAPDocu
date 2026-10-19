---
title: "DDIC - Structures"
source_file: abenddic_structures.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Structures

A [DDIC structure](../../abap-glossary/abenddic_structure_glosry.md) defines a [structured type](../../abap-glossary/abenstructured_type_glosry.md) that contains other data types as components. These components can be:

- Elementary data types

- Reference types

- Structured types

- Table types

The name of a DDIC structure must follow [naming rules for DDIC types](abenddic_types_names.md) and additionally some special [naming rules for DDIC structures](abenddic_structures_names.md).

A DDIC structure that contains other structures as components is called a [nested structure](../../abap-glossary/abennested_structure_glosry.md). Structured components are [substructures](../../abap-glossary/abensubstructure_glosry.md) and substructures can themselves be nested. A structure that contains a string type, reference type, or table type as a direct or nested component is a [deep structure](../../abap-glossary/abendeep_structure_glosry.md). A structure that contains only elementary data types (except string types) as direct or nested components is a [flat structure](../../abap-glossary/abenflat_structure_glosry.md). A program-internal object declared with reference to a structure is a data object structured correspondingly (or [structure](../../abap-glossary/abenstructure_glosry.md) for short).

- [Technical properties of structures](abenddic_structures_tech.md)

- [Semantic properties of structures](abenddic_structures_sema.md)

A DDIC structure can be included in another structure as an [include structure](abenddic_include_structure.md), with the components of the included structure being added as the components of the including structure.

Structures can be defined as source-code-based structures using [dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md). The following section is a summary of the syntax of the source code-based definition:

- [Dictionary DDL for Structure Definitions](abenddic_define_structure.md)

## Hints

- A [CDS entity](../../abap-glossary/abencds_entity_glosry.md) ([CDS view](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_v1_views.md), [CDS table function](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_table_functions.md), [CDS hierarchy](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_hierarchies.md), or [CDS abstract entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_abstract_entities.md)) also represents a structured type and can be used as such in ABAP programs but not in the ABAP Dictionary.

- [Mesh types](../../abap-glossary/abenmesh_type_glosry.md) cannot currently be defined in the ABAP Dictionary.

- DDIC structures can be released for [developer extensibility](../../abap-glossary/abendev_extensibility_glosry.md) under the [C0 release contract](../../abap-glossary/abenc0_contract_glosry.md).

- The data types of [DDIC database tables](../ddic-database-tables/abenddic_database_tables.md) are all flat (not nested) structures.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The structure `SOADDRESS` for the address of a SAPoffice user is a nested structure with substructures.
