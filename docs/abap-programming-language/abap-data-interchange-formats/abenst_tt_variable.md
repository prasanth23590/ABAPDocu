---
title: "ST - tt:variable, Variables"
source_file: abenst_tt_variable.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Structure of ST Programs > ST - Data Declarations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:variable, Variables

## Syntax

``` abap
<tt:variable name="..." [ref-type="..."] 
                        [[s-val="..."][d-val="..."]]|[val="..."] />  
```

## Description

The statement `tt:variable` can be used to declare one or more variables in an ST program outside of a template. The attribute `name` is used to declare a symbolic name, which can be used to access the variable. This name can have a maximum of 30 characters.

The symbolic name is not case-sensitive and must be unique. The namespace also includes the data roots declared with [`tt:root`](abenst_tt_root.md) and the parameters declared with [`tt:parameter`](abenst_tt_parameter.md).

The variables in the context of the [main template](abenst_tt_template_main.md) can be addressed directly. The variables of the main template are not known in [subtemplates](abenst_tt_template_sub.md).

Variables are data of the ST program that, unlike the data roots, are not bound to ABAP data objects.

`ref-type` can be used to define the variable as a reference variable. The value of `ref-type` determines the static type of the reference variable. All global ABAP classes and interfaces for an object reference variable are possible, as are data types for a data reference variable. The names of classes and interfaces are specified directly and without namespaces. The names of data types must be specified using an XML namespace that determines the context of the data type, as with [`tt:type`](abenst_tt_type.md). Class reference variables and interface reference variables are intended primarily for creating objects and calling instance methods. Data reference variables, however, are used for binding appropriately typed interface parameters when ABAP methods are called.

The additions `s-val` and `d-val` or `val` can be used to assign a start value to each variable. The values are specified as [ABAP values](abenst_abap_representation.md). `s-val` only works for serialization, `d-val` only works for deserialization, and `val` works for serialization and deserialization.

Within a template, the statement [`tt:assign`](abenst_tt_assign.md) can be used to assign a value to a variable. The variables area accessed using the attribute `var` of the various [ST statements](abenst_statements.md).
