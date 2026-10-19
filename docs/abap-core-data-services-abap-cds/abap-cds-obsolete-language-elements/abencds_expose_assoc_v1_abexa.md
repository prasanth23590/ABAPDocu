---
title: "CDS DDL - DDIC-Based View, Exposing CDS Associations"
source_file: abencds_expose_assoc_v1_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, select_list > CDS DDL - DDIC-Based View, SELECT, element > CDS DDL - DDIC-Based View, SELECT, expose_assoc"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, Exposing CDS Associations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how CDS associations are [exposed](abencds_select_list_association_v1.md) in the `SELECT` list of a CDS view.

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
CLASS cl_demo_cds_expose_assctns DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_expose_assctns IMPLEMENTATION. 
  METHOD main. 
 
    "Using exposed association in FROM clause 
    SELECT *                                            "#EC CI_NOWHERE 
           FROM demo_cds_expose_assoc_1\_demo_join2 AS path1 
           INTO TABLE @DATA(result1). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_1 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_1~d = demo_join2~d 
           INTO TABLE @FINAL(result1e). 
    ASSERT result1 = result1e. 
    out->write( result1 ). 
 
    "Using exposed association in FROM clause 
    SELECT * 
           FROM demo_cds_expose_assoc_1a\_demo_join2 AS path1a 
           INTO TABLE @DATA(result1a). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_1a 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_1a~d = demo_join2~d 
           INTO TABLE @FINAL(result1ae). 
    ASSERT result1a = result1ae. 
    out->write( result1a ). 
 
    "Using propagated association in FROM clause 
    SELECT *                                            "#EC CI_NOWHERE 
           FROM demo_cds_expose_assoc_2\_demo_join2 AS path2 
           INTO TABLE @DATA(result2). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_2 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_2~d = demo_join2~d 
           INTO TABLE @FINAL(result2e). 
    ASSERT result2 = result2e. 
    out->write( result2 ). 
 
    "Using propagated association in FROM clause 
    SELECT * 
           FROM demo_cds_expose_assoc_2a\_demo_join2 AS path2a 
           INTO TABLE @DATA(result2a). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_2a 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_2a~d = demo_join2~d 
           INTO TABLE @FINAL(result2ae). 
    ASSERT result2a = result2ae. 
    out->write( result2a ). 
 
 
    "Using propagated association in FROM clause 
    SELECT *                                            "#EC CI_NOWHERE 
           FROM demo_cds_expose_assoc_3\_demo_join2 AS path3 
           INTO TABLE @DATA(result3). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_3 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_3~d = demo_join2~d 
           INTO TABLE @FINAL(result3e). 
    ASSERT result3 = result3e. 
    out->write( result3 ). 
 
    "Using propagated association in FROM clause 
    SELECT * 
           FROM demo_cds_expose_assoc_3a\_demo_join2 AS path3a 
           INTO TABLE @DATA(result3a). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_3a 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_3a~d = demo_join2~d 
           INTO TABLE @FINAL(result3ae). 
    ASSERT result3a = result3ae. 
    out->write( result3a ). 
 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
 
    DELETE FROM demo_join1.                             "#EC CI_NOWHERE 
    INSERT demo_join1 FROM TABLE @( VALUE #( 
      ( a = 'a1' b = 'b1' c = 'c1' d = 'uu' ) 
      ( a = 'a2' b = 'b2' c = 'c2' d = 'uu' ) 
      ( a = 'a3' b = 'b3' c = 'c3' d = 'vv' ) 
      ( a = 'a4' b = 'b4' c = 'c4' d = 'ww' ) 
      ( a = 'a5' b = 'b5' c = 'c5' d = 'xx' ) ) ). 
    DELETE FROM demo_join2.                             "#EC CI_NOWHERE 
    INSERT demo_join2 FROM TABLE @( VALUE #( 
      ( d = 'uu' e = 'e1' f = 'f1' g = 'g1'  h = 'h1' ) 
      ( d = 'ww' e = 'e2' f = 'f2' g = 'g2'  h = 'h2' ) 
      ( d = 'xx' e = 'e3' f = 'f3' g = 'g3'  h = 'h3' ) ) ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example demonstrates how [CDS associations](../../abap-glossary/abencds_association_glosry.md) are accessed that are exposed in the `SELECT` list of CDS views. For each view, the data source is specified not directly, but as path expression, making use of an exposed association. As a comparison, the explicit join expression that produces the same result is shown.

- The following CDS view exposes its CDS association `_demo_join2`, which associates its data source `demo_join1` with the DDIC database table `demo_join1`. The field `d` used in the `ON` condition of the [association source](../../abap-glossary/abenassociation_source_glosry.md) must also be an element of the `SELECT` list.

