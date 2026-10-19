---
title: "CAST, Casting Operator"
source_file: abenconstructor_expression_cast.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Reference Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CAST, Casting Operator

## Syntax

``` abap
... CAST type( [let_exp] dobj ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md)

## Description

A [constructor expression](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) with the casting operator `CAST` performs a [downcast](../../abap-glossary/abendown_cast_glosry.md) or an [upcast](../../abap-glossary/abenup_cast_glosry.md) for the argument `dobj` and creates a reference variable of the static type `type` as a result. `type` can be specified as:

- any non-generic data type `dtype` or the completely generic data type `data`

- any [object type](../../abap-glossary/abenobject_type_glosry.md) (class or interface) including the completely generic object type `object`.

- The `#` character as a symbol for the [operand type](../../abap-glossary/abenoperand_type_glosry.md). This specification is only possible if the data type required in an operand position is unique and completely identifiable at compile time.

The parentheses must contain exactly one operand `dobj`:

- If a data type is specified, `dobj` must be a data reference variable `dref`.

- If an object type is used, `dobj` must be an object reference variable `oref`.

`dobj` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md).

The casting of `dobj` to the specified type takes place in accordance with the same rules as for the [casting operator](../../abap-glossary/abencasting_operator_glosry.md) [`?=`](abapmove_cast.md). If the specified type `type` is more specific than the static type of `dobj`, it is a [downcast](../../abap-glossary/abendown_cast_glosry.md). If `type` is more general than the static type of `dobj`, it is an explicit [upcast](../../abap-glossary/abenup_cast_glosry.md).

In [general expression positions](../abap-syntax-elements-of-an-abap-program/abengeneral_expression_positions.md), [functional positions](../abap-syntax-elements-of-an-abap-program/abenfunctional_positions.md) and [result positions](../../abap-glossary/abenresult_position_glosry.md), a constructor expression `CAST dtype( ... )` can be placed in front of `->` as follows:

- Like a data reference variable of static type `dtype`, the constructor expression can be followed by the [dereferencing operator](../../abap-glossary/abendereferencing_operat_glosry.md):

  `... CAST dtype( ... dref )->*` The result of this expression is the anonymous data object referenced by `dref`. If `dref` is initial, the uncatchable exception `DATREF_NOT_ASSIGNED` is raised.

- Like a data reference variable of a structured static type `dtype`, the constructor expression can be followed by the [object component selector](../../abap-glossary/abenobject_component_select_glosry.md) `->` pointing to a component of the structure:

  `... CAST dtype( ... dref )->comp|('comp_name') ...` The component can be specified statically as `comp` or dynamically as content of a character-like data object `comp_name`. If a dynamically specified component is not found, an exception of class `CX_SY_ASSIGN_ILLEGAL_COMPONENT` is raised. If `dref` is initial, the uncatchable exception `DATREF_NOT_ASSIGNED` is raised for static component specification and an exception of class `CX_SY_ASSIGN_ILLEGAL_COMPONENT` is raised for dynamic component specification.

- Like an object reference variable of a static class type `class` or interface type `intf`, the constructor expression can be followed by the [object component selector](../../abap-glossary/abenobject_component_select_glosry.md), pointing to:

  - An attribute of the class or interface:

    `... CAST class|intf( ... oref )->attr|('attr_name') ...` The attribute can be specified statically as `attr` or dynamically as content of a character-like data object `attr_name`. If a dynamically specified component is not found, an exception of class `CX_SY_ASSIGN_ILLEGAL_COMPONENT` is raised. If `oref` is initial, the uncatchable exception `OBJECTS_OBJREF_NOT_ASSIGNED` is raised for static component specification and an exception of class `CX_SY_ASSIGN_ILLEGAL_COMPONENT` is raised for dynamic component specification.

  - A method of the class or interface:

    `... CAST class|intf( ... oref )->meth( ... ) ...` The method can be specified only statically. Both [standalone method calls](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md) and [functional method calls](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) are possible. Such a `CAST` expression can also introduce [chained method calls](../../abap-glossary/abenchained_method_call_glosry.md). If `oref` is initial, the uncatchable exception `OBJECTS_OBJREF_NOT_ASSIGNED` is raised.

