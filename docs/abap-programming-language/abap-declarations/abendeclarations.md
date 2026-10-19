---
title: "ABAP - Declarations"
source_file: abendeclarations.html
section: "ABAP Programming Language"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP - Declarations

Declarations define the properties of program local [classes](../../abap-glossary/abenclass_glosry.md), [interfaces](../../abap-glossary/abenoo_intf_glosry.md), [data types](../../abap-glossary/abendata_type_glosry.md), [data objects](../../abap-glossary/abendata_object_glosry.md) and [field symbols](../../abap-glossary/abenfield_symbol_glosry.md). Declarations are made either with [declaration statements](../../abap-glossary/abendeclaration_statement_glosry.md) or as [inline declarations](../../abap-glossary/abeninline_declaration_glosry.md) using [declaration expressions](../../abap-glossary/abendeclaration_expression_glosry.md). Furthermore, inside [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) local helper variables can be declared with `LET` expressions.

Besides the declarations shown here, the [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) of the [parameter interface](../../abap-glossary/abenparameter_interface_glosry.md) of a [procedure](../../abap-glossary/abenprocedure_glosry.md) can be declared with the respective [modularization statements](../abap-program-structure/abenabap_language_modularization.md). For those and also for field symbols, the date type can be either [complete](../../abap-glossary/abencomplete_typing_glosry.md) or [generic](../../abap-glossary/abengeneric_typing_glosry.md) and the definition of that type is called [typing](../../abap-glossary/abentyping_glosry.md).

- [Declaration Statements](abenabap_declarations.md)

- [Inline Declarations](abeninline_declarations.md)

- [Local Declarations in Constructor Expressions](abenlocal_expr_declarations.md)

- [Typing](abentyping.md)

## Hints

- The declared entity is visible statically as soon as it is declared and is valid throughout its entire [context](../../abap-glossary/abenobj_context_glosry.md).

- Entities declared in [class pools](../../abap-glossary/abenclass_pool_glosry.md) and [interface pools](../../abap-glossary/abeninterface_pool_glosry.md) are program local within these but can be made public for external usage. This involves [global classes](../../abap-glossary/abenglobal_class_glosry.md), [global interfaces](../../abap-glossary/abenglobal_interface_glosry.md) and their [public](../../abap-glossary/abenpublic_glosry.md) components.

- Local declarations always hide the more global declarations of the superordinate contexts.
