---
title: "Chainings"
source_file: abencomponent_chaining_selector.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions > Notations for Single Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Chainings

If a deeply nested subcomponent is used at an operand position, the operand must be denoted as a chaining of all components leading to this subcomponent. This chaining contains a suitable component selector between each component. The following rules apply to such [chained names](../../abap-glossary/abenchained_name_glosry.md):

- Taken together, the names to the left of each structure component selector must address a structured data type or a structure.

- Taken together, the names to the left of each object component selector must address a reference variable.

- The class component selector can occur in a name exactly once as the first selector.

- The interface component selector can only occur more than once in a name if other component selectors are listed between the individual interface component selectors.

- If components are addressed dynamically in parentheses behind a [structure](abenstructure_component_selector.md) or [object component](abenobject_component_selector.md) selector, no static components specification can follow a dynamic specification. Once, a dynamic component specification is done, all following components must also be specified dynamically.

## Hint

In addition to the chaining of names, the following chainings are possible:

- [Method chainings](../../abap-glossary/abenmethod_chaining_glosry.md) with the object component selector

- [Chainings](../abap-processing-internal-data/abentable_exp_chaining.md) of [table expressions](../../abap-glossary/abentable_expression_glosry.md)

Chainings can be combined in any way as long as the corresponding rules are respected.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a nested structured data type `struc2` in `struc1` and a structure `struc3` in an interface `i1`.

The component `comp` of `struc3` is a data reference variable of the static type `struc1`. The `i1` interface is the component interface of `i2` and the latter is implemented in `c1`. In `c2`, a [static attribute](../../abap-glossary/abenstatic_attribute_glosry.md) is declared as the object reference of the static type `c1`. The expression in the last line can be at an operand position that expects a data object, and identifies the component `comp` of the structure `struc2` in a chaining that starts at class `c2`. A prerequisite for use of the expression is that both reference variables, `oref` and `dref`, point to the respective instances.

``` abap
INTERFACE i1. 
  TYPES: BEGIN OF struc1, 
           ... 
           BEGIN OF struc2, 
             ..., 
             comp TYPE ..., 
             ..., 
           END OF struc2, 
           ... 
         END OF struc1. 
  DATA: BEGIN OF struc3, 
          ... 
          dref TYPE REF TO struc1, 
          ... 
        END OF struc3. 
ENDINTERFACE. 
 
INTERFACE i2. 
  INTERFACES i1. 
ENDINTERFACE. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES i2. 
ENDCLASS. 
 
CLASS c2 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA oref TYPE REF TO c1. 
ENDCLASS. 
 
... 
 
... c2=>oref->i1~struc3-dref->struc2-comp ...
```
