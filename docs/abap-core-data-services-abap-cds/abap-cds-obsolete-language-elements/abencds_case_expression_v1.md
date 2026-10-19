---
title: "CDS DDL - DDIC-Based View, case_expr"
source_file: abencds_case_expression_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, case_expr

## Syntax Forms

**[Simple Case Distinction](abencds_simple_case_expression_v1.md)**

``` abap
1. ... CASE operand 
           WHEN operand1 THEN result1 
          [WHEN operand2 THEN result2] 
           ... 
          [ELSE resultn] 
      END ...
```

**[Complex Case Distinction](abencds_searched_case_expr_v1.md)**

``` abap
2. ... CASE WHEN cds_cond1 THEN result1 
          [WHEN cds_cond2 THEN result2] 
          [WHEN cds_cond3 THEN result3] 
            ... 
          [ELSE resultn] 
      END ...
```

## Description

Case distinction in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). Either a [simple case distinction](abencds_simple_case_expression_v1.md) (simple case) or a [complex case distinction](abencds_searched_case_expr_v1.md) (searched case).

Case distinctions can be specified in the [`SELECT` list](abencds_select_list_v1.md) and in operand positions of other expressions.

The following rules apply to simple and complex case distinctions regarding the handling of semantic information from [DDIC data elements](../../abap-glossary/abendata_element_glosry.md):

- The maximum technical data type of all branches (`CASE`, `THEN`, `ELSE`) is determined.

- If there are several branches that have the maximum technical type, the data element of the last branch is inherited.

- If the branches have different technical data types, the result has the maximum technical data type and no data element. Data elements are inherited only if the data type, length, and number of decimal places match between the different branches.
