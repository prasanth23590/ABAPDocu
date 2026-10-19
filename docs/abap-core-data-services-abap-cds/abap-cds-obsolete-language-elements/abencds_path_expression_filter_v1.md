---
title: "CDS DDL - DDIC-Based View, path_expr, Filter"
source_file: abencds_path_expression_filter_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, path_expr > CDS DDL - DDIC-Based View, path_expr, attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, path_expr, Filter

## Syntax

``` abap
... [WHERE] cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v1.md)

## Description

[Filter condition](../../abap-glossary/abenfilter_condition_glosry.md) for the current CDS association. If the join type is explicitly defined with [`INNER|{LEFT OUTER}`](abencds_path_expr_jointype_v1.md), the addition ` WHERE` must be specified explicitly. If this is not the case, `WHERE` must not be specified.

A filter condition is a condition [`cds_cond`](abencds_conditional_expression_v1.md) implemented as an expanded condition for the join when resolving the CDS association with the join in question. For the operands, [general](abencds_cond_expr_operands_v1.md) and [special rules](abencds_cond_expr_filter_v1.md) apply when specifying the condition.

If no filter condition is specified in the path expression, any default filter condition specified for the [CDS association](abencds_association_v1.md) is used.

## Hint

In most cases, a filter condition modifies the join expression defined for a CDS association of a path expression on the database. This means that a separate join expression is defined for each CDS association with a filter condition by default. This is not necessary, however, if a CDS association is used more than once and the same filter condition is specified. This is why the [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) [`AbapCatalog.compiler.compareFilter`](abencds_view_anno_v1.md) can be used to configure whether the filter conditions of multiple CDS associations are compared semantically for the path expressions defined as joins when a view is activated. If the filter condition matches, the associated join expression is created only once, which generally improves performance. In most cases, it is best to use the annotation and it is automatically proposed when creating a CDS view in the ADT. The result sets of the two configurations can, however, differ.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following three views contain path expressions with filter conditions in their `SELECT` list that are implemented as join expressions upon activation.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSASSFI1'
@AbapCatalog.compiler.compareFilter: true
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_assoc_filter1 
   as select from
    demo_join1
    association to Demo_Cds_Assoc_Join2 as _demo_join2 on
      _demo_join2.d = demo_join1.d
    {
      _demo_join2[ 
        inner where d = '1' ].d                         as d_2,
      _demo_join2[ 
        inner where d = '1' ].e                         as e_2,
      _demo_join2[ 
        inner where d = '1' ]._demo_join3[ 
                                inner where i = '2' ].i as i_3,
      _demo_join2[ 
        inner where d = '1' ]._demo_join3[ 
                                inner where i = '2' ].j as j_3
    }

```abap
@AbapCatalog.sqlViewName: 'DEMOCDSASSFI2'
@AbapCatalog.compiler.compareFilter: false
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_assoc_filter2 
   as select from
    demo_join1
    association to Demo_Cds_Assoc_Join2 as _demo_join2 on
      _demo_join2.d = demo_join1.d
    {
      _demo_join2[ 
        inner where d = '1' ].d                         as d_2,
      _demo_join2[ 
        inner where d = '1' ].e                         as e_2,
      _demo_join2[ 
        inner where d = '1' ]._demo_join3[ 
                                inner where i = '2' ].i as i_3,
      _demo_join2[ 
        inner where d = '1' ]._demo_join3[ 
                                inner where i = '2' ].j as j_3
    }

```abap
@AbapCatalog.sqlViewName: 'DEMOCDSASSFI3'
@AbapCatalog.compiler.compareFilter: true
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_assoc_filter3 
   as select from
    demo_join1
    association to Demo_Cds_Assoc_Join2 as _demo_join2 on
      _demo_join2.d = demo_join1.d
    {
      _demo_join2[ 
        inner where d = '1' ].d                         as d_2,
      _demo_join2[ 
        inner where d = '2' ].e                         as e_2,
      _demo_join2[ 
        inner where d = '3' ]._demo_join3[ 
                                inner where i = '5' ].i as i_3,
      _demo_join2[ 
        inner where d = '4' ]._demo_join3[ 
                                inner where i = '6' ].j as j_3
    }
```

In the first view, the annotation `AbapCatalog.compiler.compareFilter` has the recommended value `true`. The conditions are detected as identical and the variants of the path expressions on a SAP HANA database looks something like this:

