---
title: "DDIC - Semantic Properties of Domains"
source_file: abenddic_domains_sema.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Data Elements > DDIC - Domains"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Semantic Properties of Domains

Domains can have the following semantic properties:

- **Short text**

  A descriptive short text must be specified when a domain is created.

- **Documentation**

  Documentation can optionally be assigned. This documentation can be read as required.

- **Output properties**

  The output properties affect how fields defined with reference to a data element that references the domain are displayed.

  - **Output length**

    The optional output length overrides the implicit output length as assigned to the built-in elementary data types. The possible output length is determined by the data type and is checked by the ABAP Dictionary tools. If a format is assigned to the built-in data type used, the output length should be long enough for all formatting characters.

  - **Output style**

    A domain with the type of a decimal floating point number must be assigned an [output style](../ddic-built-in-data-types/abenddic_decimal_floating_point.md).

  - **Time format**

    For the data type [`TIMS`](../ddic-built-in-data-types/abenddic_builtin_types.md), a 24-hour or 12-hour format can be set for displaying fields in accordance with the ABAP [time formats](../../abap-programming-language/abap-language-environment/abentime_formats.md).

- **Value range**

  Value ranges for fields on user interfaces can be defined for domains of the [built-in types](../ddic-built-in-data-types/abenddic_builtin_types.md) `CHAR`, `NUMC`, `DEC`, `INT1`, `INT2`, `INT4`, and `INT8`. The value range is ignored for the content of data objects in ABAP programs or of DDIC database table fields that reference a data element with a domain of this type. A value range can be defined using the following:

  - Fixed values

  - Intervals

    Fixed values and intervals can be combined in any way. The following can be specified as fixed values and interval limits:

  - Alphanumeric characters including blanks and special characters for the type `CHAR`. The length is restricted to 10.

  - Positive integers (including 0) for the types `NUMC`, `INT1`, `INT2`, `INT4`, `INT8`, and `DEC` within the [value range](../ddic-built-in-data-types/abenddic_builtin_types.md) defined by the technical properties.

    A short text can be specified for each fixed value or interval, which is then displayed when used in an input help. The fixed values of a domain can be specified as special kinds of [literals](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_literal_v1.md) in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The fixed values provided by SAP can be extended by customers or partners using fixed value appends.

- **Value table**

  A value table can be a DDIC database table that is used as a default for the [check table](../ddic-database-tables/abenddic_database_tables_checktab.md) in cases where a table field of a DDIC database table that references a data element with this domain is included in a [foreign key](../ddic-database-tables/abenddic_database_tables_forkey.md). Specifying a value table alone does not trigger a check.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The domain `S_CLASS` with the type `CHAR` describes the possible classes in a flight booking. The value range of the domain is defined by the fixed values *C* (Business Class), *F* (First Class), and *Y* (Economy Class). This means that only the values *C*, *F*, and *Y* can be entered for all dynpro fields that refer to this domain.
