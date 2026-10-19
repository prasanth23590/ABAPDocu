---
title: "ST - option, Mapping Rules for XML Fragments"
source_file: abenst_option_xsdany.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects > ST - option, Mapping Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - option, Mapping Rules for XML Fragments

## Syntax

``` abap
... option="[preserveWS][,stripWS][,preserveCharRef][,noRootAttr]"  
```

## Description

If one or more of the values `preserveWS`, `stripWS`, `preserveCharRef`, or `noRootAttr` are specified for `option`, the [mapping rule for XML fragments](abenabap_xslt_asxml_fragment.md) is changed. These values are only respected by data objects that are declared with a reference to the [DDIC domain](../../abap-glossary/abendomain_glosry.md) `XSDANY`.

- `preserveWS`

  If the value `preserveWS` is specified, all whitespaces (blanks and line breaks) are preserved in deserializations.

- `stripWS`

  If the value `stripWS` is specified, all whitespace (blanks and line breaks) is stripped in deserializations.

- `preserveCharRef`

  The value `preserveCharRef` prevents character references from being resolved.

- `noRootAttr`

  The value `noRootAttr` is used to change the [mapping rule for XML fragments](abenabap_xslt_asxml_fragment.md) so that no attribute `asx:root` containing the name of the root element of the XML fragment is added to the XML element. In deserializations, the root element is given the name of the XML element.

## Hint

In deserializations to `XSDANY`, whitespace in front of the first element is removed and whitespace from the first element is preserved.

## Executable Example

[ST, Mapping of XML Fragments](abenst_xsdany_abexa.md)
