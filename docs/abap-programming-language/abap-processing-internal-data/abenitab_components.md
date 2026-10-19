---
title: "itab - comp1 comp2 ..."
source_file: abenitab_components.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - comp1 comp2 ...

Addresses individual components of internal table lines in a range of statements for processing internal tables and in [table expressions](abentable_expressions.md). If not stated otherwise, the following syntax applies to `comp1 comp2...`:

## Syntax

``` abap
... { comp_name[-sub_comp][{+off(len)}|{->attr}] } | { (name) } ...  
```

## Description

The following alternatives are available for specifying components:

- Directly specifying the name `comp_name` of a component.

  - If the data type of the components is character-like and [flat](../../abap-glossary/abenflat_glosry.md), an offset/length `+off(len)` can be appended to the name of the component, as in [substring access](../abap-operands/abenoffset_length.md), to access subareas of the component. Only directly specified numbers or constants can be specified for `off` and `len`.

  - If the component is structured, the structure component selector `-` can be used to access the `sub_comp` components of the substructure.

  - If the component has a reference type, the object component selector `->` can be used to access all visible attributes `attr` of the referenced object. In this case, a table component can be specified more than once.

- Specifying a parenthesized [character-like data object](../../abap-glossary/abencharlike_data_object_glosry.md) `name`, which contains the name of the component when the statement is executed.

  - The name of the component in `name` can contain an offset/length specification.

  - The object component selector `->` can be specified in `name` to access attributes, but only those attributes can be addressed that are known statically.

  - `name` is not case-sensitive. If `name` only contains blanks, this component specification is ignored when the statement is executed. If `name` contains a nonexistent component, an uncatchable exception is raised.

- Specifying the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` to address the whole table line as a component.

## Hints

- A component can only be specified more than once if it has a reference type. Further components, however, can be specified alongside `table_line`. This is necessary, for example, if the line type of the internal table is an object reference and the value of the reference and the value of an attribute of the object are to be specified at the same time.

- If the table has a non-structured line type, the pseudo comment `table_line` can be addressed as the only component.

- The pseudo component `table_line` is a reserved name. In ABAP and in the ABAP Dictionary, no structure components called `table_line` can be declared.

- If the line type of the internal table cannot be statically identified, the components can usually only be specified dynamically and not directly.

- The components specified do not have to be elementary.

- If the data type allows it (character-like and flat), an offset/length specification can also include adjacent components

- A [customizing include](../../abap-glossary/abencustomizing_include_glosry.md) must not be specified as a component if it is empty.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Sorting by a dynamically specified component. An incorrect name produces a runtime error.

``` abap
DATA(column) = `carrid`. 
cl_demo_input=>request( CHANGING field = column ). 
 
DATA itab TYPE TABLE OF spfli WITH EMPTY KEY. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @itab. 
 
SORT itab BY (column). 
 
cl_demo_output=>display( itab ).
```