A single `CAST` expression not followed by the object component selector `->` can be specified as a standalone statement. This makes it possible to test the feasibility of a downcast by catching the associated exception `CX_SY_MOVE_CAST_ERROR`.

If a single expression points to a data object or a component of a data object using exactly one following object component selector, `->`:

- It can be specified as a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) in a [result position](../../abap-glossary/abenresult_position_glosry.md). The type of the result must be convertible to the data type `type` with the restriction: If the result is the result of a [bit expression](../../abap-glossary/abenbit_expression_glosry.md), `type` must be byte-like or character-like with the type `c` or `string`.

- An [offset/length specification](../../abap-glossary/abenoffset_length_specific_glosry.md) [`+off(len)`](../abap-operands/abenoffset_length.md) can be appended if the data type is suitable, unless the chaining is used as a [memory area](abapassign_mem_area_writable_exp.md) of the statement `ASSIGN`.

An optional `LET` expression [`let_exp`](../abap-declarations/abaplet.md) can be specified in front of the operand to define local helper fields.

## Hints

- The casting operator `CAST` is suitable for avoiding the declaration of helper variables that are only necessary for downcasts.

- Explicit upcasts with the casting operator `CAST` are suitable for determining a more general type of a declared reference variable in [inline declarations](../abap-declarations/abeninline_declarations.md).

- No empty parentheses can be specified after `CAST`.

- Unlike [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md), `CAST` works with an existing reference variable, which means that the result does not need to be saved to persist the referenced object.

- The predicate expression [`IS INSTANCE OF`](../abap-program-flow-logic/abenlogexp_instance_of.md) or the case distinction [`CASE TYPE OF`](../abap-program-flow-logic/abapcase_type.md) can be used to check whether a cast is possible to specific classes or interfaces.

- Downcasts are also possible using the `INTO` addition of the statement [`WHEN TYPE`](../abap-program-flow-logic/abapwhen_type.md) of a case distinction using [`CASE TYPE OF`](../abap-program-flow-logic/abapcase_type.md).

