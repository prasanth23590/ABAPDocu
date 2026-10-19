---
title: "DDIC - Table Types"
source_file: abenddic_table_types.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Table Types

A [DDIC table type](../../abap-glossary/abenddic_table_type_glosry.md) defines the data type of an [internal table](../../abap-glossary/abeninternal_table_glosry.md) in ABAP. The DDIC table type defines the following properties of an internal table:

- [Line type](../../abap-glossary/abenrow_type_glosry.md)

- The [table category](../../abap-glossary/abentable_category_glosry.md)

- The [table key](../../abap-glossary/abentable_key_glosry.md)

A program-internal object declared with reference to a table type is an internal table of this type.

- [Technical properties of table types](abenddic_table_types_tech.md)

- [Semantic properties of table types](abenddic_table_types_sema.md)

## Hints

- Unlike [data elements](abenddic_data_elements.md) and [DDIC structures](abenddic_structures.md), the sole purpose of DDIC table types is to create globally visible definitions of internal tables. DDIC table types replace the definition of internal tables in [type pools](../../abap-glossary/abentype_pool_glosry.md). DDIC table types can themselves be replaced by the declaration of internal table types in global classes and interfaces, if the context is suitable. The properties of an internal table that can be defined in the ABAP Dictionary completely match those that can be specified using the statement [`TYPES ... TABLE OF`](../../abap-programming-language/abap-declarations/abaptypes_itab.md) in ABAP programs. For more information, see the in-depth documentation about [internal tables](../../abap-programming-language/abap-processing-internal-data/abenitab.md) in the ABAP programming language.

- The name of a table type must follow the [naming rules for DDIC data types](abenddic_types_names.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The table type `SPFLI_KEY_TAB` describes a hashed table with the structured line type `SPFLI` with a unique primary key and two non-unique secondary table keys.
