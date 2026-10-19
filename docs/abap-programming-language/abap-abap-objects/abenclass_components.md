---
title: "ABAP Objects - Components of Classes"
source_file: abenclass_components.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Components of Classes

The content of a class is composed of components. The components define the properties of the [objects](abenobject.md) of a class. Each component is declared in the [definition](abenclass_interface_definition.md) of the class in one of the four [visibility sections](abenclass_visibility.md) that the interfaces define externally. Within a class, all its components are visible. All components are in the same namespace, which means that the names of all components in the class must be different.

The individual components are:

- [Attributes](abenclass_attributes.md)

- [Methods](abenclass_methods.md)

- [Events](abenclass_events.md)

- [Types and constants](abenclass_types_constants.md)

There is a distinction between those components that exist on an instance-dependent basis for every object, and those that exist only once in each class, independent of the instance. The instance-dependent components are known as [instance components](../../abap-glossary/abeninstance_component_glosry.md) and the instance-independent components are referred to as [static components](../../abap-glossary/abenstatic_component_glosry.md).

In ABAP Objects, classes can define the components listed above. This description also applies to interfaces, since all components that can be declared in classes can also be declared in interfaces.

The components of classes can be [accessed](abenclass_components_addressing.md) internally and, depending on the visibility, also from outside the class. If accessed externally, [component selectors](../../abap-glossary/abencomponent_selector_glosry.md) must be used to address the components.
