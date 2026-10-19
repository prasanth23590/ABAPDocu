---
title: "Checking Typing"
source_file: abentyping_check.html
section: "ABAP Programming Language > ABAP - Declarations > Typing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Checking Typing

When data objects are assigned to typed [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) and [actual parameters](../../abap-glossary/abenactual_parameter_glosry.md) are assigned to typed [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) of [procedures](../../abap-glossary/abenprocedure_glosry.md), the system checks whether the data type of the assigned data object matches the typing of the field symbol or of the formal parameter.

- [General rules for typing](abentyping_check_general.md)

Special rules apply to:

- [Return values of functional methods](abentyping_return_values.md)

- [Literals as actual parameters](abentyping_literals.md)

- [Expressions as actual parameters](abentyping_arith_expr.md)

## Hint

When specifying data objects suitable for a typing, an assignment to a helper variable with a valid data type is often made. When methods are called, these helper variables can often be spared by using a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) in the position of an actual parameter.
