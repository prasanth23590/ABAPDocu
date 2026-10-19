---
title: "itab - Table Expressions (table_exp)"
source_file: abentable_expressions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Expressions (table_exp)

## Syntax

``` abap
... itab[ itab_line ][-comp|[ ... ]|->comp] ...  
```

[`itab_line`](abentable_exp_itab_line.md) · [`[-comp|[ ... ]|->comp]`](abentable_exp_chaining.html)

## Description

A table expression consists of an internal table `itab` directly followed by a line specification [`itab_line`](abentable_exp_itab_line.md) in square brackets `[ ]`. A chaining [`-comp|[ ... ]|->comp`](abentable_exp_chaining.md) can be appended to this line. The expression searches for the specified line in the internal table.

- If no chaining is specified, the entire line is returned as the result of the corresponding line type.

- If a [chaining](abentable_exp_chaining.md) is specified, the following is possible:

  - The structure component selector `-` can be used to access the component `comp` in the read line.

  - Square brackets `[ ... ]` can be used to chain multiple table expressions.

  - The object component selector `->` can be used to access a component `comp` of the object referenced by the preceding expression.

The result of a table expression can be used as follows:

- Read positions

  - A table expression can be specified in [general expression positions](../abap-syntax-elements-of-an-abap-program/abengeneral_expression_positions.md) and [functional operand positions](../abap-syntax-elements-of-an-abap-program/abenfunctional_positions.md) with a suitable [operand type](../../abap-glossary/abenoperand_type_glosry.md). The result is used here as an operand. The [type of the result](abentable_exp_result.md) cannot be controlled in these operand positions using [constructor operators](../../abap-glossary/abenconstructor_operator_glosry.md). A [default value](abentable_exp_optional_default.md) can be specified for lines that are not found.

  - A table expression can be specified as a special [expression variant](abapassign_mem_area_writable_exp.md) for the memory area in the statement [`ASSIGN`](abapassign.md).

  - A table expression can be specified as an argument of the built-in function [`line_index`](abenline_index_function.md) and the [predicate function](../../abap-glossary/abenpredicate_function_glosry.md) [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md).

- Write positions

  - A table expression can be specified as a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) in [result positions](../../abap-glossary/abenresult_position_glosry.md). The line found can be modified directly here.

The internal table `itab` must be specified directly using its name, a field symbol, or a dereferenced data reference as described under [Read Positions](../abap-operands/abendata_objects_usage_reading.md).

If the specified line is not found, a catchable exception of the class `CX_SY_ITAB_LINE_NOT_FOUND` is raised in all operand positions, except when

- a [default value](abentable_exp_optional_default.md) is specified in the definition of the [type of the result](abentable_exp_result.md),

- a table expression is used in the statement [`ASSIGN`](abapassign_mem_area_writable_exp.md), where `sy-subrc` is set to the value 4,

- used in the predicate function [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md), where the truth value *false* is returned,

- used in the built-in function [`line_index`](abenline_index_function.md), where the value *0* is returned.

## Hints

- In table expressions, the empty square brackets `[]` cannot be specified after `itab`. In other operand positions, these empty brackets distinguish the table body from [header lines](../../abap-glossary/abenheader_line_glosry.md).

- Functions and constructor expressions cannot currently be specified for `itab`, but the table expressions shown under [Chainings](abentable_exp_chaining.md) are possible.

- A table expression cannot be followed directly by a [specified offset/length](../../abap-glossary/abenoffset_length_specific_glosry.md) [`+off(len)`](../abap-operands/abenoffset_length.md), but after a [chaining](abentable_exp_chaining.md) whose final place is a suitable structure component after a structure component selector.

- Duplicate selections, that is, multiple reads performed on the same line of an internal table in different expressions, must be avoided in a statement or a loop with multiple table expressions. In these cases, a selection should be made before the statement or the loop and the result referenced by a field symbol or reference variable.

- The exception class `CX_SY_ITAB_LINE_NOT_FOUND` contains attributes for displaying the line number in the index or key used if an access fails. If only index accesses are used in statements with multiple table expressions, it is not possible to distinguish which expression was unsuccessful.

- Each table expression can be viewed as a short form for a variant of the statement [`READ TABLE`](abapread_table.md) that enables reads to be performed on lines of internal tables in operand positions.

- In write positions, the same [restrictions](abapread_table_outdesc.md) apply with respect to modifying key fields to table expressions whose [result](abentable_exp_result.md) is a field symbol or temporary reference variable as to other field symbols or data reference variables that point to lines of internal tables. In particular, table expressions that return a line of a sorted table or hashed table to write positions like the left side of an assignment or as actual parameters for output parameters always raise an exception.

- A table expression cannot be specified in a write position if it is a read-only table, such as an input parameter passed by reference. This restriction applies even if a [chaining](abentable_exp_chaining.md) is used and the content of the table itself is not actually modified.

- Unlike [`READ TABLE`](abapread_table.md), a table expression does not change the value of the system field `sy-tabix`, except when used in the statement [`ASSIGN`](abapassign_mem_area_writable_exp.md).

- Like the statement [`READ TABLE`](abapread_table.md), a table expression is a single line read. If multiple lines of an internal table are to be read, the statement [`LOOP`](abaploop_at_itab.md) or a [`FOR` expression](../abap-program-flow-logic/abenfor.md) generally has better performance than using table expressions in a loop.

- [Mesh path expressions](abenmesh_path_expression.md) are a special form of table expression that can be used in exactly the same way as table expressions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The content of the component `carrid` of the line of the internal table `carrier_tab` is passed to the method `get_spfli`. In this table, the component `carrname` of the [secondary key](../../abap-glossary/abensecondary_key_glosry.md) `name` has a specific value.

``` abap
DATA carrier_tab TYPE HASHED TABLE OF scarr 
                 WITH UNIQUE KEY carrid 
                 WITH NON-UNIQUE SORTED KEY name COMPONENTS carrname. 
 
SELECT * FROM scarr INTO TABLE @carrier_tab. 
 
TRY. 
    FINAL(flight_tab) = cl_demo_spfli=>get_spfli( 
      carrier_tab[ KEY name 
                   COMPONENTS carrname = 'United Airlines' ]-carrid ). 
    cl_demo_output=>display( flight_tab ). 
  CATCH cx_sy_itab_line_not_found. 
    cl_demo_output=>display( `Nothing found` ). 
ENDTRY.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first calculation with table lines is a bad example of how to use table expressions. The same selection is made three times in the same statement. The second calculation shows how this can be avoided by using an [assignment to a field symbol](abapassign_mem_area_writable_exp.md).

``` abap
DATA itab TYPE TABLE OF i. 
itab = VALUE #( ( 3 ) ( 5 ) ). 
 
"Bad example 
itab[ table_line = 3 ] = 
  itab[ table_line = 3 ] * itab[ table_line = 3 ]. 
 
"Good example 
ASSIGN itab[ table_line = 5 ] TO FIELD-SYMBOL(<fs>). 
<fs> = <fs> * <fs>.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ITAB_LINE_NOT_FOUND`

- *Cause:* The specified table line was not found.

  *Runtime error:* `ITAB_LINE_NOT_FOUND`
