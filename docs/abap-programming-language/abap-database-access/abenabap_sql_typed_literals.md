---
title: "ABAP SQL - Typed Literals"
source_file: abenabap_sql_typed_literals.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Operands sql_elem > ABAP SQL - literal"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Typed Literals

## Syntax

``` abap
... dtype`...`  
```

## Description

[Typed literals](../../abap-glossary/abentyped_literal_glosry.md) can be created for all [built-in ABAP Dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the exception of `LCHR`, `LRAW`, `GEOM_EWKB`, `PREC`, `ACCP`, `DF16_SCL`, and `DF34_SCL`. A typed literal can be used in read positions of ABAP SQL statements where [host variables](abenabap_sql_host_variables.md) are possible and where it is always handled as an [elementary SQL expression](abensql_elem.md) of the specified data type. It is passed without an ABAP-specific type conversion to the database and evaluated there.

`dtype` is the name of a built-in dictionary type and it is followed by the character-like representation of the value in single backquotes (\`). Only those values can be specified that are accepted by the data type of the literal.

When using the [literal operator](../../abap-glossary/abenliteral_operator_glosry.md) for concatenating two typed literals of the same type as a single character literal, the data type `dtype` is specified only once before the first subliteral. The syntax is, for example: ` INT8`123` & `456\`\`.

## Hints

- Typed literals should be used instead of untyped literals. They offer many advantages, such as more flexibility with regard to the data type they can have, explicit type declaration, and checking type compatibility of the value specified.

Typed literals can be split into the following categories:

- [Typed Numeric Literals](abenabap_sql_typed_literals.md#typed-numeric-literals)

- [Typed Character Literals](abenabap_sql_typed_literals.md#typed-character-literals)

- [Typed Byte Literals](abenabap_sql_typed_literals.md#typed-byte-literals)

- [Typed Literals for Character-Like Types with Special Semantics](abenabap_sql_typed_literals.md#typed-literals-for-character-like-types-with-special-semantics)

- [Typed Date and Time Literals](abenabap_sql_typed_literals.md#typed-date-and-time-literals)

- [Typed Currency and Quantity Literals](abenabap_sql_typed_literals.md#typed-currency-and-quantity-literals)

## Typed Numeric Literals

The following table describes the typed numeric literals:

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Name</strong></th>
<th><strong>Possible Characters</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code class="ph codeph">INT1</code>...<code class="ph codeph">`&lt;br&gt;`INT2`...`</code></p>
<p><code class="ph codeph">INT4</code>...<code class="ph codeph">`&lt;br&gt; `INT8`...`</code></p></td>
<td><a href="abeninteger_literal_glosry.html">Integer literal</a></td>
<td>Uninterrupted string of digits, with an optional sign + or - as a prefix. At least one digit must be specified. The value of the number must be in the value range of the respective <a href="abenddic_builtin_types.html">dictionary type</a>. An empty literal ```` is not allowed.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">DEC</code>...``</td>
<td><a href="abenpacked_number_literal_glosry.html">Packed number literal</a></td>
<td>String of digits with a maximum of one decimal point (.). This point can be located in front of, between, or after the digits. The string can be prefixed with an optional sign + or -. At least one and no more than 31 digits can be specified. The maximum number of decimal places is 14. The length used in the memory and the number of decimal places are determined by the number of digits specified. An empty literal ```` is not allowed.</td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">DECFLOAT16</code>...<code class="ph codeph">`&lt;br&gt; | `D16N`...`</code></p>
<p><code class="ph codeph">DF16_RAW</code>...<code class="ph codeph">`&lt;br&gt; | `D16R`...`</code></p>
<p><code class="ph codeph">DECFLOAT34</code>...<code class="ph codeph">`&lt;br&gt; | `D34N`...`</code></p>
<p><code class="ph codeph">DF34_RAW</code>...<code class="ph codeph">`&lt;br&gt; | `D34R`...`</code></p></td>
<td><a href="abendecfloat_literal_glosry.html">Decimal floating point literal</a></td>
<td>Mantissa followed by an optional exponent. The mantissa is a string of digits with a maximum of one decimal point (.). This point can be located in front of, between, or after the digits. The string can be prefixed with an optional sign + or -. Length restrictions, typing conventions, and scaling rules of the respective <a href="abenddic_builtin_types.html">dictionary type</a> apply. An empty literal ```` is not allowed.</td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">DF16_DEC</code>...<code class="ph codeph">`&lt;br&gt; | `D16D`...`</code></p>
<p><code class="ph codeph">DF34_DEC</code>...<code class="ph codeph">`&lt;br&gt; | `D34D`...`</code></p></td>
<td><a href="abendecfloat_literal_glosry.html">Decimal floating point literal</a></td>
<td>The rules for <a href="abenpacked_number_literal_glosry.html">packed number literals</a> (see above) apply. Furthermore, <code class="ph codeph">DF16_DEC</code> can have a maximum length of 16 digits. An empty literal ```` is not allowed.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">FLTP</code>...``</td>
<td><a href="abenbinfloat_literal_glosry.html">Binary floating point literal</a></td>
<td>Mantissa followed by an optional exponent. The mantissa is a string of digits with a maximum of one decimal point (.). This point can be located in front of, between, or after the digits. The string can be prefixed with an optional sign + or -. The maximum number of valid places is 16. An empty literal ```` is not allowed.</td>
</tr>
</tbody>
</table>

### Hints

- For all numeric literals, the rule applies that not more than one zero is allowed on the left side of the decimal point. Thus, `DEC`00.00`` ` is not allowed and `INT1`00` `` as [integer literal](../../abap-glossary/abeninteger_literal_glosry.md) is not allowed either. This rule is verified by the syntax check.

- A zero with a sign + or - is not allowed for [integer literals](../../abap-glossary/abeninteger_literal_glosry.md) and [packed number literals](../../abap-glossary/abendecfloat_literal_glosry.md). For example, `INT4`-0\`\` is not allowed. This rule is verified by the syntax check.

- For all [decimal floating point literals](../../abap-glossary/abendecfloat_literal_glosry.md), there are alternative notations for the data type. This is indicated in the table above by the \| sign.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a typed numeric literal in a `WHERE` condition.

``` abap
SELECT * 
       FROM demo_ddic_types 
       WHERE int8 = int8`32984723948723` 
       INTO TABLE @FINAL(result).
```

## Typed Character Literals

The following table describes the typed character literals:

| **Syntax**                          | **Name**                                                   | **Possible Characters**                                                                                                                                                                                                                                                                                                          |
|-------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CHAR`...\`\`                       | [Text field literal](../../abap-glossary/abentext_field_literal_glosry.md)   | String of any characters. The length of a text field literal must lie between 1 and 255 characters. An empty text field literal \`CHAR\`\`\` is allowed and denotes the initial value of one blank. To represent a backquote in a text field literal, two consecutive backquotes must be specified.                              |
| `STRING`...`` `<br>`SSTRING`...` `` | [Text string literal](../../abap-glossary/abentext_string_literal_glosry.md) | String of any characters. A typed text string literal can have a maximum of 255 characters. A typed text string literal can be empty and the typed text string literal \`STRING\`\`\` represents an empty string with length 0. To represent a backquote in a text string literal, two consecutive backquotes must be specified. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a typed character literal in a `WHERE` condition.

``` abap
SELECT * 
      FROM demo_ddic_types 
      WHERE char10 = char`hallo` 
      INTO TABLE @FINAL(result).
```

## Typed Byte Literals

The following table describes the typed byte literals:

| **Syntax**         | **Name**                                                   | **Possible Characters**                                                                                                                                                                                      |
|--------------------|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RAW`...\`\`       | [Byte field literal](../../abap-glossary/abenbyte_field_literal_glosry.md)   | String including the characters 0-9 and A-F. No other characters are allowed. The number of characters must be even. At least two characters must be specified. An empty literal \`RAW\`\`\` is not allowed. |
| `RAWSTRING`...\`\` | [Byte string literal](../../abap-glossary/abenbyte_string_literal_glosry.md) | String including the characters 0-9 and A-F. No other characters are allowed. The number of characters must be even. The empty byte string literal \`RAWSTRING\`\`\` represents an empty byte string.        |

### Hints

- The specified characters are used to represent byte values in a hexadecimal format.

- The letters A-F must be in uppercase.

- If [untyped character literals](abenabap_sql_untyped_literals.md) are used for hexadecimal values, the number of characters may be odd and the value is padded on the right with hexadecimal 0 in accordance with the [conversion rules](../abap-processing-internal-data/abenconversion_type_c.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a typed byte field literal in a `WHERE` condition.

``` abap
SELECT * 
      FROM demo_ddic_types 
      WHERE raw1 = raw`11` 
      INTO TABLE @FINAL(result).
```

## Typed Literals for Character-Like Types with Special Semantics

The following table describes the typed literals for character-like types with special semantics:

| **Syntax**    | **Name**                                                     | **Possible Characters**                                                                                                                                                                                                        |
|---------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NUMC`...\`\` | [Numeric text literal](../../abap-glossary/abennumeric_text_literal_glosry.md) | Character string consisting of the digits 0 to 9. The length of a numeric text literal must lie between 1 and 255 characters. Empty numeric text literals \`NUMC\`\`\` or blanks within numeric text literals are not allowed. |
| `CLNT`...\`\` | [Client literal](../../abap-glossary/abenclient_literal_glosry.md)             | String of any characters with a length of exactly 3 characters. Trailing blanks are not allowed. An empty literal \`CLNT\`\`\` is allowed and denotes the initial value of three blanks.                                       |
| `LANG`...\`\` | [Language key literal](../../abap-glossary/abenlang_key_literal_glosry.md)     | A language key literal can contain any character and it consists of exactly one character. A blank space is not allowed. An empty literal \`LANG\`\`\` is allowed and denotes a blank.                                         |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a typed numeric text literal in a `WHERE` condition.

``` abap
SELECT * 
      FROM demo_ddic_types 
      WHERE numc1 = numc`1234` 
      INTO TABLE @FINAL(result).
```

## Typed Date and Time Literals

The following table describes the typed date and time literals:

| **Syntax**                     | **Name**                                                 | **Possible Characters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DATS`...`` `<br>`DATN`...` `` | [Date literal](../../abap-glossary/abendate_literal_glosry.md)             | Character string that represents a date in the format `YYYYMMDD`. Must contain a valid date according to the rules for valid dates described for time stamp literals below. An empty string \`\`\`\` is not allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `TIMS`...`` `<br>`TIMN`...` `` | [Time literal](../../abap-glossary/abentime_literal_glosry.md)             | Character string that represents a time in the format `HHMMSS`. Must contain a valid time according to the rules for valid times described for time stamp literals below. An empty literal \`\`\`\` is not allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `UTCLONG`...\`\`               | [Time stamp literal](../../abap-glossary/abentime_stamp_literal_glosry.md) | Character string that represents an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) in the format `YYYY-MM-DDTHH:MM:SS,SSSSSSS`, precise to 100 nanoseconds. `YYYY-MM-DD` consists of eight digits separated by hyphens. They must represent dates that are valid in accordance with the calendar rules: `YYYY` (year): 0001 to 9999, `mm` (month): 01 to 12, `DD` (day): 01 to 31. *1582-10-05* to *1582-10-14* are skipped due to the conversion from the Julian to the Gregorian calendar. The letter *T* between the date and the time must be specified exactly as it is here. `HH:MM:SS,SSSSSSS` consists of digits separated by colons and a comma. They must represent a time in a 24-hour range in the format `HHMMSS`: 00 to 23 for `HH` (hours) and 00 to 59 for `MM` (minutes) and 00 to 59 for `SS,SSSSSSS` (seconds with a maximum of seven decimal places). More than seven decimal places can be specified, however the digits after the seventh decimal place must be *0*. The comma does not have to be specified. No other characters are allowed. An empty literal \`UTCLONG\`\`\` is allowed and denotes the initial value. |

### Hint

60 cannot be specified in a time, either as minutes or as seconds. In particular, this means that [leap seconds](../../abap-glossary/abenleap_second_glosry.md) cannot be specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of typed literals as operands in [SQL date and time functions](abenabap_sql_date_time_functions.md).

``` abap
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS 
         utcl_add_seconds( utclong`2020-04-01T12:01:01,2`,50 ) AS utcl, 
         datn_add_months( datn`17890101`,15 ) AS add_months, 
         tims_is_valid( tims`121300` ) AS tims 
       INTO @FINAL(result).
```

## Typed Currency and Quantity Literals

The following table describes the typed currency and quantity literals:

| **Syntax**    | **Name**                                                         | **Possible Characters**                                                                                                                                                                                                                                                                                                                                                                         |
|---------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CURR`...\`\` | [Currency field literal](../../abap-glossary/abencurrency_literal_glosry.md)       | Uninterrupted string of digits with an optional sign + or - as a prefix. Cannot contain more than one decimal point (.). At least one and no more than 31 digits can be specified. The maximum number of decimal places is 14. Not more than one zero is allowed on the left side of the decimal point. A zero with a sign + or - is not allowed. An empty literal \`CURR\`\`\` is not allowed. |
| `CUKY`...\`\` | [Currency key literal](../../abap-glossary/abencurrency_key_literal_glosry.md)     | String of any characters with a maximum of 5 characters. Trailing blanks are not allowed. An empty literal \`CUKY\`\`\` is allowed and denotes five blanks.                                                                                                                                                                                                                                     |
| `QUAN`...\`\` | [Quantity field literal](../../abap-glossary/abenquantity_field_literal_glosry.md) | Uninterrupted string of digits with an optional sign + or - as a prefix. Cannot contain more than one decimal point (.). At least one and no more than 31 digits can be specified. The maximum number of decimal places is 14. Not more than one zero is allowed on the left side of the decimal point. A zero with a sign + or - is not allowed. An empty literal \`QUAN\`\`\` is not allowed. |
| `UNIT`...\`\` | [Unit key literal](../../abap-glossary/abenunit_key_literal_glosry.md)             | String of any characters with a maximum of 3 characters. An empty literal \`UNIT\`\`\` is allowed and denotes two blanks.                                                                                                                                                                                                                                                                       |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a typed currency field literal in a `WHERE` condition.

``` abap
SELECT * 
      FROM demo_ddic_types 
      WHERE curr10_2 = curr`123.43` 
      INTO TABLE @FINAL(result).
```
