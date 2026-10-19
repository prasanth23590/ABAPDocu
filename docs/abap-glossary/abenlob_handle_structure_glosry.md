---
title: "LOB handle structure"
source_file: abenlob_handle_structure_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOB handle structure

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md)

## Definition

The [structure](abenstructure_glosry.md) of a special [work area](abenwork_area_glosry.md) to support [streaming](abenstreaming_glosry.md) and [locators](abenlocator_glosry.md) for [LOBs](abenlob_glosry.md) in [ABAP SQL](abenabap_sql_glosry.md). LOB handle structures have the same components as [DDIC database tables](abenddic_db_table_glosry.md) or [CDS entities](abencds_entity_glosry.md). However, there is at least one component which is assigned to a LOB, which is not a [string](abenstring_glosry.md) but instead a [LOB handle component](abenlob_handle_component_glosry.md). A LOB handle structure can be defined component by component with [ABAP statements](abenabap_statement_glosry.md) or in the [ABAP Dictionary](abenabap_dictionary_glosry.md), or it can be derived by referencing a structure that contains [LOBs](abenlob_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-declarations/abaptypes_lob_handle.md)
