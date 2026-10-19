---
title: "STATICS"
source_file: abapstatics.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# STATICS

## Deprecated Syntax

``` abap
STATICS stat [options].  
```

[`options`](abapdata.md)

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

### Description

Declares static variables `stat`. The statement `STATICS` for declaring static variables can only be used in [static methods](../../abap-glossary/abenstatic_method_glosry.md), [function modules](../../abap-glossary/abenfunction_module_glosry.md), and [subroutines](../../abap-glossary/abensubroutine_glosry.md).

The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `stat`. The syntax of the additions `options` is the same as for the statement [`DATA`](abapdata.md) for declaring regular variables. Only the additions [`READ-ONLY`](abapdata_options.md) and [`BOXED`](abapdata_boxed.md), and the declaration of [LOB handle structures](abapdata_lob_handle.md) are not possible.

As with regular local variables, variables declared using `STATICS` are only visible within their [procedure](../../abap-glossary/abenprocedure_glosry.md). However, the lifetime of a variable declared using `STATICS` corresponds to that of a global data object. The variable is created once when the [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md) is loaded into the [internal session](../../abap-glossary/abeninternal_session_glosry.md), and its content is assigned the [start value](../../abap-glossary/abenstart_value_glosry.md) of the `VALUE` addition. Calling and ending the procedure have no effect on the lifetime and content.

### Hint

In instance methods, the statement `STATICS` is not allowed. Instead, [static attributes](../../abap-glossary/abenstatic_attribute_glosry.md) of the class declared using [`CLASS-DATA`](abapclass-data.md) can be used.
