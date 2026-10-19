---
title: "Conversion Rules for Enumerated Types"
source_file: abenconversion_enumerated.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Rules for Enumerated Types

An [enumerated type](../../abap-glossary/abenenum_type_glosry.md) is a special elementary data type. Variables of this type are [enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md), which can only contain the [enumerated values](../../abap-glossary/abenenumerated_value_glosry.md) that are defined for the enumerated type. For this reason, source fields and target fields must be fully compatible in assignments between enumerated types, with one exception. The compatibility must apply to the enumerated type itself. The [base type](../../abap-glossary/abenbase_type_glosry.md) of the enumerated type is not relevant.

The only exception to this rule is the assignment of source fields with enumerated types to character-like variables of the types `c` and `string`. In this case, the following conversion rule applies:

The name and length of the [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) or the component of the [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) in which the current value of the source field is stored during the definition of the enumerated type, are assigned to the target field in uppercase letters.

This type of conversion to a character-like type can produce unexpected results. This is particularly common in operand positions in which implicit conversions take place.

There is no reverse conversion rule for assignments between character-like source fields and enumerated variables. There is however, a special rule for the conversion operator [`CONV`](abenconv_constructor_enum.md) that enables the actual value of an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) to be read in accordance with its [basis type](../../abap-glossary/abenbase_type_glosry.md).

Assignments between enumerated data objects and data objects that are not enumerated data objects lead to a syntax error or the runtime error `UC_OBJECTS_NOT_CONVERTIBLE`.

## Hints

- The following [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) are possible as operands in assignments between enumerated types:

  - Source fields can be [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) or components of [enumerated structures](../../abap-glossary/abenenumerated_structure_glosry.md) and [enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md).

  - Target fields can be [enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md).

- To be compatible, the source field and target field must have exactly the same enumerated type. An enumerated type created using [RTTC](../../abap-glossary/abenrun_time_type_creation_glosry.md) methods is never identical to a type defined using [`TYPES`](../abap-declarations/abaptypes_enum.md). A type description object created for an existing enumerated type using [RTTC](../../abap-glossary/abenrun_time_type_creation_glosry.md) methods, however, describes this type.

- [Enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) with enumerated types can be listed in all [read positions](../abap-operands/abendata_objects_usage_reading.md) where an implicit conversion to a character-like data type `c` or `string` takes place. They cannot be listed in operand positions where the operand must have a character-like data type.

- For an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md), the [ABAP Debugger](../../abap-glossary/abenabap_debugger_glosry.md) displays the name of the value that is converted into a character-like type.

- When converting to a character-like type, the direct name of the enumerated constant is always used in the context of the declaration with a maximum of 30 characters. It is not prefixed with the name of an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) with the structure component selector (`-`), nor with any class name with the class component selector (`=>`). Therefore, the conversion of enumerated objects of different enumerated types can have the same result if the names of the enumerated constants match.

- To assign a type-dependent initial value to enumerated variables, the statement [`CLEAR`](abapclear.md) or a constructor expression [`VALUE #( )`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) can be used on the right side of an assignment.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The enumerated values of the enumerated structure `p` of an enumerated type `planet` are loaded into an internal table whose line type is the enumerated type. Each line is then converted to the character-like type `string` and this is added to the internal table `planet_names`.

``` abap
TYPES: 
  BEGIN OF ENUM planet STRUCTURE p, 
    mercury, 
    venus, 
    earth, 
    mars, 
    jupiter, 
    saturn, 
    uranus, 
    neptune, 
  END OF ENUM planet STRUCTURE p. 
 
DATA planets TYPE SORTED TABLE OF planet 
             WITH UNIQUE KEY table_line. 
DO. 
  ASSIGN p-(sy-index) TO FIELD-SYMBOL(<p>). 
  IF sy-subrc <> 0. 
    EXIT. 
  ENDIF. 
  planets = VALUE #( BASE planets ( <p> ) ). 
ENDDO. 
 
DATA planet_names TYPE SORTED TABLE OF string 
                  WITH UNIQUE KEY table_line. 
planet_names = VALUE #( 
  BASE planet_names FOR enum IN planets ( CONV string( enum ) ) ). 
 
cl_demo_output=>display( planet_names ).
```
