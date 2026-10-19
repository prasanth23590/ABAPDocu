---
title: "INTERFACES, implementation"
source_file: abapinterfaces_class.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Implementing or Including Interfaces > INTERFACES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INTERFACES, implementation

## Syntax

``` abap
INTERFACES intf   
  [PARTIALLY IMPLEMENTED]   
  { {[ABSTRACT METHODS meth1 meth2 ... ]   
     [FINAL METHODS meth1 meth2 ... ]}   
  | [ALL METHODS {ABSTRACT|FINAL}] }   
  [DATA VALUES attr1 = val1 attr2 = val2 ...].  
```

[`PARTIALLY IMPLEMENTED`](../abap-program-maintenance/abapinterfaces_partially.md)

### Addition

[1. `... ABSTRACT METHODS meth1 meth2 ...`](abapinterfaces_class.md#addition-1)

[2. `... FINAL METHODS meth1 meth2 ...`](abapinterfaces_class.md#addition-2)

[3. `... ALL METHODS {ABSTRACT|FINAL}`](abapinterfaces_class.md#addition-3)

[4. `... DATA VALUES attr1 = val1 attr2 = val2 ...`](abapinterfaces_class.md#addition-4)

## Overview

### Description

In the [public](../../abap-glossary/abenpublic_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of a class, the statement `INTERFACES` implements the interface `intf` in the class. Additions can also be specified to determine the properties of interface components in the class.

All local or global interfaces that are visible here can be specified for `intf` that are not already included in a superclass of the current class. The components of the interfaces become public components of the class after the implementation. An interface component called `comp` has the name `intf~comp` in the class, where `intf` is the name of the interface and the character `~` is the interface component selector. A class must implement all methods of the interface in its implementation part, with the following exceptions:

- Interface methods declared as optional using the addition [`DEFAULT`](abapmethods_default.md).

- Interface methods that are specified in the class after the addition `ABSTRACT METHODS` and are therefore declared as abstract.

- Partial implementations are allowed in test classes using the addition [`PARTIALLY IMPLEMENTED`](../abap-program-maintenance/abapinterfaces_partially.md).

### Hints

- A class can implement any number of different interfaces. All of the interfaces implemented by a class are equal and on the same level. If an interface `intf` implemented in a class is a composite, that is, it contains component interfaces, these are implemented in the class like individual interfaces, regardless of their nesting hierarchy, and their components are addressed using the name of their component interface instead of using the name `intf`. It is generally not possible to use the interface component selector multiple times in a name (`intf1~intf2~comp`).

- Each interface appears only once in a class and every interface component `comp` is always clearly available using the `intf~comp`. Even the components of an interface that is the interface component of one or more other interface, and appears to be implemented multiple times in a class, only exist once.

- If the implementation of a non-optional method of a global interface implemented using `INTERFACES` is missing in a class, a syntax warning occurs instead of a syntax error. This prevents classes from becoming unusable due to subsequent enhancements of global interfaces. Calling a missing implementation, however, always raises an exception of the class `CX_SY_DYN_CALL_ILLEGAL_METHOD` and, if not handled, produces the runtime error `CALL_METHOD_NOT_IMPLEMENTED`. A real syntax error is produced when local interfaces are used, and the implementation is missing.

- If a class implements a method `intf~...` of a global interface `intf` implemented using `INTERFACES` in its implementation part and the method is not declared in the interface, a warning is raised by the syntax check. This type of method implementation is dead code that cannot be executed and should removed. Classes become unusable in the case of a syntax error if methods were later deleted from an implemented global interface, and which were implemented without a role in a class and had no values. An actual syntax error occurs when local interfaces are used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Implementation of an interface `intf` in a class `demo`.

``` abap
INTERFACE intf. 
  CLASS-DATA selfref TYPE REF TO intf. 
  CLASS-METHODS factory RETURNING VALUE(ref) TYPE REF TO intf. 
  ... 
ENDINTERFACE. 
 
CLASS demo DEFINITION CREATE PRIVATE. 
  PUBLIC SECTION. 
    INTERFACES intf. 
    ALIASES: 
      selfref FOR intf~selfref, 
      factory FOR intf~factory. 
    ... 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD factory. 
    IF selfref IS INITIAL. 
      selfref = NEW demo( ). 
      ref = selfref. 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(iref) = demo=>factory( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Addition 1

`... ABSTRACT METHODS meth1 meth2 ...`

## Addition 2

`... FINAL METHODS meth1 meth2 ...`

### Description

Using the additions `ABSTRACT METHODS` and `FINAL METHODS`, the individual instance methods `meth` of the interface can be made either abstract or final in the class to be implemented. The same rules apply as to the additions [`ABSTRACT`](abapmethods_abstract_final.md) and [`FINAL`](abapmethods_abstract_final.md) of the statement [`METHODS`](abapmethods.md). In particular, the whole class must be abstract if an interface method is made abstract and no interface method can be listed after `ABSTRACT METHODS` and `FINAL METHODS`.

The following can be specified as methods `meth1`, `meth2`, ...

- Instance methods that are declared in the interface `intf` itself.

- Alias names declared in the interface `intf` for instance methods declared in interfaces that are included in `intf`.

- Instance methods that are declared in interfaces included in `intf` using the name of their interface and the interface component selector (`~`). In this case the component interface cannot itself be included with the statement `INTERFACES`.

If an interface is included using multiple `INTERFACES` statements, the specifications in the additions `FINAL` and `ABSTRACT` must not produce contradictory definitions for a method.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of abstract methods when including two interfaces `intf1` and `intf2` in an abstract class `cls`.

``` abap
INTERFACE intf1. 
  METHODS meth1. 
ENDINTERFACE. 
 
INTERFACE intf2. 
  INTERFACES intf1. 
  METHODS meth2. 
ENDINTERFACE. 
 
CLASS cls DEFINITION ABSTRACT. 
  PUBLIC SECTION. 
    INTERFACES intf1 ABSTRACT METHODS meth1. 
    INTERFACES intf2 ABSTRACT METHODS meth2. 
ENDCLASS.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Short form of the preceding example. Since `intf2` includes the interface `intf1`, its methods can be specified as `intf1~meth1`. This means that a separate statement `INTERFACES intf1` is no longer possible in this class.

``` abap
INTERFACE intf1. 
  METHODS meth1. 
ENDINTERFACE. 
 
INTERFACE intf2. 
  INTERFACES intf1. 
  METHODS meth2. 
ENDINTERFACE. 
 
CLASS cls DEFINITION ABSTRACT. 
  PUBLIC SECTION. 
    INTERFACES intf2 ABSTRACT METHODS intf1~meth1 meth2. 
ENDCLASS.
```

## Addition 3

`... ALL METHODS {ABSTRACT|FINAL}`

### Description

Instead of making individual interface methods in the class abstract or final it is possible, using the addition `ALL METHODS {ABSTRACT|FINAL}`, to make all interface methods either [abstract](abapmethods_abstract_final.md) or [final](abapmethods_abstract_final.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Implementation of an interface `intf` in an abstract class `cls1`, in which all methods are made abstract and must be implemented in a subclass `cls2`.

``` abap
INTERFACE intf. 
  METHODS: 
    meth1, 
    meth2. 
  ... 
ENDINTERFACE. 
 
CLASS cls1 DEFINITION ABSTRACT. 
  PUBLIC SECTION. 
    INTERFACES intf ALL METHODS ABSTRACT. 
    ALIASES: 
      meth1 FOR intf~meth1, 
      meth2 FOR intf~meth2. 
ENDCLASS. 
 
CLASS cls2 DEFINITION INHERITING FROM cls1. 
  PUBLIC SECTION. 
    METHODS: 
      meth1 REDEFINITION, 
      meth2 REDEFINITION. 
ENDCLASS. 
 
CLASS cls2 IMPLEMENTATION. 
  METHOD meth1. 
    ... 
  ENDMETHOD. 
  METHOD meth2. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```

## Addition 4

`... DATA VALUES attr1 = val1 attr2 = val2 ...`

### Description

Using the addition `DATA VALUES`, initial values can be assigned to individual attributes `attr`. For attributes, this addition fulfills the same functions as the addition `VALUE` of the statement [`DATA`](abapdata.md) for attributes in its own class.

The following can be specified as attributes `attr1`, `attr2`, ...

- Attributes that are declared in the interface `intf` itself.

- Alias names declared in the interface `intf` for attributes declared in interfaces that are included in `intf`.

- Attributes that are declared in interfaces included in `intf` using the name of its own interface and the interface component selector (`~`). In this case the component interface cannot itself be included with the statement `INTERFACES`.

Constants declared in the interface or in a component interface with the statement [`CONSTANTS`](abapconstants.md) cannot be specified after the addition `DATA VALUES`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Implementation of an interface `intf` in a class `demo`, where the interface attributes are assigned start values.

``` abap
INTERFACE intf. 
  CLASS-DATA: 
    attr1 TYPE string, 
    attr2 TYPE string. 
  ... 
ENDINTERFACE. 
 
CLASS demo DEFINITION ABSTRACT. 
  PUBLIC SECTION. 
    INTERFACES intf 
      DATA VALUES attr1 = 'Hello' 
      attr2 = 'World'. 
    ALIASES: 
      attr1 FOR intf~attr1, 
      attr2 FOR intf~attr2. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
  FINAL(out) = cl_demo_output=>new( ). 
 
  out->write( |{ demo=>attr1 } { demo=>attr2 }| ). 
 
  out->display( ). 
ENDMETHOD. 
ENDCLASS.
```
