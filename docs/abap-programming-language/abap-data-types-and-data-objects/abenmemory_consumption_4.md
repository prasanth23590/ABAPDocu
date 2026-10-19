---
title: "Complex Data Objects with Deep Components"
source_file: abenmemory_consumption_4.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Memory Management of Deep Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Complex Data Objects with Deep Components

If data objects of [complex data types](../../abap-glossary/abencomplex_data_type_glosry.md) have many deep components, which often, for example, applies to internal tables with a deep line type for example, the administrative costs in the form of memory for references and headers must be prevented from growing disproportionately large compared to the actual data content.

For complex data objects with relatively little data content, three basic cases can be distinguished:

1.  **Complex data objects with a sparse fill level**

    A complex deep data object is sparsely populated if it contains many deep components of which most are initial. The memory requirement of such a deep initial component like this is 8 bytes for as long as the component does not yet refer to a header.

2.  **Complex data objects with a duplicative fill level**

    A complex deep data object has a duplicative fill level if it contains many deep components of which most refer to the same data. Such components share the dynamic memory and only contribute to the memory requirement of their references. For [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md), this is achieved by [sharing](abenmemory_consumption_3.md).

3.  **Complex data objects with a low fill level**

    A complex deep data object has a low fill level if it contains many deep components that refer to different objects, strings, or internal tables, but the objects only require very little memory or are empty.

Deep data objects with a fill level that is sparse, duplicative, and not too low can usually be used without any concerns.

For deep data objects with a sparse fill level and few duplicates, it is vital to consider the memory requirements for references and headers. Unlike other programming languages, ABAP is not suitable for the massive use of such data objects. If the dataset is low, a class wrapper can also be used as an alternative to internal tables, since the additional costs for objects are comparatively low.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An example of a duplicative data object with a low fill level is an internal table whose line type itself is table-like or contains table-like components. Even if the inner internal tables are initialized after previous use, they still occupy memory for reference and header, which can cause considerable memory requirements for little or no work data in the case of a large outer internal table.

## Executable Example

See Deep Data Objects, Memory Usage.
