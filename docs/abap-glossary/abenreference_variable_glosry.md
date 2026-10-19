---
title: "reference variable"
source_file: abenreference_variable_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# reference variable

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

[Data object](abendata_object_glosry.md) that contains a [reference](abenreference_glosry.md). Reference variables are either [data reference variables](abendata_reference_variable_glosry.md) or [object reference variables](abenobject_refer_variable_glosry.md). Reference variables have a length of 8 bytes and are opaque, which means the reference cannot be accessed directly. They are typed with the addition [`REF TO`](../abap-programming-language/abap-declarations/abaptypes_references.md) that defines their [static type](abenstatic_type_glosry.md). The static type is always more general than or the same as the [dynamic type](abendynamic_type_glosry.md). For assignments between reference variables, [reference semantics](abenreference_semantics_glosry.md) apply.

[***-\>* More about**](../abap-programming-language/abap-declarations/abapdata_references.md)
