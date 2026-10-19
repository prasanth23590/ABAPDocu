---
title: "Lossless Assignments, Rules"
source_file: abapmove_exact.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Lossless Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Lossless Assignments, Rules

A lossless assignment checks the assigned content, before its [conversion](../../abap-glossary/abenconversion_glosry.md) to an incompatible target object, to determine whether the assignment is possible without losses, that is:

- whether it is a valid value for the data type of the source

- whether a conversion to the target field would lead to a loss of values

- whether the value is valid for the target field after conversion

If the source contains a valid value and no values are lost, the conversion is performed in accordance with the associated [conversion rules](abenconversion_rules.md). Otherwise no assignment is made. If it is already known statically that one of the prerequisites is violated, a syntax error occurs. If this violation is not identified until the program is executed, a catchable exception is raised whose exception class is generally a subclass of `CX_SY_CONVERSION_ERROR`.

The following sections outline which rules are used by the operator [`EXACT`](abenconstructor_expression_exact.md) when checking the content of its argument with respect to the data types involved:

- [Checking Elementary Data Objects](abenmove_exact_elementary.md)

- [Checking Structures](abenmove_exact_structure.md)

- [Checking Internal Tables](abenmove_exact_itab.md)

If an exception is raised as a result of an invalid or inappropriate value, the `VALUE` attribute of the exception object is assigned this value in character form and this value is generally also included in the exception text.

No checks are made for:

- compatible data types

  The content of the argument is passed to the return value without being converted, even if it already contains an invalid value.

- reference variables

  Checks on the content of a reference variable using `EXACT` are not useful because nothing is converted and the content is either assignable or not assignable, as specified by the [assignment rules for reference variables](abenconversion_references.md).

A syntax check warning is produced if it is known statically that no checks are performed for the combination of argument and target type, making `EXACT` superfluous.

## Hint

Since lossless checks are only performed for conversions to incompatible data types, it is best to only use the operator `EXACT` to fill data objects that should only be given valid objects. Other types of assignments that require a start value to be specified in the declaration using [`VALUE`](../abap-declarations/abapdata_options.md) can create invalid values that are then not recognized when a lossless assignment is made to a compatible target field.

## Executable Example

[Lossless Assignment](abenmove_exact_abexa.md).
