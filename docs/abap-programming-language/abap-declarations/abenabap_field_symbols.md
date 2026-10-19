---
title: "Field Symbols"
source_file: abenabap_field_symbols.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Field Symbols

Field symbols are declared using the statement [`FIELD-SYMBOLS`](abapfield-symbols.md) or the declaration operator [`FIELD-SYMBOL`](abenfield-symbol_inline.md) and are either placeholders or symbolic names for existing data objects, or parts of existing data objects to which a memory area can be assigned at program runtime. A field symbol does not reserve physical space in the [data area](../../abap-glossary/abendata_area_glosry.md) of a program like a [data object](../../abap-glossary/abendata_object_glosry.md). Instead, it works as a dynamic identifier of a memory area, where a specific data object or part of an object is located. A field symbol can be used instead of data objects at operand positions of statements. When such a statement is executed, a memory area must be assigned to the field symbol using the statement [`ASSIGN`](../abap-processing-internal-data/abapassign.md) or the addition `ASSIGNING` when [processing internal tables](../abap-processing-internal-data/abentable_processing_statements.md).

Field symbols can point to almost any data object. A field symbol is similar to a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) dereferenced using `->*`. Unlike data reference variables, [value semantics](../../abap-glossary/abenvalue_semantics_glosry.md) are used to access a field symbol. Accessing a field symbol is like accessing the named data object or part of the object itself. For data reference variables, however, [reference semantics](../../abap-glossary/abenreference_semantics_glosry.md) apply.

Field symbols are used for generic work with data objects and for explicit [casting](../../abap-glossary/abencast_casting_glosry.md) of data objects, which is only possible using field symbols.

## Hints

- Field symbols to which data objects or parts of data objects are assigned in the [heap](../../abap-glossary/abenheap_glosry.md) act memory-preserving, like [heap references](../../abap-glossary/abenheap_reference_glosry.md).

- From a technical perspective, the field symbols are implemented by references or pointers, which are comparable to references in [data reference variables](../../abap-glossary/abendata_reference_variable_glosry.md). A data reference variable is declared in the same way as every other data object and the memory area for the reference it contains is in the [data area](../../abap-glossary/abendata_area_glosry.md) of the ABAP program. However, the pointer assigned to a field symbol is exclusively managed by the ABAP runtime framework and is located in a memory area, which cannot be accessed directly in an ABAP program.
