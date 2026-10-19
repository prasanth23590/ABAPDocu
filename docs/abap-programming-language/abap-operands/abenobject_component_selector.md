---
title: "Object Component Selector"
source_file: abenobject_component_selector.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions > Notations for Single Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Object Component Selector

Components of an object can be specified statically and dynamically.

- [Static Component](abenobject_component_selector.md#static-component)

- [Dynamic Component](abenobject_component_selector.md#dynamic-component)

## Static Component

The following syntax accesses a component `comp` of an object statically:

`ref->comp`

The symbol `->` is the object component selector. A reference variable `ref` must be specified as follows to the left of the object component selector:

- Name of a reference variable that can itself be a composite.

- [Functional method call](../../abap-glossary/abenfunctional_method_call_glosry.md) or [method chaining](../../abap-glossary/abenmethod_chaining_glosry.md) with a reference variable as a result.

- Single or chained [table expression](../../abap-glossary/abentable_expression_glosry.md) whose result is a reference variable.

- [Constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) with the [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) or the [casting operator](../../abap-glossary/abencasting_operator_glosry.md) [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md).

The name `comp` of the component must be to the right of the object component selector. The object component selector dereferences the reference variable `ref` and makes the components of the referenced object accessible.

- If `ref` is an object reference variable, the components `comp` of the object - attributes and methods - to which the object reference variable points are addressed using the object component selector.

- If `ref` is a data reference variable that is typed as a structure, the components `comp` of the structure to which the data reference variable points are addressed using the object component selector.

If an attempt is made to access a data object (access to an [instance attribute](../../abap-glossary/abeninstance_attribute_glosry.md) by an [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md) or access to a structure component by a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md)) using a reference variable that contains the [null reference](../../abap-glossary/abennull_reference_glosry.md), an uncatchable exception `OBJECTS_OBJREF_NOT_ASSIGNED` or `DATREF_NOT_ASSIGNED` is raised. If an attempt is made to call an [instance method](../../abap-glossary/abeninstance_method_glosry.md) with a reference variable that contains the null reference, a catchable exception of the class `CX_SY_REF_IS_INITIAL` is raised.

### Hint

If `ref` is a data reference variable, the character `*` can be specified after the object component selector `->`, which creates the general [dereferencing operator](abendereferencing_operator.md) `->*`. The expression `ref->*` labels the entire data object to which the data reference variable points. The dereferencing operator is the only way to dereference data references. The dereferencing operator cannot be specified after object reference variables. The instance components of classes can only be accessed using the expression `ref->comp`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Accesses the public attribute `a1` of a class `c1` using an object reference variable `oref`.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    DATA a1 TYPE string READ-ONLY. 
ENDCLASS. 
 
... 
 
DATA oref TYPE REF TO c1. 
 
... oref->a1 ...
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The data reference variable `dref` is typed as a structure and the component `carrid` of the referenced structure is accessed using the object component selector. The expression `dref->carrid` has the same meaning as the chaining `dref->*-carrid`.

``` abap
DATA dref TYPE REF TO sflight. 
 
... 
 
... dref->carrid ...
```

## Dynamic Component

A component of an object can be specified dynamically with the following syntax:

``` abap
`... { dref->(comp_name) } 
  | { cref->(attr_name) } 
  | { iref->(attr_name) } ...`
```

The syntax and meaning is the same as for [dynamic components](../abap-processing-internal-data/abapassign_dynamic_components.md) and [dynamic access](../abap-processing-internal-data/abapassign_mem_area_dynamic_access.md) in the statement `ASSIGN` and the result of the expressions behave like an accordingly assigned field symbol of type `ANY`.

If the component is not found, an exception of class `CX_SY_ASSIGN_ILLEGAL_COMPONENT` occurs. This exception is also raised if the reference variable is initial.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic specification of a structure component and an interface attribute of an object.

``` abap
INTERFACE intf. 
  CONSTANTS attr TYPE string VALUE `YYY`. 
ENDINTERFACE. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(dref) = NEW scarr( carrid = 'XXX' ). 
 
    DATA(comp_name) = `carrid`. 
    cl_demo_output=>write( dref->(comp_name) ). 
 
    DATA iref TYPE REF TO intf. 
    FINAL(cref) = NEW cls( ). 
    iref = cref. 
 
    comp_name = `attr`. 
    cl_demo_output=>write( iref->(comp_name) ). 
 
    comp_name = `intf~` && comp_name. 
    cl_demo_output=>write( cref->(comp_name) ). 
 
    cl_demo_output=>display( ). 
  ENDMETHOD. 
ENDCLASS.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Behavior for initial reference. The example shows that an initial reference leads to a catchable exception `CX_SY_ASSIGN_ILLEGAL_COMPONENT` for a dynamic target but to an uncatchable exception `DATREF_NOT_ASSIGNED` for a static target.

``` abap
DATA dref TYPE REF TO scarr. 
DATA target TYPE string. 
 
TRY. 
    target = dref->('CARRID'). 
  CATCH cx_sy_assign_illegal_component. 
    DATA(exc) = 'X'. 
ENDTRY. 
ASSERT exc = 'X'. 
 
"Runtime error DATREF_NOT_ASSIGNED 
"target = dref->carrid.
```
