---
title: "VALUE, Value Operator"
source_file: abenconstructor_expression_value.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# VALUE, Value Operator

## Syntax

``` abap
... VALUE type( ... ) ...  
```

## Description

A [constructor expression](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) with the value operator `VALUE` creates a result of a data type specified using `type`. The following can be specified for `type`:

- A non-generic data type `dtype`.

- The `#` character as a symbol for the [operand type](../../abap-glossary/abenoperand_type_glosry.md). This specification is only possible if the data type required in an operand position is unique and completely identifiable at compile time. The following exceptions apply:

  - When an initial value [`VALUE #( )`](abenvalue_constructor_params_init.md) is passed to a generically typed formal parameter, the type is derived from the generic type.

  - The operand after `BASE` can be evaluated when a [structure](abenvalue_constructor_params_struc.md) or an [internal table](abenvalue_constructor_params_itab.md) is constructed.

  - When used for a single table expression [`VALUE #( table_exp )`](../abap-processing-internal-data/abentable_exp_result.md).

The operator does the following:

- It creates initial values for any non-generic data types.

- It constructs the content of the following:

  - Structured types

  - Table types

- It controls the type of the result of [table expressions](../../abap-glossary/abentable_expression_glosry.md) and so enables a default value to be specified for any lines not found.

The content of the result is determined by the parameters specified in parentheses. The syntax for passing parameters depends on the type used when the value was constructed. There are specialized types of parameter passing for each possible type.

- Pass by parameter when constructing values:

  - [Initial value for all types](abenvalue_constructor_params_init.md)

  - [Structures](abenvalue_constructor_params_struc.md)

  - [Internal tables](abenvalue_constructor_params_itab.md)

- If a single [table expression](../abap-processing-internal-data/abentable_expressions.md) is specified as a parameter, `VALUE` does not construct a value and controls the type of the [result](../abap-processing-internal-data/abentable_exp_result.md) instead.

In [assignments](../abap-processing-internal-data/abenequals_operator.md) of constructor expressions to a data object using `VALUE`, the data object is used directly. It is completely overwritten with an initial value or start value before it is assigned the values specified in the parentheses.

## Hints

- The value operator `VALUE` can also be used to construct the content of existing complex data objects (structures and internal tables) and thus goes beyond the functionality of the [`VALUE`](../abap-declarations/abapdata_options.md) addition.

- The value operator `VALUE` uses mainly the same syntax as in the instance operator [`NEW`](abenconstructor_expression_new.md) to create values.

- Elementary data types as well as reference types cannot be explicitly specified for the construction of values with the `VALUE` operator except for the creation of an initial value. In contrast to the instance operator [`NEW`](abenconstructor_expression_new.md), the corresponding result can also be achieved by direct assignments. For this reason, the specification of a single operand, which is possible with `NEW`, is also not necessary and therefore not permitted. This does not affect the use of `VALUE` to control [table expressions](../../abap-glossary/abentable_expression_glosry.md) for which any suitable data types can be specified.

- Since arithmetic calculations with the results of `VALUE` for constructing values are not possible, except when creating an initial value, constructor expressions of this type cannot be specified directly in the operand positions of [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md). This does not affect constructor expressions with `VALUE` used to control [table expressions](../../abap-glossary/abentable_expression_glosry.md), which can be used for calculations for suitable results.

- The conversion operator [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) closes the gap where no elementary data objects can be constructed in operand positions using `VALUE`.

- If a constructor expression with `VALUE` is not used as the source of an assignment to a data object, the value operator `VALUE` creates a new temporary data object whose data type is determined by the specified type and whose content is determined by the parameters passed. This data object is used as the operand of a statement and then deleted after use. It is deleted either when the current statement is closed or when a relational expression is evaluated after the truth value is determined.

- In assignments to a data object, the target variable is used directly and no temporary data object is created. This variable is initialized or overwritten completely before the assignment of the values specified in the parentheses. Its original value, however, is still available in an optional [`LET` expression](../abap-declarations/abaplet.md). This is the difference between `VALUE` and the instance operator [`NEW`](abenconstructor_expression_new.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of the values of a structure of type `T100` [declared inline](../abap-declarations/abeninline_declarations.md).

``` abap
FINAL(wa) = VALUE t100( sprsl = 'E' 
                       arbgb = 'DEMO' 
                       msgnr = '111' 
                       text =  '...' ).
```
