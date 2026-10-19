---
title: "General Rules for Typing"
source_file: abentyping_check_general.html
section: "ABAP Programming Language > ABAP - Declarations > Typing > Checking Typing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# General Rules for Typing

The general rules for checking the typing apply strictly to:

- The assignment of all data objects to [field symbols](../../abap-glossary/abenfield_symbol_glosry.md)

- The binding of named data objects to [input](../../abap-glossary/abeninput_parameter_glosry.md), [input/output](../../abap-glossary/abeninput_output_parameter_glosry.md), and [output parameters](../../abap-glossary/abenoutput_parameter_glosry.md) for procedures

The general rules for checking the typing are:

- If the assignment is made to generically typed field symbols or formal parameters, the system checks whether the [technical type properties](../../abap-glossary/abentechnical_type_prpt_glosry.md) of the assigned data object are a subset of the generic type. The type properties that are not defined by typing are inherited from the actual parameter.

- In assignments to completely typed field symbols or formal parameters, the technical properties of the data type of the assigned data object must correspond exactly to the typing. In assignments to field symbols or formal parameters typed with [enumerated types](abaptypes_enum.md), the type of the assigned data object must be exactly the same enumerated type as is used for the typing.

- The result of the typing check when actual parameters are passed to formal parameters is independent of the pass by type. In a [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), the check for [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md) is always carried out, even though this can be stricter than necessary in individual cases.

- If reference variables are passed, [upcasts](../../abap-glossary/abenup_cast_glosry.md) are possible but [downcasts](../../abap-glossary/abendown_cast_glosry.md) are not. If actual parameters are passed to input parameters typed as reference variables, an [upcast](../../abap-glossary/abenup_cast_glosry.md) is only possible if there is no change of content within the procedure.

- If memory areas are assigned to field symbols typed as reference variables, the typing of the field symbol and the static type of the memory area must be the same.

- In assignments to generically and completely typed field symbols or formal parameters, only the [technical type properties](../../abap-glossary/abentechnical_type_prpt_glosry.md) are checked. The following properties are not checked:

  - Names of structure components (but the names of [mesh nodes](../../abap-glossary/abenmesh_node_glosry.md) and [mesh associations](../../abap-glossary/abenmesh_association_glosry.md) are checked).

  - Semantic properties of data types defined in the ABAP Dictionary (conversion exits, documentation, and so on)

  - [Initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md) of internal tables

    If generally typed formal parameters or field symbols are accessed dynamically, these properties are inherited from the type of the actual parameter. In static access to generically typed formal parameters or field symbols, these properties are inherited from the typing of the formal parameter.

## Hints

- The constructor operators [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) and [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md) are well suited to convert or cast invalid actual parameters to the type of a formal parameter.

- In the case of generically typed field symbols or formal parameters, and in the case of formal parameters of function modules, the typing is only checked at the time of the assignment, that is, at runtime. In the case of completely typed field symbols and formal parameters of methods, the check is performed by the [syntax check](../../abap-glossary/abensyntax_check_glosry.md).
