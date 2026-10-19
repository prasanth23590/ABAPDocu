---
title: "ABAP SQL - @( expr )"
source_file: abenabap_sql_host_expressions.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Operands sql_elem"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - @( expr )

## Syntax

``` abap
... @( expr ) ...  
```

## Description

Specification of a [host expression](../../abap-glossary/abenhost_expression_glosry.md) in an ABAP SQL statement. [Host expressions](../../abap-glossary/abenhost_expression_glosry.md) are ABAP expressions `expr` that can be specified in operand positions in ABAP SQL. `expr` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). Any expressions or calls possible here, as well as individual data objects, can be specified.

Host expressions can be specified as [elementary SQL expressions](abensql_elem.md) in all operand positions in which [SQL expressions](abapsql_expr.md) are possible. They can also occur in the following read positions in which no SQL expressions are possible:

- Operand `n` after [`UP TO`](abapselect_up_to_offset.md).

- Operand `n` after [`PACKAGE SIZE`](abapinto_clause.md).

- Right sides of [SQL conditions](abenabap_sql_stmt_logexp.md) except for `LIKE` and `IN`.

- [Actual parameters](abapselect_data_source.md) for input parameters of CDS views or CDS table functions.

- Work areas `wa` and the internal tables `itab` of the statements [`INSERT`](abapinsert_dbtab.md), [`UPDATE`](abapupdate.md), [`MODIFY`](abapmodify_dbtab.md) and [`DELETE`](abapdelete_dbtab.md).

- Right side of a [`SET` expression](abapupdate_set_expression.md) in `UPDATE`.

The relevant restrictions apply in operand positions in which host variables are handled like SQL expressions.

The host expressions of an ABAP SQL statement are evaluated from left to right and the results are passed to the database, like the content of [host variables](abenabap_sql_host_variables.md). Conversions of the result of a host expression to the data type required in the operand position must be possible and be [lossless](../abap-processing-internal-data/abapmove_exact.md). The following additional restrictions apply:

- Host expressions cannot be used in dynamic tokens.

- In a host expression of a [`SELECT` list](abapselect_list.md), it is not possible to derive a data type from the operand position for the character `#` for a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md).

## Restriction

Operands of host expressions can have a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) but not an [ABAP enumerated type](../../abap-glossary/abenenumerated_type_glosry.md).

## Hints

- In the operand positions where host expressions can be specified, it is also always possible to specify [host variables](abenabap_sql_host_variables.md) but not vice versa.

- In some operand positions in which host expressions are forbidden, but [literals](abenabap_sql_literals.md) and [host variables](abenabap_sql_host_variables.md) are allowed, the syntax `@( literal )` and `@( dobj )` can be used. It is handled as a literal or host variable rather than as an expression.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the right side of a [comparison](abenwhere_logexp_compare.md) in a [`WHERE`](abapwhere.md) condition using a [functional method call](../../abap-glossary/abenfunctional_method_call_glosry.md) in a host expression. Within the host expression, the instance operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) is used here to create a temporary object.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    METHODS get_url RETURNING VALUE(url) TYPE scarr-url. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD get_url. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    SELECT FROM scarr 
           FIELDS carrname 
           WHERE  url = @( NEW demo( )->get_url( ) ) 
           INTO TABLE @FINAL(itab). 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Examples

- [Host Expressions in the `WHERE` Condition](abenhost_expr_in_where_cond_abexa.md)

- [SQL Expressions in the `WHERE` Condition](abensql_expr_in_where_cond_abexa.md)
