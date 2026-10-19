---
title: "Path Expressions, Use in the FROM Clause"
source_file: abenpath_expr_in_from_clause_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Path Expressions sql_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Path Expressions, Use in the FROM Clause

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [path expressions](abenabap_sql_path.md) in the [`FROM` clause](abapfrom_clause.md) in ABAP SQL.

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
CLASS cl_demo_select_from_path DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_from_path IMPLEMENTATION. 
  METHOD main. 
 
    DATA: 
      tz     TYPE s_tzone    VALUE 'UTC+1', 
      currc  TYPE s_currcode VALUE 'EUR', 
      fltime TYPE s_fltime   VALUE 0. 
 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = tz 
      )->add_field( CHANGING field = currc 
      )->add_field( CHANGING field = fltime )->request( ). 
 
    "Path expression in ABAP SQL 
    SELECT DISTINCT carrname 
           FROM demo_cds_assoc_sairport_tz( tz = @( to_upper( tz ) ) ) 
                \_spfli[ fltime > @fltime ] 
                \_scarr[ currcode = @( CONV s_currcode( 
                                              to_upper( currc ) ) ) ] 
                AS scarr 
           ORDER BY carrname 
           INTO TABLE @FINAL(result_path). 
 
    "Joins in ABAP SQL 
    SELECT DISTINCT scarr~carrname 
           FROM demo_cds_assoc_sairport_tz( tz = @( to_upper( tz ) ) ) 
                  AS airports 
             INNER JOIN demo_cds_assoc_spfli_scarr AS flights 
               ON  flights~airpfrom = airports~id AND 
                   flights~fltime > @fltime 
             INNER JOIN scarr 
               ON  scarr~carrid   = flights~carrid AND 
                   scarr~currcode = @( to_upper( currc ) ) 
           ORDER BY scarr~carrname 
           INTO TABLE @FINAL(result_join). 
 
    ASSERT result_path = result_join. 
    out->write( result_path ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The first `SELECT` statement accesses the CDS view entity `demo_cds_assoc_sairport_tz`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_assoc_sairport_tz
  with parameters
    tz : s_tzone
  as select from sairport
  association of many to many demo_cds_assoc_spfli_scarr as _spfli on
    sairport.id = _spfli.airpfrom
  {
    _spfli,
   key id
  }
  where
    time_zone = $parameters.tz
```

This view entity exposes its [CDS association](../../abap-glossary/abencds_association_glosry.md) `_spfli` in its `SELECT` list. The CDS association `_spfli` uses the view entity `demo_cds_assoc_spfli_scarr` as an [association target](../../abap-glossary/abenassociation_target_glosry.md):

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_assoc_spfli_scarr
  as select from
    spfli
    association to scarr as _scarr on
      spfli.carrid = _scarr.carrid
    {
      _scarr,
      key carrid,
      key airpfrom,
          fltime
    }
```

This view exposes its [CDS association](../../abap-glossary/abencds_association_glosry.md) `_scarr` in its `SELECT` list, making it possible to specify it in path expressions after `_spfli`. This CDS association uses a DDIC database table as a data source and always closes a path expression.

In the [`FROM` clause](abapfrom_clause.md), the first `SELECT` statement uses a path expression with the CDS associations `\_spfli` and `\_scarr` after the name of the CDS view. The names of all carriers are read that depart from airports in a specific time zone. The time zone is a [parameter](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_func_parameter_list.md) of CDS view `demo_cds_assoc_sairport_tz`, and a value is passed to it. Further restrictions apply to the local currency of the airline in a filter condition for the CDS association `_scarr` and on the flight time in a filter condition for the CDS association `_spfli`

The second `SELECT` statement demonstrates which joins and conditions must be created in ABAP SQL to achieve the same result. This is guaranteed by an assertion.
