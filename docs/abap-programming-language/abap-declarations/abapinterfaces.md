---
title: "INTERFACES"
source_file: abapinterfaces.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Implementing or Including Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INTERFACES

## Syntax Forms

**[Implementing Interfaces in Classes](abapinterfaces_class.md)**

``` abap
1. INTERFACES intf 
    [PARTIALLY IMPLEMENTED] 
    { {[ABSTRACT METHODS meth1 meth2 ... ] 
       [FINAL METHODS meth1 meth2 ... ]} 
    | [ALL METHODS {ABSTRACT|FINAL}] } 
    [DATA VALUES attr1 = val1 attr2 = val2 ...]. 
```

**[Including Interfaces in Interfaces](abapinterfaces_ifac.md)**

``` abap
2. INTERFACES intf.
```

[`PARTIALLY IMPLEMENTED`](../abap-program-maintenance/abapinterfaces_partially.md)

## Description

This statement implements interfaces in classes or includes interfaces in other interfaces. It can be used in the [public](../../abap-glossary/abenpublic_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of the [declaration part](abapclass_definition.md) of classes and in [interface declarations](abapinterface_definition.md).
