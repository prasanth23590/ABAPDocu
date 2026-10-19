---
title: "CLASS, INTERFACE, DEFERRED PUBLIC"
source_file: abapclass_interface_def_pub.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Declarations > Declaration and Loading"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, INTERFACE, DEFERRED PUBLIC

## Obsolete, deprecated Syntax

``` abap
CLASS class DEFINITION DEFERRED PUBLIC. 
 
INTERFACE intf DEFERRED PUBLIC.  
```

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Description

The variants of the statements [`CLASS DEFINITION DEFERRED`](../abap-declarations/abapclass_deferred.md) and [`INTERFACE DEFERRED`](../abap-declarations/abapinterface_deferred.md) with the addition `PUBLIC` are obsolete.

The addition `PUBLIC` explicitly delays loading the class or interface until the end of the current program unit. Individual components of the class or interface can only be accessed after it has been loaded.

## Hints

- These statements were previously required to prevent unwanted recursions when referring to global classes.
