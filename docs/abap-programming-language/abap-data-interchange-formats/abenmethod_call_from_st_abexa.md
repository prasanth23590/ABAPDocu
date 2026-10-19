---
title: "ST - Method Call"
source_file: abenmethod_call_from_st_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Method Call

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the call of a static method from a Simple Transformation.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Method Call from Simple Transformation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_call_from_st DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  FINAL 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    TYPES: 
      t_spfli_tab TYPE SORTED TABLE OF spfli 
        WITH UNIQUE KEY carrid connid. 
    CLASS-DATA flight_tab TYPE t_spfli_tab . 
    METHODS constructor . 
    CLASS-METHODS get_flights 
      IMPORTING 
        !carrid TYPE spfli-carrid . 
 
  PRIVATE SECTION. 
    CLASS-DATA spfli_tab TYPE t_spfli_tab . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_call_from_st IMPLEMENTATION. 
  METHOD main. 
    DATA scarr_tab TYPE SORTED TABLE OF scarr 
                   WITH UNIQUE KEY carrid. 
 
    SELECT * 
           FROM scarr 
           INTO TABLE @scarr_tab. 
    IF sy-subrc <> 0. 
      RETURN. 
    ENDIF. 
    TRY. 
        CALL TRANSFORMATION demo_st_with_method_call 
          SOURCE scarr_tab = scarr_tab 
                 spfli_tab = spfli_tab 
          RESULT XML DATA(xml). 
        out->write_xml( xml ). 
      CATCH cx_st_call_method_error INTO DATA(exc). 
        out->write_text( exc->get_text( ) ). 
        RETURN. 
    ENDTRY. 
  ENDMETHOD. 
  METHOD get_flights. 
    flight_tab = spfli_tab. 
    DELETE flight_tab WHERE carrid <> carrid. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    SELECT * 
           FROM spfli 
           INTO TABLE @spfli_tab. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `MAIN` of the global class `CL_DEMO_CALL_FROM_ST` calls an ST program `DEMO_ST_WITH_METHOD_CALL` and passes the static attributes `SCARR_TAB` and `SPFLI_TAB` of this class to the identically named data roots of the transformation. The table `SCARR_TAB` is filled and `SPFLI_TAB` is passed empty. The ST program is as follows:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="SCARR_TAB"/> 
  <tt:root name="SPFLI_TAB"/> 
  <tt:variable name="carrid"/> 
  <tt:template> 
    <FlightList> 
      <tt:loop ref=".SCARR_TAB"> 
        <Flights> 
          <tt:attribute name="Carrier" value-ref="CARRNAME"/> 
          <tt:assign ref="carrid" to-var="carrid"/> 
          <tt:call-method class="CL_DEMO_CALL_FROM_ST" 
                          s-name="GET_FLIGHTS"> 
            <tt:with-parameter name="CARRID" var="carrid"/> 
          </tt:call-method> 
          <tt:loop ref=".SPFLI_TAB"> 
            <Connection> 
              <tt:attribute name="ID" value-ref="CONNID"/> 
              <From> 
                <tt:value ref="CITYFROM"/> 
              </From> 
              <To> 
                <tt:value ref="CITYTO"/> 
              </To> 
            </Connection> 
          </tt:loop> 
        </Flights> 
      </tt:loop> 
    </FlightList> 
  </tt:template> 
</tt:transform>
```

In a serialization in a [`tt:loop` loop](abenst_tt_loop.md), the data root `SCARR_TAB` is used to call the static method `GET_FLIGHTS` of the global class `CL_DEMO_CALL_FROM_ST`. This passes the component `carrid` of the internal table `scarr_tab` to the input parameter of the method. In the method, `spfli_tab` is filled in a different way in each loop pass in accordance with the passed parameters.
