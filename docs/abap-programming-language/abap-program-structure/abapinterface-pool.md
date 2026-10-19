---
title: "INTERFACE-POOL"
source_file: abapinterface-pool.html
section: "ABAP Programming Language > ABAP - Program Structure > Program-Initiating Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INTERFACE-POOL

## Syntax

``` abap
INTERFACE-POOL.   
```

## Description

The statement `INTERFACE-POOL` introduces an [interface pool](../../abap-glossary/abeninterface_pool_glosry.md) for a [global interface](../../abap-glossary/abenglobal_interface_glosry.md). It must be the first statement of an interface pool after any [include programs](../../abap-glossary/abeninclude_program_glosry.md) are resolved.

Interface pools are maintained exclusively with the Class Builder tool in the ABAP Workbench or with the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md). A [master program](../../abap-glossary/abenmaster_program_glosry.md) and an associated [include program](../../abap-glossary/abeninclude_program_glosry.md) are generated automatically. The statement `INTERFACE-POOL` is created in the master program.

The full name of the master program of an interface pool in the [repository](../../abap-glossary/abenrepository_glosry.md) starts with the name of the global interface, is padded with the character `=` up to and including position 30, and ends with `IP`.

The name of the include program of an interface pool included by the master program is constructed in exactly the same way as the name of the interface pool itself, however with an different ending.

## Hints

- The statements that are allowed in an interface pool are listed under [Statements in Class Pools and Interface Pools](../abap-abap-objects/abenclass_interace_pools.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The name of the master program of the interface pool of the global interface `IF_DEMO_INTERFACE_POOL` is `IF_DEMO_INTERFACE_POOL========IP` and it includes `IF_DEMO_INTERFACE_POOL========IU`.
