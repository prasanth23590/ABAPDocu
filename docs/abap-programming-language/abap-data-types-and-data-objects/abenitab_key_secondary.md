---
title: "itab - Secondary Table Key"
source_file: abenitab_key_secondary.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables > itab - Table Key"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Secondary Table Key

[Hash keys](../../abap-glossary/abenhash_key_glosry.md) and [sorted keys](../../abap-glossary/abensorted_key_glosry.md) can be declared as [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md) for each internal table. For each sorted key, an additional [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) is created.

Access to an internal table using a secondary key is always optimized. This allows additional optimized keys to be introduced for sorted and hashed tables as well as optimized key accesses for standard tables.

- Declaration of Secondary Table Keys

  For data types declared in ABAP programs, a secondary table is declared using the additions [`UNIQUE|NON-UNIQUE KEY key_name COMPONENTS`](../abap-declarations/abaptypes_secondary_key.md) of the statements [`TYPES`](../abap-declarations/abaptypes_secondary_key.md), [`DATA`](../abap-declarations/abapdata_secondary_key.md), and so on. The ABAP Dictionary provides corresponding functions for the table types created in the tool.

- Access Using Secondary Keys

  In key accesses to internal tables, the addition `WITH [TABLE] KEY key_name` can be used in [processing statements](../abap-processing-internal-data/abentable_processing_statements.md) to specify which secondary table key to use. In index accesses, the specification `USING KEY keyname` can be used to specify the [table index](../../abap-glossary/abentable_index_glosry.md) of which secondary key to use. In [table expressions](../abap-processing-internal-data/abentable_expressions.md), this is specified using the addition [`KEY`](../abap-processing-internal-data/abentable_exp_itab_line.md). Secondary keys are not selected automatically. If no secondary key is specified in a processing statement, the primary key or primary table index is always used. If no explicit key is specified for a table expression, a [free search key](../abap-processing-internal-data/abapread_table_free.md) is used to perform reads. Statements where secondary keys can be specified are:

  - [`READ TABLE itab`](../abap-processing-internal-data/abapread_table.md)

    The lines to be read can be specified using a secondary key.

  - [`LOOP AT itab`](../abap-processing-internal-data/abaploop_at_itab.md)

    The processing sequence and conditions can be controlled using a secondary table key.

  - [`INSERT itab`](../abap-processing-internal-data/abapinsert_itab.md)

    Only a secondary key for the source table can be specified here, from which multiple lines are copied. The insertion position is determined solely using the primary key and the primary index.

  - [`APPEND`](../abap-processing-internal-data/abapappend.md)

    Only a secondary key for the source table can be specified here, onto which multiple lines are appended.

  - [`MODIFY itab`](../abap-processing-internal-data/abapmodify_itab.md)

    The lines to be modified can be specified using a secondary key.

  - [`DELETE itab`](../abap-processing-internal-data/abapdelete_itab.md)

    The lines to be deleted can be specified using a secondary key.

  - [`TYPES ... ASSOCIATION`](../abap-declarations/abaptypes_mesh_association.md), [`\_assoc[ ... ]`](../abap-processing-internal-data/abenmesh_path_assoc_cond.md)

    The secondary key used in the evaluation of a [mesh path](../../abap-glossary/abenmesh_path_glosry.md) can be specified using `USING KEY`. If the system field `sy-tabix` is set in this type of access, and a sorted secondary key is used, the line number refers to the associated [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md). In statements that have not been enhanced by these additions, like [`SORT`](../abap-processing-internal-data/abapsort_itab.md), [`COLLECT`](../abap-processing-internal-data/abapcollect.md), or `PROVIDE`, secondary keys are not explicitly supported.

The key fields of a secondary table key are only write-protected if the secondary table key is in use within a `LOOP` or a `MODIFY` statement. Otherwise, the secondary key fields are not write-protected.

## Hints

- Optimized access times to the individual lines using secondary keys are [bought](abenitab_key_memory.md) in exchange for the fact that the ABAP runtime framework then needs to administer the additional keys. For hash keys, this means additional hash administration and an additional [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) for each sorted key.

- When working with internal tables for which a secondary key is declared, it must be ensured that the required key or table index is used in the processing statements.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a hashed table with a unique primary key and a non-unique sorted secondary key `cities`. The table is filled with data from a database table and accessed using a [table expression](../../abap-glossary/abentable_expression_glosry.md) with values specified for the secondary key. The first line found is read.

``` abap
DATA cityfrom TYPE spfli-cityfrom VALUE 'FRANKFURT'. 
cl_demo_input=>add_field( CHANGING field = cityfrom ). 
DATA cityto TYPE spfli-cityto VALUE 'NEW YORK'. 
cl_demo_input=>request( CHANGING field = cityto ). 
 
DATA spfli_tab 
  TYPE HASHED TABLE OF spfli 
       WITH UNIQUE KEY primary_key        COMPONENTS carrid connid 
       WITH NON-UNIQUE SORTED KEY cities  COMPONENTS cityfrom cityto. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @spfli_tab. 
 
cl_demo_output=>display( 
  VALUE #( spfli_tab[ KEY cities 
                      cityfrom = cityfrom 
                      cityto   = cityto ] OPTIONAL ) ).
```
