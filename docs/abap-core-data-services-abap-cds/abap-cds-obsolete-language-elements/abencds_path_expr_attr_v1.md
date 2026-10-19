---
title: "CDS DDL - DDIC-Based View, path_expr, attributes"
source_file: abencds_path_expr_attr_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, path_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, path_expr, attributes

## Syntax

``` abap
... [ [1|*:] [INNER|{LEFT OUTER}] [WHERE] [cds_cond] ] ...  
```

[`[1|*:]`](abencds_path_expr_card_v1.md) · [`[INNER|{LEFT OUTER}]`](abencds_path_expr_jointype_v1.md) · [`[WHERE] [cds_cond]`](abencds_path_expression_filter_v1.md)

## Description

For every CDS association [`_assoc`](abencds_association_v1.md) of a [path expression](abencds_path_expression_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), attributes for this part of the path expression can be defined in square brackets `[ ]`. The following attributes can be specified:

- With [`1|*:`](abencds_path_expr_card_v1.md), the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the section can be specified.

- With [`INNER|{LEFT OUTER}`](abencds_path_expr_jointype_v1.md) the [join type](../../abap-glossary/abenjoin_type_glosry.md) can be specified.

- With [`[WHERE] cds_cond`](abencds_path_expression_filter_v1.md) a filter condition `cds_cond` can be specified.
