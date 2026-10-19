---
title: "DDIC - Data Class of Database Tables"
source_file: abenddic_database_tables_dat_type.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Technical Properties of Database Tables > DDIC - Table-Specific Technical Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Data Class of Database Tables

For the database platform Oracle, the data class determines the physical area (tablespace) of the database in which a DDIC database table is created. For other database platforms, the data class does not have any effect and is ignored. The most important data classes for application data are:

- **APPL0 (master data)**

  Data that is rarely changed. One example of master data is data in a table of addresses, such as names, postal addresses, and telephone numbers.

- **APPL1 (transaction data)**

  Data that is frequently changed. One example of transaction data is warehouse stock that changes each time an order is placed.

- **APPL2 (organizational data)**

  Customizing data specified when the system is configured and then changed only rarely. One example is the table `T005` that contains the country codes.

- **USR and USR1 (customer data)**

  DDIC database tables for customer developments in a separate tablespace.

There are further data classes for system tables used internally by runtime frameworks, such as SDIC for ABAP Dictionary tables.
