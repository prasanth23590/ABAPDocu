---
title: "CDS DDL - CDS View Entity, Exposing CDS Associations"
source_file: abencds_expose_assoc_v2_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, select_list > CDS DDL - CDS View Entity, SELECT, element > CDS DDL - CDS View Entity, SELECT, expose_assoc"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Exposing CDS Associations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how CDS associations are [exposed](abencds_select_list_association_v2.md) in the `SELECT` list of a CDS view entity.

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
CLASS cl_demo_cds_expose_assoc_ve DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS: 
      constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_expose_assoc_ve IMPLEMENTATION. 
  METHOD main. 
 
    "Using exposed association in FROM clause 
    SELECT *                                            "#EC CI_NOWHERE 
           FROM demo_cds_expose_assoc_1_ve\_demo_join2 AS _demo_join2 
           INTO TABLE @FINAL(result1). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_1_ve 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_1_ve~d = demo_join2~d 
           INTO TABLE @FINAL(result1e). 
    ASSERT result1 = result1e. 
    out->write( result1 ). 
 
    "Using exposed association in FROM clause 
    SELECT *                                            "#EC CI_NOWHERE 
           FROM demo_cds_expose_assoc_1a_ve\_demo_join2 AS _demo_join2 
           INTO TABLE @FINAL(result1a). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_1a_ve 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_1a_ve~d = demo_join2~d 
           INTO TABLE @FINAL(result1ae). 
    ASSERT result1a = result1ae. 
    out->write( result1a ). 
 
    "Using propagated association in FROM clause 
    SELECT *                                            "#EC CI_NOWHERE 
           FROM demo_cds_expose_assoc_2_ve\_demo_join2 AS _demo_join2 
           INTO TABLE @FINAL(result2). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_2_ve 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_2_ve~d = demo_join2~d 
           INTO TABLE @FINAL(result2e). 
    ASSERT result2 = result2e. 
    out->write( result2 ). 
 
    "Using propagated association in FROM clause 
    SELECT *                                            "#EC CI_NOWHERE 
           FROM demo_cds_expose_assoc_2a_ve\_demo_join2 AS _demo_join2 
           INTO TABLE @FINAL(result2a). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_2a_ve 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_2a_ve~d = demo_join2~d 
           INTO TABLE @FINAL(result2ae). 
    ASSERT result2a = result2ae. 
    out->write( result2a ). 
 
    "Using propagated association in FROM clause 
    SELECT *                                            "#EC CI_NOWHERE 
           FROM demo_cds_expose_assoc_3_ve\_demo_join2 AS _demo_join2 
           INTO TABLE @FINAL(result3). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_3_ve 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_3_ve~d = demo_join2~d 
           INTO TABLE @FINAL(result3e). 
    ASSERT result3 = result3e. 
    out->write( result3 ). 
 
    "Using propagated association in FROM clause 
    SELECT *                                            "#EC CI_NOWHERE 
           FROM demo_cds_expose_assoc_3a_ve\_demo_join2 AS _demo_join2 
           INTO TABLE @FINAL(result3a). 
    "Explicit join 
    SELECT demo_join2~* 
           FROM demo_cds_expose_assoc_3a_ve 
             INNER JOIN demo_join2 
               ON demo_cds_expose_assoc_3a_ve~d = demo_join2~d 
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

The executable example shown above demonstrates how [CDS associations](../../abap-glossary/abencds_association_glosry.md) are accessed that are exposed in the `SELECT` list of a CDS view entity. For each view, the data source in the `SELECT` statement is specified not directly, but as path expression, making use of an exposed association. For comparison, the explicit join expression that produces the same result is shown.

