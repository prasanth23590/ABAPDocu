---
title: "ABAP CDS - Annotations"
source_file: abencds_annotations.html
section: "ABAP Core Data Services (ABAP CDS)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Annotations

A [CDS annotation](../../abap-glossary/abencds_annotation_glosry.md) enriches [CDS objects](../../abap-glossary/abencds_object_glosry.md) with metadata. It can be specified in fixed [annotation syntax](../../abap-glossary/abencds_annotation_syntax_glosry.md) for specific scopes of a [CDS](../../abap-glossary/abencds_object_glosry.md) object, namely specific places in a piece of [CDS](../../abap-glossary/abencds_source_code_glosry.md) source code.

The metadata specified by annotations is saved internally when a CDS object is activated. The system class `CL_DD_DDL_ANNOTATION_SERVICE` is used to evaluate the annotations of [CDS entities](../../abap-glossary/abencds_entity_glosry.md).

Only those annotations should be specified that have an annotation definition and the way they are specified should follow the rules in the definition. SAP delivers a set of predefined [SAP annotations](../../abap-glossary/abensap_annotation_glosry.md).

- [Specifying annotations](abencds_anno_usage.md)

- [SAP annotations](abencds_annotations_sap.md)

## Hint

Currently, only those [SAP annotations](../../abap-glossary/abensap_annotation_glosry.md) predefined by SAP should be used.

- Only those annotations should be specified in [CDS source code](../../abap-glossary/abencds_source_code_glosry.md) for which an annotation definition exists.

- Partners and customers cannot currently define their own annotations.

## More Information

For further details on annotations in ABAP CDS, see [*Annotations in ABAP CDS*](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/b22c173af13f426689e977ecff7ccf2b?version=sap_cross_product_abap) in the ABAP Data Models guide on SAP Help Portal.
