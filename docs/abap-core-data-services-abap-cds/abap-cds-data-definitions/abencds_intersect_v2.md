---
title: "CDS DDL - CDS View Entity, SELECT, INTERSECT"
source_file: abencds_intersect_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, clauses > CDS DDL - CDS View Entity, Set Operators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, INTERSECT

## Syntax

``` abap
... INTERSECT select_statement ...  
```

[`select_statement`](abencds_select_statement_v2.md)

## Description

The [set operator](../../abap-glossary/abencds_set_operators_glosry.md) `INTERSECT` returns all distinct rows that are included in all result sets of multiple [`SELECT` statements](abencds_select_statement_v2.md) of [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md). As a prerequisite, the result sets must have the same number of elements and the element pairs that occur in the same position of the result set must have a compatible data type. All data types are supported except for [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LCHR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LRAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A view using `INTERSECT` can itself be the left side of a further view using `INTERSECT`.

## Prerequisite

As a prerequisite for using the statement `INTERSECT` in a CDS view entity, the CDS view entity annotation [`Metadata.ignorePropagatedAnnotations: true`](abencds_view_entity_anno.md) must be specified.

**Rules for the Elements of a View Using `INTERSECT`**

The first SELECT statement defines the signature of the INTERSECT view. The elements of the result set of the INTERSECT view have the following properties:

- Element names

  The direct element names or the alternative element names defined using `AS` must match for each column in the [`SELECT` lists](abencds_select_list_v2.md) of all `SELECT` statements and are used.

- Key elements

  They key elements of all `SELECT` lists must match. Otherwise, a syntax check error occurs.

- Element annotations

  Only the `SELECT` list of the first `SELECT` statement can define [element annotations](abencds_element_annotations_v2.md). In all subsequent branches, element annotations are forbidden.

- Data type

  - The `SELECT` list of the first `SELECT` statement determines the DDIC data type of each element of the CDS entity.

  - The data type used to create the result set on the database is a data type whose value range covers the data types of the associated columns of all result sets involved.

The following table shows which data types can be combined with each other in a view using INTERSECT. On the left side, the data types of the SELECT list of the first SELECT statement are listed and the other columns specify with which data types of the following SELECT lists they can be combined.

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

**Amounts and Quantities in `INTERSECT` Views**

If the elements of a UNION view are [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md), [CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md), or [CDS calculated quantities](../../abap-glossary/abencds_calculated_quantity_glosry.md), the following rules apply:

- Since the annotation `Metadata.ignorePropagatedAnnotations: true` is mandatory in `UNION` views, all reference annotations are lost and must be provided again within the first `SELECT` branch.

  - For elements of data type `CURR` or `QUAN` as well as for calculated quantities, the reference annotation is mandatory.

  - Elements of other data types lose their reference information and their characteristic as amount or quantity field. The respective reference annotation can be assigned anew to declare the field an amount or quantity field. This is optional.

- Calculated quantity fields can be merged only with other calculated quantity fields. Amount fields and quantity fields can be merged with each other, as long as the data types match (see matrix above).

- For amount fields of type `CURR`, the number of decimal places must match exactly in all `UNION` branches.

- **Note:** Elements of data type `CURR` are incompatible to any other data type. The function [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) can be used to convert an amount field of data type `CURR` into an amount field of data type `DECFLOAT34`.

**Associations in Views Using `INTERSECT`**

A CDS view entity in which result sets are formed with INTERSECT can define and expose [CDS associations](../../abap-glossary/abencds_association_glosry.md). Such an association must be defined and exposed in the same way in all SELECT statements combined with INTERSECT. That is, CDS associations that are exposed in the respective SELECT lists must appear in all SELECT statements combined with INTERSECT and the following requirements must be met:

- They have the same [cardinality](../../abap-glossary/abencardinality_glosry.md).

- They must be exposed at the same position in the `SELECT` list using a [path expression](abencds_path_expression_v2.md).

- They must have the same `ON` conditions, that is:

  - The conditions must relate to the same fields in the association source and association target and express the same logic for these fields.

  - The fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) that are listed in an `ON` condition must be at identical positions in the `SELECT` list.

- **Note:** It is **not** required that the associations are defined with the same alias name.

These rules also apply if a CDS association is defined in a data source of a SELECT statement and is exposed by the current statement. From outside, the CDS associations with the same name that are exposed in the individual SELECT lists act like a CDS association exposed by the INTERSECT result set. There are no restrictions on CDS associations that are not exposed in the SELECT lists.

**Nesting of `INTERSECT` Branches**

In CDS view entities, nesting of INTERSECT clauses is possible. To nest an INTERSECT clause within another INTERSECT clause, use brackets ( ... ). A nested INTERSECT clause is merged first and its result set is then merged again with the result sets of the other INTERSECT branches.

## Restrictions

- Defining new to-child and to-parent associations is not possible in a view using `INTERSECT`. Exposing to-child and to-parent associations that were defined in the data source of the `SELECT` statement is possible.

- Annotations are only allowed in the `SELECT` list of the first `SELECT` statement. In all following branches, annotations are not allowed.

## Hints

- If the length of the value range of an element from the `SELECT` list of the first `SELECT` statement does not cover the associated elements of the following `SELECT` statements, it is advisable to define an appropriate type with a suitable [`CAST`](abencds_cast_expression_v2.md) expression.

- The maximum number of different `SELECT` statements that can be merged using `INTERSECT` depends on the database system. If this number is exceeded, the CDS view entity cannot be activated.

- The addition `ALL` is not available for the set operator `INTERSECT`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity combines the result sets of two `SELECT` statements using `INTERSECT`. It returns only those rows returned by both queries.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, set operator INTERSECT'
@Metadata.ignorePropagatedAnnotations: true

define view entity DEMO_CDS_INTERSECT 
as select from sflight
{
  carrid,
  connid
}
where price > 1000

intersect

select from spfli
{
  carrid,
  connid
}
```

The class `CL_DEMO_CDS_INTERSECT` uses [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) to access the view and it displays the result set.
