---
title: "CDS DDL - CDS View Entity, SELECT, element"
source_file: abencds_select_list_entry_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, select_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, element

## Syntax

``` abap
... { [@element_annot1] 
      [@element_annot2] 
      ... 
        [KEY]   { field             [AS alias] } 
              | { include aspect    [AS alias] } 
              | { expose_assoc      [AS alias] } 
              | { path_expr.element [AS alias] } 
              | { literal            AS alias  } 
              | { parameter          AS alias  } 
              | { session_variable   AS alias  } 
              | { aggr_expr          AS alias  } 
              | { arith_expr         AS alias  } 
              | { builtin_func       AS alias  } 
              | { SQL-based scalar function 
                                     AS alias  } 
              | { reuse_exp          AS alias  } 
              | { case_expr          AS alias  } 
              | { cast_expr          AS alias  } 
              | { EnumConstant       AS alias  } 
                  ... 
    }  
```

[`@element_annot1`](abencds_element_annotations_v2.md) · [`@element_annot2`](abencds_element_annotations_v2.md) · [`field`](abencds_field_v2.md) · [`include aspect`](abencds_include_aspect.md) · [`expose_assoc`](abencds_select_list_association_v2.md) · [`path_expr`](abencds_path_expression_v2.md) · [`literal`](abencds_literal_v2.md) · [`parameter`](abencds_parameter_v2.md) · [`session_variable`](abencds_session_variable_v2.md) · [`aggr_expr`](abencds_aggregate_functions_v2.md) · [`arith_expr`](abencds_arithmetic_expression_v2.md) · [`builtin_func`](abencds_builtin_functions_v2.md) · [`SQL-based scalar function`](abencds_sql_scalar_function.md) · [`reuse_exp`](abencds_reusable_expression_v2.md) · [`case_expr`](abencds_case_expression_v2.md) · [`cast_expr`](abencds_cast_expression_v2.md) · [`EnumConstant`](abencds_enum_field_v2.md)

### Addition

