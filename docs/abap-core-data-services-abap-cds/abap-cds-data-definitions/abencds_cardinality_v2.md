---
title: "CDS DDL - CDS View Entity, cardinality"
source_file: abencds_cardinality_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, Associations > CDS DDL - CDS View Entity, ASSOCIATION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, cardinality

## Syntax Forms

**Cardinality Syntax Written in Words**

``` abap
     [ OF {{EXACT ONE} | MANY | ONE} ] TO {{EXACT ONE} | MANY | ONE} 
```

**Numeric Syntax**

``` abap
      [min..max]
```

### Alternative

[1. `OF {EXACT ONE | MANY | ONE} TO {EXACT ONE | MANY | ONE}`](abencds_cardinality_v2.md#alternative-1)

[2. `... [min..max] ...`](abencds_cardinality_v2.md#alternative-2)

## Overview

### Description

Specifies a [cardinality](../../abap-glossary/abencardinality_glosry.md) to express the relation between the rows of the data sources. The following options are available:

- The cardinality can be written in words. In this case, a [source](../../abap-glossary/abensource_cardinality_glosry.md) and a [target cardinality](../../abap-glossary/abentarget_cardinality_glosry.md) can be specified. This syntax variant is the recommended option.

- The cardinality can be specified in numbers in square brackets. In this case, the minimum and maximum cardinality of the [association target](../../abap-glossary/abenassociation_target_glosry.md) is specified. No source cardinality can be specified. The implicit default source cardinality is `MANY`.

- The cardinality is optional and can be left out. In this case, the implicit default is many-to-one. SAP recommends always specifying the cardinality explicitly.

The cardinality specification documents the semantics of the data model. It is used by the [SAP HANA SQL Optimizer](../../abap-glossary/abenquery_optimizer_glosry.md) for performance optimizations by suppressing surplus joins on any databases that support this addition. It is important that the cardinality specification matches the data in question. Otherwise, the result is undefined and can depend on the entries in the `SELECT` list.

The use of 'to many' associations (cardinality \[n..\*\]) in the SELECT list modifies the cardinality of the results set. Each row of the data source can produce multiple result rows when a 'to many' association is resolved. It is the responsibility of the data modeler to ensure that the declared cardinality matches the actual data relationships.

If no cardinality is specified, the implicit default cardinality is `MANY TO ONE`.

### Hints

- To avoid undefined behavior, the cardinality should always be defined to match the data in question.

  **Note:** The cardinality is mainly descriptive, not prescriptive. It does not force a matching result set.

- The specified cardinality is evaluated by the syntax check in the CDS DDL of CDS or in ABAP SQL. A non-matching cardinality can produce a syntax check warning. In CDS view extensions, using a 'to many' association in the SELECT list raises a syntax error, since it could change the cardinality of the result set of the extended entity.

- The numeric syntax and the syntax written in words must not be mixed. It extended entity. association in words and the target cardinality of the same association in numbers.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows how an incorrect cardinality leads to unexpected results. A CDS view entity joins the DDIC database tables `SCARR` and `SPFLI` in a CDS association `_spfli` without specifying the cardinality explicitly. The implicitly set cardinality is `MANY TO ONE`. If the CDS association is used in a path specified in the `SELECT` list, this is implemented on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) as a left outer join using the addition `MANY TO ONE`. The actual cardinality of the data is, however, `TO MANY`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_WRONG_CARDINALITY_1
  as select from scarr
/*+[hideWarning] { "IDS" : [ "CARDINALITY_CHECK" ] }*/
  association to spfli as _spfli on _spfli.carrid = scarr.carrid
{
  key scarr.carrid   as carrid,
      scarr.carrname as carrname,
      _spfli.connid  as connid
}
```

The class `CL_DEMO_CDS_WRONG_CRDNLTY_1` uses different `SELECT` statements to access the view. The two reads return a different number of rows. This shows that the cardinality should always be defined explicitly to match the data in question to avoid unexpected behavior.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity joins the DDIC database tables `SCARR` and `SPFLI` in a CDS association `_spfli` while specifying the cardinality explicitly and correctly. If the CDS association is used in a path specified in the `SELECT` list, this is implemented on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) as a left outer many-to-many join. This matches the actual cardinality of the data.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPLICIT_CARD_1
  as select from scarr
  association of many to many spfli as _spfli 
    on _spfli.carrid = scarr.carrid
{
  key scarr.carrid   as carrid,
      scarr.carrname as carrname,
      _spfli.connid  as connid
}
```

The class `CL_DEMO_CDS_EXPLICIT_CARD_1` uses different `SELECT` statements to access the view. The two reads return the same number of rows.

## Alternative 1

`OF {EXACT ONE | MANY | ONE} TO {EXACT ONE | MANY | ONE}`

### Description

The cardinality written in words specifies the source and target cardinality, that means, how many entries of the data source match the entries of the association target. The following cardinality specifications are possible:

- `OF EXACT ONE TO EXACT ONE`

- `OF EXACT ONE TO MANY`

- `OF EXACT ONE TO ONE`

- `OF MANY TO EXACT ONE`

- `OF MANY TO MANY`

- `OF MANY TO ONE`

- `OF ONE TO EXACT ONE`

- `OF ONE TO MANY`

- `OF ONE TO ONE`

The cardinality syntax written in words is available in [CDS table entities](../../abap-glossary/abencds_table_entity_glosry.md), [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md), [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md), and [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md). It is not available in any other CDS entity.

### Hints

- SAP recommends using the cardinality syntax written in words instead of the numeric syntax, since it improves query performance in some scenarios.

- Further details can be found on SAP Help Portal in the SAP HANA SQL Reference Guide for SAP HANA Platform.

- In case of [to-child associations](../../abap-glossary/abento_child_association_glosry.md), the source cardinality must be set to `EXACT ONE`. It can also be left out and is then implicitly set to `EXACT ONE`. No other source cardinality is valid for to-child associations.

- When a [path expression](../../abap-glossary/abenpath_expression_glosry.md) of a `TO EXACT ONE` association is used with a [filter condition](../../abap-glossary/abenfilter_condition_glosry.md), then the join is rewritten to a `TO ONE JOIN` on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) to avoid potential cardinality conflicts. This is indicated by a syntax check warning. This can be circumvented by specifying the cardinality [attribute](abencds_path_expr_card_v2.md) `TO EXACT ONE` in this path expression. Then, the join is not rewritten and remains a `TO EXACT ONE` join on the SAP HANA database.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity defines an association with the cardinality `EXACT ONE TO ONE` to a text provider view.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, card in words'
@AbapCatalog.entityBuffer.propagationAllowed:true

