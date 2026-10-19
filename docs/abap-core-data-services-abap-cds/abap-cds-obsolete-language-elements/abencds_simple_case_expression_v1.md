---
title: "CDS DDL - DDIC-Based View, simple_case_expr"
source_file: abencds_simple_case_expression_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, case_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, simple_case_expr

## Syntax

``` abap
... CASE operand 
         WHEN operand1 THEN result1 
        [WHEN operand2 THEN result2] 
         ... 
        [ELSE resultn] 
    END ...  
```

## Description

Simple [case distinction](abencds_case_expression_v1.md) (`simple case`) in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The case distinction compares the values of operand `operand` with operands `operand1`, `operand2`, ... and produces the operand `result` as the result after the first `THEN` for which the comparison is true. If no matches are found, the `result` specified after `ELSE` is selected. If `ELSE` is not specified, the result is the [null value](../../abap-glossary/abennull_value_glosry.md).

- The following can be specified for `operand`:

  - [Fields](abencds_field_v1.md) of a data source [`data_source`](abencds_data_source_v1.md) of the current CDS view

  - [Parameters](abencds_parameter_v1.md)

  - [Session variables](abencds_session_variable_v1.md)

  - [Path expressions](abencds_path_expression_v1.md) that identify a field of a data source [`data_source`](abencds_data_source_v1.md)

  - [Built-in functions](abencds_builtin_functions_v1.md)

  - [Arithmetic expressions](abencds_arithmetic_expression_v1.md)

- The following can be specified for `operand1`, `operand2`, ... :

  - [Literals](abencds_literal_v1.md) without a domain prefix

  - Fields of a data source [`data_source`](abencds_data_source_v1.md) of the current CDS view

  - [Path expressions](abencds_path_expression_v1.md) that identify a field of a data source [`data_source`](abencds_data_source_v1.md)

  - [Built-in functions](abencds_builtin_functions_v1.md)

  - A further case distinction

- The following can be specified for `result1`, `result2`, ...:

  - [Literals](abencds_literal_v1.md) without a domain prefix

  - Fields of a data source [`data_source`](abencds_data_source_v1.md) of the current CDS view

  - [Path expressions](abencds_path_expression_v1.md) that identify a field of a data source [`data_source`](abencds_data_source_v1.md)

  - [Aggregate expressions](abencds_aggregate_functions_v1.md)

  - [Casting expressions](abencds_cast_expression_v1.md)

  - [Built-in functions](abencds_builtin_functions_v1.md)

  - [Arithmetic expressions](abencds_arithmetic_expression_v1.md)

  - A further case distinction

The operand `operand` must be [comparable](abencds_cond_expr_types_v1.md) with `operand1`, `operand2`, ... When the CDS view is activated, a result type is determined from the operands `result1`, `result2`, ... that covers their types. The operands must be compatible with each other.

The operands cannot have the [type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`.

## Hints

- The SQL standard specifies the result of a case distinction, but not the order in which the operands are evaluated. Potentially, the result may even be evaluated before the associated condition. This means that any expressions specified as operands must have no side effects and must not be dependent on each other.

- On the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), operands are evaluated in parallel for reasons of optimization. The order in which the operands are evaluated is undefined. If an exception is raised when an operand is evaluated, the entire case distinction is canceled. In this case, it does not matter which conditions apply and the order in which they are listed. For this reason, it is advisable not to use any exceptions in expressions specified as operands. For more information, see the [HANA-specific SQL documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Case distinction in a `SELECT` list.

``` abap
case partner.bp_role 
    when '01' then 'customer' 
    when '02' then 'supplier' 
end as partner_role
```
