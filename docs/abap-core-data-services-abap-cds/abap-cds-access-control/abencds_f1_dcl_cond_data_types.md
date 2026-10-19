---
title: "CDS DCL - DEFINE ROLE, Data Types"
source_file: abencds_f1_dcl_cond_data_types.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, Data Types

The operand specified on the left side of a [condition](abencds_dcl_role_conditions.md) of an [access rule](abencds_dcl_role_rules.md) of a [CDS role](../../abap-glossary/abencds_role_glosry.md) cannot have all the [built-in data types in ABAP Dictionary](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). Only the following types are allowed:

- Numeric types

  - `INT1`, `INT2`, `INT4`, `INT8`

  - `DEC`

  - `DF16_DEC`, `DF16_RAW`, `DECFLOAT16`

  - `DF34_DEC`, `DF34_RAW`, `DECFLOAT34`

- Character-like types

  - `CHAR`

  - `SSTRING`

- Binary types

  - `RAW`

    CDS elements of type `RAW` support the operators [`IS [NOT] NULL`](../abap-cds-data-definitions/abencds_cond_expr_null_v2.md) and [`IS [NOT] INITIAL`](../abap-cds-data-definitions/abencds_cond_expr_initial_v2.md) and use as a part of the left side for a user-defined aspect or a PFCG mapping. Comparisons with a literal or an authorization field are not possible.

- Special types

  - `DATS`, `DATN`, `TIMS`, `TIMN`, `UTCLONG`

  - `NUMC`

Any other data types generally produce a syntax error in the definition of a CDS role. In [PFCG conditions](abencds_f1_cond_pfcg.md), however, invalid data types are sometimes not detected until runtime.

In PFCG conditions, field values of [authorizations](../../abap-glossary/abenauthorization_glosry.md) are compared with [CDS elements](../../abap-glossary/abencds_element_glosry.md) of the allowed data types and an appropriate [conversion](abencds_f1_dcl_pfcg_mapping.md) takes place.

Unlike `DATS` and `TIMS`, the types `DATN` and `TIMN` do not allow the [`LIKE`](../abap-cds-data-definitions/abencds_cond_expr_like_v2.md) operator to be used.
