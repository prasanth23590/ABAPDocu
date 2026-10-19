---
title: "Notations for Single Operands"
source_file: abenoperands_names.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Notations for Single Operands

A single operand, that is, an operand that is not an expression, can either be elementary or be a combination of components. Composite operands are:

- Structured data types or data objects (structure)

- Instances of classes (objects)

- Classes

- Interfaces

As a consequence, names for operands are either elementary names or names constructed from multiple names separated by component selectors. An elementary name is used for addressing the following:

- Elementary operands

- Components that are unique in the current context

- Superunits made up of components

[Naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the elementary names. Composite names with component selectors are used for addressing individual components. A component can itself be a superunit of further components. Subcomponents can be addressed by [chaining](../../abap-glossary/abenchaining_glosry.md) multiple names.

- [Structure Component Selector](abenstructure_component_selector.md)

- [Object Component Selector](abenobject_component_selector.md)

- [Class Component Selector](abenclass_component_selector.md)

- [Interface Component Selector](abeninterface_component_selector.md)

- [Dereferencing Operator](abendereferencing_operator.md)

- [Chainings](abencomponent_chaining_selector.md)

- [Offset/Length Specifications for Substring Access](abenoffset_length.md)

## Hint

In addition to the component selectors listed here, [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) also has a [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) (`~`).
