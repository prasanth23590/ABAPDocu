---
title: "ABAP CDS - Simple Types"
source_file: abencds_simple_types.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Simple Types

A [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) is a [CDS user-defined type](../../abap-glossary/abencds_user_defined_type_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) that defines an [elementary data type](../../abap-glossary/abenelementary_data_type_glosry.md). CDS simple types are defined with the following special [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) statement in [ADT](../../abap-glossary/abenadt_glosry.md):

- [CDS DDL - `DEFINE TYPE simple_type`](abencds_define_simple_type.md)

CDS simple types can be used for typing in the following contexts:

- In ABAP CDS, simple types can be used for typing of elements or parameters or in cast expressions. The methods of the class `CL_DD_SOBJECT_FACTORY` handle CDS simple types and evaluate fields typed with reference to a simple type.

- In ABAP, a simple type can be specified after the addition `TYPE`. The properties of the type can be evaluated using [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md).

When used for typing, simple types pass their metadata defined by [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md). In addition, simple types can be nested, providing extended reuse capabilities compared to DDIC data elements and DDIC domains.

A [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) cannot be used as a data type in [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md). For example, it cannot be used to type [DDIC data elements](../../abap-glossary/abendata_element_glosry.md) or DDIC views.

Frameworks:

- CDS types are specifically designed for the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md). They support metadata for [OData](../../abap-glossary/abenodata_glosry.md) and SAP Fiori-based scenarios.

- CDS types are supported by analytical runtimes such as the [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md).

- The [annotations](../../abap-glossary/abencds_annotation_glosry.md) of a CDS type can be evaluated using the methods of the class `CL_DD_DDL_ANNOTATION_SERVICE`.

## Hint

CDS simple types are a successor of [DDIC domains](../../abap-glossary/abendomain_glosry.md) and [DDIC data elements](../../abap-glossary/abendata_element_glosry.md). They are mainly intended for use within frameworks such as the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md). They support metadata for [OData](../../abap-glossary/abenodata_glosry.md) and SAP Fiori-based scenarios.

## More Information

*ABAP Data Models* development guide, section about [CDS simple types](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/ad9e96b6630348378cde737cde66ffc9?version=sap_cross_product_abap).
