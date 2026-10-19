---
title: "Boxed Components"
source_file: abenboxed_components.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Boxed Components

Boxed components are structures that are not stored in their superordinate context. Instead, an internal reference that points to the actual structure is stored instead of the structure. A boxed component is therefore always a [deep](../../abap-glossary/abendeep_glosry.md) component of its context.

It is currently possible to declare substructures of structured data types and structured attributes of classes as

- [static boxes](abenstatic_boxes.md)

These boxes support [initial value sharing](../../abap-glossary/abeninitial_value_sharing_glosry.md).

## Hints

- Boxed components are a middle ground between [static](../../abap-glossary/abenstatic_data_object_glosry.md) and [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md). Their memory requirements are not fixed when the program is started in the [internal session](../../abap-glossary/abeninternal_session_glosry.md), but they can be handled like static data objects with a fixed length.

- A nested structure that contains a boxed component as a component is always a [deep structure](../../abap-glossary/abendeep_structure_glosry.md).

- Structures of the ABAP Dictionary can also contain boxed components. ABAP Dictionary database tables cannot contain any boxed components since their structures must be flat.

- In [RTTS](../../abap-glossary/abenrun_time_type_services_glosry.md) classes and objects, boxed components are handled as follows:

  - The class `CL_ABAP_TYPEDESCR` contains the constant `TYPEKIND_BREF` for static boxes. The value of these constants is specified as the type of a static box in the component table `COMPONENTS` of the class `CL_ABAP_STRUCTDESCR` or the attribute table `ATTRIBUTES` of the classes `CL_ABAP_CLASSDESCR` or `CL_ABAP_INTFDESCR`.

  - In the return value of the method `GET_COMPONENTS` of the class `CL_ABAP_STRUCTDESCR` or `GET_ATTRIBUTE_TYPE` of the classes `CL_ABAP_CLASSDESCR` or `CL_ABAP_INTFDESCR`, boxed components are listed as type description objects of the class `CL_ABAP_REFDESCR`, like reference variables. The method `GET_REFERENCED_TYPE` of this class returns a type description object for the substructure. A type description object of the class `CL_ABAP_REFDESCR`, which describes a boxed component, cannot be used in the statements [`CREATE DATA`](../abap-creating-objects-and-values/abapcreate_data.md) or [`ASSIGN CASTING`](../abap-processing-internal-data/abapassign_casting.md).
