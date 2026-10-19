---
title: "Assignment and Conversion Rules"
source_file: abenconversion_rules.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Assignment and Conversion Rules

When the value of a source object (`source`) is assigned to a destination object (`destination`), three cases can be distinguished with respect to the data type:

1.  `source` and `destination` are [compatible](../../abap-glossary/abencompatible_glosry.md), which means that all [technical type properties](../../abap-glossary/abentechnical_type_prpt_glosry.md) match. The content is transferred from `source` to `destination` without being converted. For flat data objects and coherent character-like or byte-like structural areas, a copy of the source object is created down to the exact byte. In the case of [deep](../../abap-glossary/abendeep_glosry.md) data objects, a reference is created whose actual byte-like content is not visible externally in the destination object. When entire structures are assigned, the behavior in terms of [alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md) is undefined. The binary content of an alignment gap in the destination structure can either be copied from the source structure or keep the original value.

2.  `source` and `destination` are not compatible but can be [converted](../../abap-glossary/abenconvertible_glosry.md). The content of `source` is converted in accordance with the conversion rules and then transferred to `destination`. Two data types are convertible if a conversion rule exists for them. An exception is raised if the content of `source` cannot be handled in accordance with the conversion rules. After an exception, the content of `destination` depends on the category of the data type. An assignment where a conversion takes place is always slower than an assignment without conversion.

3.  If the data objects are neither compatible nor convertible, no assignment can take place. If the syntax check recognizes this state, a syntax error is raised, otherwise an uncatchable exception is raised when the program is executed.

The following sections describe the conversion rules. Conversion rules exist for:

- [Elementary data objects](abenconversion_elementary.md)

- [Structures](abenconversion_struc.md)

- [Internal tables](abenconversion_itab.md)

- [Meshes](abenconversion_mesh.md)

- [Enumerated types](abenconversion_enumerated.md)

The special [assignment rules for reference variables](abenconversion_references.md) are listed in a separate section.

The conversion rules shown here generally apply to all [assignments](abenequals_operator.md) and all statements in which the content of data objects is changed. Exceptions to these rules are described in the individual statements.

The [conversion operator](../../abap-glossary/abenconversion_operator_glosry.md) [`CONV`](abenconstructor_expression_conv.md) can be used in many operand positions to convert a source value to an explicitly specified target data type in accordance with the rules described here. System classes are available for special conversions of character sets and numeric formats.

## Hints

- In the [operand positions](../../abap-glossary/abenoperand_position_glosry.md) of many statements, assignments take place internally according to the assignment rules. Whether the exceptions that occur during an assignment can be handled or not depends on the operands and the operand position. The following are some examples:

  - If [functional method calls](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) are used in operand positions, exceptions that can be handled when data objects are used directly cannot be handled, and produce runtime errors directly instead.

  - In [comparisons](../abap-program-flow-logic/abenlogexp.md), some different [rules](../abap-program-flow-logic/abenlogexp_rules_operands.md) apply than in assignments. Exceptions that are catchable in assignments are either handled implicitly or lead to runtime errors and cannot be handled explicitly in comparisons.

  - Using [expressions](../../abap-glossary/abenexpression_glosry.md) in operand positions can make uncatchable exceptions catchable in some cases.

- The [lossless operator](../../abap-glossary/abenlossless_operator_glosry.md) [`EXACT`](abenconstructor_expression_exact.md) can be used to perform checks before the conversion is executed that ensure that only valid values are assigned and that no values are lost in assignments.

- Checks generally are not made on assignments between compatible data objects. If a data object already contains an invalid value, for example an invalid date or time in a date or time field, it is transferred like a valid value if the assignment is being made to a compatible data object.

- In order to check if two data types are compatible at runtime, the method `APPLIES_TO_DATA` of RTTI class `CL_ABAP_DATADESCR` can be used. This can be helpful to prevent uncatchable exceptions when assigning generically typed data objects that are neither compatible nor convertible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Method `APPLIES_TO_DATA` of RTTI class `CL_ABAP_DATADESCR` is used to check the compatibility of generically typed field symbols pointing to different data objects. Assigning the content of `<fs1>` to `<fs3>` would raise an uncatchable exception.

``` abap
DATA num1 TYPE i. 
DATA num2 TYPE i. 
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
 
DATA(o) = cl_demo_output=>new( ). 
 
FIELD-SYMBOLS: 
  <fs1> TYPE any, 
  <fs2> TYPE any, 
  <fs3> TYPE any. 
 
ASSIGN num1 TO <fs1>. 
ASSIGN num2 TO <fs2>. 
ASSIGN itab TO <fs3>. 
 
o->next_section( 'i vs. i' ). 
IF CAST cl_abap_datadescr( cl_abap_typedescr=>describe_by_data( <fs1> ) 
    )->applies_to_data( <fs2> ). 
  o->write( 'Compatible' ). 
 
  <fs1> = <fs2>. 
 
ELSE. 
  o->write( 'Not compatible' ). 
ENDIF. 
 
o->next_section( 'i vs. itab' ). 
IF CAST cl_abap_datadescr( cl_abap_typedescr=>describe_by_data( <fs1> ) 
    )->applies_to_data( <fs3> ). 
  o->write( 'Compatible' ). 
 
  <fs1> = <fs3>. 
 
ELSE. 
  o->write( 'Not compatible' ). 
ENDIF. 
 
o->display( ).
```
