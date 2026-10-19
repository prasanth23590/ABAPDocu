---
title: "Sharing Between Dynamic Data Objects"
source_file: abenmemory_consumption_3.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Memory Management of Deep Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Sharing Between Dynamic Data Objects

When reference variables are assigned, only the references are copied. After an assignment, source and target variables point to the same data object or instance of a class (more precisely, to their headers).

Sharing also takes place internally in [assignments](../../abap-glossary/abenassignment_glosry.md) between similar [strings](../../abap-glossary/abenstring_glosry.md) and between similar [internal tables](../../abap-glossary/abeninternal_table_glosry.md) whose line types do not themselves contain table types. This means that the actual data values are not copied at first. Only the necessary administration entries are copied, so that the target object refers to the same data as the source object.

For strings, a new internal reference is created that points to the existing string header. For internal tables, a new internal reference and a new table header, which refers to the existing [table body](../../abap-glossary/abentable_body_glosry.md), are created.

Sharing between dynamic data objects is, of course, only active for as long as multiple dynamic data objects are involved, or more than one internal reference refers to the data values. As soon as only one internal reference refers to the data, sharing no longer takes place. Such cases occur, for example, if involved dynamic data objects only exist during the lifetime of a procedure, or if they are recorded as anonymous data objects by the Garbage Collector.

Active sharing between existing dynamic data objects is canceled when either the source object or target object is accessed in change mode (copy-on-write semantics). The actual copy process for the data values then takes place and the references and headers are changed accordingly.

The following figure illustrates the sharing of dynamic data objects. The upper section shows how strings are shared on the left and how internal tables are shared on the right side. The lower section shows how sharing is canceled when the source or target object is changed.

  
![figure](images_abdoc_sharing.gif)  

## Hints

- Table sharing usually only occurs for tables whose line types do not themselves contain table types. Otherwise, the prerequisite for "similar tables" is kept deliberately vague. Tables are similar if they at least have the exact same table type, that is the same line type, table category, and keys. There are other table combinations that are also considered to be similar and in which sharing can take place. However, this is an internal optimization measure that may be changed between releases. Therefore, programming should never be based on when table sharing occurs and when it is canceled again.

- Sharing also occurs during [pass by value](../../abap-glossary/abenpass_by_value_glosry.md) to procedures.

- Sharing is not canceled by changes to the objects for reference variables that point to the same data object or the same instance of a class.

- Another type of sharing is the [initial value sharing](../../abap-glossary/abeninitial_value_sharing_glosry.md) of [boxed components](../../abap-glossary/abenboxed_component_glosry.md) for which the initial value is stored only once per AS instance.
