---
title: "primary table key"
source_file: abenprimary_table_key_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# primary table key

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Each [internal table](abeninternal_table_glosry.md) has a primary [table key](abentable_key_glosry.md) that is either a user-defined key or the [standard key](abenstandard_key_glosry.md). In [hashed tables](abenhashed_table_glosry.md), the primary key is a [hash key](abenhash_key_glosry.md) and in [sorted tables](abensorted_table_glosry.md), the primary key is a [sorted key](abensorted_key_glosry.md). Both table types are [key tables](abenkey_table_glosry.md) for which key access is optimized, and the primary key thus has its own administration. The key fields of these tables are write-protected when individual lines are accessed. [Standard tables](abenstandard_table_glosry.md) also have a primary key, but the corresponding access is not optimized, there is no separate key administration, and the key fields are not write-protected.

[***-\>* More about**](../abap-programming-language/abap-data-types-and-data-objects/abenitab_key_primary.md)
