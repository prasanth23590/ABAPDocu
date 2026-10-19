---
title: "ABAP Type Hierarchy"
source_file: abentype_hierarchy.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Type Hierarchy

The [ABAP types](../../abap-glossary/abenabap_type_glosry.md) form the following ABAP type hierarchy:

  
![figure](images_abdoc_types_objects.gif)  

The left side of the figure shows the hierarchy of all types and instances, that is, which types are possible in ABAP and the objects that can be created from the types. The right side lists the [generic data types](../../abap-glossary/abengeneric_data_type_glosry.md) assigned to individual nodes of the type hierarchy.

In principle, data types are distinguished from object types.

- [Data types](../../abap-glossary/abendata_type_glosry.md) are used to describe [data objects](../../abap-glossary/abendata_object_glosry.md). They are further divided into elementary, reference, and complex types. Data types are either [built-in types](../../abap-glossary/abenbuiltin_data_type_glosry.md) or they can be defined locally in the program and across the system in the ABAP Dictionary. Data objects as instances of data types are fields in the actual sense. They contain the local program data that a program uses at runtime.

- [Object types](../../abap-glossary/abenobject_type_glosry.md) are used to describe objects in [ABAP Objects](../../abap-glossary/abenabap_objects_glosry.md). They are divided into classes and interfaces. Object types contain the data types mentioned above and functions. Object types are not built-in and must be defined in the program or in the class library. Classes describe an object completely. They define which data types and which functions an object contains. Interfaces describe a partial aspect of an object. The data types and functions of an interface can be implemented by multiple classes. Objects as instances of classes are actual software objects in [ABAP Objects](../../abap-glossary/abenabap_objects_glosry.md) and support object-oriented programming by including methods and events in addition to data.
