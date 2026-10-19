---
title: "ST - data, Assertions"
source_file: abenst_data.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control > ST - tt:cond, Conditional Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - data, Assertions

## Syntax

``` abap
... data="..." ...  
```

## Description

The following assertions can be specified for the content of the `data` attribute of a [`tt:cond`](abenst_tt_cond.md) element:

| **Assertion**                                                  | **Meaning**                                                                                                        |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `initial(node)`                                                | Met if the bound ABAP data object is initial.                                                                      |
| `initial(var(variable))`                                       | Met if the variable is initial.                                                                                    |
| `dnode\|var(variable) = value`, `value = dnode\|var(variable)` | Met if the value of the connected ABAP data object or the variables corresponds to the value specified in `value`. |

The operands of the assertions can be data nodes, variables, or values.

- Data nodes `node` are specified in a [special form](abenst_addressing_nodes_in_cond.md).

- Variables are specified in the form `var(variable)`, where `variable` is a [variable](abenst_tt_variable.md) or a [parameter](abenst_tt_parameter.md).

- Values `value` are ABAP values in the associated [representation](abenst_abap_representation.md).

An assertion can be specified as a comma-separated list of multiple of the above assertions. An assertion of this type is met if all assertions in the list are met. Each data node may appear only once in the list.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The element *X* defined in `DEMO_ST_DATA1` is only considered in serializations if the ABAP data object bound to `ROOT` is 11.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <tt:s-cond data="ROOT=11"> 
      <X> 
        <tt:value ref="ROOT"/> 
      </X> 
    </tt:s-cond> 
  </tt:template> 
</tt:transform>
```

The element *X* defined in `DEMO_ST_DATA2` is only considered in serializations if the value of the ABAP data object bound to `ROOT1` is initial and the value of the ABAP data object bound to `ROOT2` is 22.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:template> 
    <tt:s-cond data="initial(ROOT1),ROOT2=22"> 
      <X> 
        ... 
      </X> 
    </tt:s-cond> 
  </tt:template> 
</tt:transform>
```
