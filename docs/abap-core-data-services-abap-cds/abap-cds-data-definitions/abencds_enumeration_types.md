---
title: "ABAP CDS - Enumerated Types"
source_file: abencds_enumeration_types.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Enumerated Types

A [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) is a [CDS user-defined type](../../abap-glossary/abencds_user_defined_type_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) that defines an [enumerated type](../../abap-glossary/abenenum_type_glosry.md). CDS enumerated types are defined with the following statement in [ADT](../../abap-glossary/abenadt_glosry.md):

- [CDS DDL - `DEFINE TYPE ENUM`](abencds_define_enum_type.md)

CDS enumerated types are mainly used to check allowed values. They restrict the values that can be passed to CDS elements or CDS parameters, which are typed with an enumerated type.

- In ABAP CDS, enumerated types can be used for typing of elements or parameters, in cast expressions, as operands in expressions, and in comparisons. The methods of the class `CL_DD_SOBJECT_FACTORY` handle CDS enumerated types and evaluate fields typed with reference to an enumerated type.

- In ABAP, a CDS enumerated type can be directly used for the typing of enumeration variables and its enumeration constants can be used as operands in read positions. Before the first usage in an ABAP program, an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) with the name of the CDS enumerated type is implicitly declared in the global context of the program. The enumerated constants of the CDS enumerated type are represented by the components of this structure in alphabetical order. From that point on, a CDS enumerated type can be used in exactly the same way as ABAP enumerated type with such an enumerated structure. For a complete description of the use of enumerated objects in ABAP, see the topic [Enumerated Objects (enum)](../../abap-programming-language/abap-processing-internal-data/abenenumerated_types_usage.md).

A [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) cannot be used as a data type in [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md).

Frameworks:

- CDS user-defined types are supported by analytical runtimes such as the [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md).

- The [annotations](../../abap-glossary/abencds_annotation_glosry.md) of a CDS user-defined type can be evaluated using the methods of the class `CL_DD_DDL_ANNOTATION_SERVICE`.

- CDS enumerated types can currently **not** be used in OData scenarios and in Fiori applications built with the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md).

## Hints

- Enumerated types are also available in the ABAP programming language. Enumerated types in ABAP are described in the following topics:

  - [`TYPES, BEGIN OF ENUM enum_type`](../../abap-programming-language/abap-declarations/abaptypes_enum.md)

  - [Enumerated Objects (enum)](../../abap-programming-language/abap-processing-internal-data/abenenumerated_types_usage.md)

- CDS enumerated types are the successor of [DDIC domains](../../abap-glossary/abendomain_glosry.md) with [fixed values](../../abap-glossary/abenfixed_value_glosry.md).

## More Information

*ABAP Data Models* development guide, section on [CDS enumerated types](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/3a696faff43246cebba2309fb0842acb?version=sap_cross_product_abap).
