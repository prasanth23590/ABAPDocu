---
title: "ABAP Objects - Data Types and Constants of Classes"
source_file: abenclass_types_constants.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Classes > ABAP Objects - Components of Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Data Types and Constants of Classes

- [Data Types](abenclass_types_constants.md#data-types)

  - [Standalone Types](abenclass_types_constants.md#standalone-types)

  - [Bound Data Types](abenclass_types_constants.md#bound-data-types)

- [Constants](abenclass_types_constants.md#constants)

## Data Types

### Standalone Types

The [`TYPES`](../abap-declarations/abaptypes.md) statement can be used to declare any number of user-defined ABAP data types within a class. Types are instance-independent and only exist once for all the objects of a class.

### Bound Data Types

[Bound data types](../../abap-glossary/abenbound_data_type_glosry.md) that occur as properties of instance or static attributes also belong to the static properties of a class. After a `LIKE` addition, the class name can be used to access the properties of instance attributes (exceptions to this rule are the statements `ASSIGN ... CASTING` and `SELECT-OPTIONS ... FOR`). In addition, a reference variable can be used with an object component selector without first creating the object.

## Constants

Constants are special [static attributes](../../abap-glossary/abenstatic_attribute_glosry.md), whose values are specified when they are declared, and which cannot be changed. Constants are declared using the statement [`CONSTANTS`](../abap-declarations/abapconstants.md). Constants are instance-independent and exist only once for all the objects of a class.
