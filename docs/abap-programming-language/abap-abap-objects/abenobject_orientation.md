---
title: "ABAP Objects - Object Orientation"
source_file: abenobject_orientation.html
section: "ABAP Programming Language > ABAP - ABAP Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Object Orientation

Object orientation, or rather object-oriented programming, is a problem-solving method that represents the real world in a series of software objects.

Object-oriented programming is based on a programming model in which data and functions are unified in objects. The remaining language scope of ABAP mainly supports procedural programming, where the data is stored separately from objects and where programs that are modularized by procedures access this data.

In the following, a few general terms that are widely used in object orientation and in ABAP Objects are defined.

## Objects

Objects represent abstract or concrete objects of the real world and are the center of object oriented thinking. Objects contain data, called attributes, and provide services in the form of methods (sometimes also referred to as operations or functions). Methods typically operate on private data (also referred to as attributes or object state) that are only visible to the methods of the object. The attributes of an object are therefore not changed directly by the user, but only by the methods of the object. This guarantees the internal consistency of the object.

## Classes

Classes are program code that describes objects. Technically, an object is an instance of a class. In theory, it is possible to create an infinite number of similar objects from a single class definition. Each instance of a class (object) has its own values for all of its attributes.

## Object References

Programs identify and address objects using a unique object reference. They are used to access the attributes and methods of an object.

In object-oriented programming, objects usually have the following characteristics:

## Encapsulation

Objects restrict the external visibility of their resources (attributes and methods) for others. Each object has an interface that determines how other objects or applications can handle it. The implementation of the object is encapsulated, that is, it is not visible to the outside.

## Polymorphism

The same identically named methods can behave differently in different classes. In object-oriented programming, there is a construct called interface that can be used to address methods with the same name in different objects. While the address is always the same using the interface, the execution of the method is class-specific and can differ.

## Inheritance

A class can be derived from another class. A derived class (subclass) inherits the data and methods of its superclass. New methods can be added or existing methods redefined. Redefined methods have the same name and interface as the original method. Their classes are therefore also polymorphous.

## Benefits of Object Orientation

The benefits of object oriented programming include, among other things, meeting the following goals:

- Complex software systems become easier to understand, since an object-oriented architecture resembles reality to a greater extent than other programming techniques.

- Changes in object-oriented systems should be possible locally (at class level), without further changes being necessary in other parts of the system. This reduces overall maintenance work.

- Object-oriented programming supports the reusability of individual components by polymorphism and inheritance.

- Object-oriented systems require fewer revisions and less maintenance work, because many problems can be discovered and corrected in the design and development phases.

Achieving these goals requires:

- Object-oriented programming languages

  Object-oriented programming techniques do not necessarily depend on object-oriented programming languages. However, they do depend on the implementation of object-oriented constructions in the system kernel.

- Object-oriented tools

  Object-oriented tools support the creation of object-oriented programs with object-oriented languages. They are used to store and visualize development objects and the relationships between them.

- Object-oriented modeling

  Object-oriented modeling of a software system is the most important requirement and also the most time consuming and most difficult task when achieving the goals mentioned above. Object-oriented design includes more than just object-oriented programming, and offers logical advantages that are independent of the actual implementation.
