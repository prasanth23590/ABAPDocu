---
title: "ASSIGN, casting_spec"
source_file: abapassign_casting.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN, casting_spec

## Syntax

``` abap
... { }   
  | { CASTING { { }   
              | {TYPE type|(name)}   
              | {LIKE dobj}   
              | {[TYPE p] DECIMALS dec}  
```

### Alternative

[1. `... { }`](abapassign_casting.md#alternative-1)

[2. `... CASTING ...`](abapassign_casting.md#alternative-2)

## Overview

### Description

The specification `casting_spec` defines the data type used to handle the memory area [`mem_area`](abapassign_mem_area.md) assigned to the field symbol when a statement contains the field symbol in an operand position. Either the addition `CASTING` can be specified or nothing at all.

The following restrictions apply:

- In assignments of [table expressions](abapassign_mem_area_writable_exp.md), only the first alternative can be used without further additions.

- The `CASTING` addition cannot be used for [enumerated types](../../abap-glossary/abenenum_type_glosry.md). This means that the assigned memory area must not be an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) and the specified data type must not be an enumerated type.

## Alternative 1

`... { }`

### Description

If nothing is specified for `casting_spec`, the field symbol inherits the data type of the data object used in [`mem_area`](abapassign_mem_area.md) and the assigned memory area is handled accordingly. This data type must [match](../abap-declarations/abentyping_check_general.md) the [typing](../../abap-glossary/abentyping_glosry.md) of the field symbol.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the first assignment the field symbol has type `c` of length 3 and after the second assignment the field symbol has type `string`. The method `describe_by_data` returns the corresponding values `C 3` and `g`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FIELD-SYMBOLS <fs> TYPE csequence. 
 
ASSIGN 'xxx' TO <fs>. 
DATA(type) = cl_abap_typedescr=>describe_by_data( <fs> )->type_kind. 
out->write( type ). 
 
ASSIGN `xxx` TO <fs>. 
type = cl_abap_typedescr=>describe_by_data( <fs> )->type_kind. 
out->write( type ). 
 
out->display( ).
```

## Alternative 2

`... CASTING ...`

### Addition

[1. `... { }`](abapassign_casting.md#addition-1)

[2. `... TYPE type|(name)`](abapassign_casting.md#addition-2)

[3. `... LIKE dobj`](abapassign_casting.md#addition-3)

[4. `... [TYPE p] DECIMALS dec`](abapassign_casting.md#addition-4)

### Description

If the addition `CASTING` is used in `casting_spec`, the memory area is handled as if it had the type specified by `CASTING`.

Casting can either take place implicitly using the typing of the field symbol or explicitly using one of the additions `TYPE`, `LIKE`, or `DECIMALS`. In explicit castings, the field symbol can only be typed generically, not completely.

### Hints

- If the data type determined by `CASTING` is [deep](../../abap-glossary/abendeep_glosry.md) or if deep data objects are stored in the assigned memory area, the deep components must appear with exactly the same type and position in the assigned memory area. In particular, this means that individual [reference variables](../../abap-glossary/abenreference_variable_glosry.md) can be assigned to only one field symbol that is typed as a reference variable by the same [static type](../../abap-glossary/abenstatic_type_glosry.md).

- If the addition `CASTING` is used, the result of the statement `ASSIGN` may be platform-dependent. The internal [byte order](../abap-data-types-and-data-objects/abenbyteorder.md) of characters can, for example, be platform-dependent, which becomes apparent in a cast to a byte-like data type.

- The memory area [`mem_area`](abapassign_mem_area.md) must meet the [alignment requirements](../abap-data-types-and-data-objects/abenalignment.md) of the data type specified by the casting. When flat elementary data types are specified, for example, the memory address `mem_area` must be divisible as follows:

  - By 2 for the character-like data types `c` and `n` and the date/time types `d` and `t`.

  - By 4 for the numeric data type `i`.

  - By 8 for the numeric data types `int8`, `f`, and `decfloat16`.

  - By 8 for the time stamp type `utclong`.

  - By 16 for the numeric data type `decfloat34`.

- The static check of the statement `ASSIGN` using the addition `CASTING` is performed so that all errors are identified, regardless of the system or platform on which the check is run. A runtime check only checks the current system or the current platform.

## Addition 1

`... { }`

### Description

If the addition `CASTING` is specified without further additions, the assigned memory area is cast to the type of the field symbol. The field symbol must be either completely typed or with one of the generic built-in ABAP types `c`, `n`, `p`, or `x`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Casting of the integer 333 as a byte field. Depending on the [byte order](../../abap-glossary/abenbyte_order_glosry.md), the output is either `4D01` or `014D`.

``` abap
final(out) = cl_demo_output=>new( ). 
 
TYPES hex4 TYPE x LENGTH 2. 
FIELD-SYMBOLS <fs> TYPE hex4. 
 
ASSIGN 333 TO <fs> CASTING. 
out->write( <fs> ). 
 
out->display( ).
```

## Addition 2

`... TYPE type|(name)`

### Description

Explicit specification of a data type after `TYPE`. The name of the type can be specified as follows:

- `type`

  Direct static specification as `type`.

- `(name)`

  Specification as the content of a character-like data object `name` that contains the name of a data type in uppercase letters when the statement is executed. The following can be specified for `name`:

  - Literal or constants

    If the data object `name` is specified as a character literal or as a constant, it can be evaluated statically, and the specified type is recognized as the used object.

  - Variable

    If the data object `name` is specified as a variable, it is specified only dynamically, and the content is not evaluated statically. When the statement is executed, `name` is not evaluated until runtime in both cases.

The assigned memory area is cast to the specified type. The data type specified after `TYPE` cannot be generic, apart from the built-in ABAP types `c`, `n`, `p`, and `x`. Furthermore, [table categories](../abap-declarations/abaptypes_tabcat.md) and `REF TO` cannot be specified.

The field symbol `<fs>` can only be typed generically and not completely. The specified data type must [match](../abap-declarations/abentyping_check.md) the generic [typing](../../abap-glossary/abentyping_glosry.md) of the field symbol, meaning that [castings](../../abap-glossary/abencast_casting_glosry.md) are allowed to specialize the generic typing but not to make it more general.

If a generic character-like type `c` or `n` is specified after `TYPE`, the length of the assigned memory area must be a multiple of the length of a character in the memory when the statement is executed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Casting of a time field to a structured type with three components.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF time, 
    hours   TYPE c LENGTH 2, 
    minute  TYPE c LENGTH 2, 
    seconds TYPE c LENGTH 2, 
  END OF time. 
 
FIELD-SYMBOLS <fs> TYPE any. 
FINAL(t) = cl_demo_date_time=>get_user_time( ). 
ASSIGN t TO <fs> CASTING TYPE time. 
out->write( <fs> ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, one of the two `ASSIGN` statements produces a runtime error because the alignment requirement for the type `c` is not met. Which of the statements produces the runtime error is not generally defined and depends on the preceding declarations.

``` abap
DATA hex TYPE x LENGTH 10. 
 
FIELD-SYMBOLS <fs> TYPE any. 
 
ASSIGN hex+0(4) TO <fs> CASTING type c. 
ASSIGN hex+1(4) TO <fs> CASTING type c.
```

## Addition 3

`... LIKE dobj`

### Description

The following can be specified after `LIKE`:

- A data object `dobj` according to the rules for [`TYPES ... LIKE`](../abap-declarations/abaptypes_referring.md). The assigned memory area is cast to the data type of the data object.

- A generically typed field symbol.

  - If a memory area is assigned to the field symbol, the data type used to handle the memory area is the object of the cast.

  - If no memory area is assigned to the field symbol, a standard type resulting from the following rules is used:

    `any`, `c`, `clike`, `csequence`, `data`, and `simple` produce `c` with length 1. `decfloat` produces `decfloat34`. `n` produces `n` with length 1. `numeric` and `p` produce `p` with length 8 and no decimal places. `x` and `xsequence` produce `x` of the length 1. Generic table types raise an exception of the class `CX_SY_ASSIGN_CAST_ILLEGAL_CAST`.

- A generically typed formal parameter.

  - If an actual parameter is assigned to the formal parameter, the data type of this parameter is the object of the cast.

  - If no actual parameter is assigned to an optional formal parameter, its [associated](../abap-declarations/abentyping_generic.md) [standard type](../../abap-glossary/abenstandard_type_glosry.md) is used.

The field symbol `<fs>` can only be typed generically and not completely. The specified data type must [match](../abap-declarations/abentyping_check.md) the generic [typing](../../abap-glossary/abentyping_glosry.md) of the field symbol, meaning that [castings](../../abap-glossary/abencast_casting_glosry.md) are allowed to specialize the generic typing but not to make it more general.

### Hints

- `LIKE` can be used to refer to the data objects in its own program, and also to the public attributes of global classes.

- The standard type for generically typed field symbols specified after `CASTING LIKE` differs slightly from the [standard type](../abap-declarations/abentyping_generic.md) for generic field symbols and formal parameters (length 1 not 4 if `any` and `data` are used and no standard type for generic table types).

- If a generically typed field symbol is specified after `CASTING LIKE`, a memory area should be assigned to it when the statement is executed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Casting of a structure with three components to a time field.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  BEGIN OF time, 
    hours   TYPE c LENGTH 2 VALUE '11', 
    minute  TYPE c LENGTH 2 VALUE '55', 
    seconds TYPE c LENGTH 2 VALUE '00', 
  END OF time. 
 
FIELD-SYMBOLS <fs> TYPE any. 
FINAL(t) = cl_demo_date_time=>get_user_time( ). 
ASSIGN time TO <fs> CASTING LIKE t. 
out->write( <fs> ). 
 
out->display( ).
```

## Addition 4

`... [TYPE p] DECIMALS dec`

### Description

A numeric data object `dec` must be specified after `DECIMALS`. The assigned memory area is cast to the data type `p`, where the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) is determined by the content of `dec`. The number of decimal places must not exceed the total number of [places](../../abap-glossary/abenplace_glosry.md). `TYPE` does not need to be specified for `DECIMALS`. If `TYPE` is used, only the data type `p`, which is used anyway, can be specified.

The field symbol `<fs>` can only be typed generically and not completely. The specified data type must [match](../abap-declarations/abentyping_check.md) the generic [typing](../../abap-glossary/abentyping_glosry.md) of the field symbol, meaning that [castings](../../abap-glossary/abencast_casting_glosry.md) are allowed to specialize the generic typing but not to make it more general.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The calculation of the quotient from the packed number `pack` and the field symbol `<pack>` demonstrates the effect of casting with the addition `DECIMALS`. Factors between 10 and 100,000,000 are determined. When using `<pack>` in operand positions, a different value is used than when using `pack`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA output TYPE TABLE OF string WITH EMPTY KEY. 
DATA pack   TYPE p LENGTH 8 DECIMALS 0 VALUE '12345678'. 
FIELD-SYMBOLS <pack> TYPE p. 
 
DO 8 TIMES. 
  ASSIGN pack TO <pack> CASTING DECIMALS sy-index. 
  APPEND CONV string( pack / <pack> ) TO output. 
ENDDO. 
out->write( output ). 
 
out->display( ).
```
