---
title: "CDS DDL - DDIC-Based View, Associations and Joins"
source_file: abencds_assoc_join_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Associations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, Associations and Joins

This topic describes the different use cases of CDS associations. It explains in which use case a join is generated on the database and which [join type](../../abap-glossary/abenjoin_type_glosry.md) is generated each time. Examples and screenshots of the SQL statement generated on the database are provided to further illustrate the transformation into joins.

When a CDS association is instantiated as join on the database, then the [association source](../../abap-glossary/abenassociation_source_glosry.md) represents the left side and the [association target](../../abap-glossary/abenassociation_target_glosry.md) represents the right side of the join. The `ON` condition of the association is added to the `ON` condition of the join.

There are the following basic use cases for CDS associations:

## Using a Path Expression in the `FROM` Clause

**Use case**: the data source of a CDS view entity after `FROM` is specified as path expression.

**Example**:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_assoc_from
  as select from demo_cds_assoc_spfli._sflight
{ 
  key carrid,
      connid  
}
```

**SQL statement generated on the database**: ![figure](images_abdoc_assoc_6.png)

The SQL statement generated on the database shows that the path expression is transformed into an [inner join](../../abap-glossary/abeninner_join_glosry.md) on the database.

## Exposing a CDS Association

**Use case**: an association is defined and exposed in the element list of a CDS view entity. In this way, it can be used in other CDS entities. However, the association is not part of the output and no data is selected from the association target.

**Example**:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_assoc_exposition
  as select from scarr
  association of one to many demo_cds_assoc_spfli as _spfli 
    on scarr.carrid = _spfli.carrid
{
      _spfli,
  key carrid,
      carrname
}
```

**SQL statement generated on the database**: ![figure](images_abdoc_assoc_1.png)

The SQL statement generated on the database shows that no join is generated and that the association is not mentioned in the statement that is passed to the database.

## Adding a Field from the Association Target to the Element List

**Use case**: an association is defined and an element from the association target is included in the element list of the same CDS view entity. In this example, the association is used, but not exposed, and therefore it cannot be used in path expressions of other CDS entities.

**Example**:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_assoc_element
  as select from scarr
  association of one to many demo_cds_assoc_spfli as _spfli 
    on scarr.carrid = _spfli.carrid
{
  key carrid, 
      _spfli.connid,
      carrname
}
```

**SQL statement generated on the database**: ![figure](images_abdoc_assoc_2.png)

The SQL statement generated on the database shows that the path expression is transformed into a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) on the database.

## Using a Path Expression in the `WHERE` Clause

**Use case**: an association is defined and used in the `WHERE` condition of the same CDS view entity. In this example, the association is used, but not exposed, and therefore it cannot be used in path expressions of other CDS entities.

**Example**:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_assoc_where
  as select from scarr
  association [1..1] to demo_cds_assoc_spfli as _spfli 
    on  scarr.carrid = _spfli.carrid and _spfli.connid = '....'
{
  key carrid, 
      carrname
} where _spfli.connid = '....'
```

**SQL statement generated on the database**: ![figure](images_abdoc_assoc_3.png)

The SQL statement generated on the database shows that the path expression is transformed into a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) with the cardinality many to one.

## Using an Exposed Association in an External View

**Use case**: A CDS view entity uses an association that was defined and published in another CDS entity. The association is used in a path expression to include a field from the association target in the element list of the CDS view entity.

**Example**:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cds_assoc_external_usage
  as select from
    demo_cds_assoc_exposition 
    {
      carrid,
      carrname, 
      _spfli.connid
    }
  
```

**SQL statement generated on the database**: ![figure](images_abdoc_assoc_4.png)

The SQL statement generated on the database shows that the path expression is transformed into a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) on the database. Note that this happens in the view that uses the association, and not in the view that defines the association.

## Using an Exposed Association in ABAP SQL

**Use case**: The program `DEMO_CDS_SELECT_ASSOC` uses an association that was defined and published in a CDS view entity in a path expression in ABAP SQL.

**Example**:

``` abap
REPORT demo_cds_select_assoc. 
 
CLASS demo DEFINITION 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    SELECT carrid, 
           carrname, 
           /_spfli[ (*) ]-connid 
           FROM demo_cds_assoc_exposition 
           INTO TABLE @DATA(result). 
  ENDMETHOD. 
ENDCLASS. 
 
START-OF-SELECTION. 
  demo=>main( ).
```

**SQL statement generated on the database**: ![figure](images_abdoc_assoc_5.png)

The path expression is transformed into a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) on the database.
