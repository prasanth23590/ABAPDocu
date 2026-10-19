---
title: "DDIC - Technical Properties of Structures"
source_file: abenddic_structures_tech.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Technical Properties of Structures

A DDIC structure describes a [structure type](../../abap-glossary/abenstructured_type_glosry.md) that consists of components and has the following technical properties:

- **Component name**

  The name of a component can have a maximum of 30 characters, can consist of only letters, numbers, and underscores, and must start with a letter or a [namespace prefix](../../abap-glossary/abenname_space_prefix_glosry.md). The following restrictions apply:

  - A component name cannot be the name of the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` reserved in ABAP.

  - If a structure is to be included in a [database table](../ddic-database-tables/abenddic_database_tables.md), the components must not be given any of the reserved names that are forbidden in DDIC database tables.

- **Component type**

  - For elementary components, the technical properties ([built-in data type](../ddic-built-in-data-types/abenddic_builtin_types.md), length, and any decimal places) are defined with reference to a [data element](abenddic_data_elements.md) for an elementary DDIC type or directly in the structure component. In the case of [DDIC currency fields](../../abap-glossary/abenddic_currency_field_glosry.md) and [DDIC quantity fields,](../../abap-glossary/abenddic_quantity_glosry.md) a [reference field](abenddic_structures_sema.md) must be specified for the unit.

  - For reference-like components, the technical properties are defined using a reference to a [data element](abenddic_data_elements.md) that describes a reference type or defined directly in the structure component. When specified directly, data references can be defined by reference to any DDIC data type or to the generic type `DATA`. Object references can be defined by reference to classes or interfaces in the class library or to the generic type `OBJECT`,

  - Substructures are defined by reference to [DDIC structures](abenddic_structures.md), [DDIC database tables](../ddic-database-tables/abenddic_database_tables.md), or DDIC views. A substructure can be defined as a [static box](../../abap-glossary/abenstatic_box_glosry.md). In ABAP data objects declared with reference to the DDIC structure, a static box supports [initial value sharing](../../abap-glossary/abeninitial_value_sharing_glosry.md).

  - Tabular components are defined by reference to a [DDIC table type](abenddic_table_types.md).

- **Enhancement category**

  The [enhancement category](abenddic_structures_enh_cat.md) of a structure specifies how a structure can be extended using [customizing includes](../../abap-glossary/abencustomizing_include_glosry.md) or [append structures](../../abap-glossary/abenappend_structure_glosry.md) and affects how ABAP programs that work with data objects of this structure type are checked.

- **Activation type**

  An [activation type](../ddic-database-tables/abenddic_database_tables_act_type.md) can be defined for a structure, like for DDIC database tables, but has no specific use here.

## Hints

- In ABAP, the component names of structures are not strictly speaking a [technical type property](../../abap-glossary/abentechnical_type_prpt_glosry.md). They are listed here however to simplify the picture.

- The above rules for component names are checked strictly by the ABAP Dictionary only for table fields of DDIC database tables and not for structures. Component names of structures can contain special characters such as a colon `:` that prevent the component from being addressed in an ABAP program. For this reason, only those component names should be used that comply with the above rules.

- A substructure cannot be defined using a reference to a [CDS entity](../../abap-glossary/abencds_entity_glosry.md), nor using a reference to a [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The latter has been possible before, but since ABAP release 7.85, access to CDS-managed DDIC views is [obsolete](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_access_obsolete.md).
