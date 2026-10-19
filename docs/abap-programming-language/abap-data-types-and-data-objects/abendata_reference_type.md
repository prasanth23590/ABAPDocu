---
title: "Data References"
source_file: abendata_reference_type.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > References"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Data References

Data references can point to any data objects or to their parts (components, lines of internal tables, or subareas determined by offset or length specifications). The static type of their reference variables is either the built-in generic type `data` or any non-generic data type. Data reference variables can be used with the instance operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) for static and in the statement [`CREATE DATA`](../abap-creating-objects-and-values/abapcreate_data.md) for dynamic creation of data objects. The statement [`GET REFERENCE`](../abap-processing-internal-data/abapget_reference.md) and the reference operator [`REF`](../abap-processing-internal-data/abenconstructor_expression_ref.md) can be used to write references to existing data objects in data reference variables. When internal tables are processed, most statements have the addition [`REFERENCE INTO`](../abap-processing-internal-data/abapread_table_outdesc.md), to set references to table lines.

The [dereferencing operator](../../abap-glossary/abendereferencing_operat_glosry.md) [`->*`](../abap-operands/abendereferencing_operator.md) is used to access the data object to which a data reference points.

Data references can be [heap references](../../abap-glossary/abenheap_reference_glosry.md) or [stack references](../../abap-glossary/abenstack_reference_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Inline declaration of a data reference variable `dref` with the static type `scarr` on the left side of a corresponding anonymous data object created on the [heap](../../abap-glossary/abenheap_reference_glosry.md). Uses the dereferencing operator `->*` to access the entire data object and the object component selector `->` to access a component.

``` abap
FINAL(dref) = NEW scarr( ). 
 
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = 'LH' 
       INTO @dref->*. 
 
cl_demo_output=>display_data( dref->carrid ).
```
