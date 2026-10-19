---
title: "ST - Option for Regime"
source_file: abenst_regime_option_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects > ST - option, Mapping Rules > ST - option, Mapping Rules for Elementary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Option for Regime

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the representation of ABAP types when using regimes.

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
CLASS cl_demo_st_regime_option DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS call_transformation 
      CHANGING writer TYPE REF TO cl_sxml_string_writer. 
    DATA: 
      time    TYPE t, 
      boolean TYPE xsdboolean, 
      numtext TYPE n LENGTH 3. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_regime_option IMPLEMENTATION. 
  METHOD main. 
    time = cl_demo_date_time=>get_user_time( ). 
    boolean = abap_true. 
    numtext = '255'. 
 
    out->next_section( 'XML' ). 
    DATA(writer) = cl_sxml_string_writer=>create( 
            type = if_sxml=>co_xt_xml10 ). 
    call_transformation( CHANGING writer = writer ). 
    DATA(result) = writer->get_output( ). 
    out->write_xml( result 
       )->next_section( 'JSON' ). 
    writer = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    call_transformation( CHANGING writer = writer ). 
    result = writer->get_output( ). 
    out->write_json( result ). 
  ENDMETHOD. 
  METHOD call_transformation. 
    CALL TRANSFORMATION demo_st_regime_option 
      SOURCE time    = time 
             boolean = boolean 
             numtext = numtext 
    RESULT XML writer. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example passes various types of ABAP data to the transformation `DEMO_ST_REGIME_OPTION` and displays the result for XML and [JSON](abenabap_json.md). The transformation applies the option [`regime`](abenst_option_format.md) to the ABAP data:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="TIME"/> 
  <tt:root name="BOOLEAN"/> 
  <tt:root name="NUMTEXT"/> 
  <tt:template> 
    <array> 
      <object> 
        <str name="TIME"> 
          <tt:value ref="TIME"/> 
        </str> 
        <str name="regime(num) for TIME"> 
          <tt:value option="regime(num)" 
                    ref="TIME"/> 
        </str> 
        <str name="regime(num),decimals(2) for TIME"> 
          <tt:value option="regime(num),decimals(2)" 
                    ref="TIME"/> 
        </str> 
        <str name="BOOLEAN"> 
          <tt:value ref="BOOLEAN"/> 
        </str> 
        <str name="regime(char) for BOOLEAN"> 
          <tt:value option="regime(char)" 
                    ref="BOOLEAN"/> 
        </str> 
        <str name="regime(char),format(boolean) for BOOLEAN"> 
          <tt:value option="regime(char),format(boolean)" 
                    ref="BOOLEAN"/> 
        </str> 
        <str name="NUMTEXT"> 
          <tt:value ref="NUMTEXT"/> 
        </str> 
        <str name="regime(bin) for NUMTEXT"> 
          <tt:value option="regime(bin)" 
                    ref="NUMTEXT"/> 
        </str> 
        <str name="regime(bin),format(uri1) for NUMTEXT"> 
          <tt:value option="regime(bin),format(uri1)" 
                    ref="NUMTEXT"/> 
        </str> 
      </object> 
    </array> 
  </tt:template> 
</tt:transform>
```

The transformation creates [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) to represent both XML and JSON. The example shows the following:

- Source Field of Type `t`

  - Normal [asXML](abenabap_xslt_asxml_elementary.md) representation according to the XML schema type `xsd:time`.

  - Applying `regime(num)` gives the number of days since 01.01.0001.

  - Applying `regime(num),decimals(2)` appends two decimal places.

- Source field with reference to the special domain `XSDBOOLEAN`

  - Special representation of the value *X* in the XML schema type `xsd:boolean` as `true`.

  - Applying `regime(char)` removes the effect of the domain and `X` is represented according to the XML schema type `xsd:string`.

  - Applying `regime(char),format(boolean)` restores the representation `true`.

- Source field of type `n` with length 3

  - Normal [asXML](abenabap_xslt_asxml_elementary.md) representation according to the XML schema type `xsd:string (pattern [0-9]+)`.

  - Applying `regime(bin)` converts the number in the source field to its binary representation and represents it in the XML schema type `xsd:base64Binary`.

  - Applying `regime(bin),format(uri1)` represents the binary value hexadecimally and adds quotation marks and a prefix.
