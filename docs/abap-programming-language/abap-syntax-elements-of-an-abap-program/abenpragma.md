---
title: "Pragmas"
source_file: abenpragma.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > Program Directives"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Pragmas

## Syntax

``` abap
... ##code[par][par]...  
```

## Description

Pragmas are [program directives](../../abap-glossary/abenprogram_directive_glosry.md) that can be used to hide warnings from various check tools.

A pragma is not case-sensitive and does not contain blanks. The pragma code (`code`) determines the effect and parameters (`par`) further restrict the effect if necessary.

A warning is affected by a pragma if all the parameters *specified* match the *concrete* parameters. The concrete parameters can also be taken from the long text of the message. *Compulsory* parameters are underlined in the long text and must not be omitted. Non-compulsory parameters are optional. Optional parameters can be omitted using empty parentheses `[]` at the appropriate position or by completely omitting an end part.

A pragma applies to the current statement, that is to the statement that ends at the next `.` or `,`. Pragmas in front of the`:` of a chained statement apply to the entire chained statement.

Pragmas must only be used at specific positions in the source code for reasons of readability, namely:

- At the *start* of a line, after any number of blanks

- At the *end* of a line, only followed by `.`, `,`, or `:`.

- *Not* *after* `.`, `,`, or `:`.

  Multiple pragmas may be positioned one after another, separated by blanks, at allowed positions.

Unknown, formally incorrect, or incorrectly parameterized pragmas produce a syntax warning. Incorrectly positioned pragmas for warnings in the syntax check have no effect.

## Hints

- Find [RAP Behavior Definition Language](../../abap-glossary/abenbdl_glosry.md)-specific Pragma rules [here](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_pragma.md).

- For a system check warning, the existence of a pragma and its rules can be checked using the *long text of the message*, which in this case always exists. The description of a message in the extended program check also indicates the pragma that can be used to hide it.

- A pragma in a type definition made using [`TYPES`](../abap-declarations/abaptypes.md), for example, to hide the warning for redundant secondary keys of table types, can also be applied to data declarations using [`DATA`](../abap-declarations/abapdata.md) in the case of non-generic types and related statements that reference the data type using [`TYPE`](../abap-declarations/abapdata_referring.md). If a reference is made to a generic data type defined using `TYPES`, that is, a table type for which no primary table key is defined, a pragma specified there is not applied to the data declaration, since it uses a full table type implicitly and the pragma must potentially be specified again.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following is an example of a pragma for syntax check warnings:

\##SHADOW

This pragma can be used to hide a syntax warning in a method definition that reports the hiding of a built-in function. The pragma has an optional parameter in which the name of the function can be specified as well.

\##SHADOW\[SUBSTRING\]

A warning about *SUBSTRING* is suppressed using one of the following:

- `##SHADOW`

- `##SHADOW[SUBSTRING]`

- `##SHADOW[]`

but not using `SHADOW[FIND]`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An example of pragmas for hiding warnings from the extended program check is:

DATA TEXT TYPE STRING \##needed.

text = 'Hello Pragmas' \##no_text.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In some executable examples for key accesses to internal tables ([read](../abap-processing-internal-data/abenread_itab_using_key_abexa.md), delete), syntax warnings are hidden by the associated pragma. The pragmas are found in the long text of the syntax warnings.
