---
title: "ST - tt:value, Structures"
source_file: abenst_tt_value_structure.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:value, Structures

## Syntax

``` abap
<tt:value [ref="node"] [map="..."] 
                       [length|minLength|maxLength="len"] 
                       [xsd-type...] />  
```

## Description

The serialization and deserialization of structures results directly from the [addressing rules](abenst_addressing.md), because the structures can be mapped directly to the [tree structures](abenst_trees.md) that start from the data roots. When the current node is bound to an elementary component of an ABAP structure, the structure can be processed with `tt:value` just like an [elementary data object](abenst_tt_value_elementary.md).
