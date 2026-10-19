---
title: "News for ABAP Release 7.82"
source_file: abennews-782.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.82

The kernel release for ABAP release 7.82 is 7.82.

## ABAP CDS

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CDS Hierarchy, Caching Policy</strong></td>
<td>A hierarchy definition <a href="abencds_f1_define_hierarchy.html"><code class="ph codeph">DEFINE HIERARCHY</code></a> can now use the new addition <code class="ph codeph">CACHE ON|OFF|FORCE</code> to specify the caching policy for a generated hierarchy.</td>
</tr>
<tr class="even">
<td><strong>CDS Projection View, <code class="ph codeph">REDEFINE ASSOCIATION</code></strong></td>
<td>In CDS projection views, it is now possible to redefine the CDS associations from the projected entity in the header part. This is done using the keyword <a href="abencds_proj_view_redefined_assoc.html"><code class="ph codeph">REDEFINE ASSOCIATION</code></a>. Redefinition can include a new filter, alias name, and redirection to a new association target, which must also be a CDS projection view, thus moving the complete data model to the projection layer.</td>
</tr>
<tr class="odd">
<td><strong>ABAP Program for Migration Analysis</strong></td>
<td><p>The following documented ABAP program is now available for evaluating whether a migration from a CDS DDIC-based view (obsolete) to a CDS view entity is possible:</p>
<p><code class="ph codeph">RUTDDLS_MIGRATION_CANDIDATES</code>.</p></td>
</tr>
</tbody>
</table>

## String Processing

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XPath and XSD Regular Expressions</strong></td>
<td><p>Besides the existing support of <a href="abenpcre_regex_glosry.html">PCRE regular expressions</a> and <a href="abenposix_regex_glosry.html">POSIX regular expressions</a> (obsolete) ABAP supports now also <a href="abenxpath_regex_glosry.html">XPath regular expressions</a> and <a href="abenxsd_regex_glosry.html">XSD regular expressions</a>. Internally, those are transformed to PCRE regular expressions and processed by the PCRE2 Library.</p>
<ul>
<li>Both kinds of regular expressions can be used by the new (factory) methods <code class="ph codeph">CREATE_XPATH2</code> and <code class="ph codeph">CREATE_XSD</code> of the <a href="abenregex_system_classes.html">system classes</a> <code class="ph codeph">CL_ABAP_REGEX</code> and <code class="ph codeph">CL_ABAP_MATCHER</code>.</li>
<li>XPath regular expressions can be used by the new parameter <a href="abenstring_functions_regex.html"><code class="ph codeph">xpath</code></a> in some built-in functions.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Callouts in PCRE Regular Expressions</strong></td>
<td>The class <a href="abenregex_system_classes.html"><code class="ph codeph">CL_ABAP_MATCHER</code></a> supports callouts in <a href="abenregex_pcre_syntax.html">PCRE syntax</a> now. The method <code class="ph codeph">SET_CALLOUT</code> can be used to register a handler class that implements the interface <code class="ph codeph">IF_ABAP_MATCHER_CALLOUT</code>. The <a href="abenregex_pcre_syntax_specials.html">special characters</a> <code class="ph codeph">(?C...)</code> of a PCRE regular expression then call the interface method <code class="ph codeph">CALLOUT</code> when the method <code class="ph codeph">MATCH</code> is executed.</td>
</tr>
</tbody>
</table>

## Internal Tables

| Modification                       | Description                                                                                                                                                                                                                                                                                                      |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Alias Names for Secondary Keys** | Alias names can now be declared for [secondary keys](../../abap-glossary/abensecondary_key_glosry.md) of internal tables by using the addition `ALIAS` of [`TYPES`](../../abap-programming-language/abap-declarations/abaptypes_secondary_key.md) and [`DATA`](../../abap-programming-language/abap-declarations/abapdata_secondary_key.md). This can be helpful when changing existing secondary keys without invalidating users. |

## ABAP RESTful Application Programming Model

In release 7.82, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                           | Description                                                                                                                                                                                                                                                                                                          |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nested Determinations on Modify**    | It is now possible to trigger a [determination on modify](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_determinations.md) by another determination on modify.                                                                                                                                                                                           |
| **Always Flag in Determine Actions**   | The new addition [`always`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_determine_action.md) can be used for determinations and validations assigned to a [`determine action`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_determine_action.md). When the determine action is called, determinations and validations with this flag are executed regardless of their trigger conditions. |
| **Global Feature Control**             | The new RAP BO operation addition [`features:global`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_actions_fc.md) can be used to define global [feature control](../../abap-glossary/abenrap_feature_control_glosry.md) for RAP BO operations.                                                                                                                            |
| **Global Authorization Control**       | Global authorization control is available. It can be defined using [`authorization master (global)`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_authorization.md).                                                                                                                                                                                    |
| **Non-Locking Actions**                | The new RAP BO operation addition [`lock:none`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_lock_none.md) can be used to suppress the locking mechanism for an action.                                                                                                                                                                                 |
| **Projection BDEF, Operation Augment** | For [projections BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md), the [operation augment](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_augment_projection.md) is available. Augmentation enhances incoming requests with a custom implementation, for example with default values.                                                                                |
