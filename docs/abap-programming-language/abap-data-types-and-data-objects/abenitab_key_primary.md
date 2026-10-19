---
title: "itab - Primary Table Key"
source_file: abenitab_key_primary.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables > itab - Table Key"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Primary Table Key

Each internal table has a primary table key that allows access to individual lines of the table by specifying a key.

- The components of the primary table key are declared using the [`UNIQUE|NON-UNIQUE KEY`](../abap-declarations/abaptypes_primary_key.md) additions of the statements [`TYPES`](../abap-declarations/abaptypes_primary_key.md), [`DATA`](../abap-declarations/abapdata_primary_key.md), and so on.

- The [standard key](abenitab_standard_key.md), which can be declared both explicitly and implicitly, has a special role.

- The primary table key of a [standard table](../../abap-glossary/abenstandard_table_glosry.md) can also be [empty](abenitab_empty_key.md), that is, it does not contain any key fields.

- In the case of key accesses for internal tables, the primary key is always used implicitly in [processing statements](../abap-processing-internal-data/abentable_processing_statements.md) as long as no secondary key is specified. In [table expressions](../abap-processing-internal-data/abentable_expressions.md), the primary key must also be specified explicitly.

- The primary key has the predefined name `primary_key`, with which it can also be addressed explicitly in processing statements. In table expressions, `primary_key` or an alias name must be specified if the primary key is to be used explicitly.

- Access to an internal table using the primary table key is determined by the [table category](../../abap-glossary/abentable_category_glosry.md) and not the table key. For sorted tables and hashed tables, key access is always optimized using the primary table key. Primary key access to standard tables, however, performs a linear search.

- The key fields of the primary table key of sorted tables and hashed tables are always read-only.

- In the case of sorted tables and hashed tables, separate key administration exists for the primary table key, which enables optimized access but also affects the [memory requirement](abenitab_key_memory.md) of the internal table. There is no separate administration for the primary table key of standard tables.

## Hints

- Since sorted tables and hashed tables have real key administration for the primary key, unlike standard tables, these tables are also grouped under the term [key tables](../../abap-glossary/abenkey_table_glosry.md).

- To achieve optimized key access to standard tables, [secondary keys](../../abap-glossary/abensecondary_table_key_glosry.md) can be used.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a hashed table with a unique primary key. The table is filled with data from a database table and accessed using a [table expression](../../abap-glossary/abentable_expression_glosry.md) with values specified for the primary key.

``` abap
DATA carrid TYPE spfli-carrid VALUE 'LH'. 
cl_demo_input=>add_field( CHANGING field = carrid ). 
DATA connid TYPE spfli-connid VALUE '0400'. 
cl_demo_input=>request( CHANGING field = connid ). 
 
DATA spfli_tab 
  TYPE HASHED TABLE OF spfli 
       WITH UNIQUE KEY primary_key COMPONENTS carrid connid. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @spfli_tab. 
 
cl_demo_output=>display( 
  VALUE #( spfli_tab[ KEY primary_key 
                      carrid = carrid 
                      connid = connid ] OPTIONAL ) ).
```
