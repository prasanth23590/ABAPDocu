---
title: "ST - check, Conditions"
source_file: abenst_check.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control > ST - tt:cond, Conditional Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - check, Conditions

## Syntax

``` abap
... [s-|d-]check ="..." ...  
```

## Description

The following conditions can be specified for the content of the `[s-|d-]check` attribute of a [`tt:cond`](abenst_tt_cond.md) or [`tt:cond-var`](abenst_tt_cond-var.md) element:

**State Queries**

| **Condition**                  | **Meaning**                                         |
|--------------------------------|-----------------------------------------------------|
| `exist(node)`                  | Met if an ABAP data object is bound to the node.    |
| `[not-]initial(node)`          | Met if the bound ABAP data object is (not) initial. |
| `[not-]initial(var(variable))` | Met if the variable is (not) initial.               |

The operands of the conditions can be data nodes, variables, or values.

- Data nodes `node` are specified in a [special form](abenst_addressing_nodes_in_cond.md).

- Variables are specified in the form `var(variable)`, where `variable` is a [variable](abenst_tt_variable.md) or a [parameter](abenst_tt_parameter.md).

- Values `value` are ABAP values in the associated [representation](abenst_abap_representation.md).

Data nodes cannot be specified as operands if `check` is specified as an attribute of [`tt:cond-var`](abenst_tt_cond-var.md).

**Comparisons**

Comparisons are specified in the form:

`node|var(variable)|value operator node|var(variable)|value`

The following operators `operator` are possible:

| **`operator`** | **Meaning**                                                                                 |
|----------------|---------------------------------------------------------------------------------------------|
| `=`            | Met if both operands have the same value.                                                   |
| `!=`           | Met if both operands do not have the same value.                                            |
| `>`, `&gt;`    | Met if the value of the left operand is greater than that of the right operand.             |
| `>=`, `&gt;=`  | Met if the value of the left operand is greater than or equal to that of the right operand. |
| `&lt;`         | Met if the value of the left operand is less than that of the right operand.                |
| `&lt;=`        | Met if the value of the left operand is less than or equal to that of the right operand.    |

## Hint

In XML, the character `<` must always be represented by `&lt;`. The character `>`, on the other hand, can be used directly or represented by `&gt;`.

### Negation, Combination, and Parentheses

Conditions `cond` can be negated using `not` and can be combined using `and` or `or`, where `and` creates a stronger link than `or`. The result of such an operation is another condition.

| **Operation**     | **Meaning**                                      |
|-------------------|--------------------------------------------------|
| `not(cond)`       | Met if `cond` is not met.                        |
| `cond1 and cond2` | Met if both `cond1` and `cond2` are met.         |
| `cond1 or cond2`  | Met if not both `cond1` and `cond2` are not met. |

Conditions can be enclosed in parentheses ( ) to change the priority.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The element *X* that is defined in `DEMO_ST_CHECK1` is respected in serializations only if the ABAP data object bound to `ROOT` is not initial.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <tt:s-cond check="not-initial(ROOT)"> 
      <X> 
        <tt:value ref="ROOT"/> 
      </X> 
    </tt:s-cond> 
  </tt:template> 
</tt:transform>
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The element *X* that is defined in `DEMO_ST_CHECK2` is respected in serializations only if the ABAP data object bound to `ROOT1` is less than or equal to the value of the ABAP data object bound to `ROOT2`. It should be noted that the data root `.ROOT2` cannot be specified directly in the condition and that `ref('.ROOT2')` must be used instead.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:template> 
    <tt:ref name="ROOT1"> 
      <tt:s-cond check="$ref &lt;= ref('.ROOT2')"> 
        <X> 
          <tt:value/> 
        </X> 
      </tt:s-cond> 
    </tt:ref> 
  </tt:template> 
</tt:transform>
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The element *X* defined in `DEMO_ST_CHECK3` is only considered in serializations if the ABAP data object bound to `ROOT1` is between the values of the ABAP data objects bound to `ROOT2` and `ROOT3`. The data roots `ROOT2` and `ROOT3` cannot be specified directly in the condition and `ref('.ROOT2')` and `ref('.ROOT3')` must be used instead.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:root name="ROOT3"/> 
  <tt:template> 
    <tt:ref name="ROOT1"> 
      <tt:s-cond check="($ref &gt; ref('.ROOT2')) and 
                        ($ref &lt; ref('.ROOT3'))"> 
        <X> 
          <tt:value/> 
        </X> 
      </tt:s-cond> 
    </tt:ref> 
  </tt:template> 
</tt:transform>
```
