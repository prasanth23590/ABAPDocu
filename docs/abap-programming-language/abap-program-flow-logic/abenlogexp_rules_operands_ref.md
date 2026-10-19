---
title: "rel_exp - Comparing Reference Variables"
source_file: abenlogexp_rules_operands_ref.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparing Reference Variables

It is possible to compare data references with data references and object references with object references, but it is not possible to compare data references with object references. Two reference variables are identical if they point to the same object. Size comparisons are defined internally and always produce similar results in similar situations.

The [null reference](../../abap-glossary/abennull_reference_glosry.md) in an initial reference variable is always smaller than any non-initial reference. However, a non-initial invalid reference that no longer points to an object cannot be compared. A comparison with a non-initial invalid reference always produces an uncatchable exception.

## Hints

- For data references to be identical, the data type of the referenced objects must be [compatible](../abap-data-types-and-data-objects/abencompatibility.md) and it is not enough for the operands just to contain the same reference. If, for example, two reference variables contain the same memory address, with one pointing to a structure and the other to the first component of the structure, these variables are not identical since the data type of the operands is incompatible. Reference variables filled using [`GET REFERENCE`](../abap-processing-internal-data/abapget_reference.md) might not be identical, even though they point to the same data object if `GET REFERENCE` or the reference operator `REF` is executed for a field symbol to which the data object was assigned using [casting](../../abap-glossary/abencast_casting_glosry.md).

- The fact that non-initial invalid references cannot be compared affects all operations with internal tables where comparisons take place, for example, `WHERE` conditions, sorts, or accesses using a sorted key. If a comparison with a non-initial invalid reference takes place, a runtime error occurs.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following comparisons are both true. Although all references created with the reference operator `REF` point to the same data object in the memory, the reference created using `<fs2>` is not equal to the other two because it references another data type.

``` abap
DATA dobj TYPE d. 
ASSIGN dobj TO FIELD-SYMBOL(<fs1>). 
IF REF #( dobj ) = REF #( <fs1> ). 
  ... 
ENDIF. 
 
TYPES text TYPE c LENGTH 8. 
FIELD-SYMBOLS <fs2> TYPE text. 
ASSIGN dobj TO <fs2> CASTING. 
IF REF #( dobj ) <> REF #( <fs2> ). 
  ... 
ENDIF.
```
