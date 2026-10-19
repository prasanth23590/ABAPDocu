---
title: "Offset/Length Specifications for Substring Access"
source_file: abenoffset_length.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions > Notations for Single Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Offset/Length Specifications for Substring Access

In operand positions, it is possible to access substrings of certain data objects by specifying an offset and a length:

## Syntax

``` abap
dobj[+off][(len)]  

<fs>[+off][(len)]  

dref->*[+off][(len)]  
```

## Description

An offset `off` can be appended directly with the character `+` to the identifier `dobj` of a data object, to `<fs>` of a field symbol, or to a dereferenced data reference variable `dref->*`. A length `len` can be appended to the offset specification directly in parentheses `( )` or directly to the identifier. Offsets or lengths can be specified for:

- [Elementary](../../abap-glossary/abenelementary_data_object_glosry.md) [byte-like data objects](../../abap-glossary/abenbyte_like_data_object_glosry.md)

- [Elementary](../../abap-glossary/abenelementary_data_object_glosry.md) [character-like data objects](../../abap-glossary/abencharlike_data_object_glosry.md)

- [Flat structures](../../abap-glossary/abenflat_structure_glosry.md) where one of the following prerequisites must be met:

  - The structure only contains flat character-like components.

  - The first fragment of the [structural fragment view](../../abap-glossary/abenunicode_fragment_view_glosry.md) is flat and character-like, and the substring addressed by specifying the offset and length is located within this fragment.

The segment of the data object is used that has the offset specified in `off` and the length specified in `len` in characters or bytes. No memory area outside the field boundaries can be addressed, except for in the statement [`ASSIGN`](../abap-processing-internal-data/abapassign.md). In the case of an offset specification without a length, the entire substring is addressed from `off` characters; in the case of a length specification without an offset, the first `len` characters are addressed (different rules apply to the statement [`ASSIGN`](../abap-processing-internal-data/abapassign.md)).

The operands `off` and `len` expect data objects of the type `i`, which must contain positive integers, with the following exceptions:

- The length 0 can be specified for [strings](../../abap-glossary/abenstring_glosry.md).

- A negative offset, but never length 0, can be specified if an `<fs>` field symbol is specified in the statement [`ASSIGN`](../abap-processing-internal-data/abapassign_mem_area_static_dobj.md) for `dobj`.

- If `off` is smaller than the length of `dobj`, an asterisk (`*`) can be entered for `len`. The upper limit of `dobj` then determines the upper limit of the memory area.

If the prerequisites are not met or if the substring defined by `off` and `len` is not fully included in the data object, except in the case of [`ASSIGN`](../abap-processing-internal-data/abapassign.md), a syntax error occurs if statically identifiable. Otherwise, an exception of the class `CX_SY_RANGE_OUT_OF_BOUNDS` is raised. If `off` is specified as a numeric literal, it cannot be preceded by a plus/minus sign.

The offset and length specifications are counted in characters for character-like data objects and otherwise in bytes.

A substring specified by an offset or length specification is handled like a data object of the specified length. The data type depends on the data type of the original data object, the field symbol, or the data reference variable, as shown below:

| **Original Data Type** | **Data Type of Substring** |
|------------------------|----------------------------|
| `c`                    | `c`                        |
| `n`                    | `n`                        |
| `d`                    | `n`                        |
| `t`                    | `n`                        |
| `string`               | `string`                   |
| `x`                    | `x`                        |
| `xstring`              | `xstring`                  |
| Structure type         | `c`                        |

In a substring access, if the length of the substring matches the length of the structure to a structure exactly, the substring does not have data type `c` but is handled like the structure itself.

The following restrictions apply:

- At [write positions](../../abap-glossary/abenwrite_position_glosry.md), only flat data objects are allowed, that is, write access to substrings of strings is not possible.

- Access to substrings of strings is also not possible in the following [read positions](../../abap-glossary/abenread_position_glosry.md):

  - Specification of `dobj[+off][(len)]` as a memory area [`mem_area`](../abap-processing-internal-data/abapassign_mem_area_static_dobj.md) of the statement [`ASSIGN`](../abap-processing-internal-data/abapassign.md).

  - Specification of `dobj[+off][(len)]` as an operand of the statement [`GET REFERENCE`](../abap-processing-internal-data/abapget_reference.md) or of the reference operator [`REF`](../abap-processing-internal-data/abenconstructor_expression_ref.md).

  - Specification of `dobj[+off][(len)]` as an actual parameter for input parameters when calling [methods](../abap-calling-and-exiting-program-units/abenmethod_calls.md), [function modules](../abap-calling-and-exiting-program-units/abapcall_function.md).

- Offsets and lengths cannot be specified for literals or text symbols.

