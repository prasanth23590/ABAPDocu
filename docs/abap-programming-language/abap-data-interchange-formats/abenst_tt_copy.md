---
title: "ST - tt:copy, asXML Format"
source_file: abenst_tt_copy.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:copy, asXML Format

## Syntax

``` abap
<tt:copy [ref="node"] />  
```

## Description

Statement `tt:copy` is used to serialize in and deserialize from the [asXML format](abenabap_xslt_asxml.md). It can be used on all data objects with the exception of reference variables or objects containing reference variables as components.

The optional attribute `ref` can be used to define the [current node](abenst_tt_ref.md) for the statement. If `ref` is not specified, the current node of the surrounding element is used implicitly.

**Serialization**

In serializations, the entire ABAP data object that is bound to the current node is recursively transformed with all its components to [asXML](abenabap_xslt_asxml.md) format and inserted into the XML data in place of the statement.

**Deserialization**

In deserializations, the XML data stream is interpreted as [asXML format](abenabap_xslt_asxml.md) and its values are passed to the ABAP data object that is bound to the current node.

## Hint

In serializations of data objects using `tt:copy`, it is important to note that a node will not be automatically inserted for the asXML format created. To get valid XML data, the node must be explicitly specified in the template. If not, the XML data cannot be deserialized. The only exceptions are structures with a single component or internal tables with a single line. However, these do not generally have any practical use.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following Simple Transformation `DEMO_ST_COPY` serializes the ABAP data object that is bound to data root `ROOT` under the node `<node>` into the asXML format. If the node `<node>` is not specified, the transformation would not produce valid XML data and deserialization would raise an exception.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <node> 
      <tt:copy  ref="ROOT" /> 
    </node> 
  </tt:template> 
</tt:transform>
```

When the ABAP program from the example in section [Internal Tables](abenst_tt_loop.md) calls this transformation, the serialization process has the following result:

``` abap
<node> 
  <item> 
    <KEY>2</KEY> 
    <VALUES> 
      <item>4</item> 
      <item>8</item> 
      <item>16</item> 
    </VALUES> 
  </item> 
  <item> 
    <KEY>3</KEY> 
    <VALUES> 
      <item>9</item> 
      <item>27</item> 
      <item>81</item> 
    </VALUES> 
  </item> 
  <item> 
    <KEY>4</KEY> 
    <VALUES> 
      <item>16</item> 
      <item>64</item> 
      <item>256</item> 
    </VALUES> 
  </item> 
</node>
```

The Simple Transformation is [symmetrical](abenst_symmetry.md).
