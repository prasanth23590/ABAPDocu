---
title: "DDIC - Semantic Properties of Structures"
source_file: abenddic_structures_sema.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Semantic Properties of Structures

Structures in the ABAP Dictionary can have the following semantic properties:

- **Short text of the structure**

  Each structure is assigned a short descriptive text that must be specified when it is created.

- **Documentation**

  A structure can be assigned documentation that can be read as required.

- **Short text of components**

  Each component is assigned a short descriptive text that is inherited in any references to an existing type. A custom text can be specified if the type is defined directly.

- **Output style of components**

  A component with the directly specified type of a decimal floating point number can be assigned an [output style](../ddic-built-in-data-types/abenddic_decimal_floating_point.md).

- **Reference field** for components of the [built-in data types](../ddic-built-in-data-types/abenddic_builtin_types.md) `CURR` and `QUAN`

  For each [currency field](../ddic-built-in-data-types/abenddic_currency_field.md) with the type `CURR` and for each [quantity field](../ddic-built-in-data-types/abenddic_quantity_field.md) with the type `QUAN`, a component of the same or a different structure (or DDIC database table or view) must be defined as a reference field with the built-in data type `CUKY` or `UNIT`. This field is the [currency key](../../abap-glossary/abencurrency_key_glosry.md) or [unit key](../../abap-glossary/abenunit_glosry.md) that specifies the currency or the unit. A table in which a reference field is defined is called a reference table.

- **Check table**

  Like table fields of DDIC database tables, structure components can be assigned [check tables](../ddic-database-tables/abenddic_database_tables_checktab.md). This is useful for structures included in DDIC database tables which are part of the database table's [foreign key](../ddic-database-tables/abenddic_database_tables_forkey.md).

- **Spatial reference system**

  Structure components with the [geodata type](../../abap-glossary/abengeo_data_type_glosry.md) `GEOM_EWKB` must be assigned [spatial reference systems](../ddic-database-tables/abenddic_database_tables_sptlrf.md), just like table fields of DDIC database tables. This is relevant for structures that are included in DDIC database tables.

- **Search help**

  Structure components whose data type is specified by a data element with an elementary data type can be assigned a [search help](../../abap-glossary/abensearch_help_glosry.md). This is only useful, however, for components used for input fields on UIs.

- **Key field**

  Like table fields of DDIC database tables, structure components can be defined as [key fields](../ddic-database-tables/abenddic_database_tables_key.md). When a structure with key fields is [included in DDIC database tables](../ddic-database-tables/abenddic_database_tables_techstruc.md), however, they are not used as key fields of the DDIC database table. Either all or no fields of an included structure can become key fields when included.

- **Flag for initial values**

  Like table fields of DDIC database tables, structure components can be assigned a [flag for initial values](../ddic-database-tables/abenddic_database_tables_init.md). When a structure with such components is [included in DDIC database tables](../ddic-database-tables/abenddic_database_tables_techstruc.md), the table fields can inherit these properties.

## Hint

Structure components whose type is defined using [data elements](abenddic_data_elements.md) have the additional semantic properties of the data elements.
