---
title: "CDS DDL - DDIC-Based View, SELECT, UNION"
source_file: abencds_union_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, UNION

## Syntax

``` abap
... UNION [ALL] select_statement ...  
```

[`select_statement`](abencds_select_statement_v1.md)

## Description

Merges the rows of the result sets of two [`SELECT` statements](abencds_select_statement_v1.md) of [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) into one result set. As a prerequisite, the result sets must have the same number of elements and the element pairs that occur in the same position of the result set must have a compatible data type. The data types `DF16_...`, `DF34_...`, `LCHR`,`LRAW`,`STRING`, `RAWSTRING`, and `GEOM_EWKB` are not supported. A union result set can itself be the left side of a further union.

If the addition `ALL` is specified, all entries, even duplicates, are listed in the result set. If `ALL` is not specified, all duplicate entries are removed from the result set. For determining the duplicate rows, all columns of the result set are considered. In detail, this works as follows:

- First, all rows of all `UNION` branches are combined into one result set.

- Then, all rows that occur more than once (considering all columns, not just key fields) are deleted except for one.

The properties of the elements of the merged result set are determined as follows:

- Element names

  - If an explicit [name list](abencds_name_list_v1.md) is specified, this list determines the names of the elements

  - If no explicit [name list](abencds_name_list_v1.md) is specified, the direct element names or the alternative element names defined using `AS` must match for each column in the [`SELECT` lists](abencds_select_list_v1.md) of all `SELECT` statements and are used.

- Key elements

  The [`SELECT` list](abencds_select_list_v1.md) of the first `SELECT` statement determines the key elements.

- Element annotations

  Only the [element annotations](abencds_element_annotations_v1.md) from the [`SELECT` list](abencds_select_list_v1.md) of the first `SELECT` statement are applied.

- Data type

  - The [`SELECT` list](abencds_select_list_v1.md) of the first `SELECT` statement determines the data type of each element of the CDS entity.

  - The data type used to create the union set on the database is a data type whose value range covers the data types of the associated columns of all result sets involved.

The following table shows which data types can be merged with each other in a union. On the left side, the data types of the `SELECT` list of the first `SELECT` statement are listed and the other columns specify with which data types of the following `SELECT` lists they can be merged.

| **First/following** | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`CURR`** | **`QUAN`** | **`FLTP`** | **`CHAR`** | **`SSTRING`** | **`NUMC`** | **`DATS`** | **`TIMS`** | **`ACCP`** | **`CLNT`** | **`LANG`** | **`UNIT`** | **`CUKY`** | **`RAW`** |
|---------------------|------------|------------|------------|------------|-----------|------------|------------|------------|------------|---------------|------------|------------|------------|------------|------------|------------|------------|------------|-----------|
| **`INT1`**          | x          | w          | w          | w          | w         | w          | w          | w          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`INT2`**          | x          | x          | w          | w          | w         | w          | w          | w          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`INT4`**          | x          | x          | x          | w          | w         | w          | w          | w          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`INT8`**          | x          | x          | x          | x          | w         | w          | w          | w          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`DEC`**           | w          | w          | w          | w          | w         | w          | w          | w          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`CURR`**          | w          | w          | w          | w          | w         | w          | w          | w          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`QUAN`**          | w          | w          | w          | w          | w         | w          | w          | w          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`FLTP`**          | x          | x          | x          | w          | w         | w          | w          | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`CHAR`**          | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | w          | w             | l          | w          | w          | l          | l          | l          | l          | l          | \-        |
| **`SSTRING`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | w          | w             | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`NUMC`**          | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | w          | \-            | l          | l          | l          | l          | l          | l          | \-         | \-         | \-        |
| **`DATS`**          | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | w          | \-            | l          | x          | \-         | \-         | \-         | \-         | \-         | \-         | \-        |
| **`TIMS`**          | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | w          | \-            | l          | \-         | x          | \-         | \-         | \-         | \-         | \-         | \-        |
| **`ACCP`**          | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | l          | \-            | l          | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-        |
| **`CLNT`**          | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | l          | \-            | l          | \-         | \-         | \-         | x          | \-         | \-         | \-         | \-        |
| **`LANG`**          | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | l          | \-            | l          | \-         | \-         | \-         | \-         | x          | \-         | \-         | \-        |
| **`UNIT`**          | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | l          | \-            | \-         | \-         | \-         | \-         | \-         | \-         | x          | \-         | \-        |
| **`CUKY`**          | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | l          | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | x          | \-        |
| **`RAW`**           | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | x         |

