---
title: "ABAP SQL - Restrictions for Path Expressions"
source_file: abenabap_sql_path_restrictions.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Path Expressions sql_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Restrictions for Path Expressions

In principle, the same restrictions apply to path expressions in ABAP SQL and the [CDS associations](../../abap-glossary/abencds_association_glosry.md) or [CTE expressions](../../abap-glossary/abencte_association_glosry.md) used there as to using a corresponding [join expression](abapselect_join.md). For example, a path expression cannot be used together with the addition [`ORDER BY PRIMARY KEY`](abaporderby_clause.md). These restrictions are documented in the corresponding clauses. The following restrictions currently apply:

- Requirements for the CDS entities or common table expressions

  - The [association targets](../../abap-glossary/abenassociation_target_glosry.md) of the associations of a path expression cannot be DDIC database tables or DDIC database views with [replacement objects](../../abap-glossary/abenreplacement_object_glosry.md).

  - No [literals](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_literal_v1.md) with prefixed `#domain` or `:domain` can be used in the CDS associations of the path expression to check the fixed value in the value range of a domain.

  - Due to [implicit client handling](abenabap_sql_client_handling.md), no associations can be used whose `ON` condition accesses the client columns of their [association source](../../abap-glossary/abenassociation_source_glosry.md) or [association target](../../abap-glossary/abenassociation_target_glosry.md).

- Requirements for ABAP SQL

  - If a value greater than to one is defined for the [cardinality](../../abap-glossary/abencardinality_glosry.md) of an association of a path expression in the `FROM` clause, the identical path expression must also be specified in the [`SELECT` list](abapselect_list.md).

  - If the addition `CORRESPONDING` or an inline declaration [`@DATA|@FINAL(...)`](abapselect_into_target.md) is used in the [`INTO`](abapinto_clause.md) clause of a `SELECT` statement, columns of the [`SELECT` list](abapselect_list.md) specified using a path expression must have an alias name `alias` defined using [`AS`](abapselect_list.md).

  - A [data source](abapselect_data_source.md) specified as a path expression in the [`FROM` clause](abapfrom_clause.md) can be used in the `SELECT` statement only by using an alias name `tabalias` defined using `AS` in front of the column selector `~`.

  - The addition `USING CLIENT` cannot be combined with path expressions that contain [CDS associations](../../abap-glossary/abencds_association_glosry.md) or [CTE associations](../../abap-glossary/abencte_association_glosry.md) if they are [exposed](abapwith_associations_defining.md) by common table expressions.

  - If the alias name `tabalias` is specified statically using `AS` while the [`FROM` clause](abapfrom_clause.md) `source_syntax` is specified dynamically, no path expressions can be used here.

  - Path expressions cannot be used in the `ON` condition of a [join expression](abapselect_join.md).

  - In `SELECT` statements, path expressions cannot be used together with the additions [`FOR ALL ENTRIES`](abenwhere_all_entries.md) or [`WITH PRIVILEGED ACCESS`](abapselect_data_source.md).

## Hint

Fewer restrictions apply to the path expressions [`path_expr`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_path_expression_v2.md) in the [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) CDS DDL. If CDS association reads are required that are possible in ABAP CDS but not in ABAP SQL, they can be moved to a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).
