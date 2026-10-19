---
title: "DATA, TYPE, LIKE enum"
source_file: abapdata_enum.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, TYPE, LIKE enum

## Syntax

``` abap
DATA enum_var { {TYPE enum_type |EnumType}   
              | {LIKE enum_dobj} }   
              [VALUE val|{IS INITIAL}]   
              [READ-ONLY].  
```

[`[VALUE val|{IS INITIAL}]`](abapdata_options.md) · [`[READ-ONLY]`](abapdata_options.md)

## Description

Declaration of an [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md). An enumerated variable is declared by:

- `TYPE` reference to an [enumerated type](../../abap-glossary/abenenum_type_glosry.md) [`enum_type`](abaptypes_enum.md) defined in ABAP, or to an enumerated type [`EnumType`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_enum_type.md) defined in ABAP CDS.

- `LIKE` reference to a data object with [enumerated type](../../abap-glossary/abenenum_type_glosry.md). The following options are possible:

  - [Enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) of an enumerated type

  - Existing enumerated variables

The data type of an enumerated variable is its enumerated type. The enumerated type prescribes the [enumerated values](../../abap-glossary/abenenumerated_value_glosry.md) that an enumerated variable can contain. The [assignment rules for enumerated types](../abap-processing-internal-data/abenconversion_enumerated.md) and the allowed operand positions for enumerated variables ensure that only allowed enumerated values can be assigned to an enumerated variable.

The technical type of the enumerated value in an enumerated variable is the [base type](../../abap-glossary/abenbase_type_glosry.md) of the enumerated type. It is always a flat elementary type with a maximum length of 16 bytes.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, three enumerated variables are declared:

- `color1` by a `TYPE` reference to the enumerated type `colors`

- `color2` by a `LIKE` reference to `color1`

- `color3` by an [inline declaration](abendata_inline.md) with reference to the enumerated type `colors`

Each enumerated variable is assigned a valid value. The output shows the name of the assigned enumerated constant and the actual value for each enumerated variable. A special rule for the conversion operator [`CONV`](../abap-processing-internal-data/abenconv_constructor_enum.md) is used for the latter.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF ENUM colors, 
    red, blue, green, 
  END OF ENUM colors. 
 
DATA color1 TYPE colors VALUE red. 
 
DATA color2 LIKE color1. 
color2 = blue. 
 
DATA(color3) = VALUE colors( ). 
color3 = green. 
 
out->write( 
  |{ color1 }: { CONV i( color1 ) }\n| && 
  |{ color2 }: { CONV i( color2 ) }\n| && 
  |{ color3 }: { CONV i( color3 ) }| ). 
 
out->display( ).
```
