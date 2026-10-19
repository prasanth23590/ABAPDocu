---
title: "CDS DDL - CDS View Entity, Typed Literals"
source_file: abencds_typed_literal_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Elementary CDS Operands > CDS DDL - CDS View Entity, literal"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Typed Literals

## Syntax

``` abap
... dtype'...'  
```

[`dtype`](abencds_typing.md)

## Description

[Typed literal](../../abap-glossary/abentyped_literal_glosry.md) in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). Typed literals can be created for all [built-in ABAP Dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the exception of `LCHR`, `LRAW`, `GEOM_EWKB`, `PREC`, `ACCP`, `DF16_SCL`, `DF34_SCL`, and `VARC`. A typed literal can be used in all operand positions where this is documented.

[`dtype`](abencds_typing.md) is the name of a [built-in dictionary type](abencds_typing.md) with the type namespace `abap.` and it is followed by the character-like representation of the value in single quotes ('). Only those values can be specified that are accepted by the data type of the literal. Length and decimal places are derived from the literal value, they must not be explicitly specified.

## Hint

Typed literals should be used instead of untyped literals. They offer many advantages, such as more flexibility with regard to the data type they can have, explicit type declaration, and checking type compatibility of the value specified.

Typed literals can be divided into the following categories:

- [Typed Numeric Literals](abencds_typed_literal_v2.md#typed-numeric-literals)

- [Typed Character Literals](abencds_typed_literal_v2.md#typed-character-literals)

- [Typed Byte Literals](abencds_typed_literal_v2.md#typed-byte-literals)

- [Typed Literals for Character-Like Types with Special Semantics](abencds_typed_literal_v2.md#typed-literals-for-character-like-types-with-special-semantics)

- [Typed Date and Time Literals](abencds_typed_literal_v2.md#typed-date-and-time-literals)

- [Typed Currency and Quantity Literals](abencds_typed_literal_v2.md#typed-currency-and-quantity-literals)

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
<td><p><code class="ph codeph">abap.int1'...'</code></p>
<p><code class="ph codeph">abap.int2'...'</code></p>
<p><code class="ph codeph"> abap.int4'...'</code></p>
<p><code class="ph codeph">abap.int8'...'</code></p></td>
<td><a href="abeninteger_literal_glosry.html">Integer literal</a></td>
<td>Uninterrupted string of digits, with an optional sign + or - as a prefix. At least one digit must be specified. The value of the number must be in the value range of the respective <a href="abenddic_builtin_types.html">dictionary type</a>. An empty literal <code class="ph codeph">''</code> is not allowed.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">abap.dec'...'</code></td>
<td><a href="abenpacked_number_literal_glosry.html">Packed number literal</a></td>
<td>String of digits with a maximum of one decimal point (.). This point can be located in front of, between, or after the digits. The string can be prefixed with an optional sign + or -. At least one and no more than 31 digits can be specified. The maximum number of decimal places is 14. The length used in the memory and the number of decimal places are determined by the number of digits specified. An empty literal <code class="ph codeph">''</code> is not allowed.</td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">abap.decfloat16'...'</code></p></td>
<td><p><code class="ph codeph">abap.d16n'...'</code></p>
<p><code class="ph codeph">abap.decfloat34'...'</code></p></td>
<td><p><code class="ph codeph">abap.d34n'...'</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">abap.fltp'...'</code></td>
<td><a href="abenbinfloat_literal_glosry.html">Binary floating point literal</a></td>
<td>Mantissa followed by an optional exponent. The mantissa is a string of digits with a maximum of one decimal point (.). This point can be located in front of, between, or after the digits. The string can be prefixed with an optional sign + or -. The maximum number of valid places is 16. An empty literal <code class="ph codeph">''</code> is not allowed.</td>
</tr>
</tbody>
</table>

### Hints

- A zero with a sign + is not allowed for [integer literals](../../abap-glossary/abeninteger_literal_glosry.md) and [packed number literals](../../abap-glossary/abendecfloat_literal_glosry.md). For example, `abap.int4'+0'` is not allowed. This rule is verified by the syntax check. A zero with a sign - is allowed though.

- For all [decimal floating point literals](../../abap-glossary/abendecfloat_literal_glosry.md), there are alternative notations for the data type. This is indicated in the table above by the \| sign.

- A literal prefixed with a sign is **never** interpreted as an [arithmetic expression](abencds_arithmetic_expression_v2.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a typed numeric literal in different operand positions in a CDS view entity.

``` abap
@EndUserText.label: 'CDS view entity, numeric typed literals'

define view entity DEMO_CDS_NUMERIC_TYPED_LIT
  as select from demo_ddic_types
  
  association of many to many demo_ddic_types as _assoc
    on _assoc.d34n = abap.decfloat34'1.02'
{
  key id,
      abap.int1'1'  as int1,
      abap.dec'.15' as dec_literal,
      abap.decfloat34'123.456E789' * 100 as ArithmField,
      _assoc
}
where
  d16n = abap.d16n'123.45'
```

## Typed Character Literals

The following table describes the typed character literals:

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
<td><code class="ph codeph">abap.char'...'</code></td>
<td><a href="abentext_field_literal_glosry.html">Text field literal</a></td>
<td>String of any characters. The length of a text field literal must lie between 1 and 255 characters. An empty text field literal <code class="ph codeph">abap.char''</code> is allowed and denotes the initial value of one blank. Trailing blanks are removed but the type length includes the trimmed trailing blanks.</td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">abap.string'...'</code></p>
<p><code class="ph codeph">abap.sstring'...'</code></p></td>
<td><a href="abentext_string_literal_glosry.html">Text string literal</a></td>
<td><p>String of any characters. A typed text string literal can have a maximum of 255 characters. A typed text string literal can be empty and the typed text string literal <code class="ph codeph">abap.string''</code> represents an empty string with length 0.</p>
<p>For data type <code class="ph codeph">abap.sstring</code>, trailing blanks are removed but the type length includes the trimmed trailing blanks.</p>
<p>For data type <code class="ph codeph">abap.string</code>, trailing blanks are not removed.</p></td>
</tr>
</tbody>
</table>

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of typed character literals in a CDS view entity.

``` abap
@EndUserText.label: 'CDS view entity, typed char literals'

define view entity DEMO_CDS_CHAR_TYPED_LIT
  as select from demo_ddic_types
{
  key id,
      abap.char'aaa   '    as char_trailing_blanks,
      abap.sstring'aaa   ' as sstring_trailing_blanks,
      abap.string'aaa   '  as string_trailing_blanks,
      'aaa'                as untyped_literal
}
```

The class `CL_DEMO_CDS_CHAR_TYPED_LIT` accesses the view and demonstrates the following:

- Trailing blanks are included in the type length of text field and text string literals.

- Trailing blanks are removed from typed literals of type `CHAR` and `SSTRING`, but not from typed literals of type `STRING`.

## Typed Byte Literals

The following table describes the typed byte literals:

| **Syntax**            | **Name**                                                 | **Possible Characters**                                                                                                                                                                                       |
|-----------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abap.raw'...'`       | [Byte field literal](../../abap-glossary/abenbyte_field_literal_glosry.md) | String including the characters 0-9 and A-F. No other characters are allowed. The number of characters must be even. At least two characters must be specified. An empty literal `abap.raw''` is not allowed. |
| `abap.rawstring'...'` | `abap.rstr''`                                            | [Byte string literal](../../abap-glossary/abenbyte_string_literal_glosry.md)                                                                                                                                                    |

### Hints

- The specified characters are used to represent byte values in a hexadecimal format.

- The letters A-F must be in uppercase.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a typed byte field literal in a CDS view entity.

``` abap
@EndUserText.label: 'CDS view entity, typed byte literals'

define view entity DEMO_CDS_TYPED_BYTE_LIT
  as select from demo_ddic_types
{
  key id
}
where
  raw1 = abap.raw'AA'
```

## Typed Literals for Character-Like Types with Special Semantics

The following table describes the typed literals for character-like types with special semantics:

| **Syntax**       | **Name**                                                     | **Possible Characters**                                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abap.numc'...'` | [Numeric text literal](../../abap-glossary/abennumeric_text_literal_glosry.md) | Character string consisting of the digits 0 to 9. The length of a numeric text literal must lie between 1 and 255 characters. Empty numeric text literals `abap.numc''` or blanks within numeric text literals are not allowed. Negative values are not allowed. |
| `abap.clnt'...'` | [Client literal](../../abap-glossary/abenclient_literal_glosry.md)             | String of any characters with a length of exactly 3 characters. Blanks are not allowed. An empty literal `abap.clnt''` is not allowed.                                                                                                                           |
| `abap.lang'...'` | [Language key literal](../../abap-glossary/abenlang_key_literal_glosry.md)     | A language key literal can contain any character and it consists of exactly one character. An empty literal `abap.lang''` is not allowed. A blank space is allowed.                                                                                              |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a typed numeric text literal in a `WHERE` condition.

``` abap
@EndUserText.label: 'CDS view entity, numeric typed literals'

define view entity DEMO_CDS_NUMERIC_TEXT_TYP_LIT
  as select from demo_ddic_types
{
  key id
}
where
  numc1 = abap.numc'1'
```

## Typed Date and Time Literals

The following table describes the typed date and time literals:

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
<td><p><code class="ph codeph">abap.dats'..'</code></p>
<p><code class="ph codeph">abap.datn'...'</code></p></td>
<td><a href="abendate_literal_glosry.html">Date literal</a></td>
<td>Character string that represents a date in the format <code class="ph codeph">YYYYMMDD</code>. Must contain a valid date according to the rules for valid dates described for time stamp literals below. An empty literal <code class="ph codeph">''</code> is not allowed.</td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">abap.tims'...'</code></p>
<p><code class="ph codeph">abap.timn'...'</code></p></td>
<td><a href="abentime_literal_glosry.html">Time literal</a></td>
<td>Character string that represents a time in the format <code class="ph codeph">HHMMSS</code>. Must contain a valid time according to the rules for valid times described for time stamp literals below. An empty literal <code class="ph codeph">''</code> is not allowed.</td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">abap.utclong'...'</code></p></td>
<td><code class="ph codeph">abap.utcl'...'</code></td>
<td><a href="abentime_stamp_literal_glosry.html">Time stamp literal</a></td>
</tr>
</tbody>
</table>

### Hint

60 cannot be specified in a time, either as minutes or as seconds. In particular, this means that [leap seconds](../../abap-glossary/abenleap_second_glosry.md) cannot be specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of typed literals as operands in a CDS view entity.

``` abap
@EndUserText.label: 'CDS view entity, typed literals'

define view entity DEMO_CDS_DATE_AND_TIME_TYP_LIT
  as select from demo_ddic_types
  
  association of many to many demo_ddic_types as _assoc
    on _assoc.datn = abap.datn'20220203'
{
  key id,
      utcl_add_seconds(abap.utcl'2020-01-02 23:59:59,1234567',
                              200)             as add_seconds,

      datn_add_months(abap.datn'20200104', 13) as add_months,

      case when datn < abap.datn'20200101'
      then abap.char'<'
      else abap.char'>'
      end                                      as caseExpressionField,
      _assoc
}
where
  utcl <> abap.utcl'2018-02-21 23:59:59.1234567'
```

## Typed Currency and Quantity Literals

The following table describes the typed currency and quantity literals:

| **Syntax**       | **Name**                                                         | **Possible Characters**                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abap.curr'...'` | [Currency field literal](../../abap-glossary/abencurrency_literal_glosry.md)       | Uninterrupted string of digits with an optional sign + or - as a prefix. Cannot contain more than one decimal point (.). At least one and no more than 31 digits can be specified. Exactly two decimal places must be specified. |
| `abap.cuky'...'` | [Currency key literal](../../abap-glossary/abencurrency_key_literal_glosry.md)     | String of any characters with a maximum of 5 characters. An empty literal `abap.cuky''` is allowed and denotes five blanks.                                                                                                      |
| `abap.quan'...'` | [Quantity field literal](../../abap-glossary/abenquantity_field_literal_glosry.md) | Uninterrupted string of digits with an optional sign + or - as a prefix. Cannot contain more than one decimal point (.). At least one and no more than 31 digits can be specified. The maximum number of decimal places is 14.   |
| `abap.unit'...'` | [Unit key literal](../../abap-glossary/abenunit_key_literal_glosry.md)             | String of any characters with a maximum of 3 characters. An empty literal `''` is allowed and denotes two blanks.                                                                                                                |

If a currency or quantity field is specified in the `SELECT` list using a CDS typed literal, a reference to a currency key or unit of reference key is mandatory. This is specified with the following annotations:

- Currency key: `Semantics.amount.currencyCode`

- Unit key: `Semantics.quantity.unitOfMeasure`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

CDS view entity with currency and quantity literals.

``` abap
@EndUserText.label: 'CDS view entity, typed literals'

define view entity DEMO_CDS_CURR_AND_QUAN_TYP_LIT
  as select from demo_ddic_types
{
  key id,
      cuky,
      unit2,
      
      @Semantics.amount.currencyCode: 'cuky'
      abap.curr'123.45' as currencyField,
      
      @Semantics.quantity.unitOfMeasure: 'unit2'
      abap.quan'-200.12345' as quantityField
}
```
