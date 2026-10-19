---
title: "PERFORM, parameter_list"
source_file: abapperform_parameters.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > PERFORM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# PERFORM, parameter_list

## Deprecated Syntax

``` abap
... [TABLES   itab1 itab2 ...]   
    [USING    a1 a2 ...]   
    [CHANGING a1 a2 ...].  
```

### Addition

[1. `... TABLES itab1 itab2 ...`](abapperform_parameters.md#addition-1)

[2. `... USING a1 a2 ...`](abapperform_parameters.md#addition-2)

[3. `... CHANGING a1 a2 ...`](abapperform_parameters.md#addition-3)

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Overview

### Description

These additions assign actual parameters to the formal parameters of the parameter interface of the subroutine `subr`. All data objects whose data type matches the [typing](../../abap-glossary/abentyping_glosry.md) of the corresponding formal parameter can be specified (see [Check Typing](../abap-declarations/abentyping_check.md)) as actual parameters. Each formal parameter assumes all the properties of the actual parameter assigned to it when it is called. The order of the additions is fixed.

## Addition 1

`... TABLES itab1 itab2 ...`

### Description

The addition `TABLES` must be used to assign an internal table `itab` as an actual parameter to each table parameter `t1 t2 ...` defined for the called subroutine using the addition `TABLES` of the statement [`FORM`](../abap-obsolete-language-elements/abapform.md). The assignment of the actual parameters to the formal parameters takes place using their positions in the lists `t1 t2 ...` and `itab1 itab2 ...`

Only [standard tables](../../abap-glossary/abenstandard_table_glosry.md) can be specified for `itab`. The data is passed by reference. If a specified table `itab` has a [header line](../../abap-glossary/abenheader_line_glosry.md), this is also passed. Otherwise, the header line in the corresponding table parameter `t` is initial when it is called.

### Hint

The use of table parameters in the interface of subroutines is obsolete, but a large number of subroutines have not yet been switched to appropriately typed `USING` parameters or `CHANGING` parameters and must still be filled by the addition `TABLES` of the statement `PERFORM`.

## Addition 2

`... USING a1 a2 ...`

## Addition 3

`... CHANGING a1 a2 ...`

### Description

If the additions `USING` and `CHANGING` are specified, a type-specific actual parameter `a1 a2 ...` must be assigned to each of the formal parameters `u1 u2 ...` and `c1 c2 ...` defined for the called subroutine using the identically named additions of the statement [`FORM`](../abap-obsolete-language-elements/abapform.md). The actual parameters specified after `USING` and `CHANGING` form one single shared list. They are assigned to the formal parameters in accordance with the position in the shared list. The type of parameter passing is defined by the additions `USING` and `CHANGING` in the statement `FORM`. The addition `USING` must be in front of `CHANGING`. Otherwise, the assignment of the actual parameters to the additions `USING` and `CHANGING` is ignored by the statement `PERFORM`. It is also irrelevant whether only one or both of the additions are specified.

### Hints

- For program documentation purposes, it is best to specify the additions `USING` and `CHANGING` in the statement `FORM` in accordance with the definition of the parameter interface.

- No [substring access](../abap-operands/abenoffset_length.md) is possible to an actual parameter of type `string` or `xstring` specified after `USING` or `CHANGING`.

- [Upcasts](../../abap-glossary/abenup_cast_glosry.md) are not possible when passing an actual parameter to a `USING` parameter typed as a reference variable.

- A `USING` parameter declared for [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md) behaves in the same way as a `CHANGING` parameter, which means that the content of the actual parameter could be changed in a forbidden way.
