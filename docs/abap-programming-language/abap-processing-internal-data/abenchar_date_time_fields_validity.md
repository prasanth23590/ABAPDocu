---
title: "Validity of Date Fields and Time Fields"
source_file: abenchar_date_time_fields_validity.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Date Fields and Time Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Validity of Date Fields and Time Fields

Date fields and time fields of the types `d` and `t` can contain any characters.

- Valid values for the type `d`, however, are only those digits that are allowed as dates according to the calendar rules in the format *yyyymmdd*: *yyyy* (year): 0001 to 9999, *mm* (month): 01 to 12, *dd* (day): 01 to 31.

- Valid values for the type `t`, however, are only those digits that can be interpreted as times in the 24-hour clock format *hhmmss*. *hh* (hours): 00 to 23, *mm* (minutes): 00 to 59, *ss* (seconds): 00 to 59.

The ABAP runtime framework checks the validity at the following points:

- Date fields and time fields with invalid values raise an exception as a [source field](abenmove_exact_elementary_valid.md) of a [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md). Conversely, source fields of other types must not produce any invalid values in date fields and time fields as [target fields](abenmove_exact_elementary_fit.md) in a lossless assignment.

- Invalid values cannot be converted to [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) using the statements [`CONVERT INTO UTCLONG`](abapconvert_date_utclong.md) and [`CONVERT INTO TIME STAMP`](abapconvert_date_time-stamp.md).

- In a regular assignment to numeric fields, [date fields](abenconversion_type_d.md) and [target fields](abenconversion_type_t.md) with invalid values produce the value 0, with the following exceptions:

  - For a source field of the type `d`, the values from 10/5/1582 to 10/14/1582, which are missing due to the conversion from the Julian to the Gregorian calendar, are handled either as invalid values or as the valid values from 10/15/1582 to 10/24/1582, depending on the operand position.

  - For a source field of the type `t` that contains only digits, the numeric value is also calculated for invalid times according to the formula `hh*3600+mm*60+ss`.

- For regular assignments of [numeric fields](abennumeric_source_fields.md) to date fields and time fields, the numeric fields must be within the value range of the data type `i` and comply with the following special rules:

  - When number values are assigned to date fields that cannot result from the reverse conversion, the date field is initialized

  - Any number values can be assigned to time fields. When converted, the number value is divided by 86400 and only the integer remainder of the division is respected, which always produces a valid time in hours, minutes, and seconds.

No checks are generally made on other assignments to date fields and time fields not mapped to assignments of numeric values or to other operand positions. As a result, invalid values are produced easily by date fields and time fields, and then processed further.

## Initial Value of Date Fields

The initial value *00000000* of the data type `d` and the date 01.01.0001 play a special role in this context.

- The initial value *00000000* of data type `d` is not a valid date. A conversion of the initial value *00000000* to a numeric data type results, like all invalid values, in the value 0. The reverse conversion of the number 0 to a date field of the type `d` always produces the invalid date *00000000*. Negative and oversized numbers also produce the invalid date *00000000*.

- Since a conversion from a valid date in a field of the type `d` results in the number of days since 01.01.0001, this date is the zero point for date calculations. A conversion of a date field of the type `d` with the value *00010101* to a numeric value produces the value 0, like the conversion of the initial value or another invalid value, and the conversion cannot be reversed.

1 is the smallest number that is converted to a valid date, 02.01.0001, during assignment to a date field of type `d`. Assignments between valid date fields and numeric fields can be reversed only from this date.

In [lossless assignments](../../abap-glossary/abenlossless_assignment_glosry.md), invalid values in source fields raise exceptions instead of producing the value 0 or *00000000*. Here, the value *00010101*, which actually belongs to the value range, is considered invalid, while the initial value *00000000*, which does not actually belong to the value range, is considered valid. This means that the initial value *00000000* can be used in lossless assignments and all valid assignments between date fields and numeric fields can be reversed.

[ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) is an exception to this rule. Here, the value *00010101* is also accepted as a valid date and handled like the initial value *00000000* in operand positions in which values must comply with the rules for lossless assignments.

## Hint

The validity of the content of date fields and time fields must be guaranteed before they are accessed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Identification of an invalid date by a comparison with the value 0. For the comparison, the date field is converted to an integer field of type `i`, where an invalid date produces the value 0. The valid date *00010101*, which would also produce the value 0, is handled separately beforehand.

``` abap
FINAL(invalid_date) = '20160231'. 
 
DATA(date) = CONV d( invalid_date ). 
 
date = COND #( WHEN date = '00010101' OR date <> 0 THEN date 
               ELSE THROW cx_sy_conversion_no_date( ) ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Identification of an invalid time by a comparison with the value 0. For the comparison, the time field is converted to an integer field of type `i`, where an invalid time produces the value 0. The valid time *000000*, which would also produce the value 0, is handled separately beforehand.

``` abap
FINAL(invalid_time) = 'XXXXXX'. 
 
DATA(time) = CONV t( invalid_time  ). 
 
time = COND #( WHEN time = '000000' OR time <> 0 THEN time 
               ELSE THROW cx_sy_conversion_no_time( ) ).
```
