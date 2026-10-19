---
title: "Dynamic Calls"
source_file: abendyn_call_scrty.html
section: "ABAP Programming Language > ABAP Security Notes > Security Risks Caused by Input from Outside"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Dynamic Calls

In dynamic calls, the name of the called unit is specified as the content of a character-like data object. If some or all of this content originates outside of the calling program, there is a risk that units are called unintentionally. The only way of tackling this security risk is to perform a comparison with an include list. The class `CL_ABAP_DYN_PRG` provides the methods `CHECK_WHITELIST_STR` and `CHECK_WHITELIST_TAB` for that purpose.

Potential dynamic calls and hence a potential security risk when handling input can occur in the following cases:

- When an executable program is specified dynamically after `SUBMIT`.

- When a transaction is specified dynamically after `CALL TRANSACTION` and `LEAVE TO TRANSACTION`.

- When classes and methods are specified dynamically in a dynamic method call using [`CALL METHOD`](../abap-calling-and-exiting-program-units/abapcall_method_dynamic.md).

- When a class is specified dynamically in [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md) (a dynamic call of the instance constructor).

- When the function module is specified dynamically in a function module call using [`CALL FUNCTION`](../abap-calling-and-exiting-program-units/abapcall_function.md) (particularly if RFC is used).

- When subroutines and programs are specified dynamically in dynamic subroutine calls using [`PERFORM`](../abap-calling-and-exiting-program-units/abapperform.md).

- When the system function is specified dynamically in the internal statement `CALL`.

## Hint

As well as checking intentional calls, it is also necessary to perform a sufficient [authorization check](abenauthority_scrty.md) on the current user in program calls.
