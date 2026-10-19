---
title: "CDS DDL - CDS View Entity, case_expr"
source_file: abencds_case_expression_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, case_expr

## Syntax Forms

**[Simple Case Distinction](abencds_simple_case_expression_v2.md)**

``` abap
1. ... CASE operand 
           WHEN operand1 THEN result1 
          [WHEN operand2 THEN result2] 
           ... 
          [{ELSE resultn | ELSE NULL}] 
      END ...
```

**[Complex Case Distinction](abencds_searched_case_expr_v2.md)**

``` abap
2. ... CASE WHEN cds_cond1 THEN result1 
          [WHEN cds_cond2 THEN result2] 
          [WHEN cds_cond3 THEN result3] 
            ... 
          [{ELSE resultn | ELSE NULL}] 
      END ...
```

## Description

Case distinction in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). Either a [simple case distinction](abencds_simple_case_expression_v2.md) (simple case) or a [complex case distinction](abencds_searched_case_expr_v2.md) (searched case).

Case distinctions can be specified in the [`SELECT` list](abencds_select_list_v2.md) and in operand positions of other expressions.

The following rules apply to simple and complex case distinctions regarding the handling of semantic information from [CDS simple types](../../abap-glossary/abencds_simple_type_glosry.md) or [DDIC data elements](../../abap-glossary/abendata_element_glosry.md):

- The maximum technical data type of all `THEN` and `ELSE` branches is determined.

- The semantic information is determined as follows:

  - If none of the `THEN` or `ELSE` branches has the maximum technical data type, the result has the maximum technical data type and no semantic information.

  - If all `THEN` or `ELSE` branches that have the maximum technical data type also have the same semantic information (simple type or data element), the result has the maximum technical data type and the semantic information. Otherwise (i.e. different semantic information) the result has no semantic information.

## Hints

- When migrating a [CDS DDIC -based view](../../abap-glossary/abencds_v1_view_glosry.md) to a view entity, there may be an implicit behavior change in the derivation of semantic information from a DDIC data element or a CDS simple type, since there is a different logic for deriving semantic information. A different or no data element may be used for the CDS element resulting from a `CASE` expression. To prevent a behavior change, the element in question can be cast to a data element or simple type with the addition `PRESERVING TYPE`. For example:

  `... CAST ( my_element AS simple_type PRESERVING TYPE ) ...`

- Nested `CASE` expressions are evaluated from inner to outer.
