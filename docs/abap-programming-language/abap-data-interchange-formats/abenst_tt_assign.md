---
title: "ST - tt:assign, Value Assignment"
source_file: abenst_tt_assign.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Value Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:assign, Value Assignment

## Syntax

``` abap
<tt:assign [to-ref="node"|to-var="variable"] 
           [ref="node"|val="value"|var="variable"] />  
```

## Description

The statement `tt:assign` is used to assign a value to a [data root](abenst_tt_root.md), a [variable](abenst_tt_variable.md), or a [parameter](abenst_tt_parameter.md).

`to-ref` or `to-var` is used to specify the target field, and `ref`, `val`, or `var` to specify the source field. If no target field or no source field is specified, the [current node](abenst_tt_ref.md) is used implicitly. Target and source fields can be:

- a node `node` specified in accordance with the [addressing rules](abenst_addressing_nodes.md),

- a [variable](abenst_tt_variable.md) or a [parameter](abenst_tt_parameter.md) `variable`,

- a value `value` specified in accordance with the [rules for ABAP values](abenst_data.md) (source field only)

An assignment between reference variables using `tt:assign` is only possible if the static type of the source variable is more specific than or the same as the static type of the target variable (upcast). In all other cases, the [`tt:cast`](abenst_tt_cast.md) statement can be used to perform a downcast.

**Serialization**

In serializations, only variables (or parameters) are given the current value of the source field. If a data node is specified as the target field using `to-ref` or if the current node is specified implicitly, `tt:assign` is ignored in serializations.

**Deserialization**

In deserializations, only variables (or parameters) or directly specified values are evaluated as source fields. If a node is specified as the source field (using `ref`) or if the current node is specified implicitly, `tt:assign` is ignored in deserializations.

The following syntax can be used if the current node, or the node specified after `to-ref`, is an internal table:

``` abap
`<tt:assign [to-ref="itab"]> 
  <tt:assign [to-ref="comp"] 
             [val="value"|var="variable"] /> 
  ... 
</tt:assign>`
```

This will insert a line into the specified internal table. The values of the components are set using the inner statements `tt:assign`. This statement is ignored in serializations.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The transformation `DEMO_ST_ASSIGN` below shows value assignments:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:variable name="VARI" val="11"/> 
  <tt:parameter name="PARA" val="22"/> 
  <tt:template> 
    <tt:assign to-var="VARI" var="PARA"/> 
    <tt:assign to-ref="ROOT" var="VARI"/> 
  </tt:template> 
</tt:transform>
```

During a deserialization, the value *22* is assigned to the ABAP data object bound to the data root `ROOT`.
