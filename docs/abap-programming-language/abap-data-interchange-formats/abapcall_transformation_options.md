---
title: "CALL TRANSFORMATION, OPTIONS"
source_file: abapcall_transformation_options.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > CALL TRANSFORMATION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL TRANSFORMATION, OPTIONS

## Syntax

``` abap
... OPTIONS [clear              = val] 
            [data_refs          = val] 
            [initial_components = val] 
            [technical_types    = val] 
            [value_handling     = val] 
            [exceptions         = val] 
            [xml_header         = val] ...  
```

### Addition

[1. `... clear`](abapcall_transformation_options.md#addition-1)

[2. `... data_refs`](abapcall_transformation_options.md#addition-2)

[3. `... initial_components`](abapcall_transformation_options.md#addition-3)

[4. `... technical_types`](abapcall_transformation_options.md#addition-4)

[5. `... value_handling`](abapcall_transformation_options.md#addition-5)

[6. `... exceptions`](abapcall_transformation_options.md#addition-6)

[7. `... xml_header`](abapcall_transformation_options.md#addition-7)

[8. `... name_handling`](abapcall_transformation_options.md#addition-8)

[9. `... name_escaping`](abapcall_transformation_options.md#addition-9)

## Overview

### Description

The addition `OPTIONS` enables predefined transformation options to be specified, to which specific values can be assigned to control transformations. The values must be specified in data objects `val` of type `c` or `string`. Each transformation option may only be specified once. Multiple values separated by blanks can be specified for a transformation option in `val`. If an invalid value is specified for a transformation option, a catchable exception of class `CX_SY_TRANS_OPTION_ERROR` is raised.

### Hint

The transformations apply to XML and to [JSON](../../abap-glossary/abenjson_glosry.md), if applicable.

## Addition 1

`...clear`

### Description

The transformation option `clear` controls how the ABAP target fields are initialized when deserializing from XML or JSON to ABAP.

| **Possible Values** | **Meaning**                                                                                                                                                                                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `all`               | All target fields specified after `RESULT` are initialized before calling the transformation. This is the recommended setting.                                                                                                                                                              |
| `supplied`          | In ST, the target fields which have a root node assigned to them in the ST program are initialized before calling the transformation. In XSLT, target fields for which a root node exists in the XML data are initialized before importing the nodes. Other target fields keep their value. |
| `none`              | Default, the target fields specified after `RESULT` are not initialized, except for internal tables                                                                                                                                                                                         |

### Hint

Using the default setting (`none`) can become critical when nonexistent or empty elements are deserialized to data objects. In the case of nonexistent elements, all data objects keep their original values. In the case of empty elements, structures keep their values. In cases like this, it is advisable to use `clear` with the value *all*.

## Addition 2

`... data_refs`

### Description

The transformation option `data_refs` specifies the output of [data references](../../abap-glossary/abendata_reference_glosry.md) if the transformation is from ABAP to XML or JSON.

| **Possible Values** | **Meaning**                                                                                                                                                                                                                                                                                                                             |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `no`                | Default in ST; no data references are produced.                                                                                                                                                                                                                                                                                         |
| `heap`              | Default in XSLT and only possible there; data referenced using [heap references](../../abap-glossary/abenheap_reference_glosry.md) is output as subelements of the [asXML](../../abap-glossary/abenasxml_glosry.md) elements `asx:heap` or the asJSON object `%heap`. Data objects referenced using [stack references](../../abap-glossary/abenstack_reference_glosry.md) are not serialized. |
| `heap-or-error`     | Only possible in XSLT. Like `heap`, but the exception `CX_REFERENCE_NOT_SERIALIZABLE` is raised if the data to be serialized contains [stack references](../../abap-glossary/abenstack_reference_glosry.md).                                                                                                                                              |
| `heap-or-create`    | Only possible in XSLT. Like `heap`, but data objects referenced using [stack references](../../abap-glossary/abenstack_reference_glosry.md) are handled like data objects referenced using [heap references](../../abap-glossary/abenheap_reference_glosry.md).                                                                                                             |
| `embedded`          | Only possible in XSLT. Referenced data objects are output with the reference. It is not possible to deserialize XML data created in this way, since the identity of the objects is lost when serialized.                                                                                                                                |

### Hint

The exception `CX_REFERENCE_NOT_SERIALIZABLE` cannot be caught by specifying it directly. It can only be caught by specifying `CX_XSLT_SERIALIZATION_ERROR`.

### Executable Example

For information about the differences between serializing to `heap` and embedded elements, see [Serializations to Heap or Embedded](abenserialize_ref_heap_embed_abexa.md).

## Addition 3

`... initial_components`

### Description

The transformation option `initial_components` controls the output of initial structure components when transforming from ABAP to XML or JSON.

| **Possible Values** | **Meaning**                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `include`           | Initial components of structures are output.                                                                                                               |
| `suppress_boxed`    | Default; does not output initial [boxed components](../../abap-glossary/abenboxed_component_glosry.md) of structures; initial components of all other structures are output. |
| `suppress`          | Initial components of structures are not output.                                                                                                           |

### Hints

- The suppression of initial components in serializations reduces the data volume. However, this option should be used with caution and only if there is complete control over deserializations. If the option `clear` is not used with the value *all* in serializations, any suppressed components in ABAP data objects are ignored and the target fields keep their values. Deserialization in external systems can cause problems if a suppressed component is expected.

- The suppression of initial components also affects structure components that are typed with the domains for [XML schema data types](abenabap_xslt_asxml_schema.md). For example, a component typed with the domain `XSDBOOLEAN` is not created as output if it has the value `abap_false`. This can also cause unwanted results.

## Addition 4

`... technical_types`

### Description

The transformation option `technical_types` controls the behavior if no type description can be serialized when serializing data references to [asXML](abenasxml_reference_variable.md) or [asJSON](abenabap_asjson_reference_var.md). This is the case when the [technical type properties](../../abap-glossary/abentechnical_type_prpt_glosry.md) of the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) of the data reference variable are known, but the type does not have a name (or it only has a technical name).

| **Possible Values** | **Meaning**                                                                                                                                                                      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `error`             | Default in XSLT and only possible there. The serialization of a data reference variable with a dynamic type without a name raises the exception `CX_REFERENCE_NOT_SERIALIZABLE`. |
| `ignore`            | Only possible in XSLT. A data reference variable with a dynamic type without a name is ignored in serializations.                                                                |

### Hints

- The exception `CX_REFERENCE_NOT_SERIALIZABLE` cannot be caught by specifying it directly. It can only be caught by specifying `CX_XSLT_SERIALIZATION_ERROR`.

- Data types without names are [bound data types](../../abap-glossary/abenbound_data_type_glosry.md) or data types constructed using [RTTS](../../abap-glossary/abenrun_time_type_services_glosry.md).

## Addition 5

`... value_handling`

### Description

The transformation option `value_handling` controls the tolerance of conversions when [mapping elementary ABAP types](abenabap_xslt_asxml_elementary.md).

| **Possible Values**         | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `default`                   | Default setting; in serializations, an invalid value in a field of type `n` raises the exception `CX_SY_CONVERSION_NO_NUMBER`. When deserializing, the exception `CX_SY_CONVERSION_DATA_LOSS` is raised if target fields of the types `c`, `n`, or `x` are too short or the exception `CX_SY_CONVERSION_LOST_DECIMALS` is raised if target fields of the type `p` have too few decimal places.    |
| `move`                      | Only possible in serializations. Invalid values in a field of type `n` are copied to XML or JSON without being changed.                                                                                                                                                                                                                                                                           |
| `accept_data_loss`          | Only possible in deserializations. If target fields of types `c`, `n`, or `x` are too short, surplus data for `c` and `x` is cut off on the right and surplus data for `n` is cut off on the left.                                                                                                                                                                                                |
| `accept_decimals_loss`      | Only possible in deserializations. If target fields of the type `p` have too few decimal places, they are rounded up to the available decimal places.                                                                                                                                                                                                                                             |
| `reject_illegal_characters` | Only possible in deserializations. If a value to be deserialized contains characters that do not match the encoding of the XML data or JSON data, nor the current code page of AS ABAP, an exception of the type `CX_SY_CONVERSION_CODEPAGE` is raised. If the XML or JSON data is passed as an iXML input stream, the setting of the iXML parser overrides the encoding of the XML or JSON data. |

### Hints

- The exceptions mentioned cannot be caught by specifying them directly by `CALL TRANSFORMATION` but are packed into `CX_TRANSFORMATION_ERROR` or its subclasses.

- If a value is specified that is not supported in the specified direction however, the directly catchable exception `CX_SY_TRANS_OPTION_ERROR` is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

If `value_handling = 'reject_illegal_characters'` is specified, for example, an exception is raised if, in the XML header of XML data in the Latin-1 character set, `encoding="utf-8"` is specified and the XML data contains characters other than those of the 7-bit ASCII character set.

## Addition 6

`... exceptions`

### Description

The transformation option `exceptions` controls the behavior of exceptions packed in `CX_TRANSFORMATION_ERROR` or its subclasses.

| **Possible Values** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `resumable`         | Only in deserializations with ST. Exceptions of the class `CX_ST_DESERIALIZATION_ERROR` are raised as [resumable exceptions](../../abap-glossary/abenresumable_exception_glosry.md) of the class. If they are handled using [`CATCH BEFORE UNWIND`](../abap-program-flow-logic/abapcatch_try.md), the target field for which the exception was raised is given its type-dependent initial value and the attribute `RESULT_REF_FOR_RESUME` of the exception object contains a data reference to this target field. The terminated transformation can be resumed using [`RESUME`](../abap-program-flow-logic/abapresume.md). |

If the transformation option `exceptions = 'resumable'` is specified, an exception of the class `CX_ST_DESERIALIZATION_ERROR`, that wraps an original exception behaves as if it were raised as a resumable exception.

### Hints

- When the resumable exception is handled, the target field can also be given a different value using the attribute `RESULT_REF_FOR_RESUME` before processing is resumed using [`RESUME`](../abap-program-flow-logic/abapresume.md).

- If an exception of the class `CX_ST_DESERIALIZATION_ERROR` is raised by an exception that is itself raised in an ABAP method called during the transformation, the transformation option `exceptions = 'resumable'` alone is not sufficient to resume at the position where the exception was raised. To do this, the exception must be declared using [`RAISING RESUMABLE`](../abap-declarations/abapmethods_general.md) and raised using [`RAISE RESUMABLE EXCEPTION`](../abap-program-flow-logic/abapraise_exception_class.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Resumable raising of an exception in the deserialization of a character that does not represent a number to a numeric target field. The attribute `RESULT_REF_FOR_RESUME` points to the target field `field1`, to which a negative value is assigned to demonstrate that the deserialization did not work. The deserialization is then resumed using [`RESUME`](../abap-program-flow-logic/abapresume.md) and `field2` is given the value 2 from the XML file.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TRY. 
    CALL TRANSFORMATION demo_two_values 
      SOURCE field1 = 'x' 
             field2 = '2' 
      RESULT XML FINAL(xml). 
 
    out->write_xml( xml ). 
 
    DATA: field1 TYPE i, 
          field2 TYPE i. 
    TRY. 
        CALL TRANSFORMATION demo_two_values 
          SOURCE XML xml 
          RESULT field1 = field1 
                 field2 = field2 
          OPTIONS exceptions = 'resumable'. 
      CATCH BEFORE UNWIND cx_st_deserialization_error INTO FINAL(exc1). 
        exc1->result_ref_for_resume->*  = -1. 
        RESUME. 
    ENDTRY. 
 
    out->write( |{ field1 }, { field2 }| ). 
 
  CATCH cx_st_invalid_xml INTO FINAL(exc2). 
    out->write( exc2->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```

## Addition 7

`... xml_header`

### Description

The transformation option `xml_header` controls the output of the XML header when transforming to XML and writing to a data object of type `c`, `string`, or to an internal table.

| **Possible Values** | **Meaning**                                                 |
|---------------------|-------------------------------------------------------------|
| `no`                | No XML header is output.                                    |
| `without_encoding`  | An XML header is output without specifying the encoding.    |
| `full`              | Default; an XML header is output and encoding is specified. |

### Hint

The `xml_header` is not possible for `SOURCE JSON src_json`.

## Addition 8

`... name_handling`

### Description

Used to handle camel case elements and attribute names when serializing and deserializing. This is valid for component names of structures (types defined in ABAP or in the DDIC), attribute names of ABAP classes, parameter names of the `SERIALIZE` and `DESERIALIZE_HELPER` methods. However, names provided via `ABAP_TRANS_SRCBIND_TAB` or `ABAP_TRANS_RESBIND_TAB` tables used as part of the `CALL TRANSFORMATION` statement are not subject to name handling.

These values are supported:

- `default`

- `lower_case`

- `lower_camel_case`

- `upper_camel_case`

Rules for camel casing in serialization (in the context of ABAP Object Orientation; the reverse rules apply in deserialization):

- Characters are converted to lower case.

- The character following an underscore is converted to upper case, and the underscore is discarded. Double underscores are replaced with a single underscore.

- The first character will be lower or upper case based on the `lower_camel_case` or `upper_camel_case` value.

- Leading or trailing underscores are preserved. If only underscores exist, one underscore is dropped when using `lower_camel_case` or `upper_camel_case`. The latter also applies to the root node name. If the name is specified as an underscore as in the example `CALL TRANSFORMATION id OPTIONS name_handling = ... SOURCE _ = ...`, the resulting JSON string includes an initial JSON node: `{"":{...`.

### Hint

The option affects the asXML and asJSON representations of ABAP data when using `CALL TRANSFORMATION ID` and XSLT transformations that operate on asXML and asJSON. It does not affect reference nodes in Simple Transformation programs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the transformation of a structure to JSON. The `CALL TRANSFORMATION` statement uses the transformation `id` and the different value options for `name_handling`. The component names illustrate the camel casing rules.

``` abap
TYPES: 
  BEGIN OF s, 
    CompA    TYPE string, 
    comp_b   TYPE string, 
    comp__c  TYPE string, 
    _comp_d_ TYPE string, 
    ___      TYPE string, 
  END OF s. 
 
DATA(struc) = VALUE s( CompA = `A` 
                       comp_b = `B` 
                       comp__c = `C` 
                       _comp_d_ = `D` 
                       ___ = 'E'  ). 
 
DATA json_string TYPE string. 
DO 4 TIMES. 
  DATA(nh) = SWITCH #( sy-index WHEN 1 THEN `default` 
                                WHEN 2 THEN `lower_case` 
                                WHEN 3 THEN `lower_camel_case` 
                                WHEN 4 THEN `upper_camel_case` ). 
 
  CALL TRANSFORMATION id 
    OPTIONS name_handling = nh 
    SOURCE info = struc 
    RESULT JSON json_string. 
 
  CASE sy-index. 
    WHEN 1. 
      ASSERT json_string CS `{"INFO":{"COMPA":"A","COMP_B":"B",` && 
      `"COMP__C":"C","_COMP_D_":"D","___":"E"}}`. 
    WHEN 2. 
      ASSERT json_string CS `{"info":{"compa":"A","comp_b":"B",` && 
      `"comp__c":"C","_comp_d_":"D","___":"E"}}`. 
    WHEN 3. 
      ASSERT json_string CS `{"info":{"compa":"A","compB":"B",` && 
      `"comp_c":"C","_compD_":"D","__":"E"}}`. 
    WHEN 4. 
      ASSERT json_string CS `{"Info":{"Compa":"A","CompB":"B",` && 
      `"Comp_c":"C","_CompD_":"D","__":"E"}}`. 
  ENDCASE. 
ENDDO.
```

## Addition 9

`... name_escaping`

### Description

Used to escape names of elements and attribute names when serializing and deserializing. The option can only be used in the context of JSON transformations with the additions `... JSON`. These values are supported:

- `default`

- `no`

- `json`

`default` handles valid characters in ABAP names (for example, from the ABAP Dictionary, but not in the context of ABAP Object Orientation) that are not allowed in XML. Special characters include, for example, `/` characters (for name spaces) that are transformed to `_-`. To discard the default behavior, `no` can be used. `json` escapes in deserialization (the reverse rule applies in serialization), characters not allowed in ABAP names (in the context of ABAP Object Orientation) as the hex code of the character (single or double byte) and double underscores. For example, a space is transformed to `__20__`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example illustrates serialization and deserialization using JSON, `CALL TRANSFORMATION` statements that use the transformation `id`, and value options for `name_escaping`. The component names of the demo structure used reflect the escaping with underscores and hex codes of characters.

``` abap
TYPES: 
  BEGIN OF s, 
    /comp/a  TYPE string, 
    __00__   TYPE string, 
    __15__   TYPE string, 
    __20__   TYPE string, 
    __0041__ TYPE string, 
    __005a__ TYPE string, 
    _005a_   TYPE string, 
  END OF s. 
 
DATA(struc) = VALUE s( /comp/a = `A` 
                       __00__ = `B` 
                       __15__ = `C` 
                       __20__ = `D` 
                       __0041__ = `E` 
                       __005a__ = `F` 
                       _005a_ = `G` ). 
 
DATA struc2 LIKE struc. 
DATA json_string TYPE string. 
 
DO 3 TIMES. 
  DATA(ne) = SWITCH #( sy-index WHEN 1 THEN `default` 
                                WHEN 2 THEN `no` 
                                WHEN 3 THEN `json` ). 
 
  CALL TRANSFORMATION id 
    OPTIONS name_escaping = ne 
    SOURCE demo = struc 
    RESULT JSON json_string. 
 
  CALL TRANSFORMATION id 
     OPTIONS name_escaping = ne 
     SOURCE JSON json_string 
     RESULT demo = struc2. 
 
  CASE sy-index. 
    WHEN 1. 
      ASSERT json_string CS 
      `{"DEMO":{"_-COMP_-A":"A","__00__":"B","__15__":"C",` && 
      `"__20__":"D","__0041__":"E","__005A__":"F","_005A_":"G"}}`. 
    WHEN 2. 
      ASSERT json_string CS 
      `{"DEMO":{"/COMP/A":"A","__00__":"B","__15__":"C",` && 
      `"__20__":"D","__0041__":"E","__005A__":"F","_005A_":"G"}}`. 
    WHEN 3. 
      ASSERT json_string CS 
      `{"DEMO":{"/COMP/A":"A","\u0000":"B","\u0015":"C",` && 
      `" ":"D","A":"E","Z":"F","_005A_":"G"}}`. 
  ENDCASE. 
 
  ASSERT struc2 = struc. 
ENDDO.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_TRANS_OPTION_ERROR`

- *Cause:* Invalid transformation option or invalid value.
