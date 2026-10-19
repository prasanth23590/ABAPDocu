---
title: "ranges table"
source_file: abenranges_table_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ranges table

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

[Internal table](abeninternal_table_glosry.md) with the columns `SIGN`, `OPTION`, `LOW`, and `HIGH`. Declared with the addition [`TYPE RANGE OF`](../abap-programming-language/abap-declarations/abaptypes_ranges.md) of the statements [`DATA`](../abap-programming-language/abap-declarations/abapdata.md) and [`TYPES`](../abap-programming-language/abap-declarations/abaptypes.md). A ranges table is used to store a [ranges condition](abenranges_condition_glosry.md) internally. A ranges table can be evaluated in a [comparison expression](abenrelational_expression_glosry.md) using the [comparison operator](abencomp_operator_glosry.md) [`IN`](../abap-programming-language/abap-program-flow-logic/abenlogexp_select_option.md), where each line of the table represents a separate comparison.
