---
title: "CDS DDL - DDIC-Based View, cast_expr, Conversion Rules"
source_file: abencds_cast_expression_rules_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, cast_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cast_expr, Conversion Rules

The following sections describe the conversion rules for [cast expressions](abencds_cast_expression_v1.md) in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md).

- [Numeric Source Type](abencds_cast_expression_rules_v1.md#numeric-source-type)

  - [Source Types `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, CURR, QUAN, DECFLOAT16, and DECFLOAT34](abencds_cast_expression_rules_v1.md#source-types-int1-int2-int4-int8-dec-curr-quan-decfloat16-and-decfloat34)

- [Character-Like Source Type](abencds_cast_expression_rules_v1.md#character-like-source-type)

  - [Source Types `CHAR` and `SSTRING`](abencds_cast_expression_rules_v1.md#source-types-char-and-sstring)

  - [Source Type `NUMC`](abencds_cast_expression_rules_v1.md#source-type-numc)

  - [Source Types `DATS` and `TIMS`](abencds_cast_expression_rules_v1.md#source-types-dats-and-tims)

  - [Source Types `CLNT`, `LANG`, `UNIT`, and `CUKY`](abencds_cast_expression_rules_v1.md#source-types-clnt-lang-unit-and-cuky)

Data types that cannot be converted to each other are not listed below. In these cases, casts are either not possible or casting can only be done between operands of the same type. If the source type and the target type are technically identical, the content is transferred without being converted.

## Numeric Source Type

### Source Types `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, CURR, QUAN, DECFLOAT16, and DECFLOAT34

- Numeric target type

  - Possible target types for all numeric source types: `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `QUAN`, `DECFLOAT16`, and `DECFLOAT34`.

  - Possible target types for all numeric source types except `DECFLOAT16` and `DECFLOAT34`: `CURR` and `FLTP`.

  - The source value is converted to the internal representation of the target type.

  - If the value range is exceeded, an exception is raised that can be caught in ABAP using `CX_SY_OPEN_SQL_DB`. In the case of the target types `DEC`, `CURR`, and `QUAN`, this applies to the integer digits and any surplus decimal places are cut off without rounding.

  - In the case of the target types `DEC`, `CURR`, and `QUAN`, a syntax check warning is produced if it is known statically that an exception might be raised.

  - In the case of the target type `FLTP`, values that cannot be represented as [binary floating point numbers](../../abap-glossary/abenbinfloat_glosry.md) are converted to the next adjacent number.

- Character-like target type (not for `DECFLOAT16` and `DECFLOAT34`)

  - The possible target types are `CHAR`, `SSTRING`, and `CLNT` (only for `INT1`).

  - The number value is converted to a character string in [mathematical notation](../../abap-glossary/abenmathematical_notation_glosry.md) and is left-aligned.

  - The length of the target type must be enough for all potential values in the source type including the sign and decimal separator.

### Hint

When the source type `DEC` is converted to a character-like target type, it depends on the database whether non-relevant zeros are included before and after the decimal separator.

## Character-Like Source Type

### Source Types `CHAR` and `SSTRING`

- Character-like target type

  - The possible target types are `CHAR`, `SSTRING`, `NUMC`, `CLNT`, `LANG`, `DATS`, `TIMS`, `UNIT`, `CUKY`, and `ACCP`.

  - The character string is written to the target field as a left-aligned string including leading blanks. If the target type is too short, the string is truncated on the right and a syntax check warning occurs. If the target field is too long, it is padded on the right with blanks.

  - There is no special handling for the special target type for numeric text `NUMC` and for the date/time types `DATS` and `TIMS`. It is advisable to only convert valid values. In the case of the target type `NUMC`, the built-in function [`LPAD`](abencds_sql_functions_character_v1.md) can be used to create leading zeros.

  - The target type `ACCP` must be specified using a data element. The data element must have the same length as the data type `ACCP`.

### Source Type `NUMC`

- Numeric target type

  - The possible target types are `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, and `FLTP`.

  - The validity of the content of the source field is not checked, which means that there can be decimal places.

  - The source field must contain a character string that can be interpreted as a number. If not, an exception is raised that can be caught in ABAP using `CX_SY_OPEN_SQL_DB`.

  - If the value range in the integer digits is exceeded, an exception is raised that can be caught in ABAP using `CX_SY_OPEN_SQL_DB`.

  - In the case of the target types `DECFLOAT16` and `DECFLOAT34`, rounding takes place to the last significant place.

  - In the case of the target types `INT1`, `INT2`, and `INT4`, any decimal places in the source field raise an exception. In the case of the target types `INT8`, `DEC`, `CURR`, and `QUAN`, surplus decimal places are cut off without rounding.

  - In the case of the target type `FLTP`, values that cannot be represented as [binary floating point numbers](../../abap-glossary/abenbinfloat_glosry.md) are converted to the next adjacent number.

- Character-like target type

  - The possible target types are `CHAR`, `SSTRING`, `NUMC`, `CLNT`, `ACCP`, `DATS`, and `TIMS`.

  - The validity of the source field is not checked.

  - The character string is written to the target field as a left-aligned string including leading blanks. If the target type is too short, the string is truncated on the right and a syntax check warning occurs. If the target field is too long, it is padded on the right with blanks.

  - The lengths of the source type and target type must match for the special target type for numeric text `NUMC` and for the date/time types `DATS` and `TIMS`. No other special handling takes place. It is advisable to only convert valid values. In the case of the target type `NUMC`, the built-in function [`LPAD`](abencds_sql_functions_character_v1.md) can be used to create leading zeros.

### Source Types `DATS` and `TIMS`

- Character-like target type

  - The possible target types are `CHAR` and `SSTRING`.

  - The validity of the source field is not checked.

  - The character string is written to the target field as a left-aligned string including leading blanks. If the target type is too short, the string is truncated on the right and a syntax check warning occurs. If the target field is too long, it is padded on the right with blanks.

  - The value of the character-like date field or time field is converted to the internal value of the date type or time type.

  - The character-like date field or time field must contain a valid date or a valid time or the initial value. If not, an exception of the class `CX_SY_OPEN_SQL_DB` is raised.

### Source Types `CLNT`, `LANG`, `UNIT`, and `CUKY`

- Character-like target type

  - The possible target types are `CHAR` and `SSTRING`, which need to be specified using data elements.

  - The validity of the source field is not checked.

  - The character string is written to the target field as a left-aligned string including leading blanks. If the target type is too short, the string is truncated on the right and a syntax check warning occurs. If the target field is too long, it is padded on the right with blanks.
