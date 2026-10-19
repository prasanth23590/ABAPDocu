---
title: "AMDP - Inheritance"
source_file: abenamdp_inheritance.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Inheritance

Both interface methods and redefined methods inherited from superclasses can become [AMDP methods](abenamdp_methods.md) in the implementation, provided that their prerequisites are met and the class contains the corresponding tag interface. If a superclass contains a tag interface, this also applies to its subclasses. If an interface contains a tag interface, this also applies to classes that implement this interface.

## Executable Examples

- [AMDP - AMDP Methods in Interfaces and Superclasses (Client-safe)](abenamdp_polymorphism_cs_abexa.md)
