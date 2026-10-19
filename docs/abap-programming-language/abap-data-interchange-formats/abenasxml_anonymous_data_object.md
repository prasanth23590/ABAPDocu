---
title: "asXML - Anonymous Data Objects"
source_file: abenasxml_anonymous_data_object.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types > asXML - Mapping of Reference Variables and Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Anonymous Data Objects

An anonymous data object, that is, a data object created using `CREATE DATA` or the instance operator `NEW`, is represented as a subelement of `heap` in the form:

``` abap
<asx:heap xmlns:nspace ...> 
  <type id = "key" attr="...">...</type> 
</asx:heap>
```

The value of such a subelement is represented in the asXML representation for named data objects or for reference variables. If the anonymous data object itself is a non-initial reference variable, according to the rules above, it references another element of `heap`. Element name `type` is the data type of the data object (or the dynamic type of the reference variables) that is specified as the XML schema type name from namespace `nspace` (see table below), whereby attributes `attr` specify technical properties of the type if necessary. The mandatory attribute `id` contains the unique key `key` of the element used to reference it by the representation of the corresponding reference variables in `values` or `heap`.

The XML schema type name is constructed according to the following hierarchy:

1.  If the data type of the data object is defined in the ABAP Dictionary, the XML schema type name is the name of the data type from the ABAP Dictionary in the corresponding namespace (see table below).

2.  If the data type is an elementary ABAP type, the XML schema type name is specified in the table below.

3.  If the data type is defined as a component of a global or local class or of an interface, the XML schema type name is composed of the name of the class or the interface and the name of the data type, separated by a period (.). The corresponding namespace (see table below) indicates whether the data type is defined as a component of a global class, a local class, or an interface.

4.  If the data type is a generic reference type that is defined with `REF TO data` or `REF TO object`, the XML schema type name is `refData` or `refObject`. Both have the namespace `http://www.sap.com/abapxml/types/built-in`.

5.  Otherwise, the XML schema type name is the name of a data type defined using `TYPES`. Here, the associated namespace (see table below) indicates where the data type is defined.

A prerequisite for the construction of an XML schema type name is that the data type of the data object has a statically usable name. If the data type only exists as a property of a data object and therefore only has one [technical name](../abap-data-types-and-data-objects/abentype_names.md), an exception is raised in serializations that can be bypassed for XSLT programs by entering transformation option [`technical_types`](abapcall_transformation_options.md) for `CALL TRANSFORMATION`.

The following table shows the namespaces for the XML schema type names, where `types` in the first column stands for `http://www.sap.com/abapxml/types`. The namespaces indicate where a data type is defined. In the uppercase identifiers `PRG`, `CPOOL`, `FPOOL`, `TPOOL`, `METH`, `FUNC`, `FORM`, and `CLASS`, characters not in ranges *a* to *z*, *A* to *Z*, *0* to *9*, *\_*, or *-* are represented as *!hex(c)*, where `hex(c)` is the two-character hexadecimal representation of the ASCII codes for character *c*.

| **Namespace**                                 | **Where Defined**                                               |
|-----------------------------------------------|-----------------------------------------------------------------|
| `types/dictionary`                            | ABAP Dictionary                                                 |
| `types/program/PRG`                           | ABAP program `prg`                                              |
| `types/class-pool/CPOOL`                      | Class Pool `cpool`                                              |
| `types/type-pool/TPOOL`                       | [Type pool](../../abap-glossary/abentype_pool_glosry.md) `tpool`                  |
| `types/function-pool/FPOOL`                   | Function pool `fpool`                                           |
| `types/function/FUNC`                         | Function module `func`                                          |
| `types/method/CLASS/METH`                     | Method `meth` of a global class `class`                         |
| `types/program.method/PRG/CLASS/METH`         | Method `meth` of a local class `class` in program `prg`         |
| `types/class-pool.method/CPOOL/CLASS/METH`    | Method `meth` of a local class `class` in class pool `cpool`    |
| `types/function-pool.method/FPOOL/CLASS/METH` | Method `meth` of a local class `class` in function pool `fpool` |

The following table shows the XML schema type names for elementary ABAP types. These names differ in part from the canonical [XML schema data types](abenabap_xslt_asxml_elementary.md), since the data type of [anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md) must be specified completely. The namespaces `nspace` for the elementary ABAP types of anonymous data objects are either `xsd="http://www.w3.org/2001/XMLSchema"` for general schema types or `abap="http://www.sap.com/abapxml/types/built-in"` for special ABAP schema types for which technical properties must sometimes be specified.

| **ABAP Type** | **XML Schema Type Name** | **Attributes**                  |
|---------------|--------------------------|---------------------------------|
| `b`           | `xsd:unsignedByte`       | \-                              |
| `c`           | `abap:string`            | `maxLength`                     |
| `d`           | `abap:date`              | \-                              |
| `decfloat16`  | `abap:precisionDecimal`  | \-                              |
| `decfloat34`  | `abap:precisionDecimal`  | \-                              |
| `f`           | `xsd:double`             | \-                              |
| `i`           | `xsd:int`                | \-                              |
| `int8`        | `xsd:long`               | \-                              |
| `n`           | `abap:digits`            | `maxLength`                     |
| `p`           | `abap:decimal`           | `totalDigits`, `fractionDigits` |
| `s`           | `xsd:short`              | \-                              |
| `string`      | `xsd:string`             | \-                              |
| `t`           | `abap:time`              | \-                              |
| `utclong`     | `abap:dateTimeDec`       | \-                              |
| `x`           | `abap:base64Binary`      | `maxLength`                     |
| `xstring`     | `xsd:base64Binary`       | \-                              |

The attribute `maxLength` specifies the length for ABAP types of generic length. The XML schema type `abap:digits` restricts the value range of an element to digits only. For XML schema type `abap:decimal`, the length and the [number of decimal places](../../abap-glossary/abendecimal_place_glosry.md) are specified using attributes `totalDigits` and `fractionDigits`. The length `totalDigits` specifies the number of places between 1 and 31. In ABAP programs, the length for data objects of type `p` is specified in bytes and the number of [places](../../abap-glossary/abenplace_glosry.md) is calculated from `2&#x00D7;len-1`. In serializations, therefore, the value of `totalDigits` is always odd. In deserializations, an even value of `totalDigits` is increased by one implicitly.

## Executable Example

For information about the differences between serializing to `heap` and embedded elements, see [Serializations to Heap or Embedded](abenserialize_ref_heap_embed_abexa.md).
