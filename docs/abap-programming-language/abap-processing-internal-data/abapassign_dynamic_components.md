---
title: "ASSIGN, dynamic_components"
source_file: abapassign_dynamic_components.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN > ASSIGN, mem_area"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN, dynamic_components

## Syntax

``` abap
... { struc-(comp) }   
  | { dref->(comp_name) }   
  | { COMPONENT comp OF STRUCTURE struc } ...  
```

### Alternative

[1. `... struc-(comp)`](abapassign_dynamic_components.md#alternative-1)

[2. `... dref->(comp_name)`](abapassign_dynamic_components.md#alternative-2)

[3. `... COMPONENT comp OF STRUCTURE struc`](abapassign_dynamic_components.md#alternative-3)

## Overview

### Description

These variants for specifying the memory area [`mem_area`](abapassign_mem_area.md) of the statement [`ASSIGN`](abapassign.md) access components of structures dynamically.

In these variants, the statement `ASSIGN` sets the return code `sy-subrc`. If the assignment is successful, `sy-subrc` is set to 0. In these variants, also exceptions can occur in case of some invalid dynamic specifications. If the assignment is not successful and no exception occurs, `sy-subrc` is set to 4. If `sy-subrc` is set to 4, the state of the field symbol depends on the addition [`ELSE UNASSIGN`](abapassign_else_unassign.md):

- If `ELSE UNASSIGN` is not specified, the field symbol keeps its previous state.

- If `ELSE UNASSIGN` is specified, no memory area is assigned to the field symbol. The field symbol has the state unassigned after the `ASSIGN` statement.

### Hint

If `ELSE UNASSIGN` is not specified, it is not sufficient to evaluate the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`<fs> IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) but `sy-subrc` must be checked. If `ELSE UNASSIGN` is specified, the predicate expression as well as `sy-subrc` can be evaluated.

## Alternative 1

`... struc-(comp)`

### Description

This variant of `mem_area` assigns the memory area of a component specified in `comp` of a structure `struc` to the field symbol. `struc` is a [result position](../../abap-glossary/abenresult_position_glosry.md). The structure can be specified as a data object or as a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md). If it is detected at compile time that `struc` is not a structure, a syntax error occurs. If that is detected at runtime, the runtime error `STRUCTURE_ILLEGAL` occurs.

For `comp`, either a character-like data object or a numeric data object of type `i` can be specified:

- If `comp` is character-like, its content is interpreted as the name of the component. The name is not case-sensitive. It may contain offsets and lengths, structure component selectors, and component selectors.

- If `comp` is of type `i`, its value is interpreted as the position of the component in the structure. If the value of `comp` is 0, the memory area of the entire structure is assigned to the field symbol.

- If `comp` has a different type, a syntax error or runtime error occurs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Two dynamic assignments with dynamic specification of components:

- in the first, the structure is specified directly and the component is specified by its position.

- in the second, the structure is specified by a writable expression with constructor operator `NEW` and the component is specified by its name, which can have an offset/length specification.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    TYPES: 
      BEGIN OF struct, 
        col TYPE scarr, 
      END OF struct. 
    DATA attr TYPE struct. 
ENDCLASS. 
 
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    DATA struct TYPE scarr. 
    METHODS meth. 
ENDCLASS. 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
     FINAL(out) = cl_demo_output=>new( ). 
 
    DATA(comp1) = 1. 
    cl_demo_input=>add_field( CHANGING field = comp1 ). 
    DATA(comp2) = `col-carrid(2)`. 
    cl_demo_input=>request( CHANGING field = comp2 ). 
 
    ASSIGN struct-(comp1) TO FIELD-SYMBOL(<fs1>). 
    out->write( sy-subrc ). 
 
    ASSIGN NEW cls( )->attr-(comp2) TO FIELD-SYMBOL(<fs2>). 
    out->write( sy-subrc ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

### Executable Example

[Field Symbols, Dynamic Structure Components](abenassign_component_abexa.md)

## Alternative 2

`... dref->(comp_name)`

### Description

This variant accesses components of structures that are referenced by a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) `dref`. `dref` can be any data reference variable that points to structure that contains the component specified in a character-like field `comp_name`.

The component name does not have to be in uppercase letters. It can contain offsets/lengths, structure component selectors, object component selectors, and class component selectors, in order to assign parts of the component or referenced objects of the component.

Unlike all other operand positions, where a data reference that does not point to a data object raises an exception, no exception occurs in the statement `ASSIGN` and `sy-subrc` is set to 4.

### Hint

This syntax form corresponds to [dynamic access](abapassign_mem_area_dynamic_access.md) to object components.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic assignment of a component of a structure to a field symbol. The default value of `comp_name` denotes a substring of a component of a substructure.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  BEGIN OF struc, 
    BEGIN OF substruc, 
      col TYPE c LENGTH 10 VALUE 'abcdefghij', 
    END OF substruc, 
  END OF struc. 
 
FINAL(dref) = REF #( struc ). 
 
DATA(comp_name) = `substruc-col+2(5)`. 
cl_demo_input=>request( CHANGING field = comp_name ). 
 
ASSIGN dref->(comp_name) TO FIELD-SYMBOL(<fs>). 
 
IF sy-subrc = 0. 
  out->write( <fs> ). 
ELSE. 
  out->write( 'Wrong specification' ). 
ENDIF. 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic assignment of a component of a structure with an initial reference variable. No exception occurs but `sy-subrc` is set to 0 in this case.

``` abap
DATA dref TYPE REF TO scarr. 
 
ASSIGN dref->('carrid') TO FIELD-SYMBOL(<carrid1>). 
ASSERT sy-subrc = 4. 
 
dref = NEW #( ). 
ASSIGN dref->('carrid') TO FIELD-SYMBOL(<carrid2>). 
ASSERT sy-subrc = 0.
```

## Alternative 3

`... COMPONENT comp OF STRUCTURE struc`

### Description

This variant of `mem_area` assigns the memory area of a component `comp` of a structure `struc` to the field symbol.

`struc` is a [result position](../../abap-glossary/abenresult_position_glosry.md). The structure can be specified as a data object or as a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md). If it is detected at compile time, that `struc` is not a structure:

- A syntax error occurs if it is specified as an expression.

- No syntax error occurs, if it is specified directly as a data object.

If it is detected at runtime that `struc` is not a structure, in both cases, `sy-subrc` is set to 4 and the state of the field symbol depends on addition `ELSE UNASSIGN`.

`comp` is a [character-like](../../abap-glossary/abencharlike_expr_position_glosry.md) or [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md). The evaluation depends on the data type of `comp`:

- If the field `comp` has a text-like type (`c` or `string`) or the type of a [flat](../../abap-glossary/abenflat_structure_glosry.md) structure, which exclusively contains character-like components, its content is interpreted as the name of the component. The component name does not have to be in uppercase letters. It may contain offsets and lengths, structure component selectors, and component selectors for assigning structured data objects and attributes in classes or objects.

- If the field `comp` has a non-text-like elementary type, the content is converted to the type `i` and interpreted as the position of the component in the structure. If the value of `comp` is 0, the memory area of the entire structure is assigned to the field symbol.

- If `comp` has a different type, a syntax error or runtime error occurs.

### Hints

- If the structure `struc` is specified as a [table expression](../../abap-glossary/abentable_expression_glosry.md) and the corresponding line is not found, the exception `CX_SY_ITAB_LINE_NOT_FOUND` is raised.

- Writable expressions can be specified for `struc` but no other expressions, since only these can have a non-temporary result. Assigning a component of a temporary structure to a field symbol would not make sense.

- If `struc` is specified directly as a data object, it is advisable to specify only structures and to check this in advance if necessary. Just evaluating `sy-subrc` is not enough to determine why an assignment was not successful.

- Identifying a component by its name is far less efficient than using its position, since far more internal processes are involved. Using `COMPONENTS OF`, however, is always more efficient than specifying the name after the structure component selector within a fully dynamically specified component in a parenthesized data object `name`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of all components of a structure to a field symbol in a loop. In every loop pass, the component is assigned whose position is determined by the loop index.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = 'UA' 
       INTO @FINAL(wa). 
 
DO. 
  ASSIGN COMPONENT sy-index OF STRUCTURE wa TO FIELD-SYMBOL(<fs>). 
  IF sy-subrc <> 0. 
    EXIT. 
  ENDIF. 
  out->write( <fs> ). 
ENDDO. 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following method shows the dynamic assignment of the components of a structure that is passed to the parameter `para` of the method to a field symbol `<comp>`. The implementation uses [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md). A [downcast](../../abap-glossary/abendown_cast_glosry.md) of the type description object to the class `CL_ABAP_STRUCTDESCR` for the passed data object ensures that the object is a structure. A loop across the component table `COMPONENTS` assigns the components to the field symbol via their names.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    METHODS meth 
      IMPORTING para TYPE data. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
    TRY. 
        FINAL(struct_descr) = CAST cl_abap_structdescr( 
          cl_abap_typedescr=>describe_by_data( para ) ). 
      CATCH cx_sy_move_cast_error. 
        RETURN. 
    ENDTRY. 
    LOOP AT struct_descr->components 
            ASSIGNING FIELD-SYMBOL(<comp_descr>). 
      ASSIGN COMPONENT <comp_descr>-name 
             OF STRUCTURE para TO FIELD-SYMBOL(<comp>). 
      ... 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of a component of a line of an internal table to a field symbol.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF struc, 
    col1 TYPE i, 
    col2 TYPE i, 
  END OF struc. 
 
DATA itab TYPE STANDARD TABLE OF struc WITH EMPTY KEY. 
 
itab = VALUE #( ( col1 = 1 col2 = 2 ) 
                ( col1 = 3 col2 = 4 ) ). 
 
ASSIGN COMPONENT 2 OF STRUCTURE itab[ 2 ] TO FIELD-SYMBOL(<fs>). 
 
out->write( <fs> ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Trying to assign a component of data object that is not a structure to a field symbol. This is detected only at runtime in this variant. `sy-subrc` is set to 4 and using `ELSE UNASSIGN` the field symbol that was assigned before is unassigned.

``` abap
FINAL(field) = 111. 
 
ASSIGN field TO  FIELD-SYMBOL(<fs>). 
ASSERT <fs> IS ASSIGNED. 
 
ASSIGN COMPONENT 1 OF STRUCTURE field TO <fs> ELSE UNASSIGN. 
IF sy-subrc <> 0. 
  ASSERT <fs> IS NOT ASSIGNED. 
ENDIF.
```
