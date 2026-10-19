---
title: "CDS DDL - DDIC-Based View, SELECT, element"
source_file: abencds_select_list_entry_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, select_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, element

## Syntax

``` abap
... { [@element_annot1] 
      [@element_annot2] 
      ... 
        [KEY]   { expose_assoc      [AS alias] } 
              | { element           [AS alias] } 
              | { path_expr.element [AS alias] } 
              | { literal            AS alias  } 
              | { parameter          AS alias  } 
              | { session_variable   AS alias  } 
              | { aggr_expr          AS alias  } 
              | { arith_expr         AS alias  } 
              | { builtin_func       AS alias  } 
              | { case_expr          AS alias  } 
              | { cast_expr          AS alias  } 
      [@<element_annot1] 
      [@<element_annot2] 
      ... } 
  | { $EXTENSION.* } ...  
```

[`@element_annot1`](abencds_element_annotations_v1.md) · [`@element_annot2`](abencds_element_annotations_v1.md) · [`expose_assoc`](abencds_select_list_association_v1.md) · [`path_expr`](abencds_path_expression_v1.md) · [`literal`](abencds_literal_v1.md) · [`parameter`](abencds_parameter_v1.md) · [`session_variable`](abencds_session_variable_v1.md) · [`aggr_expr`](abencds_aggregate_functions_v1.md) · [`arith_expr`](abencds_arithmetic_expression_v1.md) · [`builtin_func`](abencds_builtin_functions_v1.md) · [`case_expr`](abencds_case_expression_v1.md) · [`cast_expr`](abencds_cast_expression_v1.md) · [`@<element_annot1`](abencds_element_annotations_v1.md) · [`@<element_annot2`](abencds_element_annotations_v1.md)

## Overview

### Description

