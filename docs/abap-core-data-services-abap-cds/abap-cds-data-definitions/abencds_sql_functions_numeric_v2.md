---
title: "CDS DDL - CDS View Entity, Numeric Functions"
source_file: abencds_sql_functions_numeric_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, Built-In Functions > CDS DDL - CDS View Entity, sql_functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Numeric Functions

The following table shows the possible numeric [SQL functions](../../abap-glossary/abensql_function_glosry.md) in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), plus the requirements made on the arguments.

<table>
<thead>
<tr class="header">
<th><strong>Function</strong></th>
<th><strong>Result</strong></th>
<th><strong>Valid Argument Types</strong></th>
<th><strong>Result Type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">ABS(arg)</code></a></td>
<td>Absolute amount of <code class="ph codeph">arg</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT8</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">CURR</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">QUAN</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT16</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT34</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">FLTP</code></a></td>
<td>Data type of <code class="ph codeph">arg</code></td>
</tr>
<tr class="even">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">CEIL(arg)</code></a></td>
<td>Returns the first integer that is greater than or equal to the value of <code class="ph codeph">arg</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT16</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT34</code></a></td>
<td>Data type of <code class="ph codeph">arg</code></td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">DIV(arg1, arg2)</code></a></td>
<td>The result of a division of <code class="ph codeph">arg1</code> by <code class="ph codeph">arg2</code> is rounded to an integer. The sign is assigned after the amounts are divided; positive if the arguments have the same sign, and negative if the arguments have different signs. <strong>Exception:</strong> <code class="ph codeph">arg2</code> has the value 0.</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT8</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a>.</td>
<td>Data type of the argument with the greatest value range</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">DIVISION(arg1, arg2, dec)</code></a></td>
<td>Division of <code class="ph codeph">arg1</code> by <code class="ph codeph">arg2</code>. The result is rounded to <code class="ph codeph">dec</code> decimal places.</td>
<td><p><code class="ph codeph">arg1</code>, <code class="ph codeph">arg2</code>: <a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT8</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a></p>
<p><code class="ph codeph">dec</code>: integer <a href="abencds_literal_v2.html">numeric literal</a> greater than or equal to 0. Length must be suitable so that the total of 31 valid places is not exceeded.</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a> with <code class="ph codeph">dec</code> decimal places. The length of the result must not be greater than 31.</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">FLOOR(arg)</code></a></td>
<td>Returns the largest integer number not greater than the value of <code class="ph codeph">arg</code>. Counterpart to <code class="ph codeph">CEIL</code>.</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT16</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT34</code></a></td>
<td>Data type of <code class="ph codeph">arg</code></td>
</tr>
<tr class="even">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">MOD(arg1, arg2)</code></a></td>
<td>Positive or negative integer remainder of the division of <code class="ph codeph">arg1</code> by <code class="ph codeph">arg2</code>.</td>
<td><p><code class="ph codeph">arg1</code>: <a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a>,<a href="abenddic_builtin_types.html"><code class="ph codeph">INT8</code></a></p>
<p><code class="ph codeph">arg2</code>: <a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a></p></td>
<td>Data type of <code class="ph codeph">arg1</code></td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">ROUND(arg, pos)</code></a></td>
<td>Rounded value of <code class="ph codeph">arg</code>. If <code class="ph codeph">pos</code> is greater than 0, the value is rounded to the position <code class="ph codeph">pos</code> on the right of the decimal separator. If this is not the case, position <code class="ph codeph">abs(pos)</code>+1 to the left of the decimal separator is rounded. This results in a 0 if the number of places is not sufficient.</td>
<td><p><code class="ph codeph">arg</code>: <a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT8</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">CURR</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">QUAN</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT16</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT34</code></a></p>
<p><code class="ph codeph">pos</code>: <a href="abencds_literal_v2.html">Literal</a>, field of a data source or <a href="abencds_parameter_v2.html">input parameter</a> of type <a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a>, or <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a></p></td>
<td>When <code class="ph codeph">arg</code> has data type <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, or <code class="ph codeph">INT4</code>, then the result has data type <code class="ph codeph">INT4</code>. For all other data types, the result has the same data type as <code class="ph codeph">arg</code>.</td>
</tr>
</tbody>
</table>

The following can be specified as the arguments `arg`:

- [Literals](abencds_literal_v2.md) of a suitable type.

- [Session variables](abencds_session_variable_v2.md) of a suitable type.

- Suitable [fields](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity.

- [Path expressions](abencds_path_expression_v2.md) that identify a suitable field of a data source [`data_source`](abencds_data_source_v2.md).

- [Input parameters](abencds_parameter_v2.md) from the parameter list [`parameter_list`](abencds_parameter_list_v2.md).

- [Reuse expressions](abencds_reusable_expression_v2.md) using `$projection`

- [SQL-based scalar functions](abencds_sql_scalar_function.md) (if they return a matching type)

- The following built-in functions and expressions (if they return a matching type):

  - Other built-in [SQL functions](abencds_sql_functions_v2.md)

  - [Arithmetic expressions](abencds_arithmetic_expression_v2.md)

  - [Aggregate expressions](abencds_aggregate_functions_v2.md)

  - Type modifications using [`CAST`](abencds_cast_expression_v2.md)

  - [Case distinctions](abencds_case_expression_v2.md) using `CASE`

## Hints

- The SQL functions [`DIV`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md) and [`MOD`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md) behave differently with respect to the signs than the ABAP operators [`DIV`](../../abap-programming-language/abap-processing-internal-data/abenarith_operators.md) and [`MOD`](../../abap-programming-language/abap-processing-internal-data/abenarith_operators.md). In the SQL function `DIV`, the amounts of the arguments are divided and then the sign is assigned (positive if the arguments have the same signs and negative if they have different signs). Accordingly, the result of `MOD` can be negative, so that multiplying the result of `DIV` by `expr2` plus the result of `MOD` produces the value of `expr1`. The ABAP operator [`MOD`](../../abap-programming-language/abap-processing-internal-data/abenarith_operators.md), on the other hand, only produces positive results. See [Example](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md).

- Currently, `CURR` and `QUAN` cannot be used with minus sign.

  This syntax is not valid: `ABS(-curr)`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity applies built-in numeric SQL functions in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_SQL_FNCTNS_NUM_VE` uses `SELECT` to access the view.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SQL_FUNCTIONS_NUM_VE
  as select from demo_expressions
{
  abs(       num1          ) as r_abs,
  ceil(      d34n1         ) as r_ceil,
  floor(     d34n2         ) as r_floor,
  div(       num1, num2    ) as r_div,
  mod(       num1, num2    ) as r_mod,
  division(  dec2, dec3, 3 ) as r_division,
  round(     dec3,  2      ) as r_round1,
  round(     dec3, -2      ) as r_round2
}
```
