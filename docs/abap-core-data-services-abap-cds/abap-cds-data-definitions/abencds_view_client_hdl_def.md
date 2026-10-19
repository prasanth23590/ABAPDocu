---
title: "ABAP CDS - Definition of Client Handling for CDS View Entities"
source_file: abencds_view_client_hdl_def.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > ABAP CDS - Client Handling in CDS View Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Definition of Client Handling for CDS View Entities

For a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), client handling is done implicitly and automatically by filtering the client ID contained in the SAP HANA session variable `CDS_CLIENT` that can be accessed in CDS using the [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](abencds_session_var_builtin_v2.md).

- [Determining Client Dependency](abencds_view_client_hdl_def.md#determining-client-dependency)

- [Determining Client Handling](abencds_view_client_hdl_def.md#determining-client-handling)

- [Properties of Client-Dependent CDS View Entities](abencds_view_client_hdl_def.md#properties-of-client-dependent-cds-view-entities)

## Determining Client Dependency

The [client dependency](../../abap-glossary/abenclient_dependency_glosry.md) of a view entity is determined by the [data sources](abencds_data_source_v2.md) used:

- If one of the data sources used in the view is client-dependent, the view is [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md).

- If none of the data sources used in the view is client-dependent, the view is [client-independent](../../abap-glossary/abenclient_independent_glosry.md).

### Hint

The client dependency of CDS view entities is not defined by annotations, as it is done for [CDS DDIC-based views](../abap-cds-obsolete-language-elements/abencds_view_client_handling_v1.md).

## Determining Client Handling

If a CDS view entity is client-dependent, the client handling is performed by filtering the client ID contained in the SAP HANA session variable `CDS_CLIENT`. The session variable algorithm expands the [joins](../../abap-glossary/abenjoin_glosry.md) of the view entity implicitly as shown in the following table. This applies to joins specified explicitly using `JOIN`, as well as to instances of joins created when using [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md).

\|**Left Side**\|**Right Side**\|`INNER JOIN`\| `LEFT OUTER JOIN`\|`RIGHT OUTER JOIN`\|`CROSS JOIN` \| \|:---\|:---\| \|Client-dependent\|Client-dependent\|Compares the client columns in the `ON` condition\|Compares the client columns in the `ON` condition\|Compares the client columns in the `ON` condition\|Transforms the cross join to an inner join using an `ON` condition for the client columns \| \|Client-independent\|Client-dependent\|`-`\|Compares the client column with the value of the [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](abencds_session_var_builtin_v2.md) in the `ON` condition\|`-`\|`-` \| \|Client-dependent\|Client-independent\|`-`\|`-`\|Compares the client column with the value of the [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](abencds_session_variable_v2.md) in the `ON` condition\|`-` \| \|Client-independent\|Client-independent\|`-`\|`-`\|`-`\|`-`\|

In addition, when client-dependent database tables are accessed, [`WHERE` clauses](abencds_where_clause_v2.md) with comparisons of the client columns with the [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](abencds_session_variable_v2.md) are added to the view implicitly. If only client-dependent [CDS entities](../../abap-glossary/abencds_entity_glosry.md) are accessed, however, no clauses are added.

It is not possible to access the data of different clients in a single read.

### Hints

- The [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](abencds_session_var_builtin_v2.md) is filled with the [current client](../../abap-glossary/abencurrent_client_glosry.md) by default.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity `DEMO_CDS_CLIENT_HANDLING` defines different kinds of [joins](../../abap-glossary/abenjoin_glosry.md) ([left outer join](../../abap-glossary/abenleft_outer_join_glosry.md), [inner join](../../abap-glossary/abeninner_join_glosry.md), and [right outer join](../../abap-glossary/abenright_outer_join_glosry.md)) between a client-independent database table (`T000`) and a client-dependent database table (`DEMO_SALES_ORDER`). It also defines and uses an [association](../../abap-glossary/abencds_association_glosry.md) between the same client-independent database table (`T000`) and the same client-dependent database table (`DEMO_SALES_ORDER`).

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

The image below shows the SQL statement that is generated on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). For the left outer join, an `ON` condition is added that compares the client field of the database table `DEMO_SALES_ORDER` with the [current client](../../abap-glossary/abencurrent_client_glosry.md). The current client is determined using the built-in SAP HANA function `SESSION_CONTEXT ('CDS_CLIENT')`, which is the equivalent to the session variable `$session.client` in ABAP CDS. In the same way, a `WHERE` clause is added that compares the client of the database table with the current client. ![figure](images_abdoc_client_handling.png)

## Properties of Client-Dependent CDS View Entities

Since client handling is performed completely implicitly in CDS view entities, a client field is not allowed in the `SELECT` list of a view entity. The result set of an ABAP SQL read on a CDS view entity can never contain a client column either.