``` abap
define view entity DEMO_CDS_EXPOSE_ASSOC_1
  as select from
    demo_join1 
    association to demo_join2 as _demo_join2 on
      _demo_join2.d = demo_join1.d
    {
      _demo_join2,
      demo_join1.d
    }
```

``` abap
When the CDS association `demo_cds_expose_assoc_1\_demo_join2` is accessed, the same inner join is created, that is explicitly used in the subsequent access\. Both produce the same result\.
```

- The following CDS view matches the preceding view, but has an additional `WHERE` condition.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSEXPASSO1A'
define view DEMO_CDS_EXPOSE_ASSOC_1A
  as select from
    demo_join1
    association to demo_join2 as _demo_join2 on
      _demo_join2.d = demo_join1.d
    {
      _demo_join2,
      demo_join1.d
    }
    where
      d = 'ww' 
```

``` abap
When the CDS association `demo_cds_expose_assoc_1a\_demo_join2` is accessed, the result set of the left side of the join is restricted by the `WHERE` condition in the association source of the path expression\.
```

- The following CDS view accesses the view `demo_cds_expose_assoc_1` above. It does not have its own CDS association, but it does expose the CDS association of its data source `demo_cds_expose_assoc_1._demo_join2`. Here, the field `demo_cds_expose_assoc_1.d` of the [association source](../../abap-glossary/abenassociation_source_glosry.md) used in the `ON` condition must again be part of the `SELECT` list.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSEXPASSO2'
define view DEMO_CDS_EXPOSE_ASSOC_2
  as select from
    DEMO_CDS_EXPOSE_ASSOC_1
    {
      DEMO_CDS_EXPOSE_ASSOC_1._demo_join2,
      DEMO_CDS_EXPOSE_ASSOC_1.d 
    }
```

``` abap
When the CDS association `demo_cds_expose_assoc_2\_demo_join2` is accessed, the same inner join is created as the subsequent explicit inner join and produces the same result\. The view `demo_cds_expose_assoc_2` is not subject to any further restrictions, which means the result is the same as when `demo_cds_expose_assoc_1\_demo_join2` is accessed\.
```

- The following CDS view matches the preceding view, but has an additional `WHERE` condition.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSEXPASSO2A'
define view DEMO_CDS_EXPOSE_ASSOC_2A
  as select from
    DEMO_CDS_EXPOSE_ASSOC_1
    {
      DEMO_CDS_EXPOSE_ASSOC_1._demo_join2,
      DEMO_CDS_EXPOSE_ASSOC_1.d
    }
    where 
      d = 'xx'
```

``` abap
When the CDS association `demo_cds_expose_assoc_2a\_demo_join2` is accessed, the result set of the left side of the join is restricted by the `WHERE` condition in the association source of the path expression\. This is different from accessing `demo_cds_expose_assoc_1a\_demo_join2`\. The CDS association defined in `demo_cds_expose_assoc_1a` is exposed, but the association source is `demo_cds_expose_assoc_2a` with a different `WHERE` condition\.
```

- The following CDS view accesses the view `demo_cds_expose_assoc_1a` above. It does not have its own CDS association, but it does expose the CDS association of its data source `demo_cds_expose_assoc_1a._demo_join2`.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSEXPASSO3'
define view DEMO_CDS_EXPOSE_ASSOC_3
  as select from
    DEMO_CDS_EXPOSE_ASSOC_1A
    {
      DEMO_CDS_EXPOSE_ASSOC_1A._demo_join2,
      DEMO_CDS_EXPOSE_ASSOC_1A.d 
    }
```

``` abap
When the CDS association `demo_cds_expose_assoc_3\_demo_join2` is accessed, the subsequent access creates an instance of the explicitly used inner join and produces its result\. The view `demo_cds_expose_assoc_3` is not subject to any further restrictions, which means the result is the same as when `demo_cds_expose_assoc_1a\_demo_join2` is accessed\.
```

- The following CDS view matches the preceding view, but has an additional `WHERE` condition.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSEXPASSO3A'
define view DEMO_CDS_EXPOSE_ASSOC_3A
  as select from DEMO_CDS_EXPOSE_ASSOC_1A
{
  DEMO_CDS_EXPOSE_ASSOC_1A._demo_join2,
  DEMO_CDS_EXPOSE_ASSOC_1A.d
}
where
  d = 'xx' 
```

``` abap
When the CDS association `demo_cds_expose_assoc_3a\_demo_join2` is accessed, the result set of the left side of the join is restricted by the `WHERE` condition in the association source of the path expression\. The disjoint `WHERE` condition in `demo_cds_expose_assoc_1a` means that no matching rows are found, however, and the result set of the left side of the join is empty\.
```
