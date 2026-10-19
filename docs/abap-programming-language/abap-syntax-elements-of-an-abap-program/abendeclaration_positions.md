---
title: "Declaration Positions"
source_file: abendeclaration_positions.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements > Operand Positions > Expression Positions for Expressions > Write Positions for Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Declaration Positions

Declaration positions are [write-only positions](../../abap-glossary/abenwrite_only_position_glosry.md) in which a [declaration expression](../../abap-glossary/abendeclaration_expression_glosry.md) can be specified for an [inline declaration](../../abap-glossary/abeninline_declaration_glosry.md). There are no declaration positions within expressions.

Declaration positions include the following:

- Positions for the inline declaration of variables with [`DATA(var)`](../abap-declarations/abendata_inline.md) and [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). These are the following [write positions](../../abap-glossary/abenwrite_position_glosry.md), where the operand type can be determined completely and where the content of the operand is not evaluated but completely overwritten.

  - Left side of an assignment with the [assignment operator `=`](../abap-processing-internal-data/abenequals_operator.md)

    [`lhs = ...`](../abap-processing-internal-data/abenequals_operator.md)

  - Actual parameters for output parameters and return values of methods for [standalone method calls](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md):

    meth( [`IMPORTING p1 = a1 p2 = a2...`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md) [`RECEIVING r = a`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md) ) If a method call is located to the right side of an assignment or is part of an expression, these actual parameters are not declaration positions.

  - Target fields when catching an exception:

    CATCH EXCEPTION [`INTO oref`](../abap-program-flow-logic/abapcatch_try.md) CLEANUP [`INTO oref`](../abap-program-flow-logic/abapcleanup.md)

  - Target fields in statements for string processing and byte string processing:

    FIND ... [`MATCH COUNT mcnt`](../abap-processing-internal-data/abapfind_options.md)

    [`MATCH OFFSET moff`](../abap-processing-internal-data/abapfind_options.md)

    [`MATCH LENGTH mlen`](../abap-processing-internal-data/abapfind_options.md)

    [`RESULTS result_tab|result_wa`](../abap-processing-internal-data/abapfind_options.md)

    [`SUBMATCHES s1 s2 ...`](../abap-processing-internal-data/abapfind_options.md)

REPLACE ... [`REPLACEMENT COUNT rcnt`](../abap-processing-internal-data/abapreplace_options.md)

[`REPLACEMENT OFFSET moff`](../abap-processing-internal-data/abapreplace_options.md)

[`REPLACEMENT LENGTH mlen`](../abap-processing-internal-data/abapreplace_options.md)

[`RESULTS result_tab|result_wa`](../abap-processing-internal-data/abapreplace_options.md)

CONCATENATE ... [`INTO result`](../abap-processing-internal-data/abapconcatenate.md)

SPLIT ... [`INTO result1 result2 ...`](../abap-processing-internal-data/abapsplit.md)

[`INTO TABLE result_tab`](../abap-processing-internal-data/abapsplit.md)

CONVERT TEXT ... [`INTO SORTABLE CODE hex`](../abap-processing-internal-data/abapconvert_text.md)

GET BIT ... [`INTO val`](../abap-processing-internal-data/abapget_bit.md). - Target fields in statements for UTC time stamps:

CONVERT UTCLONG ... [`INTO DATE dat TIME tim DAYLIGHT SAVING TIME dst`](../abap-processing-internal-data/abapconvert_utclong.md) CONVERT ... [`INTO UTCLONG time_stamp`](../abap-processing-internal-data/abapconvert_date_utclong.md) GET TIME STAMP [`time_stamp`](../abap-processing-internal-data/abapget_time-stamp.md) CONVERT TIME STAMP ... [`INTO DATE dat TIME tim DAYLIGHT SAVING TIME dst`](../abap-processing-internal-data/abapconvert_time-stamp.md) CONVERT ... [`INTO TIME STAMP time_stamp`](../abap-processing-internal-data/abapconvert_date_time-stamp.md) - Target fields in statements for internal tables:

READ TABLE ... [`[REFERENCE] INTO dobj`](../abap-processing-internal-data/abapread_table_outdesc.md) LOOP AT ... [`[REFERENCE] INTO dobj`](../abap-processing-internal-data/abaploop_at_itab_result.md) INSERT ... [`[REFERENCE] INTO dobj`](../abap-processing-internal-data/abapinsert_itab_result.md) COLLECT ... [`[REFERENCE] INTO dobj`](../abap-processing-internal-data/abapcollect_itab_result.md) APPEND ... [`[REFERENCE] INTO dobj`](../abap-processing-internal-data/abapappend_result.md) MODIFY ... [`[REFERENCE] INTO dobj`](../abap-processing-internal-data/abapmodify_itab_result.md) FIND ... IN TABLE [`MATCH COUNT mcnt`](../abap-processing-internal-data/abapfind_itab_options.md)

IN TABLE [`MATCH LINE mlin`](../abap-processing-internal-data/abapfind_itab_options.md)

