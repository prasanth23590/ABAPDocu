---
title: "DATA, BEGIN OF struc"
source_file: abapdata_struc.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, BEGIN OF struc

## Syntax

``` abap
DATA BEGIN OF struc [READ-ONLY].   
  ...   
   INCLUDE TYPE|STRUCTURE ...   
  ...   
DATA END OF struc.  
```

[`[READ-ONLY]`](abapdata_options.md) · [`INCLUDE TYPE|STRUCTURE ...`](abapinclude_type.md)

## Description

Declaration of a new [structure](../abap-data-types-and-data-objects/abendata_objects_structure.md) `struc`. This is introduced using a `DATA` statement with the addition `BEGIN OF` and must end with a `DATA` statement with the addition `END OF`.

The following can be included between these `DATA` statements:

- Any `DATA` statements, particularly further closed structures.

- The statements [`INCLUDE TYPE`](abapinclude_type.md) and [`INCLUDE STRUCTURE`](abapinclude_type.md)

The meaning of these statements is the same as in the definition of structured data types in the section [`TYPES` - `BEGIN OF`](abaptypes_struc.md). However, here it is used to create a bound structured data type. No structure can be created without at least one component.

A component of `struc` cannot be declared by referencing `struc` itself. If the name `struc` is specified after `LIKE` in the declaration of a component, a search is performed for the next object with this name in a higher [visibility section](../abap-data-types-and-data-objects/abenlifetime_and_visibility.md) and used if found. If there is no more global object with this name, a syntax error occurs.

## Hints

- The addition [`READ-ONLY`](abapdata_options.md) is only possible for the entire structure, not for individual structure components `comp`.

- A structure called `text` cannot have any components with three-character names, since these are reserved for addressing [text symbols](abentext_symbols.md). It is best to never call a structure `text` to avoid any conflicts with text symbols.

- The addition [`BOXED`](abapdata_boxed.md) cannot be specified between `DATA BEGIN OF` and `DATA END OF` when declaring components. Static boxes in structures can only be defined with [`TYPES`](abaptypes_boxed.md).

- The [value operator](../../abap-glossary/abenvalue_operator_glosry.md) [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) can be used to [construct](../abap-creating-objects-and-values/abenvalue_constructor_params_struc.md) the content of structures.

- The statements for declaring a structure are usually summarized in a [chained statement](../../abap-glossary/abenchained_statement_glosry.md) if possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, a structure `spfli_struc` is declared with an elementary component `index` and a substructure `spfli_wa`. The [`SELECT`](../abap-database-access/abapselect.md) loop shows a possible use of the nested structure.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: BEGIN OF spfli_struc, 
         index    TYPE i, 
         spfli_wa TYPE spfli, 
      END OF spfli_struc. 
 
SELECT * 
       FROM spfli 
       INTO @spfli_struc-spfli_wa. 
  spfli_struc-index += 1. 
  out->next_section( |{ spfli_struc-index }| ). 
  out->write_data( spfli_struc-spfli_wa ). 
ENDSELECT. 
 
out->display( ).
```

## Executable Examples

- [Declaration of a Simple Structure](abensimple_structure_abexa.md)

- [Declaration of a Nested Structure](abennested_structure_abexa.md)
