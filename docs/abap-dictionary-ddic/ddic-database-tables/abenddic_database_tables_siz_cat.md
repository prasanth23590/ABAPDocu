---
title: "DDIC - Size Category of Database Tables"
source_file: abenddic_database_tables_siz_cat.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Technical Properties of Database Tables > DDIC - Table-Specific Technical Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Size Category of Database Tables

The size category affects the size of the initial memory area reserved for the table on the database. Values between 0 and 9 can be specified and intervals of expected rows are assigned to these values. The interval limits assigned to each size category depend on the structure of the DDIC database table. The range can extend from approximately 1000 rows in size category 0 to several million rows in size category 9. If the initial space reserved is exceeded, a new memory area is added implicitly in accordance with the chosen size category.

## Hints

- An appropriate size category should be chosen, to prevent too many small memory areas or a memory area that is too big.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following table shows the interval limits assigned to each size category for the DDIC database table `SPFLI`.

| **Size Category** | **Expected Rows**         |
|-------------------|---------------------------|
| 0                 | 0 to 3,600                |
| 1                 | 3,600 to 14,000           |
| 2                 | 14,000 to 58,000          |
| 3                 | 58,000 to 230,000         |
| 4                 | 230,000 to 930,000        |
| 5                 | 930,000 to 1,800,000      |
| 6                 | 1,800,000 to 3,700,000    |
| 7                 | 3,700,000 to 7,400,000    |
| 8                 | 7,400,000 to 14,000,000   |
| 9                 | 14,000,000 to 590,000,000 |
