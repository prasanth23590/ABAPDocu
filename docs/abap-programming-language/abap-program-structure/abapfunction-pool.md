---
title: "FUNCTION-POOL"
source_file: abapfunction-pool.html
section: "ABAP Programming Language > ABAP - Program Structure > Program-Initiating Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FUNCTION-POOL

## Syntax

``` abap
FUNCTION-POOL fpool   
                    [MESSAGE-ID mid].  
```

### Addition

[`... MESSAGE-ID mid`](abapfunction-pool.md#addition)

## Overview

### Description

The statement `FUNCTION-POOL` introduces a [function pool](../../abap-glossary/abenfunction_pool_glosry.md). It must be the first statement of a standalone program after any [include programs](../../abap-glossary/abeninclude_program_glosry.md) are resolved.

The full name of the master program of a function pool in the [repository](../../abap-glossary/abenrepository_glosry.md) consists of the prefix `SAPL` and the name `fpool` of the statement `FUNCTION-POOL`.

A function pool is used as a framework for [function modules](../../abap-glossary/abenfunction_module_glosry.md) and is organized in include programs as follows.

- A top include with the prefix `L` and the ending `TOP` in the declaration part of the function pool.

- Optional include programs with the prefix `L` and the ending `D..` for the declaration of local classes within the top include.

- An include program with the prefix `L` and the ending `UXX` in the implementation part of the function pool. This include program includes include programs with the ending `U..` for the implementation of each [function module](../../abap-glossary/abenfunction_module_glosry.md) of the function pool. This structure must not be changed.

- Optional include programs with the prefix `L` and the ending `P..` for the implementation of the methods of local classes in the implementation part of the function pool.

- 

- 

- Optional include programs with the prefix `L` and the ending `E..` for the implementation of [event blocks](../../abap-glossary/abenevent_block_glosry.md) in the implementation part of the function pool.

- Optional include programs with the prefix `L` and the ending `F..` for the implementation of [subroutines](../../abap-glossary/abensubroutine_glosry.md) in the implementation part of the function pool.

The periods `..` represent a two-digit number. The functionality of the Function Builder is based on compliance with this naming convention.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Structure of the function pool `SAPLABAP_DOCU` from include programs:

``` abap
*&---------------------------------------------------------------------* 
*&  Function Pool SAPLABAP_DOCU 
*&---------------------------------------------------------------------* 
 
INCLUDE labap_docutop.               " Global Declarations 
 
INCLUDE labap_docue00.               " Load of Program 
 
INCLUDE labap_docuuxx.               " Function Modules 
 
INCLUDE labap_docuo01.               " PBO Modules 
 
INCLUDE labap_docui01.               " PAI Modules 
 
INCLUDE labap_docue01.               " Handling of Runtime-Events 
 
INCLUDE labap_docup01.               " Class implementations 
INCLUDE labap_docup02. 
INCLUDE labap_docup03. 
INCLUDE labap_docup04.
```

The function pool includes the top include at the first position, which contains the statement `FUNCTION-POOL` and other include programs for data and class declarations:

``` abap
*&---------------------------------------------------------------------* 
*&  Include           LABAP_DOCUTOP 
*&---------------------------------------------------------------------* 
 
FUNCTION-POOL abap_docu. 
 
INCLUDE labap_docud00.               " Global Data for Screens 
 
INCLUDE labap_docud01.               " Classes for Docu Display
```

## Addition

`... MESSAGE-ID mid`

### Description

This addition specifies a message class `mid` that allows the use of short forms of the statement [`MESSAGE`](../abap-text-repositories/abapmessage.md) in the function pool in which only the message type and message number are specified. The message class must be specified directly and appear in the column `ARBGB` of the database table `T100`. The variants of the statement [`MESSAGE`](../abap-text-repositories/abapmessage.md) in which the message class is specified override the addition `MESSAGE-ID`.
