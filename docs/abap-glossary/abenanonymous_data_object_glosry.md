---
title: "anonymous data object"
source_file: abenanonymous_data_object_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# anonymous data object

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

[Unnamed data object](abenunnamed_data_object_glosry.md) that is created using the statement [`CREATE DATA`](../abap-programming-language/abap-creating-objects-and-values/abapcreate_data.md), the [instance operator](abeninstance_operator_glosry.md) [`NEW`](../abap-programming-language/abap-creating-objects-and-values/abenconstructor_expression_new.md), or the addition [`NEW`](../abap-programming-language/abap-database-access/abapselect_into_target.md) of the [`INTO`](../abap-programming-language/abap-database-access/abapinto_clause.md) clause of a [query](abenasql_query_glosry.md) and can be addressed using [reference variables](abenreference_variable_glosry.md) or [field symbols](abenfield_symbol_glosry.md). Anonymous data objects are stored in the [heap](abenheap_glosry.md). An anonymous data object is kept alive by [heap references](abenheap_reference_glosry.md) or by field symbols that address it or part of it. See also [named data object](abennamed_data_object_glosry.md) and [literal](abenabap_literal_glosry.md).
