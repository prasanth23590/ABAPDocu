---
title: "direct update"
source_file: abendirect_update_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# direct update

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Procedure to create or update unique [secondary table keys](abensecondary_table_key_glosry.md) of [internal tables](abeninternal_table_glosry.md). After an insertion operation using [`INSERT`](../abap-programming-language/abap-processing-internal-data/abapinsert_itab.md) or [`APPEND`](../abap-programming-language/abap-processing-internal-data/abapappend.md), a modifying operating using [`MODIFY`](../abap-programming-language/abap-processing-internal-data/abapmodify_itab.md), or a block operation in which the whole table body is filled in one go, unique secondary table keys are updated immediately. See also [delayed update](abendelayed_update_glosry.md) and [lazy update](abenlazy_update_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-data-types-and-data-objects/abenitab_key_secondary_update.md)
