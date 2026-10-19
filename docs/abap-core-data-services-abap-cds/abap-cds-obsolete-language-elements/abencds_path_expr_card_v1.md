---
title: "CDS DDL - DDIC-Based View, path_expr, Cardinality"
source_file: abencds_path_expr_card_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, path_expr > CDS DDL - DDIC-Based View, path_expr, attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, path_expr, Cardinality

## Syntax

``` abap
...  1|*: ...  
```

## Description

Specifies the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the current CDS association:

- If the attribute `1:` is specified, the current CDS association is declared as unique.

- If the attribute `*:` is specified, the current CDS association is declared as non-unique.

The addition `1:` makes it possible to use filter conditions in path expressions, which are used in [`WHERE`](abencds_where_clause_v1.md) clauses or [`HAVING`](abencds_having_clause_v1.md) clauses. In a clause like this, it overwrites the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the [CDS association](abencds_association_v1.md). (The variant of the path expression can, however, be affected differently on certain database systems.)

The addition `1:` or `*:` cannot be specified as the only addition in square brackets.

## Hint

The addition `1:` prevents a syntax error if a path specified with filter conditions or with a non-unique cardinality is used in a [`WHERE`](abencds_where_clause_v1.md) clause or [`HAVING`](abencds_having_clause_v1.md) clause. However, at runtime, there is no check to validate whether the condition achieves the required unique cardinality.
