---
title: "ST - using, Preconditions"
source_file: abenst_using.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control > ST - tt:cond, Conditional Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - using, Preconditions

## Syntax

``` abap
... using="..." ...  
```

## Description

The following preconditions can be specified for the content of the `using` attribute of a [`tt:cond`](abenst_tt_cond.md) element:

| **Precondition** | **Meaning**                                                    |
|------------------|----------------------------------------------------------------|
| `exist(node)`    | Met if an ABAP data object is bound to the node.               |
| `type-...(node)` | Met if an ABAP data object of type `...` is bound to the node. |

For each [built-in ABAP type](../../abap-glossary/abenbuiltin_abap_type_glosry.md) there is a precondition `type-...` in which the data type is specified in uppercase letters (see examples). The operand `node` can be a data node that must be specified in a [special form](abenst_addressing_nodes_in_cond.md).

A precondition can be specified as a comma-separated list of multiple of the above preconditions. A precondition like this is met if all preconditions in the list are met. Each data node may appear only once in the list.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The element *X* that is defined in `DEMO_ST_USING1` is respected in serializations only if the ABAP data object bound to `ROOT` is of type `c`.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <tt:s-cond using="type-C(ref('ROOT'))"> 
      <X> 
        ... 
      </X> 
    </tt:s-cond> 
  </tt:template> 
</tt:transform>
```

Instead of *type-C(ref('ROOT'))*, *type-C(ROOT)* is of course also possible here.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The element *X* that is defined in `DEMO_ST_USING2` is not ignored in serializations only if the ABAP data object bound to `ROOT1` is of type `int8` and the ABAP data object bound to `ROOT2` is of type `d`.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:template> 
    <tt:s-cond using="type-INT8(ROOT1), type-D(ROOT2)"> 
      <X> 
        ... 
      </X> 
    </tt:s-cond> 
  </tt:template> 
</tt:transform>
```
