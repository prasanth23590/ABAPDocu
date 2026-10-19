---
title: "... meth1( ... )->meth2( ... )->..., Method Chaining"
source_file: abapcall_method_static_chain.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Static Method Calls"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ... meth1( ... )-\>meth2( ... )-\>..., Method Chaining

## Syntax

``` abap
... { meth( ... )->meth1( ... )->meth2( ... )->...->methn( ... ) } 
  | { meth( ... )->meth1( ... )->meth2( ... )->...->attr        } ...  
```

[`meth`](abapcall_method_meth_ident_stat.md) · [`meth1`](abapcall_method_meth_ident_stat.md) · [`methn`](abapcall_method_meth_ident_stat.md) · [`meth`](abapcall_method_meth_ident_stat.md)

### Alternative

[1. `meth( ... )->meth1( ... )->meth2( ... )->...->methn( ... )`](abapcall_method_static_chain.md#alternative-1)

[2. `meth( ... )->meth1( ... )->meth2( ... )->...->attr`](abapcall_method_static_chain.md#alternative-2)

## Overview

### Description

Chaining of static method calls to a chained method call or a chained attribute access. [`meth`](abapcall_method_meth_ident_stat.md), [`meth1`](abapcall_method_meth_ident_stat.md), [`meth2`](abapcall_method_meth_ident_stat.md), ..., expect [functional methods](abapcall_method_functional.md) whose return values are reference variables that point to objects with the next method in question. All methods that follow `meth` must be called using the object component selector.

The parameters are passed to the functional methods `meth`, `meth1`, `meth2`, ... using the syntax valid for [functional method calls](abapcall_method_functional.md).

### System Fields

Each method call sets the system field `sy-subrc` to 0 in the moment the method is called.

## Alternative 1

`meth( ... )->meth1( ... )->meth2( ... )->...->methn( ... )`

### Description

Chained method call. Call of the instance method `methn` of an object. The reference variable for the object is the return value of the preceding method chaining.

A chained method call can be specified as a [standalone statement](abapcall_method_static_short.md) or as a [functional method call](abapcall_method_functional.md) in a suitable [operand position](../abap-syntax-elements-of-an-abap-program/abenexpression_positions.md). The relevant rules apply in parameter passing to `meth`.

If the return value of the last method has a structured data type, the chained method call can, like a structure, be listed in front of the [structure component selector](../../abap-glossary/abenstructure_component_sel_glosry.md) `-` and be used to access a component of the structure.

### Hint

In `methn`, a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) can be specified with a [constructor operator](../../abap-glossary/abenconstructor_operator_glosry.md) [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) or [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md) for `oref` not only in a functional call, but also in standalone statements.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the method `m3` of an object of the class `c3` that is addressed using method chaining.

``` abap
CLASS c3 DEFINITION. 
  PUBLIC SECTION. 
    METHODS m3 CHANGING c3 TYPE string. 
ENDCLASS. 
 
CLASS c2 DEFINITION. 
  PUBLIC SECTION. 
    METHODS m2  IMPORTING i2        TYPE string 
                RETURNING VALUE(r2) TYPE REF TO c3. 
ENDCLASS. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS m1 IMPORTING i1        TYPE string 
                     RETURNING VALUE(r1) TYPE REF TO c2. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    CREATE OBJECT r1. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD m2. 
    CREATE OBJECT r2. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c3 IMPLEMENTATION. 
  METHOD m3. 
    c3 = 'New text'. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA txt TYPE string VALUE `test`. 
    c1=>m1( 
      i1 = `p1` )->m2( 
      i2 = `p2` )->m3( 
      CHANGING c3 = txt ). 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 2

`meth( ... )->meth1( ... )->meth2( ... )->...->attr`

### Description

Chained attribute access. Access to the instance attribute `attr` of an object. The reference variable for the object is the return value of the preceding method chaining.

If the attribute has a structured data type, the chained attribute access can, like a structure, be listed in front of the [structure component selector](../../abap-glossary/abenstructure_component_sel_glosry.md) `-` and be used to access a component of the structure.

Chained attribute access can currently only be specified in suitable [read positions](../abap-syntax-elements-of-an-abap-program/abenexpression_positions.md). Writes to an attribute addressed using method chaining are not yet possible.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Chained attribute access in example class `CL_DEMO_METHOD_CHAINING`.

``` abap
cl_demo_output=>display( 
  NEW demo( )->meth( 
    `Hello ` )->meth( `world` )->meth( `!` )->text ).
```

### Executable Example

[Method Chaining](abenmethod_chaining_abexa.md)
