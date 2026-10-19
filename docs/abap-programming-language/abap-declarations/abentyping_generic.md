---
title: "typing Addition, generic_type"
source_file: abentyping_generic.html
section: "ABAP Programming Language > ABAP - Declarations > Typing > typing Addition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# typing Addition, generic_type

## Syntax

``` abap
... { TYPE generic_type } 
  | { LIKE <generic_fs>|generic_para } ...  
```

[`generic_type`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md)

## Description

To type a formal parameter or a field symbol generically, the following is possible:

- specify any generic ABAP type [`generic_type`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) (except `object`) after `TYPE`.

- specify a field symbol visible at this position (`<generic_fs>`) or a formal parameter (`generic_para`) with generic typing, after `LIKE`. The typing defined in the declaration of the field symbol/parameter is applied. In method parameters, all generic typing is possible. No complete generic typing is possible in parameters of field symbols.

When an actual parameter or memory area is assigned to a generically typed formal parameter or field symbol, the system [checks](abentyping_check.md) whether the specified data type is a subset of the generic type. The type of the formal parameter or field symbol is derived from the type of the actual parameter.

The formal parameter or field symbol can be used at any operand position that is not excluded by this typing. The following exceptions apply:

- [Operand positions](../../abap-glossary/abenoperand_position_glosry.md) that expect internal tables. Here, only formal parameters or field symbols typed as internal table types of the corresponding table category are allowed.

- [Read positions](../../abap-glossary/abenread_position_glosry.md) in which a statically recognizable [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) is expected, such as the source field of an assignment to an [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md), or an operand in a comparison with an enumerated object. Only operands with the same [enumerated type](../../abap-glossary/abenenum_type_glosry.md) are allowed here. In [write positions](../../abap-glossary/abenwrite_position_glosry.md), however, generic formal parameters or field symbols are allowed for enumerated types. If the operand type is not known statically, the check is also only made at runtime in read positions.

The type properties specified by the typing are used in static access to a generically typed formal parameter or field symbol. In dynamic access, the properties of the assigned actual parameter or memory area assigned apply.

If no actual parameter is specified for a generically typed optional formal parameter of a method or a function module when calling the procedure and no replacement parameter is defined in the procedure, the formal parameter is typed with a [standard type](../../abap-glossary/abenstandard_type_glosry.md) in accordance with the following rules:

- `any` and `data` are converted to the type `c` with length 4.

- `c`, `clike`, `csequence`, and `simple` are converted to the type `c` with length 1.

- `n` is converted to the type `n` with length 1.

- `numeric` and `p` are converted to the type `p` with length 8 without decimal places.

- `x` and `xsequence` are converted to the type `x` with length 1.

- `ANY TABLE` and `INDEX TABLE` are converted to `STANDARD TABLE`.

- For `ANY TABLE`, `INDEX TABLE`, `[STANDARD] TABLE` `SORTED TABLE`, and `HASHED TABLE`, the line type is set to `c` with length 1.

- For generic table types without specification of a primary table key, the standard key is added for standard tables and the entire table line, except for any table-like parts, is added as the key specification for sorted tables and hashed tables.

- For generic table types, for which the primary table key is specified but uniqueness is not specified, the standard key is set to non-unique for standard tables and sorted tables, and to unique for hashed tables.

- This generic property is ignored for table types that are generic with respect to the secondary table key. This applies even if the generic property was defined explicitly with the addition [`WITH FURTHER SECONDARY KEYS`](abaptypes_keydef.md).

If a replacement parameter is specified, its type properties are applied.

## Hints

- In typing formal parameters with the generic type [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md), it should be noted that no [numeric functions](../../abap-glossary/abenmathematical_funktion_glosry.md), no [description functions](../../abap-glossary/abendescription_function_glosry.md), and no [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md) can be passed to these parameters. This restriction can be bypassed by applying the [conversion operator](../../abap-glossary/abenconversion_operator_glosry.md) [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) to the actual parameter. This restriction does not apply to the generic type `any`.

- [`ANY STRUCTURE`](abapany_structure.md) is used for fully generic structures. User-defined partially generic structured types can be created by including the `containing` addition.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, two generically typed field symbols are used in [`READ TABLE`](../abap-processing-internal-data/abapread_table.md) statement. To avoid syntax errors, `<index_table>` must be typed as an index table. However, the system does not check until runtime for `<any_object>` whether the data object assigned to it matches the line type of the table.

``` abap
FIELD-SYMBOLS: <any_object>   TYPE any, 
               <index_table>  TYPE index table. 
 
... 
 
READ TABLE <index_table> INDEX 1 
                         INTO <any_object>.
```
