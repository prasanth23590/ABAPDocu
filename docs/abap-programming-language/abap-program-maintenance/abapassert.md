---
title: "ASSERT"
source_file: abapassert.html
section: "ABAP Programming Language > ABAP - Program Maintenance > Testing and Checking Programs > Checkpoints"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSERT

## Syntax

``` abap
ASSERT [ [ID group [SUBKEY sub]]   
         [FIELDS val1 val2 ...]   
         CONDITION ] log_exp.
    
```

[`log_exp`](../abap-program-flow-logic/abenlogexp.md)

### Addition

[1. `... ID group`](abapassert.md#addition-1)

[2. `... SUBKEY sub`](abapassert.md#addition-2)

[3. `... FIELDS val1 val2 ...`](abapassert.md#addition-3)

[4. `... CONDITION`](abapassert.md#addition-4)

## Overview

### Description

This statement defines an [assertion](../../abap-glossary/abenassertion_glosry.md). Any [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) can be specified for [`log_exp`](../abap-program-flow-logic/abenlogexp.md). An assertion is either active or inactive.

- Without the addition `ID`, the assertion is always active.

- When using the addition `ID`, the activation and the behavior of the statement are controlled from outside the program by a [checkpoint group](../../abap-glossary/abencheckpoint_group_glosry.md).

When the program reaches an active assertion, the logical expression is evaluated, and the program execution continues with the statement after `ASSERT` only if the result of `log_exp` is true. After an inactive assertion, the logical expression `log_exp` is not evaluated and the program execution continues with the statement following `ASSERT`.

- If the result of `log_exp` is false, an uncatchable exception is raised for an assertion that is always active, if the addition `ID` is not specified, and the program terminates with the runtime error `ASSERTION_FAILED`.

- For an assertion activated externally, if the addition `ID` is specified, the operation mode specified for a [checkpoint group](../../abap-glossary/abencheckpoint_group_glosry.md) or the current [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md) determines how the program execution is continued.

### Hints

- If [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) are specified as operands of a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) in the logical expression `log_exp`, they must not have any side effects. This must especially apply to assertions that can be activated externally, since the program behavior otherwise depends on the activation.

- Assertions help verify certain assumptions about the state of a program in a particular location and ensure that these assumptions are met. Compared with the implementation with a conditional expression with [`THROW SHORTDUMP`](../abap-program-flow-logic/abenconditional_expression_result.md), the `ASSERT` statement is shorter, its meaning is immediately recognizable, and it can be activated externally.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The statement `ASSERT` ensures a certain condition that is necessary for its continuation. If this is not the case, the program terminates with the runtime error `ASSERTION_FAILED`.

``` abap
DATA gui_flag TYPE abap_boolean. 
CALL FUNCTION 'GUI_IS_AVAILABLE' 
  IMPORTING 
    return = gui_flag. 
 
ASSERT gui_flag = abap_true.
```

## Addition 1

`... ID group`

### Description

The addition `ID` defines that the activation of the statement `ASSERT` is controlled from outside of the program using the [checkpoint group](../../abap-glossary/abencheckpoint_group_glosry.md) `group`. If the addition `ID` is specified, the addition `CONDITION` must be specified before the `log_exp` logical expression.

The name of the checkpoint group must be specified directly, and the group must exist in the [repository](../../abap-glossary/abenrepository_glosry.md).

All checkpoint statements linked with the checkpoint group (`ASSERT`, `BREAK-POINT`, `LOG-POINT`) can be activated or deactivated using the checkpoint group. An activation setting consists of three components:

- Validity area - Checkpoints specified in the checkpoint group or [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md)

- Context - User and/or AS instance specified

- Operation mode - System behavior of the different checkpoint types (assertions, breakpoints, or logpoints)

  The following settings are possible:

  - *Inactive*

    The assertion is inactive.

  - *Log*

    Creates an entry in a special log and continues program execution with the statement following `ASSERT`. The log entries are collected in the shared memory and are written to a DDIC database table by a periodical background job. By default, any existing entries of the same `ASSERT` statement are overwritten. Each time an entry is written, a counter for the entry is increased.

  - *stop / log* or *stop / cancel*

    Branch to the ABAP Debugger.

  - *Cancel*

    Raising of an uncatchable exception and terminating the program with the runtime error `ASSERTION_FAILED`.

If the checkpoint statements are activated using the compilation unit, then the association with a specific checkpoint group no longer has any meaning.

### Hints

- If the checkpoint statements are activated using the compilation unit, a checkpoint group must still be specified, since a checkpoint statement without the addition `ID` is always active.

- The validity period of activation settings with active operation modes is limited.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the previous example, but here the behavior of the statement `ASSERT` is controlled using the checkpoint group `DEMO_CHECKPOINT_GROUP`.

``` abap
DATA gui_flag TYPE abap_boolean. 
CALL FUNCTION 'GUI_IS_AVAILABLE' 
  IMPORTING 
    return = gui_flag. 
 
ASSERT ID demo_checkpoint_group 
          CONDITION gui_flag = abap_true.
```

## Addition 2

`... SUBKEY sub`

### Description

The addition `SUBKEY` only has an effect if the statement `ASSERT` writes entries to a log. If `SUBKEY` is specified, the content of `sub` is stored in the log as a subkey. Any existing log entries of the same `ASSERT` statement are overwritten only if the subkey has the same content. If `SUBKEY` is not specified, the subkey is initial.

`sub` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md) of which the first 200 characters are evaluated. An expression or function specified here is evaluated only if the assertion is active and the logical expression is false.

## Addition 3

`... FIELDS val1 val2 ...`

### Description

After the addition `FIELDS`, a list `val1 val2 ...` of any values, except for reference variables, can be specified. If the statement `ASSERT` writes entries to a log, the specified values `val1 val2 ...` are also included in the log. If an uncatchable exception is raised, the content of the first eight specified data objects is displayed in the associated [short dump](../../abap-glossary/abenshort_dump_glosry.md). The addition `FIELDS` is ignored when a branch to the ABAP Debugger is performed.

`val1 val2 ...` are [functional operand positions](../../abap-glossary/abenfunctional_position_glosry.md) in which data objects or functional methods can be specified. The methods are executed only if the assertion is active and the logical expression is false.

If the addition `FIELDS` is specified, the addition `CONDITION` must be specified before the `log_exp` logical expression.

### Hints

- If functional methods are specified after `SUBKEY` and `FIELDS`, code for formatting log entries can be executed only after an assertion is violated.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the previous example, but here logs are provided with additional information.

``` abap
DATA gui_flag TYPE abap_boolean. 
CALL FUNCTION 'GUI_IS_AVAILABLE' 
  IMPORTING 
    return = gui_flag. 
 
ASSERT ID demo_checkpoint_group 
          SUBKEY sy-uname 
          FIELDS 'Missing GUI' 
          CONDITION gui_flag = abap_true.
```

## Addition 4

`... CONDITION`

### Description

The addition `CONDITION` introduces the logical expression. It must be specified in front of `log_exp` if one of the other additions is specified; otherwise, it can be omitted.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the first example above, but here the optional `CONDITION` addition is specified.

``` abap
DATA gui_flag TYPE abap_boolean. 
CALL FUNCTION 'GUI_IS_AVAILABLE' 
  IMPORTING 
    return = gui_flag. 
 
ASSERT CONDITION gui_flag = abap_true.
```
