---
title: "CDS DDL - DDIC-Based View, literal"
source_file: abencds_literal_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Elementary CDS Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, literal

## Syntax

``` abap
... [#|:domain.]'character_literal'|numeric_literal ...  
```

### Addition

[`... #|:domain.`](abencds_literal_v1.md#addition)

## Overview

### Description

Literal in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). It is either a character literal or a numeric literal:

- A character literal `'character_literal'` is a character string enclosed in quotation marks. If the character string consists exclusively of digits, the data type of the literal is [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If this is not the case, the data type is [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). When activated, the length of the corresponding field in the database system is set to a size at least as large as the actual length of the literal. A character literal can have a maximum of 1333 characters.

- A numeric literal `numeric_literal` is a series of digits between 0 and 9. It can be directly prefixed by a `+` or `-` sign and can contain a decimal point (`.`) after the first digit. A numeric literal without a decimal point is handled as a field of the type [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), depending on the value. A numeric literal with a decimal point is floating point number of type [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The value of a numeric literal cannot be greater than the value range of the valid types.

Literals can be used at all operand positions where this is documented.

``` abap
Escape characters: 
A single quote \('\) must be used to escape a single quote \(`'...''...'`\) in a character literal\.
```

### Hints

- `0.5` is a valid numeric literal, but `.5` is not.

- Byte-like literals are currently not supported.

- A literal prefixed with a sign is interpreted as an [arithmetic expression](abencds_arithmetic_expression_v1.md) and can be specified in all operand positions where [arithmetic expressions](abencds_arithmetic_expression_v1.md) are allowed.

- The built-in conversion function [`FLTP_TO_DEC`](abencds_conv_func_types_v1.md) can be used to convert literals with a decimal point to a packed number.

- It is **not** possible to specify a literal in an operand position that expects a type-compliant operand in a data type that is not numeric or character-like, such as `UTCLONG`.

  In the following example, the operand after `when` cannot be specified as literal and therefore, the syntax is invalid: `case utcl_current( ) when '2020020720162345' then 'ok' else 'no' end as demo`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view demonstrates various literals at operand positions.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CORPSO_VW'
define view demo_corp_sales_order
  as select from snwd_so
  association [1..1] 
    to snwd_bpa as _partner 
      on snwd_so.buyer_guid = _partner.node_key
{
  key snwd_so.so_id              as sales_order_id,
      snwd_so.buyer_guid,
      _partner.bp_id             as corporation_id,
      _partner.company_name      as corporation_name,
      'corporation'              as legal_form,
      @Semantics.currencyCode
      cast( 'EUR' as abap.cuky ) as currency_code,
      @Semantics.amount.currencyCode: 'currency_code'
      snwd_so.gross_amount       as sales_order_gross_amount
}
where
      _partner.legal_form   = 'Inc.' //Corporations only
  and snwd_so.currency_code = 'EUR'
  and snwd_so.gross_amount  > 100000
```

## Addition

`... #|:domain.`

### Description

In certain operand positions, a literal can be prefixed with a name of a [DDIC domain](../../abap-glossary/abendomain_glosry.md) `domain` introduced using the character `#` or `:` and separated by a period (`.`). In this case, a check is made to verify whether the value of the literal is defined as a [fixed value](../../abap-glossary/abenfixed_value_glosry.md) in the [value range](../../abap-dictionary-ddic/ddic-data-types/abenddic_domains_sema.md) of the domain. If this is not the case or if the domain does not exist as an active domain, a syntax check warning occurs. Apart from this, the literal is handled like a regular literal.

A domain can be specified in front of a literal in the following operand positions:

- Element of the [`SELECT` list](abencds_select_list_v1.md)

- Right side of a [comparison condition](abencds_cond_expr_comp_v1.md)

- Parameters passed to [built-in functions](abencds_builtin_functions_v1.md)

### Hints

- In the case of character literals consisting only of letters, numbers, underscores (`_`), and slashes (`/`) and that start with a letter, underscore, or slash, the quotation marks can be omitted after the domain.

  - `#domain.xXx` has the same semantics as

  - `#domain.'xXx'`.

- Numeric literals can only be checked using fixed values of numeric domains.

- Currently, not all potential literal values can be represented as fixed values of domains. For example, a numeric domain can only have positive integers as fixed values and there are no fixed values for domains of type `FLTP`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Fixed value `EXA` of the domain `ABDOCTYPE` as the operand of the `WHERE` condition of a view.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_ABAPDOCTREE'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_abapdoc_tree as
select from abapdocu_tree
       { * }
       where node_type = #ABDOCTYPE.'EXA';
```
