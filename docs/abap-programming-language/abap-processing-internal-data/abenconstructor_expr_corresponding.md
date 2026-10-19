---
title: "CORRESPONDING, Component Operator"
source_file: abenconstructor_expr_corresponding.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CORRESPONDING, Component Operator

## Syntax Forms

**[Basic Form](abencorresponding_constr_arg_type.md)**

``` abap
1. ... { CORRESPONDING {dtype|#}( [EXACT] [DEEP] 
                                  struct|{itab [duplicates]} ) } 
    | { CORRESPONDING {dtype|#}( [DEEP] 
                                 [[APPENDING] BASE ( base )] 
                                 struct|{itab [duplicates]} ) } 
    | { CORRESPONDING {dtype|#}( [[APPENDING] BASE ( base )] 
                                 struct|{itab [duplicates]} 
                                 mapping ) } ...
```

**[Lookup Table](abencorresponding_constr_using.md)**

``` abap
2. ... CORRESPONDING dtype( itab FROM lookup_tab 
                                USING [KEY key_name] s1 = t1 s2 = t2 ... 
                               [mapping] ) ...
```

**[RAP-Specific Variants for Type Mapping](../../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_corresponding.md)**

``` abap
3. ... { CORRESPONDING {dtype|#}( in_d_type MAPPING FROM ENTITY ) } 
    | { CORRESPONDING {dtype|#}( ntype MAPPING TO ENTITY ) } 
    | { CORRESPONDING {dtype|#}( in_d_type USING CONTROL ) } 
    | { CORRESPONDING {dtype|#}( in_d_type MAPPING FROM ENTITY USING CONTROL ) } 
    | { CORRESPONDING {dtype|#}( ntype CHANGING CONTROL ) } ...
```

[`duplicates`](abencorresponding_constr_dupl.md) · [`duplicates`](abencorresponding_constr_dupl.md) · [`duplicates`](abencorresponding_constr_dupl.md) · [`mapping`](abencorresponding_constr_mapping.md) · [`mapping`](abencorresponding_constr_mapping.md)

## Description

A [constructor expression](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) with the component operator `CORRESPONDING` creates a result of a data type specified using `dtype`.

- In the [basic component](abencorresponding_constr_arg_type.md), the components of a structured or tabular results are constructed from the components of a structured or tabular parameter `struc` or `itab`.

- In the [variant with lookup table](abencorresponding_constr_using.md), the components of an internal table `itab` and a lookup table `lookup_tab` are combined to form a tabular result.

- The [RAP-specific variants](../../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_corresponding.md) are used for creating structures or internal tables with type mapping in ABAP in the context of [RAP](../../abap-glossary/abenrap_glosry.md). RAP requires [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) for the communication of [RAP BO providers](../../abap-glossary/abenrap_bo_provider_glosry.md) and [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md). When including non-BDEF-derived types (`ntype`), the variants are responsible for matching them to the input (`in_d_type`) and output BDEF derived types.

The following can be specified for `dtype`:

- A [structured type](../../abap-glossary/abenstructured_type_glosry.md) or a [table type](../../abap-glossary/abentable_type_glosry.md).

- The `#` character as a symbol for the [operand type](../../abap-glossary/abenoperand_type_glosry.md). This specification is only possible if the data type required in an operand position is unique and completely identifiable at compile time. The operand type must be a structure type or a table type. When a constructor expression is assigned to a field symbol or a formal parameter with a generic table type, the operand type can only be determined at runtime.

The operator creates structures or internal tables with the specified data type. The components or columns of the result are filled using assignments of components of the parameters specified in the parentheses. The assignments are made using identical names or mapping relationships in a [mapping rule](abencorresponding_constr_mapping.md).

## Executable Examples

[Assigning Components: Examples](abencorresponding_abexas.md)
