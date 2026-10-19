---
title: "XSL - XPath Functions"
source_file: abenabap_xpath_fnctns.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - User-Defined Transformations > XSL - Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - XPath Functions

In the following, supported and not supported XSLT instructions of the [SAP XSLT processor](abenabap_xslt_processor.md) are listed. The URI for the XSLT namespace is `http://www.w3.org/1999/XSL/Transform`.

## Accessors

| **Function**       | **XPath Version** | **Description**                 |
|--------------------|-------------------|---------------------------------|
| `string([object])` | 1.0               | Converts an object to a string. |

## Functions on Numeric Values

| **Function**      | **XPath Version** | **Description**                                            |
|-------------------|-------------------|------------------------------------------------------------|
| `ceiling(number)` | 1.0               | Returns the smallest integer greater than the argument.    |
| `floor(number)`   | 1.0               | Returns the largest integer not greater than the argument. |
| `round(number)`   | 1.0               | Returns the integer closest to the argument.               |

## Functions on String Values

| **Function**                          | **XPath Version** | **Description**                                                                                                                                         |
|---------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `concat(string, string[, ...])`       | 1.0               | Returns the concatenation of the arguments.                                                                                                             |
| `normalize-space([string])`           | 1.0               | Returns the argument by removing leading and trailing whitespaces and replacing all sequences of whitespace with one space.                             |
| `string-length([string])`             | 1.0               | Returns the number of characters in the argument.                                                                                                       |
| `substring(string, number[, number])` | 1.0               | Returns the substring of the string starting at the character specified in the first number and with an optional length specified in the second number. |
| `translate(string, string, string)`   | 1.0               | Returns the first string by replacing the occurrences of characters in the second string at the specific position with the third string.                |

## Functions Based on Substring Matching

| **Function**                       | **XPath Version** | **Description**                                                                                           |
|------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------|
| `contains(string, string)`         | 1.0               | Returns true if the first string contains the second string. Otherwise, it returns false.                 |
| `starts-with(string, string)`      | 1.0               | Returns true if the first string starts with the second string. Otherwise, it returns false.              |
| `substring-after(string, string)`  | 1.0               | Returns the substring of the first string after the occurrence of the second string in the first string.  |
| `substring-before(string, string)` | 1.0               | Returns the substring of the first string before the occurrence of the second string in the first string. |

## String Functions That Use Regular Expressions

| **Function**                                | **XPath Version** | **Description**                                                                                                                                                                                                                                                   |
|---------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `matches(string, string[, string])`         | 2.0               | Returns true if the string matches the pattern in the regular expression string. The third argument defines a flag to set options the regular expression interpretation.                                                                                          |
| `replace(string, string, string[, string])` | 2.0               | Returns a string that is created by replacing elements defined in the second string by elements defined in a regular expression in the third string in the first string. The fourth argument defines a flag to set options the regular expression interpretation. |

## Boolean Constructor Functions

| **Function** | **XPath Version** | **Description** |
|--------------|-------------------|-----------------|
| `false()`    | 1.0               | Returns false.  |
| `true()`     | 1.0               | Returns true.   |

## Functions on Boolean Values

| **Function**   | **XPath Version** | **Description**                                                     |
|----------------|-------------------|---------------------------------------------------------------------|
| `not(boolean)` | 1.0               | Returns true if the argument is false. Otherwise, it returns false. |

## Functions on Nodes

| **Function**                | **XPath Version** | **Description**                                                                                                                               |
|-----------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `local-name([node-set])`    | 1.0               | Returns the name of the first node in the specified node set or the name of the current node. The name does not include the namespace prefix. |
| `name([node-set])`          | 1.0               | Returns the name of the first node in the specified node set or the name of the current node. The name does include the namespace prefix.     |
| `namespace-uri([node-set])` | 1.0               | Returns the namespace URI of the first node in the specified node set or the namespace URI of the current node.                               |
| `number([object])`          | 1.0               | Converts an object to a number.                                                                                                               |
| `lang(string)`              | 1.0               | Returns true if the specified language is the same as specified in the current node.                                                          |

## Functions on Sequences

| **Function**      | **XPath Version** | **Description**                  |
|-------------------|-------------------|----------------------------------|
| `boolean(object)` | 1.0               | Converts an object to a Boolean. |

## Aggregate Functions

| **Function**      | **Description** |
|-------------------|-----------------|
| `count(node-set)` | 1.0             |
| `sum(node-set)`   | 1.0             |

## Functions That Generate Sequences

| **Function** | **XPath Version** | **Description**                      |
|--------------|-------------------|--------------------------------------|
| `id(object)` | 1.0               | Selects elements by their unique ID. |

## Context Functions

| **Function** | **XPath Version** | **Description**                                                   |
|--------------|-------------------|-------------------------------------------------------------------|
| `position()` | 1.0               | Returns the context position of the node that is being processed. |
| `last()`     | 1.0               | Returns the context size of the node that is being processed.     |