Defines an element of a [`SELECT` list](abencds_select_list_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The names of the elements in a `SELECT` list must be unique and they are in the same namespace as the [parameters](abencds_parameter_list_v1.md) of the view.

## Alternative 1

`... expose_assoc|element|path_expr|literal|parameter|...`

### Addition

[1. `... @element_annot ... @<element_annot`](abencds_select_list_entry_v1.md#addition-1)

[2. `... KEY`](abencds_select_list_entry_v1.md#addition-2)

[3. `... AS alias`](abencds_select_list_entry_v1.md#addition-3)

### Description

Specifies individual elements in the [`SELECT` list](abencds_select_list_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- [`expose_assoc`](abencds_select_list_association_v1.md) exposes a [CDS association](../../abap-glossary/abencds_association_glosry.md), a [CDS to-child association](../../abap-glossary/abento_child_association_glosry.md), or a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) using a [path expression](abencds_path_expression_v1.md). If a CDS association with a [filter condition](abencds_path_expression_filter_v1.md) `cds_cond` is exposed, an alternative element name `alias` with `AS` must be defined. Otherwise, an alternative element name can be defined.

- When the name `element` is specified directly, an element of a data source [`data_source`](abencds_data_source_v1.md) of the current CDS view is defined as an element. The field name can be prefixed with the name of the data source or its alternative name. The prefix is separated using a period (`.`). `AS` can be used to define an alternative element name `alias`.

- [`path_expr`](abencds_path_expression_v1.md).element specifies an element `element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association of the path expression [`path_expr`](abencds_path_expression_v1.md). The element defined in this way is part of the result set of the CDS view, a field of the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md), and a component of a type defined in ABAP with respect to the CDS view. If no alternative element name `alias` is defined, and there is no [name list](abencds_name_list_v1.md), the element name is defined by the name of the element named by the path expression.

- [`literal`](abencds_literal_v1.md) can be used to declare a literal. `AS` must be used to define an alternative element name `alias`. The literal can be prefixed with the name of a domain.

- [`parameter`](abencds_parameter_v1.md) can be used to specify a parameter from the parameter list [`parameter_list`](abencds_parameter_list_v1.md). If `AS` is used, an alternative element name `alias` must be defined, which cannot be the name `pname` of the parameter.

- [`session_variable`](abencds_session_variable_v1.md) can be used to specify a session variable. `AS` must be used to define an alternative element name `alias`.

- [`aggr_expr`](abencds_aggregate_functions_v1.md), [`arith_expr`](abencds_arithmetic_expression_v1.md), [`builtin_func`](abencds_builtin_functions_v1.md), and [`case_exp`](abencds_case_expression_v1.md) can be used to specify aggregate expressions, arithmetic expressions, calls of built-in functions, and case distinctions. The expressions and functions are evaluated by the database system when the CDS view is accessed. An alternative element name `alias` must be defined with the keyword `AS`, unless there is a [name list](abencds_name_list_v1.md).

Elements with the type `CHAR` can have a maximum of 1333 characters. Elements with the type `LRAW` or `LCHR` must be at the end of the view. Only one such element is allowed per view. Furthermore, a field of type `INT2` or `INT4` must stand directly in front of such an element, representing the maximum length of the element.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

`SELECT` list with all possible elements.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_SLIST'
define view DEMO_CDS_SELECT_LIST_V1
  with parameters
    p_delay :abap.int4
  as select from
    spfli
    association to scarr as _scarr on
      _scarr.carrid = spfli.carrid
    {
      carrid,
      _scarr.carrname,
      '...'                                   as text,
      :p_delay                                as delay,
      $session.user                           as usr,
      count( * )                              as cnt,
      fltime + :p_delay                       as fltime_delayed,
      concat(concat('"',_scarr.carrname),'"') as carrname_quoted,
      case when fltime < 60  then 'short'
           when fltime > 300 then 'long'
           else 'medium'
      end                                     as duration,
      cast(connid as int4)                    as connid_number
    }
    group by
      carrid,
      connid,
      _scarr.carrname,
      fltime
```

## Addition 1

`... @element_annot ... @<element_annot`

### Description

Specifies annotations for the element. The annotations can be specified before the element using [`@element_annot`](abencds_element_annotations_v1.md) or after the element using [`@<element_annot`](abencds_element_annotations_v1.md).

### Hints

- An annotation can be used to assign further technical and semantic properties to an element for evaluation by the ABAP runtime framework. [Framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be used to give the element specific semantic properties that are evaluated by other SAP frameworks.

## Addition 2

`... KEY`

### Description

`KEY` is used to define the current element as a key element of the current [CDS entity](../../abap-glossary/abencds_entity_glosry.md). Those elements of a [`SELECT` list](abencds_select_list_v1.md) can be defined as key elements that are placed without gaps at the start of the list. The key elements of the CDS entity are evaluated as follows if they are used as a data source of a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement in ABAP SQL:

- By the addition [`ORDER BY PRIMARY KEY`](../../abap-programming-language/abap-database-access/abaporderby_clause.md).

- In implicit [access control](../../abap-glossary/abencds_access_control_glosry.md).

  If a CDS role defined for a CDS entity is evaluated when the entity is accessed, its key elements must identify a unique row in the result set. If this is not the case, the internal instance of access control can produce duplicate entries or even incorrect results when aggregate functions are used. If a unique key cannot be determined for a CDS entity, no key element should be defined. A different instance of access control is then produced internally, which is less efficient.

Since ABAP release 7.90, the keys of the CDS entity and the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) are always identical. The CDS annotation `AbapCatalog.preserveKey` has been declared [obsolete](abencds_annotation_obsolete.md) and no longer has an effect. The ABAP runtime framework always behaves as if the annotation value `true` were used, independent from using the annotation and from the value specified there.

**Caution**

The key elements of a CDS entity do not define unique lines in its result with regard to the key. An application or framework accessing a CDS entity must expect duplicate entries for the key fields in the result set. If the lines of a result set should be unique in respect to a set of key elements, it is the task of the application or framework that provides the CDS entity to define them appropriately and to document the view accordingly.

### Hints

- For [table buffering](abencds_v1_buffering.md), the key fields of the CDS-managed DDIC view (obsolete) are always the decisive key fields.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view defines two elements as key elements:

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSKEY'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view DEMO_CDS_VIEW_KEY
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

Defines an alternative element name for the current element. The alternative element name replaces the actual name of the element from the data source [`data_source`](abencds_data_source_v1.md). The view field is created under the alternative element name in the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md). Accordingly, the alternative element name must comply with the rules for names of view fields of DDIC database views, as well as the general naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md): This means that it must also meet the following requirements:

- The naming conventions for [component names](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures_tech.md) of [DDIC structures](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md) in ABAP Dictionary

- It cannot be a reserved component name. The reserved names that cannot be used are specified in the database table `TRESE`.

This is only checked, however, if there is no explicit [name list](abencds_name_list_v1.md) that overrides the alternative element names.

Alternative element names can be used in the current CDS view to grant unique names for identically named elements from different entities of the data source. When the current CDS view is accessed, the alternative element names must be used instead of the actual name. Alternative element names cannot be used within the CDS view, with one exception: alternative element names can be specified directly or after `$projection` in the `ON` condition of a [CDS association](../../abap-glossary/abencds_association_glosry.md).

### Hint

In particular, an alternative element name cannot be used as the operand of an [expression](abencds_operands_and_expr_v1.md).

## Alternative 2

`... $EXTENSION.*`

### Description

Specifies all elements of an extension in the extension concept for dictionary objects. If specified, `$EXTENSION.*` inserts (in this place) all fields of all customizing includes, append structures, and DDIC append views that exist in the current system for the DDIC database tables and which occur as a data source [`data_source`](abencds_data_source_v1.md) in the current CDS view. `$EXTENSION.*` is ignored for CDS views used as a data source and extended using [`EXTEND VIEW`](../abap-cds-data-definitions/abencds_extend_view.md).

If specified, `$EXTENSION.*` is applied to the current CDS view only. It is not applied to other CDS views in whose data source the current CDS view is used or to CDS views in the data source of the current CDS view.

`$EXTENSION.*` cannot be specified if aggregate expressions [`aggr_expr`](abencds_aggregate_functions_v1.md) occur in the current `SELECT` list or if the current CDS view is a union set created using [`UNION`](abencds_union_v1.md).

### Hints

- `$EXTENSION.*` is specified independently of when an extension is made. It is also applied when a DDIC database table or a DDIC view is extended only after the activation of the CDS view.

- The statement [`EXTEND VIEW`](../abap-cds-data-definitions/abencds_extend_view.md) can be used to extend the current CDS view.

- If the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a CDS view extended using [`EXTEND VIEW`](../abap-cds-data-definitions/abencds_extend_view.md) is specified as a data source, `$EXTENSION.*` (id specified) includes the fields of the generated [append view](../../abap-glossary/abenddic_append_view_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The data source of the CDS view `demo_sales_order_old1` is an inner join of the DDIC database tables `snwd_bpa` and `snwd_so` and contains three directly defined elements `sales_order_id`, `business_partner_id`, and `company_name` and (because `$EXTENSION.*` is specified) all fields that exist due to extensions in the DDIC database tables `snwd_bpa` and `snwd_so`. The alternative name `partner` is defined for the database `snwd_bpa` and is used in the `ON` condition. The names of the elements `sales_order_id` and `business_partner_id` are alternative element names. The element `sales_order_id` is defined as a key element.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_SO_VW1'
define view DEMO_SALES_ORDER_OLD1 as
  select from snwd_bpa as partner
    inner join
      snwd_so on partner.node_key = snwd_so.buyer_guid
  { key so_id as sales_order_id,
        bp_id as business_partner_id,
        company_name, //from snwd_bpa
        $extension.* }
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following view accesses the CDS view `DEMO_CDS_ORIGINAL_VIEW`, which is extended in the example for [`EXTEND VIEW`](../abap-cds-data-definitions/abencds_extend_view.md). `$EXTENSION.*` is ignored, if specified.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSEXT1'
define view demo_cds_extension1
   as select from
    demo_cds_original_view
    
    {
      key carrier,
      key flight,
      $extension.*
    }
```
