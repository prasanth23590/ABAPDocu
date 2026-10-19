---
title: "Event Blocks"
source_file: abenevent_blocks.html
section: "ABAP Programming Language > ABAP - Program Structure > Modularization Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Event Blocks

Event blocks are used to handle events in the ABAP runtime framework. They are introduced by an event key word and ended by the next processing block. Since there is no closing statement, it is recommended that the end of an event block is indicated with a comment line.

Within an event block, no local data types or data objects can be declared. All declarative statements in event blocks are part of the global data declarations of the ABAP program, and are visible in all subsequent processing blocks. An event block works with the global data types and data objects of the [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md), and therefore should not contain any separate declarations. **Exception:** The event blocks `AT SELECTION-SCREEN ...` and `GET ...`, which are implemented internally as procedures and can contain local data.

For reasons of data encapsulation, it is recommended that only very few functions are implemented in event blocks, and to call methods instead.

The following are the possible events:

- [Program constructor event](abenprogram_constructor.md)
