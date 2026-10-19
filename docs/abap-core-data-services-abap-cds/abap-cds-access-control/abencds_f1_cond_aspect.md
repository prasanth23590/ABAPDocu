---
title: "CDS DCL - DEFINE ROLE, aspect_condition"
source_file: abencds_f1_cond_aspect.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, aspect_condition

## Syntax

``` abap
... (element1 [, element2, ...] ) = ASPECT aspect 
      [FILTER BY ( aspect filter )] ...  
```

### Addition

[`... FILTER BY`](abencds_f1_cond_aspect.md#addition)

## Overview

### Description

Aspect condition as part of an [access condition](../../abap-glossary/abenaccess_condition_glosry.md) [`cds_cond`](abencds_dcl_role_cond_expr.md) in an [access rule](abencds_dcl_role_rules.md) of the statement [`DEFINE ROLE`](abencds_f1_define_role.md) in [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). An aspect condition specifies the user-defined aspect `aspect` defined in an aspect definition in the right side introduced by `ASPECT`.

In parentheses, the left side contains the ordered list of entity elements that match the output fields of the user-defined aspect.

[Left-side host expressions](abencds_dcl_cond_left_side.md) are not supported in this language element. The only comparison operator allowed is the equality operator `=`.

When any of the left side elements of an aspect condition is declared as optional with default `FALSE` and missing at runtime, the entire aspect is handled as logically false.

Missing optional elements with default `TRUE` are removed from the link condition between the aspect entity and the protected entity. This process may apply to all left side elements, in which case the aspect condition reduces to a mere existence check of any row in the aspect entity for the current user.

## Addition

`...FILTER BY`

### Description

When the aspect definition declares at least one filter element (see `DEFINE ASPECT`), you can use this addition to specify an additional selection condition for the rows of the aspect entity, before the result set is used to filter the rows of the protected entity.

The condition can use the declared aspect filters, literals, session variables and parameters of the protected entity, but you cannot refer to elements of the protected entity.

The aspect filter supports logical expressions and brackets.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

You have an aspect entity with the following content, where `NULL` denotes a [null value](../../abap-glossary/abennull_value_glosry.md):

| **`USERNAME`** | **`COSTCENTER`** | **`STATE`** |
|----------------|------------------|-------------|
| *A*            | `1`              | `U`         |
| *A*            | `2`              | `V`         |
| *A*            | `3`              | `NULL`      |
| `B`            | `1`              | `V`         |
| `B`            | `2`              | `U`         |

In the aspect definition, you specify `USERNAME` as the user element, `COSTCENTER` as the output element, and `STATE` as the filter element:

``` abap
DEFINE ASPECT DEMO_ASPECT AS SELECT FROM ... 
  WITH USER ELEMENT USERNAME 
  WITH FILTER ELEMENTS ( STATE ) 
  { COSTCENTER }
```

In an access role you filter the protected entity based on column`CostCenter` using the user-defined aspect.

GRANT SELECT ON ... WHERE (CostCenter) = ASPECT DEMO_ASPECT;

With this condition, for user A the cost centers 1, 2 and 3 will be returned.

When only the cost centers with state `U` or `NULL` are respected, you can filter the aspect rows:

``` abap
GRANT SELECT ON ... WHERE (CostCenter) = ASPECT DEMO_ASPECT FILER BY( STATE = 'U' OR STATE IS NULL );
```

For user A, this condition will return cost center 1 and 3, while for user B, cost center 2 would be returned.
