---
title: "JSON - Quick Overview"
source_file: abenjson_oview.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Quick Overview

[JSON (JavaScript Object Notation)](http://www.json.org/) is a data exchange format whose syntax generally represents a subset of the JavaScript syntax. JSON data is stored and transported as character strings in a character format.

The syntax of JSON consists of the following components:

- Syntax characters

  - **Curly brackets** `{ }` define objects.

  - **Square brackets** `[ ]` define arrays.

  - A **colon** `:` separates the name and the value of an object component.

  - A **comma** `,` separates the components inside arrays and objects.

- Representation of values

  - **Character-like values** are specified between double quotation marks `"..."`. The `\` character is used as the escape character for syntax characters.

  - **Number values** are represented in [mathematical notation](../../abap-glossary/abenmathematical_notation_glosry.md) or in [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md).

  - **Boolean values** are represented by the keywords `true` and `false`.

  - **Null values** are represented by the keyword `null`.

- Data structures

  - An **array** is an ordered list of values, arrays, or objects enclosed in square brackets `[ ]` and separated by commas `,`, which do not need to have the same type. An empty array, `[ ]`, is also possible.

  - An **object** is an ordered list of components enclosed in curly brackets `{ }` and separated by commas `,`. A component consists of a name specified in double quotation marks followed by a colon `:` followed by a value, array, or object.. An empty object, `{ }`, is also possible. Unique names for the components of an object are recommended, but not mandatory.

Empty space (blanks, line breaks) can be used anywhere before and after the syntax characters. At the top level, valid JSON data contains a single value, an array, or an object. Arrays and objects can contain further values, arrays, or objects.

## Hints

- In JavaScript, JSON data can be transformed to JavaScript objects directly using a built-in function `eval` due to its compatibility. In other programming languages, JSON data is read using parsers, which is also recommended for JavaScript for reasons of performance and security.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `CL_DEMO_JSON_EXAMPLES` shows examples of valid JSON data.
