---
title: "DATA"
source_file: abapdata.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA

## Syntax Forms

**[Using Built-In Types](abapdata_simple.md)**

``` abap
1. DATA { {var[(len)] TYPE abap_type [DECIMALS dec]} 
       | {var TYPE abap_type [LENGTH len] [DECIMALS dec]} } 
       [VALUE val|{IS INITIAL}] 
       [READ-ONLY].
```

**[Reference to Existing Types](abapdata_referring.md)**

``` abap
2. DATA var { {TYPE [LINE OF] type} 
           | {LIKE [LINE OF] dobj} } 
           [VALUE val|{IS INITIAL}] 
           [READ-ONLY].
```

**[Enumerated Variables](abapdata_enum.md)**

``` abap
3. DATA enum_var { {TYPE enum_type} 
                | {LIKE enum_dobj} } 
                [VALUE val|{IS INITIAL}] 
                [READ-ONLY].
```

**[Reference Variables](abapdata_references.md)**

``` abap
4. DATA ref { {TYPE REF TO type} 
           | {LIKE REF TO dobj} } 
           [VALUE IS INITIAL] 
           [READ-ONLY].
```

**[Structures](abapdata_struc.md)**

``` abap
5. DATA BEGIN OF struc [READ-ONLY]. 
     ... 
     DATA comp ... 
     INCLUDE {TYPE|STRUCTURE} ... 
     ... 
  DATA END OF struc.
```

**[Internal Tables](abapdata_itab.md)**

``` abap
6. DATA itab { {TYPE tabkind OF [REF TO] type} 
            | {LIKE tabkind OF dobj} } 
            [tabkeys] [INITIAL SIZE n] 
            [WITH HEADER LINE] 
            [VALUE IS INITIAL] 
            [READ-ONLY].
```

**[Ranges Table](abapdata_ranges.md)**

``` abap
7. DATA range_tab {TYPE RANGE OF type}|{LIKE RANGE OF dobj} 
                 [INITIAL SIZE n] 
                 [WITH HEADER LINE] 
                 [VALUE IS INITIAL] 
                 [READ-ONLY].
```

**[Static Boxed Components](abapdata_boxed.md)**

``` abap
9. DATA struc TYPE struc_type BOXED.
```

**[BDEF Derived Types](../../abap-rap-business-objects/abap-for-rap-business-objects/abenrpm_derived_types.md)**

``` abap
10. DATA var { {TYPE TABLE FOR} 
            | {TYPE STRUCTURE FOR} 
            | {TYPE REQUEST FOR} 
            | {TYPE RESPONSE FOR} } ...
```

[`tabkind`](abapdata_itab.md) · [`tabkind`](abapdata_itab.md) · [`tabkeys`](abapdata_keydef.md)

## Description

The statement `DATA` declares a [variable](../../abap-glossary/abenvariable_glosry.md) of any data type. The declared data object is visible within the current context as of this position. Within the declaration part of a class or an interface, `DATA` declares an instance attribute whose validity is bound to an instance of a class.

This statement has different syntax forms that enable elementary data types, reference types, structured types, and table types to be defined. With the exception of two additions ([`VALUE`](abapdata_options.md) and [`READ-ONLY`](abapdata_options.md)), these are the same syntax forms as in the statement [`TYPES`](abaptypes.md). In this way, a new data type can be defined when declaring a data object. The main difference to the statement `TYPES` is that a data type defined using `DATA`, which is not derived from an existing type, is available only as a property of the declared data object and not on its own. This kind of data type is bound to its data object.

For the definition of a structure `struc`, any data declarations are enclosed in two `DATA` statements with the additions `BEGIN OF` and `END OF`. This declares a structure `struc` that contains the enclosed data objects `comp` as `struc-comp` components. Structure definitions can be nested.

Without the addition [`VALUE`](abapdata_options.md), data objects are filled with their type-specific [initial values](../../abap-glossary/abeninitial_value_glosry.md), which are always based on the initial values of the elementary [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) ABAP types or on initial reference values.

The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the names `var`, `ref`, `struc`, `comp`, `itab`, and `range_tab`.

## Hints

- Data objects that are declared in a program, but cannot be accessed there statically, produce a warning from the enhanced program check.

- An [inline declaration](../../abap-glossary/abeninline_declaration_glosry.md) of variables is possible using the declaration operator [`DATA`](abendata_inline.md) and [`FINAL`](abenfinal_inline.md). The latter declares an [Immutable variable](../../abap-glossary/abenimmutable_variable_glosry.md) that can improve the robustness of programs.
