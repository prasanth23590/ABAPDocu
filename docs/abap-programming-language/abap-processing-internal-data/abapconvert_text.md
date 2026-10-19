---
title: "CONVERT TEXT"
source_file: abapconvert_text.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONVERT TEXT

## Syntax

``` abap
CONVERT TEXT text INTO SORTABLE CODE hex.  
```

## Description

The content of the operand `text` is converted to a sortable byte string and the result is assigned to the target field `hex`. The data object `text` itself remains unchanged.

The operand `text` must be of the type `c` or `string`. `text` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). The following can be specified for `hex`:

- An existing byte-like variable.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of type `xstring` is declared.

The content of `text` must contain valid characters. The sortable byte string is defined as a platform-dependent string in such a way that a size comparison or standard sorting of multiple of these fields produces an order in which the source fields `text` are sorted according to the [locale](../../abap-glossary/abenlocale_glosry.md) defined in the current [text environment](../../abap-glossary/abentext_environment_glosry.md). The text environment is set when an [internal session](../../abap-glossary/abeninternal_session_glosry.md) is opened.

If the target field `hex` is of type `x` and its length is not sufficient for the byte string, an uncatchable exception is raised. If the length is greater than that of the byte string, it is filled with hexadecimal 0 on the right. The sufficient length for all platforms is calculated as 24 times the length of `text` plus 24, but can be significantly shorter for some platforms. If `hex` is of type `xstring`, its length is adapted automatically.

## Hint

The statement `CONVERT TEXT` is mainly intended to fill an index column in internal tables where the column can be used to sort the lines of the table according to a locale. Since internal tables can also be sorted directly according to a locale using the addition `AS TEXT` of the statement [`SORT`](abapsort_itab.md), `CONVERT TEXT` is particularly suited for the following cases:

- An internal table should be sorted according to a locale and then searched binarily using the statement `READ TABLE` or using a [table expression](../../abap-glossary/abentable_expression_glosry.md).

- An internal table should be sorted more than once according to a locale. Using a sortable byte string ensures better performance than when using the addition `AS TEXT`.

- Indexes for DDIC database tables should be structured according to a locale.

- Textual comparisons are to be made between character-like data objects.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The characters *a* and *Z* are compared directly after they have been converted by `CONVERT TEXT`. While *Z* is in front of *a* for most code pages in direct comparisons, the comparison of the converted values returns the expected textual order. See also the [executable example](abensort_text_abexa.md) for `SORT` for internal tables.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
IF 'a' > 'Z'. 
  out->write_text( `'a' > 'Z'` ). 
ELSE. 
  out->write_text( `'a' < 'Z'` ). 
ENDIF. 
 
CONVERT TEXT: 'a' INTO SORTABLE CODE FINAL(ax), 
              'Z' INTO SORTABLE CODE FINAL(zx). 
 
IF ax > zx. 
  out->write_text( `'a' > 'Z'` ). 
ELSE. 
  out->write_text( `'a' < 'Z'` ). 
ENDIF. 
 
out->display( ).
```
