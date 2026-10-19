---
title: "ABP Auxiliary Class"
source_file: abaprap_auxiliary_class.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > CLASS, FOR BEHAVIOR OF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABP Auxiliary Class

An optional [ABP auxiliary class](../../abap-glossary/abenabp_aux_class_glosry.md) that supports the implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) (ABP). As a prerequisite, the class name must be specified after the [`auxiliary class`](../rap-behavior-definitions/abenbdl_auxiliary_class.md) in a [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). For the auxiliary class, the addition `... FOR BEHAVIOR OF bdef ...` must be specified in the declaration part, where `bdef` is the name of the BDEF.

The following aspects are relevant for an auxiliary class:

- The main purposes of an auxiliary class are as follows:

  - Provide reusable methods for an ABP

  - Allow developers to work concurrently on behavior implementation

  - Provide utility methods for raising RAP business events

- [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md), [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md), or [RAP event handler methods](../../abap-glossary/abenrap_event_handler_meth_glosry.md) as such can only be declared and implemented in an ABP. However, these methods can delegate functionality to methods in auxiliary classes.

- Unlike an ABP, an auxiliary class does not need to be [abstract](../../abap-glossary/abenabstract_glosry.md). However, similarly to the ABP, an auxiliary class is always implicitly [final](../../abap-glossary/abenfinal_glosry.md), even if the `FINAL` addition is not explicitly specified.

- Unlike an ABP, an auxiliary class can have both [static methods](../../abap-glossary/abenstatic_method_glosry.md) and [instance methods](../../abap-glossary/abeninstance_method_glosry.md) as [class components](../../abap-glossary/abenclass_component_glosry.md).

- It can access the associated RAP BO using the ABAP EML statement [`IN LOCAL MODE`](abapin_local_mode.md) and [`PRIVILEGED`](abapeml_privileged.md).

- It can use the [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) from the associated RAP BO.

- It can access [internal RAP BO operations](../../abap-glossary/abenrap_internal_operation_glosry.md).

- The [RAP authorization context](../../abap-glossary/abencds_auth_con_glosry.md) of the associated RAP BO can be activated or deactivated using `AUTHORITY-CHECK DISABLE BEGIN CONTEXT ...` and `AUTHORITY-CHECK DISABLE END`.

- Raising a RAP business event from the associated RAP BO using the statement [`RAISE ENTITY EVENT`](abapraise_entity_event.md) is possible.

- It is not recommended that you completely outsource the implementation of methods to an auxiliary class. This approach comes with significant overhead, such as the additional [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) declarations for method parameters in auxiliary classes.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code snippet shows parts of a declaration and the implementation part of an auxiliary class.

``` abap
CLASS cl DEFINITION PUBLIC ... 
   FOR BEHAVIOR OF bdef_name ... . 
   ... 
ENDCLASS. 
 
CLASS cl IMPLEMENTATION. 
   ... 
ENDCLASS.
```

## More Information

- [RAP - `auxiliary class`](../rap-behavior-definitions/abenbdl_auxiliary_class.md)

- Find more syntax options for the declaration part [here](../../abap-programming-language/abap-declarations/abapclass_definition.md).

## Executable Example

[ABP Auxiliary Class](abenabp_aux_cl_abexa.md)
