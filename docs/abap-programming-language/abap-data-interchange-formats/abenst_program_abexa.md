---
title: "ST - Example of an ST Program"
source_file: abenst_program_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Structure of ST Programs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Example of an ST Program

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Symmetrical serialization and deserialization of a nested structure.

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
CLASS cl_demo_st_program DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_program IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `Serialization` ). 
    DATA source1(10) TYPE c VALUE 'Field1'. 
    DATA source2(10) TYPE c VALUE 'Field2'. 
    CALL TRANSFORMATION demo_st_program 
      SOURCE root1 = source1 
             root2 = source2 
      RESULT XML FINAL(xml). 
    out->write_xml( xml ). 
 
    out->next_section( `Deserialization` ). 
    DATA result1 LIKE source1. 
    DATA result2 LIKE source1. 
    CALL TRANSFORMATION demo_st_program 
      SOURCE XML xml 
      RESULT root1 = result1 
             root2 = result2. 
    out->write_data( result1 
      )->write_data( result2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The called transformation `DEMO_ST_PROGRAM` shows the principal structure of an ST program:

``` abap
<?sap.transform simple?> 
<tt:transform template="tmpl1" 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:template name="tmpl1"> 
    <X0> 
      <X1> 
        <tt:value ref="ROOT1" /> 
      </X1> 
      <X2> 
        <tt:value ref="ROOT2" /> 
      </X2> 
    </X0> 
  </tt:template> 
</tt:transform>
```

The only template `tmpl1` is defined as the [main template](abenst_tt_template_main.md). Two [data roots](abenst_tt_root.md), `ROOT1` and `ROOT2`, are declared. The template contains two subelements, `X1` and `X2` of an element `X0`, which are given the values of the data roots in serializations or whose values are given to the data roots in deserializations using the statement [`tt:value`](abenst_tt_value_elementary.md). After the deserialization, `result1` and `result2` have the same content as `source1` and `source2`.
