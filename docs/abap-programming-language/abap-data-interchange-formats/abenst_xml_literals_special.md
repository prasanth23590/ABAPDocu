---
title: "ST - Special Form of Literal XML Elements"
source_file: abenst_xml_literals_special.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Literal Template Content > ST - Literal XML Elements and Attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Special Form of Literal XML Elements

## Syntax

``` abap
<element [attr] tt:value-ref="node" 
                [tt:lax=...] 
                [tt:map=...] 
                [tt:length|tt:minLength|tt:maxLength="len"] />  
```

## Description

A special form of literal XML attributes combines the [`tt:value statement`](abenst_tt_value_elementary.md) with the [general form](abenst_xml_literals_general.md).

This special form is a short form of:

``` abap
`<element [attr] [tt:lax=...]> 
  <tt:value ref="node" [map=...] 
                       [length|minLength|maxLength="len"] /> 
</element>`
```

This makes it easy to formulate the frequent use case of expressing an elementary value as the content of an XML element.

The attribute `tt:extensible` cannot be specified together with `tt:value-ref`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following ST program `DEMO_ST_XML_LITERALS1` can be used to serialize an elementary data object:

``` abap
<?sap.transform simple?> 
<tt:transform 
   xmlns:tt="http://www.sap.com/transformation-templates"> 
   <tt:root name="ROOT"/> 
   <tt:template> 
     <X my_attr="attr"> 
        <tt:value ref="ROOT" /> 
      </X> 
  </tt:template> 
</tt:transform>
```

The result of a serialization is as follows if `abc` is the value of the ABAP data object bound to `ROOT`.

`<X my_attr="attr">abc</X>`

It should be noted that literal text that contains nothing but blank spaces (blanks and line breaks) is irrelevant in ST programs by default. For this reason, the serialization does not produce the following, for example:

``` abap
<X my_attr="attr"> 
  abc 
</X>
```

If the results of serializations with indents and line breaks are shown in examples, they are usually used for clarification and are not actually part of the result.

The following ST program `DEMO_ST_XML_LITERALS2` can deserialize the result, whereby the literal attribute `my_attr` is ignored:

``` abap
<?sap.transform simple?> 
<tt:transform 
   xmlns:tt="http://www.sap.com/transformation-templates"> 
   <tt:root name="ROOT"/> 
   <tt:template> 
    <X> 
       <tt:value ref="ROOT"/> 
     </X> 
  </tt:template> 
</tt:transform>
```

The following ST program `DEMO_ST_XML_LITERALS3` shows the equivalent short form to the program above:

``` abap
<?sap.transform simple?> 
<tt:transform 
   xmlns:tt="http://www.sap.com/transformation-templates"> 
   <tt:root name="ROOT"/> 
   <tt:template> 
    <X tt:value-ref="ROOT" /> 
  </tt:template> 
 </tt:transform>
```

The following ST program `DEMO_ST_XML_LITERALS4` raises the exception `CX_ST_MATCH_ELEMENT`, because an element *X* is returned instead of element `Y`.

``` abap
<?sap.transform simple?> 
<tt:transform 
   xmlns:tt="http://www.sap.com/transformation-templates"> 
   <tt:root name="ROOT"/> 
   <tt:template> 
    <Y> 
       <tt:value ref="ROOT"/> 
     </Y> 
  </tt:template> 
</tt:transform>
```

The following ST program `DEMO_ST_XML_LITERALS5` raises the exception `CX_ST_MATCH_ATTRIBUTE` despite identical element names because the expected literal attribute `my_value` does not exist in the source document.

``` abap
<?sap.transform simple?> 
<tt:transform 
    xmlns:tt="http://www.sap.com/transformation-templates"> 
    <tt:root name="ROOT"/> 
    <tt:template> 
     <X my_value="value"> 
        <tt:value ref="ROOT" /> 
      </X> 
   </tt:template> 
 </tt:transform>
```

A correct attribute name with an incorrect attribute content raises the exception `CX_ST_MATCH_TEXT`.
