---
title: "Data Objects"
source_file: abenobjects_statements.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Data Objects

A data object is an instance of a data type and occupies as much memory space as is allowed by its type. An ABAP program only works with data that is available as content of data objects. Data objects are either created implicitly in their declaration as [named data objects](../../abap-glossary/abennamed_data_object_glosry.md) or explicitly as [anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md) using [`CREATE DATA`](../abap-creating-objects-and-values/abapcreate_data.md) or the [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md).

- The following are data objects that are not declared using keywords:

  - [Literals](abenliteral.md) are data objects that are declared in operand positions using literal source code.

  - [Text symbols](abentext_symbols.md) are character-like constant data objects that are declared outside the program.

- Declaration of variables and constants in every context:

  - [`DATA`](abapdata.md)

  - [`CONSTANTS`](abapconstants.md)

- Declaration of static attributes in classes:

  - [`CLASS-DATA`](abapclass-data.md)

- Declaration of static variables in procedures:

  - [`STATICS`](abapstatics.md)

Data objects can be declared by reference to a non-generic data type of the same ABAP program or from ABAP Dictionary. In this case, the data type determines the technical properties of the data object completely. A data object can also be constructed in the ABAP program without completely specified type definitions. The data type of a data object of this type is always complete, and does not exist independently, but rather as a property of the data object and is called a [bound data type](../../abap-glossary/abenbound_data_type_glosry.md).

For more information about data objects, see [Data Objects](../abap-data-types-and-data-objects/abendata_objects.md).
