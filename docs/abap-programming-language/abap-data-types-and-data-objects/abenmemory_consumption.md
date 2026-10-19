---
title: "Memory Management of Deep Objects"
source_file: abenmemory_consumption.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Memory Management of Deep Objects

All data types for which the content of their data objects represents the actual work data referred to as *flat* in ABAP. The [elementary data types](../../abap-glossary/abenelementary_data_type_glosry.md) of a fixed length are flat, as are structures with exclusively flat components. The memory requirements of flat data objects are defined statically by the data type. Flat data objects are always [static data objects](../../abap-glossary/abenstatic_data_object_glosry.md).

On the other hand, data types where the content of their data objects consists of [references](../../abap-glossary/abenreference_glosry.md), which, in turn, refer to work data in another memory area, are referred to as *deep*. Types of [data reference variables](../../abap-glossary/abendata_reference_variable_glosry.md) and [object reference variables](../../abap-glossary/abenobject_refer_variable_glosry.md), as well as the types of [strings](../../abap-glossary/abenstring_glosry.md), [internal tables](../../abap-glossary/abeninternal_table_glosry.md), and [boxed components](../../abap-glossary/abenboxed_component_glosry.md) are deep. Strings and internal tables are [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md) whose memory requirements can change at program runtime and are managed internally using references. Reference variables are static data objects since their actual size is fixed, whereas the size of the explicitly referenced objects is dynamic. Boxed components are a medium in between because their memory requirements in the internal session are not defined when the program is started in the internal session, but can be handled like static data objects with a fixed length. Structures are referred to as deep, regardless of [nesting](../../abap-glossary/abennested_structure_glosry.md) if they contain at least one deep component.

When using deep data objects, working memory is requested at program runtime. In the case of reference variables, this is the memory for administrative information and the objects created (instances of classes and [anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md)). In the case of dynamic data objects (strings, internal tables) and boxed components, this is the memory for administrative information and for the data objects themselves. Objects referenced by reference variables can themselves, in turn, be dynamic, that is, be or contain strings or internal tables.

The requested memory must be available in the [session memory](../../abap-glossary/abenroll_area_glosry.md) of the current [internal session](../../abap-glossary/abeninternal_session_glosry.md), since otherwise a runtime error occurs.

- [Memory Requirements for Deep Data Objects](abenmemory_consumption_1.md)

- [Maximum Size of Dynamic Data Objects](abenmemory_consumption_2.md)

- [Sharing Between Dynamic Data Objects](abenmemory_consumption_3.md)

- [Complex Data Objects with Deep Components](abenmemory_consumption_4.md)
