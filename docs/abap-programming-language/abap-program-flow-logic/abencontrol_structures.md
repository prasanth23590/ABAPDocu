---
title: "Control Structures"
source_file: abencontrol_structures.html
section: "ABAP Programming Language > ABAP - Program Flow Logic"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Control Structures

The statements in a [processing block](../../abap-glossary/abenprocessing_block_glosry.md) are organized in control structures. These define statement blocks and control the progress of the program within a processing block. They determine the conditions for processing statement blocks and how often they are run. Control structures can be nested. Statement blocks in control structures can themselves contain control structures.

The following control structures exist:

- **Sequence**

  A sequence consists of a statement block that is not defined explicitly by control statements. The statements it contains are processed exactly once without conditions. The execution of a sequence can be suspended for a certain time using a [`WAIT`](abapwait_up_to.md) statement.

- **Branch (selection)**

  A branch consists of one or more statement blocks that are defined by control statements such as [`IF`](abapif.md) or [`CASE`](abapcase.md), and that are executed depending on conditions.

- **Loop (iteration)**

  A loop consists of a statement block that is defined by control statements such as [`DO`](abapdo.md) or [`WHILE`](abapwhile.md), and that can be executed multiple times.

There are also special control structures for [exception handling](abenabap_exceptions.md).
