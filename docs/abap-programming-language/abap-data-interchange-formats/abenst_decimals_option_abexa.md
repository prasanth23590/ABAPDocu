---
title: "ST - Option for Decimal Places"
source_file: abenst_decimals_option_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects > ST - option, Mapping Rules > ST - option, Mapping Rules for Elementary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Option for Decimal Places

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the representation of numeric ABAP types and the time stamp type `utclong` with specifications for decimal places.

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
CLASS cl_demo_st_decimals_option DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS call_transformation 
      CHANGING writer TYPE REF TO cl_sxml_string_writer. 
    DATA: 
      integer   TYPE i            VALUE 1234, 
      pack      TYPE p DECIMALS 4 VALUE '1234.5678', 
      decf      TYPE decfloat34   VALUE '1234.5678', 
      binf      TYPE f            VALUE '1234.5678', 
      utclong   TYPE utclong, 
      timestmpl TYPE timestampl, 
      datetimel TYPE xsddatetime_long_z. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_decimals_option IMPLEMENTATION. 
  METHOD main. 
    utclong = utclong_current( ). 
    timestmpl = cl_abap_tstmp=>utclong2tstmp( utclong ). 
    datetimel = timestmpl. 
 
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
    CALL TRANSFORMATION demo_st_decimals_option 
      SOURCE integer      = integer 
             pack         = pack 
             decf         = decf 
             binf         = binf 
             utclong      = utclong 
             timestmpl    = timestmpl 
             datetimel    = datetimel 
      RESULT XML writer. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example passes various types of numeric ABAP data including an UTC time stamp to the transformation `DEMO_ST_DECIMALS_OPTION` and displays the result for XML and [JSON](abenabap_json.md). The transformation applies the option [`decimals`](abenst_option_format.md) to the ABAP data:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="INTEGER"/> 
  <tt:root name="PACK"/> 
  <tt:root name="DECF"/> 
  <tt:root name="BINF"/> 
  <tt:root name="UTCLONG"/> 
  <tt:root name="TIMESTMPL"/> 
  <tt:root name="DATETIMEL"/> 
  <tt:template> 
    <array> 
      <object> 
        <str name="decimals(2) for INTEGER"> 
          <tt:value option="decimals(2)" 
                    ref="INTEGER"/> 
        </str> 
        <str name="decimals(2) for PACK"> 
          <tt:value option="decimals(2)" 
                    ref="PACK"/> 
        </str> 
        <str name="decimals(2) for DECF"> 
          <tt:value option="decimals(2)" 
                    ref="DECF"/> 
        </str> 
        <str name="decimals(2) for BINF"> 
          <tt:value option="decimals(2)" 
                    ref="BINF"/> 
        </str> 
        <str name="decimals(2) for TIMESTMPL"> 
          <tt:value option="decimals(2)" 
                    ref="TIMESTMPL"/> 
        </str> 
        <str name="decimals(2) for DATETIMEL"> 
          <tt:value option="decimals(2)" 
                    ref="DATETIMEL"/> 
        </str> 
        <str name="decimals(-1) for INTEGER"> 
          <tt:value option="decimals(-1)" 
                    ref="INTEGER"/> 
        </str> 
        <str name="decimals(-1) for PACK"> 
          <tt:value option="decimals(-1)" 
                    ref="PACK"/> 
        </str> 
        <str name="decimals(-1) for DECF"> 
          <tt:value option="decimals(-1)" 
                    ref="DECF"/> 
        </str> 
        <str name="decimals(-1) for BINF"> 
          <tt:value option="decimals(-1)" 
                    ref="BINF"/> 
        </str> 
        <str name="decimals(0) for UTCLONG"> 
          <tt:value option="decimals(0)" 
                    ref="UTCLONG"/> 
        </str> 
        <str name="decimals(3) for UTCLONG"> 
          <tt:value option="decimals(3)" 
                    ref="UTCLONG"/> 
        </str> 
        <str name="format(uri1),decimals(3) for UTCLONG"> 
          <tt:value option="format(uri1),decimals(3)" 
                    ref="UTCLONG"/> 
        </str> 
        <str name="decimals(-6) for TIMESTMPL"> 
          <tt:value option="decimals(-6)" 
                    ref="TIMESTMPL"/> 
        </str> 
        <str name="decimals(3) for TIMESTMPL"> 
          <tt:value option="decimals(3)" 
                    ref="TIMESTMPL"/> 
        </str> 
        <str name="decimals(3) for DATETIMEL"> 
          <tt:value option="decimals(3)" 
                    ref="DATETIMEL"/> 
        </str> 
        <str name="format(dateTime),decimals(3) for TIMESTMPL"> 
          <tt:value option="format(dateTime),decimals(3)" 
                    ref="TIMESTMPL"/> 
        </str> 
        <str name="format(ticks),decimals(3) for TIMESTMPL"> 
          <tt:value option="format(ticks),decimals(3)" 
                    ref="TIMESTMPL"/> 
        </str> 
        <str name="format(uri1),decimals(3) for TIMESTMPL"> 
          <tt:value option="format(uri1),decimals(3)" 
                    ref="TIMESTMPL"/> 
        </str> 
      </object> 
    </array> 
  </tt:template> 
</tt:transform>
```

The transformation creates [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) to represent both XML and JSON. The UTC time stamp in the packed number `datetimel` is typed with the [special domain](abenabap_xslt_asxml_schema.md) `XSDDATETIME_LONG_Z`. This time stamp is still handled as such after the handling by `decimals`. For the number `timestmpl` of type `p`, the corresponding effect is obtained by using the additional time stamp formats specified with `format`. Time stamps in the time stamp fields of the type `utclong` are handled as such by default.
