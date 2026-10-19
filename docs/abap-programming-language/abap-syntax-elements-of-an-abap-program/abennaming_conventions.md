---
title: "Naming Conventions and Namespaces"
source_file: abennaming_conventions.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Naming Conventions and Namespaces

- [Naming Conventions](abennaming_conventions.md#naming-conventions)

- [Namespaces](abennaming_conventions.md#namespaces)

- [Reserved Names](abennaming_conventions.md#reserved-names)

## Naming Conventions

The following conventions apply to the names of all definable objects within ABAP programs, such as data types, data objects, classes, macros, and [procedures](../../abap-glossary/abenprocedure_glosry.md):

- A name can be up to 30 characters long.

- Permitted are letters from *A* to *Z*, digits from *0* to *9*, and underscores (`_`).

- The name must start with a letter or an underscore (`_`). Only outside of ABAP objects can the name also start with a different character.

- The name can have a [namespace prefix](../../abap-glossary/abenname_space_prefix_glosry.md). A namespace prefix consists of at least three characters that are enclosed by two forward slashes (`/.../`). The entire length of prefix and name must not exceed 30 characters.

- The names of predefined ABAP types or predefined data objects must not be used for data types or data objects.

- The use of names that are reserved for [ABAP words](../../abap-glossary/abenabap_word_glosry.md) and so on for custom definitions is not actually forbidden, but is strongly advised against.

- Field symbols are special in that their names have to be enclosed in angle brackets (`<...>`). The angle brackets are part of the name, which means that a field symbol could be called `<>`, but this is not recommended.

Since ABAP is not case-sensitive, the names of program-internal objects are not case-sensitive either.

### Hints

- All types possible in ABAP are in a namespace. In particular, data types and object types do not have separate namespaces. A global class, for example, cannot be created with a name that is already assigned to a data type in the ABAP Dictionary.

- The naming conventions presented here must be followed. The syntax check does not check them completely, but this should not be exploited unnecessarily.

## Namespaces

Outside of class declarations, different objects have separate namespaces, so that it is possible that data types, data objects or procedures can have the same name. Classes and interfaces thereby lie within the same namespace as data types. The namespace is valid for the respective context. Within a context, the names of the same objects must be unique.

Within a class declaration, the name of every class component - data type, attribute, method, event, or alias name - must be unique.

## Reserved Names

The following names are reserved and must not be used in personal declarations:

- User-defined data types must not have the name of a [built-in ABAP type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md). This applies to type definitions in the ABAP language and in the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md).

- The name of a structure component must not have the name of the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line`. This applies to type definitions in ABAP and in the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) as well as to data declarations and when creating data objects in ABAP.

- A [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) of an internal table must not have the predefined names `primary_key` or `loop_key`.

- The name of the [built-in data object](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_objects.md) [`space`](../abap-built-in-types-data-objects-functions-and-constructors/abenspace.md) must not be used in any positions for other declarations or data objects, except in the case of the obsolete anonymous components.

- The name of the [built-in data object](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_objects.md) [`me`](../abap-built-in-types-data-objects-functions-and-constructors/abenme.md) must not be used in classes for attributes, formal parameters, and local data objects.

### Hint

The names of the following built-in data objects are not reserved and are hidden by any identically named declarations. It is strongly advised to not create any data objects with the names of these built-in data objects:

- The structures of the [ABAP system fields](../abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md) `sy` and `syst` and the system fields themselves.
