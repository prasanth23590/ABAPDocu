---
title: "Heap References and Stack References"
source_file: abenheap_stack_reference.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > References"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Heap References and Stack References

The objects referenced by references can be in the [heap](../../abap-glossary/abenheap_glosry.md) or in the [stack](../../abap-glossary/abenstack_glosry.md). Objects in the heap are instances of classes or are [anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md). Objects in the stack are the global data objects of programs and the local data objects of procedures stacked there.

- **Heap references** point to objects or parts of objects in the heap

  Heap references are object references or data references. They are created either when new objects are created in the heap using the statements [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md) or [`CREATE DATA`](../abap-creating-objects-and-values/abapcreate_data.md), or when applying the statement [`GET REFERENCE`](../abap-processing-internal-data/abapget_reference.md) or the addition [`REFERENCE INTO`](../abap-processing-internal-data/abapread_table_outdesc.md) to data objects in the heap. Heap references are always memory-preserving, which means that for as long as a heap reference points to an object or a part of an object, it is not deleted by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md).

- **Stack references** point to objects or parts of objects in the stack

  Stack references are always data references and are created exclusively by applying the statement [`GET REFERENCE`](../abap-processing-internal-data/abapget_reference.md), the reference operator [`REF`](../abap-processing-internal-data/abenconstructor_expression_ref.md), or the addition [`REFERENCE INTO`](../abap-processing-internal-data/abapread_table_outdesc.md) to data objects in the stack. Stack references are not memory-preserving.

A non-initial object reference always points to an instance of a class and is therefore always a heap reference. A data reference can be a heap reference or a stack reference:

- A data reference is a heap reference if it

  - points to an instance attribute or a part of an instance attribute of an object,

  - points to an anonymous data object or a part of an anonymous data object.

- A data reference that points to a data object or a part of a data object in the stack is a stack reference.

A part of a data object is either a [structure component](../../abap-glossary/abenstructure_component_glosry.md), a line of an [internal table](../../abap-glossary/abeninternal_table_glosry.md), or a subarea specified by an [offset/length](../../abap-glossary/abenoffset_length_specific_glosry.md).

Heap references preserve memory and therefore cannot become invalid, with one exception: a heap reference to a line of an internal table becomes invalid if the table line is deleted. Stack references also become invalid if the referenced data object is removed from the stack, that is, when the associated procedure ends. The latter also applies to the local data in instance methods. The [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`IS BOUND`](../abap-program-flow-logic/abenlogexp_bound.md) for an invalid reference is false.

## Hints

- For [field symbols](../../abap-glossary/abenfield_symbol_glosry.md), the same applies in regard to preserving memory and validity as to data references. Field symbols to which objects or parts of objects are assigned in the heap are memory-preserving.

- Internal tables are [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md) and have a special role because they have their own memory management, which occupies and releases memory regardless of the statement `CREATE` and Garbage Collector. This means that heap references that point to lines in internal tables can become invalid. This is not the case for strings, since no references to substrings of strings are allowed.

- Whether a reference is classified as a heap reference or a stack reference is determined by its value and not by the type of the reference variable in which it is stored. Assignments between reference variables in particular do not change the corresponding properties of the copied references.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The heap reference `heap_ref` on the [stack](../../abap-glossary/abenstack_glosry.md) points to an anonymous data object in the [heap](../../abap-glossary/abenheap_glosry.md). The stack reference `stack_ref` also on the stack points to `heap_ref`.

``` abap
FINAL(heap_ref)  = NEW i( 111 ). 
FINAL(stack_ref) = REF #( heap_ref ).
```
