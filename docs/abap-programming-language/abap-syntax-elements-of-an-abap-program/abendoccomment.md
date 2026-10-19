---
title: "ABAP Doc"
source_file: abendoccomment.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > Program Directives"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Doc

## Syntax

``` abap
... "!...  
```

## Description

A comment for ABAP Doc is introduced by the string `"!`. This is a special form of a regular [line end comment](abencomment.md) that is introduced by `"`. ABAP Doc allows [declarations](../../abap-glossary/abendeclaration_glosry.md) in ABAP programs to be documented, based on special ABAP Doc comments. In tools of an [ABAP development environment](../../abap-glossary/abenabap_dev_envir_glosry.md), such as [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md), that support [ABAP Doc](../../abap-glossary/abenadt_glosry.md), the content of ABAP Doc comments is evaluated, converted to HTML, and then displayed appropriately.

- [Rules for ABAP Doc Comments](abendoccomment.md#rules-for-abap-doc-comments)

- [Parameter Interface of Procedures](abendoccomment.md#parameter-interface-of-procedures)

- [Documenting Inline Declarations](abendoccomment.md#documenting-inline-declarations)

- [Formatting](abendoccomment.md#formatting)

- [Short Texts and Their Synchronization](abendoccomment.md#short-texts-and-their-synchronization)

- [Documentation Links](abendoccomment.md#documentation-links)

## Hints

- A special ABAP Doc comment [`"! @testing ...`](../abap-program-maintenance/abentest_relations.md) can be used to define a [test relation](../../abap-glossary/abentest_relation_glosry.md) between a [test class](../../abap-glossary/abentest_class_glosry.md) or a [test method](../../abap-glossary/abentest_method_glosry.md) and another repository object.

## Rules for ABAP Doc Comments

The following rules must be followed to ensure that an ABAP Doc comment is evaluated correctly:

- An ABAP Doc comment is one of the following:

  - A single [comment line](../../abap-glossary/abencomment_line_glosry.md) that only contains the comment

  - A multiline block of consecutive comment lines. The content of a block is summarized into a single ABAP Doc comment.

- An ABAP Doc comment (a line or a line block) must be linked as follows to one [declaration statement](../../abap-glossary/abendeclaration_statement_glosry.md) only (**Note:** ABAP Doc comments are possible for inline declarations; special rules apply):

  - If the declaration statement does not form a [chained statement](../../abap-glossary/abenchained_statement_glosry.md), an ABAP Doc comment can be located directly in front of the declaration statement and cannot be separated by empty lines.

  - If the declaration statement forms a [chained statement](../../abap-glossary/abenchained_statement_glosry.md), the colon must be placed after the keyword. An ABAP Doc comment can be placed in front of the identifier of each declared entity.

    ABAP Doc comments are not allowed at any other positions.

- A single-line ABAP Doc comment cannot be empty. Lines without content are allowed as a mean of formatting in blocks.

- An ABAP Doc comment can contain special tokens and tags for documenting the parameter interface of procedures, or for formatting purposes.

- The special characters *"*, *'*, *\<*, *\>*, *@*, *{*, *\|*, and *}* can, if necessary, be escaped using *"*, *'*, *\<*, *\>*, *&#64;*, *&#123;*, *&#124;*, and *&#125;*.

A violation of this rule produces a syntax check warning.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Basic use of ABAP Doc comments as single lines, blocks and chained statements.

``` abap
"! Basic usage of ABAP Doc 
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    "! Constant character string for a single blank. 
    CONSTANTS blank TYPE string VALUE ` `. 
    "! Method to fill the private structure struct with values 
    "! and append it to internal table itab. 
    METHODS meth. 
  PRIVATE SECTION. 
    DATA: 
      "! Three-component structure 
      BEGIN OF struct, 
        "! Component one 
        comp1 TYPE i, 
        "! Component two 
        comp2 TYPE i, 
        "! Component three 
        comp3 TYPE i, 
      END OF struct, 
      "! Internal table of structure struct 
      itab LIKE TABLE OF struct. 
ENDCLASS.
```

## Parameter Interface of Procedures

The [parameter interface](../../abap-glossary/abenparameter_interface_glosry.md) of [procedures](../../abap-glossary/abenprocedure_glosry.md) and of [events](../../abap-glossary/abenevent_glosry.md) in classes can be documented in the corresponding ABAP Doc commentary with a special syntax:

| **Documentation for** | **Syntax**                       |
|-----------------------|----------------------------------|
| Interface parameters  | `@parameter name\|documentation` |
| Class-based exception | `@raising name\|documentation`   |
| Classic exceptions    | `@exception name\|documentation` |

The specification of `@parameter`, `@raising`, and `@exception` must be placed directly after `"!` and thus introduce a new line. The name (`name`) of an existing parameter or an exception must be specified after `@parameter`, `@raising`, `@exception`. This must be followed by the corresponding documentation, separated by `|`. This documentation is closed by the next `@parameter`, `@raising`, `@exception` or by the end of the ABAP Doc comment. No further documentation can be placed behind an interface documentation as another interface documentation. Each interface parameter or every exception can only be specified once.

### Hint

The arrangement of the parameter interface documentation of procedures does not depend on the order of the corresponding declarations. For reasons of readability, however, the order of the parameters and exceptions in the ABAP Doc comment should be the same as the order of the declarations.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of ABAP Doc comments for the parameter interface of a method.

``` abap
"! Method to check if two sources are identical 
"! and that returns a corresponding boolean value. 
"! 
"! @parameter source1     | First source 
"! @parameter source2     | Second source 
"! @parameter ignore_case | Pass abap_true to ignore case 
"! 
"! @parameter result      | Returns abap_true if sources are identic 
"! 
"! @raising   cx_invalid_source 
"!                        | One of the sources is empty 
METHODS compare 
  IMPORTING 
    source1       TYPE text 
    source2       TYPE text 
    ignore_case   TYPE abap_bool DEFAULT abap_false 
  RETURNING 
    VALUE(result) TYPE abap_bool 
  RAISING 
    cx_invalid_source.
```

## Documenting Inline Declarations

Variables declared inline can be documented in the corresponding ABAP Doc commentary. These variables include data objects, immutable variables, data reference variables, and field symbols. You can use the special syntax `@variable name | documentation`.

Contexts where ABAP Doc comments are supported:

- Standalone inline declarations, where variables are declared using `DATA` or `FINAL` on the left-hand side of an assignment with the assignment operator `=`. In these cases, the `@variable` syntax should not be used, as the ABAP Doc comment is automatically associated with the declared variable.

- Non-standalone inline declarations, such as those included in method calls, internal table processing, or `ASSIGN` statements, can include ABAP Doc comments. These comments should be placed immediately before the statement and must explicitly reference the variable name using the `@variable` syntax.

  - When dealing with method calls that involve multiple inline declarations, you can define an ABAP Doc comment with multiple `@variable` specifications, each referring to a specific actual parameter.

### Hint

Note that not all contexts where inline declarations are possible, including ABAP SQL `SELECT` statements, support ABAP Doc comments for inline declarations.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of ABAP Doc comments with inline declarations:

``` abap
"! Calculation result of addition 
DATA(add_result) = 1 + 3. 
 
"! <p>Calculation result of subtraction<br> 
"! Should be the same as { @link .DATA:add_result }</p> 
FINAL(subtract_result) = 6 - 2. 
 
"ABAP Doc comments for actual paramters declared inline 
TRY. 
    "! 16 Byte System UUID in Binary Format 
    DATA(uuid_x16) = cl_system_uuid=>create_uuid_x16_static( ). 
 
    "! @variable c22 | 16 Byte System UUID in Base64 
    "! @variable c32 | 16 Byte System UUID in Base32 
    "! @variable c26 | 16 Byte System UUID in Hex Format 
    "! @variable c36 | 16 Byte System UUID in RFC4122 Format 
    cl_system_uuid=>convert_uuid_x16_static( 
      EXPORTING 
        uuid     = uuid_x16 
      IMPORTING 
        uuid_c22 = FINAL(c22) 
        uuid_c32 = FINAL(c32) 
        uuid_c26 = FINAL(c26) 
        uuid_c36 = FINAL(c36) ). 
  CATCH cx_uuid_error. 
ENDTRY. 
 
"! Demo string table 
DATA(str_table) = VALUE string_table( ( `AB,AP` ) ( `Hel,lo` ) 
                                      ( `Wor,ld` ) ). 
 
"! @variable <line> | Table line assigned to field symbol 
LOOP AT str_table ASSIGNING FIELD-SYMBOL(<line>). 
  "! @variable split1 | First split result 
  "! @variable split2 | Second split result 
  SPLIT <line> AT ',' INTO DATA(split1) FINAL(split2). 
ENDLOOP. 
 
"! @variable dref | Table line referenced via a data reference variable 
LOOP AT str_table REFERENCE INTO DATA(dref). 
  ... 
ENDLOOP. 
 
"! @variable wa | Table line assigned to a data object 
LOOP AT str_table INTO DATA(wa). 
  ... 
ENDLOOP. 
 
"! @variable line | Table line stored in a data object 
READ TABLE str_table INTO DATA(line) INDEX 1. 
 
"! @variable ref | Table line referenced via a data reference variable 
READ TABLE str_table reference INTO DATA(ref) INDEX 1. 
 
"! @variable <fs> | Table line assigned to field symbol 
ASSIGN str_table[ 1 ] TO FIELD-SYMBOL(<fs>).
```

## Formatting

The following tags can be used within the documentation texts of ABAP Doc comments, to format the output of the documentation in a suitable development environment. These tags are a subset of the HTML tags.

| **Formatting**  | **Tag**                                |
|-----------------|----------------------------------------|
| Header, level1  | `<h1>...</h1>`                         |
| Header, level2  | `<h2>...</h2>`                         |
| Header, level3  | `<h3>...</h3>`                         |
| Paragraph       | `<p>...</p>`                           |
| Italic text     | `<em>...</em>`                         |
| Bold text       | `<strong>...</strong>`                 |
| Unnumbered list | `<ul><li>...</li>...<li>...</li></ul>` |
| Numbered list   | `<ol><li>...</li>...<li>...</li></ol>` |
| Line break      | `<br>`                                 |

An open tag must be closed before a new section of the ABAP Doc comment starts. A new section is introduced by `@parameter`, `@raising` or `@exception`.

The following attributes are possible:

- In the `<ol>` tag, the attributes `reversed`, `start`, and `type` can be specified with their usual HTML meaning.

- In the `<p>` tag, the attributes `class` and `lang` can be specified. For more information about the meaning of these attributes, see *Short Texts and Their Synchronization*.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of formatting in an ABAP Doc comment for a class. The [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) display the documentation according to the formatting.

``` abap
"!<h1>Class demo</h1> 
"!<p>This class must <strong>not</strong> be used in production.</p> 
"!The class serves the following tasks: 
"!<ul><li>Demo 1</li> 
"!    <li>Demo 2</li> 
"!    <li>Demo 3</li></ul> 
"!<br><br> 
CLASS demo DEFINITION. 
  ... 
ENDCLASS.
```

## Short Texts and Their Synchronization

Parts of ABAP Doc comments can be marked as short texts and the short texts of classes and function modules and their components can be synchronized with ABAP Doc comments. To mark a part of an ABAP Doc comment as a short text, it can be tagged as follows:

`<p class="shorttext">...</p>`

A paragraph tagged like this is displayed as a header when displaying the documentation in [ADT](../../abap-glossary/abenadt_glosry.md).

To synchronize the ABAP Doc short texts and the short texts stored as system documentation, the tag can be specified as follows (this is optional):

`<p class="shorttext synchronized">...</p>`

In this case, the length of the short text in ABAP Doc is restricted to the length of the corresponding short text of the system documentation and is synchronized with the associated short text in the original language of the class or function module as follows:

- When an ABAP Doc short text is created or modified in the source code, the corresponding short text of the repository object is used when the source code is saved. If the short text in ABAP Doc is empty, the short text of the repository object is deleted. If `class="shorttext synchronized"` is used to remove a full paragraph, the short text of the repository object is preserved. This synchronization works independently of the tool used.

- If a short text of a method or a function module in the system documentation is modified, for which a paragraph with `class="shorttext synchronized"` occurs in ABAP Doc, the short text is replaced accordingly in the source text when saving. When a short text in the system documentation is deleted, an empty paragraph is produced. When a new short text is created in the system documentation for which there is not yet a short text in ABAP Doc, it does not yet lead to the creation of the paragraph in the source code.

An ABAP Doc short text is part of the source code and is not connected to the translation. Since it replaces the translatable short text of the repository object in its original language connected to the translation during synchronization, it must also be specified in the original language. This is a deviation from the rule that ABAP Doc comments must always be in English. The original language can be marked in the source code by being specified as follows (this is optional):

`<p class="shorttext" lang="...">...</p>`

The attribute `lang` uses the HTML standard. It must be used to specify the original language of the repository object as a two-character ISO code, otherwise, a syntax check warning occurs. This attribute makes it clear in which language the short text should be specified in the source code. It is also intended for future enhancements regarding the translatability of short texts.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See the class `CL_DEMO_ABAP_DOC` in a source code editor. It contains ABAP Doc comments for the class itself, a type, a method, and its parameters, and an attribute. The ABAP Doc comments contain short texts that are synchronized with the short texts in the system documentation in the original language English. The class can be copied to a personal temporary class to test the synchronization.

## Documentation Links

In an ABAP Doc comment, the following syntax can be used to refer to the documentation of other repository objects:

`... {@link [[[kind:]name.]...][kind:]name} ...`

In curly brackets after `@link`, a path specification for a repository object is made, which refers to its documentation. When the documentation is displayed in [ADT](../../abap-glossary/abenadt_glosry.md), a link is created at this position that displays the documentation of the repository object if it is available, when it is selected.

- `name` is used to specify the name of a repository object, for example, a [class](../../abap-glossary/abenclass_glosry.md) or an [interface](../../abap-glossary/abenoo_intf_glosry.md), or a component of a repository object, which is not case-sensitive.

- `kind` is used to specify the type of the repository object or a component of a repository object. `kind` must be specified as shown for the following repository objects:

  - `DATA` for constants, variables, and procedure parameters in the appropriate context

  - `DOMA` for [DDIC domains](../../abap-glossary/abendomain_glosry.md)

  - `EVNT` for [events](../../abap-glossary/abenevent_glosry.md) in classes

  - `FUNC` for [function modules](../../abap-glossary/abenfunction_module_glosry.md) in function pools

  - `FUGR` for [function pools](../../abap-glossary/abenfunction_pool_glosry.md)

  - `INTF` for [interfaces](../../abap-glossary/abenoo_intf_glosry.md) implemented in a class to access its components.

  - `METH` for [methods](../../abap-glossary/abenmethod_glosry.md)

  - `PROG` for [ABAP programs](../../abap-glossary/abenabap_program_glosry.md)

  - `SEAM` for [test seams](../../abap-glossary/abentest_seam_glosry.md)

  - `XSLT` for [XSLT programs](../../abap-glossary/abenxslt_program_glosry.md) and [Simple Transformations](../../abap-glossary/abensimple_transformation_glosry.md)

    `kind` cannot and must not be specified for global data types and object types (classes and interfaces). These repository objects are solely addressed by their names. This applies specifically to [CDS entities](../../abap-glossary/abencds_entity_glosry.md).

- When a repository object is addressed, the path specification is usually single-level. When a component of a repository is addressed, for example a method of a class or a local class of a program, the path specification is usually multileveled, whereby each segment is separated by a period (`.`). The segments between the periods can also be empty. This turns the path into a relative path and the next higher context of the current context is addressed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Documentation of a local class `html` of a program using ABAP Doc comments that contain references to the documentation of a global class and to the ABAP Doc documentation of the current program.

``` abap
"! Default html string for method {@link .html.METH:show} 
"! of local class {@link .html}. 
CONSTANTS 
  default TYPE string VALUE `<html><body>Default</body><html>`. 
 
"! <h1>Class html</h1> 
"! Wraps {@link cl_abap_browser}. 
CLASS html DEFINITION. 
  PUBLIC SECTION. 
    "! <h1>Method show</h1> 
    "! Calls {@link cl_abap_browser.METH:show_html} 
    "! of {@link cl_abap_browser} 
    "! and passes parameter {@link .METH:show.DATA:html }. 
    "! @parameter html | Parameter for 
    "! {@link cl_abap_browser.METH:show_html.DATA:html_string}. 
    "! The default value is {@link .DATA:default}. 
    METHODS show 
      IMPORTING 
        html TYPE string DEFAULT default. 
ENDCLASS. 
 
CLASS html IMPLEMENTATION. 
  METHOD show. 
    cl_abap_browser=>show_html( html_string = html ). 
  ENDMETHOD. 
ENDCLASS.
```
