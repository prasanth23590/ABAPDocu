---
title: "Program-Initiating Statements"
source_file: abenabap_program_statement.html
section: "ABAP Programming Language > ABAP - Program Structure"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Program-Initiating Statements

The program-initiating statements are:

- [`FUNCTION-POOL`](abapfunction-pool.md)

- [`CLASS-POOL`](abapclass-pool.md)

- [`INTERFACE-POOL`](abapinterface-pool.md)

The initiating statement of each program depends on the program type specified in the [program properties](../../abap-glossary/abenprogram_property_glosry.md).

All statements that follow the program-initiating statements in the source code or that are included as [include programs](../../abap-glossary/abeninclude_program_glosry.md) are handled as a single unit by ABAP Compiler.

The first statement of every standalone ABAP program must be a program-initiating statement, and each program can only contain one of these statements. The only other statement allowed at the first position instead of the initiating statement is the statement `INCLUDE`. In this case, a program-initiating statement must appear at the first position of the program after the include program is resolved when it is generated.

Class pools, interface pools, function pools are independent [compilation units](../../abap-glossary/abencompilation_unit_glosry.md). Include programs, on the other hand, are only used in the context of compilation units.
