---
title: "Exiting Processing Blocks"
source_file: abenleave_processing_blocks.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Exiting Program Units"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exiting Processing Blocks

[Processing blocks](../../abap-glossary/abenprocessing_block_glosry.md) can be exited implicitly using:

- [regular exiting](abenend_processing_blocks.md)

or program-driven, using:

- [`RETURN`](abapreturn.md)

- [`EXIT`](abapexit_processing_blocks.md)

- [`CHECK`](abapcheck_processing_blocks.md)

The subsequent program flow depends on the type of processing block.

In addition to the statements described here, statements that call other units without returning to the caller after the call is made, also terminate their processing block. These include:

[Messages](../../abap-glossary/abenmessage_glosry.md) and raised [exceptions](../../abap-glossary/abenexception_glosry.md) can also exit processing blocks.

## Hints

- Exiting a procedure using `RETURN`, `EXIT` or `CHECK` is the error-free termination of the procedure. Formal parameters for which the pass by value is defined are not passed to the assigned actual parameters only if the procedure terminates after an error (an exception is raised or a message is sent).
