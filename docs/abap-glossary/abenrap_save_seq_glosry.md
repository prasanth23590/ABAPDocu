---
title: "RAP save sequence"
source_file: abenrap_save_seq_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP save sequence

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

The RAP save sequence is part of the [RAP BO](abenrap_bo_glosry.md) runtime and is triggered after at least one successful modification was performed during the [interaction phase](abenrap_int_phase_glosry.md). It saves data from the [transactional buffer](abentransactional_buffer_glosry.md) on the database.

The RAP save sequence is divided into three phases that are entered in this order:

- [RAP early save phase](abenearly_rap_save_phase_glosry.md)

- [RAP late save phase](abenlate_rap_save_phase_glosry.md)

- [RAP cleanup phase](abenrap_cleanup_phase_glosry.md)
