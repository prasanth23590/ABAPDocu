---
title: "indicator structure"
source_file: abenindicator_structure_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# indicator structure

[ABAP Language](../abap-programming-language/abenabala_glossary.md) [ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md)

## Definition

[Substructure](abensubstructure_glosry.md) of a [structured type](abenstructured_type_glosry.md). The indicator structure is the last component of the structured type and mirrors the preceding components. The components of the substructure serve as indicators for features of the preceding components. Besides actual indicator structures, there are also [condensed indicator structures](abencondensed_ind_structure_glosry.md) that are realized by [byte fields](abenbyte_field_glosry.md) where the individual bits serve as indicators. Indicator structures can be defined with the addition [`WITH INDICATORS`](../abap-programming-language/abap-declarations/abaptypes_indicators.md) of the statement [`TYPES`](../abap-programming-language/abap-declarations/abaptypes_indicators.md) and can be used as [ABAP SQL indicators](abenabap_sql_indicator_glosry.md). In the latter case, also [inline declarations](abeninline_declaration_glosry.md) are possible.
