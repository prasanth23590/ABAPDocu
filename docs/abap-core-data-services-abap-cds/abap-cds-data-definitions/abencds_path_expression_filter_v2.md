---
title: "CDS DDL - CDS View Entity, path_expr, Filter"
source_file: abencds_path_expression_filter_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, path_expr > CDS DDL - CDS View Entity, path_expr, attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, path_expr, Filter

## Syntax

``` abap
... [WHERE] cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v2.md)

## Description

[Filter condition](../../abap-glossary/abenfilter_condition_glosry.md) for the current CDS association. If the join type is explicitly defined with [`INNER|{LEFT OUTER}`](abencds_path_expr_jointype_v2.md), the addition ` WHERE` must be specified explicitly. If this is not the case, `WHERE` must not be specified.

A filter condition is a condition [`cds_cond`](abencds_conditional_expression_v2.md) implemented as an expanded condition for the join when transforming the CDS association into a join.

For the operands of the filter condition of a path expression of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), the following rules apply:

- All relational operators are allowed.

- The Boolean operators `NOT`, `AND`, and `OR` are allowed.

- `lhs` expects a [field](abencds_field_v2.md) of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the current [CDS association](../../abap-glossary/abencds_association_glosry.md) or a [CDS enumerated constant](abencds_enum_field_v2.md).

- `rhs` expects a [field](abencds_field_v2.md) of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the current [CDS association](abencds_association_v2.md), a [literal](abencds_literal_v2.md), a [parameter](abencds_parameter_v2.md), a [session variable](abencds_session_variable_v2.md), an [SQL-based scalar function](abencds_sql_scalar_function.md), or a [built-in function](abencds_builtin_functions_v2.md).

  **Exception:** if the operator `LIKE` is used, then `rhs` must be a character literal.

- Path expressions are not supported.

- Other [expressions](abencds_expressions_v2.md) are not supported.

Special rules apply when the operands of the condition are [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md). These rules are described in the topic [CDS DDL - Using CDS Enumerated Types](abencds_use_enum_type.md).

If no filter condition is specified in the path expression, any default filter condition specified for the [CDS association](abencds_association_v2.md) is used.

## Hint

In [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), the filter conditions of multiple CDS associations are by default compared semantically. If the filter conditions match, the associated join expression is created only once. This generally improves performance.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity contains path expressions with filter conditions in its `SELECT` list that are implemented as join expressions upon activation.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ASSOC_FILTER_VE
  as select from demo_join1
  association to Demo_Cds_Assoc_Join2 as _demo_join2 
    on _demo_join2.d = demo_join1.d
{
  key a,
      _demo_join2[inner where d = '1' ].d               as d_2,
      _demo_join2[inner where d = '1' ].e               as e_2,
      _demo_join2[inner where d = '1' ].
                  _demo_join3[inner where i = '2' ].i   as i_3,
      _demo_join2[inner where d = '1' ].
                  _demo_join3[
                              inner where i = '2' ].j   as j_3
}
```

The following image shows the joins created on the database: ![figure](images_abdoc_path_expr.png)
