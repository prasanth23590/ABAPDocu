---
title: "ST - tt:skip, Skip Elements"
source_file: abenst_tt_skip.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:skip, Skip Elements

## Syntax

``` abap
<tt:skip [name="name"] [count="cnt"]/>  
```

## Description

The `tt:skip` statement makes it possible to skip XML elements in deserializations. The statement can be located anywhere in a template.

**Serialization**

In serializations, `tt:skip` is ignored.

**Deserialization**

In deserializations, `tt:skip` has the following effect:

- Without additions, the following XML content of the inbound stream is consumed up to the end of the current element or non-literal attribute, but no ST statements are executed.

- Using the attributes `name` and `count`, as many consecutive elements of the name `name` are not deserialized as specified by the number in `cnt`.

- Using the attribute `name` but not `count`, or using the attribute `count="*"`, any number of consecutive elements with the name `name` are not deserialized.

- Not using the attribute `name` but using the attribute `count` attribute, as many subsequent elements after the current element are not deserialized as specified in `cnt`. For `cnt`, a number or `*` can be specified, where `*` can stand for any number of elements.

In deserializations, when comparing the template, the `tt:skip` statement is compared to the structure of the inbound XML stream as if the skipped elements were specified in its place. This means that a `tt:skip` statement with the `name` attribute is correct only if this position of the inbound XML stream also has the corresponding number of elements of the specified name, and the element of a template executed after a `tt:skip` statement must correspond to the element in the XML data that follows after the skipped elements.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the Simple Transformation `DEMO_ST_SKIP` below, the template is divided into a part for serialization and a part for deserialization. In deserializations, the first two `X1` elements, all `X2` elements after the first `X2` element, and the `Y` element including all its subelements are skipped.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
      <struc tt:ref="ROOT"> 
      <tt:serialize> 
          <X1><tt:value ref="COL0" /></X1> 
          <X1><tt:value ref="COL1" /></X1> 
          <X1><tt:value ref="COL2" /></X1> 
          <X2><tt:value ref="COL3" /></X2> 
          <X2><tt:value ref="COL4" /></X2> 
          <X2><tt:value ref="COL5" /></X2> 
          <Y> 
            <X3><tt:value ref="COL6" /></X3> 
            <X3><tt:value ref="COL7" /></X3> 
            <X3><tt:value ref="COL8" /></X3> 
          </Y> 
          <X4><tt:value ref="COL9" /></X4> 
      </tt:serialize> 
      <tt:deserialize> 
        <tt:skip name="X1" count="2" /> 
        <X1><tt:value ref="COMPA" /></X1> 
        <X2><tt:value ref="COMPB" /></X2> 
        <tt:skip name="X2" count="*" /> 
        <tt:skip name="Y" count="1" /> 
        <X4><tt:value ref="COMPC" /></X4> 
        <tt:skip/> 
      </tt:deserialize> 
    </struc> 
  </tt:template> 
</tt:transform>
```

The following ABAP program can call the transformation:

``` abap
DATA xml_string TYPE string. 
 
DATA: BEGIN OF struc, 
        col0 TYPE i VALUE 0, 
        col1 TYPE i VALUE 1, 
        col2 TYPE i VALUE 2, 
        col3 TYPE i VALUE 3, 
        col4 TYPE i VALUE 4, 
        col5 TYPE i VALUE 5, 
        col6 TYPE i VALUE 6, 
        col7 TYPE i VALUE 7, 
        col8 TYPE i VALUE 8, 
        col9 TYPE i VALUE 9, 
      END OF struc. 
 
DATA: BEGIN OF result, 
        compa TYPE i, 
        compb TYPE i, 
        compc TYPE i, 
      END OF result. 
 
CALL TRANSFORMATION demo_st_skip 
  SOURCE root = struc 
  RESULT XML xml_string. 
 
CALL TRANSFORMATION demo_st_skip 
  SOURCE XML xml_string 
  RESULT root = result.
```

After the deserialization, the components of `result` are given the values of the third, fourth, and tenth component of `struc`.
