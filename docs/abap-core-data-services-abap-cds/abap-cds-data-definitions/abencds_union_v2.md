---
title: "CDS DDL - CDS View Entity, SELECT, UNION"
source_file: abencds_union_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, clauses > CDS DDL - CDS View Entity, Set Operators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, UNION

## Syntax

``` abap
... UNION [ALL] select_statement ...  
```

[`select_statement`](abencds_select_statement_v2.md)

## Description

Merges the rows of the result sets of multiple [`SELECT` statements](abencds_select_statement_v2.md) of [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) into one result set. As a prerequisite, the result sets must have the same number of elements and the element pairs that occur in the same position of the result set must have a compatible data type. A union result set can itself be the left side of a further union.

If the addition `ALL` is specified, all entries, even duplicates, are listed in the result set. If `ALL` is not specified, all duplicate entries are removed from the result set. For determining the duplicate rows, all columns of the result set are considered. In detail, this works as follows:

- First, all rows of all `UNION` branches are combined into one result set.

- Then, all rows that occur more than once (considering all columns, not just key fields) are deleted except for one.

**Data Types**

If the addition ALL is specified, all data types are possible in a union view. Elements with data types [`LRAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`LCHR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) must be at the end of the view and an element of type INT2 or INT4 must stand directly in front of such an element, representing the maximum length of the element. Only one such element is allowed per view.

