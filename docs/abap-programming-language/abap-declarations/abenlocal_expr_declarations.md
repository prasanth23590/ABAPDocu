---
title: "Local Declarations in Constructor Expressions"
source_file: abenlocal_expr_declarations.html
section: "ABAP Programming Language > ABAP - Declarations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Local Declarations in Constructor Expressions

In most [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), variables and field symbols can be declared as local fields. The declaration takes place inside a constructor expression within an embedded

- [`LET` expression `let_exp`](abaplet.md)

`LET` expressions can be used in the following constructor expressions:

- [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md)

  - [Single values](../abap-creating-objects-and-values/abennew_constructor_params_single.md)

  - [Structures](../abap-creating-objects-and-values/abennew_constructor_params_struct.md)

  - [Internal tables](../abap-creating-objects-and-values/abennew_constructor_params_itab.md)

  - [Classes](../abap-creating-objects-and-values/abennew_constructor_params_class.md)

- [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md)

  - [Structures](../abap-creating-objects-and-values/abenvalue_constructor_params_struc.md)

  - [Internal tables](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md)

- [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md)

- [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md)

- [`EXACT`](../abap-processing-internal-data/abenconstructor_expression_exact.md)

- [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md)

- [`COND`](../abap-program-flow-logic/abenconditional_expression_cond.md)

- [`SWITCH`](../abap-program-flow-logic/abenconditional_expression_switch.md)

`LET` expressions are also possible in all iteration expressions with [`FOR`](../abap-program-flow-logic/abenfor.md).
