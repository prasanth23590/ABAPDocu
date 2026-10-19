---
title: "Constructor Operators for Constructor Expressions"
source_file: abenconstructor_expressions.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Constructor Operators for Constructor Expressions

## Syntax

``` abap
... NEW|VALUE|CONV|CORRESPONDING|CAST|REF|EXACT|REDUCE|FILTER|COND|SWITCH 
     type( ... ) ...  
```

[`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) · [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) · [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) · [`CORRESPONDING`](../abap-processing-internal-data/abenconstructor_expr_corresponding.md) · [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md) · [`REF`](../abap-processing-internal-data/abenconstructor_expression_ref.md) · [`EXACT`](../abap-processing-internal-data/abenconstructor_expression_exact.md) · [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md) · [`FILTER`](../abap-processing-internal-data/abenconstructor_expression_filter.md) · [`COND`](../abap-program-flow-logic/abenconditional_expression_cond.md) · [`SWITCH`](../abap-program-flow-logic/abenconditional_expression_switch.md)

## Description

A constructor expression consists of the following:

- A built-in [constructor operator](../../abap-glossary/abenconstructor_operator_glosry.md)

- A data type or object type `type` that matches the operator and that can be derived implicitly from the operand position using the specification `#`

- Type-specific parameters specified in parentheses

Each constructor expression creates a result whose data type is determined by the specified type. The parameters specified in parentheses are used to pass input values. The following constructor operators exist:

- The instance operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) is used to create objects in operand positions. The result is a reference variable of the static type `type` that points to the created object. The input values determine the content of the created object.

- The value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) is used to fill complex data objects with values in operand positions, create initial values of any data type, or control the result of [table expressions](../../abap-glossary/abentable_expression_glosry.md). The result is a data object of the specified type `type`. The input values determine the content of the result.

- The conversion operator [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) is used for conversions between data types in operand positions. The result is a data object of the specified type `type` produced by the conversion from an input value.

- The casting operator [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md) is used for downcasts of reference variables in operand positions. The result is a reference variable of the static type `type` produced by the assignment from an input value.

- The reference operator [`REF`](../abap-processing-internal-data/abenconstructor_expression_ref.md) is used to construct a data reference to a data object in operand positions or to control the results of [table expressions](../../abap-glossary/abentable_expression_glosry.md). The result is a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md).

- The component operator [`CORRESPONDING`](../abap-processing-internal-data/abenconstructor_expr_corresponding.md) is used to construct a structure or an internal table in an operand position. The result is a structure or internal table whose components are filled with values from identically named components or components of a parameter specified using a mapping rule.

- The lossless operator [`EXACT`](../abap-processing-internal-data/abenconstructor_expression_exact.md) is used to create a value in an operand position without losing data. The result is a data object of the specified type that originates from a [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md) or a [lossless calculation](../../abap-glossary/abenlossless_calculation_glosry.md).

- The reduction operator [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md) constructs a value from conditional iterations or from table iterations.

- The filter operator [`FILTER`](../abap-processing-internal-data/abenconstructor_expression_filter.md) constructs an internal table by filtering the lines of an internal table.

- The conditional operators [`COND`](../abap-program-flow-logic/abenconditional_expression_cond.md) and [`SWITCH`](../abap-program-flow-logic/abenconditional_expression_cond.md) are used to create values or raise class-based exceptions in operand positions in accordance with conditions. The result depends on any logical expressions or on a case distinction.

A constructor expression can be specified in [general expression positions](../abap-syntax-elements-of-an-abap-program/abengeneral_expression_positions.md) and [functional positions](../abap-syntax-elements-of-an-abap-program/abenfunctional_positions.md) with an appropriate [operand type](../../abap-glossary/abenoperand_type_glosry.md). The result is used as an operand here. In a [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md) or [relational expression](../../abap-glossary/abenrelational_expression_glosry.md), the specified type `type` is used in the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) or [comparison type](../../abap-glossary/abencomparison_type_glosry.md). An expression with the operator `VALUE` that is not used to create an initial value cannot be specified directly in an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) because it never matches the operand type here. Expressions with the operators `NEW` and `CAST` can be positioned directly in front of the [object component selector](../../abap-glossary/abenobject_component_select_glosry.md) `->` and can occur in [chainings](../../abap-glossary/abenchaining_glosry.md).

Data types and classes that are visible and usable in the current operand position can be specified for `type`. This includes the [built-in ABAP types](../../abap-glossary/abenbuiltin_abap_type_glosry.md), types defined using [`TYPES`](../abap-declarations/abaptypes.md), types from the [ABAP Dictionary](../../abap-dictionary-ddic/abenabap_dictionary.md), and both local and global classes. If the data type required in an operand position is unique and can be identified completely, the `#` character can be used instead of an explicit type specification `type` and the [operand type](../../abap-glossary/abenoperand_type_glosry.md) is used. If the operand type is not unique and is not known completely, if possible, a type inference is performed to determine a data type. This is described in each constructor expression.

[`LET`](../abap-declarations/abaplet.md) expressions can be used to define local helper fields in all suitable constructor expressions.

## Hints

- Constructor operators can be classified as follows:

  - Constructor operators like `NEW` and `VALUE` construct new values, for which components are passed except when the initial value is created, whereas constructor operators like `CONV`, `CAST`, `REF`, and `EXACT` convert a single passed value.

  - Constructor operators like `NEW`, `CAST`, and `REF` always return reference variables, whereas constructor operators like `VALUE`, `CONV`, and `EXACT` return all types of data objects.

- Unlike [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md) or [table expressions](../../abap-glossary/abentable_expression_glosry.md), constructor expressions cannot be placed on the left side of a [structure component selector](../../abap-glossary/abenstructure_component_sel_glosry.md), since constructing a structure only to access a single component is pointless.

- If a data type from ABAP Dictionary is used for the type, the result of a constructor is given its semantic properties.

- A [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md) does not determine the type of its operands. If constructor expressions are used as operands of calculation expressions, the `#` character can only be specified for `type` if the type can be determined from the constructor expression itself.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Filling of an internal table `itab` with the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md). The data type is inferred from the left side of the assignment.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
 
itab = VALUE #( ( 1 ) ( 2 ) ( 3 ) ).
```
