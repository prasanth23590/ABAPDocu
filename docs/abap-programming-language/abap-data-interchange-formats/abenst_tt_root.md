---
title: "ST - tt:root, Data Roots"
source_file: abenst_tt_root.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Structure of ST Programs > ST - Data Declarations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:root, Data Roots

## Syntax

``` abap
<tt:root name="..." [[line-]type="..." 
                    [length="..."] 
                    [decimals="..."]] 
                    [...] />  
```

## Description

To be able to access ABAP data, an ST program must contain at least one declaration of a data root outside a template. The data roots are the interfaces of the ST program to the ABAP data objects, specified in the statement [`CALL TRANSFORMATION`](abapcall_transformation.md) as source or target fields. Data roots are defined using the statement `tt:root`. A name must be assigned to the data root with the `name` attribute. It can be typed with the attribute `[line-]type`.

The data roots declared on the [`tt:transform`](abenst_tt_transform.md) level form the context of the [main template](abenst_tt_template_main.md) and can be addressed directly within it. The data roots are not recognized in [subtemplates](abenst_tt_template_sub.md). However, they can be bound to the local data roots of subtemplates when these templates are [called](abenst_tt_apply.md).

## Hint

An ST program that does not contain a data root describes a constant XML fragment that does not access ABAP data. In the statement `CALL TRANSFORMATION`, the syntax requires source fields or target fields to be specified. Data objects specified when ST programs are called without data roots are ignored in serializations and not changed in deserializations. The example for [literal texts](abenst_tt_text.md) uses ST programs without data roots.

## Data Root Name

The attribute `name` is used to declare a symbolic name that can be bound to an ABAP data object. This binding is achieved by assigning these names as `bni` to the data object `ei` in serializations or to `fi` in deserializations in the statement [`CALL TRANSFORMATION`](abapcall_transformation.md).

The symbolic name is not case-sensitive and must be unique. The namespace also includes the data roots declared using [`tt:parameter`](abenst_tt_parameter.md) and the parameters declared using [`tt:variable`](abenst_tt_variable.md). No data roots other than the ones specified here can be used in the statement `CALL TRANSFORMATION`.

## Typing the Data Root

The data root can be typed with a data type using the attribute `type` or `line-type` of `tt:root`. Whereas `type` directly specifies the type, `line-type` means that it is an internal table of the named type.

For data roots without explicit typing, no checks are made until the transformation is executed. Explicit typing is used to check the ST program statically. Examples of invalid operations that can be recognized by the compiler are:

- Access to a nonexistent structure component

- Loop across a non-table-like node

- Handling a structured node as elementary

Elementary ABAP types, types from the repository, and types of the same ST program that are defined using [`tt:type`](abenst_tt_type.md) can be specified as the value of `[line-]type`. The same restrictions apply to the type specifications as to the type statement [`tt:value`](abenst_tt_type.md).

## Accessing a Data Root

Access to a data root is described under [Addressing the Data Roots](abenst_addressing_root_node.md). [Serializations and deserializations](abenst_serial_deserial.md) are subject to the general restriction that the content of a data root cannot be modified by serialization and only writes can be performed on a data root in deserializations.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Six data roots including typing are declared in the following transformation. The data root `R1` has the elementary ABAP type `d`, `R2` has the type *internal table with elementary line type `i`*, `R3` has the type `SCARR` from the ABAP Dictionary, `R4` has the type `ABAP_BOOL` from the type pool `ABAP`, and `R5` is a table of line type `TYP` defined in the global class `CL_DEMO_ABAP_DOC`. The type of `R6` is defined as the name `STRUCT` in the transformation itself.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates" 
  xmlns:ddic="http://www.sap.com/abapxml/types/dictionary" 
  xmlns:tp="http://www.sap.com/abapxml/types/type-pool/ABAP" 
  xmlns:cl= 
    "http://www.sap.com/abapxml/types/class-pool/CL_DEMO_ABAP_DOC" 
  xmlns:def="http://www.sap.com/abapxml/types/defined" > 
  <tt:type name="STRUCT"> 
    <tt:node name="C1" type="I"/> 
    <tt:node name="C2" type="I"/> 
  </tt:type> 
  <tt:root name="R1" type="D"/> 
  <tt:root name="R2" line-type="I"/> 
  <tt:root name="R3" type="ddic:SCARR"/> 
  <tt:root name="R4" type="tp:ABAP_BOOL"/> 
  <tt:root name="R5" line-type="cl:TYP"/> 
  <tt:root name="R6" type="def:STRUCT"/> 
</tt:transform>
```
