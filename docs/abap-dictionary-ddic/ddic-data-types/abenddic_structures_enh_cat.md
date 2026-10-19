---
title: "DDIC - Enhancement Category of Structures"
source_file: abenddic_structures_enh_cat.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures > DDIC - Technical Properties of Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Enhancement Category of Structures

DDIC structures and DDIC database tables that are delivered by SAP can be extended using [customizing includes](../../abap-glossary/abencustomizing_include_glosry.md) or [append structures](../../abap-glossary/abenappend_structure_glosry.md).

These types of changes cause problems if the extensions change the [structure fragment view](../../abap-glossary/abenunicode_fragment_view_glosry.md). For this reason, DDIC structures and DDIC database tables are classified in order to be able to recognize and handle problems related to structure extensions. This classification is used in the syntax check for ABAP programs to create a warning at all positions where a program works with structures, and where later structure extensions could cause syntax errors or changed program behavior. When a structure or a DDIC database table is defined in the ABAP Dictionary, the enhancement categories shown in the following table can be used as a classification.

| **Level** | **Category**                                | **Meaning**                                                                    |
|-----------|---------------------------------------------|--------------------------------------------------------------------------------|
| 1         | Not classified                              | The structure does not have an enhancement category.                           |
| 2         | Cannot be enhanced                          | The structure must not be extended.                                            |
| 3         | Can be enhanced (character-like)            | All structure components and their extensions must be character-like and flat. |
| 4         | Can be enhanced (character-like or numeric) | All structure components and their extensions must be flat.                    |
| 5         | Can be enhanced (deep)                      | All structure components and their extensions can have any data type.          |

The warnings from the program check are classified into three levels, depending on the effects of the allowed structure extensions:

| **Level** | **Type of Check** | **Meaning**                                                                                                         |
|-----------|-------------------|---------------------------------------------------------------------------------------------------------------------|
| A         | Syntax check      | An extension that completely exhausts the enhancement category of the affected structure produces a syntax error.   |
| B         | Extended check    | Permitted extensions can produce syntax errors, but not always.                                                     |
| C         | Extended check    | Permitted extensions cannot produce syntax errors, although changes to program behavior do cause semantic problems. |

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

If the structure `ddic_struc` in the ABAP Dictionary is defined only with [flat](../../abap-glossary/abenflat_glosry.md) components but is classified as *Can be enhanced (deep)*, the following program section produces a warning in the syntax check. If the structure were to be extended by a [deep](../../abap-glossary/abendeep_glosry.md) component after the program was delivered, the program would have incorrect syntax and would no longer be executable. In this case, therefore either the structure `ddic_struc` must be classified in the ABAP Dictionary as *Can be enhanced (character-like)* or else the offset/length cannot be specified in the program.

``` abap
DATA: my_struc TYPE ddic_struc, 
      str TYPE string, 
      off  TYPE i, 
      len TYPE i. 
... 
str = my_struc+off(len).
```
