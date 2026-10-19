---
title: "ST - length, minLength, maxLength, Specified Length"
source_file: abenst_length.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - length, minLength, maxLength, Specified Length

## Syntax

``` abap
... length="len" ...   
... minLength="len" ...   
... maxLength="len" ...  
```

## Description

The attributes `length`, `minLength`, and `maxLength` can be used to specify a length `len` for [`tt:value`](abenst_tt_value_elementary.md), [`tt:write`](abenst_tt_write.md), and [`tt:read`](abenst_tt_read.md). This restricts the length of the data to be passed in serializations and deserializations.

Positive integers can be specified for `len`. Lengths can be specified for data nodes or variables with the ABAP types `c`, `x`, `string`, and `xstring`. Any other data types ignore any length specifications.

Specifying the `length` attribute always affects `tt:value` and `tt:write` as if `minLength` and `maxLength` were listed at the same time with the value specified for `len`.

**Serialization**

The `minLength` or `length` attribute defines the resulting XML value as representing at least the number of characters or bytes defined in `len`. If a passed value contains fewer characters, or bytes, it is filled on the right with blanks or *0x00* until it is of the specified length and an XML value is created. The `maxLength` or `length` attribute defines the maximum number of characters or bytes that can be passed. If the XML value to be serialized contains more characters or bytes than specified by `len`, the exception `CX_ST_CONSTRAINT_ERROR` is raised, unless only trailing blanks or zero bytes in a serialization of a data object with type `c` or `x` are affected.

**Deserialization**

The `minLength` attribute is ignored by deserialization. The `maxLength` or `length` attribute defines the maximum number of characters or bytes expected in the XML value. If the XML value to be deserialized contains more characters or bytes than specified by `len`, the exception `CX_ST_CONSTRAINT_ERROR` is raised, unless only trailing blanks or zero bytes in a deserialization to a data object with type `c` or `x` are affected.

## Hint

Exception `CX_ST_CONSTRAINT_ERROR` cannot be caught directly during the call of `CALL TRANSFORMATION`, instead it is wrapped in `CX_ST_SERIALIZATION_ERROR` or `CX_ST_DESERIALIZATION_ERROR`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following transformation `DEMO_ST_SPECIFIED_LENGTH` performs serializations and deserializations with differing lengths:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <tt:serialize> 
      <Text> 
        <tt:value length="8" ref="ROOT"/> 
      </Text> 
    </tt:serialize> 
    <tt:deserialize> 
      <Text> 
        <tt:value length="4" ref="ROOT"/> 
      </Text> 
    </tt:deserialize> 
  </tt:template> 
</tt:transform>
```

The following ABAP program can call the transformation:

``` abap
DATA: text        TYPE string VALUE `1234`, 
      xml_xstring TYPE string, 
      exc_trafo   TYPE REF TO cx_transformation_error, 
      exc_prev    TYPE REF TO cx_root. 
 
CALL TRANSFORMATION demo_st_specified_length 
                    SOURCE root = text 
                    RESULT XML xml_xstring. 
 
cl_abap_browser=>show_xml( xml_string = xml_xstring ). 
 
TRY. 
    CALL TRANSFORMATION demo_st_specified_length 
                        SOURCE XML xml_xstring 
                        RESULT root = text. 
 
  CATCH cx_st_deserialization_error INTO exc_trafo. 
    ... 
    IF exc_trafo->previous IS NOT INITIAL. 
      exc_prev = exc_trafo->previous. 
      ... 
    ENDIF. 
ENDTRY.
```

The result of the transformation is:

`<Text>1234 </Text>`

Since more characters are passed by the deserialization than expected, the exception `CX_ST_CONSTRAINT_ERROR` is raised, which is wrapped in the exception `CX_ST_DESERIALIZATION_ERROR`.
