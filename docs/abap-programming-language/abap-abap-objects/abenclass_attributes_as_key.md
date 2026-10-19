---
title: "ABAP Objects - Object References in Internal Tables"
source_file: abenclass_attributes_as_key.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Object References in Internal Tables

If the line type of an internal table contains object reference variables as components `comp`, the attributes `attr` of the object to which each reference of the line points can be used as key values when reading, sorting, and modifying table lines. This is possible in the following statements or expressions:

- `LOOP AT itab ... WHERE comp->attr ...`

- `READ TABLE itab ... WITH [TABLE] KEY comp->attr = ...`

- ` ... itab [ KEY ... comp->attr = ... ] ...`

- `SORT itab BY comp->attr ...`

- `DELETE itab WHERE comp->attr ...`

- `MODIFY itab ... TRANSPORTING ... WHERE comp->attr ...`

If a table contains unstructured lines with the type of an object reference variable, the attributes of the object to which a line points can be addressed using `table_line->attr`.
