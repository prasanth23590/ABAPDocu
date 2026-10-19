---
title: "asXML - Mapping Additional XML Schema Data Types"
source_file: abenabap_xslt_asxml_schema.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping Additional XML Schema Data Types

In addition to the [XML schema data types](http://www.w3.org/TR/xmlschema-2/) required for [mapping elementary ABAP types](abenabap_xslt_asxml_elementary.md), there are additional XML schema data types for which there is no direct equivalent in the form of built-in ABAP types. To enable type-friendly deserialization of these external types to ABAP data objects, a special [DDIC domain](../../abap-glossary/abendomain_glosry.md) is implemented in the ABAP Dictionary for each required XML schema data type. The name of the domain starts with `XSD`. Any elementary ABAP data objects whose data type is defined using a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) that refers to such a DDIC domain are mapped to the associated XML schema data type, both when serialized and when deserialized. The required conversions are performed internally. This applies to both [XSL transformations](abenabap_xslt.md) and [simple transformations](abenabap_st.md).

The following table provides a summary of the XML schema data types supported by domains and additionally supported types (`UUID`, `currCode`, and `unitCode`).

<table>
<thead>
<tr class="header">
<th><strong>XML Schema Type</strong></th>
<th><strong>XML Representation</strong></th>
<th><strong>Domain</strong></th>
<th><strong>ABAP Representation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">xsd:boolean</code></td>
<td><em>true</em>, <em>false</em></td>
<td><code class="ph codeph">XSDBOOLEAN</code></td>
<td><em>X</em>, blank</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsd:date</code></td>
<td><em>2007-10-01</em></td>
<td><code class="ph codeph">XSDDATE_D</code></td>
<td><em>20071001</em></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsd:time</code></td>
<td><em>11:55:00</em></td>
<td><code class="ph codeph">XSDTIME_T</code></td>
<td><em>115500</em></td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsd:dateTime</code></td>
<td><em>2006-07-27T17:03:34Z</em></td>
<td><code class="ph codeph">XSDDATETIME_Z</code>, <code class="ph codeph">XSDDATETIME_LONG_Z</code>, <code class="ph codeph">XSDDATETIME_OFFSET</code>, <code class="ph codeph">XSDDATETIME_LOCAL</code>, <code class="ph codeph">XSDDATETIME_LOCAL_DT</code></td>
<td><em>20060727170334</em></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsd:QName</code></td>
<td><em>prefix:name</em></td>
<td><code class="ph codeph">XSDQNAME</code></td>
<td><em>{URI}name</em></td>
</tr>
<tr class="even">
<td><code class="ph codeph">UUID</code></td>
<td><em>00505691&amp;#x2011;3e2f&amp;#x2011;1ed5&amp;#x2011;b8ba&amp;#x2011;87b9ac1248c9</em></td>
<td><code class="ph codeph">XSDUUID_RAW</code>, <code class="ph codeph">XSDUUID_CHAR</code>, <code class="ph codeph">XSDUUID_BASE64</code></td>
<td><p><em>005056913E2F1ED5B8BA87B9AC1248C9</em>,</p>
<p><em>051MaJul7jMukeUvh198oG</em></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsd:language</code></td>
<td><em>EN</em>, <em>DE</em></td>
<td><code class="ph codeph">XSDLANGUAGE</code></td>
<td><em>D</em>, <em>E</em></td>
</tr>
<tr class="even">
<td><code class="ph codeph">currCode</code></td>
<td><em>EUR</em>, <em>USD</em></td>
<td><code class="ph codeph">XSDCURRCODE</code></td>
<td><em>EUR</em>, <em>USD</em></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">unitCode</code></td>
<td><em>KMT</em>, <em>SMI</em></td>
<td><code class="ph codeph">XSDUNITCODE</code></td>
<td><em>KM</em>, <em>MI</em></td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsd:base64Binary</code></td>
<td><em>AQEAACDmEAAA5WGh1jSnSEANcayL20ghQA==</em></td>
<td><code class="ph codeph">XSDGEO</code></td>
<td><em>0101000020E6100000E561A1D634A748400D71AC8BDB482140</em></td>
</tr>
</tbody>
</table>

The following sections describe the domains and their mappings in more detail.

- [boolean](abenabap_xslt_asxml_schema.md#boolean)

- [date](abenabap_xslt_asxml_schema.md#date)

- [dateTime](abenabap_xslt_asxml_schema.md#datetime)

- [QName](abenabap_xslt_asxml_schema.md#qname)

- [time](abenabap_xslt_asxml_schema.md#time)

- [UUID](abenabap_xslt_asxml_schema.md#uuid)

- [language](abenabap_xslt_asxml_schema.md#language)

- [currCode](abenabap_xslt_asxml_schema.md#currcode)

- [unitCode](abenabap_xslt_asxml_schema.md#unitcode)

- [base64Binary](abenabap_xslt_asxml_schema.md#base64binary)

The following applies to all domains:

- in deserializations of an empty XML element in an ABAP data object, which is typed with reference to this type of domain, the initial value of the associated elementary ABAP type is assigned as usual.

- The transformation option [`initial_components`](abapcall_transformation_options.md) for suppressing initial values in serializations has the same effect as for regular data types. This can lead to unexpected behavior in deserializations, if the transformation option [`clear`](abapcall_transformation_options.md) is not used with the value *all*.

## Hints

- By specifying [`format`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement [`tt:value`](abenst_tt_value_elementary.md), many of the formats here can also be applied to ABAP data objects that are not typed with a domain of this type.

- By specifying [`regime`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement [`tt:value`](abenst_tt_value_elementary.md), the effect of the domains shown here is disabled.

- Exceptions that occur when mapping the domains shown here can in some cases be suppressed by specifying [`noError`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement [`tt:value`](abenst_tt_value_elementary.md).

- Exceptions from mappings cannot be handled directly. Instead, the exception `CX_TRANSFORMATION_ERROR` (or one of its subclasses) from statement [`CALL TRANSFORMATION`](abapcall_transformation.md) can be handled. The attribute `PREVIOUS` then contains a reference to the original exception.

- Apart from `XSDQNAME`, all domains are also supported in [transformations for JSON](abenabap_json_trafos.md).

## boolean

The domain `XSDBOOLEAN` has the data type `CHAR` with length 1 and therefore supports the usual ABAP representation of a [truth value](../../abap-glossary/abentruth_value_glosry.md) using *X* for true and blank for false. These values are entered as [fixed values](../../abap-glossary/abenfixed_value_glosry.md) for the domain and are checked when an ABAP data object linked to this domain is serialized. The serialization creates the values *true* and *false* in XML. A deserialization also accepts the non-canonical XML values *1* and *0*. Any other values raise the exception `CX_SY_CONVERSION_NO_BOOLEAN`. An empty element creates the value blank in deserializations.

### Hints

- By specifying [`noError`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement [`tt:value`](abenst_tt_value_elementary.md), an exception for invalid ABAP values in serialization can be avoided. All values except blank are then interpreted as true.

- The transformation option [`initial_components`](abapcall_transformation_options.md) suppresses components of type `XSDBOOLEAN` in serializations, if the components contain the value blank for *false*. Therefore, this option should be used carefully.

- The return value of the Boolean function [`xsdbool`](../abap-program-flow-logic/abenboole_functions.md) has the type `XSDBOOLEAN`.

## date

The XML schema data type `date` for dates is supported by both the built-in ABAP type [`d`](abenabap_xslt_asxml_elementary.md) and the domain `XSDDATE_D`. This domain has the data type `DATS`. When data is serialized and deserialized, the validity of the date is also checked, which is not the case with the built-in ABAP type `d`. An empty element creates the value *00000000* in deserializations.

### Hint

By specifying [`noError`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement [`tt:value`](abenst_tt_value_elementary.md), an exception for an invalid date in serialization can be prevented again.

## dateTime

The XML schema data type `dateTime` supports the representation of dates and times in a field, based on ISO 8601. An XML value of this type is either in UTC format, contains a time zone, or represents a local time. Five domains are assigned to this schema data type:

- The domains `XSDDATETIME_Z` and `XSDDATETIME_LONG_Z` have the data types `DEC` with length 15 or 21. `XSDDATETIME_Z` has no decimal places and `XSDDATETIME_LONG_Z` has seven decimal places. These domains support the long and short form of [time stamps in packed numbers](../abap-processing-internal-data/abentime_stamps_packed.md), which is always interpreted as the current [UTC](../../abap-glossary/abenutc_glosry.md) reference time. The serialization generates values in the UTC format (`yyyy-mm-ddThh:mm:ss.fffffffZ`) in XML. Only significant decimal places are written to XML. A deserialization accepts XML values in UTC format (closed by `Z`) or with time zones (closed by `{+|-}hh:mm`). The time zones are converted to the associated UTC value. No precision may be lost in deserializations. This means that only XML values with a maximum of seven decimal places can be deserialized. An empty element creates the value 0 in deserializations.

- The domain `XSDDATETIME_OFFSET` has the data type `CHAR` with length 18. It allows mappings to XML values in which a time zone is specified (`yyyy-mm-ddThh:mm:ss{+|-}hh:mm`). The predefined format for an ABAP data object of type `XSDDATETIME_OFFSET` is `yyyymmddhhmmss{+|-}mmm`. In a deserialization, the time zone of the XML value specified in hours and minutes is converted to a three-digit number of minutes and vice versa in serializations. An empty element creates a string filled with blanks in deserializations.

- The domain `XSDDATETIME_LOCAL` has the data type `CHAR` with length 14. The domain `XSDDATETIME_LOCAL_DT` has the data type `NUMC` with length 14. They enable mappings to XML values that specify a local time (`yyyy-mm-ddThh:mm:ss`). This means that they do not exist in UTC format and no time zone is specified. The predefined format for an ABAP data object of type `XSDDATETIME_LOCAL` or `XSDDATETIME_LOCAL_DT` is `yyyymmddhhmmss`. The main differences between the two data types are their initial values. An empty element creates a string filled with blanks or zeros in deserializations.

Invalid values raise the exception `CX_SY_CONVERSION_NO_DATE_TIME`.

### Hint

[Time stamp fields with time stamp type](../abap-processing-internal-data/abenutclong.md) are mapped to the format `yyyy-mm-ddThh:mm:ss.fffffffZ` by default.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serialization and deserialization of a time stamp field of the type `utclong` and an UTC time stamp in a packed number of the type `XSDDATETIME_LONG_Z`. The generated XML is as follows:

``` abap
<asx:abap version="1.0" xmlns:asx="http://www.sap.com/abapxml"> 
 <asx:values> 
  <TS>2019-04-15T11:22:10.1230000Z</TS> 
  <TSP>2019-04-15T11:22:10.123Z</TSP> 
 </asx:values> 
</asx:abap>
```

The element `<TS>` and element `<TSP>` can be deserialized in both time stamp fields and in packed numbers of the type `XSDDATETIME_LONG_Z`.

``` abap
DATA(ts)  = 
  CONV utclong( '2019-04-15 11:22:10,123' ). 
DATA(tsp) = 
  CONV xsddatetime_long_z( cl_abap_tstmp=>utclong2tstmp( ts ) ). 
 
CALL TRANSFORMATION id 
     SOURCE ts  = ts 
            tsp = tsp 
     RESULT XML FINAL(xmlstr). 
 
CALL TRANSFORMATION id 
     SOURCE XML xmlstr 
     RESULT ts  = ts 
            tsp = ts. 
 
CALL TRANSFORMATION id 
     SOURCE XML xmlstr 
     RESULT ts  = tsp 
            tsp = tsp.
```

## QName

The domain `XSDQNAME` has the data type `STRING`. The XML schema data type `QName` represents qualified names. In XML, a qualified name can have a prefix that is separated by a colon. A prefix of this type must be linked with a URI in a namespace declaration of the current element or a higher-level element. In ABAP, a name of this type is represented as the content of a string in the form *{URI}name*.

When an ABAP object of the type `XSDQNAME` is serialized, the URI specified in curly brackets is used to create the associated prefix. If there is no namespace declaration for the URI in the right context, it is inserted in the current element, with the resulting namespaces being given the names *n0*, *n1*, ... If the URI is linked with the default namespace, no prefix is created. If no URI is specified in curly brackets, no prefix is created either. This latter case is possible only if the default namespace is not used simultaneously in the current element. Otherwise, the exception `CX_ST_INVALID_XML` is raised, which can occur only in Simple Transformations.

When a value with a prefix is deserialized to an ABAP data object of the type `XSDQNAME`, the URI is searched for in a linked namespace declaration. If no URI is found, the exception `CX_SY_CONVERSION_NO_QNAME` is raised. If a value without prefix is deserialized, the URI of the default namespace is used (if available) or only the name is placed in the string.

An initial data object of the type `XSDQNAME` creates an empty element when serialized and vice versa when deserialized. In both serializations and deserializations, the correctness of the specified name with respect to the valid naming conventions is checked. If violated, an exception of the class `CX_SY_CONVERSION_NO_QNAME` is raised.

The class `CL_ABAP_XSDTYPE_HELPER` contains the methods `TO_XSDQNAME` and `FROM_XSDQNAME` for the conversion of URIs and names to the type `XSDQNAME` and vice versa.

### Executable Example

[asXML, Mapping of Qualified Names](abenasxml_qnames_abexa.md)

## time

The XML schema data type `time` for times is supported by both the built-in ABAP type [`t`](abenabap_xslt_asxml_elementary.md) and the domain `XSDTIME_T`. This domain has the data type `TIMS`. When data is serialized and deserialized, the validity of the time is also checked, which is not the case with the built-in ABAP type `t`. An empty element creates the value *000000* in deserializations.

### Hint

Specifying [`noError`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement[`tt:value`](abenst_tt_value_elementary.md) again prevents an exception due to an invalid time in serializations.

## UUID

The domains have the following meaning:

- `XSDUUID_RAW` has the data type `RAW` with length 16 for 16-byte [UUIDs](../../abap-glossary/abenuuid_glosry.md) in binary format.

- `XSDUUID_CHAR` has the data type `CHAR` with length 32 for 16-byte [UUIDs](../../abap-glossary/abenuuid_glosry.md) in hexadecimal format.

- `XSDUUID_BASE64` has the data type `CHAR` with length 22 for 16-byte [UUIDs](../../abap-glossary/abenuuid_glosry.md) in [base64](../../abap-glossary/abenbase64_glosry.md) format.

A serialization creates the hexadecimal XML schema representation from data objects of these types, with hyphens and lowercase letters. Deserializations accept uppercase letters as well. A character-like UUID of type `XSDUUID_CHAR` can contain only uppercase letters in serializations. Invalid UUIDs raise the exception `CX_SY_CONVERSION_NO_UUID`. An empty element creates byte strings or character strings filled with hexadecimal zeros or blanks in deserializations.

### Hint

UUIDs can be generated in ABAP data objects by the class `CL_SYSTEM_UUID`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serialization of a 16-byte [UUID](../../abap-glossary/abenuuid_glosry.md) in [base64](../../abap-glossary/abenbase64_glosry.md) format.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA uuid TYPE xsduuid_base64. 
TRY. 
    uuid = cl_uuid_factory=>create_system_uuid( )->create_uuid_c22( ). 
  CATCH cx_uuid_error. 
    ... 
ENDTRY. 
 
CALL TRANSFORMATION id SOURCE uuid = uuid 
                       RESULT XML FINAL(xml). 
 
out->write_xml( xml ). 
 
out->display( ).
```

### Executable Example

[asXML, Mapping of UUIDs](abenabap_xslt_mapping_abexa.md)

## language

The domain `XSDLANGUAGE` has the data type [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 1. It allows mappings of one-character internal language codes to the associated two-character external ISO codes and vice versa. The rule for the mapping is specified in the columns `SPRAS` (single-character code) and `LAISO` (two-character code) of the database table `T002`. In serializations, the single-character code is searched for in the table `T002` and the associated two-character code is used as an XML value. The opposite happens in deserializations. In deserializations, lowercase letters are transformed to uppercase letters first. If no code is found in the table `T002`, the following relationship is evaluated:

`Y = ( X2 - 0x20 ) + ( X1 - 0x20 ) * ( 0x80 - 0x20 ) + 0xAC00`

Here, `Y` is the 16-bit Unicode value of the single-character code and `X1` and `X2` are the 7-bit ASCII values of the two characters in the two-character code.

- In serializations, an attempt is made to create a two-character code that satisfies this relationship. If this is not possible, the exception `CX_SY_CONVERSION_UNKNOWN_LANGU` is raised.

- In deserializations, the single-character code is calculated in accordance with this formula. The exception `CX_SY_CONVERSION_UNKNOWN_LANGU` is raised if the XML value is longer than two characters (except when the third character is a hyphen, in which case only the first two characters are used) or if the 7-bit ASCII values of the characters are less than `0x20` or greater than or equal to `0x80`.

### Hint

Specifying [`noError`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement [`tt:value`](abenst_tt_value_elementary.md) again prevents an exception due to an unknown language in serializations. In this case, no conversion is performed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serializes a language code with transformation ID in accordance with table `T002`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA language TYPE xsdlanguage VALUE 'x'. 
cl_demo_input=>request( CHANGING field = language ). 
TRY. 
    CALL TRANSFORMATION id SOURCE language = language 
                           RESULT XML FINAL(xml). 
    out->write_xml( xml ). 
  CATCH cx_transformation_error INTO FINAL(exc_trafo). 
    out->write( exc_trafo->get_text( ) ). 
    IF exc_trafo->previous IS NOT INITIAL. 
      out->write( exc_trafo->previous->get_text( ) ). 
    ENDIF. 
ENDTRY. 
 
out->display( ).
```

## currCode

The domain `XSDCURRCODE` has the data type [`CUKY`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 5. It allows mappings of SAP-specific currency codes to external ISO currency codes and vice versa. The rule for the mapping is specified in the columns `WAERS` (SAP code) and `ISOCD` (ISO code) of the database table `TCURC`. In serializations, the SAP code is searched for in the table `TCURC` and the associated ISO code is used as an XML value and vice versa in deserializations. If a code is not found in the table `TCURC`, the exception `CX_SY_CONVERSION_UNKNOWN_CURR` is raised.

### Hint

Specifying [`noError`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement [`tt:value`](abenst_tt_value_elementary.md) again prevents an exception due to an unknown SAP code in serializations. In this case, no conversion is performed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serializes a currency code with transformation in accordance with table `TCURC`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA currcode TYPE xsdcurrcode VALUE 'EUR'. 
cl_demo_input=>request( CHANGING field = currcode ). 
TRY. 
    CALL TRANSFORMATION id SOURCE currcode = currcode 
                           RESULT XML FINAL(xml). 
    out->write_xml( xml ). 
  CATCH cx_transformation_error INTO FINAL(exc_trafo). 
    out->write( exc_trafo->get_text( ) ). 
    IF exc_trafo->previous IS NOT INITIAL. 
      out->write( exc_trafo->previous->get_text( ) ). 
    ENDIF. 
ENDTRY. 
 
out->display( ).
```

## unitCode

The domain `XSDUNITCODE` has the data type [`UNIT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 3. It allows mappings of SAP-specific unit codes to external ISO unit codes and vice versa. The rule for the mapping is specified in the columns `MSEHI` (SAP code) and `ISOCODE` (ISO code) of the database table `T006`. In serializations, the SAP code is searched for in the table `T006` and the associated ISO code is used as an XML value and vice versa in deserializations. If a code is not found in the table `T006`, the exception `CX_SY_CONVERSION_UNKNOWN_UNIT` is raised.

### Hint

By specifying [`noError`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement [`tt:value`](abenst_tt_value_elementary.md), an exception for an unknown SAP code in serialization can be avoided. In this case, no conversion is performed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serializes a unit of measurement with transformation in accordance with table `T006`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA unitcode TYPE xsdunitcode VALUE 'TON'. 
cl_demo_input=>request( CHANGING field = unitcode ). 
TRY. 
    CALL TRANSFORMATION id SOURCE unitcode = unitcode 
                           RESULT XML FINAL(xml). 
    out->write_xml( xml ). 
  CATCH cx_transformation_error INTO FINAL(exc_trafo). 
    out->write( exc_trafo->get_text( ) ). 
    IF exc_trafo->previous IS NOT INITIAL. 
      out->write( exc_trafo->previous->get_text( ) ). 
    ENDIF. 
ENDTRY. 
 
out->display( ).
```

## base64Binary

The domain `XSDGEO` has the data type [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). Using the domain `XSDGEO`, it is possible to serialize spatial data in the [Extended Well-Known Binary (EWKB)](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_geo_data.md) representation to the [GeoJSON format](https://datatracker.ietf.org/doc/html/rfc7946) and deserialize spatial data in the GeoJSON format to the EWKB representation.

### Hints

- By specifying the [`format`](abenst_option_format.md) value in the [`option`](abenst_option.md) attribute of the ST statement [`tt:value`](abenst_tt_value_elementary.md), the conversion between EWKB and the GeoJSON format is defined. The spatial reference ID (SRID) can be specified as follows:

  - `format(geo=0)` is the same as `format(geometry)`. This is the default spatial reference system.

  - `format(geo=4326)` is the same as `format(geography)` and defines the spatial reference system as WGS 84 standard.

  - `format(geo=3857)` defines the spatial reference system as WGS 84 / Pseudo-Mercator standard.

  - Any available SRID can be used.

- It is not possible to run a simple transformation in XML mode when using `option` to specify a spatial reference system.

- If `XSDGEO` is used for conversions with the [transformation ID](abapcall_transformation.md), the SRID must be assigned to the data field. The SRID of the EWKB value must be the same as defined in the annotated value. Otherwise, the exception `CX_XSDGEO_ERROR` is raised. For more information, refer to [DDIC - Spatial Reference System](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_sptlrf.md).

- The exception `CX_XSDGEO_ERROR` is raised if the EWKB value or the GeoJSON value has a format error.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serializes the EWKB representation to the GeoJSON format using the transformation ID.

``` abap
TYPES town TYPE demo_xsdgeo. 
 
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(town) = VALUE town( name = 'Walldorf' 
  location = '0101000020E6100000E561A1D634A748400D71AC8BDB482140' ). 
 
DATA(json_writer) = cl_sxml_string_writer=>create( 
                     if_sxml=>co_xt_json ). 
 
TRY. 
    CALL TRANSFORMATION id 
      SOURCE root = town 
      RESULT XML json_writer. 
  CATCH cx_xsdgeo_error. 
ENDTRY. 
 
DATA(geo_json) = cl_abap_codepage=>convert_from( 
                  json_writer->get_output( ) ). 
 
out->display( geo_json ).
```
