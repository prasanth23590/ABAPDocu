---
title: "ST - tt:empty, Empty Content"
source_file: abenst_tt_empty.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control > ST - tt:cond, Conditional Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:empty, Empty Content

## Syntax

``` abap
<tt:empty />  
```

## Description

In [conditioned transformations](abenst_tt_cond.md), it is possible to express empty template content explicitly using `tt:empty`: The element is allowed only within an element [`tt:[s-|d-]cond`](abenst_tt_cond.md) and must be the only element there. It is ignored (has no content) in serializations. In deserializations, it is possible to use `<tt:empty />` to express an empty [pattern](abenst_pattern.md).
