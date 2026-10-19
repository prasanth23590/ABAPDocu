---
title: "DDIC - Data Elements"
source_file: abenddic_data_elements.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Data Elements

A [DDIC data element](../../abap-glossary/abendata_element_glosry.md) defines an [elementary data type](../../abap-glossary/abenelementary_data_type_glosry.md) or a [reference type](../../abap-glossary/abenreference_type_glosry.md). DDIC data elements describe the technical type properties and the semantic meaning of an object that is defined with reference to the data element. Data elements are the elementary components of complex types such as [DDIC structures](abenddic_structures.md), [DDIC table types](abenddic_table_types.md), or [DDIC database tables](../ddic-database-tables/abenddic_database_tables.md). An object which is declared program-internally with reference to a data element always has one of the elementary built-in ABAP types. The type in question is defined by the mapping of the [built-in types](../ddic-built-in-data-types/abenddic_builtin_types.md) in the ABAP Dictionary to ABAP types.

- [Technical properties of data elements](abenddic_data_elements_tech.md)

- [Semantic properties of data elements](abenddic_data_elements_sema.md)

## Hints

- [ABAP Core Data Services](../../abap-glossary/abenabap_core_data_services_glosry.md) offer [CDS simple types](../../abap-glossary/abencds_simple_type_glosry.md) for defining [elementary data types](../../abap-glossary/abenelementary_data_type_glosry.md) natively in ABAP CDS. CDS simple types can be enriched with semantic information using [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md). This semantic information is evaluated by frameworks such as the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md) when a simple type is used for typing. Moreover, simple types can be nested within each other and therefore offer advanced reuse capabilities compared to DDIC data elements.

- The technical properties of a data element can be defined either directly or by using a reusable [domain](abenddic_domains.md). This is why the concept is known as a two-level domain concept.

- The name of a data element must follow the [naming rules for DDIC data types](abenddic_types_names.md).
