---
title: "ST - Structure of ST Programs"
source_file: abenst_programs_structure.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Structure of ST Programs

## Syntax

``` abap
<?sap.transform simple?> 
<tt:transform [template="tmpl"] 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
 
  [<tt:type name="..." [...]> 
     ... 
   </tt:type> 
   ...] 
 
  [<tt:root name="root1" [...] /> 
   <tt:root name="root2" [...] /> 
   ...] 
  [<tt:parameter name="para1" [...] /> 
   <tt:parameter name="para2" [...] /> 
   ...] 
  [<tt:variable name="vari1" [...] /> 
   <tt:variable name="vari2" [...] /> 
   ...] 
 
  [<tt:template [name=="tmpl"]> 
     ... 
   </tt:template>] 
  [<tt:template [name=="..."]> 
     ... 
   </tt:template> 
  ...] 
 
</tt:transform>  
```

## Description

An ST program must consist of valid XML data that is structured as shown here.

- The first line `<? ... ?>` serves to identify the transformation type (ST). It does not need to be entered because the syntax check adds it automatically.

- The elements of the namespace *http://www.sap.com/transformation-templates* are [ST statements](abenst_statements.md). The namespace prefix `tt` is used in this documentation as a convention for this namespace. ST statements can be XML elements or attributes. All other components of an XML element are so called literal elements, which means that they have no semantics within the ST language.

- Elements of an ST program are:

  - The mandatory root element [`tt:transform`](abenst_tt_transform.md). All other elements must be enclosed in the root element.

  - Type definitions using [`tt:type`](abenst_tt_type.md).

  - Various data declarations using [`tt:root`](abenst_tt_root.md), [`tt:parameter`](abenst_tt_parameter.md), and [`tt:variable`](abenst_tt_variable.md).

  - A [main template](abenst_tt_template_main.md) defined with `tt:template` and any number of [subtemplates](abenst_tt_template_sub.md). A template is a pattern for the XML data into which ABAP data is serialized or from which data is deserialized.

    These elements can be in any order.

## Hint

In this documentation and in the example programs, double quotation marks (*"*) are used as outer quotation marks and single quotation marks (*'*) as inner quotation marks. However, as usual in XML, this is not mandatory. For example, `'not-initial(ref("X.Y"))'` can be written instead of `"not-initial(ref('X.Y'))"`.

## Executable Example

[Example of an ST program](abenst_program_abexa.md)
