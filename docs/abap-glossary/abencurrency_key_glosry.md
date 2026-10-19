---
title: "currency key"
source_file: abencurrency_key_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# currency key

[DDIC](../abap-dictionary-ddic/abenddic_glossary.md)

## Definition

Component of a [DDIC structure](abenddic_structure_glosry.md), or [DDIC database table](abenddic_db_table_glosry.md) of the type [`CUKY`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) defined in the [ABAP Dictionary](abenabap_dictionary_glosry.md). A currency key can be linked to a [currency field](abencurrency_field_glosry.md) of a structure, database table, or view. The currency key contains a [currency code](abencurrency_id_glosry.md) from the database table `TCURC`, and is used to define the currency for the currency field. By default, the number of decimal places of a currency is always two. Currencies with a different number of decimal places must be entered additionally in the table `TCURX`, where the number of decimal places can be defined explicitly.

[***-\>* More about**](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md)
