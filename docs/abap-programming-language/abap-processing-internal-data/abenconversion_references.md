---
title: "Assignment Rules for Reference Variables"
source_file: abenconversion_references.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Reference Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Assignment Rules for Reference Variables

The content of a reference variable can only be assigned to another reference variable and the following rules apply:

- [data references can only be assigned to data reference variables](abenconversion_references_data.md)

- [object references can only be assigned to object reference variables](abenconversion_references_objects.md)

No conversion takes place when variables are assigned. For an assignment to take place, the [static type](../../abap-glossary/abenstatic_type_glosry.md) of the target reference variable must be more general than or the same as the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) of the source reference variable. After a successful assignment, the target reference variable points to the same object as the source reference variable, that is, the target reference variable inherits the dynamic type of the source reference variable.

- [Static Type and Dynamic Type](abenconversion_references.md#static-type-and-dynamic-type)

- [Upcast and Downcast](abenconversion_references.md#upcast-and-downcast)

  - [Upcast](abenconversion_references.md#upcast)

  - [Downcast](abenconversion_references.md#downcast)

Assignments between reference variables and data objects that are not reference variables lead to a syntax error or the runtime error `OBJECTS_MOVE_NOT_SUPPORTED`.

## Static Type and Dynamic Type

Each reference variable has a dynamic type and a static type.

- The dynamic type is defined at runtime of the program, and is the data type of the data object or the class of the object to which the reference variable points. It determines the components the object contains.

- The static type is determined in the declaration of the reference variable. In data references, the static type is either a non-generic data type or the predefined generic type `data`. In object references, the static type is either a class or an interface, so an object reference can also be referred to as a class reference or an interface reference.

The static type of a reference variable is always less specific or the same as the dynamic type. This basic rule determines all assignments between reference variables.

### Hint

An initial reference variable contains the [null reference](../../abap-glossary/abennull_reference_glosry.md), which does not point to any objects. This means that it does not have a data type or a class as a dynamic type. The same applies to a non-initial reference variable that contains an invalid reference that no longer points to an object.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The object reference variable `oref` has the static type `super_class`. After the object is generated with `NEW`, its dynamic type is the special class `sub_class` - as shown by [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md).

``` abap
CLASS super_class DEFINITION. 
ENDCLASS. 
 
CLASS sub_class DEFINITION INHERITING FROM super_class. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA oref TYPE REF TO super_class. 
    oref = NEW sub_class( ). 
 
    cl_demo_output=>display( CAST cl_abap_classdescr( 
      cl_abap_refdescr=>describe_by_object_ref( oref ) 
                                                 )->absolute_name ). 
  ENDMETHOD. 
ENDCLASS.
```

## Upcast and Downcast

In an assignment between reference variables, the target variable inherits the dynamic type of the source variable. An assignment is possible if the static type of the target variable is less specific or the same as the dynamic type of the source variable.

### Upcast

If the static type of the target variables is less specific or the same as the static type of the source variable, an assignment is always possible. The name upcast comes from the fact that the movement within the inheritance tree is upwards. Since the target variable can have more dynamic types in comparison to the source variables, this assignment is also referred to as a widening cast. An upcast is possible in all ABAP statements in which the content of a data object is assigned to another data object. This includes, for example, assignments with the regular assignment operator ([`=`](abapmove_cast.md)), the insertion of lines in internal tables, or passes from actual to formal parameters.

Explicit castings using the [casting operator](../../abap-glossary/abencasting_operator_glosry.md) [`?=`](abapmove_cast.md) are also possible, but not usually necessary. Using the [casting operators](../../abap-glossary/abencasting_operator_glosry.md) [`CAST`](abenconstructor_expression_cast.md) for an upcast in combination with [inline declarations](../abap-declarations/abeninline_declarations.md), however, can be a good way of providing a reference variable with a more general type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See the previous example. The statement `iref = NEW class( )` is an upcast, because it is followed by an reference variable of the static type of a superclass that points to an object of a subclass.

### Downcast

If the static type of the target variable is more specific than the static type of the source variable, a check must be made at runtime, before the assignment is executed, whether it is less specific or the same as the dynamic type of the source variable. The name downcast comes from the fact that the movement in the inheritance space is downwards. Since the target variable can accept fewer dynamic types in comparison to the source variable, this assignment is also referred to as a narrowing cast. A downcast must always be performed explicitly. The following options are available:

- Special assignment with the [casting operator](../../abap-glossary/abencasting_operator_glosry.md) [`?=`](abapmove_cast.md).

- Use of a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) with the [casting operator](../../abap-glossary/abencasting_operator_glosry.md) [`CAST`](abenconstructor_expression_cast.md).

- Use of the addition `INTO` of the statement [`WHEN TYPE`](../abap-program-flow-logic/abapwhen_type.md) in a case distinction with [`CASE TYPE OF`](../abap-program-flow-logic/abapcase_type.md) for object reference variables.

If this prerequisite is not met, a catchable exception is raised, and the reference variable keeps its original value during the assignment.

### Hints

- For non-initial source variables, the predicate expression [`IS INSTANCE OF`](../abap-program-flow-logic/abenlogexp_instance_of.md) or the case distinction [`CASE TYPE OF`](../abap-program-flow-logic/abapcase_type.md) can be used to check whether a downcast is possible in specific classes or interfaces.

- The dynamic type of an initial or invalid source variable is undefined. In a downcast, the [null reference](../../abap-glossary/abennull_reference_glosry.md) or an invalid reference that does not point to an object can be assigned to every target variable that can be specified here.

- When a subclass is instantiated, an associated object reference variable cannot be cast to the subclass until the [instance constructors](../../abap-glossary/abeninstance_constructor_glosry.md) of all superclasses have been executed. When an instance constructor is executed, the dynamic type of the object reference variable is the current superclass.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows the three ways of performing a downcast for object reference variables.

- If the casting operator [`?=`](abapmove_cast.md) is used, the exception `CX_SY_MOVE_CAST_ERROR` is caught if a downcast is not possible.

- If the casting operator [`CAST`](abenconstructor_expression_cast.md) is used, the predicate expression [`IS INSTANCE OF`](../abap-program-flow-logic/abenlogexp_instance_of.md) is used in advance to check whether the downcast is possible.

- The use of the addition `INTO` of the statement [`WHEN TYPE`](../abap-program-flow-logic/abapwhen_type.md) in a case distinction with [`CASE TYPE OF`](../abap-program-flow-logic/abapcase_type.md) combines the check and the downcast.

In each of the three cases, `oref` is assigned to the class reference variable that is reached first. A check with `IS INSTANCE OF` would of course also be possible before the use of the casting operator `?=`.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    DATA a1 TYPE string VALUE `C1`. 
ENDCLASS. 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    DATA a2 TYPE string VALUE `C2`. 
ENDCLASS. 
CLASS c3 DEFINITION INHERITING FROM c2. 
  PUBLIC SECTION. 
    DATA a3 TYPE string VALUE `C3`. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(o) = cl_demo_output=>new( ). 
 
    DATA oref TYPE REF TO object. 
 
    oref = NEW c1( ). 
    DATA: 
      cref11 TYPE REF TO c1, 
      cref12 TYPE REF TO c2, 
      cref13 TYPE REF TO c3. 
    TRY. 
        cref13 ?= oref. 
        o->write( cref13->a3 ). 
      CATCH cx_sy_move_cast_error. 
        TRY. 
            cref12 ?= oref. 
            o->write( cref12->a2 ). 
          CATCH cx_sy_move_cast_error. 
            TRY. 
                cref11 ?= oref. 
                o->write( cref11->a1 ). 
              CATCH cx_sy_move_cast_error. 
            ENDTRY. 
        ENDTRY. 
    ENDTRY. 
 
    oref = NEW c2( ). 
    IF oref IS INSTANCE OF c3. 
      FINAL(cref23) = CAST c3( oref ). 
      o->write( cref23->a3 ). 
    ELSEIF oref IS INSTANCE OF c2. 
      FINAL(cref22) = CAST c2( oref ). 
      o->write( cref22->a2 ). 
    ELSEIF oref IS INSTANCE OF c1. 
      FINAL(cref21) = CAST c1( oref ). 
      o->write( cref21->a1 ). 
    ENDIF. 
 
    oref = NEW c3( ). 
    CASE TYPE OF oref. 
      WHEN TYPE c3 INTO FINAL(cref33). 
        o->write( cref33->a3 ). 
      WHEN TYPE c2 INTO FINAL(cref32). 
        o->write( cref32->a2 ). 
      WHEN TYPE c1 INTO FINAL(cref31). 
        o->write( cref31->a1 ). 
    ENDCASE. 
 
    o->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
