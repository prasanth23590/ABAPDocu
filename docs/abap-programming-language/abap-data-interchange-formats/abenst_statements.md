---
title: "ST - Overview of Statements"
source_file: abenst_statements.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Overview of Statements

ST programs are XML data consisting of literal elements and ST statements. ST statements can be distinguished from literal elements (XML elements, attributes, and text) by their namespace `"http://www.sap.com/transformation-templates"`, for which the prefix `tt` is used by convention.

During serialization and deserialization, literal elements are copied unchanged into a target document or consumed from a source document and compared. ST statements are executed according to their semantics.

Data is addressed using [tree structures](abenst_trees.md) whose root nodes (data roots) are bound to ABAP data objects. The root nodes can always be addressed directly using their names. In addition, a current node can be defined, which can be addressed using `$ref`.

| **ST statement**                | **Meaning**                                                                                                                                        |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `<tt:apply ...>`                | [Calls](abenst_tt_apply.md) a subtemplate                                                                                                        |
| `<tt:assign ...>`               | [Assigns](abenst_tt_assign.md) a value to data                                                                                                   |
| `<tt:attribute ...>`            | [Non-literal attribute](abenst_tt_attribute.md)                                                                                                  |
| `<tt:call ...>`                 | [Calls](abenst_tt_call.md) an ST program                                                                                                         |
| `<tt:call-method ...>`          | Calls a [static method](abenst_tt_call-method_static.md) or an [instance method](abenst_tt_call-method_instance.md) in ABAP Objects            |
| `<tt:cast ...>`                 | [Downcasts](abenst_tt_cast.md) reference variables                                                                                               |
| `<tt:clear ...>`                | [Initializes](abenst_tt_clear.md) data                                                                                                           |
| `<tt:cond ...>`                 | [Conditional transformation](abenst_tt_cond.md)                                                                                                  |
| `<tt:cond-var ...>`             | [Condition for variables](abenst_tt_cond-var.md)                                                                                                 |
| `<tt:context ...>`              | [Context for local data roots](abenst_tt_template_sub.md) in subtemplates                                                                        |
| `<tt:copy ...>`                 | [Transformation](abenst_tt_copy.md) to and from asXML                                                                                            |
| `<tt:create-object ...>`        | [Creates objects](abenst_tt_create.md) in ABAP Objects                                                                                           |
| `<tt:d-cond ...>`               | [Conditional transformation](abenst_tt_cond.md) for deserializations                                                                             |
| `<tt:deserialize ...>`          | Defines the [transformation direction](abenst_tt_serialize_deserialize.md)                                                                       |
| `<tt:empty ...>`                | [Empty pattern](abenst_tt_empty.md)                                                                                                              |
| `<... tt:extensible="..."...>`  | [Extensibility](abenst_tt_extensible.md) of literal XML elements                                                                                 |
| `<tt:front ...>`                | [Initial part](abenst_tt_type.md) of a structured type                                                                                           |
| `<tt:group ...>`                | [Groups](abenst_tt_group.md) conditional transformations                                                                                         |
| `<tt:include ...>`              | [Includes](abenst_tt_include.md) an ST program                                                                                                   |
| `<... tt:lax="..." ...>`        | [Name comparison](abenst_tt_lax.md) of literal XML elements                                                                                      |
| `<tt:loop ...>`                 | [Loops](abenst_tt_loop.md) across internal tables                                                                                                |
| `<tt:namespace ...>`            | Defines a [namespace](abenst_tt_namespace.md)                                                                                                    |
| `<tt:node ...>`                 | [Component](abenst_tt_type.md) of a type                                                                                                         |
| `<tt:parameter ...>`            | Declares [parameters](abenst_tt_parameter.md)                                                                                                    |
| `<tt:read ...>`                 | [Reads](abenst_tt_read.md) a variable from XML                                                                                                   |
| `<tt:read-write ...>`           | [Short form](abenst_tt_read_write.md) of `<tt:read ...>` and `<tt:write ...>`                                                                    |
| `<tt:ref ...>`                  | Sets the [current node](abenst_tt_ref.md)                                                                                                        |
| `<... tt:ref="..."...>`         | Sets the [current node](abenst_tt_ref.md) for a literal XML element                                                                              |
| `<tt:root ...>`                 | Declares a [data root](abenst_tt_root.md)                                                                                                        |
| `<tt:serialize ...>`            | Defines the [transformation direction](abenst_tt_serialize_deserialize.md)                                                                       |
| `<tt:s-cond ...>`               | [Conditional transformation](abenst_tt_cond.md) for serializations                                                                               |
| `<tt:skip ...>`                 | [Skips XML](abenst_tt_skip.md) elements in deserializations                                                                                      |
| `<tt:switch ...>`               | [ST - tt:switch, Case Distinction](abenst_tt_switch.md) Defines a [case distinction](abenst_tt_switch.md) between conditional transformations. |
| `<tt:switch-var ...>`           | [Case distinctions](abenst_tt_switch-var.md) for variables                                                                                       |
| `<tt:template ...>`             | [Main template](abenst_tt_template_main.md) or [subtemplates](abenst_tt_template_sub.md)                                                       |
| `<tt:text ...>`                 | [Literal text](abenst_tt_text.md)                                                                                                                |
| `<tt:transform ...>`            | [Root element](abenst_tt_transform.md) of an ST program                                                                                          |
| `<tt:type ...>`                 | [Type definition](abenst_tt_type.md)                                                                                                             |
| `<tt:value ...>`                | Transforms [elementary data objects](abenst_tt_value_elementary.md) and [structures](abenst_tt_value_structure.md)                             |
| `<... tt:value-ref ="..." ...>` | [Short form](abenst_tt_value_elementary.md) of the transformation of elementary data objects                                                     |
| `<tt:variable ...>`             | Declares a [variable](abenst_tt_variable.md)                                                                                                     |
| `<tt:with-parameter ...>`       | Passes values to [ST programs](abenst_tt_call.md), [subtemplates](abenst_tt_apply.md), and [ABAP methods](abenst_tt_call-method_static.md)   |
| `<tt:with-root ...>`            | Passes data nodes to [ST programs](abenst_tt_call.md) and [subtemplates](abenst_tt_apply.md)                                                   |
| `<tt:write ...>`                | [Writes](abenst_tt_write.md) a variable to XML                                                                                                   |
