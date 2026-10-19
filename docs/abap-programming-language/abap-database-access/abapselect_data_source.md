---
title: "SELECT, FROM data_source"
source_file: abapselect_data_source.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM data_source

## Syntax

``` abap
... { dbtab  [WITH PRIVILEGED ACCESS]   
   | cds_entity[sql_para][sql_path] 
                        |{[PROVIDED BY logical_external_schema] 
                          [WITH PRIVILEGED ACCESS]}   
   | +cte[sql_path]   
   | hierarchy_data   
   | @itab }   
   [ declare_client ] ...  
```

[`sql_para`](abenabap_sql_parameters.md) · [`sql_path`](abenabap_sql_path.md) · [`sql_path`](abenabap_sql_path.md) · [`hierarchy_data`](abenselect_hierarchy_data.md) · [`@itab`](abapselect_itab.md) · [`declare_client`](abapselect_declare_client.md)

### Alternative

[1. `... dbtab [WITH PRIVILEGED ACCESS]`](abapselect_data_source.md#alternative-1)

[2. `... cds_entity[sql_para][sql_path]|{[PROVIDED BY ...] [WITH PRIVILEGED ACCESS]}`](abapselect_data_source.md#alternative-2)

[3. `... +cte[sql_path]`](abapselect_data_source.md#alternative-3)

[4. `... hierarchy_data`](abapselect_data_source.md#alternative-4)

[5. `... @itab`](abapselect_data_source.md#alternative-5)

## Overview

### Description

Specifies an individual [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) `dbtab`, a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md) `cds_entity`, a common [table expression](../../abap-glossary/abencommon_table_expression_glosry.md) `+cte`, [hierarchy data](abenselect_hierarchy_data.md), an [internal table](../../abap-glossary/abeninternal_table_glosry.md) [`@itab`](abapselect_itab.md), or a [CDS system entity](../../abap-glossary/abencds_system_entity_glosry.md) in the [`FROM`](abapfrom_clause.md) clause of a [query](../../abap-glossary/abenasql_query_glosry.md).

With the addition [`declare_client`](abapselect_declare_client.md), a [client column](../../abap-glossary/abenclient_column_glosry.md) can be declared temporarily for a data source that is client-independent otherwise.

**Note:** Regarding views, there is the restriction that only those whose key fields are located together at the beginning of the view can be accessed.

## Alternative 1

`... dbtab [WITH PRIVILEGED ACCESS]`

### Addition

[`... WITH PRIVILEGED ACCESS`](abapselect_data_source.md#addition)

### Description

Specifies a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) `dbtab`.

### Hints

- The [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) must be specified using the exact name defined for it. More specifically, no name for the [database schema](../../abap-glossary/abendatabase_schema_glosry.md) can be prefixed. An ABAP SQL statement always accesses the database schema assigned to the current [database user name](../../abap-glossary/abendatabase_user_name_glosry.md). In cases where the [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md) or a [service connection](../../abap-glossary/abenservice_connection_glosry.md) is used, this is the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the data of the CDS view entity `DEMO_CDS_SCARR_SPFLI_VE`.

``` abap
SELECT * 
       FROM demo_cds_scarr_spfli_ve 
       ORDER BY id, carrier, flight, departure, destination 
       INTO TABLE @FINAL(result).
```

## Addition

`... WITH PRIVILEGED ACCESS`

### Description

The addition `WITH PRIVILEGED ACCESS` is currently ignored by DDIC database tables.

### Hints

- If [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) is implemented for DDIC database tables and DDIC views in a future release, the addition `WITH PRIVILEGED ACCESS` will turn it off.

## Alternative 2

`... cds_entity[sql_para][sql_path]|{[PROVIDED BY ...] [WITH PRIVILEGED ACCESS]}`

### Addition

[1. `... sql_path`](abapselect_data_source.md#addition-1)

[2. `... PROVIDED BY logical_external_schema`](abapselect_data_source.md#addition-2)

[3. `... WITH PRIVILEGED ACCESS`](abapselect_data_source.md#addition-3)

### Description

Specifies a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md) `cds_entity` created with the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md).

The CDS entity `cds_entity` is specified using its name defined after the respective [`DEFINE`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_ddl_syntax.md) statement of the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md).

- If the CDS entity has input parameters, actual parameters must be assigned to them in a parenthesized list [`sql_para`](abenabap_sql_parameters.md).

- A path expression [`sql_path`](abenabap_sql_path.md) can be specified for CDS views or CDS hierarchies with [CDS associations](../../abap-glossary/abencds_association_glosry.md). This expression defines its [association target](../../abap-glossary/abenassociation_target_glosry.md) as a data source of the `SELECT` statement.

CDS hierarchies are handled like [ABAP SQL hierarchies](../../abap-glossary/abensql_hierarchy_glosry.md) and special [rules](abenselect_hierarchy.md) apply.

### Hints

- [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md) cannot be accessed in ABAP SQL.

- There are special [CDS system entities](../../abap-core-data-services-abap-cds/abap-cds-system-entities/abencds_system_entities.md) for usage in ABAP SQL and in ABAP CDS that contain general functionality for generating tabular data.

- By default, [data aging](../../abap-glossary/abendata_aging_glosry.md) is respected when an [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) is accessed, and only current data is read. This default setting can be changed using various methods.

- If a [CDS role](../../abap-glossary/abencds_role_glosry.md) is defined for the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) and [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) is not disabled using the value *\#NOT_ALLOWED* for the annotation `@AccessControl.authorizationCheck` or using the addition `WITH PRIVILEGED ACCESS` or [`PRIVILEGED ACCESS`](abapselect_privileged_access.md), [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) is applied to `SELECT` statements and only data that matches the [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) is read. If no data is read due CDS access control, `sy-subrc` is set to 4 as usual. When a [CDS-managed DDIC view](../../abap-glossary/abencds_mngdddic_view_glosry.md) is accessed, no implicit access control takes place.

- CDS table functions and CDS hierarchies cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). An ABAP SQL statement that accesses a CDS table function bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads the data of the CDS view `DEMO_CDS_SCARR_SPFLI`.

``` abap
SELECT * 
       FROM demo_cds_scarr_spfli 
       ORDER BY id, carrier, flight, departure, destination 
       INTO TABLE @FINAL(result).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code demonstrates the creation of a series of numbers using the [CDS system table function](../../abap-glossary/abencds_system_tabfunc_glosry.md) `SERIES_GENERATE_INTEGER`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * FROM series_generate_integer( step       = 2, 
                                       from_value = 1, 
                                       to_value   = 10 ) 
  ORDER BY element_number 
  INTO TABLE @FINAL(integer_series_gen). 
 
out->write( integer_series_gen ). 
 
out->display( ).
```

## Addition 1

`... sql_path`

### Description

Specifies a path expression [`sql_path`](abenabap_sql_path.md) after a CDS entity. In this case, the entity must be a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md), [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) (deprecated), or a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) that exposes the first [CDS association](../../abap-glossary/abencds_association_glosry.md) of the path expression in its `SELECT` list or element list. A CDS view must be specified using its name `cds_entity` defined after [`DEFINE VIEW`](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_define_view_v1.md). All [CDS associations](../../abap-glossary/abencds_association_glosry.md) of the path expression must be exposed in the `SELECT` lists of the CDS entities involved for use from outside.