Without the addition ALL, data types [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LCHR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LRAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not supported.

## Prerequisite

As a prerequisite for using the statement `UNION` in a CDS view entity, the CDS view entity annotation [`Metadata.ignorePropagatedAnnotations: true`](abencds_view_entity_anno.md) must be specified.

**Rules for the Elements of a `UNION` View**

In general, the first SELECT statement defines the signature of the UNION view. Here are the details on the properties of the elements of the merged result set:

- Element names

  The direct element names or the alternative element names defined using `AS` must match for each column in the [`SELECT` lists](abencds_select_list_v2.md) of all `SELECT` statements and are used.

- Key elements

  They key elements of all `SELECT` lists must match. Otherwise, a syntax check error occurs.

- Element annotations

  Only the `SELECT` list of the first `SELECT` statement can define [element annotations](abencds_element_annotations_v2.md). In all subsequent branches, element annotations a forbidden.

- Data type

  - The `SELECT` list of the first `SELECT` statement determines the DDIC data type of each element of the CDS entity.

  - The data type used to create the union set on the database is a data type whose value range covers the data types of the associated columns of all result sets involved.

The following table shows which data types can be merged with each other in a union. On the left side, the data types of the SELECT list of the first SELECT statement are listed and the other columns specify with which data types of the following SELECT lists they can be merged.

| **First/following** | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`DF16_...`** | **`DF34_...`** | **`CURR`** | **`QUAN`** | **`FLTP`** | **`CHAR`** | **`SSTRING`** | **`STRING`** | **`NUMC`** | **`DATS`** | **`DATN`** | **`TIMS`** | **`TIMN`** | **`UTCL`** | **`ACCP`** | **`CLNT`** | **`LANG`** | **`UNIT`** | **`CUKY`** | **`RAW`** | **`GEOM_EWKB`** |
|---------------------|------------|------------|------------|------------|-----------|----------------|----------------|------------|------------|------------|------------|---------------|--------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|-----------|-----------------|
| **`INT1`**          | x          | w          | w          | w          | w         | \-             | \-             | \-         | w          | w          | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`INT2`**          | x          | x          | w          | w          | w         | \-             | \-             | \-         | w          | w          | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`INT4`**          | x          | x          | x          | w          | w         | \-             | \-             | \-         | w          | w          | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`INT8`**          | x          | x          | x          | x          | w         | x              | \-             | \-         | w          | w          | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`DEC`**           | w          | w          | w          | w          | w         | w              | w              | \-         | w          | w          | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`DF16_...`**      | w          | w          | w          | w          | w         | x              | \-             | \-         | w          | w          | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`DF34_...`**      | w          | w          | w          | w          | w         | x              | x              | \-         | w          | w          | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`CURR`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | d          | \-         | \-         | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`QUAN`**          | w          | w          | w          | w          | w         | w              | w              | \-         | w          | w          | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`FLTP`**          | x          | x          | x          | w          | w         | w              | w              | \-         | w          | x          | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`CHAR`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | w          | w             | \-           | l          | w          | \-         | w          | \-         | \-         | l          | \-         | l          | \-         | \-         | \-        | \-              |
| **`SSTRING`**       | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | w          | w             | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`STRING`**        | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | \-         | \-            | w            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`NUMC`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | w          | \-            | \-           | l          | l          | \-         | l          | \-         | \-         | l          | \-         | l          | \-         | \-         | \-        | \-              |
| **`DATS`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | w          | \-            | \-           | l          | x          | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`DATN`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | \-         | \-            | \-           | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`TIMS`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | w          | \-            | \-           | l          | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`TIMN`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | \-         | \-            | \-           | \-         | \-         | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`UTCL`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-         | \-        | \-              |
| **`ACCP`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | l          | \-            | \-           | l          | \-         | \-         | \-         | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-        | \-              |
| **`CLNT`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | x          | \-         | \-         | \-         | \-        | \-              |
| **`LANG`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | l          | \-            | \-           | l          | \-         | \-         | \-         | \-         | \-         | \-         | \-         | x          | \-         | \-         | \-        | \-              |
| **`UNIT`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | x          | \-         | \-        | \-              |
| **`CUKY`**          | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | x          | \-        | \-              |
| **`RAW`**           | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | x         | \-              |
| **`GEOM_EWKB`**     | \-         | \-         | \-         | \-         | \-        | \-             | \-             | \-         | \-         | \-         | \-         | \-            | \-           | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-        | x               |

There are no further restrictions to note in combinations using *x*. The following rules apply to the other combinations:

- In combinations with *w*, the length or the value range of the data type in the first `SELECT` must be long enough for all following `SELECT` lists. If this is not the case, a syntax check warning is raised.

- In combinations using *l*, the lengths of the data types must match exactly.

- In combinations using *d*, the number of decimal places must match exactly.

If the length or value range of the first element does not cover the following elements in combinations with *w*, the value returned by the database can be too great for the data type of the element of the CDS entity. It is still possible to activate the view here, but the content may be truncated or exceptions may be raised in ABAP SQL [queries](../../abap-glossary/abenasql_query_glosry.md) if a type reference is applied to the entity. This is due to the [assignment rules](../../abap-programming-language/abap-database-access/abenselect_into_conversion.md) of the [`INTO`](../../abap-programming-language/abap-database-access/abapinto_clause.md) clause. Assignments to ABAP data objects with a sufficiently large value range, on the other hand, do not cause problems.

**Amounts and Quantities in `UNION` Views**

If the elements of a UNION view are [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md), [CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md), or [CDS calculated quantities](../../abap-glossary/abencds_calculated_quantity_glosry.md), the following rules apply:

- Since the annotation `Metadata.ignorePropagatedAnnotations: true` is mandatory in `UNION` views, all reference annotations are lost and must be provided again within the first `SELECT` branch.

  - For elements of data type `CURR` or `QUAN` as well as for calculated quantities, the reference annotation is mandatory.

  - Elements of other data types lose their reference information and their characteristic as amount or quantity field. The respective reference annotation can be assigned anew to declare the field an amount or quantity field. This is optional.

- Calculated quantity fields can be merged only with other calculated quantity fields. Amount fields and quantity fields can be merged with each other, as long as the data types match (see matrix above).

- For amount fields of type `CURR`, the number of decimal places must match exactly in all `UNION` branches.

- **Note:** Elements of data type `CURR` are incompatible to any other data type. The function [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) can be used to convert an amount field of data type `CURR` into an amount field of data type `DECFLOAT34`.

**Associations in `UNION` Views**

A CDS view entity in which union sets are formed with UNION can expose [CDS associations](../../abap-glossary/abencds_association_glosry.md). Such an association must be defined and exposed in the same way in all SELECT statements merged with UNION. That is, CDS associations that are exposed in the respective SELECT lists must appear in all SELECT statements merged with UNION and the following requirements must be met:

- They have the same [cardinality](../../abap-glossary/abencardinality_glosry.md).

- They must be exposed at the same position in the `SELECT` list using a [path expression](abencds_path_expression_v2.md).

- They must have the same `ON` conditions, that is:

  - The conditions must relate to the same fields in the association source and association target and express the same logic for these fields.

  - The fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) that are listed in an `ON` condition must be at identical positions in the `SELECT` list.

