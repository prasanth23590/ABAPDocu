---
title: "sql_exp - sql_cast, Conversion Rules"
source_file: abensql_cast_rules.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_cast"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_cast, Conversion Rules

The following sections describe the conversion rules for [cast expressions](abensql_cast.md) in ABAP SQL.

- [Numeric Source Type](abensql_cast_rules.md#numeric-source-type)

  - [Source Type `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, `FLTP`](abensql_cast_rules.md#source-type-int1-int2-int4-int8-dec-curr-quan-decfloat16-decfloat34-fltp)

  - [Source Type `DF16_DEC`, `DF34_DEC`](abensql_cast_rules.md#source-type-df16_dec-df34_dec)

- [Character-Like Source Type](abensql_cast_rules.md#character-like-source-type)

  - [Source Types `CHAR`, `SSTRING`](abensql_cast_rules.md#source-types-char-sstring)

  - [Source Type `NUMC`](abensql_cast_rules.md#source-type-numc)

  - [Source Types `DATN`, `TIMN`](abensql_cast_rules.md#source-types-datn-timn)

  - [Source Types `DATS`, `TIMS`, `CLNT`](abensql_cast_rules.md#source-types-dats-tims-clnt)

  - [Source Types `LANG`, `UNIT`, `CUKY`](abensql_cast_rules.md#source-types-lang-unit-cuky)

Data types that cannot be converted to each other are not listed. In these cases, casts are either not possible or only casts between type-compliant operands. If the source type and the target type are technically identical, the content is transferred without being converted.

## Numeric Source Type

### Source Type `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, `FLTP`

- Numeric target type

  The possible target types are `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, and `FLTP`.

  - The source value is converted to the internal representation for the target type.

  - If the value range is exceeded, a catchable exception of class `CX_SY_OPEN_SQL_DB` is raised. In the case of the target types `DEC`, `CURR`, and `QUAN`, this applies to the integer digits and any surplus decimal places are cut off without rounding. In the case of the target types `DECFLOAT16`, `DECFLOAT34`, and `FLTP`, any surplus decimal places are cut off with rounding.

  - In the case of the target type `FLTP`, values that cannot be represented as [binary floating point numbers](../../abap-glossary/abenbinfloat_glosry.md) are converted to the next adjacent number.

- Character-like target type

  The possible target types are `CHAR` and `SSTRING`.

  - The number value is converted to a character string in [mathematical notation](../../abap-glossary/abenmathematical_notation_glosry.md) without decimal separators and is left-aligned.

  - The length of the target type must be sufficient for all potential values including the sign.

  - In the case of the source types `DECFLOAT16` and `DECFLOAT34`, [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md) is produced from a specific value.

  - In the case of the source type `FLTP` either the [mathematical](../../abap-glossary/abenmathematical_notation_glosry.md) or [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md) is produced from a specific value.

### Hint

When the source type `DEC` is converted to a character-like target type, it is database-dependent whether non-relevant zeros are included in front of and after the decimal separator.

### Source Type `DF16_DEC`, `DF34_DEC`

- Numeric target type

  The possible target types are `INT1`, `INT2`, `INT4`, `INT8`, `DECFLOAT16`, `DECFLOAT34`, and `FLTP`.

  - The source value is converted to the internal representation for the target type.

  - If the value range is exceeded, a catchable exception of class `CX_SY_OPEN_SQL_DB` is raised. In the case of the target type `FLTP`, any surplus decimal places are cut off with rounding.

  - In the case of the target type `FLTP`, values that cannot be represented as [binary floating point numbers](../../abap-glossary/abenbinfloat_glosry.md) are converted to the next adjacent number.

## Character-Like Source Type

### Source Types `CHAR`, `SSTRING`

- Character-like target type

  The possible target types are `CHAR`, `SSTRING`, `NUMC`, `DATS`, `TIMS`, `CLNT`, `LANG`, `UNIT`, and `CUKY`.

  - The character string is written to the target field as a left-aligned string including leading blanks. If the target type is too short, it is truncated on the right. If the target field is too long, it is padded on the right with blanks.

  - There is no special handling for the special target type for numeric text, `NUMC`, and for the date/time types `DATS` and `TIMS`. It is advisable to only convert valid values.

- Numeric target type

  The possible target types are `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, and `FLTP`.

  - The source field must contain a character string that can be interpreted as a number, otherwise a catchable exception of class `CX_SY_OPEN_SQL_DB` is raised.

  - If the value range is exceeded, a catchable exception of class `CX_SY_OPEN_SQL_DB` is raised. In the case of the target types `DEC`, `CURR`, and `QUAN`, this applies to the integer digits and any surplus decimal places are cut off without rounding. In the case of the target type `FLTP`, any surplus decimal places are cut off without rounding. In the case of the target types `DECFLOAT16` and `DECFLOAT34`, rounding takes place to the last significant place.

  - In the case of the target type `FLTP`, values that cannot be represented as [binary floating point numbers](../../abap-glossary/abenbinfloat_glosry.md) are converted to the next adjacent number.

### Source Type `NUMC`

- Numeric target type

  The possible target types are `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, and `FLTP`.

  - The validity of the content of the source field is not checked, which means that there can be decimal places.

  - The source field must contain a character string that can be interpreted as a number, otherwise a catchable exception of class `CX_SY_OPEN_SQL_DB` is raised.

  - If the value range in the integer places is exceeded, a catchable exception of class `CX_SY_OPEN_SQL_DB` is raised.

  - In the case of the target types `DECFLOAT16` and `DECFLOAT34`, rounding takes place to the last significant place.

  - In the case of the target types, `INT1`, `INT2`, and `INT4`, any decimal places in the source field raise an exception. In the case of the target types `INT8`, `DEC`, `CURR`, and `QUAN`, surplus decimal places are cut off without rounding.

  - In the case of the target type `FLTP`, values that cannot be represented as [binary floating point numbers](../../abap-glossary/abenbinfloat_glosry.md) are converted to the next adjacent number.

- Character-like target type

  The possible target types are `CHAR`, `SSTRING`, `NUMC`, `CLNT`, `DATS`, and `TIMS`.

  - The validity of the content of the source field is not checked.

  - The character string is written to the target field as a left-aligned string including leading blanks. If the target type is too short, it is truncated on the right. If the target field is too long, it is padded on the right with blanks.

  - There is no special handling for the special target type for numeric text, `NUMC`, and for the date/time types `DATS` and `TIMS`. It is advisable to only convert valid values.

### Source Types `DATN`, `TIMN`

- Date/time fields as target type

  The possible target type for `DATN` is `DATS` and the possible target for `TIMN` is `TIMS`.

  - The value of the date field or time field is converted to the internal value of the date type or time type.

  - The date field or time field must contain a valid date or a valid time or the initial value. If not, an exception of the class `CX_SY_OPEN_SQL_DB` is raised.

### Source Types `DATS`, `TIMS`, `CLNT`

- Character-like target type

  The possible target types are `CHAR`, `SSTRING`, and `NUMC`.

  - The validity of the content of the source field is not checked.

  - The character string is written to the target field as a left-aligned string including leading blanks. If the target type is too short, it is truncated on the right. If the target field is too long, it is padded on the right with blanks.

  - There is no special handling for the special target type for numeric text, `NUMC`. It is advisable to only convert valid values.

- Date/time fields as target type (not for `CLNT`)

  The possible target type for `DATS` is `DATN` and the possible target for `TIMS` is `TIMN`.

  - The value of the date field or time field is converted to the internal value of the date type or time type.

  - The date field or time field must contain a valid date or a valid time or the initial value. If not, an exception of the class `CX_SY_OPEN_SQL_DB` is raised.

- Numeric target type (not for `CLNT`)

  The possible target types are `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, and `FLTP`.

  - The source value is converted to the internal representation for the target type.

  - The date field or time field must contain a valid date or a valid time or the initial value. If not, an exception of the class `CX_SY_OPEN_SQL_DB` is raised.

  - In the case of the target type `FLTP`, values that start with 0 are truncated to the first number greater than 0.

### Source Types `LANG`, `UNIT`, `CUKY`

- Character-like target type

  The possible target types are `CHAR` and `SSTRING`.

  - The character string is written to the target field as a left-aligned string including leading blanks. If the target type is too short, it is truncated on the right. If the target field is too long, it is padded on the right with blanks.
