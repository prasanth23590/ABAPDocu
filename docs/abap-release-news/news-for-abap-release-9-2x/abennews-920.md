---
title: "News for ABAP Release 9.20"
source_file: abennews-920.html
section: "ABAP Release News > News for ABAP Release 9.2x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 9.20

The kernel release for ABAP release 9.20 is 9.20.

## ABAP CDS

| Modification                          | Description                                                                                                                                                                                                                                                                       |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **External Entities: Default Values** | The keyword `DEFAULT` is supported for elements in [CDS external entities](../../abap-glossary/abencds_external_entity_glosry.md). `DEFAULT` can be used to specify a default value for an element. The default value is returned when there is no matching element name in the remote data source. |

## Data Types

| Modification                  | Description                                                                                                                                                                                                                                             |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Typing Generic Structures** | The syntax [`TYPE ANY STRUCTURE`](../../abap-programming-language/abap-declarations/abapany_structure.md) allows fully generic structured types to be created. The syntax [`TYPE ANY STRUCTURE CONTAINING`](../../abap-programming-language/abap-declarations/abapany_structure_containing.md) allows partially generic structured types to be created. |

## Transformations

| Modification                                         | Description                                                                                                                                                                                            |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New Options for `CALL TRANSFORMATION` Statements** | New options are available for `CALL TRANSFORMATION` statements: `name_handling` to handle camel case elements and attribute names and `name_escaping` to escape names of elements and attribute names. |
