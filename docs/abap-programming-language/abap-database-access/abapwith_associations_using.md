---
title: "WITH, ASSOCIATIONS, path"
source_file: abapwith_associations_using.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH > WITH, ASSOCIATIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, ASSOCIATIONS, path

## Syntax

``` abap
... sql_path [AS alias] 
    [REDIRECTED TO +cte VIA target] ...  
```

[`sql_path`](abenabap_sql_path.md)

### Addition

[`... REDIRECTED TO +cte VIA target`](abapwith_associations_using.md#addition)

## Overview

### Description

Specifies an existing [CDS association](../../abap-glossary/abencds_association_glosry.md) or [CTE association](../../abap-glossary/abencte_association_glosry.md) using an [SQL path expression](../../abap-glossary/abensql_path_expression_glosry.md) [`sql_path`](abenabap_sql_path.md) in the addition [`WITH ASSOCIATIONS`](abapwith_associations.md) when a common table expression is defined in a [`WITH`](abapwith.md) statement. The path expression exposes the association at its end. The exposing table expression is the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the exposed association and any join expressions that are created when the association is used in a path expression use the exposing table expression as their left side.

The root element of each path expression can be the following associations:

- CDS associations

  - exposed in the `SELECT` list of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) in cases where these views are used as a [data source](abapselect_data_source.md) in the [subquery](abapwith_subquery.md) of the common table expression.

  - exposed using `WITH ASSOCIATIONS` of preceding table expressions of the current [`WITH`](abapwith.md) statement in cases where these table expressions are used as a [data source](abapselect_data_source.md) in the [subquery](abapwith_subquery.md) of the common table expression.

- CTE associations defined and exposed using `WITH ASSOCIATIONS` of preceding table expressions of the current [`WITH`](abapwith.md) statement in cases where these table expressions are used as a [data source](abapselect_data_source.md) in the [subquery](abapwith_subquery.md) of the common table expression.

If [`~`](abenabap_sql_path.md) is used to prefix the path expression with the name of the data source that exposes its first association, this name must be the name used in the table expression. Therefore, if [`AS`](abapfrom_clause.md) is used to define an alias name, this name must be used instead of the original name in the path expression.

[Parameter passing](abenabap_sql_parameters.md) is not allowed in the final association of the specified path expressions and the [type of the join](abenabap_sql_path_filter.md) must not be defined. All fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) of a path expression that occur in the `ON` condition of the association must be elements of the `SELECT` list of the common table expression. In path expressions that contain only one association, the elements can be specified as single elements or by using `*` or `dbtab~*`. If a path expression contains more than one association, an element must be specified as a path expression closed by the field that has the same [attributes](abenabap_sql_path_filter.md) as the path expression used for exposing.

`AS` can be used to specify an alias name `alias` for the exposed association, under which it can be addressed in the subsequent queries of the current `WITH` statement. The alias name can contain letters, digits, the minus sign (`-`), and the underscore (`_`) in any order.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `WITH` statement is a syntax example only and does not have a function. Its main role is to show different ways of specifying path expressions and operands.

``` abap
WITH 
  +cte1 AS ( SELECT * 
                    FROM demo_cds_expose_assoc AS subsrc 
                    WHERE subsrc~\_spfli[ MANY TO MANY 
                      ]-carrid = '...' ) 
             WITH ASSOCIATIONS ( subsrc~\_spfli AS assoc1 ), 
  +cte2 AS ( SELECT * FROM +cte1 ) 
             WITH ASSOCIATIONS ( +cte1~\assoc1[ carrid = '...' ] 
                                 AS assoc2 ) 
  SELECT carrid AS id 
         FROM +cte1\assoc1 AS mainsrc 
         WHERE mainsrc~carrid = '...' 
  UNION 
  SELECT carrid AS id 
         FROM +cte2 
         WHERE +cte2~\assoc2[ (*) ]-carrid = '...' 
         ORDER BY id 
         INTO TABLE @FINAL(result).
```

### Executable Example

[Exposing Associations](abenwith_associations_abexa.md)

## Addition

`... REDIRECTED TO +cte VIA target`

### Description

The addition `REDIRECTED TO` replaces the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the association exposed using `WITH ASSOCIATIONS` with the common table expression specified as `+cte`.

