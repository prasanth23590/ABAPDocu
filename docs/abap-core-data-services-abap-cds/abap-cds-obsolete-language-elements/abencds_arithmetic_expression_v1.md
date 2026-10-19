---
title: "CDS DDL - DDIC-Based View, arith_expr"
source_file: abencds_arithmetic_expression_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, arith_expr

## Syntax

``` abap
... [-]operand1 [+|-|*|/ [-]operand2 [+|-|*|/ [-]operand3 ... ]] ...  
```

## Description

Arithmetic expression in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). An arithmetic expression uses arithmetic operators to calculate a numeric value from numeric operands. The possible operators are as follows:

| **Operator** | **Meaning**                               |
|--------------|-------------------------------------------|
| `+`          | Adds the operands                         |
| `-`          | Subtracts the right operand from the left |
| `*`          | Multiplies the operands                   |
| `/`          | Divides the left operand by the right     |

A minus sign (`-`) before an operand multiplies the operand by -1. The data type of the operands must be numeric and be based on one of the [built-in data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, or `FLTP`. The following can be specified:

- [Numeric literals](abencds_literal_v1.md) without a domain prefix

- Numeric [fields](abencds_field_v1.md) of a data source [`data_source`](abencds_data_source_v1.md) of the current CDS view.

- [Parameter](abencds_parameter_v1.md) with numeric data type

- [Path expressions](abencds_path_expression_v1.md) that identify a numeric field of a data source [`data_source`](abencds_data_source_v1.md)

- [Built-in functions](abencds_builtin_functions_v1.md) that return a numeric type

- [Casting expressions](abencds_cast_expression_v1.md) that return a numeric type

The subexpressions of an arithmetic expression can be placed in parentheses `(...)`.

The following table shows which data types can be combined using the operators `+`, `-`, and `*` and the data type of the result:

| **`+`, `-`, `*`** | **`INT1`**   | **`INT2`**   | **`INT4`**   | **`INT8`**   | **`DEC`**    | **`CURR`**   | **`QUAN`**   | **`DECFLOAT16`** | **`DECFLOAT34`** | **`FLTP`** |
|-------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|------------------|------------------|------------|
| **`INT1`**        | `INT4`       | `INT4`       | `INT4`       | `INT8`       | `DEC`        | `CURR`       | `QUAN`       | `DECFLOAT16`     | `DECFLOAT34`     | \-         |
| **`INT2`**        | `INT4`       | `INT4`       | `INT4`       | `INT8`       | `DEC`        | `CURR`       | `QUAN`       | `DECFLOAT16`     | `DECFLOAT34`     | \-         |
| **`INT4`**        | `INT4`       | `INT4`       | `INT4`       | `INT8`       | `DEC`        | `CURR`       | `QUAN`       | `DECFLOAT16`     | `DECFLOAT34`     | \-         |
| **`INT8`**        | `INT8`       | `INT8`       | `INT8`       | `INT8`       | `DEC`        | `CURR`       | `QUAN`       | `DECFLOAT16`     | `DECFLOAT34`     | \-         |
| **`DEC`**         | `DEC`        | `DEC`        | `DEC`        | `DEC`        | `DEC`        | `CURR`       | `QUAN`       | `DECFLOAT16`     | `DECFLOAT34`     | \-         |
| **`CURR`**        | `CURR`       | `CURR`       | `CURR`       | `CURR`       | `CURR`       | `CURR`       | `DEC`        | `DECFLOAT16`     | `DECFLOAT34`     | \-         |
| **`QUAN`**        | `QUAN`       | `QUAN`       | `QUAN`       | `QUAN`       | `QUAN`       | `DEC`        | `QUAN`       | `DECFLOAT16`     | `DECFLOAT34`     | \-         |
| **`DECFLOAT16`**  | `DECFLOAT16` | `DECFLOAT16` | `DECFLOAT16` | `DECFLOAT16` | `DECFLOAT16` | `DECFLOAT16` | `DECFLOAT16` | `DECFLOAT16`     | `DECFLOAT34`     | \-         |
| **`DECFLOAT34`**  | `DECFLOAT34` | `DECFLOAT34` | `DECFLOAT34` | `DECFLOAT34` | `DECFLOAT34` | `DECFLOAT34` | `DECFLOAT34` | `DECFLOAT34`     | `DECFLOAT34`     | \-         |
| **`FLTP`**        | \-           | \-           | \-           | \-           | \-           | \-           | \-           | \-               | \-               | `FLTP`     |

The following table shows which data types can be combined using the operator `/` and the data type of the result:

| **`/`**          | **`DECFLOAT16`** | **`DECFLOAT34`** | **`FLTP`** |
|------------------|------------------|------------------|------------|
| **`DECFLOAT16`** | `DECFLOAT16`     | `DECFLOAT34`     | \-         |
| **`DECFLOAT34`** | `DECFLOAT34`     | `DECFLOAT34`     | \-         |
| **`FLTP`**       | \-               | \-               | `FLTP`     |

Note the following special conditions:

- If an expression contains an operand of type `DEC`, `CURR` or `QUAN`, the expression is a decimal expression. In this case, the syntax check checks that the result of each operation is in the value range of the type `DEC` with length 31 and a maximum of 14 decimal places. If any operands are specified that could produce other values, a syntax error occurs.

- If an expression has an operand of type `DECFLOAT16` or `DECFLOAT34`, then it is a decimal floating point expression.

- If an expression has an operand of type `FLTP`, then it is a binary floating point expression, in which all operands must be of type `FLTP`.

- When a division is performed with the operator `/`, it must be a floating point expression. This means the operands must be of type `DECFLOAT16`, `DECFLOAT34`, or [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in combinations shown in the table above, or numeric literals with decimal places. Other numeric data types are not possible. The right operand cannot have the value 0.

Arithmetic expressions can be used as [elements](abencds_select_list_entry_v1.md) of a [`SELECT` list](abencds_select_list_v1.md), where they need alternative element names defined using `AS`.

## Hints

- When a division is performed with two numbers of type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), the SQL function [`DIVISION`](abencds_sql_functions_numeric_v1.md) can be used.

- To convert operands into the appropriate types, [`CAST` expressions](abencds_cast_expression_v1.md) can be used. The built-in conversion function [`FLTP_TO_DEC`](abencds_conv_func_types_v1.md) can be used for the specific task of converting operands of type `FLTP` to packed numbers.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

`SELECT` list of a CDS view with arithmetic expressions.

``` abap
@AbapCatalog.sqlViewName: 'SALES_ORDER_VW' 
define view sales_order as 
  select from snwd_so 
         association [1..*] to snwd_so_i as _item 
           on snwd_so.node_key = _item.parent_key 
         { key snwd_so.node_key, 
               gross_amount, 
               gross_amount - tax_amount as pre_tax_amount, 
               cast(gross_amount as abap.fltp) 
                 + (cast( -gross_amount as abap.fltp) * 0.03) 
                   as reduced_amount, 
            cast(gross_amount as abap.fltp) * 0.03 as overall_savings, 
            _item.so_item_pos as item_position, 
            _item.gross_amount as item_gross_amount, 
            cast(_item.gross_amount as abap.fltp) * 0.97 as item_savings 
 }
```
