---
title: "sql_func - Numeric Functions"
source_file: abensql_arith_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Numeric Functions

## Syntax

``` abap
... func( arg1[, arg2] ... ) ...  
```

## Description

Calls a numeric function `func` as an [SQL expression](abapsql_expr.md) or operand of an expression in ABAP SQL. The arguments `arg1`, `arg2`, ... of the function are specified as a comma-separated list in parentheses. A blank must be placed after the opening parenthesis and in front of the closing parenthesis.

The following table shows the numeric functions that can be specified as SQL expressions and the requirements on the arguments. The meaning of the functions can be found under [SQL Functions for Numeric Values](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md). The value *x* in the ABAP SQL In-Memory Engine column indicates that the function can be executed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) and that the use of [this function](abensql_engine_expr.md) does not bypass [table buffering](../../abap-glossary/abentable_buffering_glosry.md) does not cause the transport of an internal table accessed with [`FROM @itab`](abapselect_itab.md) to the database.

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Result</strong></th>
<th><strong>Valid Argument Types</strong></th>
<th><strong>Result Type</strong></th>
<th><strong>ABAP SQL In-Memory Engine</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">ABS( sql_exp )</code></a></td>
<td>Absolute amount of <code class="ph codeph">sql_exp</code></td>
<td>All numeric types except the <a href="abenddic_decimal_floating_point.html">replacement types for decimal floating point numbers</a></td>
<td>Type of the argument.</td>
<td>x</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">CEIL( sql_exp )</code></a></td>
<td>Rounded to the first integer that is greater than or equal to the value of <code class="ph codeph">sql_exp</code></td>
<td><code class="ph codeph">DECFLOAT16</code> and <code class="ph codeph">DECFLOAT34</code> as well as <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, and <code class="ph codeph">QUAN</code> with decimal places</td>
<td><p><code class="ph codeph">DEC(MIN(p-s+1,31),0)</code> for <code class="ph codeph">DEC(p,s)</code> argument.</p>
<p>Respective decimal floating point type for decimal floating point argument.</p></td>
<td>x</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">DIV( sql_exp1,sql_exp2 )</code></a></td>
<td>The result of a division of <code class="ph codeph">sql_exp1</code> by <code class="ph codeph">sql_exp2</code> is rounded to an integer. The sign is assigned after the amounts are divided; positive if the arguments have the same sign, and negative if the arguments have the same sign, and negative if the arguments have different signs. <strong>Exception:</strong> <code class="ph codeph">sql_exp2</code> has the value 0.</td>
<td><code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, and <code class="ph codeph">INT8</code> plus <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, and <code class="ph codeph">QUAN</code> without decimal places</td>
<td><p>Type of the argument with the greatest value range for integer types.</p>
<p>For expressions involving <code class="ph codeph">DEC</code> types, <code class="ph codeph">DEC</code> without decimal places that can contain the largest possible result for the first argument.</p></td>
<td>x</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">DIVISION( sql_exp1,sql_exp2,dec )</code></a></td>
<td>Division of <code class="ph codeph">sql_exp1</code> by <code class="ph codeph">sql_exp2</code>. The result is rounded to <code class="ph codeph">dec</code> decimal places.</td>
<td><p><code class="ph codeph">sql_exp1</code>, <code class="ph codeph">sql_exp2</code>: <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, <code class="ph codeph">INT8</code>, <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, and <code class="ph codeph">QUAN</code></p>
<p><code class="ph codeph">dec</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, <code class="ph codeph">int8</code> greater than or equal to 0 and not greater than the maximum value of 6 and the length of <code class="ph codeph">sql_exp2</code> plus the number of decimal places of <code class="ph codeph">sql_exp1</code> plus 1</p></td>
<td><code class="ph codeph">DEC</code> with <code class="ph codeph">dec</code> decimal places. The length of the result is the length of <code class="ph codeph">sql_exp1</code> minus the decimal places in <code class="ph codeph">sql_exp1</code> plus the decimal places in <code class="ph codeph">sql_exp2</code> plus <code class="ph codeph">dec</code>. This value must not be greater than 31.</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">FLOOR( sql_exp )</code></a></td>
<td>Largest integer number not greater than the value of <code class="ph codeph">sql_exp</code></td>
<td><code class="ph codeph">DECFLOAT16</code> and <code class="ph codeph">DECFLOAT34</code> as well as <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, and <code class="ph codeph">QUAN</code> with decimal places</td>
<td><p><code class="ph codeph">DEC(MIN(p-s+1,31),0)</code> for <code class="ph codeph">DEC(p,s)</code> argument.</p>
<p>Respective decimal floating point type for decimal floating point argument.</p></td>
<td>x</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">GREATEST( sql_exp1, sql_exp2[, sql_expn] )</code></a></td>
<td>Largest value of a set of arguments.</td>
<td><code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, <code class="ph codeph">INT8</code>, <code class="ph codeph">DEC</code>, <code class="ph codeph">DECFLOAT16</code>, <code class="ph codeph">DECFLOAT34</code>, <code class="ph codeph">FLTP</code>, <code class="ph codeph">CHAR</code>, <code class="ph codeph">SSTRING</code>, <code class="ph codeph">DATN</code>, <code class="ph codeph">DATS</code>, <code class="ph codeph">TIMN</code>, <code class="ph codeph">TIMS</code>,<code class="ph codeph">ACCP</code>, <code class="ph codeph">UTCLONG</code>, <code class="ph codeph">NUMC</code>, <code class="ph codeph">CLNT</code>, <code class="ph codeph">LANG</code>, <code class="ph codeph">CURR</code>, <code class="ph codeph">CUKY</code>, <code class="ph codeph">QUAN</code>, and <code class="ph codeph">UNIT</code></td>
<td>Type of the argument.</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">LEAST( sql_exp1, sql_exp2[, sql_expn] )</code></a></td>
<td>Smallest value of a set of arguments.</td>
<td><code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, <code class="ph codeph">INT8</code>, <code class="ph codeph">DEC</code>, <code class="ph codeph">DECFLOAT16</code>, <code class="ph codeph">DECFLOAT34</code>, <code class="ph codeph">FLTP</code>, <code class="ph codeph">CHAR</code>, <code class="ph codeph">SSTRING</code>, <code class="ph codeph">DATN</code>, <code class="ph codeph">DATS</code>, <code class="ph codeph">TIMN</code>, <code class="ph codeph">TIMS</code>,<code class="ph codeph">ACCP</code>, <code class="ph codeph">UTCLONG</code>, <code class="ph codeph">NUMC</code>, <code class="ph codeph">CLNT</code>, <code class="ph codeph">LANG</code>, <code class="ph codeph">CURR</code>, <code class="ph codeph">CUKY</code>, <code class="ph codeph">QUAN</code>, and <code class="ph codeph">UNIT</code></td>
<td>Type of the argument.</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">MOD( sql_exp1,sql_exp2 )</code></a></td>
<td>Positive or negative integer remainder of the division of <code class="ph codeph">sql_exp1</code> by <code class="ph codeph">sql_exp2</code></td>
<td><code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, and <code class="ph codeph">INT8</code> plus <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, and <code class="ph codeph">QUAN</code> without decimal places</td>
<td>Type of the argument with the greatest value range.</td>
<td>x</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_numeric.html"><code class="ph codeph">ROUND( sql_exp,pos )</code></a></td>
<td>Rounded value of <code class="ph codeph">sql_exp</code>. If <code class="ph codeph">pos</code> is greater than 0, the value is rounded to the position <code class="ph codeph">pos</code> on the right of the decimal separator. If this is not the case, position <code class="ph codeph">abs(pos)</code>+1 to the left of the decimal separator is rounded. This results in a 0 if the number of places is not sufficient.</td>
<td><p><code class="ph codeph">sql_exp</code>: <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, <code class="ph codeph">INT8</code>, <code class="ph codeph">DEC</code>, <code class="ph codeph">DECFLOAT16</code>, <code class="ph codeph">DECFLOAT34</code>, <code class="ph codeph">CURR</code>, and <code class="ph codeph">QUAN</code></p>
<p><code class="ph codeph">pos</code>: <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, and <a href="abensql_null.html">null expression</a></p></td>
<td><p>Type of <code class="ph codeph">sql_exp</code>, where <code class="ph codeph">INT1</code> and <code class="ph codeph">INT2</code> are converted to <code class="ph codeph">INT4</code>, and <code class="ph codeph">CURR</code> and <code class="ph codeph">QUAN</code> are converted to <code class="ph codeph">DEC</code>.</p>
<p><code class="ph codeph">DEC(MIN(p-s+1,31),0)</code> for a <code class="ph codeph">DEC(p,s)</code> argument.</p></td>
<td>-</td>
</tr>
</tbody>
</table>