- The following CDS view entity exposes its CDS association `_demo_join2`, which associates its data source `demo_join1` with the DDIC database table `demo_join1`. The field `d` used in the `ON` condition of the [association source](../../abap-glossary/abenassociation_source_glosry.md) must also be an element of the `SELECT` list.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC_1_VE
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
When the CDS association `demo_cds_expose_assoc_1_ve\_demo_join2` is accessed, the same inner join is created that is explicitly used in the subsequent access\. Both produce the same result\.
```

- The following CDS view entity matches the preceding view, but has an additional `WHERE` condition.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC_1A_VE
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
When the CDS association `demo_cds_expose_assoc_1a_ve\_demo_join2` is accessed, the result set of the left side of the join is restricted by the `WHERE` condition in the association source of the path expression\.
```

- The following CDS view entity accesses the view `demo_cds_expose_assoc_1_ve` above. It does not have its own CDS association, but it exposes the CDS association of its data source `demo_cds_expose_assoc_1_ve._demo_join2`. Here, the field `demo_cds_expose_assoc_1_ve.d` of the [association source](../../abap-glossary/abenassociation_source_glosry.md) used in the `ON` condition must again be part of the `SELECT` list.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC_2_VE
  as select from
    DEMO_CDS_EXPOSE_ASSOC_1_VE
    {
      DEMO_CDS_EXPOSE_ASSOC_1_VE._demo_join2,
      DEMO_CDS_EXPOSE_ASSOC_1_VE.d 
    }
```

``` abap
When the CDS association `demo_cds_expose_assoc_2_ve\_demo_join2` is accessed, the same inner join is created as the subsequent explicit inner join and produces the same result\. The CDS view entity `demo_cds_expose_assoc_2_ve` is not subject to any further restrictions, which means the result is the same as when `demo_cds_expose_assoc_1_ve\_demo_join2` is accessed\.
```

- The following CDS view entity matches the preceding view, but has an additional `WHERE` condition.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC_2A_VE
  as select from
    DEMO_CDS_EXPOSE_ASSOC_1_VE
    {
      DEMO_CDS_EXPOSE_ASSOC_1_VE._demo_join2,
      DEMO_CDS_EXPOSE_ASSOC_1_VE.d
    }
    where 
      d = 'xx'
```

``` abap
When the CDS association `demo_cds_expose_assoc_2a_ve\_demo_join2` is accessed, the result set of the left side of the join is restricted by the `WHERE` condition in the association source of the path expression\. This is different from accessing `demo_cds_expose_assoc_1a_ve\_demo_join2`\. The CDS association defined in `demo_cds_expose_assoc_1a_ve` is exposed, but the association source is `demo_cds_expose_assoc_2a_ve` with a different `WHERE` condition\.
```

- The following CDS view entity accesses the view `demo_cds_expose_assoc_1a_ve` above. It does not have its own CDS association, but it exposes the CDS association of its data source `demo_cds_expose_assoc_1a_ve._demo_join2`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC_3_VE
  as select from
    DEMO_CDS_EXPOSE_ASSOC_1A_VE
    {
      DEMO_CDS_EXPOSE_ASSOC_1A_VE._demo_join2,
      DEMO_CDS_EXPOSE_ASSOC_1A_VE.d 
    }
```

``` abap
When the CDS association `demo_cds_expose_assoc_3_ve\_demo_join2` is accessed, the subsequent access creates an instance of the explicitly used inner join and produces its result\. The view `demo_cds_expose_assoc_3_ve` is not subject to any further restrictions, which means the result is the same as when `demo_cds_expose_assoc_1a_ve\_demo_join2` is accessed\.
```

- The following CDS view entity matches the preceding view, but has an additional `WHERE` condition.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC_3A_VE
  as select from DEMO_CDS_EXPOSE_ASSOC_1A_VE
{
  DEMO_CDS_EXPOSE_ASSOC_1A_VE._demo_join2,
  DEMO_CDS_EXPOSE_ASSOC_1A_VE.d
}
where
  d = 'xx' 
```

``` abap
When the CDS association `demo_cds_expose_assoc_3a_ve\_demo_join2` is accessed, the result set of the left side of the join is restricted by the `WHERE` condition in the association source of the path expression\. The disjoint `WHERE` condition in `demo_cds_expose_assoc_1a_ve` means that no matching rows are found, however, and the result set of the left side of the join is empty\.
```