- An offset/length specification cannot be attached directly to a table expression [`itab[ ... ]`](../abap-processing-internal-data/abentable_expressions.md), but to a [chaining](../abap-processing-internal-data/abentable_exp_chaining.md) whose last position is a suitable structure component after a structure component selector.

- No offset or length can be specified for an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with an [enumerated type](../../abap-glossary/abenenum_type_glosry.md), regardless of the [base type](../../abap-glossary/abenbase_type_glosry.md).

- In case of dynamically [specified operands](abenoperands_specifying.md) in parentheses, no length specification can be made.

- A dereferenced data reference variable `dref->*` must be typed completely.

- For a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md), no offsets or lengths can be specified as [memory areas](../abap-processing-internal-data/abapassign_mem_area_writable_exp.md) of the statement `ASSIGN` or as operands of the reference operator [`REF`](../abap-processing-internal-data/abenconstructor_expression_ref.md) (table expressions only).

- The following applies when [assigning](../abap-processing-internal-data/abenequals_operator.md) data objects of fixed length with offset/length specifications to an [inline declaration](../../abap-glossary/abeninline_declaration_glosry.md) with the declaration operator [`DATA`](../abap-declarations/abendata_inline.md) or [`FINAL`](../abap-declarations/abenfinal_inline.md):

  - If the offset/length specification is applied to a data object that is directly assigned to the inline declaration, `off` and `len` must be literals or constants. Variables are not allowed.

  - If the offset/length specification is applied to a data object that is the result of chaining that involves a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) or a [table expression](../../abap-glossary/abentable_expression_glosry.md), the data type of the declared data object is the data type of the assigned data object in its full length and the substring is assigned according to the respective [conversion rules](../abap-processing-internal-data/abenconversion_rules.md).

## Hints

- For reads on substrings of character-like data objects, built-in [substring functions](../abap-processing-internal-data/abensubstring_functions.md) that allow searches for substrings and offsets/lengths are also available. The substring functions can also be used to process arguments where offsets and lengths cannot be specified, such as data objects with an [enumerated type](../../abap-glossary/abenenum_type_glosry.md) because there is an implicit conversion to `string`.

- It is recommended that offsets with the value 0 are always specified explicitly, that is, `dobj+0(len)` instead of `dobj(len)` to differentiate substring access in the source code clearly from other language constructs that also contain parentheses, such as dynamic specifications, method calls, or inline declarations.

- Except when used as [memory area](../abap-processing-internal-data/abapassign_mem_area_static_dobj.md) of an [`ASSIGN`](../abap-processing-internal-data/abapassign.md) statement, a specification of `dobj+0(*)`, `dobj+0`, or `dobj(*)` is interpreted as `dobj`. In this case, `dobj` can also be a data object where substring access according to the rules above is not possible. The same is true for `dobj+off(len)`, `dobj+off`, or`dobj(len)` if `off` and `len` are literals or constants whose value is *0* or the same as the length of `dobj`, respectively.

- The above restriction regarding offset/length specifications for results of chainings involving table or constructor expressions is not valid for types that are inferred at runtime, e.g. when passing to generic parameters of procedures. Then the data type of the substring is used.

- No substring access `cnt(len)`, `sum(len)` can be performed on data objects named `cnt` and `sum` unless an offset is specified explicitly.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Offset/length specifications after a [`FIND`](../abap-processing-internal-data/abapfind.md) statement.

``` abap
FINAL(str) = 'aaaXXXbbb'. 
FIND PCRE `\p{Lu}+` IN str MATCH OFFSET FINAL(off) 
                           MATCH LENGTH FINAL(len). 
IF sy-subrc = 0. 
   final(offlen) = off + len. 
   cl_demo_output=>new( 
    )->write( str(off) 
    )->write( str+off(len) 
    )->write( str+offlen 
    )->display( ). 
ENDIF.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following structure has character-like and non-character-like components:

``` abap
DATA: 
  BEGIN OF struc, 
    a TYPE c LENGTH 3,    "Length 3 characters 
    b TYPE n LENGTH 4,    "Length 4 characters 
    c TYPE d,             "Length 8 characters 
    d TYPE t,             "Length 6 characters 
    e TYPE decfloat16,    "Length 8 bytes 
    f TYPE c LENGTH 28,   "Length 28 characters 
    g TYPE x LENGTH 2,    "Length 2 bytes 
  END OF struc.
```

The [fragment view](../../abap-glossary/abenunicode_fragment_view_glosry.md) splits the structure into five areas, F1 - F5.

``` abap
 [ aaa | bbbb | cccccccc | ddd | AAA | eeee | fffffffffffff | gg ] 
[            F1               |  F2 |  F3  |       F4      | F5 ]
```

Offset and length accesses are only possible on the character-like initial fragment F1 only, for example `struc(21)` or `struc+7(14)`. An access such as `struc+57(2)` is not allowed.

## Executable Example

[Offset/Length Specifications](abendata_process_fields_abexa.md)
