---
title: "CLASS-METHODS, class_constructor"
source_file: abapclass-methods_constructor.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > CLASS-METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-METHODS, class_constructor

## Syntax

``` abap
CLASS-METHODS class_constructor.  
```

## Description

This statement declares the static constructor `class_constructor` of a class. It can only be used in the [public](../../abap-glossary/abenpublic_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of the declaration part of a class.

Each class has a predefined method `class_constructor` in its public visibility section. Its functions can be implemented class-specifically by explicit declaration. Without explicit declaration, the static constructor is empty.

The static constructor is called automatically exactly once per class and [internal session](../../abap-glossary/abeninternal_session_glosry.md) before the class is first accessed. Access to a class is the generation of an instance of the class or a static component using the class component selector, with the exception of is addressing a type or a constant of the class.

When a subclass is first accessed, the inheritance tree is searched for the next-highest superclass whose static constructor was not yet called. Afterwards, the static constructor of this superclass is called followed by those of all subsequent subclasses up to the addressed subclass. The static constructor must be fully executed, otherwise a runtime error occurs.

Like all static methods, the static constructor can only access the static components of its class. Furthermore, the static constructor must not explicitly address its own class.

## Hints

- Like instance constructors, static constructors are also an exception to the rule that all public components along a path in the inheritance tree are in one namespace.

- The time of execution of the static constructor is not fixed, but it is definitely called before the class is first accessed.

- A static constructor can call static methods of its class. Such a method must be implemented accordingly and must not rely on the static constructor being executed completely.

- It is not necessary to execute the static constructor to access a type or a constant of a class. This type of access therefore does not result in a call.

- The execution order of static constructors is dependent on the program flow. Static constructors must be implemented so that they can be executed in any order.

- In static constructors, class-based exceptions cannot be declared using `RAISING`, since it is generally not determined whether the user of a class is the first user and whether or not this user must handle exceptions propagated by the static constructor.

- If a [static component of a superclass](../abap-abap-objects/abeninheritance_statical.md) is addressed using the name of a subclass, the superclass is addressed and its static constructor is executed, but not the static constructor of the subclass.

- An unsuccessful dynamic access to a nonexistent component of a class does not count as an access to the class and the static constructor is not executed in this case.

- The static constructor should only be used according to its purpose to initialize global class data. It should not be used to call sophisticated processes, where the program flow cannot be controlled by the caller. This includes especially those that involve user interactions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

When a class is first accessed, the static constructor of the class sets static attributes to the current date and time.

``` abap
CLASS some_class DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS class_constructor. 
  PRIVATE SECTION. 
    CLASS-DATA: 
      start_time TYPE t, 
      start_date TYPE d. 
ENDCLASS. 
 
CLASS some_class IMPLEMENTATION. 
  METHOD class_constructor. 
    CONVERT UTCLONG utclong_current( ) 
            INTO DATE start_date 
                 TIME start_time 
            TIME ZONE 'UTC'. 
  ENDMETHOD. 
ENDCLASS.
```
