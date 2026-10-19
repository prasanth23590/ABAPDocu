---
title: "database cursor"
source_file: abendatabase_cursor_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# database cursor

## Definition

Pointer to the result set of a database selection. The database cursor is always assigned to a line of the result set. In [ABAP SQL](abenabap_sql_glosry.md), cursor handling is implicit, except for the statements `OPEN CURSOR`, `FETCH`, and `CLOSE CURSOR`. A program can open a maximum of 17 database cursors simultaneously using the [ABAP SQL interface](abenabap_sql_interface_glosry.md).
