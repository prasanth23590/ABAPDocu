---
title: "=, Assign Data Objects"
source_file: abapmove.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > =, Assignment Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# =, Assign Data Objects

## Syntax

``` abap
destination = dobj.  
```

## Description

In the simplest assignment case, a data object `dobj` is on the right side of the [assignment operator `=`](abenequals_operator.md) and can be specified as described under [Read Positions](../abap-operands/abendata_objects_usage_reading.md). The content of the data object is assigned to the left side, `destination`. If necessary, type-dependent conversions are made in accordance with the [conversion rules](abenconversion_rules.md). The variant shown here applies to all assignments between operands that are not reference variables. Special [rules](abapmove_cast.md) apply to reference variables.

The following can be specified for `destination`:

- Any data object that can be specified in a [write position](../../abap-glossary/abenwrite_position_glosry.md). The data type of the data object must be either [compatible](../../abap-glossary/abencompatible_glosry.md) with the data type of `dobj` or the content of `dobj` must be convertible to the data type of `destination` in accordance with one of the [conversion rules](abenconversion_rules.md).

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). If the data type of `dobj` is complete, it is used for the declaration. If `dobj` is a generically typed field symbol or a formal parameter of this type, the following data types are used:

  - `string` for `csequence` and `clike`

  - `xstring` for `xsequence`

  - `decfloat34` for `numeric` and `decfloat`

  - `p` with the length 8 and no decimal places if `p` is generic

  - The [standard key](../../abap-glossary/abenstandard_key_glosry.md) for a standard table type with generic primary table key

    Generic data types other than table types that are explicitly generic with respect to their secondary table keys cannot be made more concrete and produce a syntax error. An [offset/length specification](../abap-operands/abenoffset_length.md) can be applied to `dobj`. If `dobj` has a data type of fixed length, `off` and `len` must be literals or constants. Variables are not allowed. The data type used for the declaration is the data type of the substring as described for [offset/length specifications](../abap-operands/abenoffset_length.md).

## Hints

- The special assignment operator [?=](abapmove_cast.md) performs [downcasts](../../abap-glossary/abendown_cast_glosry.md) and is available for [assignments of reference variables](abenreference_assignments.md).

- If `dobj` and/or `destination` are field symbols, the content of the data objects to which the field symbols point is used as in all ABAP statements. The actual pointer content of a field symbol can only be changed using the statement [`ASSIGN`](abapassign.md) or the addition `ASSIGNING` when processing internal tables ([value semantics](../../abap-glossary/abenvalue_semantics_glosry.md)).

- Inline declarations are not possible for every conceivable generic type of `dobj`. This is because the rules for deriving the used data type apply even in an inline declaration at the position of an actual parameter for a generically typed output parameter of a method apply. Here, the typing check allows fewer combinations than the conversion rules of an assignment.

- If an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md) is specified as an operand of an assignment, in nearly all [operand positions](../abap-operands/abenoperands_data_objects.md), the header line is addressed and not the [table body](../../abap-glossary/abentable_body_glosry.md). To address the table body of a table with a header line, `[]` must be appended to the table name.

- Strings and internal tables are addressed internally using references. When assignments are made between strings and between internal tables of the same type (if the line types themselves do not contain any table types), only the internal administrative information is passed for performance reasons. After the assignment, the actual string or the actual [table body](../../abap-glossary/abentable_body_glosry.md) is addressed by the source object as well as the target object ([sharing](../../abap-glossary/abensharing_glosry.md)). Sharing is only removed when the data object is accessed to be changed and a copy of the content is made. The sharing is shown in the memory consumption display of the ABAP Debugger. For internal tables whose line type itself contains internal table types, no sharing takes place. Sharing can, however, take place for the subtables of a certain line type.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of a literal to a text string.

``` abap
DATA text TYPE string. 
 
text = `blah`.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of a generically typed field symbol, `<fs>`, to a data object, `number`, declared inline. In the assignment, the field symbol has the type `i` but the field `number` is already created with the type `decfloat34` when the program is generated. A syntax check warning about this is hidden using the pragma `##type`.

``` abap
FIELD-SYMBOLS <fs> TYPE numeric. 
 
ASSIGN 1 TO <fs>. 
 
FINAL(number) = <fs> ##type.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_CONVERSION_NO_NUMBER`

- *Cause:* Operand cannot be interpreted as number when assigned to a [numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)

  *Runtime error:* `CONVT_NO_NUMBER`

`CX_SY_CONVERSION_OVERFLOW`

- *Cause:* Overflow in arithmetic operation (type `p`, with specified length)

  *Runtime error:* `BCD_FIELD_OVERFLOW`

- *Cause:* Operand too big or (interim) result too big

  *Runtime error:* `CONVT_OVERFLOW`
