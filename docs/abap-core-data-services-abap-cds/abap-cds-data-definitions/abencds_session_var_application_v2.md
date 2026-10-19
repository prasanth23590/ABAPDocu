---
title: "CDS DDL - CDS View Entity, Application Session Variables"
source_file: abencds_session_var_application_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Elementary CDS Operands > CDS DDL - CDS View Entity, session_variable"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Application Session Variables

## Syntax

``` abap
... $session.vname ...  
```

## Description

Specifies an application [session variable](../../abap-glossary/abensession_variable_glosry.md) `vname` in an operand position in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The variable must be prefixed by `$session.`.

Application session variables are required for specific applications and they can be set by dedicated system programs using a special system class. The following application session variables exist:

| **vname**        | **Value when accessed**                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------|
| `bs_instance_id` | Instance ID of the current business service instance. The returned value has the data type `SSTRING`. |
| `bs_zone_id`     | Zone ID of the current business service instance. The returned value has the data type `SSTRING`.     |

## Prerequisite

A CDS view entity that accesses an application session variable must be usable as replacement object. That implies that the respective CDS view entity must not have any [input parameters](abencds_parameter_v2.md).

## Hints

- From a technical perspective, session variables indicate global variables of the current database. Application session variables are set to their value by dedicated system programs using a special system class. Like [ABAP system fields](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md), they are modifiable from an ABAP program. However, they should not be changed in application programs. They should only be used for reads. Otherwise, important information for further program execution may be lost.

- The annotation [`environment.systemField`](abencds_f1_parameter_annotations.md) is relevant for built-in session variables, but not for application session variables.

- In existing CDS view entities without corresponding input parameters, session variables can be passed to the input parameters of CDS view entities or CDS table functions used there.

- Application session variables are supported only in CDS view entities. However, it is possible to build a CDS DDIC-based view (obsolete) on top of a CDS view entity with application session variables. The information is passed on to the CDS DDIC-based view (obsolete) in this case.

## Restrictions

- CDS view entities with application session variables cannot be used in [AMDP](../../abap-glossary/abenamdp_glosry.md), since AMDP does not support application session variables.

- The [ADT](../../abap-glossary/abenadt_glosry.md) function Data Preview does not work for CDS view entities with application session variables.
