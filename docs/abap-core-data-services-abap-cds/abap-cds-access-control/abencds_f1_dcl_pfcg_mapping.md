---
title: "CDS DCL - DEFINE ROLE, Converting Field Values"
source_file: abencds_f1_dcl_pfcg_mapping.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition > CDS DCL - DEFINE ROLE, pfcg_condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, Converting Field Values

Elements of CDS entities are linked with an [authorization object](../../abap-glossary/abenauthorization_object_glosry.md) in [PFCG conditions](abencds_f1_cond_pfcg.md) in the [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). The [access condition](../../abap-glossary/abenaccess_condition_glosry.md) itself is generated from [authorizations](../../abap-glossary/abenauthorization_glosry.md) of the current user for the authorization object. Here, the value of [CDS elements](../../abap-glossary/abencds_element_glosry.md) is supplied with field values of the authorizations. The following points should be noted.

- [Invalid Values](abencds_f1_dcl_pfcg_mapping.md#invalid-values)

- [Wildcard Characters](abencds_f1_dcl_pfcg_mapping.md#wildcard-characters)

## Invalid Values

The field values of authorizations are saved as text fields with length 40. For the assignment, they must be convertible to the [data type](abencds_f1_dcl_cond_data_types.md) of the CDS elements:

- The rules for [lossless assignments](../../abap-glossary/abenlossless_assignment_glosry.md) must be followed. If this is not possible, the field value is ignored.

- If an authorization requests a pattern comparison using a wildcard character (`*`), the data type of the CDS element must be character-like.

If a field value cannot be converted, the field value is ignored.

### Hints

- Field values that are ignored are, for example, field values that are longer than the CDS element or field values with a non-numeric content for a numeric CDS element.

- If field values are ignored, CDS access control may block access completely.

- Ignored field values are not logged, which means that they cannot be known to the system administrator or to the user.

## Wildcard Characters

If a field value contains a wildcard character (`*`) as its final character, it is used to create a `LIKE` condition in which the wildcard character `*` is replaced by the SQL wildcard character `%`.

If the field value contains the SQL wildcard characters `%` and `_`, the escape character `#` is assigned to them implicitly. This means that CDS access control checks the characters `%` and `_` in field values like regular characters.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The field value `"10%*"` produces the condition `LIKE '10#%%' ESCAPE '#'`.
