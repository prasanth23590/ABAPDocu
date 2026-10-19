---
title: "ST - tt:include, Include Transformations"
source_file: abenst_tt_include.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Reusing ST Programs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:include, Include Transformations

## Syntax

``` abap
<tt:include name="trafo" [templates="tmpl1 tmpl2 ..."] />  
```

## Description

In a simple transformation (ST) program, the `tt:include` statement can be used to include a different ST program `trafo`. The `tt:include` statement makes the templates and type definitions of the included program usable in the current ST program. The ST program `trafo` must exist in the repository. `trafo` is not case-sensitive.

The ST statement `tt:include` can only be listed in an ST program outside of templates. By default, it includes all named templates of a transformation `trafo` at transformation level (unnamed [main templates](abenst_tt_template_main.md) are not included). No namespace conflicts can occur and transformations must not include themselves.

If the attribute `templates` is specified, only the templates `tmpl1 tmpl2` specified there and the templates called by them using [`tt:apply`](abenst_tt_apply.md) are included.

## Hint

Only those transformations whose named templates do not conflict with existing named templates can be included in another transformation. [`tt:apply`](abenst_tt_apply.md) can be used to use the included named templates as subtemplates in the including template.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The ST program below corresponds to the example from [Subtemplates Without Their Own Data Roots](abenst_tt_template_sub.md), except that the subtemplate of an included ST program is used.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:template> 
    <!-- ... --> 
  </tt:template> 
  <tt:template name="TEMP_SUB"> 
    <name> 
      <tt:value ref="$ref.name"/> 
    </name> 
    <work> 
      <tt:value ref="$ref.work"/> 
    </work> 
  </tt:template> 
</tt:transform>
```

The statement `tt:include` could also be placed in front of the main template. The included ST program can be implemented as follows:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates" 
  template="TEMP_MAIN"> 
  <tt:root name="ROOT"/> 
  <tt:template name="TEMP_MAIN"> 
    <week> 
      <day1 tt:ref="ROOT.DAY1"> 
        <tt:apply name="TEMP_SUB"/> 
      </day1> 
      <day2 tt:ref="ROOT.DAY2"> 
        <tt:apply name="TEMP_SUB"/> 
      </day2> 
      <!-- ... --> 
    </week> 
  </tt:template> 
  <tt:include name="DEMO_ST_INCLUDE"/> 
</tt:transform>
```
