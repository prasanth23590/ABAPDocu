---
title: "Operators"
source_file: abenoperators.html
section: "ABAP Programming Language > ABAP - Operands > Expressions in Operand Positions > Operators and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Operators

ABAP contains the following operators:

- Operators that perform special operations in operand positions:

  - [**Declaration Operators**](../abap-declarations/abeninline_declarations.md)

    The declaration operators `DATA` and `FIELD-SYMBOL` declare variables or field symbols in operand positions.

  - [**Constructor Operators**](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md)

    The constructor operators `NEW`, `VALUE`, `CONV`, `CORRESPONDING`, `CAST`, `REF`, `EXACT`, `REDUCE`, `FILTER`, `COND`, and `SWITCH` construct values for data objects of specific data types in constructor expressions.

- Operators that combine multiple operands to a single expression:

  - [**Assignment Operators**](../abap-processing-internal-data/abenequals_operator.md)

    The assignment operator `=` combines the source field and target field of an assignment. The special [casting operator](../../abap-glossary/abencasting_operator_glosry.md) `?=` performs a [downcast](../../abap-glossary/abendown_cast_glosry.md) during the assignment. The [addition assignment operator](../../abap-glossary/abenadd_assignment_op_glosry.md) ([`+=`](../abap-processing-internal-data/abencalculation_assignments.md)), [subtraction assignment operator](../../abap-glossary/abensub_assignment_op_glosry.md) ([`-=`](../abap-processing-internal-data/abencalculation_assignments.md)), [multiplication assignment operator](../../abap-glossary/abenmult_assignment_op_glosry.md) ([`*=`](../abap-processing-internal-data/abencalculation_assignments.md)), [division assignment operator](../../abap-glossary/abendiv_assignment_op_glosry.md) ([`/=`](../abap-processing-internal-data/abencalculation_assignments.md)), or [concatenation assignment operator](../../abap-glossary/abenconcat_assignment_op_glosry.md) ([`**=`](../abap-processing-internal-data/abencalculation_assignment_string.md)) performs a [calculation assignment](../../abap-glossary/abencalculation_assignment_glosry.md). Furthermore, the operator `=` binds actual parameters to formal parameters, for example in procedure calls or when working with [data clusters](../../abap-glossary/abendata_cluster_glosry.md).

  - [**Arithmetic Operators**](../abap-processing-internal-data/abapcompute_arith.md)

    The arithmetic operators `+`, `-`, `*`, `/`, `DIV`, `MOD`, and `**` combine two or more numeric operands to an arithmetic expression. In addition, the characters `+` and `-` act as algebraic signs in arithmetic expressions.

  - [**Bit Operators**](../abap-processing-internal-data/abapcompute_bit.md)

    The bit operators `BIT-AND`, `BIT-OR`, and `BIT-XOR` combine two or more byte-like operands to a bit expression. The bit operator `BIT-NOT` negates a byte-like operand.

  - [**String Operators**](../abap-processing-internal-data/abapcompute_string.md)

    The string operator `&&` concatenates two character-like operands to a string expression.

  - [**Relational Operators**](../abap-program-flow-logic/abenlogexp.md)

    Relational operators occur in relational expressions, which in turn are components of logical expressions. The [comparison operators](../../abap-glossary/abencomp_operator_glosry.md) `=`, `<>`, `<`, `>`, `<=`,`>=`, `BETWEEN`, and so on combine two or more operands of any data type to a comparison expression. There are additional relational operators for specific data types. The [predicate operator](../../abap-glossary/abenpredicate_operator_glosry.md) `IS` makes a statement about an operand.

  - [**Boolean Operators**](../abap-program-flow-logic/abenlogexp_boole.md)

    The Boolean operators `AND`, `OR`, and `EQUIV` combine the results of individual logical expressions to one logical expression. The result of a logical expression is either true or false. The Boolean operator `NOT` negates the result of a logical expression.

- Operator that combine two operands during program compilation:

  - [**Literal Operator**](../abap-declarations/abenliteral_operator.md)

    The literal operator `&` combines two literals or two string templates to form one literal or string template.
