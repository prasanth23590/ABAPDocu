---
title: "standard key"
source_file: abenstandard_key_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# standard key

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

[Primary table key](abenprimary_table_key_glosry.md) of an [internal table](abeninternal_table_glosry.md), whose [key fields](abenkey_field_glosry.md) in a structured [line type](abenrow_type_glosry.md) are all table fields with [character-like data types](abencharlike_data_type_glosry.md) and [byte-like data types](abenbyte_like_data_typ_glosry.md). If the line type contains [substructures](abensubstructure_glosry.md), they are broken down into elementary [components](abenstructure_component_glosry.md). The standard key for non-structured line types is the entire table line, if the line type itself is not a table type. If there are no corresponding table fields, or the line type itself is a table type, the standard key of [standard tables](abenstandard_table_glosry.md) is empty or contains no key fields.

[***-\>* More about**](../abap-programming-language/abap-data-types-and-data-objects/abenitab_standard_key.md)
