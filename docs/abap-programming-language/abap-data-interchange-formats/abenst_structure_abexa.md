---
title: "ST - Structures"
source_file: abenst_structure_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the symmetrical serialization and deserialization of a nested structure.

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
CLASS cl_demo_st_structure DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_structure IMPLEMENTATION. 
  METHOD main. 
    DATA: BEGIN OF struc1, 
            col1 TYPE c LENGTH 10 VALUE 'ABCDEFGHIJ', 
            col2 TYPE i VALUE 111, 
            BEGIN OF struc2, 
              col1 TYPE d VALUE '20040126', 
              col2 TYPE t VALUE '084000', 
            END OF struc2, 
          END OF struc1, 
          result LIKE struc1. 
    TRY. 
        "Serialization 
        CALL TRANSFORMATION demo_st_structure 
          SOURCE para = struc1 
          RESULT XML DATA(xml). 
        out->write_xml( xml ). 
        "Deserialization 
        CALL TRANSFORMATION demo_st_structure 
          SOURCE XML xml 
          RESULT para = result. 
        IF result = struc1. 
          out->write_text( 'Symmetric transformation!' ). 
        ENDIF. 
      CATCH cx_st_error. 
        out->write_text( 'Error in Simple Transformation' ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the ABAP class, a nested structure `struc1` is serialized to `xml_string` using the Simple Transformation `DEMO_ST_STRUCTURE` and deserialized using the same transformation.

The Simple Transformation `DEMO_ST_STRUCTURE` has the following form:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates" 
              template="temp" version="0.1"> 
  <tt:root name="PARA"/> 
  <tt:template name="temp"> 
    <X> 
      <X1> 
        <tt:value ref="PARA.COL1"/> 
      </X1> 
      <X2> 
        <tt:value ref="PARA.COL2"/> 
      </X2> 
      <X2> 
        <tt:copy ref="PARA.STRUC2"/> 
      </X2> 
    </X> 
  </tt:template> 
</tt:transform>
```

The transformation consists of a template `temp` that defines the structure of the XML data and establishes relationships between value nodes and components of the structure. The ST statements [`tt:value`](abenst_tt_value_elementary.md) and [`tt:copy`](abenst_tt_copy.md) are used to serialize and deserialize the structure components. The reverse transformation creates the same content in the structure `result` as in `struc1`.
