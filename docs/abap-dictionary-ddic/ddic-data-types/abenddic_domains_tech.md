---
title: "DDIC - Technical Properties of Domains"
source_file: abenddic_domains_tech.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Data Elements > DDIC - Domains"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Technical Properties of Domains

The only technical property of a domain is the description of an elementary data type whose following technical properties are defined directly in the domain:

- [Built-in data type](../ddic-built-in-data-types/abenddic_builtin_types.md) in the ABAP Dictionary

- Length

- A number of decimal places (optional)

## Hint

When existing domains are modified, all users of the domain are also affected. In particular, [foreign keys](../ddic-database-tables/abenddic_database_tables_forkey.md) can become inconsistent when used for the fields of DDIC database tables, which makes [adjustments](../ddic-database-tables/abenddic_database_tables_adj.md) necessary.