The arguments `sql_exp`, `sql_exp1`, `sql_exp3`, and `pos` can be any [SQL expressions](abapsql_expr.md) with the appropriate data types. The possible types are specified as built-in [dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The possible data types for literals, host variables, and host expressions are the ABAP types [assigned](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the dictionary types above.

If an argument of a numeric function has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the full numeric function is the null value.

## Hints

- The SQL functions [`DIV`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md) and [`MOD`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md) behave differently with respect to the signs than the ABAP operators [`DIV`](../abap-processing-internal-data/abenarith_operators.md) and [`MOD`](../abap-processing-internal-data/abenarith_operators.md). In the SQL function `DIV`, the amounts of the arguments are divided and then the sign is assigned (positive if the arguments have the same signs and negative if they have different signs). Accordingly, the result of `MOD` can be negative, so that multiplying the result of `DIV` by `expr2` plus the result of `MOD` produces the value of `expr1`. The ABAP operator [`MOD`](../abap-processing-internal-data/abenarith_operators.md), on the other hand, only produces positive results. See [Example](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md).

- If a `CHAR` field of variable length is used as an argument in the SQL function [`GREATEST`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md) or [`LEAST`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md), the inferred type has the maximum length.

- The SQL function [`GREATEST`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md) must not be confused with the aggregate function [`MAX`](abensql_agg_func.md) and the SQL function [`LEAST`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md) must not be confused with the aggregate function [`MIN`](abensql_agg_func.md). While `MAX` and `MIN` determine the maximum and minimal value of a SQL expression in a row set, `GREATEST` and `LEAST` determine the largest and smallest value of a set of arguments in a row set.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of flight time from minutes to hours. Round distance with null.

``` abap
SELECT FROM spfli 
       FIELDS carrid, 
              connid, 
              division( fltime,60,2 ) AS fltime, 
              round( distance, NULL ) AS distance 
       ORDER BY carrid, connid 
       INTO TABLE @FINAL(result). 
 
cl_demo_output=>display( result ).
```

## Executable Example

[SQL Expressions, Arithmetic Calculations](abensql_expr_arith_abexa.md)
