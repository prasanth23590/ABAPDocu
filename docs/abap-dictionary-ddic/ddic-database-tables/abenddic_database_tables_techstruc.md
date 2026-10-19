---
title: "DDIC - Structure-Specific Technical Properties of Database Tables"
source_file: abenddic_database_tables_techstruc.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Technical Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Structure-Specific Technical Properties of Database Tables

The following technical properties are mostly the same as those of a [DDIC structure](../ddic-data-types/abenddic_structures_tech.md) in ABAP Dictionary:

- **Table fields (columns)**

  A table field is a component of the structure of the DDIC database table and describes the name, the data type, and any semantic properties of a field of a DDIC database table. A table field is a component of the structured data type of the table and the corresponding [rules](../ddic-data-types/abenddic_structures_tech.md) apply to the component name and component type, with the following restrictions:

  - The name of a table field cannot be a reserved name. The reserved names that cannot be used are specified in the DDIC database table `TRESE`. This is also important when using [include structures](../ddic-data-types/abenddic_include_structure.md).

  - A table field always has one elementary data type. Reference types, substructures, and table types are not possible. The elementary data type is specified directly for the table field or by using a data element and is always based on a [built-in dictionary type](../ddic-built-in-data-types/abenddic_builtin_types.md). A table field has a platform-dependent type in the physical database table. For each platform, there is a mapping between the elementary types in the ABAP Dictionary and the platform-dependent types. If only [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) is used, this mapping is transparent for ABAP programmers and only the built-in types in the ABAP Dictionary and their ABAP types are relevant for the ABAP program.

  - Fields with the type `CHAR` can have a maximum of 1333 characters.

  - Fields with the type `LRAW` or `LCHR` must be at the end of the table. Only one such field is allowed per table. Directly in front of a field with the type `LRAW` or `LCHR`, there must be a field with the type `INT2` or `INT4` that defines the maximum length of the field.

- **Include structures**

  DDIC structures, but not DDIC database tables or DDIC views, can be included in a DDIC database table as [include structures](../ddic-data-types/abenddic_include_structure.md). A structure can only be included in a table if its components meet the table field prerequisites above. In particular, an included structure cannot contain any substructures. Any naming conflicts must be bypassed by defining suffixes. As in regular structures, the include can be assigned a group name.

  - When a structure is included, all its fields can be flagged as [key fields](abenddic_database_tables_key.md). The include structure must then be inserted between the existing key fields or directly after them. The key properties of the individual fields of an included structure do not have any effect. Either all fields are included as key fields or none.

  - When an include structure is included, the [flag for initial values](abenddic_database_tables_init.md) can be set for the entire include structure. In this case, the fields in the include structure for which this property is set keep their property, but if this property is not set, it is also not switched on. If the flag for initial values is not set for the included include structure, this property is removed for all its fields.

    The fields of an included include structure are still part of the structure. They can only be edited via the structure and any changes made to the structure affect all including database tables. The fields of an included include structure can also be transformed to direct fields of the DDIC database table that are no longer linked with the originally included structure.

- **Enhancement category**

  The same applies to the enhancement category of DDIC database tables as to the [enhancement category of structures](../ddic-data-types/abenddic_structures_enh_cat.md).

The following applies with respect to the number of fields and length of the structure of a DDIC database table:

- Number of fields

  - A table in the software component `SAP_BASIS` can contain a maximum of 750 fields.

  - A table in a software component other than `SAP_BASIS` can contain 1000 fields if the [storage type](abenddic_database_tables_storage.md) is Row Store and 1500 fields if the storage type is Column Store.

- The total of all field lengths is limited. The following applies with respect to the total of the number of bytes of the non-character-like fields and the number of characters of the flat character-like fields:

  - In a table in the software component `SAP_BASIS`, the total cannot be greater than 4030.

  - In the ABAP Dictionary, no limit applies to tables in software components other than `SAP_BASIS`. The limit defined in the current database platform applies (in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) this is 512 KB).

    In the case of deep fields such as `STRING`, `RAWSTRING`, `LRAW`, `LCHR`, and `GEOM_EWKB`, only the bytes of the references are counted and not the actual content.

## Hints

- A DDIC database table cannot be defined using a nested structure, since nested structures are not possible in every supported database.

- If the prerequisites above are met, an existing DDIC structure can be transformed to a DDIC database table. Conversely, a DDIC database table can also be transformed to a DDIC structure, whereby the database object is deleted.

- Renaming of fields that already contain data is not supported. If the name of an existing field is changed in a DDIC database table, an [adjustment](abenddic_database_tables_adj.md) takes place, where the field with the old name is deleted in the physical database table and a field with the new name is appended. All data in the column with the old name are lost.
