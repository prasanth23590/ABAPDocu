---
title: "Calling Processing Blocks"
source_file: abencall_processing_blocks.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Calling Processing Blocks

In every [processing block](../../abap-glossary/abenprocessing_block_glosry.md) of an ABAP program, processing blocks of the same program can be called (internal calls) or processing blocks of other ABAP programs can be called (external calls).

- Direct [call of procedures](abencall_procedures.md).

- Indirect call of [event handlers](abencall_event_handler.md) by raising events from the same class in methods. This supplies the interface of the event handler. A prerequisite for the execution of an event handler is its [registration](abapset_handler.md).
