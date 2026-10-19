---
title: "CREATE DATA, HANDLE"
source_file: abapcreate_data_handle.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE DATA, HANDLE

## Syntax

``` abap
CREATE DATA dref     
                 TYPE HANDLE handle.  
```

## Description

The statement `CREATE DATA` uses the addition `HANDLE` to create a data object whose data type is described by an [RTTS](../../abap-glossary/abenrun_time_type_services_glosry.md) [type description object](../../abap-glossary/abentype_object_glosry.md). For `handle`, a reference variable of the static type of class `CL_ABAP_DATADESCR` or its subclasses that points to a type description object must be specified. The type description object may have been created by using the RTTS methods on existing data objects or by using the dynamic definition of a new data type.

The type description object must describe a non-generic type. Only type description objects for the generic ABAP types `c`, `n`, `p`, and `x` create and use a new [bound data type](../../abap-glossary/abenbound_data_type_glosry.md) with the [standard values](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md). Similarly, a type description object for a standard table with a generic table type creates and uses a new bound table type with a standard key.

## Hints

- The following are important methods for the dynamic definition of data types:

  - `GET_C`, `GET_D`, `GET_F` ... of the class `CL_ABAP_ELEMDESCR` for type description objects of elementary data types. These create either a new type description object in accordance with the input parameters or reuse an existing type object.

  - `GET` of the classes `CL_ABAP_STRUCTDESCR`, `CL_ABAP_TABLEDESCR`, and `CL_ABAP_REFDESCR` as well as `GET_BY_NAME` of the class `CL_ABAP_REFDESCR` for type description objects of structures, internal tables, and reference variables. These return the type description object that was specified by the input parameters. Either a new type description object is created or an existing one is used again.

  - `CREATE` of the classes `CL_ABAP_STRUCTDESCR`, `CL_ABAP_TABLEDESCR`, and `CL_ABAP_REFDESCR` for creating type description objects for structures, internal tables, and reference variables. These return the type description object that was specified by the input parameters. A new type description object is always created.

- It is recommended that the `GET` methods are used instead of `CREATE` to avoid creating multiple type description objects for a single type.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an anonymous data object using a type description object for a dictionary structure that is obtained using [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md).

``` abap
DATA dref TYPE REF TO data. 
 
FINAL(type) = CAST cl_abap_datadescr( 
  cl_abap_typedescr=>describe_by_name( 'SCARR' ) ). 
 
CREATE DATA dref TYPE HANDLE type.
```

## Executable Example

[Creating a Structure Using RTTC](abencreate_data_via_rttc_abexa.md)
