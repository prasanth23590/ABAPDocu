---
title: "CDS DDL - CDS View Entity, SELECT, JOIN"
source_file: abencds_joined_data_source_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, data_source"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, JOIN

## Syntax

``` abap
... { [INNER] [cardinality] JOIN 
     | LEFT OUTER [cardinality] JOIN 
     | RIGHT OUTER JOIN 
     | CROSS JOIN } 
       data_source [ON cds_cond] ...  
```

[`data_source`](abencds_data_source_v2.md) · [`cds_cond`](abencds_conditional_expression_v2.md)

### Addition

[1. `... ON cds_cond`](abencds_joined_data_source_v2.md#addition-1)

[2. `... cardinality`](abencds_joined_data_source_v2.md#addition-2)

## Overview

### Description

Defines a [join](../../abap-glossary/abenjoin_glosry.md) between two data sources of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The code above is part of the syntax of a data source [`data_source`](abencds_data_source_v2.md) and recursively contains the syntax of a second data source [`data_source`](abencds_data_source_v2.md). Two joined data sources represent a join expression.

Every join expression for an inner or outer join must contain a join condition [`cds_cond`](abencds_conditional_expression_v2.md) after `ON` (for details, see Addition 1 below). A join expression for a cross join cannot contain any join condition.

``` abap
When joining two or more data sources, each element of the `SELECT` list must have the name of its data source as prefix\. 
Example: `source1.field`
```

[Inner joins](../../abap-glossary/abeninner_join_glosry.md), [outer joins](../../abap-glossary/abenouter_join_glosry.md), and [cross joins](../../abap-glossary/abencross_join_glosry.md) are possible:

- A join between two data sources using `INNER JOIN` or just `JOIN` selects all entries of the data sources whose fields match the `ON` condition.

- A join between two data sources using `LEFT OUTER JOIN` selects all entries on the left side. A join between two data sources using `RIGHT OUTER JOIN` selects all entries on the right side. Entries that match the `ON` condition have the same content as in the inner join. In entries that do not match the `ON` condition, the elements on the right or left side have the [null value](../../abap-glossary/abennull_value_glosry.md). When the CDS view entity is used in ABAP SQL, null values are set to the type-dependent initial value.

- When two data sources are joined using `CROSS JOIN`, the result is their cross product. All entries on the left side are combined with all entries on the right side. The number of rows in the result set is the number of rows on the left side multiplied by the number of rows on the right side.

Nested join expressions are evaluated in the following order:

- In the case of inner and outer joins, by the arrangement of the `ON` conditions. From left to right, the most adjacent `ON` conditions are assigned to each `JOIN` and this expression is parenthesized implicitly. These implicit parentheses can be made explicit using actual parentheses, `( )`. This is optional.

- By default, cross joins are evaluated from left to right. The priority of the evaluation can be affected by parentheses `( )`.

  - If multiple cross joins are combined, the order of the evaluation is irrelevant. The result is always the same and the number of rows is the product of the number of rows of all involved data sources.

  - If cross joins are combined with inner and outer joins, the result can depend on the order of evaluation or the parentheses.

### Hints

- A `WHERE` condition for a `SELECT` statement with joins affects the result set created using the joins.

- An inner join or a cross join between two individual data sources is commutative. If the left and right side are switched, the result remains the same.

- The function [`coalesce`](abencds_coalesce_expression_v2.md) can be used to prevent null values in the result set.

- A cross join behaves like an inner or outer join whose `ON` condition is always true. A cross join with a `WHERE` condition has the same result as an inner join with an identical `ON` condition. Unlike the inner join, in a cross join all data is read first before the condition is evaluated. In an inner join only data that meets the `ON` condition is read.

- Cross joins should be used with caution. Since it is not possible to specify an `ON` condition, all data of all involved data sources is read. In the case of very large datasets, the result set (whose number of rows is always the product of the number of all rows of both data sources) can quickly become very large.

- On the database, a cross join of two client-dependent data sources is defined internally as an inner join, whose `ON` condition checks whether the client columns of the left and right side are equal. If one side is client-independent, the cross join is defined as specified.

- In nested join expressions, parentheses are recommended for making the code easier to read. In the case of inner and outer joins, the parentheses can be specified exactly where the `ON` conditions specify parentheses implicitly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity `DEMO_CDS_CLIENT_HANDLING` defines different kinds of [joins](../../abap-glossary/abenjoin_glosry.md) ([left outer join](../../abap-glossary/abenleft_outer_join_glosry.md), [inner join](../../abap-glossary/abeninner_join_glosry.md), and [right outer join](../../abap-glossary/abenright_outer_join_glosry.md)) between the database table `T000` and the database table `DEMO_SALES_ORDER`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS View entity_client handling'
define view entity DEMO_CDS_CLIENT_HANDLING
  as select from
                       t000             as client_independent
      left outer join  demo_sales_order as _LeftOuter
        on _LeftOuter.id = client_independent.cccategory
      inner join       demo_sales_order as _Inner
        on _Inner.id = client_independent.cccategory
      right outer join demo_sales_order as _RightOuter
        on _RightOuter.id = client_independent.cccategory
    association to many demo_sales_order as _Assoc
      on _Assoc.id = client_independent.cccategory
    {
      key _Assoc.so_key,
          _Assoc.id,
          _Inner.id      as id_inner,
          _LeftOuter.id  as id_LeftOuter,
          _RightOuter.id as id_RightOuter,
          client_independent.cccategory
    }
    where client_independent.mtext = abap.char'SAP AG Konzern'
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following non-parenthesized chaining of join expressions

``` abap
... from tab1 
      join 
        tab2 
          join 
            tab3 on tab2.id = tab3.id 
                 on tab1.id = tab2.id ...
```

is parenthesized implicitly as follows:

``` abap
... from tab1 
      join 
        ( tab2 
            join 
              tab3 on tab2.id = tab3.id ) on tab1.id = tab2.id ...
```

No elements from `tab1` can be specified in the inner `ON` condition.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following view entity contains a cross join of table `T000` of all clients of an AS ABAP with the entries for the message class `SABAPDEMOS` in the table `T100`. The class `CL_DEMO_CDS_CROSS_JOIN_VE` accesses the view entity. Without the `WHERE` condition, the result set would be very large.

``` abap
@EndUserText.label: 'CDS view entity with a cross join'
define view entity DEMO_CDS_CROSS_JOIN_VE
  as select from
                 t000
      cross join t100
    {
      key t000.mandt,
          t000.mtext,
          t100.sprsl,
          t100.arbgb,
          t100.msgnr,
          t100.text
    }
    where
      t100.arbgb = abap.char'SABAPDEMOS'
```

## Addition 1

`... ON cds_cond`

### Description

[Join condition](../../abap-glossary/abenjoin_condition_glosry.md). A join condition must be specified for an inner or outer join. A join condition must not be specified for a cross join.

The syntax of the relational expressions of a join condition [`cds_cond`](abencds_conditional_expression_v2.md) is subject to the following restrictions:

- All [relational operators](abencds_conditional_expression_v2.md) are allowed. That means all comparison operators are allowed as well as `BETWEEN`, `LIKE`, `IS [NOT] NULL`, and `IS [NOT] INITIAL`.

- The Boolean operators `NOT`, `AND`, and `OR` are allowed.

- `lhs` expects a [field](abencds_field_v2.md) of one of the two [`data_sources`](abencds_data_source_v2.md) of the join. If a comparison operator is used as operator, then `lhs` can also be a literal.

- `rhs` expects a [field](abencds_field_v2.md) of one of the two [`data_sources`](abencds_data_source_v2.md) of the join, a [literal](abencds_literal_v2.md), a [parameter](abencds_parameter_v2.md), a [session variable](abencds_session_variable_v2.md), a [built-in function](abencds_builtin_functions_v2.md), or a [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md). **Exception:** when using the operator `LIKE`, then `rhs` must be a character literal.

- Path expressions are not allowed

- Other CDS DDL expressions are not allowed.

Special rules apply when the operands of the `ON` condition are [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md). These rules are described in the topic [CDS DDL - Using CDS Enumerated Types](abencds_use_enum_type.md).

## Addition 2

`... cardinality`

### Description

For an inner join or a left outer join, a [cardinality](../../abap-glossary/abencardinality_glosry.md) can optionally be specified. A [source](../../abap-glossary/abensource_cardinality_glosry.md) and [target](../../abap-glossary/abentarget_cardinality_glosry.md) cardinality can be specified, or only a target cardinality. The following cardinality specifications are possible:

- `EXACT ONE TO EXACT ONE`

- `EXACT ONE TO MANY`

- `EXACT ONE TO ONE`

- `MANY TO EXACT ONE`

- `MANY TO MANY`

- `MANY TO ONE`

- `ONE TO EXACT ONE`

- `ONE TO MANY`

- `ONE TO ONE`

- `TO ONE`

- `TO EXACT ONE`

- `TO MANY`

The [SQL Optimizer](../../abap-glossary/abenquery_optimizer_glosry.md) uses the cardinality specification for performance optimization. It attempts to suppress surplus joins. To avoid undefined behavior, the cardinality should always be defined to match the data in question.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Incorrect use of `TO ONE` in CDS view entities. The data in the DDIC database tables `SCARR` and `SPFLI` do not have the cardinality `TO ONE`, but `TO MANY`. On a SAP HANA database, the result is dependent on the [`SELECT` list](../../abap-programming-language/abap-database-access/abapselect_list.md). If the [`SELECT` list](../../abap-programming-language/abap-database-access/abapselect_list.md) contains columns from both the left and right side of the join expression, no optimization takes place. If the [`SELECT` list](../../abap-programming-language/abap-database-access/abapselect_list.md) does not contain any columns from the right side of the join expression, an optimization takes place. If the aggregate function `COUNT(*)` is used, an optimization takes place. When an optimization takes place, only that data is read that meets the specified cardinality.

``` abap
@EndUserText.label: 'CDS view entity with join expression'
define view entity DEMO_CDS_WRONG_TO_ONE_1_VE
  as select from
                             scarr as c
      left outer many to one join spfli as p
        on c.carrid = p.carrid
    {
      c.carrid   as carrid,
      c.carrname as carrname,
      p.connid   as connid
    }

```abap
@EndUserText.label: 'CDS view entity with join expression'
define view entity DEMO_CDS_WRONG_TO_ONE_2_VE
  as select from           scarr as c
    left outer many to one join spfli as p on c.carrid = p.carrid
{
  c.carrid   as carrid,
  c.carrname as carrname
}

```abap
@EndUserText.label: 'CDS view entity with join expression'
define view entity DEMO_CDS_WRONG_TO_ONE_3_VE
  as select from           scarr as c
    left outer many to one join spfli as p on c.carrid = p.carrid
{
  count(*) as cnt
}
```

The class `CL_DEMO_CDS_WRONG_TO_ONE_VE` accesses the CDS view entities and displays the results.
