---
title: "ST - Formatting Options"
source_file: abenst_format_option_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects > ST - option, Mapping Rules > ST - option, Mapping Rules for Elementary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Formatting Options

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how ABAP types are mapped using formatting options.

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
CLASS cl_demo_st_format_option DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS call_transformation 
      CHANGING writer TYPE REF TO cl_sxml_string_writer. 
    DATA: 
      boolean        TYPE abap_boolean, 
      hex            TYPE xstring VALUE '0123456789ABCDEF', 
      utclong        TYPE utclong, 
      datetime       TYPE timestamp, 
      datetime_long  TYPE timestampl, 
      datetimeoffset TYPE c LENGTH 18, 
      datetimelocal  TYPE c LENGTH 14, 
      guid_16        TYPE x LENGTH 16, 
      guid_32        TYPE c LENGTH 32, 
      guid_22        TYPE c LENGTH 22, 
      qname1         TYPE string VALUE `{uri_1}name1`, 
      qname2         TYPE string VALUE `{uri_2}name2`, 
      uri            TYPE string VALUE `:;<=>?[\]^_``{|}~`, 
      uri1           TYPE string VALUE `Rock'n'Roll & Blues`, 
      language       TYPE sy-langu VALUE 'E', 
      currcode       TYPE I_Currency-Currency VALUE 'EUR', 
      unitcode       TYPE I_UnitOfMeasure-UnitOfMeasure VALUE 'TON', 
      number         TYPE p DECIMALS 3 VALUE '123.000', 
      numtext        TYPE n LENGTH 10 VALUE '0000123456'. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_format_option IMPLEMENTATION. 
  METHOD main. 
 
    utclong        = utclong_current( ). 
    datetime       = cl_abap_tstmp=>utclong2tstmp_short( utclong ). 
    datetime_long  = cl_abap_tstmp=>utclong2tstmp( utclong ). 
    datetimeoffset = |{ datetime WIDTH = 14 }+180|. 
    datetimelocal  = datetime. 
 
    FINAL(system_uuid) = cl_uuid_factory=>create_system_uuid( ). 
    TRY. 
        guid_16 = system_uuid->create_uuid_x16( ). 
        guid_32 = system_uuid->create_uuid_c32( ). 
        guid_22 = system_uuid->create_uuid_c22( ). 
      CATCH cx_uuid_error. 
        CLEAR guid_16. 
        CLEAR guid_32. 
        CLEAR guid_22. 
    ENDTRY. 
 
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
    FINAL(user_time) = cl_demo_date_time=>get_user_time( ). 
    FINAL(user_date) = cl_demo_date_time=>get_user_date( ). 
    CALL TRANSFORMATION demo_st_format_option 
      SOURCE boolean        = boolean 
             hex            = hex 
             time           = user_time 
             date           = user_date 
             utclong        = utclong 
             datetime       = datetime 
             datetime_long  = datetime_long 
             datetimeoffset = datetimeoffset 
             datetimelocal  = datetimelocal 
             guid_16        = guid_16 
             guid_32        = guid_32 
             guid_22        = guid_22 
             qname1         = qname1 
             qname2         = qname2 
             uri            = uri 
             urifull        = uri 
             uri1           = uri1 
             language       = language 
             currcode       = currcode 
             unitcode       = unitcode 
             number         = number 
             numtext = numtext 
      RESULT XML writer. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example passes various types of ABAP data to the transformation `DEMO_ST_FORMAT_OPTION` and provides the result for XML and [JSON](abenabap_json.md). The transformation applies those [formatting options](abenst_option_format.md) to the ABAP data that match its data type:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="BOOLEAN"/> 
  <tt:root name="HEX"/> 
  <tt:root name="TIME"/> 
  <tt:root name="DATE"/> 
  <tt:root name="DATETIME"/> 
  <tt:root name="DATETIME_LONG"/> 
  <tt:root name="UTCLONG"/> 
  <tt:root name="DATETIMEOFFSET"/> 
  <tt:root name="DATETIMELOCAL"/> 
  <tt:root name="GUID_16"/> 
  <tt:root name="GUID_32"/> 
  <tt:root name="GUID_22"/> 
  <tt:root name="QNAME1"/> 
  <tt:root name="QNAME2"/> 
  <tt:root name="URI"/> 
  <tt:root name="URIFULL"/> 
  <tt:root name="URI1"/> 
  <tt:root name="LANGUAGE"/> 
  <tt:root name="CURRCODE"/> 
  <tt:root name="UNITCODE"/> 
  <tt:root name="NUMBER"/> 
  <tt:root name="NUMTEXT"/> 
  <tt:template> 
    <array> 
      <object> 
        <bool name="boolean"> 
          <tt:value option="format(boolean)" ref="BOOLEAN"/> 
        </bool> 
        <str name="hex"> 
          <tt:value option="format(hex)" ref="HEX"/> 
        </str> 
        <str name="dateTime for UTCLONG"> 
          <tt:value option="format(dateTime)" ref="UTCLONG"/> 
        </str> 
        <str name="dateTime for TIMESTAMP"> 
          <tt:value option="format(dateTime)" ref="DATETIME"/> 
        </str> 
        <str name="dateTime for TIMESTAMPL"> 
          <tt:value option="format(dateTime)" ref="DATETIME_LONG"/> 
        </str> 
        <str name="dateTimeOffset for c, LENGTH 18"> 
          <tt:value option="format(dateTimeOffset)" ref="DATETIMEOFFSET"/> 
        </str> 
        <str name="dateTimeOffset for UTCLONG"> 
          <tt:value option="format(dateTimeOffset)" ref="UTCLONG"/> 
        </str> 
        <str name="dateTimeOffset for TIMESTAMP"> 
          <tt:value option="format(dateTimeOffset)" ref="DATETIME"/> 
        </str> 
        <str name="dateTimeOffset for TIMESTAMPL"> 
          <tt:value option="format(dateTimeOffset)" ref="DATETIME_LONG"/> 
        </str> 
        <str name="dateTimeLocal for c, LENGTH 14"> 
          <tt:value option="format(dateTimeLocal)" ref="DATETIMELOCAL"/> 
        </str> 
        <str name="dateTimeLocal for UTCLONG"> 
          <tt:value option="format(dateTimeLocal)" ref="UTCLONG"/> 
        </str> 
        <str name="dateTimeLocal for TIMESTAMP"> 
          <tt:value option="format(dateTimeLocal)" ref="DATETIME"/> 
        </str> 
        <str name="dateTimeLocal for TIMESTAMPL"> 
          <tt:value option="format(dateTimeLocal)" ref="DATETIME_LONG"/> 
        </str> 
        <str name="ticks for d"> 
          <tt:value option="format(ticks)" ref="DATE"/> 
        </str> 
        <str name="ticks for UTCLONG"> 
          <tt:value option="format(ticks)" ref="UTCLONG"/> 
        </str> 
        <str name="ticks for TIMESTAMP"> 
          <tt:value option="format(ticks)" ref="DATETIME"/> 
        </str> 
        <str name="ticks for TIMESTAMPL"> 
          <tt:value option="format(ticks)" ref="DATETIME_LONG"/> 
        </str> 
        <str name="ticksOffset for c, LENGTH 18"> 
          <tt:value option="format(ticksOffset)" ref="DATETIMEOFFSET"/> 
        </str> 
        <str name="ticksOffset for UTCLONG"> 
          <tt:value option="format(ticksOffset)" ref="UTCLONG"/> 
        </str> 
        <str name="ticksOffset for TIMESTAMP"> 
          <tt:value option="format(ticksOffset)" ref="DATETIME"/> 
        </str> 
        <str name="ticksOffset for TIMESTAMPL"> 
          <tt:value option="format(ticksOffset)" ref="DATETIME_LONG"/> 
        </str> 
        <str name="duration"> 
          <tt:value option="format(duration)" ref="TIME"/> 
        </str> 
        <str name="guid for X, LENGTH 16"> 
          <tt:value option="format(guid)" ref="GUID_16"/> 
        </str> 
        <str name="guid for C, LENGTH 32"> 
          <tt:value option="format(guid)" ref="GUID_32"/> 
        </str> 
        <str name="guid for C, LENGTH 22"> 
          <tt:value option="format(guid)" ref="GUID_22"/> 
        </str> 
        <str name="qName, first"> 
          <tt:value option="format(qName)" ref="QNAME1"/> 
        </str> 
        <str name="qName, second"> 
          <tt:value option="format(qName)" ref="QNAME2"/> 
        </str> 
        <str name="uri"> 
          <tt:value option="format(uri)" ref="URI"/> 
        </str> 
        <str name="uriFull"> 
          <tt:value option="format(uriFull)" ref="URIFULL"/> 
        </str> 
        <str name="uri1 for string"> 
          <tt:value option="format(uri1)" ref="URI1"/> 
        </str> 
        <str name="uri1 for xstring"> 
          <tt:value option="format(uri1)" ref="HEX"/> 
        </str> 
        <str name="uri1 for t"> 
          <tt:value option="format(uri1)" ref="TIME"/> 
        </str> 
        <str name="uri1 for UTCLONG"> 
          <tt:value option="format(uri1)" ref="UTCLONG"/> 
        </str> 
        <str name="uri1 for TIMESTAMP"> 
          <tt:value option="format(uri1)" ref="DATETIME"/> 
        </str> 
        <str name="uri1 for TIMESTAMPL"> 
          <tt:value option="format(uri1)" ref="DATETIME_LONG"/> 
        </str> 
        <str name="uri2 for guid_16"> 
          <tt:value option="format(uri2)" ref="GUID_16"/> 
        </str> 
        <str name="uri2 for guid_32"> 
          <tt:value option="format(uri2)" ref="GUID_32"/> 
        </str> 
        <str name="uri2 for d"> 
          <tt:value option="format(uri2)" ref="DATE"/> 
        </str> 
        <str name="uri2 for UTCLONG"> 
          <tt:value option="format(uri2)" ref="UTCLONG"/> 
        </str> 
        <str name="uri2 for TIMESTAMP"> 
          <tt:value option="format(uri2)" ref="DATETIME"/> 
        </str> 
        <str name="uri2 for TIMESTAMPL"> 
          <tt:value option="format(uri2)" ref="DATETIME_LONG"/> 
        </str> 
        <str name="language"> 
          <tt:value option="format(language),noError" ref="LANGUAGE"/> 
        </str> 
        <str name="currCode"> 
          <tt:value option="format(currCode),noError" ref="CURRCODE"/> 
        </str> 
        <str name="unitCode"> 
          <tt:value option="format(unitCode),noError" ref="UNITCODE"/> 
        </str> 
        <str name="currency=CURRCODE"> 
          <tt:value option="format(currency=CURRCODE)" ref="NUMBER"/> 
        </str> 
        <str name="unit=UNITCODE"> 
          <tt:value option="format(unit=UNITCODE)" ref="NUMBER"/> 
        </str> 
        <str name="alpha"> 
          <tt:value option="format(alpha)" ref="NUMTEXT"/> 
        </str> 
      </object> 
    </array> 
  </tt:template> 
</tt:transform>
```

The transformation creates [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) to represent both XML and JSON. It should be noted that the formats `ticks` and `ticksOffset` only have a special meaning in JSON, where they create the JSON representation of UNIX time stamps for OData.
