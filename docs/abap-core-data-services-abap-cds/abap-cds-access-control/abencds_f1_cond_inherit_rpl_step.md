---
title: "CDS DCL - DEFINE ROLE, replacement_step"
source_file: abencds_f1_cond_inherit_rpl_step.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition > CDS DCL - DEFINE ROLE, inherit_condition > CDS DCL - DEFINE ROLE, replacing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, replacement_step

## Syntax

``` abap
... { PFCG_FILTER [ OBJECT auth_object ] FIELD auth_field VALUE  old WITH new } 
  | { PARAMETERS WITH ( param1 : value1 [, param2 : value2 ...]  ) } 
  | { ROOT WITH path_expr [INCLUDING PARAMETERS ] } 
  | { ELEMENT source_match WITH target } 
  | { PREFIX WITH prefix } 
  | { CONDITIONS ON ANY OF ( element1 [, element2 ... ] ) WITH (TRUE|FALSE |VOID ) } 
  | { IF ALL CONDITIONS VOID THEN (TRUE|FALSE|VOID) } ...  
```

### Variant

[1. `... PFCG_FILTER [OBJECT auth_object] FIELD auth_field VALUE old WITH new`](abencds_f1_cond_inherit_rpl_step.md#variant-1)

[2. `... PARAMETERS WITH ( param1 : value1 [, param2 : value2 ...] )`](abencds_f1_cond_inherit_rpl_step.md#variant-2)

[3. `... ROOT WITH path_expr [INCLUDING PARAMETERS ]`](abencds_f1_cond_inherit_rpl_step.md#variant-3)

[4. `... ELEMENT source_match WITH target`](abencds_f1_cond_inherit_rpl_step.md#variant-4)

[5. `... PREFIX WITH prefix`](abencds_f1_cond_inherit_rpl_step.md#variant-5)

[6. `... CONDITIONS ON ANY OF (element1 [, element2 ...]) WITH (TRUE |FALSE |VOID)`](abencds_f1_cond_inherit_rpl_step.md#variant-6)

[7. `... IF ALL CONDITIONS VOID THEN (TRUE |FALSE |VOID)`](abencds_f1_cond_inherit_rpl_step.md#variant-7)

## Overview

### Description

A replacement step operates on a set of inherited [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) and can update or replace them.

## Variant 1

`... PFCG_FILTER [OBJECT auth_object] FIELD auth_field VALUE old WITH new`

### Addition

[`... OBJECT auth_object`](abencds_f1_cond_inherit_rpl_step.md#addition-1)

### Description

This replacement step processes the literal values which are mapped to authorization fields in PFCG conditions.

`auth_field` selects the authorization field. Occurrences of the value `old` are then replaced with the value `new`. Both values must be written as literals in single quotes.

## Addition

`... OBJECT auth_object`

### Description

With this addition, the replacement process can be restricted to the authorization object `auth_object`.

### Hints

- Specifying nonexistent authorization objects or authorization fields produces a syntax error.

- The values in `old` and `new` may be validated against a set of fixed value if the authorization field has such (for example ACTVT). Non-existing values produce a warning.

- To swap values, three replacements must be made. First, the first value is set to a temporary helper value that must be different from the existing values. This helper value must be replaced again after the second value is replaced. The helper value can have no more than 40 characters.

- This step raises a warning when it was reached by at least one PFCG filter with matching field name (and, if given, authorization object), but none of them had a matching filter value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Replacement based on authorization field name independent of authorization object.

**Input:**

``` abap
 (...) = ASPECT PFCG_AUTH( OBJECT_1, ..., ACTVT = '03' )  OR 
 (...) = ASPECT PFCG_AUTH( OBJECT_2, ..., ACTVT = '03' )
```

**Replacement step:**

PFCG_FILTER FIELD ACTVT VALUE '03' WITH 'F4'

**Output:**

``` abap
(...) = ASPECT PFCG_AUTH( OBJECT_1, ..., ACTVT = 'F4' ) OR 
(...) = ASPECT PFCG_AUTH( OBJECT_2, ..., ACTVT = 'F4' )
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Replacement of authorization field in a dedicated authorization object only.

**Input:**

``` abap
(...) = ASPECT PFCG_AUTH( OBJECT_1, ..., ACTVT = '03' ) OR 
(...) = ASPECT PFCG_AUTH( OBJECT_2, ..., ACTVT = '03' )
```

**Replacement step:**

PFCG_FILTER OBJECT OBJECT_1 FIELD ACTVT VALUE '03' WITH 'F4'

**Output:**

``` abap
(...) = ASPECT PFCG_AUTH( OBJECT_1, ..., ACTVT = 'F4' ) OR 
(...) = ASPECT PFCG_AUTH( OBJECT_2, ..., ACTVT = '03' )
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Exchange of two authorization field values using a temporary helper value.

**Input:**

``` abap
 (...) = ASPECT PFCG_AUTH( OBJECT_1, ..., ACTVT = '01' ) OR 
 (...) = ASPECT PFCG_AUTH( OBJECT_2, ..., ACTVT = '02' )
```

**Replacement step:**

``` abap
PFCG_FILTER FIELD ACTVT VALUE '02'   WITH 'TEMP', 
PFCG_FILTER FIELD ACTVT VALUE '01'   WITH '02', 
PFCG_FILTER FIELD ACTVT VALUE 'TEMP' WITH '01'
```

**Output:**

``` abap
(...) = ASPECT PFCG_AUTH( OBJECT_1, ..., ACTVT = '02' ) OR 
(...) = ASPECT PFCG_AUTH( OBJECT_2, ..., ACTVT = '01' )
```

## Variant 2

`... PARAMETERS WITH ( param1 : value1 [, param2 : value2 ...] )`

### Description

References to CDS parameters (`$parameters param...`) used in the inherited access conditions (either within path filters of left side elements or as left side host expressions) are replaced by new parameter values `value`.

For `value` you can insert:

- Literals

- Session variables (`$SESSION...`)

- Parameter references of the target entity.

### Hints

- When you replace a parameter reference of the source with a parameter reference of the target entity, successive steps in the same `REPLACING` section will not touch this parameter any further.

- When you have multiple parameters to replace, you can so in individual steps, or within a single step as comma separated list (or in any mixture of both).

- This step raises a warning when it has been reached by at least one parameter reference, but none of them could be updated by it. When you have specified multiple replacements in a single step, the applicability of one of them already suppresses this warning.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Replacement of the parameters `P1` and `P2` or the source entity with a parameter of the target entity and a literal.

**Input:**

toX ( F = \$PARAMETERS.P1 OR G = \$PARAMETERS.P2 )

**Replacement step:**

PARAMETERS WITH ( P1 : \$PARAMETERS.P2, P2 : 'U' )

``` abap
**Output:** 
`toX ( F = $PARAMETERS.P2 OR G = 'U' )`
```

The same result would have been created with two separate steps:

``` abap
PARAMETERS WITH ( P1 : $PARAMETERS.P2 ), 
PARAMETERS WITH ( P2 : 'U' )
```

## Variant 3

`... ROOT WITH path_expr [INCLUDING PARAMETERS]`

### Addition

[`...INCLUDING PARAMETERS`](abencds_f1_cond_inherit_rpl_step.md#addition-2)

### Description

This replacement step processes left side CDS elements and relocates them into the provided association `path_expr`.

The path expression can have one or more levels and can be specified in the same way as in the CDS entity.

The entity of the last path component must be the source entity of the inheritance condition.

### Hints

- Left side CDS elements that were produced by a preceding replacement step (`ROOT WITH`, `ELEMENT WITH`, `PREFIX WITH`) are not updated.

- When the last path component points to a view with parameters, those can be specified in a parameter binding. For all non-optional parameter this is mandatory

- A path expression prefix makes it possible to protect a CDS entity with the access rules of the association target of one of its CDS association.

- This step emits a warning when it is reached by at least one left side element but updated none.

- The optionality property of the inbound CDS element is lost during this replacement step because the formerly optional element is after this replacement step no longer the first component of the resulting path expression. However, you can declare optionality for the first component of `path_expr`.

- An incoming condition using DCL function `OPTIONAL_ELEMENT_EXIST` is replaced depending on the comparison operator:

  - `OPTIONAL_ELEMENT_EXISTS( ... ) IS INITIAL --> FALSE`

  - `OPTIONAL_ELEMENT_EXISTS( ... ) IS NOT INITIAL --> TRUE`

## Addition

`...INCLUDING PARAMETERS`

### Description

When the entity of the last association component of `path_expr` has parameters and some of them are specified as part of the `ROOT WITH` statement, this parameter binding is used to perform parameter replacement in the condition set.

### Hints

- This statement is a short form of the sequence `ROOT WITH` with a parameter binding for the last component and `PARAMETER WITH` with the same parameter binding.

- In contrast to the explicit form, the short form does not produce a warning when there are no parameters that can be replaced.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

You have a base entity `S` (for example a released SAP entity) and create a custom entity `C` using `S` as datasource.

``` abap
DEFINE VIEW ENTITY C 
  AS SELECT FROM S 
  ASSOCIATION [1..1] TO S AS toS ON ... 
  { ... }
```

Using the association `toS`, access control of `S` can now be taken over to `C`:

``` abap
GRANT SELECT ON C WHERE INHERITING CONDITIONS FROM ENTITY S 
   REPLACING { ROOT WITH toS };
```

An access condition of `S` like

state = 'X'

will then be executed for `C` as

toS.state = 'X'

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the example above, `S` has a parameter `DEMO` and the access condition is

toState\[f = \$parameters.DEMO\].value = 'A'

In entity `C`, this parameter is supplied with a fixed value 'P'

DEFINE VIEW ENTITY C AS SELECT FROM S( DEMO : 'P' ) ...

In the access control, the usage of the unchanged `toS` allows and eventually even requires the parameter to be supplied.

``` abap
 GRANT SELECT ON C WHERE INHERITING CONDITIONS FROM ENTITY S 
  REPLACING { ROOT WITH toS( DEMO : 'P' ) };
```

This would result in the access condition

toS.toState\[f = \$parameters.DEMO\].value = 'X'

This still requires that also `C` has the parameter `DEMO`.

By adding `INCLUDING PARAMETERS`

``` abap
GRANT SELECT ON C WHERE INHERITING CONDITIONS FROM ENTITY S 
  REPLACING { ROOT WITH toS( DEMO : 'P' ) INCLUDING PARAMETERS };
```

you apply a parameter replacement and the result is

toS.toState\[f = 'P'\].value = 'X'

## Variant 4

`...ELEMENT source_match WITH target`

### Description

This replacement step searches for left side CDS elements matching the given `source_match` and replaces them by the given `target`.

Both `source_match` and `target` must together belong to one of the following categories:

- A plain entity field or a path expression ending with a field.

  In this flavor, the statement replaces dedicated left side CDS elements.

- An association with an arbitrary number of path components.

  In this flavor, the statement allows renaming of associations, while preserving all parts after the matching source components. Parameter bindings or path filters of the last source match component can either by specified in the source match and by this get consumed or can remain unmentioned in the source match in which case they are taken over to the resulting element. The provided target may contain parameter bindings or path filters at all locations.

The source matching process has the following properties:

- The components of the source match must be fully present in the incoming element.

- Parameter bindings and path filters for all but the last path component must be present/absent identically, and when present must be literally the same, that is except case insensitivity for identifiers there is no further normalization. For example the path filter *a = 1 and b = 1* will not match the path filter *b = 1 and a = 1*.

### Hints

- Left side CDS elements that were produced by a preceding replacement step (`ROOT WITH`, `ELEMENT WITH`, `PREFIX WITH`) are never matched.

- This step emits a warning when it matched with no left side element, irrespective of whether the inherited condition set contains left side elements at all.

- When a processed left side element contains parameter bindings or path filters and is matched by a source match which does not consume either of them, and the target also provides an object of the same type, an error occurs.

- The optionality property of the inbound CDS element is lost during this replacement step because the formerly optional element is replaced by this step by a new target element explicitly declared in the current access control. However, you can declare optionality for the first component of `target`.

- Due to the treatment of optionality, a statement `ELEMENT X WITH X` may have an effect:

  - When the inbound element was optional, the outbound element *X* is no longer optional (unless you make it optional itself in the current access control).

  - When the inbound element is not optional, this statement allows it to make the output element optional by a declaration in the current access control (remember that `WITH OPTIONAL ELEMENTS` only operates on left side CDS elements written in the current access control).

- An incoming condition using DCL function `OPTIONAL_ELEMENT_EXISTS` is replaced depending on the comparison operator:

  - `OPTIONAL_ELEMENT_EXISTS( ... ) IS INITIAL --> FALSE`

  - `OPTIONAL_ELEMENT_EXISTS( ... ) IS NOT INITIAL --> TRUE`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Instead of full examples for each possible case, the following table shows in compact form various combinations of source match and target in the `ELEMENT WITH` operator and how they operate on incoming left side elements.

<table>
<thead>
<tr class="header">
<th><strong>source_match</strong></th>
<th><strong>Input Left Side Element</strong></th>
<th><strong>Match</strong></th>
<th>** target**</th>
<th><strong>Output Left Side Element</strong></th>
<th><strong>Explanation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>A</em></td>
<td><em>A</em></td>
<td>Yes</td>
<td><code class="ph codeph">B</code></td>
<td><code class="ph codeph">B</code></td>
<td>Simple entity field</td>
</tr>
<tr class="even">
<td><em>A</em></td>
<td><code class="ph codeph">B</code></td>
<td>No</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><em>A</em></td>
<td><code class="ph codeph">toB</code></td>
<td>Error</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><em>A</em></td>
<td><code class="ph codeph">toB.A</code></td>
<td>No</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><em>A</em></td>
<td><em>A</em></td>
<td>Yes</td>
<td><code class="ph codeph">toB.C</code></td>
<td><code class="ph codeph">toB.C</code></td>
<td>You can replace a field with a path expression.</td>
</tr>
<tr class="even">
<td><em>A</em></td>
<td><em>A</em></td>
<td>Yes</td>
<td><code class="ph codeph">toB (p:'x' ).toC [i=3 ].toD(q:'Y') [j=5].E</code></td>
<td><code class="ph codeph">toB (p:'X').toC [i=3].toD(q:'Y') [j=5].E</code></td>
<td>Parameters and filters are supported in the target.</td>
</tr>
<tr class="odd">
<td><em>A</em></td>
<td><em>A</em></td>
<td>Yes</td>
<td><em>A</em></td>
<td><em>A</em></td>
<td><p>At first, this looks like a <code class="ph codeph">NOOP</code>, but it isn't. It has a meaning when optional elements are involved.</p>
<p>With this replacing, the author of the DCL source containing the <code class="ph codeph">ELEMENT A WITH A</code> explicitly declares that he/she knows that the inherited entity containes element <em>A</em> (otherwise, the own DCL source would be syntactically incorrect already here). Optionality for <em>A</em> from the inherited source is therefore removed, as from that point on, the existence of <em>A</em> is certain.</p>
<p>Similarly, when the inherited source contains <em>A</em> and the author of the current DCL source wants to have <em>A</em> optional from this point on, this statement is the only way to let the own <code class="ph codeph">WITH OPTIONAL ELEMENTS (A DEFAULT ...)</code> become applicable to the inherited <em>A</em>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">toA.B</code></td>
<td><code class="ph codeph">toA.B</code></td>
<td>Yes</td>
<td><code class="ph codeph">?</code></td>
<td><code class="ph codeph">?</code></td>
<td>You can match path expressions and replace them as above with anything you like (<code class="ph codeph">?</code> can be field or path expression, the latter with parameters and filters, see above).</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">toA.B</code></td>
<td><code class="ph codeph">toA.C</code></td>
<td>No</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><code class="ph codeph">toA.B</code></td>
<td><code class="ph codeph">toB.B</code></td>
<td>No</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">toA.B</code></td>
<td><code class="ph codeph">toC</code></td>
<td>Error</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><code class="ph codeph">toA(p:'X').toB[i=3].C,</code></td>
<td><code class="ph codeph">toA(p:'X').toB[i=3].C</code></td>
<td>Yes</td>
<td><code class="ph codeph">?</code></td>
<td><code class="ph codeph">?</code></td>
<td>Source matcher can have parameter bindings and filters</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">toA(p:'X').toB[i=3].C</code></td>
<td><code class="ph codeph">toA(p:'Y').toB[i=3].C</code></td>
<td>No</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><code class="ph codeph">toA(p:'X').toB[i=3].C</code></td>
<td><code class="ph codeph">toA(p:'X').toB[3=i].C</code></td>
<td>No</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">toA</code></td>
<td><code class="ph codeph">toA.B</code></td>
<td>Yes</td>
<td><code class="ph codeph">toX</code></td>
<td><code class="ph codeph">toX.B</code></td>
<td>Replacement of an (open) association with another one in the target entity. The trailing part after the match is taken over after the target fragment.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">toA.toB</code></td>
<td><code class="ph codeph">toA.toB.toC.toD.E</code></td>
<td>Yes</td>
<td><code class="ph codeph">toX.toY</code></td>
<td><code class="ph codeph">toX.toY.toC.toD.E</code></td>
<td>The same with longer chains.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">toA[i=3]</code></td>
<td><code class="ph codeph">toA[i=3].B</code></td>
<td>Yes</td>
<td><code class="ph codeph">toX</code></td>
<td><code class="ph codeph">toX.B</code></td>
<td>The filter from the left-side has been consumed by the source matcher (this and the following examples use a path filter for demonstration, with parameter bindings the same would happen, and when parameter bindings and filters come together, both operate independently from each other).</td>
</tr>
<tr class="even">
<td><code class="ph codeph">toA[i=3]</code></td>
<td><code class="ph codeph">toA[i=3].B</code></td>
<td>Yes</td>
<td><code class="ph codeph">toX[i=4]</code></td>
<td><code class="ph codeph"> toX[i=4].B</code></td>
<td>The target fragment can supply the resulting left-side with its own path filter.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">toA[i=3]</code></td>
<td><code class="ph codeph">toA[i=4].B</code></td>
<td>No</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><code class="ph codeph">toA</code></td>
<td><code class="ph codeph">toA[i=3].B</code></td>
<td>Yes</td>
<td><code class="ph codeph">toX</code></td>
<td><code class="ph codeph">toX[i=3].B</code></td>
<td>The filter has not been consumed by the matcher and is therefore taken over from the left-side and attached to the target fragment.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">toA</code></td>
<td><code class="ph codeph">toA[i=3].B</code></td>
<td>Yes</td>
<td><code class="ph codeph">toX[i=3]</code></td>
<td>Error</td>
<td>As the filter from the left side has not been consumed, it must be taken over to the target fragment. But this one already has a filter. This potential conflict is not permissive (even when both are literally the same).</td>
</tr>
</tbody>
</table>

## Variant 5

`PREFIX WITH prefix`

**This replacement step is not released for usage in customer created access controls but only internally at SAP.**

### Description

This replacement step processes left side CDS elements and changes the name of the first component such that it starts with the provided `prefix`.

When the concatenation of prefix and component name exceeds the maximum component name length of 30 characters, a name compression algorithm will shorten the component name accordingly in a way that ensures name uniqueness but preserves some readability.

The prefix can contain the ampersand character `&` at a single location. Then, this location of the resulting component name will contain an upwards counting number which is used when the same component name is handled with this replacement step again.

### Hints

- Left side CDS elements that were produced by a preceding replacement step `(ROOT WITH, ELEMENT WITH, PREFIX WITH)` are not updated.

- This step emits a warning when it is reached by at least one left side element but updated none.

- Optionality of the inbound left side CDS element is preserved by this step.

- DCL function `OPTIONAL_ELEMENT_EXISTS` is preserved with the updated element name.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following table demonstrates the effects of the statement.

| **Input element**           | **Prefix** | **Output element**               | **Comment**                                                                                                                                                                                                                            |
|-----------------------------|------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *A*                         | `P_`       | `P_A`                            |                                                                                                                                                                                                                                        |
| `toB.C`                     | `P_`       | `P_toB.C`                        |                                                                                                                                                                                                                                        |
| `ALREADY_LONG_ELEMENT_NAME` | `LONGPF`   | `LONGPFALREAD_F3BD3673_ENT_NAME` | The exact syntax of the shortening may look different, this shall only provide the idea. The algorithm of the shortening is not published and only available internally at SAP as API for the components eligible to use this feature. |
| *A*                         | `SAP_&_`   | `SAP_1_A`                        | Initial prefix for view stacks.                                                                                                                                                                                                        |
| `SAP_1_A`                   | `SAP_&_`   | `SAP_2_A`                        | Follow-up prefix for view stacks.                                                                                                                                                                                                      |

## Variant 6

`... CONDITIONS ON ANY OF (element1[, element2 ...]) WITH (TRUE|FALSE| VOID)`

### Description

This replacement step replaces an entire access condition with one of the given operators `TRUE`, `FALSE` or `VOID`, when any of its left side elements matches one of the given elements `element1`, `element2`, ... .

The match elements can be either fields or path expressions, also open associations are supported.

Parameter bindings and path filters must not be specified, as a match element only considers the component names and matches incoming path expressions irrespectively of whether they contain parameter bindings or path filters.

### Hints

- Left side CDS elements that were produced by a preceding replacement step (`ROOT WITH`, `ELEMENT WITH`, `PREFIX WITH`) are not updated.

- The usage of an element list is a short form or multiple `CONDITIONS ON ANY OF` statements for the individual elements.

- The step generates a warning when it could not match any of the given elements with an incoming left side element.

- When using this statement with the replacement option `VOID`, later changes in the inherited condition set may let the own access control become syntactically invalid when all conditions get replaced by `VOID`. To protect against this situation, you can use step `IF ALL CONDITIONS VOID THEN` as guard.

- All elements of the element list must exist in the inheriting CDS entity. This statement is therefore not suitable to suppress nonexistent CDS elements in the future.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The inherited condition

( toA\[F = 1\].B, C ) = ASPECT PFCG_AUTH( ... )

will be replaced by `TRUE` with any of the following steps:

- `CONDITIONS ON ANY OF ( toA ) WITH TRUE`

- `CONDITIONS ON ANY OF ( toA.B ) WITH TRUE`

- `CONDITIONS ON ANY OF ( C ) WITH TRUE`

## Variant 7

`IF ALL CONDITIONS VOID THEN (TRUE|FALSE|VOID)`

### Description

This step analyzes the current state of the condition set in the inheritance/replacement procedure. When it comprises only the `VOID` operator, the entire condition set is replaced by the given replacement value

### Hints

- This step is intended as a guard step when using `CONDITIONS ON ANY OF ... WITH VOID`.

- The possibility to replace the condition set in this situation again with `VOID` exists for symmetry only, it is not sensible to do so.

- This step does not generate a warning when it is not used. A good firefighter does not complain when there is no work to do.
