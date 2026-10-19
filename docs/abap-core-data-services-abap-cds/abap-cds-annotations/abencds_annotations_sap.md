---
title: "ABAP CDS - SAP Annotations"
source_file: abencds_annotations_sap.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - SAP Annotations

SAP annotations are [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md) created and delivered by SAP as [CDS objects](../../abap-glossary/abencds_object_glosry.md) in the form of [CDS annotation definitions](../../abap-glossary/abencds_anno_definition_glosry.md).

The annotation definitions determine the following for these objects:

- The name of the annotation

- The [annotation values](../../abap-glossary/abenannotation_value_glosry.md) that can be specified

- [Subannotations](../../abap-glossary/abensub_annotation_glosry.md) that can be specified

- [Annotation arrays](../../abap-glossary/abenannotation_array_glosry.md) that can be specified

Any SAP annotations specified in [annotation syntax](../../abap-glossary/abencds_annotation_syntax_glosry.md) in [CDS source code](../../abap-glossary/abencds_source_code_glosry.md) are evaluated by SAP.

- [ABAP CDS - ABAP Annotations](abencds_annotations_abap.md)

- [ABAP CDS - Framework-Specific Annotations](abencds_annotations_frmwrk.md)

- [ABAP CDS - SAP Annotation Documentation](abencds_annotations_ktd_docu.md)

- [ABAP CDS - Annotation Properties](abencds_sap_anno_props.md)

ABAP annotations are evaluated when the object defined in the CDS source code is activated or when the object is used in the ABAP runtime framework. Framework-specific annotations, on the other hand, are evaluated by frameworks of other software components. An ABAP annotation can also be evaluated by frameworks of other software components. Any application annotations that are not evaluated by a framework are ignored.

## Hints

- Apart from the SAP annotations delivered by SAP, no annotations should currently be specified in [CDS source code](../../abap-glossary/abencds_source_code_glosry.md).

- The program `ABAP_DOCU_CDS_ANNOS_OVERVIEW` shows all SAP annotations and their properties.
