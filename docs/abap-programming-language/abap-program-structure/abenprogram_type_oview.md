---
title: "ABAP Program Types"
source_file: abenprogram_type_oview.html
section: "ABAP Programming Language > ABAP - Program Structure"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Program Types

The type of an ABAP program determines, among other things, which declarations and processing blocks a program can contain and how it can be executed in the ABAP runtime framework.

The following table shows the program types for standalone programs ([compilation units](../../abap-glossary/abencompilation_unit_glosry.md)) and how they affect their properties:

| **Program Type**                                                                                   | **Program-Initiating Statement**            | **Execution**                                                             | **Global Declarations**                                                                                                                       | **Processing Blocks**                        | **Dynpros** | **Text Pools** |
|----------------------------------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|-------------|----------------|
| [Class pool](../../abap-glossary/abenclass_pool_glosry.md)                                                           | [`CLASS-POOL`](abapclass-pool.md)         | [Call](../abap-calling-and-exiting-program-units/abenmethod_calls.md) of a visible method                         | A global class of the class library, local interfaces and classes, statements [`TYPES`](../abap-declarations/abaptypes.md) and [`CONSTANTS`](../abap-declarations/abapconstants.md) | Methods only                                 | No          | Yes            |
| [Interface pool](../../abap-glossary/abeninterface_pool_glosry.md)                                                   | [`INTERFACE-POOL`](abapinterface-pool.md) | None                                                                      | A global interface of the class library                                                                                                       | None                                         | No          | No             |
| [Function pool](../../abap-glossary/abenfunction_pool_glosry.md) or [function group](../../abap-glossary/abenfunction_group_glosry.md) | [`FUNCTION-POOL`](abapfunction-pool.md)   | Call of a function module using [`CALL FUNCTION`](../abap-calling-and-exiting-program-units/abapcall_function.md) | Local interfaces and classes, all other declarative statements                                                                                | All except event blocks for reporting events | Yes         | Yes            |

The second column of the table shows the respective [program-initiating statement](abenabap_program_statement.md), the third column shows the type of execution for which the program type is mainly designated. The fourth column shows which declarations can be made in the [global declaration part](../../abap-glossary/abenglobal_declaration_sect_glosry.md) of a program with the specified type. The fifth column indicates which [processing blocks](../../abap-glossary/abenprocessing_block_glosry.md) the program can contain. The sixth column indicates whether standalone dynpros are supported. The final column indicates whether standalone [text pools](../../abap-glossary/abentext_pool_glosry.md) can be created.
