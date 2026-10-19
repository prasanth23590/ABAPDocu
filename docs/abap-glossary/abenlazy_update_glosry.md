---
title: "lazy update"
source_file: abenlazy_update_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# lazy update

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Procedure to create or update non-unique [secondary table keys](abensecondary_table_key_glosry.md) in [internal tables](abeninternal_table_glosry.md). Non-unique secondary tables keys are not updated straight after insert operations using [`INSERT`](../abap-programming-language/abap-processing-internal-data/abapinsert_itab.md) or [`APPEND`](../abap-programming-language/abap-processing-internal-data/abapappend.md), a block operation in which the whole table body is filled at once, or after a modifying operation using [`MODIFY`](../abap-programming-language/abap-processing-internal-data/abapmodify_itab.md), [field symbols](abenfield_symbol_glosry.md), or [data references](abendata_reference_glosry.md). They are updated at the next explicit usage. See also [direct update](abendirect_update_glosry.md) and [delayed update](abendelayed_update_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-data-types-and-data-objects/abenitab_key_secondary_update.md)
