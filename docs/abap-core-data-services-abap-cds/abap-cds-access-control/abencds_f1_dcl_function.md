---
title: "CDS DCL - DEFINE ROLE, dcl_function"
source_file: abencds_f1_dcl_function.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, dcl_function

## Syntax

``` abap
... { SACF_CHECK_IN_USE( NAME => scenario_name [, OBJECT => auth_object ] ) 
          IS [NOT] INITIAL } 
  | { OPTIONAL_ELEMENT_EXISTS( NAME => element ) 
          IS [NOT] INITIAL } 
  | { SWITCH_RUNTIME_STATE( NAME => switch_name ) 
          IS [NOT] INITIAL } 
  | { TOGGLE_RUNTIME_STATE( NAME => toggle_name ) 
          IS [NOT] INITIAL } 
  | { CONTEXT_NODE_EXISTS(...) 
          IS [NOT] INITIAL } ...  
```

### Variant

[1. `... SACF_CHECK_IN_USE ...`](abencds_f1_dcl_function.md#variant-1)

[2. `... OPTIONAL_ELEMENT_EXISTS ...`](abencds_f1_dcl_function.md#variant-2)

[3. `... SWITCH_RUNTIME_STATE ...`](abencds_f1_dcl_function.md#variant-3)

[4. `... TOGGLE_RUNTIME_STATE ...`](abencds_f1_dcl_function.md#variant-4)

[5. `... CONTEXT_NODE_EXISTS ...`](abencds_f1_dcl_function.md#variant-5)

## Overview

### Description

DCL functions are evaluated in the ABAP application server before the [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) are sent to the database.

They evaluate to either logical `TRUE` or logical `FALSE` and then may result in reduction of the logical expression tree of the access control.

### Hint

The effect of the DCL function applies at runtime only. Syntactical correctness of the access control must be always given.

For example, in a condition like `dcl_function` `AND element IS NULL` a syntax error will appear when element does not exist, even when the `dcl_function` at the time of compilation behaves like a logical `FALSE`.

## Variant 1

`... SACF_CHECK_IN_USE ...`

### Description

Using this DCL function, the state of switchable authorization checks can be queried and used in an access control to enable or disable condition blocks.

The function behaves like the ABAP method `CL_SACF=>SACF_CHECK_IN_USE` with its parameters `ID_NAME` and `ID_OBJECT`. The returned value can only be tested by the `IS [NOT] INITIAL` operator:

- `SACF_CHECK_IN_USE( ... ) IS INITIAL` is `TRUE` when the given scenario (eventually specifically for the given authorization object) is not active, that is, an authorization check switched by this scenario behaves like full authorization.

- `SACF_CHECK_IN_USE( ...) IS NOT INITIAL` is `TRUE` when the given scenario (eventually specifically for the given authorization object) is active, that is, an authorization check switched by this scenario is executed based on the users authorizations.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This access control realizes a migration from an old authorization object `OLD_AUTH` to a new authorization object `NEW_AUTH` based on the SACF scenario `NEW_AUTH_SWITCH`. As soon as this scenario is activated, the old authorization object is no longer considered.

``` abap
GRANT SELECT ON cds_entity 
  WHERE 
    SACF_CHECK_IN_USE (NAME => NEW_AUTH_SWITCH ) IS INITIAL 
      AND 
    ( element ) = ASPECT PFCG_AUTH( OLD_AUTH, F ) 
  OR 
    SACF_CHECK_IN_USE( NAME => NEW_AUTH_SWITCH ) IS NOT INITIAL 
      AND 
    ( element ) = ASPECT PFCG_AUTH( NEW_AUTH, F );
```

### Hint

When you only need to introduce new authorization objects without the need to instantly disable the evaluation of a predecessor, the regular syntax addition to PFCG conditions is preferred:

`( element ) = ASPECT PFCG_AUTH( NEW_AUTH IN SCENARIO NEW_AUTH_SWITCH, F)`

## Variant 2

`... OPTIONAL_ELEMENT_EXISTS ...`

### Description

With this DCL function, existence of the given CDS element in the protected entity can be queried at runtime. Based on the outcome of the check, larger condition blocks in the access control can then be enabled or disabled.

It is an extension to the concept of optional elements ([`WITH OPTIONAL ELEMENTS`](abencds_dcl_role_cond_rule.md)) and allows application not only for newly introduced elements, but also for replacement scenarios in which an element is semantically replaced by another element.

### Hints

- The element which is queried in the function must be declared as optional element.

  By using the function with an element, you explicitly make clear that the element may be missing, therefore declaring it optional is mandatory to avoid syntactically wrong access controls when the element is missing.

- The element which is queried in the function must be used at least once outside in the access control in a condition statement.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This access control formerly realized access control using an association.

To increase the selection performance, this association should be replaced by a replica of the used element in the protected entity itself (`itemState`).

As this element is not instantly available in CDS entities which inherit their access conditions from this entity, the new element is introduced as optional element (the default value `FALSE` is secure by default, but in the current case not used at runtime due to the DCL function), and in this case, the former access control should apply.

As soon as the new element becomes available, it should be used instead and the former one no longer be used at all (to avoid performance degradation due to join evaluation).

``` abap
GRANT SELECT ON cds_entity 
   WITH OPTIONAL ELEMENTS (itemState DEFAULT FALSE ) 
     WHERE 
       OPTIONAL_ELEMENT_EXISTS( NAME => itemState ) IS INITIAL 
         AND 
          toItem.state = 'A' 
     OR 
       OPTIONAL_ELEMENT_EXISTS( NAME => itemState ) IS NOT INITIAL 
         AND 
          itemState = 'A';
```

## Variant 3

`... SWITCH_RUNTIME_STATE ...`

### Description

This function retrieves the runtime state of a switch in the [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md) (SFW):

- If the switch state is *On*, the result of the function is considered non-initial and testing the function with `IS NOT INITIAL` returns `TRUE`, while testing with `IS INITIAL` returns `FALSE`.

- Otherwise, the result of the function is initial and the test result is reversed under the two operators mentioned above.

### Hints

- For switches in the Switch Framework of type *Feature Toggle*, use the dedicated DCL function `TOGGLE_RUNTIME_STATE`.

- This function is only evaluated at runtime. See the documentation for the CDS role addition [`SWITCHABLE`](abencds_f1_define_role.md) for another type of switch dependency in CDS access control that affects the access control generation process.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

If the switch with the name `SWITCH_NAME` is active (*On*), the access condition tests the value of the field `STATE1`, otherwise it tests the value of the field `STATE2`.

``` abap
GRANT SELECT ON cds_entity 
  WHERE 
    IF 
      ( SWITCH_RUNTIME_STATE( NAME => SWITCH_NAME ) IS NOT INITIAL ) 
    THEN 
      { STATE1 = 'A' } 
    ELSE 
      { STATE2 = 'A' };
```

## Variant 4

`... TOGGLE_RUNTIME_STATE ...`

### Description

This function behaves like `SWITCH_RUNTIME_STATE` at runtime. The difference between the two functions is the type of the switch whose name is specified in the `NAME` parameter. While `TOGGLE_RUNTIME_STATE` can only be used for switches of type *Feature Toggle*, the function `SWITCH_RUNTIME_STATE` can only be used for switches of other types.

The rationale for using two different functions is the best practice that feature toggles should exist only temporarily until the feature they guard becomes a core feature, while switches of other types are long-lived.

The dedicated function allows the reader of the access control to immediately recognize that the content is ephemeral.

## Variant 5

`... CONTENT_NODE_EXISTS ...`

### Description

This function is reserved for use by SAP.
