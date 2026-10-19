---
title: "table_exp - Chainings"
source_file: abentable_exp_chaining.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - Chainings

[Table expressions](abentable_expressions.md) can be chained with the structure component selector `-`, with other table expressions, and with the object component selector `->`.

- [Chainings with the Structure Component Selector](abentable_exp_chaining.md#chainings-with-the-structure-component-selector)

- [Chainings with Table Expressions](abentable_exp_chaining.md#chainings-with-table-expressions)

- [Chainings with the Object Component Selector](abentable_exp_chaining.md#chainings-with-the-object-component-selector)

If the constructor operator `VALUE` or `REF` is specified before a chaining to [control the result](abentable_exp_result.md), only the final result is affected. Any intermediate results are always temporary field symbols and the corresponding performance notes should be considered.

## Hint

Chainings of table expressions with functional method calls, that is, specifying the internal table as a functional method call `meth( ... )[ ... ]` or `meth( ... )-comp[ ... ]` and accessing the internal table using a chained attribute access `meth( ... )->itab[ ... ]`, are not yet possible. Table expressions cannot currently be placed on the right of a method call in [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md).

## Chainings with the Structure Component Selector

A table expression can be chained as follows using the structure component selector `-`:

- If the result of a table expression `itab[ ... ]` is a structure, the structure component selector can be used to read each component `comp` of the structure:

  ` ... itab[ ... ]-comp|(comp) ...` As described for the [structure component selector](../abap-operands/abenstructure_component_selector.md), the component can be specified statically by `comp` or dynamically by `(comp)`. After a dynamic specification, only dynamic specifications can follow, but no static specification any more.

  - If a statically specified `comp` has a suitable type, a [specified offset/length](../../abap-glossary/abenoffset_length_specific_glosry.md) [`+off(len)`](../abap-operands/abenoffset_length.md) can be appended, except when the chaining is used as a [memory area](abapassign_mem_area_writable_exp.md) of the statement `ASSIGN` or as an operand of the reference operator [`REF`](abentable_exp_result.md).

  - A field `comp` used for a dynamic specification can contain an integer number for a position or the name of a component.

- If a structure `struct` has a table-like component `comp`, it can be specified as the name of the internal table of a table expression:

  ` ... struct-comp[ ... ] ...`

Both of these alternatives can be combined, enabling a structured component selector to be located directly on the left and right of a table expression.

### Hint

If the reference operator [`REF`](abenconstructor_expression_ref.md) is specified in front of a chaining whose result is a component of a structured table line, it creates a reference to this component.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the first column of the second line of the table-like second component of the first line of the internal table `itab`. The result is 4.

``` abap
TYPES: BEGIN OF struct1, 
         col1 TYPE i, 
         col2 TYPE i, 
       END OF struct1, 
       tab1 TYPE TABLE OF struct1 WITH EMPTY KEY, 
       BEGIN OF struct2, 
         col1 TYPE i, 
         col2 TYPE tab1, 
       END OF struct2, 
       tab2 TYPE TABLE OF struct2 WITH EMPTY KEY. 
 
FINAL(itab) = 
  VALUE tab2( 
    ( VALUE struct2( col1 = 1 
                     col2 = VALUE tab1( 
                              ( VALUE struct1( col1 = 2 
                                               col2 = 3 ) ) 
                              ( VALUE struct1( col1 = 4 
                                               col2 = 5 ) ) ) ) ) 
    ( VALUE struct2( col1 = 6 
                     col2 = VALUE tab1( 
                              ( VALUE struct1( col1 = 7 
                                               col2 = 8 ) ) 
                              ( VALUE struct1( col1 = 9 
                                               col2 = 10 ) ) ) ) ) ). 
 
FINAL(num) = itab[ 1 ]-col2[ 2 ]-col1.
```

### Executable Example

Table Expressions, Chainings

## Chainings with Table Expressions

If the result of a table expression `itab[ ... ]` is an internal table, it can be used as the name of the internal table of a table expression:

`... itab[ ... ][ ... ] ...`

An expression of this type can

- itself be continued with square brackets `[ ... ]`, if its result is again table-like.

- be combined with the information from structure component selectors above.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In an internal table nested twice, reads the first line of the innermost table in the second line of the center table in the second line of the outermost table. The result is 7.

``` abap
TYPES: tab1 TYPE TABLE OF i    WITH EMPTY KEY, 
       tab2 TYPE TABLE OF tab1 WITH EMPTY KEY, 
       tab3 TYPE TABLE OF tab2 WITH EMPTY KEY. 
 
FINAL(itab) = VALUE tab3( 
               ( VALUE tab2( 
                   ( VALUE tab1( 
                       ( 1 ) 
                       ( 2 ) ) ) 
                   ( VALUE tab1( 
                       ( 3 ) 
                       ( 4 ) ) ) ) ) 
               ( VALUE tab2( 
                   ( VALUE tab1( 
                       ( 5 ) 
                       ( 6 ) ) ) 
                   ( VALUE tab1( 
                       ( 7 ) 
                       ( 8 ) ) ) ) ) ). 
 
FINAL(num) = itab[ 2 ][ 2 ][ 1 ].
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Direct chaining of table expressions and chaining with the structure component selector in a single expression. Reading of the structure component of the innermost nested table with the value 13.

``` abap
TYPES: BEGIN OF struct1, 
         col1 TYPE i, 
         col2 TYPE i, 
       END OF struct1, 
       tab1 TYPE TABLE OF struct1 WITH EMPTY KEY, 
       BEGIN OF struct2, 
         col1 TYPE i, 
         col2 TYPE TABLE OF tab1 WITH EMPTY KEY, 
       END OF struct2, 
       tab2 TYPE TABLE OF struct2 WITH EMPTY KEY. 
 
FINAL(itab) = 
  VALUE tab2( 
    ( VALUE struct2( 
              col1 = 1 
              col2 = VALUE #( 
                       ( VALUE tab1( 
                           ( VALUE struct1( 
                                     col1 = 2 
                                     col2 = 3 ) ) 
                           ( VALUE struct1( 
                                     col1 = 4 
                                     col2 = 5 ) ) ) ) 
                       ( VALUE tab1( 
                           ( VALUE struct1( 
                                     col1 = 6 
                                     col2 = 7 ) ) 
                           ( VALUE struct1( 
                                     col1 = 8 
                                     col2 = 9 ) ) ) ) ) ) ) 
    ( VALUE struct2( 
              col1 = 10 
              col2 = VALUE #( 
                       ( VALUE tab1( 
                           ( VALUE struct1( 
                                     col1 = 11 
                                     col2 = 12 ) ) 
                           ( VALUE struct1( 
                                     col1 = 13 
                                     col2 = 14 ) ) ) ) 
                       ( VALUE tab1( 
                          ( VALUE struct1( 
                                    col1 = 15 
                                    col2 = 16 ) ) 
                          ( VALUE struct1( 
                                    col1 = 17 
                                    col2 = 18 ) ) ) ) ) ) ) ). 
 
FINAL(num) = itab[ 2 ]-col2[ 1 ][ 2 ]-col1.
```

## Chainings with the Object Component Selector

If the result of a table expression or one of the preceding chainings has a reference type, these chainings can be placed directly in front of the [object component selector](../../abap-glossary/abenobject_component_select_glosry.md) to access the components of the referenced object:

`... itab[ ... ]->comp|(comp_name) ...`

` ... itab[ ... ]-comp->comp|(comp_name) ...`

`... struct-comp[ ... ]->comp|(comp_name) ...`

`... itab[ ... ][ ... ]->comp|(comp_name) ...`

A component addressed in this way can, depending on its properties, be used in all suitable operand positions and particularly in further chainings.

As described for the [object component selector](../abap-operands/abenobject_component_selector.md), components can be specified statically by `comp` or dynamically by `(comp_name)`. After a dynamic specification, only dynamic specifications can follow, but no static specification any more.

### Hints

- More specifically, the [dereferencing operator](../../abap-glossary/abendereferencing_operat_glosry.md) `->*` can be specified after table expressions.

- An [instance method](../../abap-glossary/abeninstance_method_glosry.md) call can be a [standalone call](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md) or a [functional method call](../abap-calling-and-exiting-program-units/abapcall_method_functional.md). The obsolete form of the statement [`CALL METHOD`](../abap-obsolete-language-elements/abapcall_method_static.md) cannot be used.

- No table expressions can be specified in a write position for a read-only internal table. This also applies when the object component selector is used to access another object. Furthermore, [standalone method calls](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md) a not possible using a read-only internal table.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dereferencing a line of an internal table of data reference variables and accessing a single component.

``` abap
DATA itab TYPE TABLE OF REF TO scarr WITH EMPTY KEY. 
 
itab = VALUE #( ( NEW scarr( carrid = 'XX' carrname = 'YYYY' ) ) ). 
 
cl_demo_output=>new( 
  )->write_data( itab[ 1 ]->* 
  )->write_data( itab[ 1 ]->carrid 
  )->write_data( itab[ 1 ]->carrname )->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Filling of an internal table of reference variables with object references and accessing attributes and methods of the objects using table expressions in front of the object component selector.

``` abap
CLASS number DEFINITION. 
  PUBLIC SECTION. 
    DATA value TYPE i. 
    METHODS: 
      get RETURNING VALUE(r) TYPE i, 
      constructor IMPORTING n TYPE i. 
ENDCLASS. 
 
CLASS number IMPLEMENTATION. 
  METHOD get. 
    r = value. 
  ENDMETHOD. 
  METHOD constructor. 
    value = n. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    TYPES itab TYPE TABLE OF REF TO number WITH EMPTY KEY. 
    FINAL(itab) = VALUE itab( FOR j = 1 UNTIL j > 2 
                             ( NEW number( j ) ) ). 
    DATA(n1) = itab[ 1 ]->value. 
    DATA(n2) = itab[ 2 ]->get( ). 
  ENDMETHOD. 
ENDCLASS.
```
