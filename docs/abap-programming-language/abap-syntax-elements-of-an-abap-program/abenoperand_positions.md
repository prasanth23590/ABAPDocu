---
title: "Operand Positions"
source_file: abenoperand_positions.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Operand Positions

Most ABAP statements have operand positions, where [operands](../abap-operands/abenoperands.md) can be specified as tokens. The following operand positions can be distinguished:

- Operand positions where the values of operands are processed:

  - [read position](../../abap-glossary/abenread_position_glosry.md)

    At a read position, the content of an operand is read but not changed when the statement is executed.

  - [write position](../../abap-glossary/abenwrite_position_glosry.md)

    At a write position, the content of an operand is changed when the statement is executed.

- Besides the above operand positions, there are also positions in ABAP statements, where not the value of the operand is processed. Examples are:

  - Type specifications in declarations or typings.

  - The names of procedures or programs called by a statement.

  - The names of resources such as CDS entities or database tables accessed in ABAP SQL.

The following topics provide a detailed description of read and write positions:

- [Operand Type](abenoperand_type.md)

- [Expression Positions for Expressions](abenexpression_positions.md)

  - [Write Positions Expressions](abenexpression_positions_write.md)

  - [Read Positions for Expressions](abenexpression_positions_read.md)
