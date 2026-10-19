---
title: "CDS DDL - Using CDS Enumerated Types"
source_file: abencds_use_enum_type.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE > ABAP CDS - Enumerated Types > CDS DDL - DEFINE TYPE ENUM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Using CDS Enumerated Types

This section summarizes the use of [CDS elements](../../abap-glossary/abencds_element_glosry.md) with an enumerated type.

- [Declaration](abencds_use_enum_type.md#declaration)

- [Operand Positions for CDS Elements with an Enumerated Type](abencds_use_enum_type.md#operand-positions-for-cds-elements-with-an-enumerated-type)

  - [CDS Enumerated Type](abencds_use_enum_type.md#cds-enumerated-type)

  - [CDS Enumerated Constant](abencds_use_enum_type.md#cds-enumerated-constant)

  - [CDS Enumerated Element](abencds_use_enum_type.md#cds-enumerated-element)

- [Simple Case Expressions](abencds_use_enum_type.md#simple-case-expressions)

- [Cast Expressions](abencds_use_enum_type.md#cast-expressions)

- [Logical Expressions](abencds_use_enum_type.md#logical-expressions)

- [Parameter Passing](abencds_use_enum_type.md#parameter-passing)

- [Type Descriptions](abencds_use_enum_type.md#type-descriptions)

## Executable Example

[CDS Enumerated Type, Use](abencds_enum_abexa.md)

## Declaration

The following enumerated operands are available:

- **CDS enumerated type**

  The [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) `EnumType` itself.

- **CDS enumerated constant**

  An [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) `EnumConstant` defines a value of the value set of an enumerated type. A CDS enumerated constant is specified using the name of the enumerated type `EnumType`, followed by a period (.), a hash character (#), and the name of an enumerated constant `EnumConstant`. Example: `EnumType.#EnumConstant`

- **CDS enumerated element**

  A [CDS enumerated element](../../abap-glossary/abencds_enum_element_glosry.md) contains one of the enumerated values of the respective enumerated type. CDS enumerated elements can be defined as follows:

  1.  Using a [cast expression](abencds_cast_expression_v2.md).

  2.  Exposing an [input parameter](../../abap-glossary/abeninput_parameter_glosry.md), defined in the parameter list after [`WITH PARAMETERS`](abencds_parameter_list_v2.md) and typed with an enumerated type `EnumType` as an element in the `SELECT` list of a CDS entity.

  3.  Exposing a field typed with an enumerated type from a [data source](abencds_data_source_v2.md) or from an [association target](../../abap-glossary/abenassociation_target_glosry.md).

  4.  Using a [case expression](abencds_case_expression_v2.md) with operands of an enumerated type.

  5.  Reusing an expression from the `SELECT` list via [`$projection`](abencds_reusable_expression_v2.md).

  6.  Using an enumerated constant in the element list of a CDS entity.

The technical storage type of the content of an operand of an enumerated element is the [base type](../../abap-glossary/abenbase_type_glosry.md) of the CDS enumerated type. However, in the code element information in ADT or in the debugger, the data type of CDS enumerated elements is displayed as `ENUM`. The possible content is defined by the [enumerated values](../../abap-glossary/abenenumerated_value_glosry.md) `EnumValue1`, `EnumValue2`, ..., of which exactly one value must have the type-specific initial value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity demonstrates operands of an enumerated type.

``` abap
@AbapCatalog.viewEnhancementCategory: [#NONE]
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, enum demo'

define view entity DEMO_CDS_ENUM_TYPE_USAGE_2

  with parameters
    p1 : DEMO_CDS_ENUM_CHAR
  as select from DEMO_CDS_ENUM_TYPE_USAGE_1
{
  key Id,
      friday,

      cast(abap.char'A' as DEMO_CDS_ENUM_CHAR) as CastExp,

      $parameters.p1                           as EnumParameterField,

      DEMO_CDS_ENUM_CHAR.#second_value         as EnumConstantField,

      case friday
      when DEMO_CDS_ENUM_STACK.#FRI
      then DEMO_CDS_ENUM_STACK.#SAT
      else null
      end                                      as EnumCase,

      $projection.EnumCase                     as ReuseField
}
```

The following image of the code element information of the CDS view entity `DEMO_CDS_ENUM_TYPE_USAGE_2` shows that the input parameter `p1` and all the fields, except for the key field `Id`, are typed with an enumerated type. ![figure](images_enum1.jpg)

## Operand Positions for CDS Elements with an Enumerated Type

CDS enumerated elements are currently available in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md), [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md) and [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md) in the following operand positions:

### CDS Enumerated Type

A CDS enumerated type `EnumType` can be used in the following places:

- To type another CDS enumerated type as described in the topic [CDS DDL - `DEFINE TYPE ENUM`](abencds_define_enum_type.md).

  **Note:** The maximum nesting depth is five. This means that a stack of enumerated types can have a maximum of five layers, from base to top-most.

- In [cast expressions in CDS view entities](abencds_cast_expression_v2.md).

- In [cast expressions in CDS projection views](abencds_proj_view_element.md).

  **Note:** Remember that casting in CDS projection views is only possible with the addition `PRESERVING TYPE`. **Example**: `cast(ProjField as MyEnumType preserving type) as NewProjField`

- For [typing](abencds_typing.md) of elements in [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md) and in [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md).

- For [typing](abencds_typing.md) of parameters in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), CDS custom entities, and CDS abstract entities

- In ABAP for typing data objects with the statement `TYPE`.

### CDS Enumerated Constant

A CDS enumerated constant can be used in the following places:

- As a CDS element in the `SELECT` list of a CDS view entity

  Syntax: `MyEnum.#EnumConstant as FieldName`

- As actual parameters for input parameters of CDS view entities and [CDS analytical queries](../../abap-glossary/abencds_analytic_query_glosry.md).

  **Note:** An enumerated constant of an enumerated type `EnumType` can be passed to an input parameter that is typed with the same CDS enumerated type `EnumType`.

- In a simple case expression in the `WHEN`, `THEN`, and `ELSE` branches. However, an enumerated constant is not valid as an operand after `CASE`.

- In a complex case expression as a right-hand operand of the `WHEN` condition and as operand after `THEN`.

- As an operand (left or right) in a [`WHERE`](abencds_where_clause_v2.md) clause in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md), and [CDS analytical query](../../abap-glossary/abencds_analytic_query_glosry.md).

- In a [path filter](abencds_path_expression_filter_v2.md) of a path expression as left-hand operand.

- In ABAP for value assignments and in comparisons as described in topic [Enumerated Objects (enum)](../../abap-programming-language/abap-processing-internal-data/abenenumerated_types_usage.md).

### CDS Enumerated Element

A CDS enumerated element can be used in the following places:

- As an element in the `SELECT` list of a CDS entity.

- As an element in the projection list of a [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md).

- In a simple case expression of a CDS view entity.

- In a complex case expression of a CDS view entity.

- In a reuse expression using `$projection` in the `SELECT` list of a CDS view entity and a CDS analytical query.

- As an operand (left or right) of a `WHERE` clause in a CDS entity.

- As a field of the [`GROUP BY`](abencds_group_by_v2.md) clause of a CDS entity.

- As an operand of a [`HAVING`](abencds_having_clause_v2.md) clause in a CDS entity.

- As an operand of an association `ON` condition of a CDS association and of a to-parent association in a CDS view entity, CDS abstract entity and CDS transactional query.

- As an operand of a join `ON` condition of a join between two data sources in a CDS view entity.

- In a default filter condition of a CDS association, defined using [`WITH DEFAULT FILTER`](abencds_simple_association_v2.md).

- In a path filter of a path expression as left or right-hand operand.

- In ABAP for value assignments and in comparisons as described in topic [Enumerated Objects (enum)](../../abap-programming-language/abap-processing-internal-data/abenenumerated_types_usage.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity defines a `WHERE` condition with the CDS enumerated element `WEEKDAY` and the parameter `P_WEEKDAY`. The parameter is also typed with a CDS enumerated type.

``` abap
@AbapCatalog.viewEnhancementCategory: [#NONE]
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, enum'

define view entity DEMO_CDS_ENUM_3
  with parameters
    p_weekday : DEMO_CDS_ENUM_WEEKDAY
  as select from DEMO_CDS_ENUM_1
{
  key carrid,
  key connid,
  key fldate,
      weekday
}
where
  weekday = $parameters.p_weekday
```

The following code snippet accesses the view entity displayed above, passes an actual parameter to the input parameter `P_WEEKDAY`, and displays the result.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
FROM demo_cds_enum_3( p_weekday = @demo_cds_enum_weekday-fri ) 
INTO TABLE @DATA(result). 
 
out->write( result ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet defines an enumerated variable with reference to a CDS enumerated type in ABAP. It assigns an enumerated constant from the same enumerated type to the variable.

``` abap
DATA wd_cds  TYPE demo_cds_enum_weekday. 
 
wd_cds = demo_cds_enum_weekday-tue.
```

## Simple Case Expressions

CDS enumerated elements can be used in [simple case expressions](abencds_simple_case_expression_v2.md) in CDS entities. The following rules apply:

- The operand after `CASE` must be a CDS enumerated element. CDS enumerated constants and CDS enumerated types are not possible.

- The operands after `WHEN`, `THEN`, and `ELSE` can be CDS fields with an enumerated data type or CDS enumerated constants.

- The operands after `CASE` and `WHEN` must have the same CDS enumerated type and the operands after `THEN` and `ELSE` must also have the same CDS enumerated type.

## Cast Expressions

When [casting](abencds_cast_expression_v2.md) to a CDS enumerated type, the operand of the cast expression must be compatible with the base type of the CDS enumerated type. The [cast matrix](abencds_cast_expression_v2.md) and the [conversion rules](abencds_cast_expression_rules_v2.md) for casting apply with respect to the base type.

If the addition `PRESERVING TYPE` is specified, the data type and length of the operand and the base type of the CDS enumerated type must match exactly.

## Logical Expressions

Enumerated operands can be used in logical expressions in the following clauses:

- `WHERE` clause

- `HAVING` clause

- Association `ON` condition, except in `ON` conditions in CDS custom entities.

- Join `ON` condition

- Path filter of a path expression

- Default filter condition of an association

- Complex case distinction

The following rules apply:

- CDS enumerated elements can be used as a left or right hand operand. As relational operators, comparison operators, `IS INITIAL`, and `IS NULL` are supported. The Boolean operator `NOT` is supported.

- For comparisons between operands of an enumerated data type, the rule applies that an operand can only be compared with an operand with the same enumerated type. The values of the operands are compared in accordance with their base type. An exception to this rule are type stacks. If an enumerated type is defined with reference to another CDS enumerated type, these two types are compatible with each other.

- Enumerated constants are supported as operands of a `WHERE` clause, as an operand of a complex case distinction, as an operand of a path filter, or as operand of a default filter of an association. As relational operators, comparison operators are supported. Each enumerated type has an initial enumerated value, which makes checks with the predicate expression [`IS INITIAL`](abencds_cond_expr_initial_v2.md) possible. `IS [NOT] NULL` is not supported.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS enumerated type `DEMO_CDS_ENUM_STACK` is based on the CDS enumerated type `DEMO_CDS_ENUM_WEEKDAY`. It inherits the definition and the annotations of the referenced type.

``` abap
@EndUserText.label: 'CDS enum typed with another enum' 
define type DEMO_CDS_ENUM_STACK: DEMO_CDS_ENUM_WEEKDAY
```

`DEMO_CDS_ENUM_STACK` and `DEMO_CDS_ENUM_WEEKDAY` are compatible with each other and can be used in comparisons. Example:

``` abap
IF demo_cds_enum_stack-mon = demo_cds_enum_weekday-fri. ENDIF.
```

## Parameter Passing

Input parameters that are typed with a CDS enumerated type can have the following actual parameters:

- A CDS enumerated constant of the same CDS enumerated type.

- An input parameter that is typed with the same CDS enumerated type.

## Type Descriptions

In [RTTS](../../abap-glossary/abenrun_time_type_services_glosry.md), enumerated operands are described by objects of the class `CL_ABAP_ENUMDESCR`. This class can be used for [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) and [RTTC](../../abap-glossary/abenrun_time_type_creation_glosry.md) purposes. Like any enumerated type, an enumerated type created using RTTC is only compatible with itself.

The following attributes exist in a type description of the class `CL_ABAP_ENUMDESCR`:

- `KIND` always has the value *E* for the elementary base type.

- `TYPE_KIND` always has the value *k*.

- `BASE_TYPE_KIND` describes the base type.

- `MEMBERS` is a table of the enumerated constants and the associated enumerated values.

### Executable Example

[Enumerated Elements, Type Description](abencds_enum_description_abexa.md)

## Restrictions

- CDS enumerated types cannot be used in [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- CDS enumerated types cannot be used for typing in DDIC objects such as [DDIC data types](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_types.md), DDIC views, and [DDIC extensions](../../abap-glossary/abenddic_extension_glosry.md).

### Hints

- An enumerated type is always an elementary data type. Likewise, the associated type description class `CL_ABAP_ENUMDESCR` is a subclass of `CL_ABAP_ELEMDESCR`.

- The base type describes how each enumerated value of the value set is stored internally, but it is not the type of the associated enumerated constant that can be used in a program. Its type is the enumerated type `ENUM` itself.
