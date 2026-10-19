---
title: "regex - Parsing with PCRE Regular Expression"
source_file: abenpcre_parsing_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - Syntax > regex - PCRE Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - Parsing with PCRE Regular Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how to use a PCRE regular expression to parse a syntax.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_pcre_parsing DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
INCLUDE demo_pcre_parsing_helper_def. 
INCLUDE demo_pcre_parsing_helper_impl. 
CLASS ast_builder DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES if_abap_matcher_callout. 
    METHODS: 
    constructor, 
    get_root 
    RETURNING VALUE(root) TYPE REF TO ast_node. 
  PRIVATE SECTION. 
    DATA: m_stack TYPE REF TO node_stack. 
ENDCLASS. 
 
CLASS ast_builder IMPLEMENTATION. 
  METHOD constructor. 
    m_stack = NEW node_stack( ). 
  ENDMETHOD. 
  METHOD if_abap_matcher_callout~callout. 
    DATA: kind TYPE string, 
    child TYPE REF TO ast_node, 
    cond_child TYPE REF TO ast_node, 
    then_child TYPE REF TO ast_node, 
    else_child TYPE REF TO ast_node, 
    node TYPE REF TO ast_node. 
    kind = callout_string. 
    CASE kind. 
      WHEN `true` OR `false` OR `zero` OR `one`. 
        "nodes without children 
        m_stack->push( NEW ast_node( kind ) ). 
      WHEN `succ` OR `pred` OR `iszero`. 
        "nodes with a single child node 
        child = m_stack->pop( ). 
        node = NEW ast_node( kind ). 
        node->append( child ). 
        m_stack->push( node ). 
      WHEN `if`. 
        "node(s) with three child nodes; 
        "child notes have to be popped 
        "off the stack in reverse order 
        else_child = m_stack->pop( ). 
        then_child = m_stack->pop( ). 
        cond_child = m_stack->pop( ). 
        node = NEW ast_node( kind ). 
        node->append( cond_child ). 
        node->append( then_child ). 
        node->append( else_child ). 
        m_stack->push( node ). 
      WHEN OTHERS. 
        "should not happen 
    ENDCASE. 
  ENDMETHOD. 
  METHOD get_root. 
    root = m_stack->pop( ). 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_pcre_parsing IMPLEMENTATION. 
  METHOD main. 
    DATA(input) = 
      `succ( if true then 1 else iszero( if false then 0 else 1 ) )`. 
    cl_demo_input=>new( 
     )->add_text( `Enter something in the following syntax:` 
     )->add_text( `t ::= true | false | 0 | 1 | if t then t ` && 
                  `else t | succ( t ) | pred( t ) | iszero( t )` 
     )->request( CHANGING field = input ). 
 
    "The regex contains named subroutine definitions (?<name> ...) 
    "that call each other recursively 
    "and contains callouts (?C"...") 
    "to trigger construction of the AST nodes 
    FINAL(regex) = cl_abap_regex=>create_pcre( 
    pattern = 
         `(?(DEFINE)` 
      && `  (?<t_true>true(?C"true"))` 
      && `  (?<t_false>false(?C"false"))` 
      && `  (?<t_zero>0(?C"zero"))` 
      && `  (?<t_one>1(?C"one"))` 
      && `  (?<n_if>if\s+(?&n_t)\s+then\s+(?&n_t)\s+else` & 
            `\s+(?&n_t)(?C"if"))` 
      && `  (?<n_succ>succ\s*\(\s*(?&n_t)\s*\)(?C"succ"))` 
      && `  (?<n_pred>pred\s*\(\s*(?&n_t)\s*\)(?C"pred"))` 
      && `  (?<n_iszero>iszero\s*\(\s*(?&n_t)\s*\)(?C"iszero"))` 
      && `  (?<n_t>(?&t_true)|(?&t_false)|(?&t_zero)|(?&t_one)|` & 
            `(?&n_if)|(?&n_succ)|(?&n_pred)|(?&n_iszero))` 
      && `)` 
      && `^\s*(?&n_t)\s*$` ). 
 
    FINAL(matcher) = regex->create_matcher( text = input ). 
    FINAL(builder) = NEW ast_builder( ). 
    matcher->set_callout( builder ). 
 
    IF matcher->match( ). 
      out->write_text( 
        builder->get_root( )->to_string( ) ). 
    ELSE. 
      out->write_text( 
        `The given input cannot be parsed` ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Advanced example for using [PCRE syntax](abenregex_pcre_syntax.md) for regular expressions. Using subroutines defined with [`(?<name> ...)`](abenregex_pcre_syntax_specials.md) and callouts with [`(?C"...")`](abenregex_pcre_syntax_specials.md), an abstract syntax tree (AST) is generated from an input if it follows the example's syntax rules.
