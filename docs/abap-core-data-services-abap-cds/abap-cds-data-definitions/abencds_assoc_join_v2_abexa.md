---
title: "CDS DDL - CDS View Entity, Joins of CDS Associations"
source_file: abencds_assoc_join_v2_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, path_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Joins of CDS Associations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how path expressions are transformed to joins in ABAP CDS.

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
CLASS cl_demo_cds_assoc_joins_ve DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
 
  PRIVATE SECTION. 
    TYPES wa1 TYPE demo_join1 . 
    TYPES wa2 TYPE demo_join2 . 
    TYPES wa3 TYPE demo_join3 . 
    TYPES: 
      BEGIN OF wa. 
        INCLUDE TYPE wa1 AS wa1 RENAMING WITH SUFFIX _1. 
        INCLUDE TYPE wa2 AS wa2 RENAMING WITH SUFFIX _2. 
        INCLUDE TYPE wa3 AS wa3 RENAMING WITH SUFFIX _3. 
  TYPES END OF wa . 
    METHODS fill_tables . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_assoc_joins_ve IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      path_outer TYPE TABLE OF demo_cds_assoc_join1_o_ve 
                 WITH DEFAULT KEY, 
      path_inner TYPE TABLE OF demo_cds_assoc_join1_i_ve 
                 WITH DEFAULT KEY, 
      join_outer TYPE TABLE OF wa WITH DEFAULT KEY, 
      join_inner TYPE TABLE OF wa WITH DEFAULT KEY. 
 
    fill_tables( ). 
 
    out->begin_section( 'CDS Views' 
      )->begin_section( 'Path with [left outer]' ). 
    SELECT * 
           FROM demo_cds_assoc_join1_o_ve 
           INTO TABLE @path_outer.                      "#EC CI_NOWHERE 
    SORT path_outer. 
    out->write( path_outer 
      )->next_section( 'Path with [inner]' ). 
    SELECT * 
           FROM demo_cds_assoc_join1_i_ve 
           INTO TABLE @path_inner.                      "#EC CI_NOWHERE 
    SORT path_inner. 
    out->write( path_inner 
      )->end_section( )->end_section( 
      )->begin_section( `ABAP SQL Joins` 
      )->begin_section( 
        `LEFT OUTER JOINs` ). 
    SELECT FROM 
             demo_cds_assoc_join1_o_ve AS t1 
               LEFT OUTER JOIN 
                 demo_cds_assoc_join2_ve AS t2 ON t2~d = t1~d_1 
                     LEFT OUTER JOIN 
                       demo_join3 AS t3 ON t3~l = t2~d 
           FIELDS t1~a_1, 
                  t1~b_1, 
                  t1~c_1, 
                  t1~d_1, 
                  t2~d AS d_2, 
                  t2~e AS e_2, 
                  t2~f AS f_2, 
                  t2~g AS g_2, 
                  t2~h AS h_2, 
                  t3~i AS i_3, 
                  t3~j AS j_3, 
                  t3~k AS k_3, 
                  t3~l AS l_3                           "#EC CI_NOWHERE 
           INTO CORRESPONDING FIELDS OF TABLE @join_outer. 
    SORT join_outer. 
    out->write( join_outer 
      )->next_section( `INNER JOINs` ). 
    SELECT FROM 
             demo_cds_assoc_join1_i_ve AS t1 
               INNER JOIN 
                 demo_cds_assoc_join2_ve AS t2 ON t2~d = t1~d_1 
                     INNER JOIN 
                       demo_join3 AS t3 ON t3~l = t2~d 
           FIELDS t1~a_1, 
                  t1~b_1, 
                  t1~c_1, 
                  t1~d_1, 
                  t2~d AS d_2, 
                  t2~e AS e_2, 
                  t2~f AS f_2, 
                  t2~g AS g_2, 
                  t2~h AS h_2, 
                  t3~i AS i_3, 
                  t3~j AS j_3, 
                  t3~k AS k_3, 
                  t3~l AS l_3 
           INTO CORRESPONDING FIELDS OF TABLE @join_inner. 
    SORT join_inner. 
    out->write( join_inner ). 
    ASSERT path_inner = join_inner. 
    ASSERT path_outer = join_outer. 
  ENDMETHOD. 
  METHOD fill_tables. 
    out->begin_section( `Database Tables` ). 
    DELETE FROM demo_join1.                             "#EC CI_NOWHERE 
    INSERT demo_join1 FROM TABLE @( VALUE #( 
      ( a = 'a1' b = 'b1' c = 'c1' d = 'uu' ) 
      ( a = 'a2' b = 'b2' c = 'c2' d = 'uu' ) 
      ( a = 'a3' b = 'b3' c = 'c3' d = 'vv' ) 
      ( a = 'a4' b = 'b4' c = 'c4' d = 'ww' ) ) ). 
    SELECT * FROM demo_join1 INTO TABLE @FINAL(itab1).  "#EC CI_NOWHERE 
    DELETE FROM demo_join2.                             "#EC CI_NOWHERE 
    INSERT demo_join2 FROM TABLE @( VALUE #( 
      ( d = 'uu' e = 'e1' f = 'f1' g = 'g1'  h = 'h1' ) 
      ( d = 'ww' e = 'e2' f = 'f2' g = 'g2'  h = 'h2' ) 
      ( d = 'xx' e = 'e3' f = 'f3' g = 'g3'  h = 'h3' ) ) ). 
    SELECT * FROM demo_join2 INTO TABLE @FINAL(itab2).  "#EC CI_NOWHERE 
    DELETE FROM demo_join3.                             "#EC CI_NOWHERE 
    INSERT demo_join3 FROM TABLE @( VALUE #( 
      ( i = 'i1' j = 'j1' k = 'k1' l = 'vv' ) 
      ( i = 'i2' j = 'j2' k = 'k2' l = 'vv' ) 
      ( i = 'i3' j = 'j3' k = 'k3' l = 'ww' ) ) ). 
    SELECT * FROM demo_join3 INTO TABLE @FINAL(itab3).  "#EC CI_NOWHERE 
    out->begin_section( `demo_join1` 
      )->write( itab1 
      )->next_section( `demo_join2` 
      )->write( itab2 
      )->next_section( `demo_join3` 
      )->write( itab3 
      )->end_section( 
      )->end_section( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates which joins are implemented for [path expressions](abencds_path_expression_v2.md) containing [CDS associations](../../abap-glossary/abencds_association_glosry.md). The following two CDS view entities - `DEMO_CDS_ASSOC_JOIN1_O_VE` and `DEMO_CDS_ASSOC_JOIN1_I_VE` - access their own association `_demo_join2` in path expressions of the `SELECT` list and the [exposed](abencds_select_list_association_v2.md) CDS association `_demo_join3` of `DEMO_CDS_ASSOC_JOIN2`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ASSOC_JOIN1_O_VE
  as select from demo_join1
  association to DEMO_CDS_ASSOC_JOIN2_VE as _demo_join2
    on _demo_join2.d = demo_join1.d
{
 key  demo_join1.a                                      as a_1,
      demo_join1.b                                      as b_1,
      demo_join1.c                                      as c_1,
      demo_join1.d                                      as d_1,
      _demo_join2[left outer].d                         as d_2,
      _demo_join2[left outer].e                         as e_2,
      _demo_join2[left outer].f                         as f_2,
      _demo_join2[left outer].g                         as g_2,
      _demo_join2[left outer].h                         as h_2,
      _demo_join2[left outer]._demo_join3[left outer].i as i_3,
      _demo_join2[left outer]._demo_join3[left outer].j as j_3,
      _demo_join2[left outer]._demo_join3[left outer].k as k_3,
      _demo_join2[left outer]._demo_join3[left outer].l as l_3
}

```abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ASSOC_JOIN1_I_VE
  as select from demo_join1
  association to DEMO_CDS_ASSOC_JOIN2_VE as _demo_join2
    on _demo_join2.d = demo_join1.d
{
 key  demo_join1.a                            as a_1,
      demo_join1.b                            as b_1,
      demo_join1.c                            as c_1,
      demo_join1.d                            as d_1,
      _demo_join2[inner].d                    as d_2,
      _demo_join2[inner].e                    as e_2,
      _demo_join2[inner].f                    as f_2,
      _demo_join2[inner].g                    as g_2,
      _demo_join2[inner].h                    as h_2,
      _demo_join2[inner]._demo_join3[inner].i as i_3,
      _demo_join2[inner]._demo_join3[inner].j as j_3,
      _demo_join2[inner]._demo_join3[inner].k as k_3,
      _demo_join2[inner]._demo_join3[inner].l as l_3
}

```abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ASSOC_JOIN2_VE
  as select from demo_join2
  association to many demo_join3 as _demo_join3
    on _demo_join3.l = demo_join2.d
{
      _demo_join3,
  key demo_join2.d,
      demo_join2.e,
      demo_join2.f,
      demo_join2.g,
      demo_join2.h
}
```

[`LEFT OUTER`](abencds_path_expr_jointype_v2.md) and [`INNER`](abencds_path_expr_jointype_v2.md) are explicitly specified in the path expressions.

- `LEFT OUTER` specifies the implementation of CDS associations as a left outer join, which is the default behavior at these places.

- `INNER` specifies the implementation of CDS associations as an inner join, which overwrites the default behavior at these places.

In the DDL source code editor of the [ADT](../../abap-glossary/abenadt_glosry.md), the respective join can be seen in the display of the generated SQL DDL statement.

The class `CL_DEMO_CDS_ASSOC_JOINS_VE` displayed above shows that the result sets of the CDS view entities `DEMO_CDS_ASSOC_JOIN1_O_VE` and `DEMO_CDS_ASSOC_JOIN1_I_VE` are identical to the result sets of ABAP SQL statements [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) with explicitly programmed left outer and inner joins. The CDS view entities and the DDIC database table `DEMO_JOIN3` above are accessed. All involved database tables are filled with sample data. With an inner join, unlike a left outer join, only the row is returned for which the join condition `t3~l = t2~d` is fulfilled.
