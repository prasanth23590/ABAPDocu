---
title: "Return Values of Functional Methods"
source_file: abentyping_return_values.html
section: "ABAP Programming Language > ABAP - Declarations > Typing > Checking Typing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Return Values of Functional Methods

The return value of a [functional method](../../abap-glossary/abenfunctional_method_glosry.md) is always completely typed and is always passed by value. An actual parameter can be appended to the return value as follows:

- Specification of the method in an [operand position](../abap-operands/abenoperands_expressions.md)

  If a functional method is used in an operation position, the return value is used like a data object whose data type is determined with an exception by the complete typing of the return value (a type-compliant actual parameter is implicitly bound to it). Checking of this typing is not necessary (or is always successful). An error always occurs, however, if the typing of the return value is not compatible with the [operand type](../../abap-glossary/abenoperand_type_glosry.md). If the return value of a functional method is bound as an actual parameter to a generically typed formal parameter of type `p`, the method inherits the decimal places of the return value but not its length. In this case the formal parameter is given a length of 16.

- [Method call](../abap-obsolete-language-elements/abapcall_method_static.md) with the addition [`RECEIVING`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md)

  If an actual parameter is specified explicitly after `RECEIVING`, it does not have to comply with the [general typing rules](abentyping_check_general.md) for typing the formal parameter. Instead, it is enough if the formal parameter can be converted to the actual parameter in accordance with the [conversion rules](../abap-processing-internal-data/abenconversion_rules.md).

If an exception is raised when the return value is assigned to a formal parameter or when it is used as an operand, it cannot always be handled, but cause a runtime error, depending on the operand position.

## Hints

- If reference variables are returned using `RECEIVING`, an [upcast](../../abap-glossary/abenup_cast_glosry.md) is possible but a [downcast](../../abap-glossary/abendown_cast_glosry.md) is not.

- The special rule that a generic formal parameter of type `p` gets the length of 16 when a functional method is passed does not apply to the other generic types `any`, `data`, `simple`, or `numeric`.
