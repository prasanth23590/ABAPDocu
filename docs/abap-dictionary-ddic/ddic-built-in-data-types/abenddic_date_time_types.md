---
title: "DDIC - Date Fields, Time Fields, and Time Stamp Fields"
source_file: abenddic_date_time_types.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types > DDIC - Properties of the Built-In Dictionary Types > DDIC - Special Dictionary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Date Fields, Time Fields, and Time Stamp Fields

The following data types in ABAP Dictionary describe date fields, time fields, and time stamp fields:

- [Date Types, Time Types, and Time Stamp Types](abenddic_date_time_types.md#date-types-time-types-and-time-stamp-types)

- [Character-Like Date Fields and Time Fields](abenddic_date_time_types.md#character-like-date-fields-and-time-fields)

## Date Types, Time Types, and Time Stamp Types

The following built-in data types in ABAP Dictionary represent real date types, time types, and time stamp types in a database:

- [`DATN`](abenddic_builtin_types.md) for date fields in the database.

- [`TIMN`](abenddic_builtin_types.md) for time fields in the database.

- [`UTCLONG`](abenddic_builtin_types.md) for time stamp fields in the database.

Database fields with these types generally contain only valid values for dates, times, and UTC time stamps according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) in the internal representation of the database. These types are currently only supported by [SAP HANA databases](../../abap-glossary/abenhana_database_glosry.md).

### Hints

- The dictionary types `DATN` and `TIMN` are mapped to the character-like ABAP date type and time type [`d`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) or [`t`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md). The built-in ABAP type [`utclong`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md), on the other hand, provides a real time stamp type for `UTCLONG`.

- The initial value of `UTCLONG` is denoted as "Empty" that is mapped to an [empty time stamp](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/3f81ccc7e35d44cbbc595c7d552c202a) on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) and to the initial value of [`utclong`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) in ABAP.

- The types `DATN` and `TIMN` are recommended for saving individual dates and times. Access to dates and times in the corresponding functions and expressions is optimized for these types. In the case of the dictionary types `DATS` and `TIMS`, such access may not be possible at all or they may need to be converted to real date and time types.

## Character-Like Date Fields and Time Fields

Instances of the following data types in ABAP Dictionary are created on the database using character-like fields:

- [`DATS`](abenddic_builtin_types.md) for [date fields](../../abap-glossary/abendate_field_glosry.md)

  From a technical perspective, the built-in data type `DATS` describes objects of the type `CHAR` with a length of 8 characters. It is intended to be used for a [calendar date](../../abap-glossary/abencalendar_date_glosry.md) with the format `YYYYMMDD`. However, there is no validity check when writing to or reading from database fields of this type.

- [`TIMS`](abenddic_builtin_types.md) for [time fields](../../abap-glossary/abentime_field_glosry.md)

  From a technical perspective, the built-in data type `TIMS` describes objects of the type `CHAR` with a length of 6 characters. It is intended to be used for a [time](../../abap-glossary/abenday_time_glosry.md) with the format `HHMMSS`. However, there is no validity check when writing to or reading from database fields of this type.

- [`ACCP`](abenddic_builtin_types.md) for posting periods

  From a technical perspective, the built-in data type `ACCP` describes objects of the type `CHAR` with a length of 6 characters. It is intended to be used for a posting period with the format `YYYYMM`. This is not checked however when writing to or reading from database fields of this type.

### Hints

- If possible, the types `DATN` and `TIMN` should be used.
