---
title: "CALL TRANSFORMATION"
source_file: abapcall_transformation.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL TRANSFORMATION

## Syntax

``` abap
CALL TRANSFORMATION ID   
                  | trans|(name)   
                    [PARAMETERS {p1 = e1 p2 = e2 ...}|(ptab)]   
                    [OPTIONS options]   
                    SOURCE {XML src_xml} 
                         | {JSON src_json} 
                         | {{bn1 = e1 bn2 = e2 ...}|(stab)}   
                    RESULT {XML rslt_xml} 
                         | {JSON rslt_json} 
                         | {{bn1 = f1 bn2 = f2 ...}|(rtab)}.  
```

[`OPTIONS options`](abapcall_transformation_options.md)

### Alternative

[1. `... ID ...`](abapcall_transformation.md#alternative-1)

[2. `... trans|(name) ...`](abapcall_transformation.md#alternative-2)

### Addition

[1a. `... SOURCE {XML src_xml}|{JSON src_json}|{{bn1 = e1 bn2 = e2 ...}|(stab)}`](abapcall_transformation.md#addition-1a)

[1b. `... RESULT {XML rslt_xml}|{JSON rslt_json} |{{bn1 = f1 bn2 = f2 ...}|(rtab)}`](abapcall_transformation.md#addition-1b)

[2. `... PARAMETERS {{p1 = e1 p2 = e2 ...}|(ptab)}`](abapcall_transformation.md#addition-2)

## Overview

### Description

This statement calls the specified [XSL transformation](../../abap-glossary/abenxsl_transformation_glosry.md) (XSLT) or a [Simple Transformation](../../abap-glossary/abensimple_transformation_glosry.md) (ST). The source of the transformation is specified behind `SOURCE` and the result is stored as specified behind `RESULT`. `PARAMETERS` can be used to pass parameters to the transformation. The addition [`OPTIONS`](abapcall_transformation_options.md) can be used to specify transformation options `options`. The possible transformation types are:

- from XML to XML (for XSLT only)

- from XML to ABAP

- from JSON to XML

- from JSON to ABAP

- from ABAP to JSON

- from ABAP to ABAP (for XSLT only)

[JSON-XML](../../abap-glossary/abenjson_xml_glosry.md), which maps [JSON](../../abap-glossary/abenjson_glosry.md) data to XML, can be used to execute all categories of transformations for JSON that are also possible for XML. For more information, see [Transformations for JSON](abenabap_json_trafos.md).

### Hints

- The characters *\<*, *\>*, *&*, *"*, and *'*, which have a separate meaning in XML syntax, are handled automatically for XML data. When XML data is written, the required XML notation *\<*, *\>*, *&*, *"*, or *'* is automatically created in values of elements or attributes. When XML data is read, the XML notation is transformed to the corresponding characters. It is not usually necessary to apply the escape character function [`escape`](../abap-processing-internal-data/abenescape_functions.md) or a similar method to character-like XML results of the statement `CALL TRANSFORMATION` and would produce incorrect results. An exception to this rule is creating HTML data with XSLT if it contains JavaScript parts.

- When JSON data is written, [special characters](abenjson_oview.md) in character-like values are prefixed automatically with the escape character *\\*. Conversely, the escape character is removed from character-like values when JSON data is read.

- When a transformation is performed, methods from the [class libraries for XML](abenabap_xml_libs.md) are used internally.

  - In the case of XSLT, a [DOM](../../abap-glossary/abendom_glosry.md) is always needed as a source. This DOM is constructed and processed using the [iXML Library for ABAP Cloud](abenabap_ixml_lib_cloud.md). In the case of the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`, the [iXML Library for ABAP Cloud](abenabap_ixml_lib_cloud.md) is used only if the corresponding objects are specified as source or target.

    The library that is used affects the character set that is supported. The iXML Library supports [UCS-2](../../abap-glossary/abenucs2_glosry.md) and the sXML Library supports [UTF](../../abap-glossary/abenutf_glosry.md).

## Alternative 1

`... ID ...`

### Description

Specifies the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` directly. This transformation exists as an XSL transformation in the repository but is executed by the runtime framework in an optimized ID engine, depending on the transformation source or target. For more information, see:

- [Identity transformation](abenabap_xslt_id.md)

- [Identity Transformation for JSON](abenabap_json_trafo_id.md)

### Executable Example

[Executable Example of an Identity Transformation](abenxslt_abexa.md)

## Alternative 2

`... trans|(name) ...`

### Description

Specifies any transformation. The transformation addition can be specified either statically or dynamically:

- `trans`

  If static, the transformation is specified directly as `trans`.

- `(name)`

  If dynamic, the transformation is specified as the uppercase content of a parenthesized character-like data object `name`.

The specified transformation must exist as an [XSLT program](../../abap-glossary/abenxslt_program_glosry.md) or as a [Simple Transformation](../../abap-glossary/abensimple_transformation_glosry.md) in the [repository](../../abap-glossary/abenrepository_glosry.md). If a dynamically specified transformation is not found, an exception of the class `CX_INVALID_TRANSFORMATION` is raised.

### Executable Example

[Executable Example of a Simple Transformation](abenst_program_abexa.md)

## Addition 1a

`... SOURCE {XML src_xml}|{JSON src_json}|{{bn1 = e1 bn2 = e2 ... }|(stab)}`

### Description

Specifying the source.

**Transformation of XML Data**

When `XML src_xml` is specified, the [XML](../../abap-glossary/abenxml_glosry.md) data contained in `src_xml` is transformed. `src_xml` can exist in the following forms:

- As a data object with the type `string` or as a [standard table](../../abap-glossary/abenstandard_table_glosry.md) with a [flat](../../abap-glossary/abenflat_glosry.md) character-like line type, which can contain the following data:

  - Character-like [XML](../../abap-glossary/abenxml_glosry.md) data in XML 1.0 format.

  - Character-like [JSON](../../abap-glossary/abenjson_glosry.md) data. When any transformation `trans|(name)` is used, the JSON data is converted to the associated [JSON XML format](../../abap-glossary/abenjson_xml_glosry.md) and passed to this transformation. The predefined [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) [`ID`](abenabap_json_trafo_id.md) handles the JSON data directly.

- As a data object with the type `xstring` or as a [standard table](../../abap-glossary/abenstandard_table_glosry.md) with a [flat](../../abap-glossary/abenflat_glosry.md) byte-like line type, which can contain the following data:

  - Byte-like representation of the characters in [XML](../../abap-glossary/abenxml_glosry.md) data in XML 1.0 format, in accordance with a code page such as UTF-8.

  - [XML](../../abap-glossary/abenxml_glosry.md) data in [Binary XML](../../abap-glossary/abenbinary_xml_glosry.md) format.

  - Byte-like representation of the characters in [JSON](../../abap-glossary/abenjson_glosry.md) data, in accordance with a code page such as UTF-8. When any transformation `trans|(name)` is used, the JSON data is converted to the associated [JSON XML format](../../abap-glossary/abenjson_xml_glosry.md) and passed to this transformation in this way. The predefined [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) [`ID`](abenabap_json_trafo_id.md) handles the JSON data directly.

- As an interface reference variable for objects in the [iXML Library for ABAP Cloud](abenabap_ixml_lib_cloud.md) (XSLT only):

  - Interface reference variable with the type `IF_IXML_ISTREAM_CORE` that points to an [input stream](abenabap_ixml_lib_c_input_output.md) that reads XML data.

  - Interface reference variable with the type `IF_IXML_NODE` that points to a node or an entire XML document in [DOM representation](abenabap_ixml_lib_c_dom_access.md).

- As a reference variable of the type `IF_SXML_READER` for [XML Reader](../../abap-glossary/abenxml_reader_glosry.md) in the [sXML Library](abenabap_sxml_lib.md). The transformation moves the reader by one node and processes the entire matching subtree. If the transformation is successful, the reader is located at the end of the processed data. Any valid reader can be specified:

  - XML readers for [XML](../../abap-glossary/abenxml_glosry.md) data in XML 1.0 format.

  - XML readers for [XML](../../abap-glossary/abenxml_glosry.md) data in [Binary XML](../../abap-glossary/abenbinary_xml_glosry.md) format.

  - XOP readers for [XML](../../abap-glossary/abenxml_glosry.md) data in [XOP](../../abap-glossary/abenxop_glosry.md) format.

  - JSON readers for [JSON data](../../abap-glossary/abenjson_glosry.md). When any transformation `trans|(name)` is used, the JSON reader returns the JSON data in [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) format. When a predefined [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) [`ID`](abenabap_json_trafo_id.md) is used, the JSON data is handled directly.

### Hints

- The interface `IF_SXML_READER` is part of the API of the [sXML Library](abenabap_sxml_lib.md), whose objects can be accessed using `CALL TRANSFORMATION`.

- Transformations of XML data in [XOP format](../../abap-glossary/abenxop_glosry.md) are only possible with an XOP reader in the sXML Library. All other formats can be also specified in appropriate strings or internal tables.

- When XML data is specified in strings or internal tables, it is best to use byte strings or byte-like line types and the UTF-8 code page for the representation. If the encoding is defined using a [user-defined transformation](abenabap_xslt_self_written.md) and the XML data is specified in strings or internal tables, there is no effect on the XML result encoding.

- The methods `CONVERT` of the interfaces `IF_ABAP_CONV_IN` and `IF_ABAP_CONV_OUT` of objects created using the class `CL_ABAP_CONV_CODEPAGE` can be used to transform character-like XML data or JSON data to a byte-like representation in accordance with a code page and vice versa.

- The interfaces `IF_IXML_ISTREAM_CORE` and `IF_IXML_NODE` are part of the API of the [iXML Library for ABAP Cloud](abenabap_ixml_lib_cloud.md), whose objects can be accessed using `CALL TRANSFORMATION`.

**Transformation of JSON Data**

When `JSON src_json` is specified, the [JSON](../../abap-glossary/abenjson_glosry.md) data contained in `src_json` is transformed. `src_json` can exist in the following forms:

- As a data object with the type `string`.

- As a data object with the type `xstring`.

- As a reference variable of the type [`IF_JSON_READER`](abenabap_json_lib_reader.md).

**Transformation of ABAP Data**

`bn1 = e1 ...` or `(stab)` is used to specify the ABAP data `e1 e2 ...` to be transformed.

- When the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` is called, the ABAP data is either serialized to the [canonical XML format](abenabap_xslt_asxml.md) [asXML](../../abap-glossary/abenasxml_glosry.md) or to the [canonical JSON format](abenabap_asjson.md) [asJSON](../../abap-glossary/abenasjson_glosry.md), depending on the target.

- When an XSLT program is called, the ABAP data is serialized to the [canonical XML representation](abenabap_xslt_asxml.md), which is then used as the source of the XSL transformation. `bn1 bn2 ...` is used to specify the names of the XML elements that represent the ABAP data objects in the canonical XML representation.

- When a Simple Transformation is called, the transformation has read-only access to the ABAP data using the names `bn1 bn2 ...`.

Instead of using a static parameter list, the data objects can be passed dynamically as value pairs in the columns of an internal table `stab` that has the type `abap_trans_srcbind_tab` from the [type pool](../../abap-glossary/abentype_pool_glosry.md) `ABAP`.

Serializations convert the elementary components of the ABAP data objects to [asXML](../../abap-glossary/abenasxml_glosry.md) or [asJSON](../../abap-glossary/abenasjson_glosry.md), in accordance with the [mappings for built-in ABAP types](abenabap_xslt_asxml_elementary.md) or for [further XML schema data types](abenabap_xslt_asxml_schema.md). This can raise the exceptions described there, some of which can be bypassed by using [transformation options](abapcall_transformation_options.md).

The case of the names in the XML data or JSON data depends on how they are specified in the ABAP runtime framework. If specified statically (`b1`, `b2`, ...), uppercase is used and if specified dynamically in `stab`, the case used there is used.

### Hint

When a Simple Transformation is called, the serialization always creates an internal [XML writer](../../abap-glossary/abenxml_writer_glosry.md), which can be addressed using the interface `IF_SXML_WRITER` from [sXML](abenabap_sxml_lib.md) Library. The object is accessed using attributes of the ST statement [`tt:call-method`](abenst_tt_call-method_static.md).

## Executable Examples

- 

- For deserializations of ABAP data from an XML reader in the sXML Library, see [sXML-Library, Transformation from XML Reader](abensxml_trafo_from_reader_abexa.md).

## Addition 1b

`... RESULT {XML rslt_xml}|{JSON rslt_json}|{{bn1 = f1 bn2 = f2 ...}|(rtab)}`

### Description

Specifying the target.

**Transformation to XML Data**

When `XML rslt_xml` is specified, a transformation to [XML](../../abap-glossary/abenxml_glosry.md) data takes place and this data is passed to `rslt_xml`. `rslt_xml` can exist in the following forms:

- As a variable with the type `string` or as a standard table with a flat character-like line type. The XML data returned by the transformation is stored in XML 1.0 format as a character string in the string or in the table. Here, a byte order mark (BOM) is used as a prefix.

- As a variable with the type `xstring` or as a standard table with a flat byte-like line type. The XML data returned by the transformation is stored in XML 1.0 format as a byte string in the string or table. The byte string represents the characters of the XML data in accordance with the code page UTF-8. A byte order mark (BOM) is not used as a prefix.

- As an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable with the type `xstring` is created.

- As an interface reference variable for objects in the [iXML Library for ABAP Cloud](abenabap_ixml_lib_cloud.md) (XSLT only):

  - Interface reference variable with the type `IF_IXML_OSTREAM_CORE` that points to an [output stream](abenabap_ixml_lib_c_input_output.md) that writes XML data.

  - Interface reference variable with the type `IF_IXML_DOCUMENT` that points to an [XML document](abenabap_ixml_lib_c_input_output.md) in [DOM](../../abap-glossary/abendom_glosry.md) representation.

- As a reference variable with the type `IF_SXML_WRITER` for [XML](../../abap-glossary/abenxml_writer_glosry.md) writers in the [sXML](abenabap_sxml_lib.md) Library. The result of the transformation is added to the current element of the writer as a subtree. Any valid writer can be specified:

  - XML writers for [XML](../../abap-glossary/abenxml_glosry.md) data in XML 1.0 format.

  - XML writers for [XML](../../abap-glossary/abenxml_glosry.md) data in [Binary XML](../../abap-glossary/abenbinary_xml_glosry.md) format.

  - XOP writers for [XML](../../abap-glossary/abenxml_glosry.md) data in [XOP](../../abap-glossary/abenxop_glosry.md) format.

  - JSON writers for [JSON](../../abap-glossary/abenjson_glosry.md) data. A transformation `trans|(name)` must create XML data in [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) format. The predefined [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) [`ID`](abenabap_json_trafo_id.md) creates the appropriate data directly.

### Hints

- The interface `IF_SXML_WRITER` is part of the API of the [sXML Library](abenabap_sxml_lib.md), whose objects can be accessed using `CALL TRANSFORMATION`.

- Transformations to formats other than XML 1.0 are only possible with the corresponding writers in the [sXML Library](abenabap_sxml_lib.md).

- When XML data is stored in strings or internal tables, it is best to use byte strings or byte-like line types and the UTF-8 code page for the representation.

- XML data that is written to [Unicode systems](../../abap-glossary/abenunicode_system_glosry.md) as character-like data cannot be processed as character-like data in a non-Unicode system due to the byte order mark (BOM) that is predefined by the XML standard.

- The methods `CONVERT` of the interfaces `IF_ABAP_CONV_OUT` and `IF_ABAP_CONV_IN` of objects created using the class `CL_ABAP_CONV_CODEPAGE` can be used to transform character-like XML data or JSON data to a byte-like representation in accordance with a code page.

- The interfaces `IF_IXML_OSTREAM_CORE` and `IF_IXML_DOCUMENT` are part of the API of the [iXML Library for ABAP Cloud](abenabap_ixml_lib_cloud.md), whose objects can be accessed using `CALL TRANSFORMATION`.

### Security Hint

If HTML data containing JavaScript is created using the output method `html` of an XSL transformation, the syntax characters `<`, blank, *&*, *"*, and *'* in the JavaScript parts are not transformed to their [XML notation](abenxml_oview.md). To prevent cross site scripting (XSS) in HTML data that contains dynamic JavaScript parts, appropriate measures must be taken. These measures are best applied in the XSL transformation that creates the data.

**Transformation to JSON Data**

When `JSON rslt_json` is specified, a transformation to [JSON](../../abap-glossary/abenjson_glosry.md) data takes place and this data is passed to `rslt_json`. `rslt_json` can exist in the following forms:

- As a variable with the type `string`.

- As a variable with the type `xstring`.

- As a reference variable with the type [`IF_JSON_WRITER`](abenabap_json_lib_writer.md).

- As an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable with the type `xstring` is created.

**Transformation to ABAP Data**

`bn1 = f1 ...` or `(rtab)` are used to specify the ABAP target fields `f1 f2 ...` into which the XML data is to be transformed.

- When the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` is called, the source must either be a [canonical XML representation](abenabap_xslt_asxml.md) or a [canonical JSON representation](abenabap_asjson.md) of ABAP data. The canonical representation is deserialized into the ABAP data objects. `bn1 bn2 ...` is used to specify the names of the XML elements that represent the ABAP data objects in the canonical XML representation, and `f1 f2 ...` is used to specify ABAP data objects that are appropriate to the data type into which they are deserialized.

- When an XSLT program is called, the result of the XSL transformation must represent a [canonical XML representation](abenabap_xslt_asxml.md) that is deserialized into the ABAP data objects, as with the identity transformation.

- When a Simple Transformation is called, the transformation performs writes on the ABAP data using the names `bn1 bn2 ...`.

Instead of using a static parameter list, the data objects can be passed dynamically as value pairs to the columns of the internal table `rtab` that has the type `abap_trans_resbind_tab` from the [type pool](../../abap-glossary/abentype_pool_glosry.md) ABAP.

Deserialization converts the elementary XML or JSON values to elementary ABAP data types in accordance with the [mappings for built-in ABAP types](abenabap_xslt_asxml_elementary.md) or for [further XML schema data types](abenabap_xslt_asxml_schema.md). This can raise the exceptions described there, some of which can be bypassed by using [transformation options](abapcall_transformation_options.md).

The case used in the XML or JSON data must match exactly the case in the ABAP runtime framework. If specified statically (`b1`, `b2`, ...), uppercase is used and if specified dynamically in `rtab`, the case used there is used.

When deserializing from a canonical representation, if no corresponding asXML element or asJON object component exists for an ABAP object, the data object retains its previous value. If an empty XML element or an empty JSON array is assigned to an elementary or tabular ABAP data object, the ABAP data object is set to its type-dependent initial value. If an empty XML element or empty JSON object is assigned to a structure, this has the same effect as non-existent elements on the structure components. The structure components retain their previous values. The transformation option [`clear`](abapcall_transformation_options.md) with the value *all* can be used to initialize all data objects that have nonexistent or empty elements assigned to them.

In the case of the deserialization of internal tables with non-unique [table keys](../abap-data-types-and-data-objects/abenitab_key.md), the order of the duplicate lines in relation to these keys is not retained.

### Hint

When a Simple Transformation is called, deserialization always creates an internal [XML reader](../../abap-glossary/abenxml_reader_glosry.md) object, which can be addressed using the interface `IF_SXML_READER` from the [sXML Library](abenabap_sxml_lib.md). The object is accessed using attributes of the ST statement [`tt:call-method`](abenst_tt_call-method_static.md).

## Executable Examples

- 

- For transformations of XML data to the DOM representation in the iXML Library for ABAP Cloud, see [iXML Library, DOM Representation](abenixml_c_dom_abexa.md).

- 

- For transformations of ABAP data to an XML writer in the sXML Library, see [sXML Library, Transformation to XML Writer](abensxml_trafo_into_writer_abexa.md).

- For deserializations of missing or empty asXML elements or asJSON object components, see:

  - [Deserializing Missing Elements](abenabap_deserl_no_elem_abexa.md)

  - [Deserializing Empty Elements](abenabap_deserl_no_elem_abexa.md)

- For transformations of syntax characters to XML targets, see [Transformation of Syntax Characters](abencall_trafo_escaping_abexa.md).

## Addition 2

`... PARAMETERS {{p1 = e1 p2 = e2 ...}|(ptab)}`

### Description

This addition can be used to bind ABAP data objects `e1 e2 ...` to the parameters `p1 p2 ...` of an [XSL transformation](../../abap-glossary/abenxsl_transformation_glosry.md) or a [Simple Transformation](../../abap-glossary/abensimple_transformation_glosry.md). All elementary data objects and object references are allowed.

Instead of using a static parameter list, the parameters can be specified dynamically as value pairs in the columns of the internal table `ptab` that has one of the following types from the [type pool](../../abap-glossary/abentype_pool_glosry.md) ABAP:

- `abap_trans_parmbind_tab` for specifying strings,

- `abap_trans_objbind_tab` for specifying object references (for XSLT only),

- `abap_trans_parm_obj_bind_tab` for specifying data references (for XSLT only).

**Parameter Passing to XSL Transformations**

The specified parameters must be defined as input parameters in an XSL transformation as follows:

`<xsl:param name="..." sap:type="..." />`

The parameter name must be specified for the attribute `name`. Before a binding can take place, the case used in the XML document must match exactly the case specified in the ABAP runtime framework. If specified statically (`b1`, `b2`, ...), uppercase is used and if specified dynamically in `rtab`, the case used there is used.

For the optional attribute `type`, one of the type names `string`, `number`, `boolean`, `nodeset`, `xstring`, or `object(...)` can be specified, with a global ABAP class specified in parentheses behind `object`. The namespace before `type` must be defined as `xmlns:sap="http://www.sap.com/sapxsl"`, with the prefix `sap` proposed as a convention.

If no type is specified in the transformation, the data types of elementary parameters are mapped to XSL types in accordance with the following table.

| **ABAP Data Type**       | **XSL Parameter Type**                                                           |
|--------------------------|----------------------------------------------------------------------------------|
| `c`, `d`, `n`, `string`  | `string`                                                                         |
| `i` (`b`, `s`), `f`, `p` | `number`                                                                         |
| `x`, `xstring`           | `string`, where the content is represented in [Base 64](../../abap-glossary/abenbase64_glosry.md). |

If the XSL types shown in the table above are specified explicitly in the XSL transformation, appropriate elementary ABAP parameters must be specified that can be converted to the XSL type:

- The XSL type `boolean` expects ABAP parameters of the type `c` with the length one. A blank is interpreted as *false* and any other character as *true*.

- The XSL type `xstring` expects ABAP parameters of the type `x` or `xstring` and the content is represented as hexadecimal.

- The XSL types `nodeset` and `object` expect an object reference variable that points to an instance of a class. The type `nodeset` expects appropriate object properties.

If a parameter does not match the XSL type, an uncatchable exception is raised. If a parameter defined in the XSL transformation is not passed, it is set to a default value in the transformation. Any specified parameters that are not defined in the XSL transformation are ignored.

### Hints

- The XSL types `string`, `number`, `boolean`, and `nodeset` are standard XSL types, where `xstring` and `object` represent special SAP enhancements. The type `xstring` enables byte strings to be represented in hexadecimal instead of base 64. The type `object` enables ABAP methods to be called from the XSLT program.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Two calls of the following simple transformation:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:parameter kind="in" name="PARA" val="0"/> 
  <tt:root name="NUM" type="I"/> 
  <tt:template> 
    <X> 
      <tt:cond check="not-initial(var(PARA))"> 
        <tt:value ref="NUM"/> 
      </tt:cond> 
    </X> 
  </tt:template> 
</tt:transform>
```

The result depends on the parameter passed to the transformation.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
CALL TRANSFORMATION demo_st_parameter SOURCE num = 111 
                                      RESULT  XML DATA(xml). 
 
out->write_xml( xml ). 
 
CALL TRANSFORMATION demo_st_parameter SOURCE num = 111 
                                      RESULT  XML  xml 
                                      PARAMETERS para = 1. 
 
out->write_xml( xml ). 
 
out->display( ).
```

### Executable Example

[XSL Transformations Using Parameters](abenxslt_parameters_abexa.md)

**Parameter Passing to ST Programs**

In an ST program, the parameters must be defined as follows as parameters of the main template outside of a template:

``` abap
`<tt:parameter name="..." [kind="..."] 
 [[s-val="..."][d-val="..."]]|[val="..."] />`
```

When an ST program is called, output parameters and input/output parameters are supported as well as input parameters. The type of the parameter is defined using `kind` in the ST program, where *in*, *out*, and *inout* can be specified. *inout* is the default. The `val` attributes can be used to define replacement values.

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_TRANSFORMATION_ERROR`

- *Cause:* Common superclass of all transformation-specific exception classes for `CALL TRANSFORMATION`. The direct subclasses are `CX_ST_ERROR` for Simple Transformations and `CX_XSLT_EXCEPTION` for XSL transformations. When the statement `CALL TRANSFORMATION` is executed, exceptions of the class `CX_TRANSFORMATION_ERROR` and almost all its subclasses can be handled. The resumability of an exception of the subclass `CX_ST_DESERIALIZATION_ERROR` can be defined using the transformation option [`exceptions = 'resumable'`](abapcall_transformation_options.md).

  In addition, the following exceptions may be raised when a transformation is executed:

  - Exceptions like those raised in [mappings from ABAP data types to asXML](abenabap_xslt_asxml_named.md) cannot be handled directly. These exceptions raise exceptions of the class `CX_TRANSFORMATION_ERROR` (or its subclasses) and can be handled using these.

  - Exceptions raised in ABAP methods called in transformations, such as transformations of objects using the methods [`SERIALIZE_HELPER`](abenasxml_class_instances.md) and [`DESERIALIZE_HELPER`](abenasxml_class_instances.md) or when [accessing ABAP Objects from ST](abenst_abap_objects.md), raise exceptions of the class `CX_TRANSFORMATION_ERROR` (or its subclasses), if they are declared in the interface of the method [`RAISING`](../abap-declarations/abapmethods_general.md). The [resumability](../../abap-glossary/abenresumable_exception_glosry.md) of the original exception is applied here. Non-declared exceptions, on the other hand, raise the exception [`CX_SY_NO_HANDLER`](../abap-program-flow-logic/abenexceptions_procedures.md), which cannot be handled using `CX_TRANSFORMATION_ERROR` (or its subclasses).

  - The exception `CX_SY_STRING_SIZE_TOO_LARGE` can also occur but does not raise an exception of the class `CX_TRANSFORMATION_ERROR`. It must be handled directly (see below).

    The attribute `PREVIOUS` of the associated exception object always contains a reference to the original exception. If an exception of this type is not handled, the [short dump](../../abap-glossary/abenshort_dump_glosry.md) shows the original exception.

**Subclasses of `CX_ST_ERROR`**

`CX_ST_CALL_ERROR`

- *Cause:* Error when calling the transformation

`CX_ST_CALL_METHOD_ERROR`

- *Cause:* Exception in an ABAP method called from the transformation

`CX_ST_CONDITION`

- *Cause:* Error in a transformation condition

`CX_ST_CONSTRAINT_ERROR`

- *Cause:* Data object to be serialized or deserialized is too long.

`CX_ST_DESERIALIZATION_ERROR`

- *Cause:* Error in the deserialization

`CX_ST_FORMAT_ERROR`

- *Cause:* Format error in a node

`CX_ST_INVALID_XML`

- *Cause:* A serialization would produce invalid XML.

`CX_ST_MATCH`

- *Cause:* Deserialization match failed

`CX_ST_REF_ACCESS`

- *Cause:* Error in data node access

`CX_ST_RUNTIME_ERROR`

- *Cause:* Error in execution of the transformation

`CX_ST_SERIALIZATION_ERROR`

- *Cause:* Error in the serialization

`CX_ST_VALIDATION_ERROR`

- *Cause:* Failed validation with the attribute `xsd-type` in the ST statements [`tt:value`](abenst_tt_value_elementary.md), [`tt:write`](abenst_tt_write.md), or [`tt:read`](abenst_tt_read.md). This exception cannot be caught directly.

**Subclasses of `CX_XSLT_EXCEPTION`**

`CX_XSLT_ABAP_CALL_ERROR`

- *Cause:* Error when calling an ABAP method from XSLT

  *Runtime error:* `XSLT_METH_ERROR`

`CX_XSLT_DESERIALIZATION_ERROR`

- *Cause:* Error in the deserialization

  *Runtime error:* `XML_NOT_SUPPORTED`

`CX_XSLT_FORMAT_ERROR`

- *Cause:* Document is not in asXML format

  *Runtime error:* `XML_FORMAT_ERROR`

`CX_XSLT_RUNTIME_ERROR`

- *Cause:* Error in XSLT processor

  *Runtime error:* `UNCAUGHT_EXCEPTION`

`CX_XSLT_SERIALIZATION_ERROR`

- *Cause:* Error in the serialization

  *Runtime error:* `XML_NOT_SUPPORTED`

**Other exception classes**

`CX_SY_STRING_SIZE_TOO_LARGE`

- *Cause:* During a transformation, an operation with a string exceeds its [maximum size](../abap-data-types-and-data-objects/abenmemory_consumption_2.md). This exception does not raise an exception of the class `CX_TRANSFORMATION_ERROR` but must be handled directly.

  It can be handled for all kinds of transformations in the following cases:

  - The target specified behind `RESULT` is of type `xstring` or `string`.

  - The target specified behind `RESULT` is a reference variable that points to an object of the class `CL_SXML_STRING_WRITER`.

    It cannot be handled in the following cases: In these cases, a runtime error always occurs.