IN TABLE [`MATCH OFFSET moff`](../abap-processing-internal-data/abapfind_itab_options.md)

IN TABLE [`MATCH LENGTH mlen`](../abap-processing-internal-data/abapfind_itab_options.md)

IN TABLE [`RESULTS result_tab|result_wa`](../abap-processing-internal-data/abapfind_itab_options.md)

IN TABLE [`SUBMATCHES s1 s2 ...`](../abap-processing-internal-data/abapfind_itab_options.md) REPLACE ... IN TABLE [`REPLACEMENT COUNT rcnt`](../abap-processing-internal-data/abapreplace_itab_options.md)

IN TABLE [`REPLACEMENT LINE rlin`](../abap-processing-internal-data/abapreplace_itab_options.md)

IN TABLE [`REPLACEMENT OFFSET moff`](../abap-processing-internal-data/abapreplace_itab_options.md)

IN TABLE [`REPLACEMENT LENGTH mlen`](../abap-processing-internal-data/abapreplace_itab_options.md)

IN TABLE [`RESULTS result_tab|result_wa`](../abap-processing-internal-data/abapreplace_itab_options.md) - Target fields of the ABAP SQL statement `SELECT`:

SELECT ... [`INTO (elem1, elem2, ... )`](../abap-database-access/abapinto_clause.md) SELECT ... [`INTO wa`](../abap-database-access/abapinto_clause.md) SELECT ... [`INTO TABLE itab`](../abap-database-access/abapinto_clause.md) - Cursor field of the ABAP SQL statement `OPEN CURSOR`:

`OPEN CURSOR dbcur` Here, only `DATA` but not `FINAL` can be used. - Target fields of the statement `DESCRIBE`:

`DESCRIBE FIELD ... TYPE typ [COMPONENTS com] LENGTH ilen DECIMALS dec`

` OUTPUT-LENGTH olen HELP-ID hlp EDIT MASK mask` `DESCRIBE TABLE ... KIND knd LINES lin OCCURS n` `DESCRIBE DISTANCE ... INTO dst` - Target fields of various `GET` statements:

`GET PARAMETER ... FIELD dobj` `GET PF-STATUS status` GET REFERENCE [`INTO dref`](../abap-processing-internal-data/abapget_reference.md) `GET RUN TIME FIELD rtime` `GET TIME FIELD tim` - Target field for message output:

MESSAGE ... [`INTO text`](../abap-text-repositories/abapmessage.md) - Target field for a serialization:

CALL TRANSFORMATION ... [`RESULT XML rxml`](../abap-data-interchange-formats/abapcall_transformation.md) - All write positions during program generation:

`GENERATE SUBROUTINE POOL ... NAME prog error_handling` - [RAP](../../abap-glossary/abenrap_glosry.md) response structures and internal tables typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md):

MODIFY \[ENTITY\|ENTITIES\] ... \[[`` `response_param` ``](../../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_response.md)\]. COMMIT ENTITIES ... \[[`` `response_param` ``](../../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_response.md)\]. GET PERMISSIONS ... \[[`` `response_param` ``](../../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_response.md)\]. READ \[ENTITY\|ENTITIES\] ... \[[`` `response_param` ``](../../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_response.md)\]. SET LOCKS ... \[[`` `response_param` ``](../../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_response.md)\].

- Positions for the inline declaration of field symbols with [`FIELD-SYMBOL(<fs>)`](../abap-declarations/abenfield-symbol_inline.md). These are all places where a memory area can be assigned to a field symbol.

  - Field symbol in the statement `ASSIGN`:

    ASSIGN... [`TO <fs>`](../abap-processing-internal-data/abapassign.md)

  - Field symbols in statements for internal tables:

    READ TABLE ... [`ASSIGNING <fs>`](../abap-processing-internal-data/abapread_table_outdesc.md) LOOP AT ... [`ASSIGNING <fs>`](../abap-processing-internal-data/abaploop_at_itab_result.md) INSERT ... [`ASSIGNING <fs>`](../abap-processing-internal-data/abapinsert_itab_result.md) COLLECT ... [`ASSIGNING <fs>`](../abap-processing-internal-data/abapcollect_itab_result.md) APPEND ... [`ASSIGNING <fs>`](../abap-processing-internal-data/abapappend_result.md) MODIFY ... [`ASSIGNING <fs>`](../abap-processing-internal-data/abapmodify_itab_result.md)

## Hint

Unlike in [standalone method calls](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md), inline declarations cannot be specified as actual parameters for output parameters in a [functional method call](../abap-calling-and-exiting-program-units/abapcall_method_functional.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration expression [`DATA`](../abap-declarations/abendata_inline.md) for the declaration of an internal table `itab` after the addition [`INTO TABLE`](../abap-database-access/abapinto_clause.md) of a [`SELECT`](../abap-database-access/abapselect.md) statement.

``` abap
SELECT * 
       FROM scarr 
       INTO TABLE @FINAL(itab).
```
