---
title: "AMDP - Macros"
source_file: abenamdp_macros.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Macros

## Syntax

``` abap
... "$ABAP.macro( ... )" ...  
```

## Description

Specifies an [AMDP macro](../../abap-glossary/abenamdp_macro_glosry.md) in an AMDP method, which is implemented in [SQLScript](abenamdp_hdb_sqlscript.md). An AMDP macro is specified in double quotation marks and always introduced with `$ABAP`. The macro itself is specified with `macro`. The relevant parameters for the chosen macro can be specified in the parentheses. The format for `$ABAP` is case-sensitive. The format for `macro` is not case-sensitive.

The ABAP runtime framework replaces an AMDP macro, including the quotation marks, during the implementation on the database in accordance with the rule for the relevant macro. The following macros are currently predefined:

- [`$ABAP.type`](abenamdp_abap_types.md) for ABAP types

No other macros can be specified. In particular, no custom macros can be defined.

## Hints

- The syntax for macros is currently only possible in the implementation language [SQLScript](abenamdp_hdb_sqlscript.md).

- Macros that are specified in comments or in single quotation marks are not replaced.