There are no further restrictions to note in combinations using *x*. The following rules apply to the other combinations:

- In combinations with *w*, the length or the value range of the data type in the first `SELECT` must be long enough for all following `SELECT` lists. If this is not the case, a syntax check warning is raised.

- In combinations using *l*, the lengths of the data types must match exactly.

If the length or value range of the first element does not cover the following elements in combinations with *w*, the value returned by the database can be too great for the data type of the element of the CDS entity. It is still possible to activate the view here, but the content may be truncated or exceptions may be raised in ABAP SQL [queries](../../abap-glossary/abenasql_query_glosry.md) if a type reference is applied to the entity. This is due to the [assignment rules](../../abap-programming-language/abap-database-access/abenselect_into_conversion.md) of the [`INTO`](../../abap-programming-language/abap-database-access/abapinto_clause.md) clause. Assignments to ABAP data objects with a sufficiently large value range, on the other hand, do not cause problems.

A CDS view in which union sets are formed with `UNION` can expose [CDS associations](../../abap-glossary/abencds_association_glosry.md). Such an association must be defined and exposed in the same way in all `SELECT` statements merged with `UNION`. That is, CDS associations that are exposed in the respective [`SELECT` lists](abencds_select_list_v1.md) must appear in all `SELECT` statements merged with `UNION` and the following requirements must be met:

- They have the same name.

- They have the same [cardinality](../../abap-glossary/abencardinality_glosry.md).

- They must be exposed at the same position in the [`SELECT` list](abencds_select_list_v1.md) using a [path expression](abencds_path_expression_v1.md).

- They must have the same `ON` conditions, that is:

  - The conditions must relate to the same fields in the association source and association target and express the same logic for these fields.

  - The fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) that are listed in an `ON` condition must be at identical positions in the `SELECT` list.

These rules also apply if a CDS association is defined in a data source of a `SELECT` statement and is exposed by the current statement. From outside, the CDS associations with the same name that are exposed in the individual `SELECT` lists act like a CDS association exposed by the union set. There are no restrictions on CDS associations that are not exposed in the `SELECT` lists.

## Restriction

Defining new CDS compositions is not possible in a CDS view with `UNION` or `UNION ALL`.

## Hints

- Union sets can be a good way of transforming non-normalized DDIC database tables into a normalized view on the data.

- If the length of the value range of an element from the `SELECT` list of the first `SELECT` statement does not cover the associated elements of the following `SELECT` statements, it is advisable to define an appropriate type with a suitable [`CAST`](abencds_cast_expression_v1.md) expression.

- The maximum number of different `SELECT` statements that can be merged using `UNION` depends on the database system. If this number is exceeded, the CDS view cannot be activated.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view creates the union of the result sets of two `SELECT` statements. The element `col1` in the first `SELECT` list has the type `INT4`, whereas the associated element `col1` in the second `SELECT` list has the type `INT8`. This is why a syntax check warning is raised. To bypass the warning, `col2` is converted to data type `INT8` using a [`CAST`](abencds_cast_expression_v1.md) expression.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSUNIONTYPE'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view Demo_Cds_Union_Element_Type(
    id,
    col1,
    col2
  )
  as select from
    demo_expressions
    {
      id,
      num1                      as col1,
      cast( num1 as abap.int8 ) as col2
    }
union all select from
  demo_expressions
    {
      id,
      numlong1 as col1,
      numlong1 as col2
    }
```

The class `CL_DEMO_CDS_UNION_ELEMENT_TYPE` uses [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) to access the view four times:

- The first access writes directly to an internal table with the line type of the CDS entity. The access works because the value of the element `col1` matches the value range of the data type `i`.

- The second access is the same as the first but one value in the element `col1` is outside the value range of the data type `i` of the first column of the internal table `result2`. This is why an exception is raised.

- In the third access, the exception is prevented since the data type of the first column of the result set (and hence the data type of the internal table `result3`) is transformed to `int8` using a [`CAST`](../../abap-programming-language/abap-database-access/abensql_cast.md) in ABAP SQL.

- In the fourth access, the exception is prevented due to an appropriate declaration of the data type of the first column of the internal table `result4`.

The recommended method in all cases, however, is to handle the second element using a [`CAST`](abencds_cast_expression_v1.md) in the CDS view.