- **Note:** It is **not** required that the associations are defined with the same alias name.

These rules also apply if a CDS association is defined in a data source of a SELECT statement and is exposed by the current statement. From outside, the CDS associations with the same name that are exposed in the individual SELECT lists act like a CDS association exposed by the union set. There are no restrictions on CDS associations that are not exposed in the SELECT lists.

**Nesting of `UNION` Branches**

In CDS view entities, nesting of union clauses is possible. To nest a union clause within another union clause, use parentheses ( ... ). A nested union clause is merged first and its result set is then merged again with the result sets of the other union branches.

Example number 3 below demonstrates nesting of union branches.

## Restrictions

- Defining new [CDS compositions](../../abap-glossary/abencds_composition_glosry.md) is not possible in a `UNION` view. Exposing to-child and to-parent associations that were defined in a data source of the `SELECT` statements is possible.

- Annotations are only allowed in the `SELECT` list of the first `SELECT` statement. In all following branches, annotations are not allowed.

## Hints

- Union sets can be a good way of transforming non-normalized [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) into a normalized view of the data.

- If the length of the value range of an element from the `SELECT` list of the first `SELECT` statement does not cover the associated elements of the following `SELECT` statements, it is advisable to define an appropriate type with a suitable [`CAST`](abencds_cast_expression_v2.md) expression.

- The maximum number of different `SELECT` statements that can be merged using `UNION` depends on the database system. If this number is exceeded, the CDS view entity cannot be activated.

- If the annotation [`@AbapCatalog.entityBuffer.definitionAllowed`](abencds_v2_view_buffering.md) is set to `true` in a union view, a syntax check warning occurs. Union views might return duplicate records with regards to the key fields. The buffer needs a unique key in some scenarios. Therefore, unexpected buffer behavior might occur.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Union set. The element names of the `SELECT` lists must match.

``` abap
 
define view entity ... as 
  select 
    from demo_join1 
      { a as c1, b as c2, c as c3, d as c4 } 
    union 
      select 
        from demo_join2 
          { d as c1, e as c2, f as c3, g as c4 }
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity creates the union of the result sets of two `SELECT` statements. The element `col1` in the first `SELECT` list has the type `INT4`, whereas the associated element `col1` in the second `SELECT` list has the type `INT8`. This is why a syntax check warning is raised. To bypass the warning, `col2` is converted to data type `INT8` using a [`CAST`](abencds_cast_expression_v2.md) expression.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@Metadata.ignorePropagatedAnnotations: true
define view entity DEMO_CDS_UNION_ELEMENT_TYPE_VE
  as select from
    demo_expressions
    {
      id,
      num1                      as col1,
      cast( num1 as abap.int8 ) as col2,
      raw1                      as col3  
    }
union all select from
  demo_expressions
    {
      id,
      numlong1 as             col1,
      numlong1 as             col2,
      abap.raw'AABBCCDDEEAABBCCDDEE' as col3   
    }
```

The class `CL_DEMO_CDS_UNION_ELE_TYPE_VE` uses [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) to access the view four times:

- The first access writes directly to an internal table with the line type of the CDS entity. The access works because the value of the element `col1` matches the value range of the data type `i`.

- The second access is the same as the first but one value in the element `col1` is outside the value range of the data type `i` of the first column of the internal table `result2`. This is why an exception is raised.

- In the third access, the exception is prevented since the data type of the first column of the result set (and hence the data type of the internal table `result3`) is transformed to `int8` using a [`CAST`](../../abap-programming-language/abap-database-access/abensql_cast.md) in ABAP SQL.

- In the fourth access, the exception is prevented due to an appropriate declaration of the data type of the first column of the internal table `result4`.

The recommended method in all cases, however, is to handle the second element using a [`CAST`](abencds_cast_expression_v2.md) in the CDS view entity.
