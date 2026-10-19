---
title: "CDS DDL - CDS View Entity arith_expr, Amounts and Quantities"
source_file: abencds_arit_exp_calc_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, arith_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity arith_expr, Amounts and Quantities

## Syntax

``` abap
... [-]operand1 [+|-|*|/ [-]operand2 [+|-|*|/ [-]operand3 ... ]] ...  
```

## Description

Arithmetic expression in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) that operates with [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md), [CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md), and [calculated quantities](../abap-cds-data-types/abencds_calculated_quantity.md). The possible operators are as follows:

| **Operator** | **Meaning**                               |
|--------------|-------------------------------------------|
| `+`          | Adds the operands                         |
| `-`          | Subtracts the right operand from the left |
| `*`          | Multiplies the operands                   |
| `/`          | Divides the left operand by the right     |

A minus sign (`-`) before an operand multiplies the operand by -1. The operands must be CDS amount fields, CDS quantity fields, CDS calculated quantities, or numeric values of one of the following data types: `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `DECFLOAT16`, `DECFLOAT34`, `FLTP`, or `QUAN`. The operands can be specified as follows:

- CDS amount fields and CDS quantity fields must be [fields](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity or [SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md) with a suitable return value.

- CDS calculated quantities can be [fields](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity, [reuse expressions](abencds_reusable_expression_v2.md) using `$projection`, or [SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md) with a suitable return value.

- Numeric values can be specified as [literals](abencds_literal_v2.md), [fields](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity, [parameters](abencds_parameter_v2.md), [path expressions](abencds_path_expression_v2.md), [built-in functions](abencds_builtin_functions_v2.md), [SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md), [casting expressions](abencds_cast_expression_v2.md), [case distinctions](abencds_case_expression_v2.md), [aggregate expressions](abencds_aggregate_functions_v2.md), other arithmetic expressions, or [reuse expressions](abencds_reusable_expression_v2.md) using `$projection`. The data type must be appropriate.

The subexpressions of an arithmetic expression can be placed in parentheses `(...)`.

The following table shows how amount fields and quantity fields can be used with different operators and the type of the result:

\|**operands** / **operators**\|**/**\|**\***\|**+, -** \| \|:---\|:---\|:---\|:---\|:---\| \|amount, amount\|calculated quantity\|calculated quantity\| amount \| \|quantity, quantity\|calculated quantity\|calculated quantity\|quantity \| \|calculated quantity, amount\|calculated quantity\| calculated quantity\|amount \| \|amount, quantity\|calculated quantity\|calculated quantity\| - \| \|calculated quantity, number\| calculated quantity\|calculated quantity\|- \| \|calculated quantity, quantity\|calculated quantity \| calculated quantity\| quantity \| \|calculated quantity, calculated quantity\| calculated quantity

\|calculated quantity\|calculated quantity \| \|amount, number\|amount \|amount\|- \| \|number, amount\|calculated quantity \|amount\|- \| \|quantity, number\|quantity \|quantity\|- \| \|number, quantity\|calculated quantity \|quantity\|-\|

Regarding the data types of the operands and of the result, the rules for arithmetic expressions apply, see topic [CDS DDL - CDS View Entity, `arith_expr`](abencds_arithmetic_expression_v2.md). If the result is a calculated quantity, then the data type is always `DECFLOAT34`.

Note the following special conditions:

- If the result of an arithmetic expression is a CDS amount field, CDS quantity field, or a calculated quantity, then it is mandatory to assign a currency key, unit key, or calculated unit using the respective `Semantics` annotation. If no reference is assigned, a syntax check error occurs. References are not inherited or derived from the operands of the arithmetic expression.

- The following rules apply to CDS amount fields of data type ` CURR`:

  - In general, CDS amount fields of data type `CURR` cannot be used directly as operands of arithmetic expressions. They need to be converted to data type `DECFLOAT34` first, using the conversion function [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md).

    There is only one exception to this rule: if all operands are of data type `CURR` and have exactly two decimal places, then they can be used in additions and subtractions (operators + and -).

- A calculated quantity can be changed back to an amount or quantity field using the function [`GET_NUMERIC_VALUE`](abencds_conv_func_unit_curr_v2.md). Then, the required reference can be added using the required annotation, `Semantics.amount.currencyCode` or `Semantics.quantity.unitofMeasure`.

- If one of the operands is of type `FLTP`, then it is a binary floating point expression, in which all operands must be of type `FLTP`.

- When a division is performed with the operator `/`, the right operand cannot have the value 0.

## Hints

- The following conversion functions are available for CDS amount fields and CDS currency fields: [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) and [`GET_NUMERIC_VALUE`](abencds_conv_func_unit_curr_v2.md).

- A calculated unit can be used as reference only once in a view. If a view contains several calculated quantity fields, each field needs a different calculated unit.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

`SELECT` list of a CDS view entity with amounts and quantities in arithmetic expressions:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, calc quan in arith_expr'

define view entity DEMO_CDS_QUAN_ARITH
  as select from DEMO_CDS_CALC_QUANTITY_BASE
{
  key Id,
      Cuky,

      @Semantics.quantity.unitOfMeasure: 'my_calcUnit'
      curr_to_decfloat_amount(Curr102) / Quan10 as my_calcQuan,
      concat( concat( Cuky , '/' ), Unit2 )     as my_calcUnit,

      @Semantics.amount.currencyCode: 'Cuky'
      //both fields have cuky references
      Dec10 + D34n                              as AmountAddition,

      @Semantics.quantity.unitOfMeasure: 'calcUnit'
      $projection.my_calcQuan * 5               as newCalcQuan,
      concat( concat( Cuky , '/' ), Unit2 )     as calcUnit
}
```

- For the calculation of the field `my_calcQuan`, the currency field needs to be normalized using function `CURR_TO_DECFLOAT_AMOUNT`.

- `my_calcQuan` is a calculated quantity of type `DECFLOAT34` and it requires a calculated unit reference.

- `AmountAddition` is a field that adds two amount fields. The result is an amount field again and a new currency key needs to be assigned.

- `newCalcQuan` multiplies a calculated quantity with a number. A calculated unit reference is required. Each calculated unit can be used only once in a view and therefore, a new calculated unit is assigned.
