---
title: "DDIC - Technical Properties of Data Elements"
source_file: abenddic_data_elements_tech.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Data Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Technical Properties of Data Elements

A data element describes an [elementary data type](../../abap-glossary/abenelementary_data_type_glosry.md) or a [reference type](../../abap-glossary/abenreference_type_glosry.md) with the following technical properties:

- **Elementary type**

  A data element that describes an elementary type has a [built-in data type](../ddic-built-in-data-types/abenddic_builtin_types.md) from the ABAP Dictionary, a length, and, if necessary, a number of decimal places as its technical properties. These technical properties are defined either directly in the data element or they are inherited from a [domain](abenddic_domains.md).

- **Reference type**

  A data element that describes a reference type is either a type for a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) or for an [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md).

  - The [static type](../../abap-glossary/abenstatic_type_glosry.md) for a data reference variable is either the generic type `DATA`, any existing data type from the ABAP Dictionary (including [DDIC database tables](../ddic-database-tables/abenddic_database_tables.md) or views), or a directly specified [built-in data type](../ddic-built-in-data-types/abenddic_builtin_types.md).

  - The [static type](../../abap-glossary/abenstatic_type_glosry.md) for an object reference variable is either the generic type `OBJECT` or an existing global class or a global interface from the [class library](../../abap-glossary/abenclass_library_glosry.md).

## Hints

- When existing data elements are modified, all consumers of the data element are also affected. In particular, [foreign keys](../ddic-database-tables/abenddic_database_tables_forkey.md) can become inconsistent when used for fields of DDIC database tables, which makes [adjustments](../ddic-database-tables/abenddic_database_tables_adj.md) necessary.

- Global reference types from the ABAP Dictionary can be used for typing in ABAP programs. They cannot, however, be used for fields of database tables or for elements of CDS entities.
