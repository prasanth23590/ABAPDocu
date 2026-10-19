---
title: "itab - Nested Tables"
source_file: abennested_internal_tables_abexa.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, TABLE OF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Nested Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how nested internal tables are declared and used.

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
CLASS cl_demo_nested_internal_tables DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF t_address, 
        street TYPE c LENGTH 20, 
        city   TYPE c LENGTH 20, 
      END OF t_address, 
      t_address_tab TYPE STANDARD TABLE 
                    OF t_address 
                    WITH NON-UNIQUE KEY city. 
    DATA: 
      BEGIN OF company, 
        name      TYPE c LENGTH 20, 
        addresses TYPE t_address_tab, 
      END OF company, 
      company_tab        LIKE HASHED TABLE 
                  OF   company 
                  WITH UNIQUE KEY name, 
      company_sorted_tab LIKE SORTED TABLE 
                         OF   company 
                         WITH UNIQUE KEY name. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_nested_internal_tables IMPLEMENTATION. 
  METHOD main. 
 
    DATA: address TYPE t_address, 
          idx     TYPE sy-tabix. 
    FIELD-SYMBOLS <fs> LIKE company. 
 
* Filling Internal Tables 
    company_tab = VALUE #( 
      ( name   = 'Racing Bikes Inc.' 
        addresses = VALUE #( ( street = 'Fifth Avenue' 
                               city   = 'New York' ) 
                             ( street = 'Second Street' 
                               city   = 'Boston' ) ) ) 
      ( name   = 'Chocolatiers Suisse' 
        addresses = VALUE #( ( street = 'Avenue des Forets' 
                               city   = 'Geneve' ) 
                             ( street = 'Kleine Bachgasse' 
                               city   = 'Basel' ) 
                             ( street = 'Piazza di Lago' 
                               city   = 'Lugano' ) ) ) ). 
 
    out->next_section( `Table` ). 
 
    out->write( company_tab ). 
 
    out->next_section( `Some accesses` ). 
 
* Reading Internal Tables 
    READ TABLE company_tab 
         WITH TABLE KEY name = 'Racing Bikes Inc.' 
         ASSIGNING <fs>. 
    out->write( |{ <fs>-name }| ). 
    LOOP AT <fs>-addresses INTO address. 
      out->write( | { sy-tabix WIDTH = 4 }{ 
                    address-street WIDTH = 20 }{ 
                    address-city WIDTH = 20 } | ). 
    ENDLOOP. 
* Modifying Internal Tables 
    address-street = 'Rue des Montagnes'. 
    address-city   = 'Geneve'. 
    READ TABLE company_tab 
         WITH TABLE KEY name = 'Chocolatiers Suisse' 
         INTO company. 
    READ TABLE company-addresses TRANSPORTING NO FIELDS 
               WITH TABLE KEY city = address-city. 
    idx = sy-tabix. 
    MODIFY company-addresses FROM address INDEX idx. 
    MODIFY TABLE company_tab FROM company. 
* Moving and sorting Internal Tables 
    company_sorted_tab = company_tab. 
    LOOP AT company_sorted_tab INTO company. 
      out->write( |{ company-name }| ). 
      SORT company-addresses.                          "#EC CI_SORTLOOP 
      LOOP AT company-addresses INTO address. 
        out->write( | { sy-tabix WIDTH = 4 }{ 
                      address-street WIDTH = 20 }{ 
                      address-city WIDTH = 20 } | ). 
      ENDLOOP. 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example shows the declaration of two internal tables, `t_address_tab` and `company_tab`, where `t_address_tab` is contained in `company_tab`. For this, `t_address_tab` is defined as the table type. The component `addresses` of the `company` structure is declared with this type. The data type of `company` is used as the line type for the tables `company_tab` and `company_sorted_tab`.

The internal table is filled using the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md).

A line from `company_tab` is assigned to the field symbol `<fs>` using [`READ`](../abap-processing-internal-data/abapread_table.md) and its table-like component `addresses` is processed in a `LOOP`. The content of the line is assigned to the structure `address`. Since `addresses` is an index table, `sy-tabix` can be evaluated.

To change the content of the component `street` of a line of the inner table `addresses`, the index of the required line is determined using a `READ` statement and it is then used in [`MODIFY`](../abap-processing-internal-data/abapmodify_itab.md). To make the changes effective in the corresponding line of the outer hashed table as well, the key access of the `MODIFY` statement is used.

Finally, the hashed table is assigned a sorted table with the same line type. In this way, the entries are automatically sorted according to the table key `name`. The entries of the inner standard table, on the other hand, are sorted using the [`SORT`](../abap-processing-internal-data/abapsort_itab.md) statement.
