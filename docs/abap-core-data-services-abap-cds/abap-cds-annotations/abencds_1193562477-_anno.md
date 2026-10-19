---
title: "Consumption.derivation.binding.type"
source_file: abencds_1193562477-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.derivation.binding.type

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.derivation.binding[ ].type`                           |
| **Scope**   | `#ELEMENT`, `#PARAMETER`                                           |
| **Type**    | `String(12)`                                                       |
| **Enums**   | `#CONSTANT, #ELEMENT, #PARAMETER, #SYSTEM_FIELD`                   |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Consumption

Define a specific behavior that relates to the consumption of CDS content through domain-specific frameworks.

### Use Case

Using these annotations, the specific behavior is defined which is related to the consumption of CDS content. This metadata makes no assumptions about the concrete consumption technology/infrastructure, but it is applicable across multiple consumption technologies (e.g. Analytics or OData).

### Note

Annotations belonging to Consumption.filter regulate filtered queries on UIs.

Usually filter values are entered manually by the user on a UI. By using filter annotations, query filters can be influenced.

## derivation

### Short Description

You can use this annotation and the related derivation annotations to define the specific behavior which is related to the consumption of CDS content using domain-specific frameworks. This metadata makes no assumptions on the concrete consumption technology/infrastructure but is applicable across multiple consumption technologies.

The annotation can be used to derive a default value for a parameter or a filter default value for an element automatically at runtime by selecting one or more rows from a given lookup entity.

The derivation assigns a default value to a parameter if no value has been provided for it by the consumer at runtime (for example, when it is annotated with ‘`@Consumption.hidden`: true’). The derivation will be ignored if a fixed default value is specified for the parameter via ‘`@Consumption.defaultValue`’.

The derivation also adds a default filter for an element if no filter has been provided by the consumer at runtime (for example, when it is annotated with ‘`@Consumption.filter.hidden`: true’). The derivation will be ignored, if a fixed filter default value is specified for the parameter via ‘`@Consumption.filter.defaultValue`’.

An empty derivation of a hidden and mandatory parameter/filter will lead to a runtime error.

## binding

### Short Description

This annotation can be used at runtime to determine access to the lookupEntity by setting parameter values and/or a WHERE clause.

It consists of one or more entries of the following structure:

## type

Specifies how values are assigned to the targetParameter/-Element:

## Enums

## \#ELEMENT

The access to the lookupEntity is filtered to the restrictions of the local element with the name specified in value supplied at runtime. The restrictions can either originate from the runtime filter of the consumer, or from another derivation evaluated before (note that this implies a certain evaluation order of derivations), or can be omitted.

The functional scope of the restriction shall be limited to the functional scope of restricitions expressible with the `@Consumption.filter` annotation at a single element. If the runtime filter of the consumer is too complex to isloate the resitrcition within this limit, then the derivation cannot be applied.

### Note

A related `@Consumption.filter.mandatory` annotation at the element referenced by name in value can be used to enforce a runtime filter of the consumer.

In case targetParameter is specified, the restriction must be a single value, else the lookupEntity cannot be accessed.

## \#PARAMETER

The value is taken from the parameter of the annotated view (for example, “local” parameter) with the name specified in "value".

## \#CONSTANT

The access to the lookupEntity is restricted by a constant provided in value.

## \#SYSTEM_FIELD

The value is taken from the system environment with the system field name (see `@Environment.systemField`) specified in "value".
