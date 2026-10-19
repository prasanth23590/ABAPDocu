---
title: "Path Expressions, Use in the SELECT List"
source_file: abenpath_expr_in_colspec_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Path Expressions sql_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Path Expressions, Use in the SELECT List

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [path expressions](abenabap_sql_path.md) in the [`SELECT` list](abapselect_list.md) in ABAP SQL.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_cds_association_path DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_association_path IMPLEMENTATION. 
  METHOD main. 
 
    DATA carrid TYPE scarr-carrid VALUE 'AA'. 
    cl_demo_input=>new( )->request( CHANGING field = carrid ). 
 
    "Path expressions in ABAP SQL 
    SELECT scarr~carrname, 
           \_spfli[ MANY TO MANY ]-connid AS connid, 
           \_spfli[ MANY TO MANY ]\_sflight[ 
             MANY TO MANY ]-fldate AS fldate, 
           \_spfli[ MANY TO MANY ]\_sairport-name AS name 
           FROM demo_cds_assoc_scarr AS scarr 
           WHERE scarr~carrid = @carrid 
           ORDER BY carrname, connid, fldate 
           INTO TABLE @FINAL(result1). 
 
    "Joins in ABAP SQL 
    SELECT demo_cds_assoc_scarr~carrname, 
           demo_cds_assoc_spfli~connid, 
           sflight~fldate AS fldate, 
           sairport~name  AS name 
           FROM demo_cds_assoc_scarr 
             LEFT OUTER JOIN demo_cds_assoc_spfli 
               ON demo_cds_assoc_spfli~carrid = 
                    demo_cds_assoc_scarr~carrid 
             LEFT OUTER JOIN demo_cds_sflight AS sflight 
               ON sflight~carrid = demo_cds_assoc_spfli~carrid AND 
                  sflight~connid = demo_cds_assoc_spfli~connid 
             LEFT OUTER JOIN demo_cds_sairport AS sairport 
               ON sairport~id = demo_cds_assoc_spfli~airpfrom 
           WHERE demo_cds_assoc_scarr~carrid = @carrid 
           ORDER BY demo_cds_assoc_scarr~carrname, 
                    demo_cds_assoc_spfli~connid, 
                    fldate 
           INTO TABLE @FINAL(result2). 
    ASSERT result1 = result2. 
 
    "Path expressions in CDS 
    SELECT * 
       FROM demo_cds_use_assocs( p_carrid = @carrid ) 
       ORDER BY carrname, connid, fldate 
       INTO TABLE @FINAL(result3). 
    ASSERT result1 = result3. 
 
    "Joins in CDS 
    SELECT * 
       FROM demo_cds_outer_joins( p_carrid = @carrid ) 
       ORDER BY carrname, connid, fldate 
       INTO TABLE @FINAL(result4). 
    ASSERT result1 = result4. 
 
    out->write( result1 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The first `SELECT` statement accesses the CDS view entity `demo_cds_assoc_scarr`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_assoc_scarr
  as select from scarr
  association [1..*] to demo_cds_assoc_spfli as _spfli on
    scarr.carrid = _spfli.carrid
  {
    _spfli,
    key carrid,
    carrname
  }
```

This view entity exposes its [CDS association](../../abap-glossary/abencds_association_glosry.md) `_spfli` in its `SELECT` list. The CDS association `_spfli` uses the view entity `demo_cds_assoc_spfli` as an [association target](../../abap-glossary/abenassociation_target_glosry.md):

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

This view entity exposes its [CDS associations](../../abap-glossary/abencds_association_glosry.md) `_sflight` and `_sairport` in its `SELECT` list, making it possible to specify them in path expressions after `_spfli`. These CDS associations use wrappers of DDIC database tables as data sources.

The `SELECT` statement contains three path expressions in its `SELECT` list alongside an elementary column specification. The first association contains only the CDS association `_spfli` of the CDS view entity `demo_cds_assoc_scarr` specified after `FROM`. The CDS associations of the data source of the root element are added to the other two path expressions. The path expressions specify the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the associations, which prevents syntax check warnings indicating that the path expressions affect the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the result set.

The second `SELECT` statement demonstrates which joins must be created in ABAP SQL to achieve the same result. This is guaranteed by an assertion.

The third `SELECT` statement accesses the CDS view entity `demo_cds_use_assocs`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_use_assocs
  with parameters
    p_carrid :s_carrid
  as select from
    demo_cds_assoc_scarr as scarr
    {
      scarr.carrname,
      scarr._spfli.connid,
      scarr._spfli._sflight.fldate,
      scarr._spfli._sairport.name
    }
    where
      scarr.carrid = $parameters.p_carrid
```

This view shows how the same paths specified in the `SELECT` statement of the view in [CDS DDL syntax](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_path_expression_v1.md) and also achieves the same result.

Finally, a fourth `SELECT` statement accesses the CDS view entity `demo_cds_outer_joins`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_outer_joins
  with parameters
    p_carrid :s_carrid
  as select from
                      demo_cds_assoc_scarr
      left outer join demo_cds_assoc_spfli on
        demo_cds_assoc_spfli.carrid = demo_cds_assoc_scarr.carrid
      left outer join demo_cds_sflight as sflight on
            sflight.carrid = demo_cds_assoc_spfli.carrid
        and sflight.connid = demo_cds_assoc_spfli.connid
      left outer join demo_cds_sairport as sairport on
        sairport.id = demo_cds_assoc_spfli.airpfrom
    {
      demo_cds_assoc_scarr.carrname as carrname,
      demo_cds_assoc_spfli.connid   as connid,
      sflight.fldate                as fldate,
      sairport.name                 as name
    }
    where
      demo_cds_assoc_scarr.carrid = $parameters.p_carrid
```

In this view, the same result is again achieved using joins.
