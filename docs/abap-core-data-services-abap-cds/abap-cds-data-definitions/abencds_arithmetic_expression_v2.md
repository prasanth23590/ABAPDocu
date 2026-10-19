---
title: "CDS DDL - CDS View Entity, arith_expr"
source_file: abencds_arithmetic_expression_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, arith_expr

## Syntax

``` abap
... [-]operand1 [+|-|*|/ [-]operand2 [+|-|*|/ [-]operand3 ... ]] ...  
```

## Description

[Arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). An arithmetic expression uses arithmetic operators to calculate a numeric value from numeric operands. The possible operators are as follows:

| **Operator** | **Meaning**                               |
|--------------|-------------------------------------------|
| `+`          | Adds the operands                         |
| `-`          | Subtracts the right operand from the left |
| `*`          | Multiplies the operands                   |
| `/`          | Divides the left operand by the right     |

A minus sign (`-`) before an operand multiplies the operand by -1. The data type of the operands must be numeric and be based on one of the [built-in data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `DECFLOAT16`, `DECFLOAT34`, `FLTP`, or `QUAN`. The following can be specified:

- [Numeric literals](abencds_literal_v2.md)

- Numeric [fields](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity

- [Parameter](abencds_parameter_v2.md) with numeric data type

- [Path expressions](abencds_path_expression_v2.md) that identify a numeric field of a data source [`data_source`](abencds_data_source_v2.md)

- [Built-in functions](abencds_builtin_functions_v2.md) that return a numeric type

- [SQL-based scalar functions](abencds_sql_scalar_function.md) that return a numeric type

- [Casting expressions](abencds_cast_expression_v2.md) that return a numeric type

- [Case distinctions](abencds_case_expression_v2.md) that return a numeric type

- [Aggregate expressions](abencds_aggregate_functions_v2.md) that return a numeric type

- Another arithmetic expression

- A [reuse expression](abencds_reusable_expression_v2.md) using `$projection`

The subexpressions of an arithmetic expression can be placed in parentheses `(...)`.

The following table shows which data types can be combined using the operators `+`, `-`, and `*` and the data type of the result:

<table>
<thead>
<tr class="header">
<th><strong><code class="ph codeph">+</code>, <code class="ph codeph">-</code>, <code class="ph codeph">*</code></strong></th>
<th><strong><code class="ph codeph">INT1</code></strong></th>
<th><strong><code class="ph codeph">INT2</code></strong></th>
<th><strong><code class="ph codeph">INT4</code></strong></th>
<th><strong><code class="ph codeph">INT8</code></strong></th>
<th><strong><code class="ph codeph">DEC</code></strong></th>
<th><strong><code class="ph codeph">DECFLOAT16</code></strong></th>
<th><strong><code class="ph codeph">DECFLOAT34</code></strong></th>
<th><strong><code class="ph codeph">FLTP</code></strong></th>
<th><strong><code class="ph codeph">QUAN</code></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><code class="ph codeph">INT1</code></strong></td>
<td><code class="ph codeph">INT4</code></td>
<td><code class="ph codeph">INT4</code></td>
<td><code class="ph codeph">INT4</code></td>
<td><code class="ph codeph">INT8</code></td>
<td><code class="ph codeph">DEC</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td>-</td>
<td><code class="ph codeph">QUAN</code></td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">INT2</code></strong></td>
<td><code class="ph codeph">INT4</code></td>
<td><code class="ph codeph">INT4</code></td>
<td><code class="ph codeph">INT4</code></td>
<td><code class="ph codeph">INT8</code></td>
<td><code class="ph codeph">DEC</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td>-</td>
<td><code class="ph codeph">QUAN</code></td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">INT4</code></strong></td>
<td><code class="ph codeph">INT4</code></td>
<td><code class="ph codeph">INT4</code></td>
<td><code class="ph codeph">INT4</code></td>
<td><code class="ph codeph">INT8</code></td>
<td><code class="ph codeph">DEC</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td>-</td>
<td><code class="ph codeph">QUAN</code></td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">INT8</code></strong></td>
<td><code class="ph codeph">INT8</code></td>
<td><code class="ph codeph">INT8</code></td>
<td><code class="ph codeph">INT8</code></td>
<td><code class="ph codeph">INT8</code></td>
<td><code class="ph codeph">DEC</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td>-</td>
<td><code class="ph codeph">QUAN</code></td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">DEC</code></strong></td>
<td><code class="ph codeph">DEC</code></td>
<td><code class="ph codeph">DEC</code></td>
<td><code class="ph codeph">DEC</code></td>
<td><code class="ph codeph">DEC</code></td>
<td><code class="ph codeph">DEC</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td>-</td>
<td><code class="ph codeph">QUAN</code></td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">DECFLOAT16</code></strong></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT16``DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td>-</td>
<td><code class="ph codeph">DECFLOAT16</code></td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">DECFLOAT34</code></strong></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td>-</td>
<td><code class="ph codeph">DECFLOAT34</code></td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">FLTP</code></strong></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td><code class="ph codeph">FLTP</code></td>
<td>-</td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">QUAN</code></strong></td>
<td><code class="ph codeph"> QUAN</code></td>
<td><code class="ph codeph">QUAN</code></td>
<td><code class="ph codeph">QUAN</code></td>
<td><code class="ph codeph">QUAN</code></td>
<td><code class="ph codeph">QUAN</code></td>
<td><code class="ph codeph">DECFLOAT16</code></td>
<td><code class="ph codeph">DECFLOAT34</code></td>
<td>-</td>
<td><p><code class="ph codeph">*</code>: <code class="ph codeph">DECFLOAT34</code></p>
<p><code class="ph codeph">+</code>, <code class="ph codeph">-</code>: <code class="ph codeph">QUAN</code></p></td>
</tr>
</tbody>
</table>

The following table shows which data types can be combined using the operator `/` and the data type of the result:

\|**`/`**\|`INT1`\|`INT2`\|`INT4`\| `INT8`\|`DEC`\| **`DECFLOAT16`**\|**`DECFLOAT34`**\|**`FLTP`**\|`QUAN` \| \|:---\|:---\|:---\|:---\| \|**`INT1`**\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|-\|`DECFLOAT34` \| \|**`INT2`**\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|-\|`DECFLOAT34` \| \|**`INT4`**\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|-\|`DECFLOAT34` \| \|**`INT8`**\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|-\|`DECFLOAT34` \| \|**`DEC`**\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|-\|`DECFLOAT34` \| \|**`DECFLOAT16`**\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT16`\|`DECFLOAT34`\|-\|`DECFLOAT34` \| \|**`DECFLOAT34`**\|`DECFLOAT34`\| `DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\|-\|`DECFLOAT34` \| \|**`FLTP`**\|-\|-\|-\|-\|-\|-\|-\|`FLTP`\|- \| \|**`QUAN`**\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34`\|`DECFLOAT34`\| `DECFLOAT34`\|`DECFLOAT34` \|-\|`DECFLOAT34`\|

It is also possible to use [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md) and [CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md) in arithmetic expressions. The result type can be a [calculated quantity](../abap-cds-data-types/abencds_calculated_quantity.md). The rules for amounts and quantities in arithmetic expressions in CDS view entities are explained in topic [CDS View Entity, `arith_exp`, Amounts and Quantities](abencds_arit_exp_calc_v2.md).

Note the following special conditions:

- If an expression contains an operand of type `DEC`, the expression is a decimal expression. In this case, the syntax check checks that the result of each operation is in the value range of the type `DEC` with length 31 and a maximum of 14 decimal places. If any operands are specified that could produce other values, a syntax error occurs.

- If an expression has an operand of type `DECFLOAT16` or `DECFLOAT34`, then it is a decimal floating point expression.

- If an expression has an operand of type `FLTP`, then it is a binary floating point expression, in which all operands must be of type `FLTP`.

- When a division is performed with the operator `/`, the right operand cannot have the value 0.

- If an operand of an arithmetic expression has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the entire arithmetic expression is the null value.

- Data type `CURR` is also possible, but only under the following conditions:

  - All operands must be of type `CURR` and have exactly two decimal places.

  - `CURR` is only allowed in additions and subtractions (operators + and -). Not in multiplications and divisions.

Operand positions:

- Arithmetic expressions can be used as [elements](abencds_select_list_entry_v2.md) of a [`SELECT` list](abencds_select_list_v2.md), and there they need alternative element names defined using `AS`.

- An arithmetic expression can be used as the operand of an [aggregate expression](abencds_aggregate_functions_v2.md), a [built-in function](abencds_builtin_functions_v2.md), a [cast expression](abencds_cast_expression_v2.md), or a [case distinction](abencds_case_expression_v2.md).

- An arithmetic expression can be used in the condition `cds_cond` as operand `lhs` of a [complex case distinction](abencds_searched_case_expr_v2.md).

## Hints

- When a division is performed with two numbers of type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), the SQL function [`DIVISION`](abencds_sql_functions_numeric_v2.md) can be used.

- To convert operands into the appropriate types, [`CAST` expressions](abencds_cast_expression_v2.md) can be used. The built-in conversion function [`FLTP_TO_DEC`](abencds_conv_func_types_v2.md) can be used for the specific task of converting operands of type `FLTP` to packed numbers.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

`SELECT` list of a CDS view entity with arithmetic expressions.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SO_ARITH_EXPR
  as select from
    demo_so_inv_he
    association to DEMO_SALES_CDS_SO_I as _item
      on $projection.so_key = _item.so_item_key
    {
      key so_key,
          @Semantics.amount.currencyCode: 'currency_code'
          gross_amount,
          cast(gross_amount as abap.dec(10, 2)) -
          cast(tax_amount as abap.dec(10,2))    as pre_tax_amount,
          cast(gross_amount as abap.fltp) * 0.33  
                                                as overall_savings,
          _item.posnr                           as item_position,
          _item.gross_amount                    as item_gross_amount,
          cast(_item.gross_amount as abap.fltp) * 0.97 
                                                as item_savings,
          @Semantics.amount.currencyCode: 'currency_code'
          net_amount + tax_amount               as gross,
          currency_code,
          _item.currency
    }
```
