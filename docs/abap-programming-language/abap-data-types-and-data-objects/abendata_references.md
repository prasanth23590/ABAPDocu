---
title: "References"
source_file: abendata_references.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# References

References are pointers to instances. Pointers to data objects are [data references](../../abap-glossary/abendata_reference_glosry.md). Pointers to instances of classes are [object references](../../abap-glossary/abendata_reference_glosry.md). References occur in ABAP as the content of reference variables. Reference variables are data objects whose data type is a reference type.

Reference types are always created using the addition [`REF TO`](../abap-declarations/abaptypes_references.md). The content of reference variables can be checked using the predicate expression [`IS BOUND`](../abap-program-flow-logic/abenlogexp_bound.md).

The reference type is the static type of a reference variable. It defines to which types of instances its references can point. The dynamic type of a reference variable is the type from which an object was instantiated to which a reference variable points. The static type is always more general than or the same as the dynamic type. A dynamic type can be a data type or a class. A reference type or static type can be a type for a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) or an [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md). The latter are subdivided into [class reference variables](../../abap-glossary/abenclass_reference_variabl_glosry.md) and [interface reference variables](../../abap-glossary/abeninterface_ref_variable_glosry.md).

Special [conversion rules](../abap-processing-internal-data/abenconversion_references.md) apply to assignments between reference variables, depending on the static type. These rules ensure that the dynamic type is never more general than the static type ([upcast](../../abap-glossary/abenup_cast_glosry.md), [downcast](../../abap-glossary/abendown_cast_glosry.md)).

Depending on where the object referenced by a reference variable is stored, memory-preserving [heap references](../../abap-glossary/abenheap_reference_glosry.md) or non-memory-preserving [stack references](../../abap-glossary/abenstack_reference_glosry.md) can be distinguished. Special [weak references](../../abap-glossary/abenweak_reference_glosry.md) that are represented by objects of a system class, do not keep an object alive.

- [Data references](abendata_reference_type.md)

- [Object references](abenobject_reference_type.md)

- [Heap references and stack references](abenheap_stack_reference.md)

A reference in a reference variable is valid if it points to an object. For this, the predicate expression [`IS BOUND`](../abap-program-flow-logic/abenlogexp_bound.md) is true. A non-initial reference can be invalid if it points to deleted objects. A [heap reference](../../abap-glossary/abenheap_reference_glosry.md) that points to a line in an internal table can become invalid if the line is deleted. A [stack reference](../../abap-glossary/abenstack_reference_glosry.md) can become invalid if the referenced data object is removed from the stack.

## Hints

- From a technical perspective, a reference in ABAP does not refer directly to an object but to a header instead, which contains the address of the actual object and other administrative information. See also [Memory Management of Deep Data Objects](abenmemory_consumption.md).

- Internally, [strings](../../abap-glossary/abenstring_glosry.md), [internal tables](../../abap-glossary/abeninternal_table_glosry.md), and [boxed components](../../abap-glossary/abenboxed_component_glosry.md) are also addressed using references, which do not appear as the content of reference variables.
