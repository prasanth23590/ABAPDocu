---
title: "ABAP SQL - @dobj"
source_file: abenabap_sql_host_variables.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Operands sql_elem"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - @dobj

## Syntax

``` abap
... @dobj ...  
```

## Description

Specifying a [host variable](../../abap-glossary/abenhost_variable_glosry.md) in an ABAP SQL statement. Host variables are global or local data objects `dobj` declared in the ABAP program that are used in operand positions of ABAP SQL statements. Instead of the data object itself, a field symbol to which the data object is assigned can also be specified. Dereferenced data reference variables can also be specified. Depending on the operand position, the data objects can be [variables](../../abap-glossary/abenvariable_glosry.md) or [constants](../../abap-glossary/abenvariable_glosry.md). Constant host variables are [host constants](../../abap-glossary/abenhost_constant_glosry.md).

To identify a host variable, the names of [named](../../abap-glossary/abennamed_data_object_glosry.md) data objects or field symbols should always be directly prefixed by the escape character `@`. The escape character can only be used in programs, in which the program property [*fixed point arithmetic*](../../abap-glossary/abenfixed_point_arithmetic_glosry.md) is activated.

The content of host variables in read positions is passed to the database system together with the SQL statement before it is executed. The content of host variables in write positions is taken from the database system after the SQL statement is ended.

- Read positions in which host variables are handled as [elementary SQL expressions](abensql_elem.md) are subject to the corresponding rules and any mappings are made to a dictionary type. The content is evaluated on the database in accordance with this type.

- In operand positions in which host variables are not handled as SQL expressions, a [type conversion](../abap-processing-internal-data/abenconversion_rules.md) into the appropriate data type takes place if required. In read positions, it must be possible to convert the content of a host variable to the data type required in the operand position in a [lossless](../abap-processing-internal-data/abapmove_exact.md) manner. Any unsuitable [host constants](../../abap-glossary/abenhost_constant_glosry.md) produce syntax warnings or syntax errors. Host variables that cannot be converted in a lossless manner produce a catchable exception of class `CX_SY_OPEN_SQL_DATA_ERROR`.

## Restriction

Host variables can have a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) but not an [ABAP enumerated type](../../abap-glossary/abenenumerated_type_glosry.md).

## Hints

- In some operand positions in which host variables are allowed and [host expressions](abenabap_sql_host_expressions.md) are prohibited, a host variable can nevertheless be specified with the syntax `@( dobj )` and is handled as a host variable and not as an expression.

- ABAP data objects that are specified as enclosed dynamic tokens do not belong to the host variables and cannot be prefixed by the escape character `@`.

- The escape character for host variables is independent of the general escape character for names [`!`](../abap-operands/abennames_escaping.md). The escape character `!` can also be written in front of host variables that are already prefixed by the escape character `@`. However, this is not recommended.

- In addition to host variables, [literals](abenabap_sql_literals.md) can also be specified at the respective read positions in ABAP SQL statements. A literal, however, cannot and does not need to be prefixed by the escape character `@`. While [untyped literals](abenabap_sql_untyped_literals.md) are usually handled as host variables, [typed literals](abenabap_sql_typed_literals.md) are always handled as elementary SQL expressions.

- If host variables are used as [elementary SQL expressions](abensql_elem.md), in particular as operands of other SQL expressions, they are mapped to a fixed dictionary type and the corresponding rules apply. This is different from their use in other operand positions, for which conversions to different dictionary types are generally possible.

- A CDS [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) is specified as usual by using the name of the CDS enumerated type, followed by a [component selector](../../abap-glossary/abencomponent_selector_glosry.md) and the name of a CDS enumerated constant `@enumtype-enumconstant`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of different host variables, whereby the escape character `@` is always used.

``` abap
DATA carrid TYPE spfli-carrid. 
cl_demo_input=>request( CHANGING field = carrid ). 
 
DATA: BEGIN OF result, 
        carrid TYPE sflight-carrid, 
        connid TYPE sflight-connid, 
      END OF result. 
SELECT carrid, connid 
       FROM sflight 
       WHERE carrid = @carrid 
       INTO CORRESPONDING FIELDS OF @result. 
ENDSELECT. 
 
FIELD-SYMBOLS <result> LIKE result. 
SELECT carrid, connid 
       FROM sflight 
       WHERE carrid = @carrid 
       INTO CORRESPONDING FIELDS OF @<result>. 
ENDSELECT. 
 
DATA dref LIKE REF TO result. 
SELECT carrid, connid 
       FROM sflight 
       WHERE carrid = @carrid 
       INTO CORRESPONDING FIELDS OF @dref->*. 
ENDSELECT.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a host variable `prefix` with the type `c` and a host variable `name` of the type `string`. The host variable `name` is used on the right-hand side of the `WHERE` condition. A string is possible, and since the introduction of ABAP SQL expressions on the right side of a condition, also an SQL expression.

``` abap
DATA: 
  prefix TYPE c LENGTH 5, 
  name   TYPE string. 
 
SELECT FROM scarr 
       FIELDS @prefix && carrid AS carrid, 
              carrname 
       WHERE carrname = @name 
       INTO TABLE @FINAL(result).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `SELECT` statement raises an exception because the content of the host variable `carrid` cannot be assigned in a lossless manner. If `carrid` were a constant, there would be an additional syntax warning.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(carrid) = `LH          `. 
 
TRY. 
    SELECT * 
           FROM scarr 
           WHERE carrid = @carrid 
           INTO TABLE @FINAL(itab). 
  CATCH cx_sy_open_sql_data_error INTO FINAL(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```

## Description

Specifies a host variable typed with a CDS enumerated type in an ABAP SQL statement. Host variables typed with a CDS enumerated type can be specified in all operand positions that are documented in the table above.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md) `fri` is specified as host variable in different operand positions.

``` abap
DATA fri TYPE demo_cds_enum_weekday. 
SELECT char1 && '_' && char2 AS group, 
    num1, 
    @fri AS EnumField 
    FROM demo_expressions 
    WHERE @fri = @demo_cds_enum_weekday-fri 
    ORDER BY @fri 
    INTO TABLE @FINAL(itab).
```
