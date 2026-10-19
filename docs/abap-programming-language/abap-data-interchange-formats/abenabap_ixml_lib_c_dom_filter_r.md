---
title: "iXML - Reads Using Filters"
source_file: abenabap_ixml_lib_c_dom_filter_r.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Access to DOM > iXML - DOM Reads"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Reads Using Filters

When a DOM is read using [iterators](abenabap_ixml_lib_c_dom_iterat_r.md), all nodes of a document or subtree or all elements of a list are read by default. A filter can be linked with an iterator to restrict it to specific nodes or elements only. Filters can be created using factory methods from the interface `IF_IXML_NODE`. For example, a condition can be set for the name of an element as follows if `document` has the type `IF_IXML_DOCUMENT` and points to an XML:

`DATA(filter) = document->create_filter_name_ns( name = ... ).`

The static type of the reference variable `filter` is then `IF_IXML_NODE_FILTER` and the variable points to a filter object that can be passed to an iterator as follows:

``` abap
DATA(iterator) = document->create_iterator( ). 
... 
iterator->set_filter( filter ).
```

or in short

`DATA(iterator) = document->create_iterator_filtered( filter ).`

The [iterator](abenabap_ixml_lib_c_dom_iterat_r.md) then only reads elements of the name passed to the filter. The factory methods of the interface for nodes can be used to create the following filters (among others):

- `CREATE_FILTER_NODE_TYPE`: Condition for the type of a node

- `CREATE_FILTER_NAME_NS`: Condition for the name of a node

- `CREATE_FILTER_ATTRIBUTE_NS`: Condition for the name and value of an attribute

Other factory methods are available for associating multiple filters and creating special filters that implement Boolean operators:

- `CREATE_FILTER_AND`: "and" join

- `CREATE_FILTER_OR`: "or" join

- `CREATE_FILTER_NOT`: Negation

References to existing filter objects can be passed to the input parameters of these factory methods. A new filter is created that implements the Boolean operator on the passed filters.

## Hint

For more information (further filters and possible parameters), see the interface `IF_IXML_NODE`.
