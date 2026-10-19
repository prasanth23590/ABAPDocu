---
title: "CALL FUNCTION DESTINATION, parameter_list"
source_file: abapcall_function_destination_para.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > CALL FUNCTION > CALL FUNCTION, RFC > CALL FUNCTION DESTINATION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL FUNCTION DESTINATION, parameter_list

## Syntax

``` abap
... { [EXPORTING  p1 = a1 p2 = a2 ...]   
      [IMPORTING  p1 = a1 p2 = a2 ...]   
      [TABLES     t1 = itab1 t2 = itab2 ...]   
      [CHANGING   p1 = a1 p2 = a2 ...]   
      [EXCEPTIONS [exc1 = n1 exc2 = n2 ...]   
                  [system_failure        = ns [MESSAGE smess]]   
                  [communication_failure = nc [MESSAGE cmess]]   
                  [OTHERS = n_others]] }   
  | { [PARAMETER-TABLE ptab]   
      [EXCEPTION-TABLE etab] } ...  
```

### Addition

[1. `EXPORTING p1 = a1 p2 = a2 ...`](abapcall_function_destination_para.md#addition-1)

[2. `IMPORTING p1 = a1 p2 = a2 ...`](abapcall_function_destination_para.md#addition-2)

[3. `TABLES t1 = itab1 t2 = itab2 ...`](abapcall_function_destination_para.md#addition-3)

[4. `CHANGING p1 = a1 p2 = a2 ...`](abapcall_function_destination_para.md#addition-4)

[5. `EXCEPTIONS exc1 = n1 exc2 = n2 ... [MESSAGE ...]`](abapcall_function_destination_para.md#addition-5)

[6. `PARAMETER-TABLE ptab`](abapcall_function_destination_para.md#addition-6)

[7. `EXCEPTION-TABLE etab`](abapcall_function_destination_para.md#addition-7)

## Overview

### Description

Parameter passing for sRFC. These additions are used to assign actual parameters to the formal parameters of the synchronously called remote function module and return values to non-class-based exceptions. These additions essentially have the same meaning as they do in general [function module calls](abapcall_function_parameter.md).

Some other differences for specific additions are described in the following.

### Hints

- If a remote-enabled function module is not called using RFC, parameter passing behaves in the same way as in a general function module call and the corresponding exceptions are raised for incorrect formal parameters and unsuitable actual parameters.

## Addition 1

`EXPORTING p1 = a1 p2 = a2 ...`

## Addition 2

`IMPORTING p1 = a1 p2 = a2 ...`

### Description

The following differences apply to the additions `EXPORTING` and `IMPORTING`:

- In character-like formal parameters, the actual parameter can have a length different from the formal parameter. In the called function module, a shorter actual parameter is filled with blanks on the right in the input and truncated in the output. If the actual parameter is longer, the reverse applies.

- [Reference variables](../../abap-glossary/abenreference_variable_glosry.md) cannot be passed directly or as components of deep structures. As in general function module calls, however, tables with [deep](../../abap-glossary/abendeep_glosry.md) line types, structures, and strings can be passed.

- When passing internal tables with non-unique [table keys](../abap-data-types-and-data-objects/abenitab_key.md), the order of the duplicate lines in relation to these keys is not retained.

## Addition 3

`TABLES t1 = itab1 t2 = itab2 ...`

### Description

When using `TABLES` to pass data to table parameters, the difference is that only tables with [flat](../../abap-glossary/abenflat_glosry.md) line types and no [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) can be passed.

## Addition 4

`CHANGING p1 = a1 p2 = a2 ...`

### Description

With respect to the addition `CHANGING`, the same differences apply as to the additions `EXPORTING` and `IMPORTING`.

## Addition 5

`EXCEPTIONS exc1 = n1 exc2 = n2 ... [MESSAGE ...]`

### Description

The addition `EXCEPTIONS` is used to perform classic [non-class-based](../abap-program-flow-logic/abenexceptions_non_class.md) exception handling, which works in essentially the same way as in general function module calls. In addition,

If a remotely called function module raises a class-based exception during non-class-based exception handling, this exception is not transported and raises the predefined classic exception `SYSTEM_FAILURE` instead

### Hints

- Class-based exception handling in RFCs is not possible in the current release track.

## Executable Examples

## Addition 6

`PARAMETER-TABLE ptab`

## Addition 7

`EXCEPTION-TABLE etab`

### Description

These additions use the special internal tables `ptab` and `etab` to assign actual parameters to the formal parameters of the function module and return values to the non-class-based exceptions dynamically.

The description and usage of the internal tables is the same as for the [general call of function modules](abapcall_function_dynamic.md), but the RFC-specific rules apply that are described above for static parameter passing.

Furthermore, the column `message` with type `REF TO data` of exception table `etab` can be used as pointer to a character-like field for the special exceptions `system_failure` or `communication_failure`. If such an exception occurs, the character like field is filled with the same content as `smess` or `cmess` specified behind `MESSAGE` in static parameter passing.

### Hints

- The column `message` of exception table `etab` is not used for general function calls.

- The character-like field referred by column `message` can also be of type `string` here.
