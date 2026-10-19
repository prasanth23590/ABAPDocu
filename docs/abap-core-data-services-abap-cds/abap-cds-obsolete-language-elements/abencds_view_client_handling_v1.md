---
title: "ABAP CDS - Client Handling in CDS DDIC-Based Views"
source_file: abencds_view_client_handling_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Client Handling in CDS DDIC-Based Views

For a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) in ABAP CDS, the [CDS annotation](../../abap-glossary/abencds_annotation_glosry.md) [`@ClientHandling`](abencds_view_anno_v1.md) can be used to specify client handling.

- [Determining Client Dependency](abencds_view_client_handling_v1.md#determining-client-dependency)

- [Determining Client Handling](abencds_view_client_handling_v1.md#determining-client-handling)

- [Properties of Client-dependent CDS DDIC-based views (obsolete).](abencds_view_client_handling_v1.md#properties-of-client-dependent-cds-ddic-based-views-obsolete)

## Hint

CDS DDIC-Based Views are not [client-safe](../../abap-glossary/abenclient_safe_glosry.md) and cannot be used in the [`USING`](../../abap-programming-language/abap-database-access/abapmethod_by_db_proc.md) list of an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md).

## Determining Client Dependency

The annotation `@ClientHandling.type` determines the client dependency of the view. The following values can be specified for the annotation:

**\#INHERITED**

Default value. The client dependency of the view is determined by the [data sources](abencds_data_source_v1.md) used.

- If one of the data sources used in the view is [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md), the view is client-dependent.

- If none of the data sources used in the view is [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md), the view is a client-independent view.

**\#CLIENT_DEPENDENT**

The view is client-dependent. A prerequisite for this is that at least on of the [data sources](abencds_data_source_v1.md) used in the view is client-dependent. If not, a syntax error occurs.

**\#CLIENT_INDEPENDENT**

The view is a client-independent view. A prerequisite for this is that none of the [data sources](abencds_data_source_v1.md) used in the view is client-dependent. If not, a syntax error occurs.

### Hints

- CDS views for application data should usually be client-dependent.

- Unlike the annotation `@ClientDependent`, the annotation `@ClientHandling.type` cannot be used to make a CDS DDIC-based view (obsolete) into a client-independent view if it contains client-dependent data sources.

- If the annotation `@ClientHandling.type` is not specified, client dependency is derived implicitly from the client dependency of the data sources uses, as when specified with the value `#INHERITED`.

## Determining Client Handling

The annotation `@ClientHandling.algorithm` determines how implicit client handling is performed. The following values can be specified for the annotation:

**\#AUTOMATED**

Default value for the values \#INHERITED and \#CLIENT_DEPENDENT of the annotation @ClientHandling.type. Cannot be used together with its value \#CLIENT_INDEPENDENT.

The value \#AUTOMATED expands the joins of the [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) implicitly as shown in the following table. In the case of outer joins, client-independent sides are made into client-dependent sides artificially using cross joins, which avoids null values. This applies to joins specified directly using JOIN and to instances of joins created when using [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md).

\|**Left Side**\|**Right Side**\|`INNER JOIN`\| `LEFT OUTER JOIN`\|`RIGHT OUTER JOIN`\|`CROSS JOIN` \| \|:---\|:---\| \|Client-dependent\|Client-dependent\|Compares the client columns in the `ON` condition\|Compares the client columns in the `ON` condition\|Compares the client columns in the `ON` condition\|Transforms the cross join to an inner join using an `ON` condition for the client columns \| \|Client-independent\|Client-dependent\|`-`\|The left side is replaced by a cross join of the client-independent data source with the DDIC database table `T000` and a comparison of the client columns in the `ON` condition.\|`-`\|`-` \| \|Client-dependent\|Client-independent\|`-`\|`-`\|The right side is replaced by a cross join of the client-independent data source with the DDIC database table `T000` and the client columns are compared in the `ON` condition.\|`-` \| \|Client-independent\|Client-independent\|`-`\|`-`\|`-`\|`-`\|

**\#SESSION_VARIABLE**

Cannot be used together with the value \#CLIENT_INDEPENDENT of the annotation @ClientHandling.type.

The value \#SESSION_VARIABLE expands the joins of the [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) implicitly as shown in the following table. This applies to joins specified explicitly and directly using JOIN and to instances of joins created when using [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md).

\|**Left Side**\|**Right Side**\|`INNER JOIN`\| `LEFT OUTER JOIN`\|`RIGHT OUTER JOIN`\|`CROSS JOIN` \| \|:---\|:---\| \|Client-dependent\|Client-dependent\|Compares the client columns in the `ON` condition\|Compares the client columns in the `ON` condition\|Compares the client columns in the `ON` condition\|Transforms the cross join to an inner join using an `ON` condition for the client columns \| \|Client-independent\|Client-dependent\|`-`\|Compares the client column with the value of the [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](abencds_session_variable_v1.md) in the `ON` condition\|`-`\|`-` \| \|Client-dependent\|Client-independent\|`-`\|`-`\|Compares the client column with the value of the [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](abencds_session_variable_v1.md) in the `ON` condition\|`-` \| \|Client-independent\|Client-independent\|`-`\|`-`\|`-`\|`-`\|

In addition, when Client-dependent data tables are accessed, WHERE clauses with comparisons of the client columns with the [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](abencds_session_variable_v1.md) are added to the view implicitly. If only client-dependent CDS entities are accessed, however, no clauses are added.

If the session variable \$session.client is evaluated in the view, it is not possible to access the data of different clients in a single read. This applies in the following cases:

- When a client-dependent DDIC database table is a data source of the view or is a CDS view used as a data source and hence an implicit `WHERE` clause exists for the session variable.

- When client-dependent and client-independent sides are joined in an outer join and there is an implicit `ON` condition for the session variable.

The addition `USING` of the statement [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) for switching [implicit client handling](../../abap-programming-language/abap-database-access/abenabap_sql_client_handling.md) is allowed and the client specified here is used implicitly.

**\#NONE**

Default value for the value \#CLIENT_INDEPENDENT of the annotation @ClientHandling.type. Cannot be used together with its values INHERITED and \#CLIENT_DEPENDENT. No implicit client handling takes place.

### Hints

- If a view with the value `#INHERITED` of the annotation `@ClientHandling.type` is a client-independent view, no implicit client handling takes place and the values `#AUTOMATED` and `#SESSION_VARIABLE` are ignored.

- If no annotation `@ClientHandling.type` is specified, the annotation `@ClientHandling.algorithm` can be specified with the values `#AUTOMATED` or `#SESSION_VARIABLE` for the default value `#INHERITED`.

- If an annotation `@ClientHandling.type` is specified but an annotation `@ClientHandling.algorithm` is not specified, the value `#AUTOMATED` is set in `#INHERITED` and `#CLIENT_DEPENDENT` implicitly and the value `#NONE` is set in `#CLIENT_INDEPENDENT`, also implicitly.

- If none of the annotations is specified, the default values `#INHERITED` for `@ClientHandling.type` and `#AUTOMATED` for `@ClientHandling.algorithm` apply.

- The value `#NONE` can only be specified for views declared explicitly as client-independent views. If specified for views declared explicitly as client-dependent views using `#CLIENT_DEPENDENT`, self-programmed client handling would be required and this is not currently supported.

- The values `#AUTOMATED` and `#SESSION_VARIABLE` produce the same result when a client-dependent CDS view is used. They modify the way client handling is implemented internally, but do not modify the definition of the view or, its use. The value `#SESSION_VARIABLE` can improve performance by concentrating on a single client.

## Properties of Client-dependent CDS DDIC-based views (obsolete).

In ABAP SQL reads, the client dependency of a CDS view has the following consequences for the CDS entity and any associated [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md):

- [CDS entity](../../abap-glossary/abencds_entity_glosry.md)

  - The view fields of the CDS entity of a client-dependent CDS view do not cover a client column. A client column of a client-dependent CDS view specified explicitly in the [`SELECT` list](abencds_select_list_v1.md) is also not a component of the structured data type represented by the CDS entity and is removed implicitly from the result set of a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement.

  - If [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) is used to access a client-dependent CDS entity, the data of the [current client](../../abap-glossary/abencurrent_client_glosry.md) is read implicitly.

- [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md)

  - The view fields of a CDS-managed DDIC view (obsolete) of a client-dependent CDS view always cover a client column. This applies regardless of whether the client column is specified in the [`SELECT` list](abencds_select_list_v1.md).

  - If an obsolete access is made on the CDS-managed DDIC view (obsolete) using [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md), the view is handled in accordance with regular [implicit client handling](../../abap-programming-language/abap-database-access/abenabap_sql_client_handling.md), which itself can be defined using the addition `USING`.

  - The name of the client column of a CDS-managed DDIC view (obsolete) with activated client handling is defined in accordance with the following hierarchy: If the client column is specified in the `SELECT` list, its name or its alternative name is used. If the client column is not specified in the `SELECT` list, `MANDT` is used. If `MANDT` is already used as an (alternative) element name in the `SELECT` list, `CLIENT` is used. If neither `MANDT` or `CLIENT` is possible, a syntax error occurs.

### Executable Example

CDS Views, Client Handling