The [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association of the path expression is the data source of the current `SELECT` statement. The data is read in accordance with the join conditions of the CDS associations and the other conditions of the CDS views involved.

The path expression exposes only the elements of its [association target](../../abap-glossary/abenassociation_target_glosry.md) in the `SELECT` statement. If an element of this type is used as a [column specification](abenabap_sql_columns.md) in other clauses of the `SELECT` statement and the column is assigned to the data source using the column selector `~`, an alias name must be defined and used here using [`AS`](abapfrom_clause.md). Each path expression in the data source of the `FROM` clause must have an alias name defined with [`AS`](abapfrom_clause.md).

### Hints

- A CDS entity `cds_entity` with a path expression can be used in [join expressions](abapselect_join.md), like any other data source.

- In the `SELECT` statement, it is not possible to access elements of the entities of the path expression that are in front of the [association target](../../abap-glossary/abenassociation_target_glosry.md). This applies more specifically to the elements of the specified entity `cds_entity`. Regular access to these elements is possible only if they are specified again as data sources of explicit join expressions in the statement.

- A path expression cannot contain CDS associations of a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Accesses the CDS view `DEMO_CDS_ASSOC_SAIRPORT_TZ` with parameter passing and a path expression with the CDS associations `\_spfli` and `\_scarr` in the `FROM` clause.

``` abap
SELECT FROM demo_cds_assoc_sairport_tz( tz = 'UTC+1' ) 
            \_spfli 
            \_scarr[ currcode = 'EUR' ] 
            AS scarr 
       FIELDS carrname 
       ORDER BY carrname 
       INTO TABLE @FINAL(result).
```

### Executable Example

[Path Expressions, Use in the `FROM` Clause](abenpath_expr_in_from_clause_abexa.md)

## Addition 2

`... PROVIDED BY logical_external_schema`

### Description

The addition `PROVIDED BY` specifies a [logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md) that maps a [dynamic external entity](../../abap-glossary/abencds_dynamic_ee_glosry.md) to an external system.

The addition `PROVIDED BY` cannot be specified together with a path expression `sql_path` in the `FROM` clause or with the addition [`CONNECTION`](abapselect_connection.md).

## Addition 3

`... WITH PRIVILEGED ACCESS`

### Description

The addition `WITH PRIVILEGED ACCESS` disables [CDS access control](../../abap-glossary/abencds_access_control_glosry.md).

When a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) is accessed to which a [CDS role](../../abap-glossary/abencds_role_glosry.md) is assigned, its [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) are not evaluated.

