---
title: "Serializing Data References"
source_file: abenserialize_dref_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types > asXML - Mapping of Reference Variables and Objects > asXML - Named Reference Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Serializing Data References

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates serializations of data references to [asXML](../../abap-glossary/abenasxml_glosry.md) and to [asJSON](../../abap-glossary/abenasjson_glosry.md).

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_serialize_dref DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_serialize_dref IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `Serialization of Data References` ). 
    DATA xml  TYPE xstring. 
    DATA writer TYPE REF TO cl_sxml_string_writer. 
 
    "Data reference with named type 
    out->begin_section( `Data Reference with Named Type` ). 
    TYPES: 
      BEGIN OF struc, 
        comp1 TYPE i, 
        comp2 TYPE i, 
      END OF struc. 
    DATA dref1 TYPE REF TO struc. 
    dref1 = NEW #( comp1 = 111 comp2 = 222 ). 
    out->begin_section( `asXML for Heap Reference` ). 
    CALL TRANSFORMATION id SOURCE dref = dref1 
                           RESULT XML xml. 
    out->write_xml( xml 
      )->next_section( `asJSON for Heap Reference` ). 
    writer = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE dref = dref1 
                           RESULT XML writer. 
    out->write_json( writer->get_output( ) 
      )->end_section( ). 
 
    "Data reference with technical type 
    out->next_section( `Data Reference with Technical Type` ). 
    DATA: 
      BEGIN OF struc, 
        comp1 TYPE i, 
        comp2 TYPE i, 
      END OF struc, 
      dref2 LIKE REF TO struc. 
    dref2 = NEW #( comp1 = 111 comp2 = 222 ). 
    out->begin_section( `asXML for Heap Reference` 
      )->begin_section( `Without Transformation Option` ). 
    TRY. 
        CALL TRANSFORMATION id SOURCE dref = dref2 
                               RESULT XML xml. 
        out->write_xml( xml ). 
      CATCH cx_xslt_serialization_error INTO FINAL(xml_err). 
        out->write( xml_err->previous->get_text( ) ). 
    ENDTRY. 
    out->next_section( `With Transformation Option` ). 
    CALL TRANSFORMATION id SOURCE dref = dref2 
                           RESULT XML xml 
                           OPTIONS technical_types = 'ignore'. 
    out->write_xml( xml 
      )->end_section( 
      )->next_section( `asJSON for Heap Reference` 
      )->begin_section( `Without Transformation Option` ). 
    TRY. 
        writer = cl_sxml_string_writer=>create( 
          type = if_sxml=>co_xt_json ). 
        CALL TRANSFORMATION id SOURCE dref = dref2 
                               RESULT XML writer. 
        out->write_json( writer->get_output( ) ). 
      CATCH cx_xslt_serialization_error INTO FINAL(json_err). 
        out->write( json_err->previous->get_text( ) ). 
    ENDTRY. 
    out->next_section( `With Transformation Option` ). 
    writer = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE dref = dref2 
                           RESULT XML writer 
                           OPTIONS technical_types = 'ignore'. 
    out->write_json( writer->get_output( ) 
      )->end_section( 
      )->end_section( ). 
 
    "Stack reference 
    out->next_section( `Stack Reference` ). 
    DATA dref3 TYPE REF TO i. 
    dref3 = REF #( 333 ). 
    out->begin_section( `asXML for Stack Reference` 
      )->begin_section( `Without Transformation Option` ). 
    CALL TRANSFORMATION id SOURCE dref = dref3 
                           RESULT XML xml. 
    out->write_xml( xml 
      )->next_section( `With Transformation Option` ). 
    CALL TRANSFORMATION id SOURCE dref = dref3 
                           RESULT XML xml 
                           OPTIONS data_refs = 'heap-or-create'. 
    out->write_xml( xml 
      )->end_section( 
      )->next_section( `asJSON for Stack Reference` 
      )->begin_section( `Without Transformation Option` ). 
    writer = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE dref = dref3 
                           RESULT XML writer. 
    out->write_json( writer->get_output( ) 
      )->next_section( `With Transformation Option` ). 
    writer = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE dref = dref3 
                           RESULT XML writer 
                           OPTIONS data_refs = 'heap-or-create'. 
    out->write_json( writer->get_output( ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates the serialization of data reference variables using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` to the canonical formats [asXML](../../abap-glossary/abenasxml_glosry.md) and [asJSON](../../abap-glossary/abenasjson_glosry.md).

- First a data reference is serialized that points to an anonymous data object in the heap and whose dynamic type `struc` was created in the same method using the `TYPES` statement. No problems should arise from this serialization.

- Next, however, a data reference variable is serialized that points to an anonymous data object in the heap whose dynamic type does not have a name. This is the technical type of a structure and reference to this type is made using `LIKE`. A data reference variable of this type cannot be serialized without taking further actions. This exception can be prevented using the transformation option [`technical_types`](abapcall_transformation_options.md), however the data reference variable is ignored.

- Finally, a data reference variable is serialized that points to a data object in the stack. The data reference variable is ignored by default, but can be serialized using the transformation option [`data_refs`](abapcall_transformation_options.md).
