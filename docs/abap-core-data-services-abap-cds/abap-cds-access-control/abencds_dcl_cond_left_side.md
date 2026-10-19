---
title: "CDS DCL - DEFINE ROLE, Left Side Host Expressions"
source_file: abencds_dcl_cond_left_side.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, Left Side Host Expressions

Instead of an element of the protected CDS entity, one of the following expressions can be used on the left side of [literal conditions](abencds_f1_cond_literal.md), [PFCG conditions](abencds_f1_cond_pfcg.md), and [user conditions](abencds_f1_cond_user.md):

- The actual value of a [parameter](../abap-cds-data-definitions/abencds_f1_param.md) of the CDS entity replaced by `$parameters.pname`

- The value of a [session variable](../../abap-glossary/abensession_variable_glosry.md) replaced by `$session.vname`

  (For session variables in CDS DDIC-based views (obsolete), see [here](../abap-cds-obsolete-language-elements/abencds_session_variable_v1.md). For session variables in CDS view entities, see [here](../abap-cds-data-definitions/abencds_session_variable_v2.md).) The set of supported session variables in access controls may be smaller than the one in CDS in general.

- A literal value

- The DCL function `CONTEXT_NODE_VALUES`. This function is reserved for use by SAP.

Conditions with left side host expressions are evaluated before the expression is passed to the database and evaluate as a true or false predicate.

Properties:

- The operators [`LIKE`](abencds_f1_cond_literal.md) and [`NOT LIKE`](abencds_f1_cond_literal.md) are mapped to the comparison operator for character-like data type [`CP`](../../abap-programming-language/abap-program-flow-logic/abenlogexp_strings.md). This results in non-case-sensitive pattern searches.

- Left side host expressions cannot be used on the left side of [PFCG mappings](../../abap-glossary/abencds_pfcg_mapping_glosry.md) or user-defined aspects.

## Hint

Runtime support for session variables and literals on the left side is an indirect consequence of inheritance with parameter replacement and also exists in DCL source code (for reasons of consistency). Direct use is not recommended.
