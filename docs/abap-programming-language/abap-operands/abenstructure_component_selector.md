---
title: "Structure Component Selector"
source_file: abenstructure_component_selector.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions > Notations for Single Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Structure Component Selector

Components of a structure can be specified statically and dynamically.

- [Static Component](abenstructure_component_selector.md#static-component)

- [Dynamic Component](abenstructure_component_selector.md#dynamic-component)

## Hint

The structure component selector can especially used for [chainings](../abap-processing-internal-data/abentable_exp_chaining.md) behind [table expressions](../abap-processing-internal-data/abentable_expressions.md), statically as well as dynamically.

## Static Component

The following syntax accesses a component `comp` of a structure or structured data type statically:

`struct-comp`

The symbol `-` is the structure component selector. A structured data type or a structure `struct` must be specified as follows to the left of the structure component selector:

- Name of a structure or a structured type that can itself be linked.

- [Functional method call](../../abap-glossary/abenfunctional_method_call_glosry.md) or [method chaining](../../abap-glossary/abenmethod_chaining_glosry.md) with a structured result.

- Single or chained [table expression](../../abap-glossary/abentable_expression_glosry.md) that returns a structured table line.

The name `comp` of the component must be to the right of the structure component selector.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a structure `struc` with the structured data type `spfli` from the ABAP Dictionary and access to its component `carrid`.

``` abap
DATA struc TYPE spfli. 
 
... 
 
... struc-carrid ...
```

## Dynamic Component

A component of a structure (structured data object) can be specified dynamically with the following syntax:

`struc-(comp)`

The syntax and meaning is the same as for [dynamic structure components](../abap-processing-internal-data/abapassign_dynamic_components.md) in the statement `ASSIGN` and the result of the expressions behave like an accordingly assigned field symbol of type `ANY`.

If the component is not found, an exception of class `CX_SY_ASSIGN_ILLEGAL_COMPONENT` occurs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Method `GET` of class `CL_DEMO_STRUCT_COMP` returns the textual content of any component of any structure:

``` abap
METHOD get. 
  TRY. 
      comp_string = CONV string( struct-(comp) ). 
    CATCH cx_sy_assign_illegal_component INTO FINAL(exc). 
      comp_string = `Error: ` && exc->get_text( ). 
  ENDTRY. 
ENDMETHOD.
```

The following code snippet calls that method for a structure `scarr` and specifies the component via a name and via positions.

``` abap
SELECT SINGLE 
       FROM scarr 
       FIELDS 
         carrid, 
         carrname, 
         currcode, 
         url 
       WHERE carrid = 'LH' 
       INTO @FINAL(scarr). 
 
FINAL(out) = cl_demo_output=>new( ). 
 
out->next_section( 
  cl_demo_struct_comp=>get( struct = scarr 
                            comp   = 'CARRID' ) ). 
 
DO. 
  FINAL(comp) = 
    cl_demo_struct_comp=>get( struct = scarr 
                              comp   = sy-index ). 
  IF comp CS 'Error:'. 
    EXIT. 
  ELSE. 
    out->write( comp ). 
  ENDIF. 
ENDDO. 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following method of class `CL_DEMO_DYNAMIC_COMPONENT` assigns components of two structures dynamically:

- First, the structure is specified directly and the component is specified by its position.

- Second, the structure is specified by a writable expression with constructor operator `NEW` and the component is specified by its name, which can have an offset/length specification. For wrongly specified components, an exception occurs and is caught.

``` abap
METHOD main. 
  DATA(comp_position) = 2. 
  DATA(comp_name) = `col-carrid(2)`. 
  cl_demo_input=>new( 
   )->add_field( CHANGING field = comp_position 
   )->add_field( CHANGING field = comp_name 
   )->request(  ). 
 
  out->write( struct ). 
 
  TRY. 
      out->write( |{ comp_position }: { 
                     struct-(comp_position) }| ). 
    CATCH cx_sy_assign_illegal_component INTO FINAL(exc1). 
      out->write( exc1->get_text( ) ). 
  ENDTRY. 
 
  TRY. 
       out->write( |{ comp_name }: { NEW cls( )->attr-(comp_name) }| ). 
    CATCH cx_sy_assign_illegal_component INTO FINAL(exc2). 
      out->write(  exc2->get_text( ) ). 
  ENDTRY. 
 
ENDMETHOD.
```

## Executable Examples

- [Dynamic Structure Components](abendynamic_component_abexa.md)

- [`table_exp` - Accessing Components Dynamically](../abap-processing-internal-data/abentable_exp_dynamic_comp_abexa.md)
