---
title: "reference"
source_file: abenreference_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# reference

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Content of [reference variables](abenreference_variable_glosry.md). A valid reference refers to a [data object](abendata_object_glosry.md) ([data reference](abendata_reference_glosry.md)) or an [instance](abeninstance_glosry.md) of a [class](abenclass_glosry.md) ([object reference](abenobject_reference_glosry.md)). References in reference variables are either [heap references](abenheap_reference_glosry.md) or [stack references](abenstack_reference_glosry.md). Internally, [strings](abenstring_glosry.md), [internal tables](abeninternal_table_glosry.md), and [boxed components](abenboxed_component_glosry.md) are also addressed via references. From a technical point of view, an object in ABAP is referenced in multiple layers. A reference is the address of an internal header (object header, string header, or table header), which contains the address of the actual object and other administrative information such as the [data type](abendata_type_glosry.md) of a referenced data object.

[***-\>* More about**](../abap-programming-language/abap-data-types-and-data-objects/abendata_references.md)
