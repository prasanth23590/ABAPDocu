---
title: "ABAP Character Set"
source_file: abencharacter_sets.html
section: "ABAP Programming Language > ABAP - Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Character Set

Application Server ABAP supports only [Unicode systems](../../abap-glossary/abenunicode_system_glosry.md) in the current release.

- A Unicode system is an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that is based on Unicode character representation with a [code page](../../abap-glossary/abencodepage_glosry.md) for [Unicode](../../abap-glossary/abenunicode_glosry.md) and also on a corresponding operating system and database.

- A non-Unicode system is an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) with [code pages](../../abap-glossary/abencodepage_glosry.md) for single-byte code and double-byte code. Non-Unicode systems are no longer supported in the current release.

[Unicode](../../abap-glossary/abenunicode_glosry.md) (ISO/IEC 10646) with the character set [UCS](../../abap-glossary/abenucs_glosry.md) covers all existing characters. For the Unicode character set, there are different Unicode character representations, such as [UTF](../../abap-glossary/abenutf_glosry.md), in which a character can occupy between one and four bytes, or [UCS-2](../../abap-glossary/abenucs2_glosry.md), where one character occupies two bytes.

- [UTF-16](../../abap-glossary/abenutf16_glosry.md) is the [system code page](../../abap-glossary/abensystem_codepage_glosry.md) of a Unicode system. It covers all characters of the Unicode standard.

- The ABAP programming language supports the character representation [UCS-2](../../abap-glossary/abenucs2_glosry.md), which represents a subset of the characters represented by UTF-16. I covers the Basic Multilingual Plane (BMP) of the Unicode standard but not the characters of the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md).

The restriction to UCS-2 in ABAP means that a character is always assumed to have the length of two bytes. Every valid UTF-16 encoded character string is also a valid UCS-2 encoded string (potentially representing different characters), but not every valid UCS-2 encoded string is a valid UTF-16 encoded string, because high and low surrogates can occur that are not part of a surrogate pair. This generally only causes problems if character strings are truncated in the middle of a character representation from the UTF-16 surrogate area, or if individual characters of character sets are compared in character string processing. Also transformations of strings to external formats that are expecting valid Unicode characters, as for example XML, can lead to exceptions.

To be used in a [Unicode system](../../abap-glossary/abenunicode_system_glosry.md), an ABAP program must have the ABAP language version [Standard ABAP](../../abap-glossary/abenstandard_abap_glosry.md). Programs with the obsolete language version Non-Unicode ABAP can no longer be used in a Unicode system.

## Hints

- The attribute `CHARSIZE` of system class [`CL_ABAP_CHAR_UTILITIES`](../abap-processing-internal-data/abencl_abap_char_utilities.md) contains the number of bytes occupied by a character in the current system.

- For regular expressions in [PCRE syntax](../abap-processing-internal-data/abenregex_pcre_syntax.md), it can be defined whether valid UTF-16 character strings are expected or not.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The UTF-8 representation of the Unicode character `EXTRATERRESTRIAL ALIEN` is converted to its UTF-16 representation and stored in the text field `surrogate_pair`. Although the Unicode character `EXTRATERRESTRIAL ALIEN` is not contained in the Basic Multilingual Plane (BMP) of the Unicode standard its UTF-16 representation (a [surrogate pair](../../abap-glossary/abensurrogate_pair_glosry.md)) can still be stored as an ABAP character string. But almost every string operation in ABAP handles the string simply as two UCS-2 characters with string length 2. This can cause problems when the data is to be interpreted as UTF-16 outside ABAP. The results of the two offset/length accesses produce text fields of length 1 with hexadecimal content `3DD8` and `7DDC`. Since high and low surrogates can only be part of a surrogate pair and cannot appear on their own in a valid UTF-16 string, the text fields contain invalid UTF-16 strings. In a regular expression in [PCRE syntax](../abap-processing-internal-data/abenregex_pcre_syntax.md) that is introduced with `(*UTF)`, valid UTF-16 strings are expected and an exception occurs.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA surrogate_pair TYPE c LENGTH 2. 
FIELD-SYMBOLS <hex1> TYPE x. 
FIELD-SYMBOLS <hex2> TYPE x. 
 
surrogate_pair = cl_abap_codepage=>convert_from( 
  codepage = 'UTF-8' 
  source    = CONV xstring( 'F09F91BD' ) ). 
                            "U+1F47D, EXTRATERRESTRIAL ALIEN 
 
out->write_text( surrogate_pair ). 
 
FINAL(substring1) = surrogate_pair+0(1). 
FINAL(substring2) = surrogate_pair+1(1). 
 
ASSIGN substring1 TO <hex1> CASTING. 
ASSIGN substring2 TO <hex2> CASTING. 
out->write_text( |{ <hex1> } { <hex2> }| ). 
 
TRY. 
    IF matches( val = substring1 pcre = `.` ). 
       out->write_text( `PCRE without (*UTF) matches` ). 
    ENDIF. 
    IF matches( val = substring1 pcre = `(*UTF).` ). 
       out->write_text( `PCRE with (*UTF) matches` ). 
    ENDIF. 
  CATCH cx_sy_matcher INTO FINAL(exc). 
    out->write_text( exc->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```
