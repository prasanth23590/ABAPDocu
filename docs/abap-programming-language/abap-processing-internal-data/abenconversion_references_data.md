---
title: "Assignments Between Data Reference Variables"
source_file: abenconversion_references_data.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Reference Variables > Assignment Rules for Reference Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Assignments Between Data Reference Variables

Data reference variables are either completely typed or typed with the generic type `data`.

- [Upcasts in Data References](abenconversion_references_data.md#upcasts-in-data-references)

- [Downcasts in Data References](abenconversion_references_data.md#downcasts-in-data-references)

## Upcasts in Data References

An [upcast](../../abap-glossary/abenup_cast_glosry.md) in data references is possible in the following cases:

- The static types of the source variable and the target variable match according to the following rules:

  - Both are elementary data types with identical [technical type properties](../../abap-glossary/abentechnical_type_prpt_glosry.md), namely the built-in ABAP type, length, and number of decimal places. It is not important how the static types were defined.

  - Both have an identical structured type. In the case of structured types, identical technical type properties are not sufficient, but the same structured type must have been used to define the static types.

  - Both are table types with matching technical type properties, that is, line types, table category, and table key. In the case of non-structured line types, identical technical properties of the line type are sufficient. In the case of structured line types, both definitions must have been made with reference to the same structured type.

- The static type of the source variable is completely typed, and the static type of the target variable is generic.

### Hint

With respect to checks on static types, structured types behave like classes. Two differently structured types do not match, even if they consist of identical components.

## Downcasts in Data References

A [downcast](../../abap-glossary/abendown_cast_glosry.md) in data references is only possible if the static type of the source variable is generic and that of the target variable is completely typed. The syntax check makes it impossible for static types of the source variable and the target variable to be completely typed, but not identical at the same time.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The assignment from `dref1` to `dref2` is an upcast. The assignment from `dref2` to `dref1` is a downcast, which in the example below raises an exception. If the statement [`CREATE DATA`](../abap-creating-objects-and-values/abapcreate_data.md) had the addition `TYPE i`, the downcast would also have been successful.

``` abap
DATA: dref1 TYPE REF TO i, 
      dref2 TYPE REF TO data. 
 
CREATE DATA dref1. 
dref2 = dref1. 
CREATE DATA dref2 TYPE string. 
 
TRY. 
  dref1 ?= dref2. 
  CATCH cx_sy_move_cast_error. 
  ... 
ENDTRY.
```
