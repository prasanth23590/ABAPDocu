---
title: "ST - tt:clear, Initialization"
source_file: abenst_tt_clear.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Value Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:clear, Initialization

## Syntax

``` abap
<tt:clear [ref="node"|var="variable"] />  
```

## Description

The statement `tt:clear` can be used to initialize a [data root](abenst_tt_root.md), a [variable](abenst_tt_variable.md), or a [parameter](abenst_tt_parameter.md).

`ref` or `var` are used to specify the field that is to be initialized. If no field is specified, the current node is used implicitly. The following fields are possible:

- A node `node` specified in accordance with the [addressing rules](abenst_addressing.md).

- A [variable](abenst_tt_variable.md) or a [parameter](abenst_tt_parameter.md) `variable`.

**Serialization**

In serializations, only variables (or parameters) are initialized. If a node is specified with `ref` or if the current node is specified implicitly, `tt:clear` is ignored in serializations.

**Deserialization**

In deserializations, the specified nodes or variables (or parameters) are initialized.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The transformation `DEMO_ST_CLEAR` below demonstrates an initialization:

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <tt:ref name="ROOT"> 
      <X> 
        <tt:value/> 
      </X> 
      <tt:clear/> 
    </tt:ref> 
  </tt:template> 
</tt:transform>
```

In deserializations, the initial value is assigned to the ABAP data object bound to the data root `ROOT`.
