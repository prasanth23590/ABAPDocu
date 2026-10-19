---
title: "RAP BDL - General Syntax Rules"
source_file: abenbdl_general_syntax_rules.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP BDL - Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP BDL - General Syntax Rules

The general syntax rules for the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) for defining [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) are as follows:

- Keywords

  - Keywords must be written in lowercase letters. Uppercase letters are not allowed.

- Names

  - Names are not case-sensitive.

  - A name must contain at least 1 character but no more than 30 characters.

  - A name can consist of letters, numbers, and underscores (`_`).

  - A name must start with a letter or an underscore.

  - A name of a BDEF component must be unique within the current RAP BO.

- Comments

  - Two forward slashes (`//`) introduce a comment, which continues until the end of the line.

- Separators

  - Statements can be closed using a semicolon (`;`). Sometimes this is mandatory.
