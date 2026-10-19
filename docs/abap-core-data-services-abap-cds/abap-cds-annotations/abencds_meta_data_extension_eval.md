---
title: "ABAP CDS - Evaluation of Metadata Extensions"
source_file: abencds_meta_data_extension_eval.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations > ABAP CDS - Metadata Extensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Evaluation of Metadata Extensions

When evaluating annotations with the class `CL_DD_DDL_ANNOTATION_SERVICE`, the annotations from metadata extensions are considered first. If there are different metadata extensions for the same CDS entity, priority is determined by the following criteria:

- **Layer of metadata extension**

  The layer of a metadata extension is defined in its definition with [`ANNOTATE`](abencds_f1_annotate_view.md) by the annotation [`@Metadata.layer`](abencds_f1_metadata_ext_annos.md). These are the enumeration symbols for layers, in descending order of priority:

  - `#CUSTOMER`

  - `#PARTNER`

  - `#INDUSTRY`

  - `#LOCALIZATION`

  - `#CORE`

The methods of the class `CL_DD_DDL_ANNOTATION_SERVICE` collect the annotations they have returned, depending on the variant and the layers, according to the following hierarchy:

1.  The annotations are evaluated according to the layer defined by the annotation `@Metadata.layer`. Annotations found in a higher layer are no longer searched for in a lower layer, so any annotation that exists there is overridden.

2.  Then, the annotations of the CDS entity itself that are not found in a metadata extension are added as well. These can be annotations from the source code and inherited annotations. For annotations inherited from other CDS entities, any metadata extensions are evaluated first, according to the hierarchy described above.

If there are several metadata extensions in a layer, the annotations of the first metadata extension to be found are used. The metadata extensions are evaluated according to an undefined but stable order.
