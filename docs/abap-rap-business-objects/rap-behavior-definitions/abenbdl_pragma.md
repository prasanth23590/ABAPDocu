---
title: "RAP BDL - Pragmas"
source_file: abenbdl_pragma.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP BDL - Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP BDL - Pragmas

## Syntax

``` abap
... ##code...  
```

## Description

Pragmas can be used to hide [syntax check](../../abap-glossary/abensyntax_check_glosry.md) warnings.

A pragma is not case-sensitive and does not contain blanks. A pragma starts with two hash characters (`##`), followed by the pragma code `code`. The pragma code determines the effect.

A pragma applies to the current statement, that is to the statement that ends at the next semicolon ( *;* ) or curly bracket ( *{* ), or ( *}*).

Pragmas can be used at specific positions in the source code, namely:

- At the start of a line, after any number of blanks

- At the end of a line, only followed by a semicolon ( *;* ), or a curly bracket ( *{* ), or ( *}* ).

- *Not* before, after, or within parentheses `( ... )`.

  Multiple pragmas may be positioned one after another, separated by blanks, at allowed positions.

Pragmas used at a wrong position have no effect.

**Note:** The pragma must be placed within the statement, specifically at the part the warning refers to.

In the example below, a warning is issued for the `_child` association. Therefore, the pragma `##DRAFT_ASSOC` must be specified for `_child` directly in the statement (`association _child ##DRAFT_ASSOC { create; }`), not at the end of the line after the brackets, for example. Another syntax warning would be raised for the example specification `action MyAction parameter DEMO_CDS_ABSTRACT_ROOT ##TYPE;`, if the pragma `##TYPE` was not specified. The syntax warning does not refer to the action itself, but rather to the type specified. Therefore, the pragma must be specified in the statement, positioning it next to the type directly.

## Hint

The long text of the error message provides the information on which pragma can be used to hide a specific syntax check warning.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following BDEF uses different pragmas to suppress syntax check warnings:

- `##DRAFT_ASSOC`: Suppresses a syntax check warning that is issued because the association `_child` is not draft-enabled.

- `##TYPE`: Suppresses a syntax check warning that is issued because the action parameter `DEMO_CDS_ABSTRACT_ROOT` is a deep structure, but it is only used as a flat parameter in the current BDEF.

``` abap
managed implementation in class bp_demo_rap_pragma unique;
strict ( 2 );
with draft;

define behavior for DEMO_RAP_PRAGMA alias Root
persistent table demo_dbtab_root
draft table demo_dbtab_d6
lock master
total etag lchg_date_time
authorization master ( none )

{
  create;
  update;
  delete;
  association _child ##DRAFT_ASSOC { create; }

  action MyAction parameter DEMO_CDS_ABSTRACT_ROOT ##TYPE;

  field ( readonly : update ) key_field;
  field ( readonly ) lchg_date_time;

  draft action Edit;
  draft action Activate optimized;
  draft action Discard;
  draft action Resume;
  draft determine action Prepare;
}

define behavior for DEMO_RAP_PRAGMA_CHILD alias Child
persistent table demo_dbtab_child
draft table demo_draft_ch6
lock dependent by _parent
authorization dependent by _parent
//etag master <field_name>
{
  update;
  delete;
  field ( readonly ) key_field, key_field_child;
  association _parent ##DRAFT_ASSOC;

}
```
