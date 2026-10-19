---
title: "ST - Internal Tables"
source_file: abenst_table_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the serializing of an internal table.

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
CLASS cl_demo_st_table DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_table IMPLEMENTATION. 
  METHOD main. 
    DATA: BEGIN OF carrier_wa, 
            carrid   TYPE scarr-carrid, 
            carrname TYPE scarr-carrname, 
            url      TYPE scarr-url, 
          END OF carrier_wa, 
          carrier_tab LIKE TABLE OF carrier_wa, 
          xml         TYPE xstring, 
          html        TYPE string. 
 
    SELECT * 
           FROM scarr 
           INTO CORRESPONDING FIELDS OF TABLE @carrier_tab. 
 
    CALL TRANSFORMATION demo_st_table 
                        SOURCE carriers = carrier_tab 
                        RESULT XML xml. 
    out->write_xml( xml ). 
 
    CALL TRANSFORMATION demo_st_table 
                        SOURCE carriers = carrier_tab 
                        RESULT XML html 
                        OPTIONS xml_header = 'NO'. 
    out->write_html( html ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An internal table `carrier_tab` is filled with data from the database table `SCARR` and is transformed to XML using the Simple Transformation `DEMO_ST_TABLE`. The ST program is as follows:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="CARRIERS"/> 
  <tt:template> 
    <html> 
      <body> 
        <h2>Carriers:</h2> 
        <table border="2"> 
          <tr> 
            <td><b>Id</b></td> 
            <td><b>Name</b></td> 
            <td><b>Homepage</b></td> 
          </tr> 
          <tt:loop ref=".CARRIERS"> 
            <tr><td> 
                <tt:value ref="$ref.carrid"/> 
              </td> 
              <td> 
                <tt:value ref="$ref.carrname"/> 
              </td> 
              <td> 
               <a><tt:attribute name="href" value-ref="$ref.url" /> 
                 <tt:value ref="$ref.url"/></a> 
              </td> 
            </tr> 
          </tt:loop> 
        </table> 
      </body> 
    </html> 
  </tt:template> 
</tt:transform>
```

The transformation uses the ST statement [`tt:loop`](abenst_tt_loop.md) to serialize the other internal tables line by line. HTML tags are inserted into the XML data as literal elements.

The result of the transformation is first shown as an XML file and then as formatted HTML data below.
