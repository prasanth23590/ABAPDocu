---
title: "Data Objects in Write Positions"
source_file: abendata_objects_usage_writing.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Data Objects in Write Positions

Only modifiable data objects, that is, no literals, text symbols, constants, or non-modifiable formal parameters, can be specified as follows at [write positions](../../abap-glossary/abenwrite_position_glosry.md):

- Specification of a [visible data object](../abap-data-types-and-data-objects/abenlifetime_and_visibility.md) specified at this position using the identifier `dobj`, a field symbol `<fs>`, or a dereferenced data reference `dref->*` if `dref` is typed completely. Like in [read positions](../../abap-glossary/abenread_position_glosry.md), `[]` can be appended to internal tables to address the [table body](../../abap-glossary/abentable_body_glosry.md).

- Specification of a [subarea](abenoffset_length.md) of a [flat](../../abap-glossary/abenflat_glosry.md) character-like or byte-like data object using an [offset/length](../../abap-glossary/abenoffset_length_specific_glosry.md) specification. An offset or length specification cannot be made in write positions for data objects of the [deep](../../abap-glossary/abendeep_glosry.md) data types `string` and `xstring`.

- At a [declaration position](../../abap-glossary/abendeclaration_position_glosry.md), an [inline declaration](../../abap-glossary/abeninline_declaration_glosry.md) of a data object or field symbol can be made using a [declaration expression](../../abap-glossary/abendeclaration_expression_glosry.md).

- [Writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) can be listed in a [result position](../../abap-glossary/abenresult_position_glosry.md).

The following write positions can be distinguished:

- [Read/write positions](../../abap-glossary/abenread_write_position_glosry.md), where an operand is first read and then written.

- [Write-only positions](../../abap-glossary/abenwrite_only_position_glosry.md), where an operand is overwritten without being read first. For the time being, those are [declaration positions](../../abap-glossary/abendeclaration_position_glosry.md) only.

## Hints

- In [result positions](../../abap-glossary/abenresult_position_glosry.md), certain [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) can be specified.

- [Enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md) can only be used in write positions where the operand type is the enumerated type and only the associated [enumerated values](../../abap-glossary/abenenumerated_value_glosry.md) can be written.
