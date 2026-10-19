---
title: "DDIC - Data Types"
source_file: abenddic_data_types.html
section: "ABAP Dictionary (DDIC)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Data Types

Global data types can be defined as [DDIC types](../../abap-glossary/abenddic_type_glosry.md) in the ABAP Dictionary. These DDIC types are visible for and can be accessed from all repository objects of the current AS ABAP, as long as the package concept allows it.

The following data types are available in the ABAP Dictionary:

- [Data elements](abenddic_data_elements.md)

  Elementary data types or reference types with semantic properties, such as documentation or text labels. The type properties of a data element are defined either directly or using a domain. A [domain](abenddic_domains.md) determines the properties of a data element, such as the actual data type or the value range. A domain can be used by any number of data elements. A data element does not need to use a domain. In other repository objects, especially in ABAP programs, it is not possible to make a direct reference to a domain.

- [DDIC structures](abenddic_structures.md)

  Complex types whose components are other DDIC data types.

- [DDIC table types](abenddic_table_types.md)

  Complex types that describe [internal tables](../../abap-glossary/abeninternal_table_glosry.md) in ABAP.

In ABAP programs, the `TYPE` addition of declarative statements can be used to reference the DDIC data types. In these scenarios, data elements work like elementary ABAP types, structures work like structured ABAP types, and table types work like the corresponding ABAP types. The elementary components of each DDIC data type are based on a [built-in dictionary type](../ddic-built-in-data-types/abenddic_builtin_types.md) for which a [mapping](../ddic-built-in-data-types/abenddic_builtin_types.md) to the corresponding [built-in ABAP type](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) is defined. If a DDIC data type is changed, all consumers are modified automatically.

The name of a data type must follow the [naming rules for DDIC data types](abenddic_types_names.md).

In addition to its technical properties, a DDIC data type can have semantic information, such as documentation texts, texts for use on UIs, or search helps. Data types without semantic properties can also be declared in type pools.

## Hints

- DDIC data types can only be used by AS ABAP. They are not created as types on the database system.

- In addition to DDIC data types, [CDS entities](../../abap-glossary/abencds_entity_glosry.md) also represent data types which can be used as such in ABAP programs.

- Within a program, locally defined types hide identically named global types from the ABAP Dictionary.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A DDIC data type, such as the structure `DEMO_CONN`, can be referenced in the parameter interfaces of global procedures (methods or function modules) and in the ABAP programs that use the procedures.

``` abap
CLASS example DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS demo_meth 
      IMPORTING 
        para TYPE demo_conn. 
ENDCLASS. 
 
CLASS example IMPLEMENTATION. 
  METHOD demo_meth. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    DATA structure TYPE demo_conn. 
 
    example=>demo_meth( structure ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The elementary components of the structure `SYST` describe the [ABAP system fields](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The semantic properties of these components or the data elements used for them are designed for system fields used internally in programs. It is not recommended that these components or their data elements are used for other purposes, such as dynpro fields or Web Dynpro fields, only because their technical properties are suitable. Their semantic properties, in particular their text descriptions and documentation, are not usually suitable for UIs. If there are no types with suitable semantic properties that can be reused, new data types should be created.
