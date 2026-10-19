---
title: "asXML - Mapping of Enumerated Types"
source_file: abenabap_xslt_asxml_enum.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of Enumerated Types

The asXML representation of [enumerated types](../../abap-glossary/abenenum_type_glosry.md) is used in XSL transformations and in Simple Transformations. In both cases, the elementary values with enumerated types or the corresponding components of complex structures are converted in accordance with this mapping.

- When an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) is serialized, it is [converted](../abap-processing-internal-data/abenconversion_enumerated.md) to `string` and the result is represented in the corresponding [asXML format](abenabap_xslt_asxml_elementary.md). The XML representation is the name of the associated [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) or the component of the [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) with a maximum of 30 characters.

- When the [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md) is deserialized, the XML representation must correspond to the name of an [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md) of the enumerated type in uppercase letters. The enumerated variable is then assigned the enumerated value in the [base type](../../abap-glossary/abenbase_type_glosry.md). If the XML representation does not correspond to a name, this results in the exception `CX_SY_CONVERSION_NO_ENUM_VALUE`, which is usually wrapped in `CX_TRANSFORMATION_ERROR`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows the serialization of an enumerated variable `planet` to XML. Then, the name of the value *VENUS* is replaced by `JUPITER` and the result is deserialized to `planet`. `planet` then contains the value 4. A deserialization of the XML value *earth*, on the other hand, fails, because the name must be specified in uppercase letters.

``` abap
TYPES: 
  BEGIN OF ENUM planet, 
    mercury, 
    venus, 
    earth, 
    mars, 
    jupiter, 
    saturn, 
    uranus, 
    neptune, 
  END OF ENUM planet. 
 
DATA planet TYPE planet VALUE venus. 
 
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(xml) = ``. 
CALL TRANSFORMATION id SOURCE planet = planet 
                       RESULT XML xml. 
out->write_xml( xml ). 
 
REPLACE `VENUS` IN xml WITH `JUPITER` RESPECTING CASE. 
TRY. 
    CALL TRANSFORMATION id SOURCE XML xml 
                           RESULT planet = planet. 
    out->write( planet ). 
  CATCH cx_transformation_error INTO DATA(exc). 
    out->write( exc->previous->get_text( ) ). 
ENDTRY. 
 
REPLACE `JUPITER` IN xml WITH `earth` RESPECTING CASE. 
TRY. 
    CALL TRANSFORMATION id SOURCE XML xml 
                           RESULT planet = planet. 
    out->write( planet ). 
  CATCH cx_transformation_error INTO exc. 
    out->write( exc->previous->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```
