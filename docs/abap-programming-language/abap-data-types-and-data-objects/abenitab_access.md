---
title: "itab - Accessing Internal Tables"
source_file: abenitab_access.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Accessing Internal Tables

When internal tables are accessed, either the entire table, or individual lines can be addressed.

- The entire table is accessed using special statements such as [`SORT`](../abap-processing-internal-data/abapsort_itab.md), but also using general statements where internal tables can be specified at operand positions. Examples are [assignments](../abap-processing-internal-data/abapmove.md), parameter passing, target or source areas in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and many other statements that return or expect tabular data.

- Individual lines are accessed using the following:

  - [Special statements](../abap-processing-internal-data/abenitab.md) such as [`READ TABLE`](../abap-processing-internal-data/abapread_table.md), [`LOOP AT`](../abap-processing-internal-data/abaploop_at_itab.md), or [`MODIFY`](../abap-processing-internal-data/abapmodify_itab.md)

  - Table expressions [`itab[ ... ]`](../abap-processing-internal-data/abentable_expressions.md).

  - Mesh path expressions [`mesh_path`](../abap-processing-internal-data/abenmesh_path_expression.md)

    When individual lines are accessed, either a [work area](../../abap-glossary/abenwork_area_glosry.md) is used into which the line content can be read or from which it can be modified, or a line is linked to a [field symbol](../../abap-glossary/abenfield_symbol_glosry.md) or a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) and these are used to access the line directly.

The table category and the table keys are significant when internal tables are processed:

- The [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md) can be used to access [index tables](../../abap-glossary/abenindex_table_glosry.md), that is, [standard tables](../../abap-glossary/abenstandard_table_glosry.md) and [sorted tables](../../abap-glossary/abensorted_table_glosry.md). These tables always have a primary index.

- [Primary table keys](../../abap-glossary/abenprimary_table_key_glosry.md) can be used for optimized access to [sorted tables](../../abap-glossary/abensorted_table_glosry.md) and [hashed tables](../../abap-glossary/abenhashed_table_glosry.md).

- A [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) can be used to access any tables with a [sorted](../../abap-glossary/abensorted_key_glosry.md) [secondary table index](../../abap-glossary/abensecondary_table_key_glosry.md).

- The [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) can be used for optimized access to any tables with a secondary [sorted key](../../abap-glossary/abensorted_key_glosry.md) or [hash key](../../abap-glossary/abenhash_key_glosry.md).

## Hints

- Internal tables must be specified at operand positions for internal tables when the statement is executed. Only index tables can be specified at operand positions that include index access.

  - In [processing statements](../abap-processing-internal-data/abentable_processing_statements.md) for internal tables, the operands can be generically typed with TYPE [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) or TYPE [`any`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) as long as no table index is accessed. For index accesses, an operand must be typed at least with TYPE [`index table`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

  - In expressions as [`FOR expressions`](../abap-processing-internal-data/abenfor_itab.md) or [table expressions](../abap-processing-internal-data/abentable_expressions.md), an internal table must be typed at least with TYPE [`any table`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

- If the line type of internal tables contains [object reference variables](../../abap-glossary/abenobject_refer_variable_glosry.md) as the components `comp`, the attributes `attr` of the object to which the reference points can be used as key values for reading, sorting, and modifying table lines. This is always possible for statements that address individual [components](../abap-processing-internal-data/abenitab_components.md) of the table.

- The content of the primary table key cannot be changed for any writes to individual lines of [sorted tables](../../abap-glossary/abensorted_table_glosry.md) and [hashed tables](../../abap-glossary/abenhashed_table_glosry.md). If writes are performed in write positions across the entire table line in these tables, for example, as a target field of assignments or as actual parameters for output parameters, an exception is always raised. It is not possible to access entire table lines using field symbols, data references or table expressions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, data is written to an internal table with ABAP SQL, sorting takes place, and reads are demonstrated with the statement `READ TABLE` and a [table expression](../../abap-glossary/abentable_expression_glosry.md).

``` abap
DATA scarr_tab 
  TYPE STANDARD TABLE OF scarr 
       WITH NON-UNIQUE KEY carrid. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @scarr_tab. 
 
SORT scarr_tab BY carrid ASCENDING. 
 
READ TABLE scarr_tab WITH TABLE KEY carrid = 'LH' 
                     TRANSPORTING NO FIELDS. 
IF sy-subrc = 0. 
  FINAL(idx) = sy-tabix. 
  TRY. 
      cl_demo_output=>display( scarr_tab[ idx + 1 ]-carrid ). 
    CATCH cx_sy_itab_line_not_found. 
      ... 
  ENDTRY. 
ENDIF.
```