define view entity DEMO_CDS_CARDINALITY_IN_WORDS
  as select from demo_sales_mat

  association of exact one to one DEMO_SALES_CDS_MAT_TEXT as _Text 
    on  $projection.material = _Text.material
    and _Text.language       = $session.system_language
{
  key matnr as material,
      mtart as material_type,
      mtgrp as material_group,
      _Text,
      _Text.material_name
}
```

The SQL statement generated on the database shows that the path expression is transformed into a left outer exact one to one join on the database. ![figure](images_exact_one.jpg)

## Alternative 2

`... [min..max] ...`

### Description

The numeric syntax specifies the cardinality of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of a CDS view entity. The square brackets `[ ]` are part of the syntax. For `min` and `max`, positive integers (including 0) and asterisks (`*`) can be specified:

- `max` cannot be 0.

- An asterisk `*` for `max` means any number of rows.

- When a path expression of an association with max set to \* (to many) is used in the SELECT list, the number of result rows can be multiplied accordingly.

- `min` can be omitted (set to 0 if omitted).

- `min` cannot be `*`.

- When a CDS association is used in a [`WHERE` condition](abencds_where_clause_v2.md), 1 must be specified for `max`.

If the cardinality is not defined explicitly, the cardinality to-one is used implicitly (`[min..1]`).

With the numeric syntax, no source cardinality can be specified, only the cardinality of the association target. The target cardinality can be specified with high precision, since the exact number of data records returned by an association can be specified. In the SQL statement that is generated on the database, the numeric syntax is translated into words.

### Hint

SAP recommends using the cardinality syntax written in words instead of the numeric syntax, since it improves query performance in some scenarios.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity specifies the cardinality of the association target as to-many using the syntax `[*]`.

``` abap
@EndUserText.label: 'CDS view entity, numeric cardinality'
define view entity DEMO_CDS_CAR_NUMERIC
  as select from spfli
  association [*] to sflight as _Flights 
    on  $projection.carrid = _Flights.carrid
    and $projection.connid = _Flights.connid
{
  key carrid,
  key connid,
      _Flights.fldate
}
```

The SQL statement generated on the database shows that the path expression is transformed into a left outer join. The SQL statement does not contain an explicit cardinality, which means that the implicit default cardinality `MANY TO MANY` is used. ![figure](images_num_car.jpg)
