---
title: "sharing"
source_file: abensharing_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sharing

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

When [assignments](abenassignment_glosry.md) are made between [dynamic data objects](abendynamic_data_object_glosry.md) ([strings](abenstring_glosry.md) and [internal tables](abeninternal_table_glosry.md) of the same type) and if these data types are [passed by value](abenpass_by_value_glosry.md), for performance reasons, only the required internal administrative entries for the string or [table body](abentable_body_glosry.md) are passed ([table sharing](abentable_sharing_glosry.md) possible only if the [line type](abenrow_type_glosry.md) itself does not contain any [table types](abentable_type_glosry.md)). Sharing is kept until one of the data objects involved is accessed and changed. At this point, the actual copy process takes place. See also [initial value sharing](abeninitial_value_sharing_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-data-types-and-data-objects/abenmemory_consumption_3.md)
