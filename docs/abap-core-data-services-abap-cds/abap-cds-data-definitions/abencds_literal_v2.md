---
title: "CDS DDL - CDS View Entity, literal"
source_file: abencds_literal_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Elementary CDS Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, literal

[CDS literals](../../abap-glossary/abencds_literal_glosry.md) can be used in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).

In CDS, there are two different kinds of literals:

- [Typed literals](abencds_typed_literal_v2.md) (cover most built-in types of the ABAP Dictionary)

- [Untyped literals](abencds_untyped_literal_v2.md) (character literals and numeric literals)

Rules for escaping in typed and untyped literals in ABAP CDS:

- A single quote (') must be escaped

  - with a single quote: `'...''...'`

  - or with a backslash: `'...\'...'`

- A backslash (\\ must be escaped with a backslash: `'...\\...'`

## Hints

- The [literal operator](../../abap-glossary/abenliteral_operator_glosry.md) is not supported for CDS literals.

- [Fixed domain values](../abap-cds-obsolete-language-elements/abencds_literal_v1.md) are not supported in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md). However, if a CDS view entity selects data from another CDS entity with fixed domain values, then these elements with fixed domain values can be included in the current view entity.
