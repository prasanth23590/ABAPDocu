---
title: "Dereferencing Operator"
source_file: abendereferencing_operator.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions > Notations for Single Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Dereferencing Operator

The content of a data object pointed to by a [data reference](../abap-data-types-and-data-objects/abendata_reference_type.md) is accessed using the dereferencing operator:

`dref->*`

The dereferencing operator `->*` can be specified after a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) `dref`.

- If the static type of the data reference variable is not generic, the expression `dref->*` can be specified at any operand position.

- For data reference variables with the generic static type `data`, it can be specified at any operand position except for:

  - Replacement parameters behind `DEFAULT` for methods, functions or events.

  - [Components](../abap-processing-internal-data/abenitab_components.md) of internal tables.

  - Operand positions where an [index table](../../abap-glossary/abenindex_table_glosry.md) is expected.

If the data reference variable contains the [null reference](../../abap-glossary/abennull_reference_glosry.md), the uncatchable exception `DATREF_NOT_ASSIGNED` is raised when the dereferencing operator is used. The exception to this is the dereferencing in the statement `ASSIGN`.

## Hints

- The dereferencing operator uses the [object component selector](abenobject_component_selector.md).

- For an index access to an internal table referenced by a generically typed data reference variable, it must be assigned to a field symbol typed with [`index table`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) first.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Uses the dereferencing operator in a general operand position and in the statement `ASSIGN`. Only in `ASSIGN` can `dref` be initial without raising an uncatchable exception.

``` abap
DATA dref TYPE REF TO data. 
dref = NEW i( 111 ). 
 
cl_demo_output=>write( |dref->* { dref->* }| ). 
 
CLEAR dref. 
ASSIGN dref->* TO FIELD-SYMBOL(<fs>). 
cl_demo_output=>write( |sy-subrc { sy-subrc }| ). 
 
cl_demo_output=>display( ).
```
