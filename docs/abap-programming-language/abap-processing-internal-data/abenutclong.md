---
title: "Time Stamp Fields with Time Stamp Type"
source_file: abenutclong.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Time Stamp Fields with Time Stamp Type

ABAP contains the built-in ABAP type [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) for UTC time stamps with a precision of 100 nanoseconds. A data object of this time stamp type is a time stamp field. Each valid value of a time stamp field is a [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) and represents a unique time in [UTC](../../abap-glossary/abenutc_glosry.md) reference time. In accordance with the POSIX standard, [leap seconds](../../abap-glossary/abenleap_second_glosry.md) are not supported, that is, each day has exactly 86400 seconds.

- [Access to Time Stamp Fields](abenutclong.md#access-to-time-stamp-fields)

- [Initial Value of a Time Stamp Field](abenutclong.md#initial-value-of-a-time-stamp-field)

- [Internal Representation of a Time Stamp in a Time Stamp Field](abenutclong.md#internal-representation-of-a-time-stamp-in-a-time-stamp-field)

## Access to Time Stamp Fields

Time stamp fields can be used in suitable operand positions and special [assignment](abenconversion_elementary.md) and [comparison rules](../abap-program-flow-logic/abenlogexp_rules_operands.md) apply. Time stamp fields are only convertible to [text fields](../../abap-glossary/abentext_field_glosry.md) of the type `c` and [text strings](../../abap-glossary/abentext_string_glosry.md) of the type `string`.

The following functions, statements, and classes are designed specifically for time stamp fields:

- [Time stamp functions](abentimestamp_functions.md)

- [Conversion Statements for Time Stamp Fields](abentimestamp_conversions.md)

- [System Class for Time Stamp Fields](abentimestamp_system_class.md)

A time stamp field must have valid content each time it is used. If a time stamp field is used that contains an invalid UTC time stamp or the initial value, a catchable exception of the class `CX_SY_CONVERSION_NO_DATE_TIME` is usually raised. The content remains unchecked only in castings or in assignments between time stamp fields.

### Hint

For time stamp fields, conversion errors raise an exception of the class `CX_SY_CONVERSION_NOT_SUPPORTED`.

## Initial Value of a Time Stamp Field

The initial value of a time stamp is not a real time stamp value, that is, it does not represent an UTC time stamp, but an empty value, which is handled as follows:

- In [comparisons](../../abap-glossary/abencomparison_glosry.md) and sorts based on comparisons, an initial time stamp field is smaller than every real time stamp.

- An initial time stamp field passed as an argument is handled like the smallest real time stamp in the [time stamp functions](abentimestamp_functions.md).

- In the [conversion statements](abentimestamp_conversions.md), initial time stamp fields produce initial results.

- During the [conversion](abenconversion_type_utclong.md) to character-like fields, an initial time stamp field fills a text field with spaces or creates an empty text string.

- During formatting as a character string using [string templates](../../abap-glossary/abenstring_template_glosry.md), an initial time stamp field creates a character string consisting of spaces.

## Internal Representation of a Time Stamp in a Time Stamp Field

The internal representation of the valid values of a [time stamp field](../../abap-glossary/abentimestamp_field_glosry.md) with the [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) are uninterrupted sequences of integers starting from 0, where 0 represents the initial value and each number greater than 0 is assigned exactly one real time stamp.

- The minimum internal value is 1 and corresponds to the time stamp *0001-01-01T00:00:00.0000000*.

- The maximum internal value is 3,155,380,704,000,000,000 and corresponds to the time stamp *9999-12-31T23:59:59.9999999*.

- The time interval between time stamps, which is represented by two adjacent integers, is 100 ns. Each integer between the minimum and maximum value represents a time stamp of 100 ns multiplied by the value of the number after *0001-01-01T00:00:00.0000000*.

- Time stamp fields must meet an [alignment requirement](../abap-data-types-and-data-objects/abenalignment.md). Their memory address must be divisible by eight.

### Hint

Due to the switch from the Julian calendar to the Gregorian calendar, the UTC time stamps *1582-10-04 23:59:59.9999999* and *1582-10-15T00:00:00.0000000* are directly adjacent. Internally, they are represented using two consecutive integers.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet uses [`CASTING int8`](abapassign_casting.md) to show how UTC time stamps in time stamp fields are represented internally. The string representation of an initial time stamp is an empty string and internally the integer number 0.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA ts TYPE utclong. 
FIELD-SYMBOLS <fs> TYPE int8. 
ASSIGN ts TO <fs> CASTING. 
out->write( |Initial value:           { ts }| ). 
out->write( |Internal representation: { <fs> }| ). 
out->line( ). 
 
<fs> = 1. 
out->write( |First valid value:       { ts }| ). 
out->write( |Internal representation: { <fs> }| ). 
out->line( ). 
 
ts = utclong_current( ). 
out->write( |Current timestamp:       { ts }| ). 
out->write( |Internal representation: { <fs> }| ). 
out->line( ). 
 
<fs> = '3155380704000000000'. 
out->write( |Last valid value:        { ts }| ). 
out->write( |Internal representation: { <fs> }| ). 
out->line( ). 
 
<fs> = '3155380704000000001'. 
TRY. 
    out->write( |Invalid value:         { ts }| ). 
  CATCH cx_sy_conversion_no_date_time INTO FINAL(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
out->write( |Internal representation: { <fs> }| ). 
 
out->display(  ).
```
