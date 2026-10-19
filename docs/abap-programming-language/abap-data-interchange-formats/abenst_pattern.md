---
title: "ST - Pattern"
source_file: abenst_pattern.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control > ST - tt:cond, Conditional Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Pattern

When [conditional transformations](abenst_tt_cond.md) are deserialized, the criterion for the evaluation is whether the template content is also a pattern. A pattern contains one or more constructs that are used as *markers*. The most common form of a marker is a literal XML element: if the content of the condition consists of exactly one XML element, the condition has exactly one positive result if an XML element with this name follows at the current position in the XML input stream.

Marker constructs are:

- [Literal XML element](abenst_xml_literals.md) with or without content

- [Non-literal attribute](abenst_tt_attribute.md) with content

- Non-empty [literal text](abenst_tt_text.md)

- Explicit [empty template content](abenst_tt_empty.md)

Each of these constructs can be compared with the input stream in an obvious way.

A pattern can usually contain multiple markers. For example, the sequence

``` abap
<tt:cond> 
  <X> ... </X> 
</tt:cond> 
<Y> ... </Y>
```

is also a pattern; it contains the markers `<X>` and `<Y>`. A condition with this pattern is determined positively by element `X` as well as by element `Y` in the input stream (in the second case, the condition is determined negatively with `X`).

The number of marker constructs `M(c)` contained in template content `c` is defined recursively below. Template content `c` is a pattern if `M(c)` is not empty. In summary, `M(c)` consists of the markers that can be used to positively determine pattern `c`, where conditions in an initial part of `c` can also be determined negatively.

- `M(c) = {c}` for marker `c`. This means that each marker is a (primitive) pattern and the marker set for this pattern consists of the marker itself.

Some constructs propagate markers externally:

- `M(tt:deserialize) = M(tt:ref) = M(c)` for the content `c` of the construct in question.

- `M(tt:apply) = M(c)` for the body `c` of the called template.

- `M(tt:loop) = M(c)` for the loop body `c`.

Conditional transformations also propagate markers. In the case of case distinctions and groupings, the union of all cases is determined:

- `M(tt:[d-]cond) = M(c)` for the condition body `c`.

- `M(tt:group) = M(tt:switch) = M(c1) U ... U M(cn)` for all cases `ci = tt:[d-]cond`.

For all other instructions `c`, `M(c)` is empty.

For `c1 c2 ...` sequences in template content, the following applies:

- `M(c1 c2 ...) = M(c1) U M(c2 ...)`, if `c1` is a prepattern, otherwise `M(c1)`

Template content is a pre-pattern if its deserialization is possible without the use of content from the input stream. In detail:

- All constructs with an empty deserialization are pre-patterns. These are `tt:s-cond`, `tt:assign`, `tt:clear`, `tt:serialize`, `tt:write`, and compositions of these with `tt:cond-var`, `tt:switch-var`, and `tt:apply`.

- `tt:[d-]cond` is a pre-pattern if the condition body is a pattern. (If the pattern cannot be compared, the condition is determined negatively and is skipped.)

`tt:deserialize`, `tt:ref`, and `tt:apply` propagate the pre-pattern property.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The content of the following element `tt:cond` is a pattern with marker elements {`f1`, `f2`, `f3`} (but not `fx`).

``` abap
<tt:cond s-check="not-initial(F3) and initial(F6)"> 
  <tt:clear ref="F3"/> 
  <tt:cond check="not-initial(F1) or not-initial(F2)"> 
    <tt:cond check="not-initial(F1)"> 
      <tt:clear ref="F1"/> 
      <tt:serialize> 
        <f1 a="v" tt:value-ref="F1"/> 
      </tt:serialize> 
      <tt:deserialize> 
        <f1 tt:value-ref="F1"/> 
      </tt:deserialize> 
    </tt:cond> 
    <f2 tt:value-ref="F2"/> 
  </tt:cond> 
  <f3 tt:value-ref="F3"/> 
  <fx> ... </fx> 
</tt:cond>
```
