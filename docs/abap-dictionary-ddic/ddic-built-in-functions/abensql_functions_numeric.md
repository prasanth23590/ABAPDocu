---
title: "DDIC - SQL Functions for Numeric Values"
source_file: abensql_functions_numeric.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Functions > DDIC - SQL Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - SQL Functions for Numeric Values

The following table shows the numeric SQL functions that can be used by [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). The columns **ABAP CDS DDIC-Based Views**, **ABAP CDS View Entities**, and **ABAP SQL** indicate where a function can be used. The **ABAP SQL In-Memory Engine** column indicates whether the function can be executed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md).

| **SQL Function** | **Result**                                                                                          | **CDS DDIC-Based Views**                   | **CDS View Entities**                      | **ABAP SQL**                 | **ABAP SQL In-Memory Engine** |
|------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------|--------------------------------------------|------------------------------|-------------------------------|
| `ABS`            | Absolute value of argument.                                                                         | [x](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_numeric_v1.md) | [x](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_numeric_v2.md) | [x](../../abap-programming-language/abap-database-access/abensql_arith_func.md) | [x](../../abap-programming-language/abap-database-access/abensql_engine_expr.md) |
| `CEIL`           | Rounds an argument to the first integer that is greater than or equal to the value of the argument. | [x](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_numeric_v1.md) | [x](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_numeric_v2.md) | [x](../../abap-programming-language/abap-database-access/abensql_arith_func.md) | [x](../../abap-programming-language/abap-database-access/abensql_engine_expr.md) |
| `DIV`            | Division of two arguments. The result is rounded to an integer.                                     | [x](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_numeric_v1.md) | [x](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_numeric_v2.md) | [x](../../abap-programming-language/abap-database-access/abensql_arith_func.md) | [x](../../abap-programming-language/abap-database-access/abensql_engine_expr.md) |
| `DIVISION`       | Division of two arguments. The result is rounded to specified decimal places.                       | [x](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_numeric_v1.md) | [x](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_numeric_v2.md) | [x](../../abap-programming-language/abap-database-access/abensql_arith_func.md) | \-                            |
| `FLOOR`          | Largest integer number not greater than the value of the argument.                                  | [x](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_numeric_v1.md) | [x](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_numeric_v2.md) | [x](../../abap-programming-language/abap-database-access/abensql_arith_func.md) | [x](../../abap-programming-language/abap-database-access/abensql_engine_expr.md) |
| `GREATEST`       | Largest value of a set of arguments.                                                                | \-                                         | \-                                         | [x](../../abap-programming-language/abap-database-access/abensql_arith_func.md) | \-                            |
| `LEAST`          | Smallest value of a set of arguments.                                                               | \-                                         | \-                                         | [x](../../abap-programming-language/abap-database-access/abensql_arith_func.md) | \-                            |
| `MOD`            | Positive or negative integer remainder of the division of two arguments.                            | [x](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_numeric_v1.md) | [x](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_numeric_v2.md) | [x](../../abap-programming-language/abap-database-access/abensql_arith_func.md) | [x](../../abap-programming-language/abap-database-access/abensql_engine_expr.md) |
| `ROUND`          | Rounded value of an argument.                                                                       | [x](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_numeric_v1.md) | [x](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_numeric_v2.md) | [x](../../abap-programming-language/abap-database-access/abensql_arith_func.md) | \-                            |

The possible operands and data types are described in the corresponding documentation for [ABAP CDS, DDIC-Based Views](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_numeric_v1.md), [ABAP CDS, View Entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_numeric_v2.md) and [ABAP SQL](../../abap-programming-language/abap-database-access/abensql_arith_func.md).

## Hints

- The SQL functions [`DIV`](abensql_functions_numeric.md) and [`MOD`](abensql_functions_numeric.md) behave differently with respect to the signs than the ABAP operators [`DIV`](../../abap-programming-language/abap-processing-internal-data/abenarith_operators.md) and [`MOD`](../../abap-programming-language/abap-processing-internal-data/abenarith_operators.md). In the SQL function `DIV`, the amounts of the arguments are divided and then the sign is assigned (positive if the arguments have the same signs and negative if they have different signs). Accordingly, the result of `MOD` can be negative, so that multiplying the result of `DIV` by `expr2` plus the result of `MOD` produces the value of `expr1`. The ABAP operator [`MOD`](../../abap-programming-language/abap-processing-internal-data/abenarith_operators.md), on the other hand, only produces positive results.

- If a `CHAR` field of variable length is used as an argument in the SQL function `GREATEST` or `LEAST`, the inferred type has the maximum length.

- The SQL function `GREATEST` must not be confused with the aggregate function [`MAX`](../../abap-programming-language/abap-database-access/abensql_agg_func.md) and the SQL function `LEAST` must not be confused with the aggregate function [`MIN`](../../abap-programming-language/abap-database-access/abensql_agg_func.md). While `MAX` and `MIN` determine the maximum and minimal value of a SQL expression in a row set, `GREATEST` and `LEAST` determine the largest and smallest value of a set of arguments in a row set.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following table shows the results of integer divisions and their integer remainders in SQL. See also the example for the ABAP operators [`DIV`](../../abap-programming-language/abap-processing-internal-data/abenarith_operators.md) and [`MOD`](../../abap-programming-language/abap-processing-internal-data/abenarith_operators.md).

\|`expr1`\|`expr2`\|`DIV`\|`MOD`\|

\|7\|3\|2\|1\| \|-7\|3\|-2\|-1\| \|7\|-3\|-2\|1\| \|-7\|-3\|2\|-1\|
