---
title: "REF, Reference Operator"
source_file: abenconstructor_expression_ref.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Reference Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REF, Reference Operator

## Syntax

``` abap
... REF type( dobj | table_exp ) ...  
```

[`table_exp`](abentable_expressions.md)

### Alternative

[1. `... REF type( dobj )`](abenconstructor_expression_ref.md#alternative-1)

[2. `... REF type( table_exp )`](abenconstructor_expression_ref.md#alternative-2)

## Overview

### Description

A [constructor expression](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) with the reference operator `REF` creates either a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) that points to the operand `dobj` or controls a [table expression](../../abap-glossary/abentable_expression_glosry.md) [`table_exp`](abentable_expressions.md).

Existing data objects and table expressions can be specified as an operand, but no other expressions or function calls.

## Alternative 1

`... REF type( dobj )`

### Description

If a data object `dobj` is specified as an operand, the operator `REF` works like the statement [`GET REFERENCE`](abapget_reference.md) and creates a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) as a result that points to the specified data object `dobj`. `type` determines the [static type](../../abap-glossary/abenstatic_type_glosry.md) of the result. The following can be specified for `type`:

- A non-generic data type `dtype` that satisfies the rules of [upcasts in data references](abenconversion_references_data.md).

- The generic data type [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

- The `#` character for a data type that is determined by the following hierarchy:

  - If the data type required in an operand position is unique and known completely, the [operand type](../../abap-glossary/abenoperand_type_glosry.md) is used.

  - If the operand type cannot be derived from the context, the data type of `dobj` is used.

  - If the data type of `dobj` is not known statically, the generic type [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) is used.

The parentheses must contain exactly one operand `dobj`. If offsets/lengths ([`+off(len)`](../abap-operands/abenoffset_length.md)) are specified, the data type `dobj` here cannot be `string` or `xstring`.

### Hints

- The conversion operator `REF` is suitable for avoiding declarations of helper variables that are only necessary, for example, to specify data reference variables as actual parameters.

- No empty parentheses can be specified after `REF`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Filling of an internal table with the value operator `VALUE`, where the component `dref` is given a value using `REF`. This is an excerpt from the executable example for the class `CL_ABAP_BROWSER`. Other use cases can be found in the executable examples of ADBC, where parameter bindings are used.

``` abap
TYPES pict_line(1022) TYPE x. 
 
DATA  pict     TYPE STANDARD TABLE OF pict_line WITH EMPTY KEY. 
DATA  ext_data TYPE cl_abap_browser=>load_tab. 
 
ext_data = VALUE #( ( name = 'PICT.GIF' 
                      type = 'image' 
                      dref = REF #( pict ) ) ).
```

## Alternative 2

`... REF type( tab_exp )`

### Description

If a [table expression](../../abap-glossary/abentable_expression_glosry.md) [`table_exp`](abentable_expressions.md) is specified as an operand, the operator `REF` controls the type of its result and enables a default value to be specified for unfound lines, as described in the related [section](abentable_exp_result.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the operator `REF` is a data reference variable that points to the fifth line of the internal table `itab`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE STANDARD TABLE OF i WITH EMPTY KEY. 
 
itab = VALUE #( FOR i = 1 UNTIL i >= 10 ( i * 10 ) ). 
 
FINAL(dref) = REF #( itab[ 5 ] ). 
 
out->write( dref->* ). 
 
out->display( ).
```
