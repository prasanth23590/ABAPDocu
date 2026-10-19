---
title: "ST - option, Mapping Rules"
source_file: abenst_option.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - option, Mapping Rules

## Syntax

``` abap
... option="...,..."  
```

## Description

The attribute `option` can be used to override the associated mapping rule, which depends on the data type, from and to [asXML](abenabap_xslt_asxml.md) for certain data types. The possible options can be specified as the content of the attribute, in a list separated by commas. Any options that are mutually exclusive produce a syntax check warning.

- [Mapping Rules for Elementary Types](abenst_option_format.md)

- [Mapping Rules for XML Fragments](abenst_option_xsdany.md)
