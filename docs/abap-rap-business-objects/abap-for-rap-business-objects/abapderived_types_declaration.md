---
title: "Declaring Data Objects and Types with BDEF Derived Types"
source_file: abapderived_types_declaration.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Declaring Data Objects and Types with BDEF Derived Types

For the purpose of modularization, many [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) can be used outside of the reserved handler methods by declaring variables, for example, in ABAP programs. The statements `TYPES`, `DATA` and `CREATE DATA` are supported. For example, an internal table can be declared with the type [`TYPE TABLE FOR`](abaptype_table_for.md):

``` abap
TYPES tab_type TYPE TABLE FOR CREATE entity_name. 
DATA itab TYPE TABLE FOR CREATE entity_name.
```

`entity_name` must be the full name of the entity, and not the alias defined in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md), as there is no clear reference to a specific BDEF outside of handler methods in [behavior pools](../../abap-glossary/abenbehavior_pool_glosry.md).

Typing method parameters with BDEF derived types can be done by referencing an existing type, for example, as follows:

``` abap
... 
TYPES tab_type TYPE TABLE FOR CREATE demo_managed_root. 
METHODS some_meth IMPORTING itab TYPE tab_type. 
...
```

The following type declarations are supported in the context of BDEF derived types:

- [`TYPE TABLE FOR`](abaptype_table_for.md)

- [`TYPE STRUCTURE FOR`](abaptype_structure_for.md)

- [`TYPE REQUEST FOR`](abaptype_request_for.md)

- [`TYPE RESPONSE FOR`](abaptype_response_for.md)

**Declaration Options with BDEF Derived Types**

The following options are available for declaring types and data objects with BDEF derived types after ... FOR ...:

- Specifying the name of the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md), followed by `\\` and an entity of the composition tree

  - After `\\`, an alias name must be specified if an alias is defined for the entity. Otherwise, the entity name can be specified.

  - For example, `TYPES t1 TYPE TABLE FOR CREATE demo_managed_root\\demo_managed_root.`. The demo BDEF does not specify an alias name for the root entity. The example BDEF `DEMO_MANAGED_ROOT_WAS` specifies an alias for the root entity, therefore a type declaration can look like this: `TYPES t2 TYPE TABLE FOR CREATE demo_managed_root_was\\_root.`

- For convenience and as a shorter form of the previous declaration option, specifying [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md) such as the name of the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md) (i.e. the name of the BDEF) or other [CDS entities](../../abap-glossary/abencds_entity_glosry.md) of a [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) is possible

  - For example, `TYPES t3 TYPE TABLE FOR CREATE demo_managed_root.` and `TYPES t4 TYPE TABLE FOR CREATE demo_managed_root_was.`, which are the same as *t1* and *t2* respectively.

- Specifying [associations](../../abap-glossary/abencds_association_glosry.md) defined in a BDEF preceded by `\`

  - For example, `TYPES t5 TYPE TABLE FOR CREATE demo_managed_root_was\_child.`

  - Note that the longer version with `\\` followed by an entity name, `\` and an association is also possible.

**Note:**

- You can only declare types and data objects with specific BDEF derived types according to specifications in the BDEF. For example, you can only declare a type with `... FOR CREATE ...` when create operations are enabled in the BDEF.

- Several BDEF derived types can only be used in [ABAP behavior pools](../../abap-glossary/abenbehavior_pool_glosry.md).

- In [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md), you can display BDEF derived type information with F2, which typically shows the long version.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following type and data object declarations with BDEF derived types demonstrate the described declaration options.

``` abap
"Specifying RAP BO entities 
"Specifying the RAP BO root entity 
TYPES t1 TYPE TABLE FOR CREATE demo_managed_root_was. 
DATA d1 TYPE TABLE FOR CREATE demo_managed_root_was. 
"Specifying child entity 
TYPES t2 TYPE TABLE FOR UPDATE demo_managed_child_was. 
DATA d2 TYPE TABLE FOR UPDATE demo_managed_child_was. 
 
"Specifying the name of the RAP BO root entity, followed by \\ and an 
"entity of the composition tree 
"If an alias name for the entity is specified, it must be specified 
"after \\. Otherwise, the entity name can be specified. 
"t3/d3 are the same as t1/d1. 
TYPES t3 TYPE TABLE FOR CREATE demo_managed_root_was\\_Root. 
DATA d3 TYPE TABLE FOR CREATE demo_managed_root_was\\_Root. 
"In this example, t4/d4 are the same as t2/d2. 
TYPES t4 TYPE TABLE FOR UPDATE demo_managed_root_was\\_Child. 
DATA d4 TYPE TABLE FOR UPDATE demo_managed_root_was\\_Child. 
 
"Specifying associations of the RAP BO preceded by \ 
"In this example, t5/d5 are the same as t6/d6. 
TYPES t5 TYPE TABLE FOR CREATE demo_managed_root_was\_child. 
DATA d5 TYPE TABLE FOR CREATE demo_managed_root_was\_child. 
TYPES t6 TYPE TABLE FOR CREATE demo_managed_root_was\\_Root\_child. 
DATA d6 TYPE TABLE FOR CREATE demo_managed_root_was\\_Root\_child. 
"In this example, t7/d7 are the same as t8/d8. 
TYPES t7 TYPE TABLE 
  FOR READ IMPORT demo_managed_root_was\\_Child\_parent. 
DATA d7 TYPE TABLE 
  FOR READ IMPORT demo_managed_root_was\\_Child\_parent. 
TYPES t8 TYPE TABLE FOR READ IMPORT demo_managed_child_was\_parent. 
DATA d8 TYPE TABLE FOR READ IMPORT demo_managed_child_was\_parent.
```

## Executable Example

The class `CL_DEMO_RAP_EML_EXPLICIT_DECL` demonstrates the explicit declaration of variables with BDEF derived types with a simple EML `READ` statement.
