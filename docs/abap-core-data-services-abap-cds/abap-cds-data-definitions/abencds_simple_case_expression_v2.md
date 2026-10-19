---
title: "CDS DDL - CDS View Entity, simple_case_expr"
source_file: abencds_simple_case_expression_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, case_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, simple_case_expr

## Syntax

``` abap
... CASE operand 
         WHEN operand1 THEN result1 
        [WHEN operand2 THEN result2] 
         ... 
        [{ELSE resultn | ELSE NULL}] 
    END ...  
```

## Description

[Simple case distinction](../../abap-glossary/abensimple_case_glosry.md) in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The case distinction compares the values of operand `operand` with operands `operand1`, `operand2`, ... and returns the first operand specified after `THEN` for which the comparison is true as result.

If no matches are found, the result is determined by the `ELSE` branch:

- `ELSE resultn` returns the value `resultn`.

- `ELSE NULL` returns the [null value](../../abap-glossary/abennull_value_glosry.md).

If `ELSE` is not specified, the result is the [null value](../../abap-glossary/abennull_value_glosry.md)

- For `operand`, `operand1, operand2`, and for `result1, result2`, the following operands can be specified:

  - [Literals](abencds_literal_v2.md)

  - Fields of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity

  - [Parameters](abencds_parameter_v2.md)

  - [Session variables](abencds_session_variable_v2.md)

  - [Arithmetic expressions](abencds_arithmetic_expression_v2.md)

  - [Aggregate expressions](abencds_aggregate_functions_v2.md)

  - A further case distinction

  - [Cast expressions](abencds_cast_expression_v2.md)

  - [Built-in functions](abencds_builtin_functions_v2.md)

  - [SQL-based scalar functions](abencds_sql_scalar_function.md)

  - [Path expressions](abencds_path_expression_v2.md) that identify a field of a data source [`data_source`](abencds_data_source_v2.md)

  - A [reuse expression](abencds_reusable_expression_v2.md) using `$projection`.

  - [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md).

The operand `operand` must be [comparable](abencds_cond_expr_types_v2.md) with `operand1`, `operand2`, ... When the CDS view entity is activated, a result type is determined from the operands `result1`, `result2`, .... The operands of the `THEN` and `ELSE` branches must be compatible with each other.

The operands can have any [built-in data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) except for `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`.

Special rules apply to CDS enumerated elements in case expressions. They are described in the topic [CDS DDL - Using CDS Enumerated Types](abencds_use_enum_type.md).

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

The example shows a CDS view entity with two case distinctions.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SIMPLE_CASE
  with parameters
    p_number : abap.dec(12,2)
  as select from demo_employees
{
  key name,
      case name
        when 'Anna' then 'X'
        when 'Lisa' then 'Y'
        else '-'
      end as first_name,

      case $parameters.p_number
        when salary
        then utcl_current()
        else null
      end as salary
}
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows a CDS view entity with two case distinctions using amount and quantity fields.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED

define view entity DEMO_CDS_SIMPLE_CASE_1
  as select from DEMO_CDS_CALC_QUANTITY_BASE
{
  key Id,

      //amounts and calculated quantities are compatible,
      //result is a calculated quantity

      @Semantics.quantity.unitOfMeasure: 'Calcunit'
      case
      when Char1 = abap.char'A'
      then Dec10                //cuky reference -> amount field
      when Char1 = abap.char'B'
      then 100 / Dec10          //calculated quantity
      else 0
      end                                   as calcQuan,
      Cuky,
      concat( concat( Cuky , '/' ), Unit2 ) as calcUnit,


      //CURR requires conversion to DECFLOAT34

      @Semantics.amount.currencyCode : 'cuky'
      case when Char1 = abap.char'A'
      then CURR_TO_DECFLOAT_AMOUNT( Curr102 )
      else Dec10                //cuky reference
      end                                   as CurrConv
}
```
