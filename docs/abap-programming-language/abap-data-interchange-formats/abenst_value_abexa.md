---
title: "ST - tt:value"
source_file: abenst_value_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:value

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serializes and deserializes elementary data objects

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
CLASS cl_demo_st_value DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_value IMPLEMENTATION. 
  METHOD main. 
    DATA: dat TYPE d, 
          tim TYPE t, 
          ts  TYPE utclong, 
          tsp TYPE xsddatetime_z. 
 
    dat = cl_demo_date_time=>get_user_date( ). 
    tim = cl_demo_date_time=>get_user_time( ). 
    CONVERT DATE dat 
            TIME tim 
            TIME ZONE `` 
            INTO UTCLONG ts. 
    tsp = cl_abap_tstmp=>utclong2tstmp_short( ts ). 
 
    CALL TRANSFORMATION demo_st_value 
      SOURCE date      = dat 
             time      = tim 
             datetime1 = ts 
             datetime2 = tsp 
      RESULT XML FINAL(xml). 
 
    out->write_xml( xml ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The called transformation `DEMO_ST_VALUE` shows the mapping of elementary ABAP data types for date, time, and UTC time stamp to XML and back.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="DATE"/> 
  <tt:root name="TIME"/> 
  <tt:root name="DATETIME1"/> 
  <tt:root name="DATETIME2"/> 
  <tt:template> 
    <Date_and_Time> 
      <Date> 
        <tt:value ref="DATE"/> 
      </Date> 
      <Time> 
        <tt:value ref="TIME"/> 
      </Time> 
      <DateTime1> 
        <tt:value ref="DATETIME1"/> 
      </DateTime1> 
      <DateTime2> 
        <tt:value ref="DATETIME2"/> 
      </DateTime2> 
    </Date_and_Time> 
  </tt:template> 
</tt:transform>
```

It should be noted that `tsp` is defined with the special type `XSDDATETIME_Z` from the ABAP Dictionary. This type ensures that a special mapping is used for UTC time stamps in packed numbers. This happens by default for the built-in time stamp type `utclong`.

The transformation is [symmetrical](abenst_symmetry.md).
