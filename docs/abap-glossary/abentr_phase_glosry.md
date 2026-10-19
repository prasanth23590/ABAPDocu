---
title: "transactional phase"
source_file: abentr_phase_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# transactional phase

[ABAP Language](../abap-programming-language/abenabala_glossary.md) [RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

Specifies the concrete phase of a transaction. It is either the modify or the save transactional phase. They are set either implicitly, as in the case of, for example, [RAP handler](abenabp_handler_method_glosry.md) and [saver](abenabp_saver_method_glosry.md) methods, or explicitly using the static methods of class [`CL_ABAP_TX`](../abap-programming-language/abap-database-access/abaprap_cl_abap_tx.md).

In a [RAP transaction](abenrap_luw_glosry.md), the transactional phases are as follows:

- Modify: Includes the [RAP interaction phase](abenrap_int_phase_glosry.md) and the [early save phase](abenearly_rap_save_phase_glosry.md) of the [RAP save sequence](abenrap_save_seq_glosry.md).

- Save: Includes the [RAP late save phase](abenlate_rap_save_phase_glosry.md).