- The constructor operator [`CONV`](abenconstructor_expression_conv.md) is related to `CAST` but performs a [conversion](../../abap-glossary/abenconversion_glosry.md) instead of a [casting](../../abap-glossary/abencast_casting_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The source code section below shows two equally valid downcasts with the two possible [casting operators](../../abap-glossary/abencasting_operator_glosry.md) `?=` and `CAST`. Before the actual cast, its feasibility is checked using the predicate expression [`IS INSTANCE OF`](../abap-program-flow-logic/abenlogexp_instance_of.md).

``` abap
CLASS c1 DEFINITION. 
ENDCLASS. 
CLASS c2 DEFINITION INHERITING FROM c1. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA: oref1 TYPE REF TO c1, 
          oref2 TYPE REF TO c2. 
 
    oref1 = NEW c2( ). 
 
    IF oref1 IS INSTANCE OF c2. 
      oref2 ?= oref1. 
      oref2 =  CAST #( oref1 ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the dereferencing operator and component selector in `CAST` with data types. The constructor expressions can be used as [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) on the right and left side of assignments with the [assignment operator `=`](abenequals_operator.md).

``` abap
TYPES: BEGIN OF t_struc, 
        col1 TYPE i, 
        col2 TYPE i, 
       END OF t_struc. 
 
DATA dref  TYPE REF TO data. 
DATA struc TYPE t_struc. 
 
dref = NEW t_struc( ). 
 
struc      = CAST t_struc( dref )->*. 
struc-col1 = CAST t_struc( dref )->col1. 
struc-col2 = CAST t_struc( dref )->col2. 
 
CAST t_struc( dref )->*    = struc. 
CAST t_struc( dref )->col1 = struc-col1. 
CAST t_struc( dref )->col2 = struc-col2.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Introducing a method chaining with a `CAST` operator.

``` abap
INTERFACE intf. 
ENDINTERFACE. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
    METHODS: 
      meth1 RETURNING VALUE(r) TYPE REF TO cls, 
      meth2. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth1. 
    r = me. 
  ENDMETHOD. 
  METHOD meth2. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    out->write( 'meth2' ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA iref TYPE REF TO intf. 
 
    iref = NEW cls( ). 
 
    CAST cls( iref )->meth1( )->meth2( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

[RTTS](../../abap-glossary/abenrun_time_type_services_glosry.md) often requires a helper variable to perform a downcast of a type description object to a specialized class. These examples show how helper variables can be reduced by using the operator `CAST`.

``` abap
FINAL(attributes) = 
  CAST cl_abap_classdescr( 
       cl_abap_classdescr=>describe_by_name( 'CL_ABAP_FORMAT' ) 
       )->attributes. 
 
FINAL(components) = 
  CAST cl_abap_structdescr( 
       cl_abap_typedescr=>describe_by_name( 'T100' ) 
       )->components. 
 
FINAL(no_of_components) = 
  lines( CAST cl_abap_structdescr( 
              cl_abap_typedescr=>describe_by_name( 'SYST' ) 
              )->get_components( ) ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The factory method of the following class returns a reference variable of the type of the class itself. To use interface variables to access the components declared in the interface `if`, as recommended, the variable `iref`, declared inline, is cast to the type of the interface.

``` abap
INTERFACE if. 
  ... 
ENDINTERFACE. 
 
CLASS cl DEFINITION CREATE PRIVATE. 
  PUBLIC SECTION. 
    INTERFACES if. 
    CLASS-METHODS factory RETURNING VALUE(ref) TYPE REF TO cl. 
    ... 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS cl IMPLEMENTATION. 
  METHOD factory. 
    ref = NEW #( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(iref) = CAST if( cl=>factory( ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows static and dynamic specifications of components and how the system reacts to wrong specifications or to initial reference variables.

``` abap
TYPES: 
  BEGIN OF struc, 
    col TYPE i, 
  END OF struc. 
 
INTERFACE intf. 
ENDINTERFACE. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
    DATA attr TYPE string VALUE 'foo'. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA dref TYPE REF TO data. 
    DATA iref TYPE REF TO intf. 
 
    dref = NEW struc( col = 111 ). 
    iref = NEW cls( ). 
 
 
    DATA(num) = CAST struc( dref )->col. 
    ASSERT num = 111. 
    DATA(txt) = CAST cls( iref )->attr. 
    ASSERT txt = 'foo'. 
 
    CLEAR num. 
    num = CAST struc( dref )->('col'). 
    ASSERT num = 111. 
    CLEAR txt. 
    txt = CAST cls( iref )->('attr'). 
    ASSERT txt = 'foo'. 
 
    DATA(exc) = 0. 
    TRY. 
        num = CAST struc( dref )->('foo'). 
      CATCH cx_sy_assign_illegal_component. 
        exc += 1. 
    ENDTRY. 
    TRY. 
        txt = CAST cls( iref )->('foo'). 
      CATCH cx_sy_assign_illegal_component. 
        exc += 1. 
    ENDTRY. 
    CLEAR dref. 
    TRY. 
        num = CAST struc( dref )->('col'). 
      CATCH cx_sy_assign_illegal_component. 
        exc += 1. 
    ENDTRY. 
    CLEAR iref. 
    TRY. 
        txt = CAST cls( iref )->('attr'). 
      CATCH cx_sy_assign_illegal_component. 
        exc += 1. 
    ENDTRY. 
    ASSERT exc = 4. 
 
  ENDMETHOD. 
ENDCLASS. 
 
"Runtime error DATREF_NOT_ASSIGNED 
"num = CAST struc( dref )->col. 
"Runtime error OBJECTS_OBJREF_NOT_ASSIGNED 
"txt = CAST cls( iref )->attr.
```
