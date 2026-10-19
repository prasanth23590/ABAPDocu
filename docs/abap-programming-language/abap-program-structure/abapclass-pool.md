---
title: "CLASS-POOL"
source_file: abapclass-pool.html
section: "ABAP Programming Language > ABAP - Program Structure > Program-Initiating Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-POOL

## Syntax

``` abap
CLASS-POOL [MESSAGE-ID id].  
```

### Addition

[`... MESSAGE-ID mid`](abapclass-pool.md#addition)

## Overview

### Description

The statement `CLASS-POOL` introduces a [class pool](../../abap-glossary/abenclass_pool_glosry.md) for a [global class](../../abap-glossary/abenglobal_class_glosry.md). It must be the first statement of a standalone program, after any [include programs](../../abap-glossary/abeninclude_program_glosry.md) have been resolved.

Class pools are maintained with the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md). A [master program](../../abap-glossary/abenmaster_program_glosry.md) and associated [include programs](../../abap-glossary/abeninclude_program_glosry.md) are generated automatically. The statement `CLASS-POOL` is created in the master program.

The full name of the master program of a class pool in the [repository](../../abap-glossary/abenrepository_glosry.md) starts with the name of the global class, is padded with the character `=` up to and including position 30, and ends with `CP`. The names of the include programs of a class pool included by the master program are constructed in exactly the same way as the name of the class pool itself, however they have different endings.

### Hints

- The statements that are allowed in a class pool are listed under [Statements in Class Pools and Interface Pools](../abap-abap-objects/abenclass_interace_pools.md).

- For technical reasons the class pool of a [global class](../../abap-glossary/abenglobal_class_glosry.md) that can be part of an inheritance tree that is

  - a [subclass](../../abap-glossary/abensubclass_glosry.md)

  - a non-[final](../../abap-glossary/abenfinal_glosry.md) class that is not a subclass but can be a [superclass](../../abap-glossary/abensuperclass_glosry.md)

    must contain the `CO` and `CI` includes with the statements [`PROTECTED SECTION`](../abap-declarations/abapprotected.md) and [`PRIVATE SECTION`](../abap-declarations/abapprivate.md) also for empty protected and private sections.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The name of the master program of the class pool of the global class `CL_DEMO_CLASS_POOL` is `CL_DEMO_CLASS_POOL============CP`.

## Addition

`... MESSAGE-ID mid`

### Description

This addition specifies a message class `mid` that allows the use of short forms of the statement [`MESSAGE`](../abap-text-repositories/abapmessage.md) in the class pool in which only the message type and message number are specified.
