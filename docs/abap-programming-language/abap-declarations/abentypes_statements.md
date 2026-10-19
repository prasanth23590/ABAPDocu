---
title: "Data Types"
source_file: abentypes_statements.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Data Types

Data types are templates for creating data objects. Data types can be defined independently in an ABAP program or in the ABAP Dictionary. Data types can also be non-independent as properties of data objects. Data types do not use any memory space for work data but may require memory for administrative information.

In ABAP programs, data types local to the program can be defined, which can be used for [typing](../../abap-glossary/abentyping_glosry.md) or declaring further data types or data objects, depending on their validity and visibility.

Data types defined in the [public](../../abap-glossary/abenpublic_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of a [global class](../../abap-glossary/abenglobal_class_glosry.md) or [global interface](../../abap-glossary/abenglobal_interface_glosry.md) are visible to other programs.

The associated statements are:

- [`TYPES`](abaptypes.md)

- [`INCLUDE TYPE`](abapinclude_type.md)
