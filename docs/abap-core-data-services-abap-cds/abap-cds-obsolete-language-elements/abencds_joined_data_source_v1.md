---
title: "CDS DDL - DDIC-Based View, SELECT, JOIN"
source_file: abencds_joined_data_source_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, data_source"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, JOIN

## Syntax

``` abap
... { [INNER] JOIN }|{ LEFT|RIGHT OUTER [TO ONE|MANY] JOIN }|{ CROSS JOIN } 
      data_source [ON cds_cond] ...  
```

[`data_source`](abencds_data_source_v1.md) · [`cds_cond`](abencds_conditional_expression_v1.md)

### Addition

[1. `... ON cds_cond`](abencds_joined_data_source_v1.md#addition-1)

[2. `... TO ONE|MANY`](abencds_joined_data_source_v1.md#addition-2)

## Overview

### Description

Defines a [join](../../abap-glossary/abenjoin_glosry.md) between two data sources of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The code above is part of the syntax of a data source [`data_source`](abencds_data_source_v1.md) and contains the recursive syntax of a data source [`data_source`](abencds_data_source_v1.md). Two joined data sources represent a join expression.

Every join expression for an inner or outer join must contain a join condition [`cds_cond`](abencds_conditional_expression_v1.md) after `ON` (for details, see Addition 1 below). A join expression for a cross join cannot contain any join condition.

[Inner joins](../../abap-glossary/abeninner_join_glosry.md), [outer joins](../../abap-glossary/abenouter_join_glosry.md), and [cross joins](../../abap-glossary/abencross_join_glosry.md) are possible:

- A join between two data sources using `INNER JOIN` or just `JOIN` selects all entries of the data sources whose fields meet the `ON` condition.

- A join between two data sources using `LEFT OUTER JOIN` selects all entries on the left side. A join between two data sources using `RIGHT OUTER JOIN` selects all entries on the right side. Entries that meet the `ON` condition have the same content as in the inner join. In entries that do not meet the `ON` condition, the elements on the right or left side have the [null value](../../abap-glossary/abennull_value_glosry.md). When the CDS view is used in ABAP SQL, null values are set to the type-dependent initial value.

- When two data sources are joined using `CROSS JOIN`, their cross product is produced. All entries on the left side are combined with all entries on the right side. The number of rows in the result set is the number of rows on the left side multiplied by the number of rows on the right side.

Nested join expressions are evaluated in the following order:

- In the case of inner and outer joins, by the arrangement of the `ON` conditions. From left to right, the most adjacent `ON` conditions are assigned to each `JOIN` and this expression is parenthesized implicitly. These implicit parentheses can be made explicit using actual parentheses, `( )`. This is optional.

- By default, cross joins are evaluated from left to right. The priority of the evaluation can be affected by parentheses `( )`.

  - If multiple cross joins are combined, the order of the evaluation is irrelevant. The result is always the same and the number of rows is the product of the number of rows of all involved data sources.

  - If cross joins are combined with inner and outer joins, the result can depend on the order of evaluation or the parentheses.

### Hints

- A `WHERE` condition for a `SELECT` statement with joins affects the result set created using the joins.

- An inner join or a cross join between two individual data sources is commutative. If the left and right side are switched, the result remains the same.

- [Buffering](abencds_v1_buffering.md) is not recommended for a CDS view that contains an outer join. The result set can contain [null values](../../abap-glossary/abennull_value_glosry.md), which means that ABAP SQL reads can behave differently to direct database reads when the buffer is read, since null values in the buffer are transformed to initial values.

- The function [`coalesce`](abencds_coalesce_expression_v1.md) can be used to prevent null values in the result set.

- A cross join behaves like an inner or outer join whose `ON` condition is always true. A cross join with a `WHERE` condition has the same result as an inner join with an identical `ON` condition. Unlike the inner join, in a cross join all data is read first before the condition is evaluated. In an inner join only data that meets the `ON` condition is read.

- A cross join should only be used with extreme caution. Since it is not possible to specify an `ON` condition, all data of all involved data sources is read. In the case of very large datasets, the result set (whose number of rows is always the product of the number of all rows of both data sources) can quickly become very large.

- On the database, a cross join of two client-dependent data sources is defined internally as an inner join, whose `ON` condition checks whether the client columns of the left and right side are equal. If one side is not client-dependent, the cross join is defined as specified.

- In nested join expressions, parentheses are recommended for making the code easier to read. In the case of inner and outer joins, the parentheses can be specified wherever the `ON` conditions specify parentheses implicitly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view works in exactly the same way as the DDIC database view `DEMO_SCARR_SPFLI`. The class `CL_DEMO_CDS_JOIN` uses `SELECT` to access the view. Unlike when the DDIC view `DEMO_CDS_SCARR_SPFLI` is accessed, no client column is returned when the CDS entity `DEMO_SCARR_SPFLI` is accessed. The CDS-managed DDIC view `DEMO_CDS_JOIN` returns the client column too.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_JOIN'
@AccessControl.authorizationCheck: #NOT_ALLOWED
define view demo_cds_scarr_spfli(
    id,
    carrier,
    flight,
    departure,
    destination
  )
  as select from spfli
    join         scarr on scarr.carrid = spfli.carrid
{
  key spfli.carrid,
  key scarr.carrname,
  key spfli.connid,
      spfli.cityfrom,
      spfli.cityto
}
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

The following view contains a cross join of table `T000` of all clients of an AS ABAP with the entries for the message class `SABAPDEMOS` in the table `T100`. The class `CL_DEMO_CDS_CROSS_JOIN` accesses the view. The result set would be very large without this `WHERE` condition.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_CRSJN'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_cross_join
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
      t100.arbgb = 'SABAPDEMOS' 
```

## Addition 1

`... ON cds_cond`

### Description

Join condition. A join condition must be specified for an inner or outer join. A join condition must not be specified for a cross join.

The syntax of the relational expressions of a join condition [`cds_cond`](abencds_conditional_expression_v1.md) is subject to the following restrictions:

- General Rules

  - [Character literals](abencds_literal_v1.md) cannot be used in comparisons with numeric values.

  - [Numeric literals](abencds_literal_v1.md) that represent a value outside the value range of [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) must be specified as floating point literals with a decimal point.

- Special Rules:

  - All [relational operators](abencds_conditional_expression_v1.md) are allowed. That means all comparison operators are allowed as well as `BETWEEN`, `LIKE`, `IS [NOT] NULL`, and `IS [NOT] INITIAL`.

  - `lhs` expects a [field](abencds_field_v1.md) of one of the two [`data_sources`](abencds_data_source_v1.md) of the join.

  - `rhs` expects a [field](abencds_field_v1.md) of one of the two [`data_sources`](abencds_data_source_v1.md) of the join, a [literal](abencds_literal_v1.md) with optional domain prefix, a [parameter](abencds_parameter_v1.md), a [session variable](abencds_session_variable_v1.md), or a [built-in function](abencds_builtin_functions_v1.md).

  - [Path expressions](abencds_path_expression_v1.md) cannot be used.

  - [CDS DDL expressions](abencds_expressions_v1.md) cannot be used.

## Addition 2

`... TO ONE|MANY`

### Description

Specifies the [cardinality](../../abap-glossary/abencardinality_glosry.md) of a left outer join. This addition is positioned after `LEFT OUTER`, but is not possible after `RIGHT OUTER`. Only certain specific database systems apply this addition.

If the addition `TO ONE` is specified, any databases that support this addition assume that the result set defined by the left outer join matches this cardinality and the [SQL Optimizer](../../abap-glossary/abenquery_optimizer_glosry.md) attempts to suppress any surplus joins. If the result set does not match the cardinality, the result is undefined and may be dependent on the entries in the [`SELECT` list](abencds_select_list_v1.md). If the addition `TO MANY` is specified, no optimization takes place as a rule.

### Hints

- More information can be found in the documentation of the current database system. The [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), for example, supports the additions `TO ONE` and `TO MANY` and their description is part of the [HANA-specific SQL documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

- To avoid undefined and platform-dependent behavior, `TO ONE` or `TO MANY` can be specified only if the data being read meets the relevant prerequisites.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Incorrect use of `TO ONE` in CDS views. The data in the DDIC database tables `SCARR` and `SPFLI` do not have the cardinality `TO ONE` and have the cardinality `TO MANY` instead. On a SAP HANA database, for example, the result is dependent on the [`SELECT` list](../../abap-programming-language/abap-database-access/abapselect_list.md). If the left and right side are specified here, no optimization takes place. If no columns are specified on the right side (and the aggregate function [`COUNT(*)`](abencds_aggregate_functions_v1.md) is used), an optimization takes place. Here, only that data is read that meets the prerequisite cardinality.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSWTO1'
define view demo_cds_wrong_to_one_1
  as select from
                             scarr as c
      left outer to one join spfli as p on
        c.carrid = p.carrid
    {
      c.carrid   as carrid,
      c.carrname as carrname,
      p.connid   as connid
    }

```abap
@AbapCatalog.sqlViewName: 'DEMOCDSWTO2'
define view demo_cds_wrong_to_one_2
  as select from
                             scarr as c
      left outer to one join spfli as p on
        c.carrid = p.carrid
    {
      c.carrid   as carrid,
      c.carrname as carrname
    }

```abap
@AbapCatalog.sqlViewName: 'DEMOCDSWTO3'
define view demo_cds_wrong_to_one_3
  as select from
                             scarr as c
      left outer to one join spfli as p on
        c.carrid = p.carrid
    {
      count(*) as cnt
    }
```

The class `CL_DEMO_CDS_WRONG_TO_ONE` accesses the CDS views and displays the results.
