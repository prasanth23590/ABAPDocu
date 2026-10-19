---
title: "CDS DDL - CDS View Entity, Untyped Literal"
source_file: abencds_untyped_literal_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Elementary CDS Operands > CDS DDL - CDS View Entity, literal"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Untyped Literal

## Syntax

``` abap
... 'character_literal'|numeric_literal ...  
```

## Description

[Untyped literal](../../abap-glossary/abenuntyped_literal_glosry.md) in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). It is either a [character literal](../../abap-glossary/abencharacter_literal_glosry.md) or a [numeric literal](../../abap-glossary/abennumeric_literal_glosry.md):

- **Untyped character literal**

  A character literal `'character_literal'` is a character string enclosed in quotation marks. If the character string consists exclusively of digits, it is handled as a [numeric text literal](../../abap-glossary/abennumeric_text_literal_glosry.md) and the data type of the literal is [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If this is not the case, the data type is [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). When activated, the length of the corresponding field in the database system is set to a size at least as large as the actual length of the literal. A character literal can have a maximum of 1333 characters.

- **Untyped numeric literal**

  A numeric literal `numeric_literal` is a series of digits between 0 and 9. It can be directly prefixed by a `+` or `-` sign and can contain a decimal point (`.`) after the first digit. A numeric literal without a decimal point is handled as an [integer literal](../../abap-glossary/abeninteger_literal_glosry.md) of the type [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), depending on the value. A numeric literal with a decimal point is a [binary floating point literal](../../abap-glossary/abenbinfloat_literal_glosry.md) of the type [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The value of a numeric literal must be within the value range of the valid types.

Literals can be used at all operand positions where this is documented.

## Hints

- `0.5` is a valid numeric literal, but `.5` is not.

- A literal prefixed with a sign is interpreted as an [arithmetic expression](abencds_arithmetic_expression_v2.md) and can be specified in all operand positions where [arithmetic expressions](abencds_arithmetic_expression_v2.md) are allowed.

- The built-in conversion function [`FLTP_TO_DEC`](abencds_conv_func_types_v2.md) can be used to convert literals with a decimal point to a packed number.

- Literals can be of data type `CHAR`, `NUMC`, `INT1`, `INT2`, `INT4`, `INT8`, or `FLTP`. If an operand expects input of any other data type, then a literal is not possible in this operand position. There are a few exceptions to this rule, for example, some date and time conversion functions accept literal input which is then interpreted as date or time data type. These exceptions are mentioned in the documentation of the respective functions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity demonstrates various literals at operand positions while making use of the database table `SPFLI`. The class `CL_DEMO_CDS_LITERALS_VE` uses `SELECT` to access the view entity.

``` abap
@EndUserText.label: 'CDS View Entity with Literals'
define view entity DEMO_CDS_LITERALS_VE
  as select from spfli
{
  airpfrom,
  airpto,
  deptime,
  fltime,
  'Minutes' as fltime_unit,
  case countryfr
    when countryto then 'Domestic'
    else 'International'
  end       as fl_form
}
where
      fltime  < 500
  and deptime > '100000'
```
