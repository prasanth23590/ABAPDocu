---
title: "ST - tt:group, Grouping"
source_file: abenst_tt_group.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:group, Grouping

## Syntax

``` abap
<tt:group> 
  <tt:[s-|d-]cond [frq="..."] ... 
  <tt:[s-|d-]cond [frq="..."] ... 
  ... 
</tt:group>  
```

## Description

During deserializations, the statement `tt:group` can be used to react to variable XML input streams containing groups of related elements in free order. Hereby, a list of cases is specified in `tt:group`, where the syntax of each case is formulated by a conditional transformation, namely a subelement [`tt:[s-|d-]cond`](abenst_tt_cond.md). In this case, `tt:[s-]cond` defines a serialization-relevant case, and `tt:[d-]cond` a deserialization-relevant case. Other direct subelements are not possible in `tt:group`. The statement `tt:group` can be a subelement of `tt:[s-|d-]cond`.

In contrast to conditional transformations outside of `tt:group`, specifying at least one attribute [`using`](abenst_using.md), [`data`](abenst_data.md) or [`check`](abenst_check.md) for a case is not necessary, provided that the content of `tt:[s-|d-]cond` is not a [pattern](abenst_pattern.md).

In the list of cases, the following must be noted:

- Any number of serialization-relevant cases can be specified in which no attribute `using`, `data`, or `check` is specified.

- Only one deserialization-relevant case that does not contain a [pattern](abenst_pattern.md) can be specified. This case is called standard deserialization.

To control how often a deserialization-relevant case must or can be executed in deserializations, `tt:[d-]cond` within `tt:group` can contain the additional attribute `frq` (frequency) with one of three allowed values:

- `<tt:[d-]cond ... frq="1"/>`

  Required case. The case must be executed exactly once while the group is processed.

- `<tt:[d-]cond ... frq="?"/>`

  Optional case. The case is executed only once while the group is processed.

- `<tt:[d-]cond ... frq="*"/>`

  Multiple case. The case can be executed any number of times while the group is processed.

For `frq="?"` and `frq="*"`, the expected element must not necessarily exist in the inbound XML stream.

Implicit frequency: If the attribute `frq` is not specified explicitly,

- `frq="1"` is used implicitly in `tt:cond` cases that do not contain data conditions (that is, they must be executed in serializations).

- `frq="?"` is used implicitly in `tt:cond` cases that contain a data condition (that, is they may not be executed in serializations).

**Serialization**

During serialization, the element `tt:group` is executed once as follows: All serialization-relevant cases with fulfilled or no prerequisite `using`, `data`, or `check` are executed in the specified order.

**Deserialization**

During deserialization, the element `tt:group` starts a sequence of evaluation steps for the group that require some cases to be selected and also searches for a superset of these cases to be selected. The group evaluation terminates successfully when all required cases are selected or the current node does not match an unselected case.

- Frequency `1`: Mandatory case. The case is required and searched for.

- Frequency `?`: Optional case. The case is not required but searched for.

- Frequency `*`: Fallback case. The case is neither required nor searched for.

During each evaluation step, one of the deserialization-relevant cases whose maximum case frequency has not yet been reached is selected as follows:

1.  The first case that contains a suitable pattern is executed (deserialization and assertions met).

2.  If no such case exists, the system tries to execute the standard deserialization, if it exists. If the possible prerequisites `using`, `data`, or `check` of the standard deserialization are not met, the exception `CX_ST_REF_ACCESS` is raised.

3.  If no standard deserialization exists, the exception `CX_ST_GROUP_MISSING_CASE` is raised.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following transformation `DEMO_ST_GROUP` shows how groupings work:

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:root name="ROOT3"/> 
  <tt:root name="ROOT4"/> 
  <tt:template> 
    <X0> 
      <tt:group> 
        <tt:cond> 
          <X3> 
            <tt:value ref="ROOT3"/> 
          </X3> 
        </tt:cond> 
        <tt:cond frq="?"> 
          <X2> 
            <tt:value ref="ROOT2"/> 
          </X2> 
        </tt:cond> 
        <tt:cond frq="*"> 
          <X1> 
            <tt:value ref="ROOT1"/> 
          </X1> 
        </tt:cond> 
        <tt:cond> 
          <tt:skip count="1"/> 
        </tt:cond> 
      </tt:group> 
      <X4> 
        <tt:value ref="ROOT4"/> 
      </X4> 
    </X0> 
  </tt:template> 
</tt:transform>
```

Assume that an inbound XML stream has the following form:

``` abap
<X0> 
   <X1>1</X1> 
   <X1>2</X1> 
   <X2>3</X2> 
   <X2>4</X2> 
   <X3>5</X3> 
   <X4>6</X4> 
</X0>
```

The deserialization proceeds as follows:

1.  In the first evaluation step, element `X1` is used and the first element `X1` deserialized, where `ROOT1` is set to *1*.

2.  In the second evaluation step, element `X1` is used again because of the condition `tt:cond frq="*"` and the second element `X1` deserialized, where `ROOT1` is set to *2*.

3.  In the third loop pass, element `X2` is used and the first element `X2` deserialized, where `ROOT2` is set to *3*.

4.  In the fourth evaluation step, element `X2` cannot be used again because of condition `tt:cond frq="?"`. Instead, the second element `X2` is skipped in the standard deserialization with `tt:skip`. Specifying `count` is necessary because otherwise all subsequent elements would be skipped.

5.  In the fifth evaluation step, element `X3` is used and the first element `X3` deserialized, where `ROOT3` is set to *5*.

6.  All required cases of the group have been selected, so the loop ends. The element `X4` is deserialized outside of `tt:group` and `ROOT4` is set to *6*.

The examples can be executed by opening the class `CL_DEMO_ST_GROUP`.
