---
title: "PERFORM, subr_identifier"
source_file: abapperform_form.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > PERFORM > PERFORM, general"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# PERFORM, subr_identifier

## Deprecated Syntax

``` abap
... subr   
  | {subr|(sname) IN PROGRAM {prog|(pname)} [IF FOUND]}   
  | {n OF subr1 subr2 ...} ...  
```

### Alternative

[1. `... subr ...`](abapperform_form.md#alternative-1)

[2. `... subr|(sname) IN PROGRAM {prog|(pname)} [IF FOUND] ...`](abapperform_form.md#alternative-2)

[3. `... n OF subr1 subr2 ...`](abapperform_form.md#alternative-3)

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Overview

### Description

These names are used in the statement [`PERFORM`](abapperform.md) to specify the called program and the ABAP program in which it is defined.

## Alternative 1

`... subr ...`

### Description

When specified directly, `subr` calls any subroutine of the current program using its name declared in the statement [`FORM`](../abap-obsolete-language-elements/abapform.md). The subroutine must exist.

## Alternative 2

`... subr|(sname) IN PROGRAM {prog|(pname)} [IF FOUND] ...`

### Addition

[`... IF FOUND`](abapperform_form.md#addition)

\*\* This syntax is not available in the current ABAP language version.\*\*

## Alternative 3

`... n OF subr1 subr2 ...`

### Description

If specified, this selects a subroutine `subr` of the current program from a list. The list `subr1 subr2 ...` can contain up to 256 directly specified subroutines. `n` expects a numeric data object containing a number between 1 and the specified number of subroutines when the statement is executed. The subroutine `subr` is called, whose list position is in `n`. In this variant, it is not possible to specify `parameter_list` and only subroutines without a parameter interface can be called.
