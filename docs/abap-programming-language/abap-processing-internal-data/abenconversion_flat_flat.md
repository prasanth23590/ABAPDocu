---
title: "Conversion Between Flat Structures"
source_file: abenconversion_flat_flat.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Between Flat Structures

When flat structures are converted, the [fragment view](../../abap-glossary/abenunicode_fragment_view_glosry.md) of the structures must be considered. The following rules apply when converting a flat structure to another flat structure.

- When assigning structures with the same fragment view, the structure is assigned unconverted.

- When assigning structures of different lengths where the length of the [fragment view](abenunicode_fragment_view.md) exactly matches the length of the shorter structure, the assignment is made in the length of the shorter structure without conversion.

  - If the target structure is longer than the source structure, the components of the target structure located behind the shared fragments are filled with type-dependent [initial values](../../abap-glossary/abeninitial_value_glosry.md) and any alignment gaps are set to hexadecimal 0.

  - If the target structure is shorter than the source structure, the components of the source structure located behind the shared fragments are cut off.

- When assigning structures of different lengths whose fragment views match until the second last fragment of the shorter structure, and in which the next fragment is either character-like in one and byte-like in the other, the part in which the fragments are the same is assigned unconverted. The characters of the next fragment of the source structure are assigned to the corresponding fragment of the target structure without conversion and left-aligned. If this fragment in the target structure is greater than that in the source structure, the right hand side is padded with blanks or with hexadecimal 0, depending on the data type. If it is shorter, it is truncated on the right. The remaining components after this fragment are either cut off or padded. **Note:** Fields of types `n`, `d`, and `t` are handled like type `c`, meaning they are padded with spaces. In case of deep component types, the type check is strict, and it is checked for type compatibility.

No conversion rule is defined for any other cases, which means that no assignment is possible.

## Hints

- If components of data type `p` occur in the involved structures, these components form individual fragments for which only the length is significant and not the number of decimal places. When assigning such structures, the value of the source components of type `p` is cast to the number of decimal places of the target components, and the decimal point may shift. This means that the result for such a component can differ from the result of a direct assignment between the components.

- If a component of a flat structure has an [enumerated type](../../abap-glossary/abenenum_type_glosry.md), this is a separate fragment of the fragment view, regardless of its [basis type](../../abap-glossary/abenbase_type_glosry.md), and must exist at the same position and with the same type in assignments between these structures in the source and target structure.

- Since only [Unicode systems](../../abap-glossary/abenunicode_system_glosry.md) are supported in which a character is always represented by 2 bytes, the conversion rules for flat structures are less strict than in systems in which also non-Unicode systems are still supported. There, all possible alignment requirements for characters have to be considered, regardless of the actual length of a character in its character representation. When downporting programs from higher to lower releases, syntax errors might occur in the lower releases because of the stricter rules there.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following assignment between two flat structures is possible in the current release, but it was not possible as long as non-Unicode systems were still supported. In the included substructure `incl1`, the character component has the same alignment as the integer component and there is no alignment gap. However, as long as non-Unicode Systems were supported, an alignment gap had to be assumed behind the included structure in order to make the program executable in Unicode systems as well as in non-Unicode Systems.

``` abap
TYPES: 
  BEGIN OF incl1, 
    num TYPE i, 
    c2  TYPE c LENGTH 2, 
  END OF incl1. 
 
DATA: 
  BEGIN OF struc1, 
    c1 TYPE c LENGTH 2. 
    INCLUDE TYPE incl1. 
DATA: 
    c3 TYPE c LENGTH 2, 
  END OF struc1. 
 
DATA: 
  BEGIN OF struc2, 
    c1  TYPE c LENGTH 2, 
    num TYPE i, 
    c2  TYPE c LENGTH 2, 
    c3  TYPE c LENGTH 2, 
  END OF struc2. 
 
struc1 = struc2.
```
