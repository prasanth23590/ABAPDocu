---
title: "ASSIGN, writable_exp"
source_file: abapassign_mem_area_writable_exp.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN > ASSIGN, mem_area"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN, writable_exp

## Syntax Forms

**Constructor Expressions**

``` abap
1. ... NEW class( ... )->attr|(attr_name) ...

2. ... CAST type( ... )->*| dobj|(dobj_name) ...
```

**Table Expressions**

``` abap
3. ... table_exp ...
```

### Alternative

[1. `... NEW class( ... )->attr|(attr_name)`](abapassign_mem_area_writable_exp.md#alternative-1)

[2. `... CAST type( ... )->...`](abapassign_mem_area_writable_exp.md#alternative-2)

[3. `... table_exp`](abapassign_mem_area_writable_exp.md#alternative-3)

## Overview

### Description

These variants for specifying the memory area [`mem_area`](abapassign_mem_area.md) of the statement [`ASSIGN`](abapassign.md) exploit the fact that the operand position after `ASSIGN` is a [result position](../../abap-glossary/abenresult_position_glosry.md) in which [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) can be specified.

### Hints

- Writable expressions can be specified for the memory area but no other expressions, because only writable expressions can have a non-temporary result. Assigning a temporary data object to a field symbol would not make sense.

- Writable expressions cannot be specified dynamically in a data object [`name`](abapassign_mem_area_dynamic_access.md).

## Alternative 1

`... NEW class( ... )->attr|(attr_name)`

### Description

This variant for specifying the memory area [`mem_area`](abapassign_mem_area.md) of the statement [`ASSIGN`](abapassign.md) assigns an attribute of an instance of class `class` to a field symbol. The instance of the class is created inline with the [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) [`NEW class( ... )`](../abap-creating-objects-and-values/abennew_constructor_params_class.md). The object component selector `->` following the constructor expression selects the attribute.

The attribute can be specified statically as `attr` or dynamically as the content of a character-like data object `attr_name` in parentheses.

- For static specification `attr`, the same rules apply as to [statically specifying](abapassign_mem_area_static_dobj.md) the memory area, but no offsets/lengths can be specified and `sy-subrc` is not set by the `ASSIGN` statement itself.

- For dynamic specification, the rules of a [dynamic target](../abap-operands/abenobject_component_selector.md) behind the object component selector apply.

In this variant, the return code `sy-subrc` is not set by the statement `ASSIGN` itself, but by the constructor expression. The instance operator `NEW` sets the return code `sy-subrc` to 0, if the object is created successfully.

If the attribute specified dynamically in `attr_name` is not found, an exception of class `CX_SY_ASSIGN_ILLEGAL_COMPONENT` is raised. An assignment of the constructor operator `NEW` is either successful or leads to an exception and the addition `ELSE UNASSIGN` cannot be used. In case of an exception, an existing field symbol keeps it previous state.

### Hint

Assigning an attribute `attr` of an object created using `NEW` to a field symbol persists this object as long as the field symbol points to the attribute.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Constructor expression with `NEW` in the specified memory area of statement `ASSIGN` statements. The assignment of the attribute `attr` to a field symbol persists the object. In the first assignment the attribute is specified statically, in the following it is specified dynamically. The third assignment raises an exception since the attribute is not found.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    DATA attr TYPE string VALUE 'foo'. 
ENDCLASS. 
 
CLASS example DEFINITION. 
  PUBLIC SECTION. 
    METHODS main. 
ENDCLASS. 
 
CLASS example IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    ASSIGN NEW demo( )->attr TO FIELD-SYMBOL(<fs1>). 
    out->write( <fs1> ). 
 
    ASSIGN NEW demo( )->('attr') TO FIELD-SYMBOL(<fs2>). 
    out->write( <fs2> ). 
 
    TRY. 
        ASSIGN NEW demo( )->('foo') TO FIELD-SYMBOL(<fs3>). 
        out->write( <fs3> ). 
      CATCH cx_sy_assign_illegal_component INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 2

`... CAST type( ... )->...`

### Description

This variant for specifying the memory area [`mem_area`](abapassign_mem_area.md) of the statement [`ASSIGN`](abapassign.md) assigns a data object that is referenced by the result of the [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) [`CAST type( ... )`](abenconstructor_expression_cast.md) to a field symbol. The object component selector `->` following the constructor expression selects the data object. For `type`, a data type or an object type (class or interface) can be specified.

The data object assigned to the field symbol can be specified with the following [`CAST`](abenconstructor_expression_cast.md) expressions combined with the object component selector:

- `CAST dtype( ... dref )->*`

- `CAST dtype( ... dref )->comp|('comp_name')`

- `CAST class|intf( ... oref )->attr|('attr_name')`

The same rules apply as described for [`CAST`](abenconstructor_expression_cast.md) with the exception that no [offset/length specification](../../abap-glossary/abenoffset_length_specific_glosry.md) can be specified. Especially, the system behavior in case of an error is governed by the `CAST` expression. The return code `sy-subrc` is not set. An assignment of the constructor operator `CAST` is either successful or leads to an exception and the addition `ELSE UNASSIGN` must not be used. If an exception occurs, an existing field symbol keeps it previous state.

### Hint

In the `ASSIGN` statement, the `CAST` operator cannot be used for calling a method.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example is the same as one shown under [`CAST`](abenconstructor_expression_cast.md). Instead of assigning `CAST` expressions to data objects, they are assigned to field symbols here. The example shows that the system behavior in the case of an error in the `CAST` expression is the same in both examples.

``` abap
TYPES: 
  BEGIN OF struc, 
    col TYPE i, 
  END OF struc. 
 
INTERFACE intf. 
ENDINTERFACE. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
    DATA attr TYPE string VALUE 'foo'. 
ENDCLASS. 
 
CLASS example DEFINITION. 
  PUBLIC SECTION. 
    METHODS main. 
ENDCLASS. 
 
CLASS example IMPLEMENTATION. 
  METHOD main. 
 
    DATA(dref) = NEW struc( col = 111 ). 
    DATA(iref) = NEW cls( ). 
 
    ASSIGN CAST struc( dref )->col TO FIELD-SYMBOL(<num>). 
    ASSERT <num> = 111. 
    ASSIGN CAST cls( iref )->attr TO FIELD-SYMBOL(<txt>). 
    ASSERT <txt> = 'foo'. 
 
    UNASSIGN <num>. 
    ASSIGN CAST struc( dref )->('col') TO <num>. 
    ASSERT <num> = 111. 
    UNASSIGN <txt>. 
    ASSIGN CAST cls( iref )->('attr') TO <txt>. 
    ASSERT <txt> = 'foo'. 
 
    DATA(exc) = 0. 
    TRY. 
        ASSIGN CAST struc( dref )->('foo') TO <num>. 
      CATCH cx_sy_assign_illegal_component. 
        exc += 1. 
    ENDTRY. 
    TRY. 
        ASSIGN CAST cls( iref )->('foo') TO <txt>. 
      CATCH cx_sy_assign_illegal_component. 
        exc += 1. 
    ENDTRY. 
    CLEAR dref. 
    TRY. 
        ASSIGN CAST struc( dref )->('col') TO <num>. 
      CATCH cx_sy_assign_illegal_component. 
        exc += 1. 
    ENDTRY. 
    CLEAR iref. 
    TRY. 
        ASSIGN CAST cls( iref )->('attr') TO <txt>. 
      CATCH cx_sy_assign_illegal_component. 
        exc += 1. 
    ENDTRY. 
    ASSERT exc = 4. 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 3

`... table_exp`

### Description

This variant for specifying the memory area [`mem_area`](abapassign_mem_area.md) of the statement [`ASSIGN`](abapassign.md) assigns the result of the [table expression](../../abap-glossary/abentable_expression_glosry.md) [`table_exp`](abentable_expressions.md) or [table expression chaining](abentable_exp_chaining.md) to the field symbol. The result of a table expression in these positions is always a temporary field symbol.

- If a single table expression is specified, or a [chaining](abentable_exp_chaining.md) whose last position is a table expression, the entire line found is assigned to the field symbol.

- If a [chaining](abentable_exp_chaining.md) is specified whose last position is a structure component after a structure component selector, this component is assigned to the field symbol. No offsets/lengths, however, can be specified for the structure component here.

In this variant, the statement `ASSIGN` sets the return code `sy-subrc`.

- If the specified line is found, `sy-subrc` is set to 0.

- If the assignment is not successful, `sy-subrc` is set to 4, except when the end of the table is reached in binary searches in [sorted tables](../../abap-glossary/abensorted_table_glosry.md). In this case, `sy-subrc` is set to 8. If `sy-subrc` is set to 4 or 8, the state of the field symbol depends on the addition [`ELSE UNASSIGN`](abapassign_else_unassign.md):

  - If `ELSE UNASSIGN` is not specified, the field symbol keeps its previous state.

  - If `ELSE UNASSIGN` is specified, no memory area is assigned to the field symbol. The field symbol has the state unassigned after the `ASSIGN` statement.

Unlike in other use cases of table expressions, the system field `sy-tabix` is set here in the same way as in a corresponding [`READ TABLE`](abapread_table.md) statement.

In this variant of the statement `ASSIGN`, the addition [`CASTING`](abapassign_casting.md) can only be specified in assignments to an existing field symbol and not in [inline declarations](../abap-declarations/abenfield-symbol_inline.md), and only as a standalone addition. The addition [`RANGE`](abapassign_range.md) cannot be specified.

### Hints

- This variant of the statement `ASSIGN` can be regarded as a different form of [`READ TABLE ... ASSIGNING ...`](abapread_table_outdesc.md).

  - More specifically, the value of `sy-subrc` and `sy-tabix` is set as in the statement `READ TABLE` and

  - the addition [`CASTING`](abapassign_casting.md) cannot be specified after an [inline declaration](../abap-declarations/abenfield-symbol_inline.md) for the field symbol.

    Unlike `READ TABLE`, chainings can also be used to assign components of read lines or lines of nested internal tables.

- The constructor operators `VALUE` and `REF` used to control the [result](abentable_exp_result.md) of the table expression cannot be used here.

- If the specified line is not found, an exception is not raised, unlike in other uses of table expressions.

- If `ELSE UNASSIGN` is not specified, it is not sufficient to evaluate the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`<fs> IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md), but `sy-subrc` must be checked. If `ELSE UNASSIGN` is specified, the predicate expression as well as `sy-subrc` can be evaluated.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example works in the same way as the example for [`READ TABLE ... ASSIGNING ...`](abapread_table_outdesc.md). Here, the `READ` statement is replaced by an `ASSIGN` statements and the required component is assigned directly.

``` abap
DATA: carrid TYPE sflight-carrid, 
      connid TYPE sflight-connid, 
      fldate TYPE sflight-fldate. 
 
... 
 
DATA sflight_tab TYPE SORTED TABLE OF sflight 
                 WITH UNIQUE KEY carrid connid fldate. 
 
SELECT * 
       FROM sflight 
       WHERE carrid = @carrid AND 
             connid = @connid 
       INTO TABLE @sflight_tab. 
 
IF sy-subrc = 0. 
  ASSIGN sflight_tab[ KEY primary_key COMPONENTS 
                          carrid = carrid 
                          connid = connid 
                          fldate = fldate ]-price 
         TO FIELD-SYMBOL(<price>). 
  IF sy-subrc = 0. 
    <price> *= '0.9'. 
  ENDIF. 
ENDIF.
```
