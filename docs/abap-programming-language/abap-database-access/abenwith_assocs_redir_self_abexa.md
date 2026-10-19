---
title: "WITH, Exposing Associations with a Recursive Redirect"
source_file: abenwith_assocs_redir_self_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH > WITH, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, Exposing Associations with a Recursive Redirect

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the addition `REDIRECTED` of [`WITH ASSOCIATIONS`](abapwith_associations.md) where the redirect is made to the current CTE.

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
CLASS cl_demo_with_assocs_redir_self DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_with_assocs_redir_self IMPLEMENTATION. 
  METHOD main. 
    DATA selection TYPE demo_join2-d VALUE 'xx'. 
    cl_demo_input=>new( )->request( CHANGING field = selection ). 
 
    "Path expressions in main query 
 
    WITH 
      +cte AS ( SELECT FROM demo_cds_expose_assoc_1 AS cds 
                         INNER JOIN  demo_join2 AS src1 
                           ON cds~d = src1~d 
                             CROSS JOIN demo_join2 AS src2 
                       FIELDS cds~d  AS cds_d, 
                              src1~d AS src1_d, 
                              src1~e AS src1_e, 
                              src1~f AS src1_f, 
                              src2~d AS src2_d, 
                              src2~e AS src2_e, 
                              src2~f AS src2_f 
                       WHERE cds~d = @selection ) 
            WITH ASSOCIATIONS 
              ( cds~\_demo_join2 
                  REDIRECTED TO +cte VIA src1 ) 
      SELECT FROM +cte\_demo_join2 AS demo_join2 
             FIELDS demo_join2~* 
             ORDER BY cds_d, 
                      src1_d, 
                      src1_e, 
                      src1_f, 
                      src2_d, 
                      src2_e, 
                      src2_f 
             INTO TABLE @FINAL(resulta). 
 
    WITH 
      +cte AS ( SELECT FROM demo_cds_expose_assoc_1 AS cds 
                         INNER JOIN  demo_join2 AS src1 
                           ON cds~d = src1~d 
                             CROSS JOIN demo_join2 AS src2 
                       FIELDS cds~d  AS cds_d, 
                              src1~d AS src1_d, 
                              src1~e AS src1_e, 
                              src1~f AS src1_f, 
                              src2~d AS src2_d, 
                              src2~e AS src2_e, 
                              src2~f AS src2_f 
                       WHERE cds~d = @selection ) 
            WITH ASSOCIATIONS 
              ( cds~\_demo_join2 
                  REDIRECTED TO +cte VIA src2 ) 
      SELECT FROM +cte\_demo_join2 AS demo_join2 
             FIELDS demo_join2~* 
             ORDER BY cds_d, 
                      src1_d, 
                      src1_e, 
                      src1_f, 
                      src2_d, 
                      src2_e, 
                      src2_f 
             INTO TABLE @FINAL(resultb). 
 
    IF NOT ( 
       resulta IS INITIAL AND 
       resultb IS INITIAL  ). 
      ASSERT resulta <> resultb. 
    ENDIF. 
 
    "Explicite joins in main query 
 
    WITH 
      +cte AS ( SELECT FROM demo_cds_expose_assoc_1 AS cds 
                         INNER JOIN  demo_join2 AS src1 
                           ON cds~d = src1~d 
                             CROSS JOIN demo_join2 AS src2 
                       FIELDS cds~d  AS cds_d, 
                              src1~d AS src1_d, 
                              src1~e AS src1_e, 
                              src1~f AS src1_f, 
                              src2~d AS src2_d, 
                              src2~e AS src2_e, 
                              src2~f AS src2_f 
                       WHERE cds~d = @selection ) 
      SELECT FROM +cte AS cte_1 
               INNER JOIN +cte AS cte_2 
                 ON cte_1~cds_d = cte_2~src1_d 
             FIELDS cte_2~* 
             ORDER BY cte_2~cds_d, 
                      cte_2~src1_d, 
                      cte_2~src1_e, 
                      cte_2~src1_f, 
                      cte_2~src2_d, 
                      cte_2~src2_e, 
                      cte_2~src2_f 
             INTO TABLE @FINAL(join_resulta). 
    ASSERT join_resulta = resulta. 
 
    WITH 
      +cte AS ( SELECT FROM demo_cds_expose_assoc_1 AS cds 
                         INNER JOIN  demo_join2 AS src1 
                           ON cds~d = src1~d 
                             CROSS JOIN demo_join2 AS src2 
                       FIELDS cds~d  AS cds_d, 
                              src1~d AS src1_d, 
                              src1~e AS src1_e, 
                              src1~f AS src1_f, 
                              src2~d AS src2_d, 
                              src2~e AS src2_e, 
                              src2~f AS src2_f 
                       WHERE cds~d = @selection ) 
      SELECT FROM +cte AS cte_1 
               INNER JOIN +cte AS cte_2 
                 ON cte_1~cds_d = cte_2~src2_d 
             FIELDS cte_2~* 
             ORDER BY cte_2~cds_d, 
                      cte_2~src1_d, 
                      cte_2~src1_e, 
                      cte_2~src1_f, 
                      cte_2~src2_d, 
                      cte_2~src2_e, 
                      cte_2~src2_f 
             INTO TABLE @FINAL(join_resultb). 
    ASSERT join_resultb = resultb. 
 
    "Show results of CTEs 
 
    SELECT FROM demo_cds_expose_assoc_1 AS cds 
                         INNER JOIN  demo_join2 AS src1 
                           ON cds~d = src1~d 
                             CROSS JOIN demo_join2 AS src2 
           FIELDS cds~d  AS cds_d, 
                  src1~d AS src1_d, 
                  src1~e AS src1_e, 
                  src1~f AS src1_f, 
                  src2~d AS src2_d, 
                  src2~e AS src2_e, 
                  src2~f AS src2_f 
           WHERE cds~d = @selection 
           INTO TABLE @FINAL(ctea). 
    DATA itab_resulta LIKE resulta. 
    itab_resulta = VALUE #( 
      FOR wa2 IN ctea 
      FOR wa1 IN ctea WHERE ( src1_d = wa2-src1_d ) 
        ( cds_d  = wa1-cds_d 
          src1_d = wa1-src1_d 
          src1_e = wa1-src1_e 
          src1_f = wa1-src1_f 
          src2_d = wa1-src2_d 
          src2_e = wa1-src2_e 
          src2_f = wa1-src2_f ) ). 
    SORT itab_resulta BY table_line. 
    ASSERT itab_resulta = resulta. 
 
    SELECT FROM demo_cds_expose_assoc_1 AS cds 
                         INNER JOIN  demo_join2 AS src1 
                           ON cds~d = src1~d 
                             CROSS JOIN demo_join2 AS src2 
           FIELDS cds~d  AS cds_d, 
                  src1~d AS src1_d, 
                  src1~e AS src1_e, 
                  src1~f AS src1_f, 
                  src2~d AS src2_d, 
                  src2~e AS src2_e, 
                  src2~f AS src2_f 
           WHERE cds~d = @selection 
           INTO TABLE @FINAL(cteb). 
    DATA itab_resultb LIKE resultb. 
    itab_resultb = VALUE #( 
      FOR wb2 IN cteb 
      FOR wb1 IN cteb WHERE ( src2_d = wb2-src1_d ) 
        ( cds_d  = wb1-cds_d 
          src1_d = wb1-src1_d 
          src1_e = wb1-src1_e 
          src1_f = wb1-src1_f 
          src2_d = wb1-src2_d 
          src2_e = wb1-src2_e 
          src2_f = wb1-src2_f ) ). 
    SORT itab_resultb BY table_line. 
    ASSERT itab_resultb = resultb. 
 
    out->write( resulta 
      )->write_text( 'comes from' 
      )->write( data = ctea name = '+cte1' 
      )->write( 'INNER JOIN' 
      )->write( data = ctea name = '+cte2' 
      )->write( 'ON +cte1~cds_d = +cte2~src1_d' 
      )->line( 
      )->write( resultb 
      )->write_text( 'comes from' 
      )->write( data = cteb name = '+cte1' 
      )->write( 'INNER JOIN' 
      )->write( data = cteb name = '+cte2' 
      )->write( 'ON +cte1~cds_d = +cte2~src2_d' ). 
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

As in the example [Exposing Association with a Redirect](abenwith_assocs_redirect_abexa.md), a common table expression `+cte` accesses the CDS view entity `DEMO_CDS_EXPOSE_ASSOC_1` and exposes its CDS association `_demo_join2`. Here, however, the redirect is made to the current common table expression and not to a preceding common table expression. This expression specifies the [association target](../../abap-glossary/abenassociation_target_glosry.md) `demo_join2` of the exposed CDS association twice as an additional data source under the names `src1` and `src2`.

- In the first `WITH` statement, the data source is specified using `src1`.

- In the second `WITH` statement, the data source is specified using `src2`.

The results of the two reads are different from each other. The following reads again demonstrate which join instances are created. The different results come from the different `ON` conditions, where the column of `src1` and the column of `src2` are both evaluated once.