``` abap
CREATE VIEW "DEMOCDSASSFI1" AS SELECT 
  "=A0"."D" AS "D_2", 
  "=A0"."E" AS "E_2", 
  "=A1"."I" AS "I_3", 
  "=A1"."J" AS "J_3" 
FROM ( 
  "DEMO_JOIN1" "DEMO_JOIN1" INNER JOIN "DEMO_CDS_ASJO2" "=A0" ON ( 
    "=A0"."D" = "DEMO_JOIN1"."D" AND 
    "=A0"."D" = N'1' 
  ) 
) INNER JOIN "DEMO_JOIN3" "=A1" ON ( 
  "=A1"."L" = "=A0"."D" AND 
  "=A1"."I" = N'2' 
)
```

In the second view, `AbapCatalog.compiler.compareFilter` has the value `false` and a join expression is defined for each CDS association of the path expressions regardless of the identical conditions. This means that this variant looks like the variant of the third views (in which all conditions are different):

``` abap
CREATE VIEW "DEMOCDSASSFI2" AS SELECT 
  "=A0"."D" AS "D_2", 
  "=A1"."E" AS "E_2", 
  "=A3"."I" AS "I_3", 
  "=A5"."J" AS "J_3" 
FROM ( 
  ( 
    ( 
      ( 
        ( 
          "DEMO_JOIN1" "DEMO_JOIN1" INNER JOIN "DEMO_CDS_ASJO2" "=A0" ON ( 
            "=A0"."D" = "DEMO_JOIN1"."D" AND 
            "=A0"."D" = N'1' 
          ) 
        ) INNER JOIN "DEMO_CDS_ASJO2" "=A1" ON ( 
          "=A1"."D" = "DEMO_JOIN1"."D" AND 
          "=A1"."D" = N'1' 
        ) 
      ) INNER JOIN "DEMO_CDS_ASJO2" "=A2" ON ( 
        "=A2"."D" = "DEMO_JOIN1"."D" AND 
        "=A2"."D" = N'1' 
      ) 
    ) INNER JOIN "DEMO_JOIN3" "=A3" ON ( 
      "=A3"."L" = "=A2"."D" AND 
      "=A3"."I" = N'2' 
    ) 
  ) INNER JOIN "DEMO_CDS_ASJO2" "=A4" ON ( 
    "=A4"."D" = "DEMO_JOIN1"."D" AND 
    "=A4"."D" = N'1' 
  ) 
) INNER JOIN "DEMO_JOIN3" "=A5" ON ( 
  "=A5"."L" = "=A4"."D" AND 
  "=A5"."I" = N'2' 
) 
 
CREATE VIEW "DEMOCDSASSFI3" AS SELECT 
  "=A0"."D" AS "D_2", 
  "=A1"."E" AS "E_2", 
  "=A3"."I" AS "I_3", 
  "=A5"."J" AS "J_3" 
FROM ( 
  ( 
    ( 
      ( 
        ( 
          "DEMO_JOIN1" "DEMO_JOIN1" INNER JOIN "DEMO_CDS_ASJO2" "=A0" ON ( 
            "=A0"."D" = "DEMO_JOIN1"."D" AND 
            "=A0"."D" = N'1' 
          ) 
        ) INNER JOIN "DEMO_CDS_ASJO2" "=A1" ON ( 
          "=A1"."D" = "DEMO_JOIN1"."D" AND 
          "=A1"."D" = N'2' 
        ) 
      ) INNER JOIN "DEMO_CDS_ASJO2" "=A2" ON ( 
        "=A2"."D" = "DEMO_JOIN1"."D" AND 
        "=A2"."D" = N'3' 
      ) 
    ) INNER JOIN "DEMO_JOIN3" "=A3" ON ( 
      "=A3"."L" = "=A2"."D" AND 
      "=A3"."I" = N'5' 
    ) 
  ) INNER JOIN "DEMO_CDS_ASJO2" "=A4" ON ( 
    "=A4"."D" = "DEMO_JOIN1"."D" AND 
    "=A4"."D" = N'4' 
  ) 
) INNER JOIN "DEMO_JOIN3" "=A5" ON ( 
  "=A5"."L" = "=A4"."D" AND 
  "=A5"."I" = N'6' 
)
```
