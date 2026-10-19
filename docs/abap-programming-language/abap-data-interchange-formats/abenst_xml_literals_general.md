---
title: "ST - General Literal XML Elements"
source_file: abenst_xml_literals_general.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Literal Template Content > ST - Literal XML Elements and Attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - General Literal XML Elements

## Syntax

``` abap
<element [attr] [tt:ref="node">] 
                [tt:lax=...] 
                [tt:extensible=...]> 
  ... 
</element>  
```

## Description

Here, `element` is the name of the element and `attr` is a set of optional literal attributes with any name. The optional ST-specific attribute [`tt:ref`](abenst_tt_ref.md) sets the current node `node` for the context of the literal element.

The optional ST-specific attributes [`tt:lax`](abenst_tt_lax.md) and [`tt:extensible`](abenst_tt_extensible.md) only have an effect during deserialization. `tt:lax` determines whether the element name `element` may differ during deserialization. `tt:extensible` specifies whether the content of the element can be extended by unspecified elements.

**Serializing Literal XML Elements**

In serializations, the element beginning `<element [attr]>` and its literal attributes `attr` are passed to the target XML data, the content of the element is serialized, and then the element ending `</element>` is passed. If there are multiple identically named literal attributes, only the last one is passed.

**Deserializing Literal XML Elements**

In deserializations, the beginning of the element is compared with the current position of the outbound XML data. By default, the source XML data must contain an identically named element with all literal attributes `attr` of the same content. The order of the literal attributes is of no importance. Superfluous literal attributes of the element in the source document are always ignored. If there are multiple identically named literal attributes, only the last one is respected.

After a successful comparison of the element beginning, the element content is deserialized and then the element ending is consumed.

## Hint

For information about handling namespaces, see [`tt.namespace`, Namespaces](abenst_tt_namespace.md).
