---
title: "sql_agg - GROUPING"
source_file: abengrouping_function.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, GROUP BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_agg - GROUPING

## Syntax

``` abap
 ... GROUPING( col )  
```

[`col`](abenabap_sql_columns.md)

## Description

The result of the grouping function `GROUPING` indicates whether a specific column is part of the [aggregation](../../abap-glossary/abenaggregate_expression_glosry.md). After the grouping function `GROUPING`, a column name in parentheses is expected as an argument.

The return value of the grouping function `GROUPING` has the data type [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The following return values of the grouping function are possible here:

| **Value** | **Meaning**                                    |
|-----------|------------------------------------------------|
| 0         | The column is **not** part of the aggregation. |
| 1         | The column is part of the aggregation.         |

The columns that are part of the aggregation contain the null values as placeholders in the corresponding results. More specifically, the grouping function `GROUPING` determines whether the column that contains a null value in the result was part of the aggregation or whether it was already the null value in the [data source](abapselect_data_source.md).

****Rules****

- The grouping function can only be used in the [`SELECT`](abapselect_list.md) list and in the [`HAVING`](abaphaving_clause.md) clause.

- The grouping function can be used only if the [`GROUP BY`](abapgroupby_clause.md) clause contains the addition [`GROUPING SETS`](abapgrouping_sets_clause.md).

- The column used as an argument of the grouping function `GROUPING` must also be added to the `GROUP BY` list.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example calculates the number of Lufthansa flights depending on the plane type (the column `planetype`) and the connection (the column `connid`). Here, the grouping function for the plane type column or connection column is used to determine whether they are part of the aggregation.

``` abap
SELECT FROM sflight 
       FIELDS carrid, 
              connid, 
              planetype, 
              COUNT( * ) AS flights_count, 
              grouping( connid ) AS agg_connid, 
              grouping( planetype ) AS agg_planetype 
       WHERE carrid = 'LH' 
       GROUP BY GROUPING SETS ( ( carrid, planetype ), 
                                ( carrid, connid ), 
                                (  ) ) 
       ORDER BY connid, planetype 
       INTO TABLE @FINAL(result_grouping). 
 
cl_demo_output=>display( result_grouping ).
```

## Executable Example

[`GROUPING`, Aggregate Function](abengrouping_function_abexa.md)
