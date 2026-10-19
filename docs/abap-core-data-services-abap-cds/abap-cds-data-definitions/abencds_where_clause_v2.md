---
title: "CDS DDL - CDS View Entity, SELECT, WHERE"
source_file: abencds_where_clause_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, WHERE

## Syntax

``` abap
... WHERE cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v2.md)

## Description

Defines a `WHERE` condition for the result set of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). When the CDS view entity is accessed, the result set contains only the data from the data source [`data_source`](abencds_data_source_v2.md) that meets the condition [`cds_cond`](abencds_conditional_expression_v2.md) specified after `WHERE`.

The fields evaluated in the condition do not need to be defined as elements of the CDS view entity in the [`SELECT` list](abencds_select_list_v2.md).

If the view entity makes use of multiple data sources by using join expressions, then all fields specified in the `WHERE` condition must be prefixed with the name of their data source separated by a period (.). The prefix is required in all cases, even if the field names are unique.

The following rules apply to the operands and syntax of the `WHERE` condition of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md):

- All relational operators are allowed. That means all comparison operators are allowed as well as `BETWEEN`, `LIKE`, `IS [NOT] NULL`, and `IS [NOT] INITIAL`.

- The Boolean operators `NOT`, `AND`, and `OR` are supported.

- `lhs` expects a [field](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md), a [path expression](abencds_path_expression_v2.md), a [built-in function](abencds_builtin_functions_v2.md), an [SQL-based scalar function](abencds_sql_scalar_function.md), a [cast expression](abencds_cast_expression_v2.md), or a [CDS enumerated constant](abencds_enum_field_v2.md).

  If a comparison operator is used as relational operator, then `lhs` can also be a [literal](abencds_literal_v2.md), a [case expression](abencds_case_expression_v2.md), or an [arithmetic expression](abencds_arithmetic_expression_v2.md). If `IS NULL` is used as relational operator, then `lhs` can also be a [case expression](abencds_case_expression_v2.md).

- `rhs` can be a [field](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md), a [path expression](abencds_path_expression_v2.md), a [literal](abencds_literal_v2.md), a [parameter](abencds_parameter_v2.md), a [session variable](abencds_session_variable_v2.md), a [cast expression](abencds_cast_expression_v2.md), a [built-in function](abencds_builtin_functions_v2.md), a [SQL-based scalar function](abencds_sql_scalar_function.md), or a [CDS enumerated constant](abencds_enum_field_v2.md).

  If a comparison operator is used as relational operator, then `rhs` can also be a [case expression](abencds_case_expression_v2.md) or an [arithmetic expression](abencds_arithmetic_expression_v2.md).

  - **Exception:** when using the operator `LIKE`, `rhs` must be a character literal.

- A field of a data source can be specified using a path expression [`path_expr`](abencds_path_expression_v2.md).element, as long as the CDS associations of the expression do not have any [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md) as [association target](../../abap-glossary/abenassociation_target_glosry.md) and the cardinality of all traversed associations is to-one:

  - The [cardinality](../../abap-glossary/abencardinality_glosry.md) of the contained [CDS associations](../../abap-glossary/abencds_association_glosry.md) is to-one.

  - The path expression contains the [cardinality specification](abencds_path_expr_card_v2.md) attribute to-one.

    `element` can be used to specify an element of the association target of the last CDS association of the path.

- Other expressions and function calls are not allowed.

Special rules apply when the operands of a `WHERE` condition are [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md). These rules are described in the topic [CDS DDL - Using CDS Enumerated Types](abencds_use_enum_type.md).

**Limitation**

The condition in the WHERE clause must not start with parentheses. This is not valid:

... WHERE (field1 + field2) \* 5 \< 1000

The following workarounds are possible:

- You may change the order of the operands so that the expression written in parentheses does not appear as first operand.

  Example: `... WHERE 5 * (field1 + field2) < 1000`

- You may add `1*` at the start to avoid starting with a parenthesis.

  Example: `... WHERE 1 * (field1 + field2) * 5 < 1000`

## Hint

Unlike in the [`HAVING` condition](abencds_having_clause_v2.md), [aggregate expressions](abencds_aggregate_functions_v2.md) cannot be specified in the `WHERE` condition.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `demo_sales_order_where` has a `WHERE` condition that contains the relational operators `LIKE` and `BETWEEN`, a string function, and a cast expression.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_ORDER_WHERE
  as select from
    demo_sales_order
    association to demo_sales_bupa as _partner
      on $projection.id = _partner.id
    {
      key so_key,
          id,
          company_code,
          _partner.family_name
    }
    where
          _partner.family_name like    'S%'
      and length( _partner.family_name ) = abap.int1'4'
      and created_on between abap.dats'20200101' and abap.dats'20200401'
      and cast( _partner.birth_name as DEMO_BT_BIRTH_NAME
                preserving type )  =       abap.char'Meier'
```