The addition `WITH PRIVILEGED ACCESS` cannot be specified together with a path expression `sql_path` in the `FROM` clause. It affects only the CDS entity for which it is specified. It does not affect the CDS entities exposed using CDS associations of the specified CDS entity.

The addition `WITH PRIVILEGED ACCESS` of the `FROM` clause cannot be used together with the addition [`PRIVILEGED ACCESS`](abapselect_privileged_access.md) that affects the complete `SELECT` statement.

### Hints

- The addition `WITH PRIVILEGED ACCESS` overrides all delivered and user-defined roles.

- CDS access control can also be disabled using the annotation `@AccessControl.authorizationCheck:#NOT_ALLOWED` when a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md) is defined.

- If the addition `WITH PRIVILEGED ACCESS` is specified together with a path expression `sql_path` in a [column specification](abenabap_sql_columns.md), a syntax warning occurs because it does only affect the source of the path. The addition [`PRIVILEGED ACCESS`](abapselect_privileged_access.md) can be used to modify the complete `SELECT` statement.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the addition `WITH PRIVILEGED ACCESS` when the CDS view `DEMO_CDS_AUTHORITY_LITERAL_2` is accessed, which is linked with the following CDS role:

``` abap
CDS or DDIC source code was not found
```

Unlike the class `CL_DEMO_CDS_AUTH_LITERAL`, the following read reads all data of the view.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM demo_cds_authority_literal_2 WITH PRIVILEGED ACCESS 
       ORDER BY carrid 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

## Alternative 3

`... +cte[sql_path]`

### Addition

[`... sql_path`](abapselect_data_source.md#addition-1)

### Description

Specifies a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) `cte` in a subquery or the closing [main query](../../abap-glossary/abenmainquery_glosry.md) of a [`WITH`](abapwith.md) statement.

