---
title: "rel_exp - Comparing Structures"
source_file: abenlogexp_rules_operands_struc.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparing Structures

It is possible to compare structures with structures and structures with elementary fields:

- [Compatible](../abap-data-types-and-data-objects/abencompatibility.md) structures are compared component by component, whereby any nested structures are resolved recursively. Two structures are equal if the content of their components matches. In the case of unequal structures, the first unequal component pair determines the result of the comparison.

- It is possible to compare incompatible structures and structures with elementary fields provided that the structures concerned are [flat](../../abap-glossary/abenflat_glosry.md).

  - Comparisons between two flat structures require that their [fragment views](../../abap-glossary/abenunicode_fragment_view_glosry.md) match for the length of the shorter structure. Before the comparison, the shorter structure is padded to the length of the longer structure. Here, all character-like components are padded with blanks and all other components with their type-dependent [initial value](../../abap-glossary/abeninitial_value_glosry.md). The comparison then takes place in stages according to the fragment view.

  - Comparisons between a flat structure and an elementary field are subject to the following rules:

    If the flat structure is character-like, it is handled in the comparison as an elementary field of type `c`. If the flat structure is not just character-like, the elementary field must have the type `c` and the first fragment of the [structure fragment view](../../abap-glossary/abenunicode_fragment_view_glosry.md) must be character-like and at least as long as the elementary field. If the elementary field is shorter than the structure, it is extended to the length of the structure before the comparison and then handled implicitly like a structure. The character-like parts of the extension are padded with blanks and all other components are padded with their type-dependent initial value.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following comparison is true because the structure is handled like a field of type `c` with length 8.

``` abap
TYPES: 
  BEGIN OF struc, 
    year  TYPE c LENGTH 4, 
    month TYPE c LENGTH 2, 
    day   TYPE c LENGTH 2, 
  END OF struc. 
 
FINAL(date)  = cl_demo_date_time=>get_user_date( ). 
FINAL(struc) = VALUE struc( year  = date(4) 
                            month = date+4(2) 
                            day   = date+6(2) ). 
 
ASSERT date = struc.
```