[1. `... @element_annot ...`](abencds_select_list_entry_v2.md#addition-1)

[2. `... KEY`](abencds_select_list_entry_v2.md#addition-2)

[3. `... AS alias`](abencds_select_list_entry_v2.md#addition-3)

## Overview

### Description

Specifies individual elements in the [`SELECT` list](abencds_select_list_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The names of the elements in a `SELECT` list must be unique and they are in the same namespace as the [parameters](abencds_parameter_list_v2.md) of the view.

- [field](abencds_field_v2.md) defines an element of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity as an element. The field name can be prefixed with the name of the data source or its alternative name. The prefix is separated using a period (`.`). `AS` can be used to define an alternative element name `alias`.

  If the view entity makes use of multiple [data sources](abencds_data_source_v2.md) by using one or more join expressions, then all elements in the `SELECT` list **must** be prefixed with the name of their data source separated by a period (.). The prefix is required in all cases, even if the field names are unique.

- [`include aspect`](abencds_include_aspect.md) includes 1 to n elements of a [CDS aspect](abencds_ddl_aspect_glosry.md).

- [`expose_assoc`](abencds_select_list_association_v2.md) exposes a [CDS association](../../abap-glossary/abencds_association_glosry.md), a [CDS to-child association](../../abap-glossary/abento_child_association_glosry.md), or a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) using a [path expression](abencds_path_expression_v2.md). If a CDS association with a [filter condition](abencds_path_expression_filter_v2.md) `cds_cond` is exposed, an alternative element name `alias` with `AS` must be defined. Otherwise, an alternative element name can be defined.

- [`path_expr`](abencds_path_expression_v2.md).element specifies an element `element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association of the path expression [`path_expr`](abencds_path_expression_v2.md). This is referred to as [SQL path target field](../../abap-glossary/abensql_target_field_glosry.md). The element defined in this way is part of the result set of the CDS view entity and a component of a type defined in ABAP with respect to the CDS view entity. If no alternative element name `alias` is defined, the element name is defined by the name of the element named by the path expression.

- [`literal`](abencds_literal_v2.md) can be used to declare a literal. `AS` must be used to define an alternative element name `alias`.

- [`parameter`](abencds_parameter_v2.md) can be used to specify a parameter from the [`parameter list`](abencds_parameter_list_v2.md). An alternative element name using the keyword `AS` must be defined, and it cannot be the name `pname` of the parameter.

- [`session_variable`](abencds_session_variable_v2.md) can be used to specify a session variable. `AS` must be used to define an alternative element name `alias`.

- [`reuse_exp`](abencds_reusable_expression_v2.md) reuses an expression defined in the `SELECT` list in another operand position of the same CDS view entity. An alternative element name specified using `AS` is required.

- An [SQL-based scalar function](abencds_sql_scalar_function.md) can be defined as an element. An alias name is mandatory.

- [`aggr_expr`](abencds_aggregate_functions_v2.md), [`arith_expr`](abencds_arithmetic_expression_v2.md), [`builtin_func`](abencds_builtin_functions_v2.md),[`case_exp`](abencds_case_expression_v2.md), and [`cast_expr`](abencds_cast_expression_v2.md) can be used to specify aggregate expressions, arithmetic expressions, calls of built-in functions, case distinctions, and cast expressions. The expressions and functions are evaluated by the database system when the CDS view entity is accessed. An alternative element name `alias` must be defined with the keyword `AS`.

- [`EnumConstant`](abencds_enum_field_v2.md) defines an [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) as an element. An alias name is mandatory.

Elements with the type `CHAR` can have a maximum of 1333 characters. Elements with the type `LRAW` or `LCHR` must be at the end of the view. Only one such element is allowed per view. Furthermore, a field of type `INT2` or `INT4` must stand directly in front of such an element, representing the maximum length of the element.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

`SELECT` list with all possible elements.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_CDS_SALES_ORDER_VE
  with parameters
    p_delay : abap.int4
  as select from
    spfli
    association of many to one scarr as _scarr
      on _scarr.carrid = spfli.carrid
    {
      key carrid,
          _scarr.carrname,
          'abc'                                     as literal,
          $parameters.p_delay                       as parameterExample,
          $session.user_date                        as currentDate,
          count(*)                                  as cnt,
          fltime + $parameters.p_delay              as fltime_delayed,
          concat(concat('"', _scarr.carrname), '"') as carrname_quoted,
          case when fltime < 60 then 'short'
          when fltime > 60 then 'long'
          else 'medium'
          end                                       as duration,
          cast(connid as int4)                      as connid_number
    }
    group by
      carrid,
      _scarr.carrname,
      fltime,
      connid
```

## Addition 1

`... @element_annot ...`

### Description

Specifies annotations for the element. The annotations must be specified before the element using ` @element_annot`. All possible element annotations are listed in topic [element annotations](abencds_element_annotations_v2.md).

### Hints

- An annotation can be used to assign further technical and semantic properties to an element for evaluation by the ABAP runtime framework. [Framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be used to give the element specific semantic properties that are evaluated by other SAP frameworks.

## Addition 2

`... KEY`

### Description

`KEY` is used to define the current element as a key element of the current [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). All key elements must be placed without gaps at the start of the `SELECT` list.

Notes on the key elements of the CDS entity if they are used as a data source of a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement in ABAP SQL:

- Key elements are evaluated by the addition [`ORDER BY PRIMARY KEY`](../../abap-programming-language/abap-database-access/abaporderby_clause.md) and in implicit [access control](../../abap-glossary/abencds_access_control_glosry.md).

  **Note:** If a CDS role defined for a CDS entity is evaluated when the entity is accessed, its key elements must identify a unique row in the result set. If this is not the case, the internal instance of access control can produce duplicate entries or even incorrect results when aggregate functions are used. If a unique key cannot be determined for a CDS entity, no key element should be defined. A different instance of access control is then produced internally, which is less efficient.

- The key addition marks the primary key equivalent of the respective view.

- Key columns must have equivalent semantics to the primary key columns in a persistence object or writable view: they must uniquely identify records and return non-null values. For persistence objects, this is assured by data integrity constraints (creating a database primary key). In contrast, for CDS views, this must be assured by the modeling of the `SELECT` statement and underlying view and is not automatically enforced by declaring columns as keys. A violation, such as a view with keys returning duplicate records or null values in a key field, is a data integrity error. This may lead to failures, wrong or inconsistent results in consumption layers. If in doubt, use suitable select constructs (for example `DISTINCT`/`GROUP BY`, `WHERE NOT NULL`) or do not declare key columns.

- A [view entity buffer](../../abap-glossary/abencds_view_entity_b_glosry.md) requires a unique key. Records with duplicate keys might lead to unexpected buffer behavior.

Apart from that, the key elements of the CDS entity are mainly used to document the semantics of the data model. The addition `KEY` does not have any effect when the CDS view entity is activated and when other accesses are performed during program executions.

A CDS view entity without any to-child or to-parent association can be defined without any key fields.

If the CDS view entity defines any to-child or to-parent association, then it must contain at least one key field at the start of the `SELECT` list.

**Caution**

Defining key elements in a CDS view entity does not guarantee unique lines. It is the responsibility of the application or framework to define them correctly. An application framework that accesses a CDS entity may encounter duplicate entries for key fields in the result set if the views and data are poorly defined.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity defines two elements as key elements:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_VIEW_ENTITY_KEY
  as select from spfli
{
  key cityfrom,
  key cityto,
      carrid,
      connid
}
```

Since those are not the same as the key fields of the underlying database table `SPFLI`, the result set of the view can contain duplicate entries in respect to the key elements. Class `CL_DEMO_CDS_ENTITY_KEY` shows the result of an ABAP SQL access to the view. The key elements are evaluated by the addition `ORDER BY PRIMARY KEY`, but apart from that, the key elements have no effect. When trying to select into a hashed table that uses the key elements for its unique key, a runtime error will occur most probably.

## Addition 3

`... AS alias`

### Description

Defines an alternative element name for the current element. The alternative element name replaces the actual name of the element from the data source [`data_source`](abencds_data_source_v2.md). The alternative element name must comply with the general naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md): This means that it must also meet the following requirements:

- The naming conventions for [component names](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures_tech.md) of [DDIC structures](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md) in ABAP Dictionary

- It cannot be a reserved component name. The reserved names that cannot be used are specified in the database table `TRESE`.

Alternative element names can be used in the current CDS view entity to grant unique names for identically named elements from different entities of the data source. When the current CDS view entity is accessed, the alternative element names must be used instead of the actual name. Alternative element names cannot be used within the view entity, with one exception: alternative element names can be specified after `$projection` in the `ON` condition of a [CDS association](../../abap-glossary/abencds_association_glosry.md).

### Hint

In particular, an alternative element name cannot be used as the operand of an [expression](abencds_operands_and_expr_v2.md).