- The following can be specified for `+cte`:

  - A common table expression defined in front of the current common table expression in the current [`WITH`](abapwith.md) statement.

  - The current common table expression

    `+cte` must specify the [association target](../../abap-glossary/abenassociation_target_glosry.md) as a data source of the exposed association in the `FROM` clause of the subquery.

- `VIA` must be followed by the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the exposed association under the name it uses in the `FROM` clause of `+cte`:

  - The [association target](../../abap-glossary/abenassociation_target_glosry.md) must be specified after `VIA` even if it is used only once. If [`AS`](abapfrom_clause.md) is used to define an alias name, this name must be specified.

  - If the [association target](../../abap-glossary/abenassociation_target_glosry.md) is used more than once as a data source of join expressions, one of these occurrences must be specified after `VIA`. The occurrence can be specified using the alias name or, if necessary, using its original name.

    All columns that occur in the `ON` condition of the exposed association must be listed as columns of the data source specified after `VIA` in the `SELECT` list of the subquery of `+cte`. If the [association target](../../abap-glossary/abenassociation_target_glosry.md) occurs more than once in the `FROM` clause of `+cte`, the addition `VIA` defines that these columns of the result set, which represent the right side of the join expression created when the exposed association is used in a subsequent path expression, are used in the `ON` condition of the expression.

If an [attribute](abenabap_sql_path_filter.md) is specified for the [association target](../../abap-glossary/abenassociation_target_glosry.md) when the exposed association is used in a subsequent path expression, this attribute affects the target `+cte` of the redirect. An attribute specified after `WITH ASSOCIATIONS` when the association is exposed, however, is applied to the original association target of the exposed association.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The common table expression `+cte2` of the following `WITH` statement uses the path expression `demo_cds_expose_assoc~\_spfli` to expose the CDS association `_spfli` that is itself exposed in the CDS view `demo_cds_expose_assoc`. The common table expression `+cte2` hence replaces this view as the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the CDS association. This is meaningless in this example, however, since the subquery of the common table expression reads all data from the data source. The common table expression `+cte1` uses `REDIRECTED TO +cte1~demo_cds_assoc_spfli` to replace the [association target](../../abap-glossary/abenassociation_target_glosry.md) `demo_cds_assoc_spfli` of the exposed path expression. `demo_cds_assoc_spfli` is the only data source of the common table expression `+cte1`. In the main query of the `WITH` statement, the path expression `+cte2\_spfli` is used to access the [association target](../../abap-glossary/abenassociation_target_glosry.md) `+cte1` of the exposed CDS association, which is restricted by the `WHERE` condition.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA carrid TYPE spfli-carrid. 
cl_demo_input=>request( CHANGING field = carrid ). 
 
WITH 
  +cte1 AS ( SELECT * 
                    FROM demo_cds_assoc_spfli 
                    WHERE carrid = @carrid ), 
  +cte2 AS ( SELECT * 
                    FROM demo_cds_expose_assoc ) 
        WITH ASSOCIATIONS ( demo_cds_expose_assoc~\_spfli 
          REDIRECTED TO +cte1 VIA demo_cds_assoc_spfli ) 
  SELECT spfli~* 
         FROM +cte2\_spfli AS spfli 
         ORDER BY spfli~carrid, spfli~connid 
         INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

[DDL Source Code](../../abap-glossary/abenddl_source_code_glosry.md) of `DEMO_CDS_EXPOSE_ASSOC`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC
  as select from scarr
  association [1..*] to demo_cds_assoc_spfli as _spfli 
    on scarr.carrid = _spfli.carrid
{
      _spfli,
  key scarr.carrid as scarr_carrid,
      _spfli._sflight,
      _spfli.carrid,
      _spfli.connid  
}
```

[DDL Source Code](../../abap-glossary/abenddl_source_code_glosry.md) of `DEMO_CDS_ASSOC_SPFLI`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_assoc_spfli 
  as select from
    spfli
    association [1..*] to demo_cds_sflight as _sflight on
          spfli.carrid = _sflight.carrid
      and spfli.connid = _sflight.connid
    association [1..1] to demo_cds_sairport as _sairport on
      spfli.airpfrom = _sairport.id
    {
      _sflight,
      _sairport,
      key carrid,
      key connid,
      airpfrom
    }
```

## Executable Examples

- [Exposing Associations with a Redirect](abenwith_assocs_redirect_abexa.md)

- [Exposing Associations with a Recursive Redirect](abenwith_assocs_redir_self_abexa.md)
