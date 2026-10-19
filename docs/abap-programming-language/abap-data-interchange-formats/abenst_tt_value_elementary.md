---
title: "ST - tt:value, Elementary Data Objects"
source_file: abenst_tt_value_elementary.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:value, Elementary Data Objects

## Syntax

``` abap
<tt:value [ref="node"] [map="..."] 
                       [length|minLength|maxLength="len"] 
                       [xsd-type...] 
                       [option="...,..."] />  
```

## Description

This form of the ST statement `tt:value` serializes and deserializes elementary data objects.

The optional attribute `ref` can be used to define the [current node](abenst_tt_ref.md) for the statement. If `ref` is not specified, the current node of the surrounding element is used.

Elementary ABAP values are mapped to XML values and vice versa in accordance with the [asXML rules for elementary types](abenabap_xslt_asxml_elementary.md). A special [mapping](abenabap_xslt_asxml_schema.md) is defined for data objects whose elementary data type refers to special domains in the ABAP Dictionary.

- [`map`](abenst_map.md) can be used to specify a mapping list that maps multiple values to a single value.

- [`length`](abenst_length.md), [`minLength`](abenst_length.md), or [`maxLength`](abenst_length.md) can be used to specify a length.

- The value can be validated by specifying [`xsd-type...`](abenst_xsd_type.md).

- [`option="...,..."`](abenst_option.md) can be specified to define special formats for certain data types, so that the formats override the associated mapping rule.

**Serialization**

If [`map`](abenst_map.md) is not specified, the value of the elementary ABAP data object that is bound to the current node is inserted into the XML data in place of the statement in asXML format or in the format specified in [`option`](abenst_option.md) in serializations.

**Deserialization**

During deserialization, the current value of the XML inbound stream is passed to the ABAP data object. The end of the XML value is determined either by the end of the text node (for example, at the element end) or by the beginning of a literal text following directly in the ST program. The XML value must match the asXML representation of the ABAP data type or a format specified in [`option`](abenst_option.md) and be in its value range.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

[Simple Transformation, `tt:value`](abenst_value_abexa.md)
