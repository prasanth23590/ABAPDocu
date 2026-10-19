---
title: "Filling a Structure"
source_file: abenstructure_filling_abexa.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Structures > Examples of Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Filling a Structure

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the filling of a nested structure.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_structure_filling DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    TYPES: 
      BEGIN OF name_type, 
        title   TYPE string, 
        prename TYPE string, 
        surname TYPE string, 
      END OF name_type, 
      BEGIN OF street_type, 
        name   TYPE string, 
        number TYPE string, 
      END OF street_type, 
      BEGIN OF city_type, 
        zipcode TYPE string, 
        name    TYPE string, 
      END OF city_type, 
      BEGIN OF address_type, 
        name   TYPE name_type, 
        street TYPE street_type, 
        city   TYPE city_type, 
      END OF address_type. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_structure_filling IMPLEMENTATION. 
  METHOD main. 
    DATA: name TYPE name_type, 
          addr TYPE address_type. 
    name-title   = `Mr.`. 
    name-prename = `Duncan`. 
    name-surname = `Pea`. 
    addr-name = name. 
    addr-street-name   = `Vegetable Lane`. 
    addr-street-number = `11`. 
    addr-city-zipcode = `349875`. 
    addr-city-name    = `Botanica`. 
 
    FINAL(address) = 
      VALUE address_type( 
        name-title   = `Mr.` 
        name-prename = `Duncan` 
        name-surname = `Pea` 
        street = VALUE #( name   = `Vegetable Lane` 
                          number = `11` ) 
        city   = VALUE #( zipcode = `349875` 
                          name    = `Botanica` ) ). 
 
    ASSERT address = addr. 
 
    out->write( address ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In this example, the structure from the executable example [Declaring a Nested Structure](../abap-declarations/abennested_structure_abexa.md) is defined with [`TYPES`](../abap-declarations/abaptypes_struc.md) as the data type `address_type` and used for the data objects `addr` and `address`. A separate structure type is also defined for each of the substructures.

If a structure is declared with the statement `DATA` by reference to a structure type as shown here, the addition [`VALUE`](../abap-declarations/abapdata_options.md) cannot be used. Instead, the structure must be filled by accessing the components. In particular, this also applies to the frequently occurring reference to structures of the ABAP Dictionary. There are mainly two ways for doing this:

- In the first part of the method `main`, the structure `addr` is filled using the structure component selector. The component `name` is assigned a prefilled structure. In the components `street` and `city`, the components that are nested there are accessed.

- In the second part of the method `main`, the structure `address` is filled with the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md), but the structure itself is created using an inline declaration. The parentheses after `VALUE` show different options for accessing the components of substructures. Either the structure component selector is used again in the same way as for the substructure `name`, or additional `VALUE` operators are nested, such as for `street` and `city`.

The content of both structures is the same. The value operator `VALUE` represents the modern way, where the need of expressing all the component names explicitly is replaced by the use of parentheses.
