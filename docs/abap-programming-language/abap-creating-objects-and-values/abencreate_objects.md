---
title: "ABAP - Creating Objects and Values"
source_file: abencreate_objects.html
section: "ABAP Programming Language"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP - Creating Objects and Values

This section describes how data objects and instances of classes are created and values constructed.

- [Creating Objects](abencreate_objects.md#creating-objects)

- [Constructing Values](abencreate_objects.md#constructing-values)

## Creating Objects

Creating an object or data object is equivalent to the dynamic creation of an instance of a data type or a class. While instances of classes can only be created as described in this section, instances of data types, that is data objects, declared using the statement [`DATA`](../abap-declarations/abapdata.md), or related statements such as [`CONSTANTS`](../abap-declarations/abapconstants.md), are created automatically as named data objects when their [context](../../abap-glossary/abenobj_context_glosry.md) is loaded into the internal session. Data objects only need to be created dynamically if the data type is only known when the program is executed, or if large amounts of memory are only to be used for short periods of time.

Dynamically created objects can only be addressed using reference variables and are deleted from the internal session by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md) if they are no longer referenced.

Objects can be created using one of the following:

- [`CREATE DATA`](abapcreate_data.md)

- [`CREATE OBJECT`](abapcreate_object.md)

- The [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abenconstructor_expression_new.md) for creating objects in [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md) and [functional operand positions](../../abap-glossary/abenfunctional_position_glosry.md)

- The addition [`NEW`](../abap-database-access/abapselect_into_target.md) in the `INTO` clause of ABAP SQL for the implicit creation of data objects as target areas.

Data objects and objects are created in the [internal session](../../abap-glossary/abeninternal_session_glosry.md) of the current program by default, and only programs in the same internal session can access them.

## Constructing Values

The attribute values of a newly created instance of a class can be constructed using the [instance constructor](../../abap-glossary/abeninstance_constructor_glosry.md) of the class. The input parameters of the instance constructor can be filled using the `EXPORTING` addition of the statement [`CREATE OBJECT`](abapcreate_object.md) or using actual parameters for the instance operator [`NEW`](abenconstructor_expression_new.md).

The values of dynamically created or statically declared data objects can be constructed using the following [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md):

- When anonymous data objects are created dynamically using the instance operator [`NEW`](abenconstructor_expression_new.md), values for all data types, particularly structured and tabular types, can be constructed and assigned to the created data object.

- The [value operator](../../abap-glossary/abenvalue_operator_glosry.md) [`VALUE`](abenconstructor_expression_value.md) can also be used to construct the content of complex data objects (structures, internal tables) and thus exceeds the functionality of the [`VALUE`](../abap-declarations/abapdata_options.md) addition.

### Hint

Like any constructor expression, the value operator [`VALUE`](abenconstructor_expression_value.md) can be used in [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md) and in [functional operand positions](../../abap-glossary/abenfunctional_position_glosry.md), including particularly the right side of an assignment to an [inline declaration](../abap-declarations/abeninline_declarations.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Inline declarations of a reference variable `dref` and a structured variable `dobj`. The instance operator `NEW` creates an anonymous data object that is referred to by `dref`. Using functional method calls, the instance operator `NEW` and the value operator `VALUE` are used to construct and assign values for the components of the structures.

``` abap
DATA(dref) = NEW struct( col1 = meth->get_col1( ) 
                         col2 = meth->get_col1( ) ). 
 
DATA(dobj) = VALUE struct( col1 = meth->get_col1( ) 
                           col2 = meth->get_col1( ) ).
```
