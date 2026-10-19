---
title: "CASE TYPE OF"
source_file: abapcase_type.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Control Structures > Branches"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CASE TYPE OF

## Syntax

``` abap
CASE TYPE OF oref.   
  [WHEN TYPE class|intf [INTO target1].   
    [statement_block1]]   
  [WHEN TYPE class|intf [INTO target2].   
    [statement_block2]]   
  ...   
  [WHEN OTHERS.   
    [statement_blockn]]   
ENDCASE.  
```

### Addition

[`... INTO target`](abapcase_type.md#addition)

## Overview

### Description

Special [case distinction](../../abap-glossary/abencase_distinction_glosry.md) for [object reference variables](../../abap-glossary/abenobject_refer_variable_glosry.md). This form of a control structure introduced using [`CASE`](abapcase.md) checks the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) of a non-initial object reference variable and the [static type](../../abap-glossary/abenstatic_type_glosry.md) of an initial object reference variable `oref`. `oref` expects an object reference variable with the static type of a class or an interface. `oref` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md).

A class `class` or an interface `intf` that can be used at this position must be specified after `WHEN TYPE`. The first statement block `statement_block` is executed for which the class `class` or the interface `intf` is more general than or equal to the following:

- A dynamic type of a non-initial object reference variable `oref`

- A static type of an initial object reference variable `oref`

If this does not apply to any class `class` or interface `intf`, the statement block is executed after `WHEN OTHERS`. No object type `class` or `intf` can be specified if it is known statically that it does not fulfill the condition.

### Hints

- A case distinction using `CASE TYPE OF` is another way of writing the following branch using [`IF`](abapif.md) and the predicate expression [`IS INSTANCE OF`](abenlogexp_instance_of.md) and the corresponding rules and notes apply:

  IF oref [`IS INSTANCE OF`](abenlogexp_instance_of.md) class\|intf. \[statement_block1\] ELSEIF oref [`IS INSTANCE OF`](abenlogexp_instance_of.md) class\|intf. \[statement_block2\] ... ELSE. \[statement_blockn\] ENDIF.

- In the control structure, more specific classes `class` or interfaces `intf` must be listed before more general classes or interfaces to enable the associated statement block to be executed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Case distinction for the dynamic type of an object reference variable `oref`, from more specific to more general classes. In the case shown, `c2` is the first class that fulfills the condition. `oref` can be assigned to `ref2` with static type `c2` without raising an exception.

``` abap
CLASS c1 DEFINITION. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
ENDCLASS. 
 
CLASS c3 DEFINITION INHERITING FROM c2. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
 
    DATA oref TYPE REF TO object. 
 
    DATA: ref1 TYPE REF TO c1, 
          ref2 TYPE REF TO c2, 
          ref3 TYPE REF TO c3. 
 
    oref = NEW c2( ). 
 
    CASE TYPE OF oref. 
      WHEN TYPE c3. 
        ref3 ?= oref. 
      WHEN TYPE c2. 
        ref2 ?= oref. 
      WHEN TYPE c1. 
        ref1 ?= oref. 
      WHEN OTHERS. 
        ... 
    ENDCASE. 
 
  ENDMETHOD. 
ENDCLASS.
```

### Executable Example

[Case Distinction `CASE TYPE OF` for Exceptions](abencase_type_of_exception_abexa.md)

## Addition

`... INTO target`

### Description

For every statement `WHEN TYPE` of a case distinction introduced using `CASE TYPE OF`, a target variable `target` can be specified after the optional addition `INTO` as follows:

- An existing [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md) `ref` whose [static type](../../abap-glossary/abenstatic_type_glosry.md) is more general than or equal to the class `class` or interface `intf` specified in the statement.

- An inline declaration [`DATA(ref)`](../abap-declarations/abendata_inline.md) or [`FINAL(ref)`](../abap-declarations/abenfinal_inline.md). In this case, an object reference variable with the static type of the class `class` or the interface `intf` is declared.

If the addition `INTO` is specified in the first `WHEN` statement that fulfills the condition, the reference `oref` is assigned to `ref` before the statement block is executed, whereby both [upcasts](../../abap-glossary/abenup_cast_glosry.md) and [downcasts](../../abap-glossary/abendown_cast_glosry.md) can be performed.

### Hint

The statement

`WHEN TYPE class|intf INTO ref.`

is a semantically identical short form of

``` abap
WHEN TYPE class|intf. 
  ref = oref.
```

The statement

`WHEN TYPE class|intf INTO DATA(ref).`

is a semantically identical short form of

``` abap
WHEN TYPE class|intf. 
  DATA(ref) = CAST class|intf( oref ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following case distinction shows the short form of the case distinction of the previous example.

``` abap
CLASS c1 DEFINITION. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
ENDCLASS. 
 
CLASS c3 DEFINITION INHERITING FROM c2. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
 
    DATA oref TYPE REF TO object. 
 
    DATA: ref1 TYPE REF TO c1, 
          ref2 TYPE REF TO c2, 
          ref3 TYPE REF TO c3. 
 
    oref = NEW c2( ). 
 
    CASE TYPE OF oref. 
      WHEN TYPE c3 INTO ref3. 
      WHEN TYPE c2 INTO ref2. 
      WHEN TYPE c1 INTO ref1. 
      WHEN OTHERS. 
        ... 
    ENDCASE. 
 
  ENDMETHOD. 
ENDCLASS.
```

### Executable Example

[Case Distinction `CASE TYPE OF` for RTTI](abencase_type_of_rtti_abexa.md)