The `SELECT` statement accesses the result set of the common table expression. All common table expressions can be used that were defined in the same `WITH` statement in front of the current `SELECT` statement.

### Hint

If a common table expression is used as the data source, a temporary database table is accessed, which is available during the `WITH` statement.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Access to the result set of the common table expression `+carriers` in a join expression of the `FROM` clause of the main query of the statement [`WITH`](abapwith.md).

``` abap
WITH +carriers AS ( 
  SELECT carrid, carrname 
         FROM scarr ) 
  SELECT FROM +carriers 
           INNER JOIN spfli 
             ON +carriers~carrid = spfli~carrid 
         FIELDS +carriers~carrname, 
                spfli~connid, 
                spfli~cityfrom, 
                spfli~cityto 
         WHERE spfli~carrid = 'LH' 
         INTO TABLE @FINAL(result).
```

## Addition

`... sql_path`

### Description

Specifies a path expression [`sql_path`](abenabap_sql_path.md) after a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) `+cte` that is specified as the data source of a query in a [`WITH`](abapwith.md) statement. The common table expression must expose the first association of the path expression with the addition [`WITH ASSOCIATIONS`](abapwith_associations.md). The association can be a [CDS association](../../abap-glossary/abencds_association_glosry.md) or a [CTE association](../../abap-glossary/abencte_association_glosry.md).

The same rules apply as when specifying a path expression after a CDS entity `cds_entity` that is specified as a data source. In particular, the path expression must have an alias name defined with [`AS`](abapfrom_clause.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The [association target](../../abap-glossary/abenassociation_target_glosry.md) of the path expression `\_scarr` exposed by the common table expression `+cte` is used as the data source of the [main query](../../abap-glossary/abenmainquery_glosry.md) of a [`WITH`](abapwith.md) statement.

``` abap
WITH 
  +cte AS ( SELECT * 
                   FROM demo_cds_assoc_spfli_scarr ) 
             WITH ASSOCIATIONS ( \_scarr ) 
  SELECT carrid, carrname 
         FROM +cte\_scarr AS scarr 
         INTO TABLE @FINAL(result).
```

## Alternative 4

`... hierarchy_data`

### Description

Specifies the following [hierarchy data](abenselect_hierarchy_data.md):

- An [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md)

- A [hierarchy navigator](../../abap-glossary/abenhierarchy_navigator_glosry.md) [`hierarchy_navigator`](abenselect_hierarchy_data.md) that accesses an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Access to an SQL hierarchy as a data source created by the hierarchy generator [`HIERARCHY`](abenselect_hierarchy_generator.md).

``` abap
SELECT hierarchy~*, hierarchy_level 
       FROM HIERARCHY( SOURCE demo_cds_parent_child_source 
                       CHILD TO PARENT ASSOCIATION _relat 
                       START WHERE id = 'A' 
                       MULTIPLE PARENTS ALLOWED ) AS hierarchy 
       INTO TABLE @FINAL(result).
```

## Alternative 5

`... @itab`

### Description

Specifies an internal table [`@itab`](abapselect_itab.md) as a [host variable](abenabap_sql_host_variables.md) whose name `itab` must be prefixed with the `@` character. For more information, see [`SELECT - FROM @itab`](abapselect_itab.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Using `SELECT` to access an internal table as an alternative to the statement [`READ TABLE`](../abap-processing-internal-data/abapread_table.md). Unlike `READ TABLE`, the statement `SELECT` offers a (dynamic) `WHERE` condition and evaluates the field list for the [inline declaration](../../abap-glossary/abeninline_declaration_glosry.md). The statement is executed on the AS ABAP and the data in the internal table is not transported to the database.

``` abap
DATA itab TYPE TABLE OF scarr WITH EMPTY KEY. 
 
... 
 
DATA cond TYPE string. 
 
... 
 
SELECT SINGLE 
       FROM @itab AS carriers 
       FIELDS carrid, carrname 
       WHERE (cond) 
       INTO @FINAL(wa).
```
