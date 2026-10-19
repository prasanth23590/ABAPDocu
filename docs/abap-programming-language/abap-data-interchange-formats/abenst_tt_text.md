---
title: "ST - tt:text, Literal Text"
source_file: abenst_tt_text.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Literal Template Content"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:text, Literal Text

## Syntax

``` abap
...>literal<...  

...><tt:text>literal</tt:text><...  
```

## Description

Here, `literal` stands for literal text. Each piece of content of a template that is not an element (in other words, not positioned between `< >`), is literal text. This includes line breaks and blanks that are combined under the term whitespace.

The first line above shows unmarked literal text. In ST programs, literal text can also be marked using the ST statement `tt:text`, indicated in the second line. The difference between these variants is that an unmarked literal text `literal` is ignored in serializations and deserializations if it contains nothing but blanks. A marked text is never ignored.

**Serializing Literal Text**

If a literal text is respected, all its characters are written to the target XML data. This includes any whitespace. Nothing is transferred if a text is ignored.

**Deserializing Literal Text**

The literal text of the XML source document is compared character by character (including blanks and line breaks) to the ST program and consumed. This means that at every position in the inbound stream at which there is literal text, the same text must appear in the ST program and must also be respected there.

## Hint

Literal texts with other characters other than whitespaces should be used sparingly; always identified with `tt:text`, and should not span multiple lines because line breaks and indents are potential sources of errors in deserializations. Unflagged texts should only be used to format the ST program with line breaks and blanks (indents). To avoid problems in deserializations of literal texts, they can be skipped using [`tt:skip`](abenst_tt_skip.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following ST program `DEMO_ST_TEXT1` contains four elements, `X1` to `X4`, with literal text.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:template> 
    <X0> 
      <X1> a b c </X1> 
      <X2><tt:text> d e f </tt:text></X2> 
      <X3>     </X3> 
      <X4><tt:text>     </tt:text></X4> 
    </X0> 
  </tt:template> 
</tt:transform>
```

The result of a serialization is as follows, with the blanks in `X3` being ignored:

`<X0><X1> a b c </X1><X2> d e f </X2><X3/><X4> </X4></X0>`

This XML data can itself be deserialized again by the above ST program. The ST program `DEMO_ST_TEXT2` below raises the exception `CX_ST_MATCH_ELEMENT`, because no blanks exist in the ST program for the blanks in the inbound stream within `X4`, due to the missing `tt:text` marking.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:template> 
    <X0> 
      <X1>a b c</X1> 
      <X2><tt:text>d e f</tt:text></X2> 
      <X3>     </X3> 
      <X4>     </X4> 
    </X0> 
  </tt:template> 
</tt:transform>
```

The ST program `DEMO_ST_TEXT3` below cannot deserialize the XML data either, because it expects line breaks in `X1` and more blanks due to the indent.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:template> 
    <X0> 
      <X1> 
        a b c 
      </X1> 
      <X2><tt:text>d e f</tt:text></X2> 
      <X3>     </X3> 
      <X4>     </X4> 
    </X0> 
  </tt:template> 
</tt:transform>
```

The ST program `DEMO_ST_TEXT4` below can deserialize the XML data, where all elements are skipped using [`tt:skip`](abenst_tt_skip.md).

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:template> 
    <X0> 
      <X1><tt:skip /></X1> 
      <X2><tt:skip /></X2> 
      <X3><tt:skip /></X3> 
      <X4><tt:skip /></X4> 
    </X0> 
  </tt:template> 
</tt:transform>
```
