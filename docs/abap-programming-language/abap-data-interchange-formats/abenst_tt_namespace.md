---
title: "ST - tt:namespace, Namespaces"
source_file: abenst_tt_namespace.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:namespace, Namespaces

## Syntax

``` abap
<tt:namespace name="prefix"|name=""/>  
```

## Description

The ST statement `tt.namespace` declares an explicit namespace.

By default, namespace declarations are only written to the resulting XML data in serializations if the associated namespace prefix is used as part of the name in a literal XML element or attribute or in a non-literal attribute. A namespace declaration is written exactly to the element in which it is required. Namespace declarations whose prefix is not used explicitly are ignored in serializations. In deserializations, the binding of the namespace prefix to the correct URI is checked.

For XML elements of the resulting XML data in which a namespace declaration is required even though the relevant namespace prefix is not part of a name but used, for example, as content of an attribute, this can be forced in serializations by using the statement `tt:namespace`. The statement can be specified one or more times within a literal XML element before its subelements. Each statement declares a namespace for the current XML element with the namespace prefix specified after the attribute `name`. The namespace prefix must be known in the current context, that is, it must have been defined in a surrounding XML element with `xmlns:prefix="uri"`.

**Serializing Namespace Declarations**

If a surrounding element does not yet contain a declaration of the namespace, the statement `tt:namespace name="prefix"` inserts the definition `xmlns:prefix="uri"` into the definition of the literal XML element and thus applies it to all its subelements. The statement `tt:namespace name=""` inserts the definition `xmlns="uri"` if defined in a surrounding XML element. Within the XML element, no other declarations of this namespace are created. In particular, other `tt:namespace` statements within the same XML element are ignored.

**Deserializing Namespace Declarations**

In deserializations, the statement `tt:namespace` is ignored.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The ST program `DEMO_ST_NAMESPACE1` below shows how namespaces are handled by default:

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates" 
  xmlns:abc="www.abc.com" xmlns:xyz="www.xyz.com"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <X0> 
      <context1 xmlns:abc="www.abc.com" attr="abc:uvw"> 
        <X>...</X> 
      </context1> 
      <context2> 
        <abc:X xyz:attr="xyz">...</abc:X> 
        <xyz:Y>...</xyz:Y> 
      </context2> 
    </X0> 
  </tt:template> 
</tt:transform>
```

The definition of the namespace with the prefix `abc` in element `context1` is not needed in standard XML and is omitted in serializations. In the subelements `abc:X` and `xyz:Y` of `context2`, the declaration of namespaces is needed and inserted in serializations. The result of a serialization is as follows:

``` abap
<X0> 
  <context1 attr="abc:uvw"> 
    <X> 
     ... 
    </X> 
  </context1> 
  <context2> 
    <abc:X 
      xmlns:abc="www.abc.com" 
      xmlns:xyz="www.xyz.com" xyz:attr="xyz"> 
      ... 
    </abc:X> 
    <xyz:Y xmlns:xyz="www.xyz.com"> 
      ... 
    </xyz:Y> 
  </context2> 
</X0>
```

The ST program `DEMO_ST_NAMESPACE2` below contains explicit namespace declarations:

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates" 
  xmlns:abc="www.abc.com" 
  xmlns:xyz="www.xyz.com"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <X0> 
      <context1 attr="abc:uvw"> 
        <tt:namespace name="abc" /> 
        <X>...</X> 
      </context1> 
      <context2> 
        <tt:namespace name="abc" /> 
        <tt:namespace name="xyz" /> 
        <abc:X xyz:attr="xyz">...</abc:X> 
        <xyz:Y>...</xyz:Y> 
      </context2> 
    </X0> 
  </tt:template> 
</tt:transform>
```

The `tt:namespace` statements are used to explicitly insert namespace declarations for the prefixes `abc` and `xyz` into the elements `context1` and `context2`. Now the content of attribute `attr` of `context1` can be evaluated with specific reference to the namespace and the declaration of namespaces is no longer needed in the elements `abc:X` and `xyz:Y` of `context2`.
