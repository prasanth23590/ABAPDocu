---
title: "ST - xsd-type, Validation"
source_file: abenst_xsd_type.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - xsd-type, Validation

## Syntax

``` abap
... xsd-type="type" 
   [xsd-maxInclusive="max"] 
   [xsd-maxExclusive ="max"] 
   [xsd-minInclusive="min"] 
   [xsd-minExclusive ="min"] 
   [xsd-totalDigits="dgts"] 
   [xsd-fractionDigits="dgts"] ...  
```

## Description

These attributes can be used with [`tt:value`](abenst_tt_value_elementary.md), [`tt:write`](abenst_tt_write.md), and [`tt:read`](abenst_tt_read.md) to validate the value.

The attribute `xsd-type` can be used to specify an XML schema data type `type`. The serialized or deserialized value must be in the value range of this type. If not, an exception of the class `CX_ST_VALIDATION_ERROR` is raised, which is not caught directly but by using `CX_ST_SERIALIZATION_ERROR`, `CX_ST_DESERIALIZATION_ERROR`, and its superclasses. The following subtypes of `xsd:decimal` can be specified for `type`: `xsd:byte, xsd:decimal, xsd:int, xsd:integer, xsd:long, xsd:negativeInteger, xsd:nonNegativeInteger, xsd:nonPosistiveInteger, xsd:positiveInteger, xsd:short, xsd:unsignedByte, xsd:unsignedInt, xsd:unsignedLong`, and `xsd:unsignedShort`.

Together with the `xsd-type` attribute, the following restrictions (constraining facets) allowed by the XML schema can be specified as additional attributes:

- `xsd-maxInclusive` and `xsd-maxExclusive`: The value must be less than or equal to or less than `max`. `max` must be in the value range of the XML schema data type and cannot be less than a simultaneous lower limit `min`.

- `xsd-minInclusive` and `xsd-minExclusive`: The value must be greater than or equal to or greater than `min`. `min` must be in the value range of the XML schema data type and cannot be greater than a simultaneous upper limit `max`.

- `xsd-totalDigits` and `fractionDigits`: The value can have a maximum of `dgts` digits or decimal places. `dgts` must fit the other restrictions.

After the transformation from ABAP, serializations perform the validation to XML. Before the transformation from XML, deserializations perform the validation to ABAP. In both cases, the data type of the bound ABAP data object is ignored.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serialization of ABAP data with validation in the simple transformation `DEMO_ST_XSD_TYPE`.

``` abap
<?sap.transform simple?> 
<tt:transform 
   xmlns:tt="http://www.sap.com/transformation-templates"> 
   <tt:root name="NUM"/> 
   <tt:template> 
    <Number> 
       <tt:value ref="NUM" 
           xsd-type="short" xsd-minInclusive="30000"/> 
     </Number> 
  </tt:template> 
</tt:transform>
```

The transformation only accepts numbers between 30000 and 32767. The following ABAP program calls the transformation and catches the validation exceptions.

``` abap
DATA int TYPE i. 
DATA xml_string TYPE string. 
TRY. 
    CALL TRANSFORMATION demo_st_xsd_type 
          SOURCE num = int 
          RESULT XML xml_string. 
    cl_demo_output=>display( 'OK' ). 
  CATCH cx_st_error. 
    cl_demo_output=>display( 'Not OK' ). 
ENDTRY.
```
