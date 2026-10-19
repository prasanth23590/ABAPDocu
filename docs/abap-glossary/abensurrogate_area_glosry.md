---
title: "surrogate area"
source_file: abensurrogate_area_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# surrogate area

[General](abenabap_glossary.md)

## Definition

Subset of the characters that can be represented in [Unicode](abenunicode_glosry.md) (`U+10000` to `U+10FFFF`) that includes, for example, musical notes or special Asian characters. Addressed directly in [UTF-8](abenutf8_glosry.md) and [UTF-32](abenutf32_glosry.md); addressed using [surrogates](abensurrogates_glosry.md) in [UTF-16](abenutf16_glosry.md). [UCS-2](abenucs2_glosry.md) (supported by the ABAP programming language) does not support characters from the surrogate area. ABAP interprets a character from the surrogate area as two characters.
