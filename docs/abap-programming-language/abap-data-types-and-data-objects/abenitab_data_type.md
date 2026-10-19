---
title: "itab - Table Type"
source_file: abenitab_data_type.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Type

A [table type](../../abap-glossary/abentable_type_glosry.md) defined as a [DDIC table type](../../abap-glossary/abenddic_table_type_glosry.md) or using [`TYPES`](../abap-declarations/abaptypes_itab.md) or [`DATA`](../abap-declarations/abapdata_itab.md) is specified completely using the following [technical type properties](../../abap-glossary/abentechnical_type_prpt_glosry.md):

- **Line type**

  The [line type](../../abap-glossary/abenrow_type_glosry.md) of an internal table can be any data type. If the line type is structured, the individual components of a line are also referred to as the columns of the internal table.

- **Table category**

  The [table category](../../abap-glossary/abentable_category_glosry.md) defines how an internal table is administered and how its individual lines can be accessed. There are three table categories:

  - [Standard tables](../../abap-glossary/abenstandard_table_glosry.md) are administered internally using a [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md), which can be implemented using a logical index if necessary. The table can be accessed using either a table index or a [table key](../../abap-glossary/abentable_key_glosry.md). The primary key of a standard table is always non-unique. The response time for accessing the table using the primary key depends linearly on the number of entries in the table. [Secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md) can be defined to make key access to standard tables more efficient.

  - [Sorted tables](../../abap-glossary/abensorted_table_glosry.md) are also administered internally using a [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md). They are always sorted according to the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md). Sorting is in ascending order by size according to the [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) for the data types of the key fields and returns the same result as the [`SORT`](../abap-processing-internal-data/abapsort_itab.md) statement without specifying additions. The table can be accessed using either a table index or a [table key](../../abap-glossary/abentable_key_glosry.md). The primary key of a sorted table can be either unique or non-unique. The response time for accessing the table using the primary key depends logarithmically on the number of table entries, since a binary search is used.

  - [Hashed tables](../../abap-glossary/abenhashed_table_glosry.md) are administered internally using a [hash algorithm](../../abap-glossary/abenhash_algorithm_glosry.md). Hashed tables can be accessed using a [table key](../../abap-glossary/abentable_key_glosry.md) or a [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md). The primary key of hashed tables is always unique. The response time for primary key access is constant and independent of the number of entries in the table.

- **Table key**

  A [table key](../../abap-glossary/abentable_key_glosry.md) is used to identify lines in a table (see below). There are two possible key types for internal tables: [primary keys](../../abap-glossary/abenprimary_table_key_glosry.md) and optional [secondary keys](../../abap-glossary/abensecondary_table_key_glosry.md). Every internal table has a primary key, which is either the [standard key](../../abap-glossary/abenstandard_key_glosry.md) or a user-defined key. Depending on the table category, the primary key can be defined as unique or non-unique. A secondary key is either a sorted key, which can be unique or non-unique, or a unique hash key. If keys are unique, a line with a specific content in the [key fields](../../abap-glossary/abenkey_field_glosry.md) can exist only once in the internal table. A table key can consist of components of the line type or of the entire line ([pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line`) if they are not internal tables or do not contain internal tables. When a table key is defined, the order of the key fields is significant.

Unlike all other user-defined data types, a table type defined in the ABAP Dictionary or using [`TYPES`](../abap-declarations/abaptypes_itab.md) does not have to be specified completely. Either only the keys or the line type and the keys can remain unspecified. This makes the type generic and it can be used only for [typings](../../abap-glossary/abentyping_glosry.md) of field symbols and formal parameters. The predefined [generic ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) `ANY TABLE` and `INDEX TABLE` can be used for this purpose. The first type includes all table categories and the second type includes standard tables and sorted tables, known as [index tables](../../abap-glossary/abenindex_table_glosry.md).

Like [strings](../../abap-glossary/abenstring_glosry.md), internal tables are [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md). Their line type, table category, and table key are always specified completely, but the number of lines is variable and restricted only by the capacity restrictions of specific system installations (see [Maximum Size of Dynamic Data Objects](abenmemory_consumption_2.md)).

An additional type property that is not one of the [technical type properties](../../abap-glossary/abentechnical_type_prpt_glosry.md) and thus is ignored by the [compatibility checks](../../abap-glossary/abencompatible_glosry.md) is the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md). When defining a table type, the addition [`INITIAL SIZE`](../abap-declarations/abaptypes_itab.md) can be used to affect the initial memory requirement.

## Hint

Table keys are evaluated when [typing](../../abap-glossary/abentyping_glosry.md) is checked. Only actual parameters that have the same keys can be assigned to a formal parameter or a field symbol whose table type has a non-generic primary key or one or more secondary keys.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a table type `spfli_tab` with the structured line type `SPFLI` from the ABAP Dictionary, the table category hashed table, a unique primary key, and exactly one non-unique sorted secondary key `cities`.

``` abap
TYPES spfli_tab 
  TYPE HASHED TABLE OF spfli 
       WITH UNIQUE KEY carrid connid 
       WITH NON-UNIQUE SORTED KEY cities COMPONENTS cityfrom cityto 
       WITHOUT FURTHER SECONDARY KEYS.
```
