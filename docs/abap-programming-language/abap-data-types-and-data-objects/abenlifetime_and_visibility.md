---
title: "Validity and Visibility"
source_file: abenlifetime_and_visibility.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Validity and Visibility

The context of a declarative statement in the source code of a program determines the validity and visibility of the declared component. In ABAP programs, there are three contexts in which data types and data objects can be declared:

- **Locally in Procedures**

  Local data in [procedures](../../abap-glossary/abenprocedure_glosry.md) is valid while a procedure is being executed. It is created when the procedure is called and deleted when the procedure is exited. In addition to their local data and formal parameters, procedures see the global data of the [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md). Methods also 'see' the components of their class.

- **As Components of Classes**

  [Static attributes](../../abap-glossary/abenstatic_attribute_glosry.md) of classes exist for as long as the [internal session](../../abap-glossary/abeninternal_session_glosry.md) of the ABAP program exists. Instance attributes of classes are bound to the lifetime of objects. They are created when an object is instantiated and deleted along with the object by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md). Classes also see the global data of the compilation unit.

- **Globally in the Compilation Unit**

  Global program data exists for as long as the internal session of the ABAP program exists. It is created when the program is loaded in the internal session, and deleted from the internal session when the program is removed. An ABAP program usually only sees its own global data

All contexts see the program-independent type definitions of ABAP CDS, of the ABAP Dictionary and the type definitions and data declarations in the public visibility sections of global classes. Local declarations, however, hide global declarations with the same name. The following methods can be used to unhide these declarations:

- In methods, components of classes can be addressed using an [object component selector](../../abap-glossary/abenobject_component_select_glosry.md).

- In statements in which a dynamic specification of a data type, a class, or an interface is possible, a global type can be addressed by specifying an [absolute type name](../../abap-glossary/abenabsolute_typename_glosry.md).

In addition to context-dependent visibility, the position of the declaration in the source text also plays a role. In a statement of an ABAP program only previous declarations are visible, regardless of the context. To ensure that the order in the program matches the context-dependent visibility, all global declarations of a program should be listed at the start of the source code, before the first [processing block](../../abap-glossary/abenprocessing_block_glosry.md), and all local declarations should be listed immediately after the introduction of a procedure. The definition of an interface and the declaration part of a class are global declarations in this view. Note that reference variables that refer to a class can only be declared after the class has been declared. The implementation part, on the other hand, is one of the processing blocks.

## Hints

- The [ABAP system fields](../abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md) are located outside of the contexts listed above. They are hidden by global program data objects with the same names.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of an instance attribute `attr` of a class, and a local field `field` of a method. Reference is made to the outer declarations in the inner declaration.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    DATA attr TYPE demo_ddic_types-string VALUE `instance attribute`. 
    METHODS meth. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    DATA field LIKE attr VALUE `local field`. 
  ENDMETHOD. 
ENDCLASS.
```
