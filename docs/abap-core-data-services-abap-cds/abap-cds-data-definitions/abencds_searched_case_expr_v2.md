---
title: "CDS DDL - CDS View Entity, searched_case_expr"
source_file: abencds_searched_case_expr_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, case_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, searched_case_expr

## Syntax

``` abap
... CASE WHEN cds_cond1 THEN result1 
        [WHEN cds_cond2 THEN result2] 
        [WHEN cds_cond3 THEN result3] 
          ... 
        [{ELSE resultn | ELSE NULL}] 
    END ...  
```

[`cds_cond1`](abencds_conditional_expression_v2.md) · [`cds_cond2`](abencds_conditional_expression_v2.md) · [`cds_cond3`](abencds_conditional_expression_v2.md)

## Description

[Complex case distinction](../../abap-glossary/abencomplex_case_glosry.md) (searched case) in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The case distinction evaluates the conditions [`cds_cond1`](abencds_conditional_expression_v2.md), [`cds_cond2`](abencds_conditional_expression_v2.md), ... and returns the first operand specified after `THEN` for which the comparison is true as result. If none of the conditions are true, the result is determined by the `ELSE` branch:

- `ELSE resultn` returns the value `resultn`.

- `ELSE NULL` returns the [null value](../../abap-glossary/abennull_value_glosry.md).

If `ELSE` is not specified, the result is the [null value](../../abap-glossary/abennull_value_glosry.md).

The following rules apply to the conditions specified after `WHEN`:

- All [relational operators](abencds_conditional_expression_v2.md) are allowed. That means that comparison operators, `BETWEEN`, `LIKE`, `IS NULL` and `IS INITIAL` are allowed.

- The Boolean operators `NOT`, `AND`, and `OR` are allowed.

- `lhs` expects a [field](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md), a [path expression](abencds_path_expression_v2.md), a [built-in function](abencds_builtin_functions_v2.md), an [SQL-based scalar function](abencds_sql_scalar_function.md), or a [cast expression](abencds_cast_expression_v2.md).

  If a comparison operator is used, then `lhs` can also be an [aggregate function](abencds_aggregate_functions_v2.md), a [case expression](abencds_case_expression_v2.md), an arithmetic expression, or a parameter. If the relational operator `IS NULL` is used, then `lhs` can also be another [case expression](abencds_case_expression_v2.md), an [arithmetic expression](abencds_arithmetic_expression_v2.md), or a [parameter](abencds_parameter_v2.md).

- `rhs` can be a [field](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md), a [literal](abencds_literal_v2.md), a [parameter](abencds_parameter_v2.md), a [session variable](abencds_session_variable_v2.md), a [cast expression](abencds_cast_expression_v2.md), a [reuse expression](abencds_reusable_expression_v2.md), a [built-in function](abencds_builtin_functions_v2.md), an [SQL-based scalar function](abencds_sql_scalar_function.md), or a path expression.

  If a comparison operator is used, then `rhs` can also be an [aggregate function](abencds_aggregate_functions_v2.md), a [case expression](abencds_case_expression_v2.md), or an [arithmetic expression](abencds_arithmetic_expression_v2.md). **Exception:** for the operator [`LIKE`](abencds_cond_expr_like_v2.md), `rhs` must be a character literal.

- A field of a data source can be specified using a path expression [`path_expr`](abencds_path_expression_v2.md).element, as long as the CDS associations of the expression do not have any [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md) as [association targets](../../abap-glossary/abenassociation_target_glosry.md) and the expression is unique:

  - The [cardinality](../../abap-glossary/abencardinality_glosry.md) of the contained [CDS associations](../../abap-glossary/abencds_association_glosry.md) is to-one.

  - The path expression contains the [cardinality specification](abencds_path_expr_card_v2.md) attribute to-one.

    `element` can be used to specify an element of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association of the path.

Special rules apply to [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md) in complex case expressions. They are described in the topic [CDS DDL - Using CDS Enumerated Types](abencds_use_enum_type.md).

**Rules for Amounts and Quantities**

The result data type of a case expression is determined by all THEN branches and the ELSE branch. If the result data type is a [CDS amount field](../../abap-glossary/abencds_amount_field_glosry.md), a [CDS quantity field](../../abap-glossary/abencds_quantity_glosry.md), or a [CDS calculated quantity](../../abap-glossary/abencds_calculated_quantity_glosry.md), a reference annotation must be assigned. The following table shows how the result data type is calculated if one or more of the operands result1, result2, ... are amount and/or quantity fields.

| **operand1/operand2**   | **Amount**          | \*\* Quantity\*\*   | \*\* Calculated Quantity\*\* | **Number**          |
|-------------------------|---------------------|---------------------|------------------------------|---------------------|
| **Amount**              | amount              | calculated quantity | calculated quantity          | calculated quantity |
| **Quantity**            | calculated quantity | quantity            | calculated quantity          | calculated quantity |
| **Calculated Quantity** | calculated quantity | calculated quantity | calculated quantity          | calculated quantity |
| **Number**              | calculated quantity | calculated quantity | calculated quantity          | number              |

- It is not mandatory that the operands and the result point to the same reference field.

- The following rules apply to amount fields of data type `CURR`:

  - fields of data type `CURR` are compatible only to other amount fields of data type `CURR` and only if they have exactly the same number of decimal places.

  - To combine an amount field of data type `CURR` with a field of another data type, a conversion to data type `DECFLOAT34` using the conversion function [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) is required.

## Hints

- The SQL standard specifies the result of a case distinction, but not the order in which the operands are evaluated. Potentially, the result may even be evaluated before the associated condition. This means that any expressions specified as operands must have no side effects and must not be dependent on each other.

- On the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), operands are evaluated in parallel for reasons of optimization. The order in which the operands are evaluated is undefined. If an exception is raised when an operand is evaluated, the entire case distinction is canceled. In this case, it does not matter which conditions apply and the order in which they are listed. For this reason, it is advisable not to use any exceptions in expressions specified as operands. For more information, see the [HANA-specific SQL documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity has a complex case distinction in the `SELECT` list.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_searched_case_ve
  as select from
    spfli
    {
      key carrid,
      key connid,
          distance,
          distid,
          case
            when distance >= 2000 then 'long-haul flight'
            when distance >= 1000 and
                 distance <  2000 then 'medium-haul flight'
            when distance <  1000 then 'short-haul flight'
                                  else 'error'
          end as flight_type
    }
    where
      distid = 'MI'
```

The class `CL_DEMO_CDS_SEARCHED_CASE_VE` uses [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) to access the view and shows the result.
