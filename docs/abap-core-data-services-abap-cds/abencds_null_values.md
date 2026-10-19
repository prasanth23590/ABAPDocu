---
title: "ABAP CDS - Null Values"
source_file: abencds_null_values.html
section: "ABAP Core Data Services (ABAP CDS)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Null Values

A [null value](../abap-glossary/abennull_value_glosry.md) is a special value returned by a [database](../abap-glossary/abendatabase_glosry.md) in order to indicate an undefined value or result.

In ABAP CDS, null values can be handled using one of the following:

- The condition [`IS NULL`](abap-cds-data-definitions/abencds_cond_expr_null_v2.md).

- The addition [`ELSE NULL`](abap-cds-data-definitions/abencds_case_expression_v2.md) in a case distinction in a CDS view entity.

- The function [`COALESCE`](abap-cds-data-definitions/abencds_coalesce_expression_v2.md).

- The parameter `on_null` in [date and time conversion functions](abap-cds-data-definitions/abencds_date_time_conversions_v2.md).

In the `SELECT` statement of a CDS view entity, null values can be produced by

- [aggregate functions](../abap-glossary/abenaggregate_function_glosry.md),

- in outer [joins](../abap-glossary/abenjoin_glosry.md),

- in [CDS expressions](../abap-glossary/abencds_expression_glosry.md).

The topic [ABAP SQL - Null Values](../abap-programming-language/abap-database-access/abenabap_sql_null_values.md) explains the handling of null values in ABAP SQL.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, the field `NullResult` contains a null value because the `CASE` expression on the left side does not find a true `WHEN` condition. It evaluates the `ELSE` branch, and sets the result to null accordingly.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity that return a null value'
define view entity DEMO_CDS_NULL
  as select from demo_expressions
{
  'A'             as id,

  case
    when id = 'Y'
    then 'Z'
    else null 
    end as NullResult
}
```

The following `SELECT` statement evaluates the CDS view entity using the [ABAP SQL coalesce function](../abap-programming-language/abap-database-access/abensql_coalesce.md). Since the case expression returns a null value, the coalesce function returns `'Null'` as result.

``` abap
SELECT 
  FROM demo_cds_null 
  FIELDS coalesce( NullResult, 'Null' ) AS coalesced 
  INTO TABLE @FINAL(result).
```
