---
title: "asXML - Mapping of Elementary ABAP Types"
source_file: abenabap_xslt_asxml_elementary.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of Elementary ABAP Types

The asXML representation of elementary ABAP types is used in XSL transformations and in Simple Transformations. In both cases, the elementary values or the elementary components of complex structures are converted in accordance with this mapping.

For elementary data objects with [built-in ABAP types](../../abap-glossary/abenbuiltin_data_type_glosry.md), the asXML representation is based on the representation of [XML schema data types](http://www.w3.org/TR/xmlschema-2/) from the namespace `xsd="http://www.w3.org/2001/XMLSchema"`, where dates and times are represented in accordance with ISO-8601 and binary data is represented in accordance with [Base64](../../abap-glossary/abenbase64_glosry.md). The mapping of ABAP types to the XML schema data types is not fully bijective due to the different value ranges. For example, a time zone can be specified for the XML schema data type `xds:date`, which is not possible for the ABAP type `d`.

- [Mapping Tables](abenabap_xslt_asxml_elementary.md#mapping-tables)

  - [Numeric Data Types](abenabap_xslt_asxml_elementary.md#numeric-data-types)

  - [Character-Like Data Types](abenabap_xslt_asxml_elementary.md#character-like-data-types)

  - [Byte-Like Data Types](abenabap_xslt_asxml_elementary.md#byte-like-data-types)

  - [Date Types, Time Types, and Time Stamp Types](abenabap_xslt_asxml_elementary.md#date-types-time-types-and-time-stamp-types)

- [Special Features of Serialization](abenabap_xslt_asxml_elementary.md#special-features-of-serialization)

- [Special Features of Deserialization](abenabap_xslt_asxml_elementary.md#special-features-of-deserialization)

## Hints

- Some of the mapping rules can be overridden by specifying [`format`](abenst_option_format.md), [`decimals`](abenst_option_format.md), [`regime`](abenst_option_format.md), and [`noError`](abenst_option_format.md) in the [`option`](abenst_option.md) attribute of the ST statement [`tt:value`](abenst_tt_value_elementary.md).

- Exceptions from mappings cannot be handled directly. Instead, the exception `CX_TRANSFORMATION_ERROR` (or one of its subclasses) from statement [`CALL TRANSFORMATION`](abapcall_transformation.md) can be handled. The attribute `PREVIOUS` then contains a reference to the original exception.

- The exceptions that occur when mapping the data types shown here can in some cases be suppressed by specifying [`noError`](abenst_option_format.md) in the [`option`](abenst_option.md) attribute of the ST statement [`tt:value`](abenst_tt_value_elementary.md).

## Mapping Tables

### Numeric Data Types

| **ABAP Type** | **ABAP Representation** | **XML Schema Type**                    | **XML Representation** |
|---------------|-------------------------|----------------------------------------|------------------------|
| `b`           | *123*                   | `xsd:unsignedByte`                     | *123*                  |
| `s`           | *-123*                  | `xsd:short`                            | *-123*                 |
| `i`           | *-123*                  | `xsd:int`                              | *-123*                 |
| `int8`        | *-123*                  | `xsd:long`                             | *-123*                 |
| `p`           | *-1.23*                 | `xsd:decimal`                          | *-1.23*                |
| `decfloat16`  | *123E+1*                | `precisionDecimal`, `totalDigits = 16` | *1.23E+3*              |
| `decfloat34`  | *-3.140...0E+02*        | `precisionDecimal`, `totalDigits = 34` | *-314.0...0*           |
| `f`           | *-3.140...0E+02*        | `xsd:double`                           | *-3.14E2*              |

### Hints

- In the case of ABAP type `p`, a number with more decimal places than available places (twice the length minus one) is considered invalid and cannot be serialized to asXML.

- If [`noError`](abenst_option_format.md) is specified in the [`option`](abenst_option.md) attribute of the ST statement [`tt:value`](abenst_tt_value_elementary.md), an invalid sign byte for type `p` is interpreted as a plus sign, which prevents the corresponding exception.

- The type `precisionDecimal` is not yet an official XML schema type.

### Character-Like Data Types

| **ABAP Type** | **ABAP Representation** | **XML Schema Type**             | **XML Representation** |
|---------------|-------------------------|---------------------------------|------------------------|
| `c`           | *\_Hi*                  | `xsd:string`                    | *\_Hi*                 |
| `string`      | *\_Hello\_*             | `xsd:string`                    | *\_Hello\_*            |
| `n`           | *001234*                | `xsd:string` (`pattern [0-9]+`) | *001234*               |

### Byte-Like Data Types

| **ABAP Type** | **ABAP Representation** | **XML Schema Type** | **XML Representation** |
|---------------|-------------------------|---------------------|------------------------|
| `x`           | *ABCDEF*                | `xsd:base64Binary`  | *q83v*                 |
| `xstring`     | *456789AB*              | `xsd:base64Binary`  | *RweJqw==*             |

### Date Types, Time Types, and Time Stamp Types

| **ABAP Type** | **ABAP Representation**       | **XML Schema Type** | **XML Representation**       |
|---------------|-------------------------------|---------------------|------------------------------|
| `d`           | *20020204*                    | `xsd:date`          | *2002-02-04*                 |
| `t`           | *201501*                      | `xsd:time`          | *20:15:01*                   |
| `utclong`     | *2019-04-10 12:37:29.5040200* | `xsd:datetime`      | *2019-04-10T12:37:29.50402Z* |

### Hint

During the serialization of a time stamp field of the type `utclong`, only the significant decimal places are generated. There may also be fewer than seven decimal places for the deserialization.

## Special Features of Serialization

In serializations, ABAP values are converted to the appropriate character-like XML format. Deserializations operate in the opposite direction. The following differences apply compared to the usual [conversion rules](../abap-processing-internal-data/abenconversion_rules.md) that apply in ABAP.

- In serializations of [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md), the same format is created as for their [conversion to type `string`](../abap-processing-internal-data/abenconversion_type_decfloat.md).

- When data objects with the type `x` are serialized, trailing bytes with the value hexadecimal 0 are handled in the same way as trailing blanks with data type `c` and are ignored.

- When the following ABAP data objects are serialized to asXML, partial checks are made to see whether the ABAP data object has a valid value:

  - A data object with the type `n` can contain only digits.

  - A data object with the type `p` must represent a valid packed number.

  - A data object with the type `d` or `t` cannot contain any leading or trailing blanks and the corresponding separator (*-* or *:*) at the same time.

  - A data object of the type `utclong` must contain a valid value. The initial value results in an empty XML element.

Any violations of these rules raise catchable exceptions, some of which can be bypassed by specifying a [transformation option](abapcall_transformation_options.md) after the `OPTIONS` addition of the `CALL TRANSFORMATION` statement.

### Hints

- To check the validity of dates and times, the domains [`XSDDATE_D`](abenabap_xslt_asxml_schema.md) and [`XSDTIME_T`](abenabap_xslt_asxml_schema.md) can be used instead of the data types `d` and `t`.

- If [`noError`](abenst_option_format.md) is specified in the [`option`](abenst_option.md) attribute of the ST statement [`tt:value`](abenst_tt_value_elementary.md), leading and trailing blanks are ignored for type `n`, which prevents the corresponding exception.

## Special Features of Deserialization

- For deserialization to [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md), the [conversion rule for source fields of the type `c`](../abap-processing-internal-data/abenconversion_type_c.md) is used.

- Deserializations to an ABAP data object must retain the precision of the XML value:

  - Numeric types cannot lose any [places](../../abap-glossary/abenplace_glosry.md).

  - In character-like or byte-like data types with fixed lengths (`c`, `n`, `x`), the target object must have enough places for the entire content, unless only leading and trailing blanks in data type `c` and leading zeros in data type `n` are affected.

- Structures cannot be converted to elementary data objects.

- Deserializations fill data objects of the type `c` or `x` with blanks or hexadecimal 0 on the right, as usual, if fewer characters or bytes are passed than can fit in the data object.

- If the required XML element does not exist in deserializations to an elementary data object, the elementary data object keeps its previous value. If an empty element is assigned to an elementary data object, it is set to its type-dependent initial value. To initialize the data object in either case, the transformation option [`clear`](abapcall_transformation_options.md) can be used with the value *all*.

Any violations of these rules raise catchable exceptions such as `CX_SY_CONVERSION_DATA_LOSS`, some of which can be bypassed by specifying a [transformation option](abapcall_transformation_options.md) after the `OPTIONS` addition of the `CALL TRANSFORMATION` statement.

### Executable Example

[asXML, Mapping of Elementary Data Types](abenasxml_elementary_abexa.md)
