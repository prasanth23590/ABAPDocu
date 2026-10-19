---
title: "WITH, Exposing Associations with a Redirect"
source_file: abenwith_assocs_redirect_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH > WITH, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, Exposing Associations with a Redirect

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the addition `REDIRECTED` of [`WITH ASSOCIATIONS`](abapwith_associations.md) for [common table expressions](../../abap-glossary/abencommon_table_expression_glosry.md).

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
CLASS cl_demo_with_assocs_redir DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_with_assocs_redir IMPLEMENTATION. 
  METHOD main. 
    DATA selection TYPE demo_join2-d VALUE 'xx'. 
    cl_demo_input=>new( )->request( CHANGING field = selection ). 
 
    "Path expressions in main query 
 
    WITH 
      +cte1 AS ( SELECT d, e, f 
                        FROM demo_join2 
                        WHERE d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
            WITH ASSOCIATIONS 
              ( demo_cds_expose_assoc_1~\_demo_join2 
                  REDIRECTED TO +cte1 VIA demo_join2 ) 
      SELECT demo_join2~* 
             FROM +cte2\_demo_join2 AS demo_join2 
             ORDER BY d, e, f 
             INTO TABLE @FINAL(result1). 
 
    WITH 
      +cte1 AS ( SELECT FROM demo_join2 AS src1 
                          CROSS JOIN demo_join2 AS src2 
                        FIELDS src1~d AS src1_d, 
                               src1~e AS src1_e, 
                               src1~f AS src1_f, 
                               src2~d AS src2_d, 
                               src2~e AS src2_e, 
                               src2~f AS src2_f 
                        WHERE src1~d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
            WITH ASSOCIATIONS 
              ( demo_cds_expose_assoc_1~\_demo_join2 
                  REDIRECTED TO +cte1 VIA src1 ) 
      SELECT demo_join2~* 
             FROM +cte2\_demo_join2 AS demo_join2 
             ORDER BY src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             INTO TABLE @FINAL(result2a). 
 
    WITH 
      +cte1 AS ( SELECT FROM demo_join2 AS src1 
                          CROSS JOIN demo_join2 AS src2 
                        FIELDS src1~d AS src1_d, 
                               src1~e AS src1_e, 
                               src1~f AS src1_f, 
                               src2~d AS src2_d, 
                               src2~e AS src2_e, 
                               src2~f AS src2_f 
                        WHERE src1~d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
            WITH ASSOCIATIONS 
              ( demo_cds_expose_assoc_1~\_demo_join2 
                  REDIRECTED TO +cte1 VIA src2 ) 
      SELECT demo_join2~* 
             FROM +cte2\_demo_join2 AS demo_join2 
             ORDER BY src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             INTO TABLE @FINAL(result2b). 
 
    WITH 
      +cte1 AS ( SELECT FROM demo_join2 AS src1 
                          CROSS JOIN demo_join2 AS src2 
                        FIELDS src1~d AS src1_d, 
                               src1~e AS src1_e, 
                               src1~f AS src1_f, 
                               src2~d AS src2_d, 
                               src2~e AS src2_e, 
                               src2~f AS src2_f 
                        WHERE src2~d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
            WITH ASSOCIATIONS 
              ( demo_cds_expose_assoc_1~\_demo_join2 
                  REDIRECTED TO +cte1 VIA src1 ) 
      SELECT demo_join2~* 
             FROM +cte2\_demo_join2 AS demo_join2 
             ORDER BY src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             INTO TABLE @FINAL(result3a). 
 
    WITH 
      +cte1 AS ( SELECT FROM demo_join2 AS src1 
                          CROSS JOIN demo_join2 AS src2 
                        FIELDS src1~d AS src1_d, 
                               src1~e AS src1_e, 
                               src1~f AS src1_f, 
                               src2~d AS src2_d, 
                               src2~e AS src2_e, 
                               src2~f AS src2_f 
                        WHERE src2~d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
            WITH ASSOCIATIONS 
              ( demo_cds_expose_assoc_1~\_demo_join2 
                  REDIRECTED TO +cte1 VIA src2 ) 
      SELECT demo_join2~* 
             FROM +cte2\_demo_join2 AS demo_join2 
             ORDER BY src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             INTO TABLE @FINAL(result3b). 
 
    IF NOT ( 
       result2a IS INITIAL AND 
       result2b IS INITIAL AND 
       result3a IS INITIAL AND 
       result3b IS INITIAL ). 
      ASSERT result2a <> result2b. 
      ASSERT result2a <> result3a. 
      ASSERT result2a <> result3b. 
      ASSERT result2b <> result3a. 
      ASSERT result2b <> result3b. 
      ASSERT result3a <> result3b. 
    ENDIF. 
 
    "Explicite joins in main query 
 
    WITH 
      +cte1 AS ( SELECT d, e, f 
                        FROM demo_join2 
                        WHERE d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
      SELECT +cte1~d, +cte1~e, +cte1~f 
             FROM +cte2 
               INNER JOIN +cte1 
                 ON +cte2~d = +cte1~d 
             ORDER BY +cte1~d, +cte1~e, +cte1~f 
             INTO TABLE @FINAL(join_result1). 
    ASSERT join_result1 = result1. 
 
    WITH 
      +cte1 AS ( SELECT FROM demo_join2 AS src1 
                          CROSS JOIN demo_join2 AS src2 
                        FIELDS src1~d AS src1_d, 
                               src1~e AS src1_e, 
                               src1~f AS src1_f, 
                               src2~d AS src2_d, 
                               src2~e AS src2_e, 
                               src2~f AS src2_f 
                        WHERE src1~d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
      SELECT src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             FROM +cte2 
               INNER JOIN +cte1 
                 ON +cte2~d = +cte1~src1_d 
             ORDER BY src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             INTO TABLE @FINAL(join_result2a). 
    ASSERT join_result2a = result2a. 
 
    WITH 
      +cte1 AS ( SELECT FROM demo_join2 AS src1 
                          CROSS JOIN demo_join2 AS src2 
                        FIELDS src1~d AS src1_d, 
                               src1~e AS src1_e, 
                               src1~f AS src1_f, 
                               src2~d AS src2_d, 
                               src2~e AS src2_e, 
                               src2~f AS src2_f 
                        WHERE src1~d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
      SELECT src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             FROM +cte2 
               INNER JOIN +cte1 
                 ON +cte2~d = +cte1~src2_d 
             ORDER BY src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             INTO TABLE @FINAL(join_result2b). 
    ASSERT join_result2b = result2b. 
 
    WITH 
      +cte1 AS ( SELECT FROM demo_join2 AS src1 
                          CROSS JOIN demo_join2 AS src2 
                        FIELDS src1~d AS src1_d, 
                               src1~e AS src1_e, 
                               src1~f AS src1_f, 
                               src2~d AS src2_d, 
                               src2~e AS src2_e, 
                               src2~f AS src2_f 
                        WHERE src2~d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
      SELECT src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             FROM +cte2 
               INNER JOIN +cte1 
                 ON +cte2~d = +cte1~src1_d 
             ORDER BY src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             INTO TABLE @FINAL(join_result3a). 
    ASSERT join_result3a = result3a. 
 
    WITH 
      +cte1 AS ( SELECT FROM demo_join2 AS src1 
                          CROSS JOIN demo_join2 AS src2 
                        FIELDS src1~d AS src1_d, 
                               src1~e AS src1_e, 
                               src1~f AS src1_f, 
                               src2~d AS src2_d, 
                               src2~e AS src2_e, 
                               src2~f AS src2_f 
                        WHERE src2~d = @selection ), 
      +cte2 AS ( SELECT demo_cds_expose_assoc_1~d 
                        FROM  demo_cds_expose_assoc_1 ) 
      SELECT src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             FROM +cte2 
               INNER JOIN +cte1 
                 ON +cte2~d = +cte1~src2_d 
             ORDER BY src1_d, src1_e, src1_f, src2_d, src2_e, src2_f 
             INTO TABLE @FINAL(join_result3b). 
    ASSERT join_result3b = result3b. 
 
    "Replace CTEs with internal tables 
 
    SELECT d, e, f 
           FROM demo_join2 
           WHERE d = @selection 
           INTO TABLE @FINAL(cte1_1). 
    SELECT demo_cds_expose_assoc_1~d 
           FROM  demo_cds_expose_assoc_1 
           INTO TABLE @FINAL(cte2_1). 
    DATA itab_result1 LIKE result1. 
    itab_result1 = VALUE #( 
      FOR wa2_1 IN cte2_1 
      FOR wa1_1 IN cte1_1 WHERE ( d = wa2_1-d ) 
        ( d = wa1_1-d e = wa1_1-e  f = wa1_1-f ) ). 
    SORT itab_result1 BY table_line. 
    ASSERT itab_result1 = result1. 
 
    SELECT FROM demo_join2 AS src1 
             CROSS JOIN demo_join2 AS src2 
           FIELDS src1~d AS src1_d, 
                  src1~e AS src1_e, 
                  src1~f AS src1_f, 
                  src2~d AS src2_d, 
                  src2~e AS src2_e, 
                  src2~f AS src2_f 
           WHERE src1~d = @selection 
           INTO TABLE @FINAL(cte1_2a). 
    SELECT demo_cds_expose_assoc_1~d 
           FROM  demo_cds_expose_assoc_1 
           INTO TABLE @FINAL(cte2_2a). 
    DATA itab_result2a LIKE result2a. 
    itab_result2a = VALUE #( 
      FOR wa2_2a IN cte2_2a 
      FOR wa1_2a IN cte1_2a WHERE ( src1_d = wa2_2a-d ) 
        ( src1_d = wa1_2a-src1_d 
          src1_e = wa1_2a-src1_e 
          src1_f = wa1_2a-src1_f 
          src2_d = wa1_2a-src2_d 
          src2_e = wa1_2a-src2_e 
          src2_f = wa1_2a-src2_f ) ). 
    SORT itab_result2a BY table_line. 
    ASSERT itab_result2a = result2a. 
 
    SELECT FROM demo_join2 AS src1 
             CROSS JOIN demo_join2 AS src2 
           FIELDS src1~d AS src1_d, 
                  src1~e AS src1_e, 
                  src1~f AS src1_f, 
                  src2~d AS src2_d, 
                  src2~e AS src2_e, 
                  src2~f AS src2_f 
           WHERE src1~d = @selection 
           INTO TABLE @FINAL(cte1_2b). 
    SELECT demo_cds_expose_assoc_1~d 
           FROM  demo_cds_expose_assoc_1 
           INTO TABLE @FINAL(cte2_2b). 
    DATA itab_result2b LIKE result2b. 
    itab_result2b = VALUE #( 
      FOR wa2_2b IN cte2_2b 
      FOR wa1_2b IN cte1_2b WHERE ( src2_d = wa2_2b-d ) 
        ( src1_d = wa1_2b-src1_d 
          src1_e = wa1_2b-src1_e 
          src1_f = wa1_2b-src1_f 
          src2_d = wa1_2b-src2_d 
          src2_e = wa1_2b-src2_e 
          src2_f = wa1_2b-src2_f ) ). 
    SORT itab_result2b BY table_line. 
    ASSERT itab_result2b = result2b. 
 
    SELECT FROM demo_join2 AS src1 
             CROSS JOIN demo_join2 AS src2 
           FIELDS src1~d AS src1_d, 
                  src1~e AS src1_e, 
                  src1~f AS src1_f, 
                  src2~d AS src2_d, 
                  src2~e AS src2_e, 
                  src2~f AS src2_f 
           WHERE src2~d = @selection 
           INTO TABLE @FINAL(cte1_3a). 
    SELECT demo_cds_expose_assoc_1~d 
           FROM  demo_cds_expose_assoc_1 
           INTO TABLE @FINAL(cte2_3a). 
    DATA itab_result3a LIKE result3a. 
    itab_result3a = VALUE #( 
      FOR wa2_3a IN cte2_3a 
      FOR wa1_3a IN cte1_3a WHERE ( src1_d = wa2_3a-d ) 
        ( src1_d = wa1_3a-src1_d 
          src1_e = wa1_3a-src1_e 
          src1_f = wa1_3a-src1_f 
          src2_d = wa1_3a-src2_d 
          src2_e = wa1_3a-src2_e 
          src2_f = wa1_3a-src2_f ) ). 
    SORT itab_result3a BY table_line. 
    ASSERT itab_result3a = result3a. 
 
    SELECT FROM demo_join2 AS src1 
             CROSS JOIN demo_join2 AS src2 
           FIELDS src1~d AS src1_d, 
                  src1~e AS src1_e, 
                  src1~f AS src1_f, 
                  src2~d AS src2_d, 
                  src2~e AS src2_e, 
                  src2~f AS src2_f 
           WHERE src2~d = @selection 
           INTO TABLE @FINAL(cte1_3b). 
    SELECT demo_cds_expose_assoc_1~d 
           FROM  demo_cds_expose_assoc_1 
           INTO TABLE @FINAL(cte2_3b). 
    DATA itab_result3b LIKE result3b. 
    itab_result3b = VALUE #( 
      FOR wa2_3b IN cte2_3b 
      FOR wa1_3b IN cte1_3b WHERE ( src2_d = wa2_3b-d ) 
        ( src1_d = wa1_3b-src1_d 
          src1_e = wa1_3b-src1_e 
          src1_f = wa1_3b-src1_f 
          src2_d = wa1_3b-src2_d 
          src2_e = wa1_3b-src2_e 
          src2_f = wa1_3b-src2_f ) ). 
    SORT itab_result3b BY table_line. 
    ASSERT itab_result3b = result3b. 
 
    out->write( result1 
      )->write_text( 'comes from' 
      )->write( data = cte2_1 name = '+cte2' 
      )->write( 'INNER JOIN' 
      )->write( data = cte1_1 name = '+cte1' 
      )->write( 'ON +cte2~d = +cte1~d' 
      )->line( 
      )->write( result2a 
      )->write_text( 'comes from' 
      )->write( data = cte2_2a name = '+cte2' 
      )->write( 'INNER JOIN' 
      )->write( data = cte1_2a name = '+cte1' 
      )->write( 'ON +cte2~d = +cte1~src1_d' 
      )->line( 
      )->write( result2b 
      )->write_text( 'comes from' 
      )->write( data = cte2_2b name = '+cte2' 
      )->write( 'INNER JOIN' 
      )->write( data = cte1_2b name = '+cte1' 
      )->write( 'ON +cte2~d = +cte1~src2_d' 
      )->line( 
      )->write( result3a 
      )->write_text( 'comes from' 
      )->write( data = cte2_3a name = '+cte2' 
      )->write( 'INNER JOIN' 
      )->write( data = cte1_3a name = '+cte1' 
      )->write( 'ON +cte2~d = +cte1~src1_d' 
      )->line( 
      )->write( result3b 
      )->write_text( 'comes from' 
      )->write( data = cte2_3b name = '+cte2' 
      )->write( 'INNER JOIN' 
      )->write( data = cte1_3b name = '+cte1' 
      )->write( 'ON +cte2~d = +cte1~src2_d' ). 
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

The common table expression `+cte2` accesses a CDS view entity using the following source code:

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

This example demonstrates different redirects of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the CDS association `demo_cds_expose_assoc_1~\_demo_join2` exposed by `+cte2` to a preceding common table expression `+cte1`:

- The first `WITH` statement shows a simple example in which the association target `demo_join2` of the CDS association `_demo_join2` exposed by `+cte2` occurs once under its name in `+cte1` as a data source. Only `demo_join2` can be specified after `VIA`. When the path expression `+cte2\_demo_join2` is accessed, an inner join is created between the result sets of `+cte2` and `+cte1`, whose `ON` condition compares the columns of the result sets defined by the CDS association.

- The next `WITH` statements show examples in which the association target `demo_join2` of the CDS association `_demo_join2` exposed by `+cte2` occurs twice as a data source in `+cte1` under different names, `src1` and `src2`.

  - `src1` is specified after `VIA` in the redirect of the first `WITH` statement. The `ON` condition of the join instance created when the path expression is accessed uses the column of the result set determined by`src1`.

  - `src2` is specified after `VIA` in the redirect of the second `WITH` statement. The `ON` condition of the join instance created when the path expression is accessed uses the column of the result set determined by`src2`.

  - The next two `WITH` statements repeat the preceding statements with a different `WHERE` condition in `+cte1`, which then produces different results.

The results of all reads are different from each other. The following reads demonstrate which join instances are created:

- First, the same `WITH` statements are executed as above, but the CDS association is not exposed. Instead, the inner join between the two common table expressions is shown explicitly. More specifically, the difference between the `ON` conditions `+cte2~d = +cte1~src1_d` and `cte2~d = +cte1~src2_d` should be noted, which demonstrates the effect of the data sources specified using `VIA`.

- The subqueries of the `WITH` statements are then executed as separate `SELECT` statements to store their results in internal tables for display purposes. Joins are also realized from internal tables using the value operator `VALUE`.

The example ensures that the results of associated reads also match each other.
