---
title: "DDIC - Include Structures"
source_file: abenddic_include_structure.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Include Structures

Components of a structure can be defined by including the components of other DDIC structures, including DDIC database tables or DDIC views. These included structures are referred to as include structures or includes for short. From a technical perspective, the structure in which an include structure is included refers to the included structure and is modified accordingly whenever changes are made to the included structure. An include structure can itself contain include structures, with the maximum nesting depth being nine includes.

When an include structure is included, all of its components are added to the encompassing structure. No substructure is created, which means that the components are inserted as if they were specified individually at this position and they are handled like directly defined components. Regular components and include structures can be combined as required.

When a structure is included as an include structure, it can be assigned a group name and a three-character suffix.

- In ABAP programs, the group name is an additional addressing option for data objects declared with reference to the structure. All components of the included structure form a [component group](../../abap-glossary/abencomponent_group_glosry.md) and can be addressed together using this name or individual components can be addressed using the structure component selector (`-`) after the name.

- A suffix is added to each individual component's name to avoid naming conflicts. The original name of an include structure that is included in an encompassing structure must not exceed 27 characters.

Group names and suffixes are assigned in the same way as with the additions `AS name [RENAMING WITH SUFFIX suffix]` of the statement [`INCLUDE TYPE`](../../abap-programming-language/abap-declarations/abapinclude_type.md) in ABAP programs. Unlike in the statement `INCLUDE TYPE`, an include structure in the ABAP Dictionary can have a suffix without a specified name.

The fields of an include structure still belong to the include structure. They can only be edited by modifying the included structure and any changes made to the included structure affect all including structures. The fields of an included structure can, however, also be transformed to direct fields of the including structure. These fields are then no longer linked with the originally included structure.

The components of an include structure can be assigned [check tables](abenddic_structures_sema.md) and [search helps](abenddic_structures_sema.md) in the context of the including structure. These assignments extend the components of the included structure or replace existing assignments.

## Hints

- Including structures is highly error-prone due to possible naming conflicts between components, particularly in the case of subsequent extensions to the included structure. If possible, substructures should be used instead. If this is not possible, for example, in [DDIC database tables](../ddic-database-tables/abenddic_database_tables.md), suffixes should be used to avoid naming conflicts.

- Including structures should not be confused with the inheritance of components as provided by the ABAP Dictionary tool. Inheritance means that the definition of a component is simply copied to a different structure and there is no link to the original structure. Similarly, an existing include can be resolved to individual component definitions.

- The name of a group is just an additional addressing option and does not resolve any naming conflicts. In particular, group names in statements like [`MOVE-CORRESPONDING`](../../abap-programming-language/abap-processing-internal-data/abapmove-corresponding.md) or [`SELECT INTO CORRESPONDING`](../../abap-programming-language/abap-database-access/abapinto_clause.md) are ignored. Components renamed with a suffix, on the other hand, are renamed for real.

- Group names must not be used in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) when [specifying a column](../../abap-programming-language/abap-database-access/abenabap_sql_columns.md).

- A [CDS entity](../../abap-glossary/abencds_entity_glosry.md) (such as a [CDS view](../../abap-glossary/abencds_entity_glosry.md), [CDS table function](../../abap-glossary/abencds_table_function_glosry.md), or a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md)) cannot be included as an include structure. A [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a [CDS DDIC-based view](../../abap-glossary/abencds_v1_view_glosry.md) cannot be included either, because its usage is [obsolete](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_access_obsolete.md) since ABAP release 7.85.

- If you assign a group name and suffix to an include, the suffix is added to all component names within the include. This includes components of nested includes. If you specify only a suffix without a group name, the suffix is added only to the components of the include itself, not to those of nested includes. Adding, deleting, or changing a group name for an include with a suffix is an incompatible change. It can lead to data loss if the named include is used in database tables.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The structure `DEMO_WEEK` includes the structure `DEMO_DAY` five times as an include structure with group names and suffixes. The class `CL_DEMO_INCLUDE_STRUCTURE` shows how its components can be accessed in ABAP.
