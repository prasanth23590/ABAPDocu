---
title: "ABAP SQL - literal"
source_file: abenabap_sql_literals.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Operands sql_elem"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - literal

[ABAP SQL literals](../../abap-glossary/abenabap_sql_literal_glosry.md) can be used in read positions of ABAP SQL statements where [host variables](abenabap_sql_host_variables.md) are possible. Unlike host variables, they are not prefixed with the escape character `@`. The [literal operator](../../abap-glossary/abenliteral_operator_glosry.md) can be used to combine two literals of the same type into a single literal.

In ABAP SQL, there are two different kinds of literals:

- [Typed literals](abenabap_sql_typed_literals.md) (cover most built-in types of the ABAP Dictionary)

  Typed literals are always handled like elementary SQL expressions

- [Untyped literals](abenabap_sql_untyped_literals.md) (character literals and numeric literals)

  Untyped literals are either handled like elementary SQL expressions or like host variables.
