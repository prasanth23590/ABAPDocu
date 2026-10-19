---
title: "[CLASS-]METHODS, AMDP OPTIONS"
source_file: abapmethods_amdp_options.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# \[CLASS-\]METHODS, AMDP OPTIONS

## Syntax

``` abap
[CLASS-]METHODS meth ... AMDP OPTIONS [READ-ONLY] 
                                      [client_handling] ...  
```

[`client_handling`](abapmethods_amdp_options_client.md)

### Addition

[`... READ-ONLY`](abapmethods_amdp_options.md#addition)

## Overview

### Description

The addition `AMDP OPTIONS` for [`METHODS`](../abap-declarations/abapmethods.md) and [`CLASS-METHODS`](../abap-declarations/abapclass-methods.md) statements can be used to declare properties of [AMDP methods](abenamdp_methods.md) of global classes or interfaces. After `AMDP OPTIONS`, at least one property must be specified. The following properties can be set:

- `READ ONLY` in order to allow only read accesses to database objects in the method implementation.

- Different options [`client_handling`](abapmethods_amdp_options_client.md) that affect the client handling of the method implementation.

If the addition `AMDP OPTIONS` is used in the declaration of a method, but the method is implemented as a regular ABAP method without the addition [`BY DATABASE PROCEDURE|FUNCTION`](abapmethod_by_db_proc.md), the properties specified by `AMDP OPTIONS` are ignored. However, the following restrictions for AMDP methods apply to the method declaration:

- If there is no `RETURNING` parameter, the restrictions for [AMDP procedure implementations](abenamdp_procedure_methods.md) apply.

- If there is a `RETURNING` parameter, the restrictions described for [AMDP function implementations](abenamdp_function_methods.md) apply.

A prerequisite for using `AMDP OPTIONS` is that the global class or the interface must contain a [tag interface](../../abap-glossary/abentag_interface_glosry.md) [`IF_AMDP_MARKER_...`](abenamdp_classes.md) for [AMDP classes](../../abap-glossary/abenamdp_class_glosry.md). `AMDP OPTIONS` cannot be used in the following cases:

- in local classes

- for the [constructors](../../abap-glossary/abenconstructor_glosry.md) [`constructor`](../abap-declarations/abapmethods_constructor.md) or [`class_constructor`](../abap-declarations/abapclass-methods_constructor.md)

- for [event handlers](../../abap-glossary/abenevent_handler_glosry.md) declared with [`FOR EVENT`](../abap-declarations/abapmethods_event_handler.md)

- for [redefinitions](../../abap-glossary/abenredefinition_glosry.md) declared with [`REDEFINITION`](../abap-declarations/abapmethods_redefinition.md)

- for [AMDP function implementations](../../abap-glossary/abenamdp_function_method_glosry.md) for [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) declared with [`FOR TABLE FUNCTION`](abapclass-methods_for_tabfunc.md)

- for [AMDP function implementations](../../abap-glossary/abenamdp_function_method_glosry.md) for [CDS scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md) declared with [`FOR SCALAR FUNCTION`](abapclass-methods_for_scalfunc.md).

## Addition

`... READ-ONLY`

### Description

If the option `READ-ONLY` is specified, only reads of database tables are allowed in the [implementation](abapmethod_by_db_proc.md) of the [database procedure](../../abap-glossary/abendatabase_procedure_glosry.md) or [database function](../../abap-glossary/abendatabase_function_glosry.md). Only database procedures or database functions of other AMDP methods that are also marked as `READ-ONLY` can be called. This is checked during the syntax check or at runtime.

This property can also be specified using the addition `OPTIONS` in the implementation of an AMDP method with [`METHOD meth BY DATABASE PROCEDURE|FUNCTION`](abapmethod_by_db_proc.md). It applies when specified either in the declaration or in the implementation of the method, or in both places.

In the current ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), the addition `READ-ONLY` must be specified at least once.
