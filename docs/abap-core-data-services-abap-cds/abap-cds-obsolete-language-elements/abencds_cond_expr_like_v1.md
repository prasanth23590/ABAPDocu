---
title: "CDS DDL - DDIC-Based View, cds_cond, LIKE"
source_file: abencds_cond_expr_like_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, LIKE

## Syntax

``` abap
... lhs [NOT] LIKE rhs [ESCAPE esc]...  
```

### Addition

[`... ESCAPE esc`](abencds_cond_expr_like_v1.md#addition)

## Overview

### Description

Pattern comparison in a [condition](abencds_conditional_expression_v1.md) in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The relational expression is true if the string in `lhs` matches (does not match) the pattern in `rhs`.

Rules for the operands `lhs` and `rhs`:

- The operand `lhs` must stick to the context-dependent rules listed in topic [CDS DDL - DDIC-based View, `cds_cond`, Operands](abencds_cond_expr_operands_v1.md).

- The data types of the operands must be comparable as described in topic [CDS DDL - DDIC-based View, `cds_cond`, Comparable Types](abencds_cond_expr_types_v1.md). Only character-like data types can be used.

- For `rhs`, only character-like [literals](abencds_literal_v1.md) without domain prefix are allowed.

Rules for the pattern in `rhs`:

- '%' is a wildcard character that represents any character string (including an empty string)

- '\_' stands for any character

### Hints

- Do not use patterns in `rhs` that are closed by wildcard characters to search for trailing blanks. The semantics of searches of this type are dependent on the database system that is used and in general do not produce the required result.

- If `lhs` contains the [null value](../../abap-glossary/abennull_value_glosry.md), then the comparison `lhs LIKE '%'` is **not** true. In ABAP SQL, this comparison **is** true (as described in topic [`sql_cond, LIKE`](../../abap-programming-language/abap-database-access/abenwhere_logexp_like.md)).

## Addition

`... ESCAPE esc` .### Description

The addition `ESCAPE` can be used to define a single-character [escape character](../../abap-glossary/abenescape_character_glosry.md). `esc` expects a character-like [literal](abencds_literal_v1.md) with the length 1 containing the escape character. In the pattern in `rhs`, the escape character in `esc` can be placed before a wildcard character or before the escape character itself. Then, the character directly following the escape character loses its special meaning.

If an escape character in `rhs` is not placed in front of one of the valid characters, a syntax error occurs.

The character `#` is recommended for the escape character `esc`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

To search for the pattern '100%', the following expression can be used with `#` as the escape character.

... LIKE '100#%' ESCAPE '#' ...
