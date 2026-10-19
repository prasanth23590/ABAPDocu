---
title: "Data Objects in Read Positions"
source_file: abendata_objects_usage_reading.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Data Objects in Read Positions

Data objects can be specified as follows at [read positions](../../abap-glossary/abenread_position_glosry.md).

- Specification of a [literal](../../abap-glossary/abenabap_literal_glosry.md).

- Specification of a [data object visible](../abap-data-types-and-data-objects/abenlifetime_and_visibility.md) at this position using the identifier `dobj`, a [field symbol](../../abap-glossary/abenfield_symbol_glosry.md) `<fs>`, or a data reference `dref->*` dereferenced using the [dereferencing operator](../../abap-glossary/abendereferencing_operat_glosry.md) `->*` if `dref` is typed completely.

  Here, the identifiers of data objects also include the specification of [text symbols](../../abap-glossary/abentext_symbol_glosry.md) using the following:

`... text-idf ...`,

Here, `idf` is the three-character ID of the text symbol or chaining of reference variables. If a field symbol is used, it must be assigned to a memory area and a data reference must point to a data object, otherwise an uncatchable exception is raised. As an alternative to specifying a text symbol using `text-idf`, the three-character ID of a text symbol can also be appended to the [text field literal](../../abap-glossary/abentext_field_literal_glosry.md) in parentheses:

`... '...'(idf) ...`

If the text symbol exists in the currently loaded [text pool](../../abap-glossary/abentext_pool_glosry.md), then the content of the corresponding text symbol is used instead of the text field literal, otherwise the literal is used.

- If the data object is an internal table, the expressions `dobj[]`, `<fs>[]`, or `dref->*[]` can also be used. An exception to this is specification of the internal table of a [table expression](../../abap-glossary/abentable_expression_glosry.md), where `[]` cannot be appended to the name.

- Specification of a [subarea](abenoffset_length.md) of a character-like or byte-like data object -or a character-like initial part of a structure- by specifying an [offset/length](../../abap-glossary/abenoffset_length_specific_glosry.md).

- At some positions, numeric values must be specified directly as digits. In contrast to [numeric literals](../../abap-glossary/abennumeric_literal_glosry.md), it is often not possible to specify a plus/minus sign. Examples are numbers specified in declarative statements for the length of elementary data objects or for the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md) of internal tables.

## Hints

- Text symbols cannot be listed at all read positions. For example, they are not allowed for specifying the target of dynamic [executions](../abap-calling-and-exiting-program-units/abenabap_execution.md).

- A [system field](../../abap-glossary/abensystem_field_glosry.md) should only be specified as an operand in a read position if its content is not set by the same statement. Otherwise, this can lead to undefined system behavior.

- The predicate expressions [`IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) and [`IS BOUND`](../abap-program-flow-logic/abenlogexp_assigned.md) can be used to check the usability of field symbols and data references.

- A data reference variable with a generic static type can only be deserialized using the statement [`ASSIGN dref->* TO <fs>`](../abap-processing-internal-data/abapassign_mem_area_dynamic_dobj.md).

- At many read positions, [functions or expressions](abenoperands_expressions.md) can be specified instead of data objects.

- [Enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) with an [enumerated type](../../abap-glossary/abenenum_type_glosry.md) can be used in all read positions in which the operand type is their enumerated type or in which the operand is converted to one of the character-like types `c` or `string`.
