---
title: "ST - tt:attribute, Non-Literal Attributes"
source_file: abenst_tt_attribute.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:attribute, Non-Literal Attributes

## Syntax

``` abap
<tt:attribute name="attr" [ref="node"]> 
  ... 
</tt:attribute>  
```

## Description

Non-literal attributes of ST programs are defined using the `tt:attribute` statement. A non-literal attribute is assigned to an attribute of an XML element of the XML data. In serializations, the content of the non-literal attribute sets the attribute value in the XML data. In deserializations, the attribute value in the XML data is read and processed.

This statement can be specified one or more times within a literal XML element before its subelements. Each statement defines a non-literal attribute of the current XML element with the name `attr` specified in `name`. The optional `ref` attribute sets the [current node](abenst_tt_ref.md) `node` for the context of the non-literal attribute `attr`.

## Serializing Non-Literal Attributes

### Description

During serialization, the attribute name `attr` is written together with `="` or `='` into the definition of the current XML element. After that, the content of `tt:attribute` is serialized and the result is written after `attr="` or `attr='`. The result of the serialization must not be structured, which means that it must not contain subelements. Finally, the attribute is completed with `"` or `'`.

### Hint

In valid XML data, the attribute names of an XML element must be unique. For performance reasons, this is not checked in serializations of non-literal attributes. Instead, it must be done by the application developers themselves.

## Deserializing Non-Literal Attributes

### Description

In deserializations, the name of the attribute is compared to the attributes of the current XML element in the source XML data. The order of the attributes is not relevant. The deserialization fails if the attribute does not exist in the inbound stream. After that, the value of the attribute is deserialized according to the content of `tt:attribute` and the closing character is compared. The deserialization fails if not the entire content of the attribute is deserialized. Surplus attributes of the inbound stream are ignored.

## Special Form of Non-Literal Attributes

### Description

This special form of non-literal attributes combines the `tt:value` statement with the general syntax:

``` abap
`<tt:attribute name="attr" value-ref="node" 
                         [map=...] />`
```

This special form is a short form of:

``` abap
`<tt:attribute name="attr"> 
  <tt:value ref="node" [map=...] /> 
</tt:attribute>`
```

This allows the simple formulation of the frequent use case of expressing an elementary value as the content of an attribute.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the ST program `DEMO_ST_ATTRIBUTE1` below, the values of the data roots `ROOT1` and `ROOT2` are serialized as values of the attributes `attr1` and `attr2` of element *X* or are deserialized from them.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:template> 
    <X> 
      <tt:attribute name="attr1" value-ref="ROOT1"/> 
      <tt:attribute name="attr2" value-ref="ROOT2"/> 
      <Y>...</Y> 
    </X> 
  </tt:template> 
</tt:transform>
```

If the values *Text1* and *Text2* are passed to `ROOT1` and `ROOT2`, the result of a serialization is:

``` abap
<X attr1="Text1" attr2="Text2"> 
  <Y>...</Y> 
</X>
```

To deserialize the above result again, the ST program `DEMO_ST_ATTRIBUTE2` below is used, even though the sequence of the attributes is different.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:template> 
    <X> 
      <tt:attribute name="attr2" value-ref="ROOT2"/> 
      <tt:attribute name="attr1" value-ref="ROOT1"/> 
      <Y>...</Y> 
    </X> 
  </tt:template> 
</tt:transform>
```
