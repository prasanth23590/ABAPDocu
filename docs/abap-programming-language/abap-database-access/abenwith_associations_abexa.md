---
title: "WITH, Exposing Associations"
source_file: abenwith_associations_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH > WITH, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, Exposing Associations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how CDS associations are exposed using [`WITH ASSOCIATIONS`](abapwith_associations.md) after a common [table expression](../../abap-glossary/abencommon_table_expression_glosry.md).

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
CLASS cl_demo_cds_with_associations DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_with_associations IMPLEMENTATION. 
  METHOD main. 
    WITH 
      +cte_2 AS ( SELECT demo_cds_expose_assoc_1~d 
                         FROM  demo_cds_expose_assoc_1 ) 
             WITH ASSOCIATIONS 
               ( demo_cds_expose_assoc_1~\_demo_join2 ) 
      SELECT * 
             FROM +cte_2\_demo_join2 AS demo_join2 
             INTO TABLE @FINAL(result2). 
    out->write( result2 ). 
 
    WITH 
      +cte_2a AS ( SELECT demo_cds_expose_assoc_1~d 
                          FROM  demo_cds_expose_assoc_1 
                          WHERE d = 'xx' ) 
              WITH ASSOCIATIONS 
                ( demo_cds_expose_assoc_1~\_demo_join2 ) 
      SELECT * 
             FROM +cte_2a\_demo_join2 AS demo_join2 
             INTO TABLE @FINAL(result2a). 
    out->write( result2a ). 
 
    WITH 
      +cte_3 AS ( SELECT demo_cds_expose_assoc_1a~d 
                         FROM  demo_cds_expose_assoc_1a ) 
             WITH ASSOCIATIONS 
               ( demo_cds_expose_assoc_1a~\_demo_join2 ) 
      SELECT * 
             FROM +cte_3\_demo_join2 AS demo_join2 
             INTO TABLE @FINAL(result3). 
    out->write( result3 ). 
 
    WITH 
      +cte_3a AS ( SELECT demo_cds_expose_assoc_1a~d 
                          FROM  demo_cds_expose_assoc_1a 
                          WHERE d = 'xx' ) 
              WITH ASSOCIATIONS 
                ( demo_cds_expose_assoc_1a~\_demo_join2 ) 
      SELECT * 
             FROM +cte_3a\_demo_join2 AS demo_join2 
             INTO TABLE @FINAL(result3a). 
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

The common table expressions in this example access the CDS views `demo_cds_expose_assoc_1` and `demo_cds_expose_assoc_1a` of the [executable example](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_expose_assoc_v1_abexa.md) for [exposing](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_select_list_association_v1.md) CDS associations in the `SELECT` list of CDS views. The subqueries of the common table expressions `+cte_2`, `+cte_2a`, `+cte_3`, and `+cte_3a` match the queries of the CDS views `demo_cds_expose_assoc_2`, `demo_cds_expose_assoc_2a`, `demo_cds_expose_assoc_3`, and `demo_cds_expose_assoc_3a` used in the executable example. The additions [`WITH ASSOCIATIONS`](abapwith_associations.md) expose the CDS association `_demo_join2` of the data sources of the subqueries. In the case of the CDS views, this is done in their `SELECT` list. When accessed using the path expression in the main queries of the `WITH` statements, the exposed CDS associations produce the exact same results as the corresponding accesses in the [example](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_expose_assoc_v1_abexa.md) for the CDS views. This demonstrates that the result sets of the subqueries are used as the left side of the join instances.
