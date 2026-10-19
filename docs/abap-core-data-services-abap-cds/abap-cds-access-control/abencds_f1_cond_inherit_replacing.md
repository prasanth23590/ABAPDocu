---
title: "CDS DCL - DEFINE ROLE, replacing"
source_file: abencds_f1_cond_inherit_replacing.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition > CDS DCL - DEFINE ROLE, inherit_condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, replacing

## Syntax

``` abap
... REPLACING { replacement_step [, replacement_step, ...] }  
```

[`replacement_step`](abencds_f1_cond_inherit_rpl_step.md) · [`replacement_step`](abencds_f1_cond_inherit_rpl_step.md)

## Description

This addition modifies inherited access conditions from source entity `cds_entity` before they are applied to the protected entity of the own access rule.

It contains a sequence of replacement steps [`replacement_step`](abencds_f1_cond_inherit_rpl_step.md) which are executed in the order as appearing in the statement from left to right.

The first step operates on the inherited conditions and provides its result to the next step as input.

The result of the last step acts as output of the inheritance condition.
