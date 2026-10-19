---
title: "DDIC DDL - DEFINE STRUCTURE, ext_annos"
source_file: abenddicddl_define_ext_annos.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures > DDIC - Dictionary DDL for Structure Definitions > DDIC DDL - DEFINE STRUCTURE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE STRUCTURE, ext_annos

## Syntax

``` abap
@AbapCatalog.enhancement.fieldSuffix: 'suffix' 
@AbapCatalog.enhancement.quotaMaximumFields: integer 
@AbapCatalog.enhancement.quotaMaximumBytes: integer  
```

## Description

The following annotations are required for [C0 release](../../abap-glossary/abenc0_contract_glosry.md) of a DDIC structure. They are evaluated only in the context of [C0 release](../../abap-glossary/abenc0_contract_glosry.md) for [developer extensibility](../../abap-glossary/abendev_extensibility_glosry.md).

- `@AbapCatalog.enhancement.fieldSuffix` defines a 3-character element suffix `suffix`. This suffix is to be used for all fields of an extension created by customers or partners from a [restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md). The purpose is to avoid field naming clashes. The following rules apply:

  - `suffix` must consist of exactly 3 alphabetical characters \[A-Z\].

  - If the object is a partner or customer object, the suffix must begin with Y or Z.

  - If the object is an SAP object, the suffix must not begin with Y or Z.

  - Field suffixes should be unique. If the specified field suffix is already registered by a different development object, a syntax check warning occurs.

- `@AbapCatalog.enhancement.quotaMaximumFields` defines the maximum number of fields that can be appended to the corresponding object by customers and partners. In other words, it reserves a field count for customer and partner extensions.

  The annotation value `integer` must be an integer between 0 and 1000. A value between 100 and 560 is recommended. Otherwise, a syntax check warning occurs. The sum of fields of the original object and reserved fields must not exceed the technical limitations of the object in question. Current technical limitations are:

  - DDIC database table that is part of the software component `SAP_BASIS`: 750 fields.

  - DDIC database table, [storage type](../ddic-database-tables/abenddic_database_tables_storage.md) Row Store: 1000 fields.

  - DDIC database table, storage type Column Store: 1500 fields.

  - DDIC structure: 9999 fields.

- `@AbapCatalog.enhancement.quotaMaximumBytes` defines the maximum byte capacity that can be appended to the corresponding object by customers and partners. In other words, it reserves a byte capacity for customer and partner extensions. The annotation value `integer` must be an integer. The sum of bytes of the original object and reserved bytes must not exceed the technical limitation of 2 to the power of 19 minus 1 bytes (2^19-1). The recommended number of reserved bytes is between 1.000 and 56.000 bytes per structure.

## Hints

- The same annotations can also be specified in the definition of a DDIC database table using [`DEFINE TABLE`](../ddic-database-tables/abenddicddl_define_table.md) for C0 release of the database table in question.
