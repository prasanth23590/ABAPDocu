---
title: "Consistency Checks for Released APIs"
source_file: abenrestricted_apis_atc_consi.html
section: "ABAP APIs > Release Contracts > Contract Checks for Released APIs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consistency Checks for Released APIs

The following shows the documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) of the [ATC](../../abap-glossary/abenatc_glosry.md) check `API_CONSISTENCY`:

## API_CONSISTENCY

## What is checked?

Development objects like CDS views, classes or interfaces can be released as stable APIs for a dedicated purpose.

Use this check to detect inconsistencies in released APIs with respect to their secure and comfortable usage in a restricted development environment.

Depending on the purpose, a released object must comply with the corresponding *release contract*:

- **C0 (Extend)**: This contract ensures stability at dedicated extension points in APIs. Extensibility can be restricted to either *Use in Key User Apps* or *Use in Cloud Development*, or it can be allowed for both types of use. Extension points for *Use in Key User Apps*, namely in the app *Custom Fields*, can be defined by SAP only.

- **C1 (System-Internal Use)**: This contract ensures a technically stable public interface for system-internal use. The compatibility of the public interface includes all its existing parameters, elements, associations to released targets, and their technical data types. Further optional parameters, elements, or associations might be added later, but existing parameters, elements, or associations must not be changed or even removed. Alphanumeric elements might be elongated but will never be shortened. System-internal use can be restricted to either *Use in Key User Apps* or *Use in Cloud Development*, or it can be allowed for both types of use.

- **C2 (Use as Remote API)**: This contract ensures a technically stable public interface for use as remote API. Similar to the contract C1, the compatibility of the public interface includes all its existing parameters, elements, associations to released targets, and their technical data types. Further optional parameters, elements, or associations might be added later, but existing parameters, elements, or associations must not be changed or even removed. But in addition to contract C1, to ensure that external consumers of the API don't need to be adjusted after an upgrade, also the elongation of its elements and parameters is not allowed.

- **C3 (Manage Configuration Content)**: This contract ensures a stable persistence for own configuration content that can be exported, imported, displayed and edited using dedicated APIs and editors. The compatibility of the persistence includes its key definition and all the fields. Optional non-key fields might be added later, but existing fields must not be changed or even removed. Alphanumeric fields might be elongated but will never be shortened. Furthermore, the customer namespace reservations for a released table mustn't be changed.

- **C4 (Use in ABAP-Managed Database Procedures)**: This contract ensures a technically stable public interface for use in ABAP-Managed Database Procedures (AMDP). Similar to the contract C1, the compatibility of the public interface includes all its existing parameters, elements, associations to released targets, and their technical data types. But in contrast to contract C1, no changes are permitted once the object has been released.

The check takes into account development objects with the following *release states*:

- *Released*

- *Released with Feature Toggle*

- *Deprecated*

- *Not to Be Released, Stable*

To release a development object or display its release state, open the object in the *ABAP Development Tools* and click on the *API State* tab of its *Properties view*. Alternatively, open the context menu of the development object in the Project Explorer and choose menu item *API State*.

The release state of an object is transported as an instance of the logical transport object APIS. In the object directory, the release state entry of an object can be found using search pattern R3TR APIS \<ObjectName\>\* (e.g. R3TR APIS I_CURRENCY\* to find the entry of CDS view I_Currency, resulting in R3TR APIS I_CURRENCY DDLS).

## How is the check done?

Each released development object is checked for inconsistencies. These checks comprise of *dependency checks* (to ensure that only other released development objects are referenced in the public part of the API), *object-type-independent checks* (e.g. to ensure that an appropriate successor was specified for a deprecated API), *object-type-specific checks* (e.g. to ensure that a released class is marked as FINAL) and *domain-specific checks* (e.g. to ensure that only suitable annotations are used in a CDS view released for system-internal use).

## Procedure

### Removing Inconsistencies

Each check message describes an inconsistency in a development object which was released as API.

Depending on the severity, inconsistencies must be removed either prior to releasing or can be resolved afterwards also.

### Exemptions for Inconsistencies

In some cases, inconsistencies can't be avoided, but due to their potential criticality, evaluation by an expert is required.

## Checks

### Object-Type-Independent Checks

| Category                                     | Checks                                                                                                                                                                                                                                   |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Release State *Released with Feature Toggle* | feature toggle must exist                                                                                                                                                                                                                |
| Release State *Released with Feature Toggle* | feature toggle must have lifecycle status *Phased Rollout* or *Deferred Adoption*; when the lifecycle status of a feature toggle is changed to *Released*, the release state of the checked object must be changed to *Released* as well |
| Release State *Released with Feature Toggle* | feature toggle must be system-wide                                                                                                                                                                                                       |
| Release State *Deprecated*                   | the object type must support deprecation                                                                                                                                                                                                 |
| Release State *Deprecated*                   | the deprecated object must have at least one successor                                                                                                                                                                                   |
| Release State *Deprecated*                   | all successors must exist, be of an allowed type (allowed types depend on the type of the deprecated object), and be released APIs for the same contract                                                                                 |

### Object-Type-Specific Checks

### Application Job Templates (SAJT)

### Contract C1

| Property          | Check            | Remark |
|-------------------|------------------|--------|
| Job Catalog Entry | must be released |        |

#### BAdI Definitions (ENHS/BADI_DEF)

### Contract C1

| Property        | Check                                                                                 | Remark |
|-----------------|---------------------------------------------------------------------------------------|--------|
| BAdI Definition | must not be flagged for SAP internal use                                              |        |
| BAdI Definition | released key-user tools must have an example class assigned                           |        |
| BAdI Definition | must have a released interface (C1 contract) assigned                                 |        |
| BAdI Definition | if the BAdI definition is an AMDP BAdI, it must be released with the C4 contract also |        |
| BAdI Definition | should be multiple-used                                                               |        |

### Contract C4

| Property        | Check                                                 | Remark |
|-----------------|-------------------------------------------------------|--------|
| BAdI Definition | must be an AMDP BAdI                                  |        |
| BAdI Definition | must have a released interface (C4 contract) assigned |        |
| BAdI Definition | must be released with the C1 contract also            |        |

#### Behavior Definitions (BDEF)

### Contract C0

| Property                                                            | Check                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Remark                                                                                         |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Header                                                              | Behavior definitions without "strict(2);" (on top level) cannot be released for contract C0.                                                                                                                                                                                                                                                                                                                                                                           | "strict(...)" is not needed in interfaces.                                                     |
| Header                                                              | Behavior definitions without "extensible" (on top level) cannot be released for contract C0.                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                |
| Header                                                              | Behavior definitions without "draft" (on top level) cannot be released for contract C0.                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                |
| Header                                                              | After releasing this business object (BO), at least one interface must be released for contract C0.                                                                                                                                                                                                                                                                                                                                                                    | This does not apply to projections and abstract behavior definitions.                          |
| Header of Interface                                                 | An interface can only be released for contract C0 if the base business object (BO) has been released for C0.                                                                                                                                                                                                                                                                                                                                                           |                                                                                                |
| Header of Interface                                                 | Interfaces must be released for contract C1 before they are released for contract C0.                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                |
| Header of Projection                                                | Projections with "use draft as dependent;" cannot be released.                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                |
| Header of Abstract Entity                                           | Abstract behavior definitions must have "with hierarchy" (or "with hierarchy like entity") on top level.                                                                                                                                                                                                                                                                                                                                                               |                                                                                                |
| Entities                                                            | A 'draft query view' must be specified for each extensible entity.                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                |
| Entities                                                            | The CDS annotation "`@AbapCatalog.extensibility.allowNewCompositions`: true" is not permitted if the business object (BO) is unmanaged.                                                                                                                                                                                                                                                                                                                                |                                                                                                |
| Entities                                                            | If an entity has the CDS annotation "`@AbapCatalog.extensibility.allowNewCompositions`: true", it must be extensible in the behavior definition.                                                                                                                                                                                                                                                                                                                       |                                                                                                |
| Draft Action                                                        | The draft action "Activate" should be defined as "optimized".                                                                                                                                                                                                                                                                                                                                                                                                          | This is required if the business object (BO) is extensible with determinations or validations. |
| General rules for names in extensions                               | a\) If the name of the extension starts with an ABAP namespace (such as /MY123/), the names of its elements (actions, functions, determinations etc.) must start with this namespace as well. b) If the name of the extension starts with Y or Z, element names must start with YY or ZZ. If YY is chosen, it must not be followed by a digit between 1 and 9 or the letter A, M, or S. c) Otherwise, element names must neither start with a namespace nor YY nor ZZ. |                                                                                                |
| Names in a *new entity* that is defined in an extension             | Names inside this entity can be without prefix.                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                |
| Names in an extension that is *not* in "ABAP for Cloud Development" | Names can be without prefix.                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                |
| Names that are *not* defined in an extension                        | Names can be without prefix or the prefix must correspond to the name of the behavior definition.                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                |

### Contract C1

| Property                  | Check                                                                                                                                        | Remark                                                                                                                                                                                                              |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header                    | Only interfaces, projections, and abstract behavior definitions can be released.                                                             |                                                                                                                                                                                                                     |
| Header                    | With "language version 'ABAP for Cloud development'", only interfaces and abstract BDEFs can be released.                                    |                                                                                                                                                                                                                     |
| Header                    | Behavior definitions without "strict(2);" cannot be released.                                                                                | "strict(...)" is not needed in interfaces.                                                                                                                                                                          |
| Header                    | Abstract behavior definitions must have "with hierarchy" (or "with hierarchy like entity") on top level.                                     |                                                                                                                                                                                                                     |
| Header                    | Behavior definitions with "use draft as dependent;" cannot be released.                                                                      |                                                                                                                                                                                                                     |
| Own Authorization Context | The authorization objects listed in the "own authorization context" must be released for contract C1.                                        | For interfaces, the "own authorization context" of the base is considered.                                                                                                                                          |
| Entities                  | When a behavior definition is released for contract C1, all underlying CDS entities must also be released for contract C1.                   |                                                                                                                                                                                                                     |
| Entities                  | Non-root entities must not have a CREATE operation.                                                                                          |                                                                                                                                                                                                                     |
| Entities                  | The underlying CDS entities must not have any virtual elements, path expressions, or localized fields (specified by the addition LOCALIZED). |                                                                                                                                                                                                                     |
| Fields                    | Key fields must be "readonly" or "readonly:update".                                                                                          |                                                                                                                                                                                                                     |
| Mappings                  | Projections with a mapping cannot be released.                                                                                               |                                                                                                                                                                                                                     |
| Foreign Entities          | The behavior definitions of foreign entities must be released.                                                                               |                                                                                                                                                                                                                     |
| Associations              | The targets of associations must be released.                                                                                                |                                                                                                                                                                                                                     |
| Actions/Functions         | Parameters and results must be released.                                                                                                     | Releasing the behavior definition (rather than just the data definition/CDS entity) is required for "deep" parameters/results (abstract behavior definitions) and results specified by "result \[...\] entity ...". |
| Actions/Functions         | Deep parameters must have "with control" or "with hierarchy like entity" in their behavior definition.                                       | For results and event parameters, "with control" should not be used.                                                                                                                                                |
| Actions/Functions         | The result must not be a custom entity.                                                                                                      |                                                                                                                                                                                                                     |
| Events                    | Parameters must be released.                                                                                                                 | Parameters of events (except managed events) must always be abstract. Releasing the behavior definition (rather than just the data definition/CDS entity) is required for "deep" parameters.                        |
| Events                    | Events at a root node require that CDS annotation `@ObjectModel.sapObjectNodeType.name` of the base root entity refers to a root node.       |                                                                                                                                                                                                                     |
| Events                    | Events at a non-root node require that CDS annotation `@ObjectModel.sapObjectNodeType.name` of the base entity refers to a non-root node.    |                                                                                                                                                                                                                     |

#### CDS Entities (DDLS/CDS_STOB)

### Contract C0

C0-release for CDS entities with visibility *Use in Key User Apps* is available SAP-internally only. The corresponding checks are performed in transaction SCFD_REGISTRY and as ATC checks like described in the *Custom Fields Adoption Guideline*.

For CDS entities with visibility *Use in Cloud Development*, see below.

| Property                     | Check                                                                                                                                                                                                                                                                                                                      | Remark                                                                                                                                                                                                                                                     |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DDLS Source Type             | Only CDS view entities, CDS projection views, CDS abstract entities or CDS custom entities can be released.                                                                                                                                                                                                                |                                                                                                                                                                                                                                                            |
| Extensibility Quota          | A quota can be defined with the annotations'`@AbapCatalog.extensibility.quota.maximumFields`' and '`@AbapCatalog.extensibility.quota.maximumBytes`'. If a quota is defined, both annotations need to be provided. If a quota is not defined, then the extensible object cannot be extended with fields, only associations. | This is to ensure that technical restrictions on the size of a CDS entity are not violated by the addition of extension fields.                                                                                                                            |
| Data Sources                 | All data sources (i.e. base objects and association targets) behind aliases that are listed in '`@AbapCatalog.extensibility.dataSources`' must be C0 or C1-released. Furthermore, the only allowed aliases are either aliases of data sources contained in the FROM clause of the CDS entity or extension include views.   | This check applies to CDS view entities and CDS projection views.                                                                                                                                                                                          |
| Element Suffix               | An element suffix needs to be set for the extensible CDS entity with the annotation '`@AbapCatalog.extensibility.elementSuffix`'.                                                                                                                                                                                          |                                                                                                                                                                                                                                                            |
| Element Name Prefixes        | No elements starting with YY / ZZ. Also, elements may not start with /-Namespace, different from the enclosing object, if they end with the element suffix defined for the object.                                                                                                                                         | All elements must follow the namespace rules, in order to prevent collisions between SAP, partners and customers.                                                                                                                                          |
| Allow New Compositions       | The annotation '`@AbapCatalog.extensibility.allowNewCompositions`' can only be set to true if it is a root entity or contains a to-parent association or is a transactional projection view.                                                                                                                               |                                                                                                                                                                                                                                                            |
| Extensibility                | Either '`@AbapCatalog.extensibility.extensible`' must be explicitly set to true or '`@AbapCatalog.viewEnhancementCategory`' must be set to \#PROJECTION_LIST.                                                                                                                                                              |                                                                                                                                                                                                                                                            |
| Extensibility                | For abstract or custom entities, '`@AbapCatalog.extensibility.extensible`' must be explicitly set to true.                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                            |
| Enhancement Category         | '`@AbapCatalog.viewEnhancementCategory`' cannot be set to \#UNION or \#GROUP_BY.                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                            |
| Client-Dependency            | The C0 release of client independent views is not supported                                                                                                                                                                                                                                                                | This check applies to CDS view entities and CDS projection views. Later introduction of client dependent data sources would be incompatible.                                                                                                               |
| Unions                       | Usage of unions is not allowed                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                            |
| Group By                     | Usage of group by is not allowed                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                            |
| Join Complexity              | If the CDS entity contains more than 32 joins a warning is issued, if it contains more than 64 joins, an error is thrown.                                                                                                                                                                                                  | This check applies to CDS view entities and CDS projection views. A high join complexity may lead to upgrade errors. The HANA SQL execution plan is used to determine the number of joins in the CDS entity.                                               |
| Buffering                    | Entity buffering (annotation '`@AbapCatalog.entityBuffering`') is not supported.                                                                                                                                                                                                                                           | Customer extension could use features that break buffering for the CDS entity                                                                                                                                                                              |
| Related Draft Objects        | If the CDS entity has a related draft query view, this view must be C0-released. The same applies for the underlying draft table: Either the table must be itself C0-released or must contain a C0-released structure.                                                                                                     | This is to enable customer extension fields can also be added in the corresponding draft objects. Note: This is only necessary if the extensible CDS entity defines any stable datasources with the annotation '`@AbapCatalog.extensibility.dataSources`'. |
| Provider Contract            | For a CDS projection view, a provider contract needs to be specified.                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                            |
| General Usage of Annotations | As defined by meta-annotation `@CompatibilityContract.usageAllowed` in the annotation definition file of the respective annotation                                                                                                                                                                                         |                                                                                                                                                                                                                                                            |

### Contract C1

| Property                      | Check                                                                                                                                                                                                                                                                                      | Remark                                                                                                                                         |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Entity                        | Name must not start with P\_, being the naming convention for private views.                                                                                                                                                                                                               |                                                                                                                                                |
| Entity                        | Name must not start with E\_, being the naming convention for extension include views.                                                                                                                                                                                                     |                                                                                                                                                |
| Entity                        | Must not be registered as extension include view in transaction SCFD_REGISTRY.                                                                                                                                                                                                             |                                                                                                                                                |
| Entity                        | A parallel release for contract C2 is not possible.                                                                                                                                                                                                                                        |                                                                                                                                                |
| Entity                        | Only entities of source type view, projection view, view entity, abstract entity, and custom entity can be released (see domain DDDDLSRCTYPE).                                                                                                                                             |                                                                                                                                                |
| Entity                        | Must not have an implicit select list (i.e. SELECT is not allowed).                                                                                                                                                                                                                        |                                                                                                                                                |
| Elements                      | CDS enumerated types that serve as typing for exposed fields must also be released for contract C1.                                                                                                                                                                                        |                                                                                                                                                |
| Parameters                    | Type of parameter must be either a released data element, CDS simple type, or a built-in data type (e.g. abap.char).                                                                                                                                                                       |                                                                                                                                                |
| Parameters                    | CDS simple type enums that serve as typing for exposed parameters must also be released for contract C1.                                                                                                                                                                                   |                                                                                                                                                |
| Associations                  | If the association target of a public association has release state Deprecated, the association alias in the projection list must be marked accordingly using annotation `@API.element.releaseState`: \#DEPRECATED.                                                                        |                                                                                                                                                |
| Associations                  | If the CDS entity does not contain a key element, the association target must be released for contract C1.                                                                                                                                                                                 |                                                                                                                                                |
| Annotations                   | As defined by meta-annotation `@CompatibilityContract.usageAllowed` in the annotation definition file of the respective annotation.                                                                                                                                                        |                                                                                                                                                |
| Annotations                   | If an element or public association is marked as deprecated or decommissioned with the help of annotation @API.element.releaseState and its values \#DEPRECATED or \#DECOMMISSIONED respectively, a successor must be specified using annotation `@API.element.successor: '<ElementRef>'`. |                                                                                                                                                |
| Annotations                   | Also when inherited from a view below, the annotations @API.element.releaseState and `@API.element.successor: '<ElementRef>'` must be set locally in each released view to document deprecation in the source code.                                                                        |                                                                                                                                                |
| Deprecation / Decommissioning | The successor element or public association specified with `@API.element.successor: '<ElementRef>'` must exist and must not have a more restricted release state and visibility than its predecessor.                                                                                      | Currently, the check forbids to mark CDS view elements as \#DECOMMISSIONED. Special approval for this can be granted by means of an exemption. |
| Deprecation / Decommissioning | If decommissiong is announced for an element or association using annotation `@API.element.decommissioningPlannedForYearMonth`, its value must be given in the format YYYY-MM.                                                                                                             |                                                                                                                                                |
| Deprecation / Decommissioning | Decommissioning can be announced for elements and associations with `@API.element.releaseState` \#DEPRECATED only.                                                                                                                                                                         |                                                                                                                                                |

### Contract C2

| Property                      | Check                                                                                                                                                                                                                                                                                      | Remark                                                                                                                                         |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Entity                        | Name must not start with P\_, being the naming convention for private views.                                                                                                                                                                                                               |                                                                                                                                                |
| Entity                        | Name must not start with E\_, being the naming convention for extension include views.                                                                                                                                                                                                     |                                                                                                                                                |
| Entity                        | Must not be registered as extension include view in transaction SCFD_REGISTRY.                                                                                                                                                                                                             |                                                                                                                                                |
| Entity                        | A parallel release for contract C1 is not possible.                                                                                                                                                                                                                                        |                                                                                                                                                |
| Entity                        | Only entities of source type view, projection view, view entity, abstract entity, and custom entity can be released (see domain DDDDLSRCTYPE).                                                                                                                                             |                                                                                                                                                |
| Entity                        | Must not have an implicit select list (i.e. SELECT is not allowed).                                                                                                                                                                                                                        |                                                                                                                                                |
| Elements                      | CDS enumerated types that serve as typing for exposed fields must also be released for contract C2.                                                                                                                                                                                        |                                                                                                                                                |
| Parameters                    | Type of parameter must be either a released data element, CDS simple type, or a built-in data type (e.g. abap.char).                                                                                                                                                                       |                                                                                                                                                |
| Parameters                    | CDS simple type enums that serve as typing for exposed parameters must also be released for contract C2.                                                                                                                                                                                   |                                                                                                                                                |
| Associations                  | If the association target of a public association has release state Deprecated, the association alias in the projection list must be marked accordingly using annotation `@API.element.releaseState`: \#DEPRECATED.                                                                        |                                                                                                                                                |
| Associations                  | If the CDS entity does not contain a key element, the association target must be released for contract C2.                                                                                                                                                                                 |                                                                                                                                                |
| Annotations                   | As defined by meta-annotation `@CompatibilityContract.usageAllowed` in the annotation definition file of the respective annotation.                                                                                                                                                        |                                                                                                                                                |
| Annotations                   | If an element or public association is marked as deprecated or decommissioned with the help of annotation @API.element.releaseState and its values \#DEPRECATED or \#DECOMMISSIONED respectively, a successor must be specified using annotation `@API.element.successor: '<ElementRef>'`. |                                                                                                                                                |
| Annotations                   | Also when inherited from a view below, the annotations @API.element.releaseState and `@API.element.successor: '<ElementRef>'` must be set locally in each released view to document deprecation in the source code.                                                                        |                                                                                                                                                |
| Deprecation / Decommissioning | The successor element or public association specified with `@API.element.successor: '<ElementRef>'` must exist and must not have a more restricted release state and visibility than its predecessor.                                                                                      | Currently, the check forbids to mark CDS view elements as \#DECOMMISSIONED. Special approval for this can be granted by means of an exemption. |
| Deprecation / Decommissioning | If decommissiong is announced for an element or association using annotation `@API.element.decommissioningPlannedForYearMonth`, its value must be given in the format YYYY-MM.                                                                                                             |                                                                                                                                                |
| Deprecation / Decommissioning | Decommissioning can be announced for elements and associations with `@API.element.releaseState` \#DEPRECATED only.                                                                                                                                                                         |                                                                                                                                                |

#### CDS Scalar Function Definitions (DSFD)

### Contract C1

| Property   | Check                                                                                                                            | Remark |
|------------|----------------------------------------------------------------------------------------------------------------------------------|--------|
| Parameters | If data elements or CDS types are used for the parameters of the function, those types also need to be released for contract C1  |        |
| Parameters | The built-in type abap.clnt may not be used                                                                                      |        |
| Result     | If a data element or a CDS type is used for the return type of the function, this type also needs to be released for contract C1 |        |

### Contract C2

| Property   | Check                                                                                                                            | Remark                                                |
|------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Parameters | If data elements or CDS types are used for the parameters of the function, those types also need to be released for contract C2  |                                                       |
| Parameters | The built-in type abap.clnt may not be used                                                                                      |                                                       |
| Parameters | No generic types may be used                                                                                                     |                                                       |
| Parameters | No reference handling with the addition WITH REFERENCE TYPE may be defined                                                       | This also applies for the result type of the function |
| Result     | If a data element or a CDS type is used for the return type of the function, this type also needs to be released for contract C2 |                                                       |

#### CDS Scalar Function Implementation References (DSFI)

### Contract C1

| Property       | Check                                                                        | Remark                                                   |
|----------------|------------------------------------------------------------------------------|----------------------------------------------------------|
| Function       | The used CDS scalar function definition needs to be released for contract C1 |                                                          |
| AMDP Reference | The referenced AMDP function implementation needs to exist                   | This applies only for SQL-based function implementations |

### Contract C2

| Property       | Check                                                                        | Remark                                                   |
|----------------|------------------------------------------------------------------------------|----------------------------------------------------------|
| Function       | The used CDS scalar function definition needs to be released for contract C2 |                                                          |
| AMDP Reference | The referenced AMDP function implementation needs to exist                   | This applies only for SQL-based function implementations |

#### Check Categories (CHKC)

### Contract C1

| Property        | Check            | Remark |
|-----------------|------------------|--------|
| Parent Category | must be released |        |

#### Check Objects (CHKO)

### Contract C1

| Property           | Check                            | Remark |
|--------------------|----------------------------------|--------|
| Category           | must be released                 |        |
| Implementing Class | must not be marked as 'internal' |        |

#### Check Variants (CHKV)

### Contract C1

| Property | Check            | Remark |
|----------|------------------|--------|
| Checks   | must be released |        |

#### Classes (CLAS)

see section *Classes (CLAS) and Interfaces (INTF)*

#### Classes (CLAS) and Interfaces (INTF)

### Contract C1

| Property            | Check                                                                               | Remark                                                                                             |
|---------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Class               | must be final                                                                       |                                                                                                    |
| Class               | instantiation must be private                                                       |                                                                                                    |
| Attributes          | referenced types must be released                                                   | applies to public attributes only                                                                  |
| Attributes          | if their type is a BDEF derived type, the underlying BDEF must be released          |                                                                                                    |
| Constants           | referenced types must be released                                                   | applies to public constants only                                                                   |
| Methods             | may raise class-based exceptions only                                               |                                                                                                    |
| Methods             | RAP transactional contract must be specified                                        | applies to public methods only                                                                     |
| Method Parameters   | referenced types must be released                                                   |                                                                                                    |
| Exceptions          | must be class-based exceptions                                                      |                                                                                                    |
| Types               | line types of referenced table types must be released                               | any other types do not need to be released                                                         |
| Types               | for BDEF derived types, the underlying BDEF must be released                        |                                                                                                    |
| Method AMDP Options | client option must be either `CDS SESSION CLIENT DEPENDENT` or `CLIENT INDEPENDENT` | applies to AMDP classes and interfaces only; not setting any client handling option is not allowed |

### Best Practices

To ensure functional correctness, stability and security of your API as well as the testability of applications which make use of your API, released classes and interfaces should meet the following requirements.

### Signature

To ensure that your functionality can be mocked using the *ABAP test double framework*, all publicly addressable methods, attributes, types, events and aliases should be defined in an interface.

The only public element of a released class should be the static factory method GET_INSTANCE or CREATE_INSTANCE, returning a reference to this interface (see section *Instantiation* also).

To decouple instantiation from implementation, consider releasing a dedicated factory class only, and keep the functionality in one or more separate classes which implement the interface returned by the factory method described below.

### Instantiation

A released class should be defined as CREATE PRIVATE by default.

Provide a public static factory method GET_INSTANCE or CREATE_INSTANCE instead, returning a reference to the interface described in section *Signature*.

This way, users of your API can mock your functionality easily using the *ABAP test double framework*.

If no instance-specific data is kept in member variables of the implementing class, use a singleton pattern with GET_INSTANCE method.

### Referenced Types

For the data types referenced by the publicly addressable parameters and attributes of released classes and interfaces, there are two main options:

1.  Refer to released ABAP development objects. This option is preferable for data types that are used throughout a whole application area.

2.  Define the data types in a self-contained manner, i.e. directly in the interface using the `TYPES` statement. This is the first choice for data types of stand-alone APIs that perform dedicated tasks like e.g. JSON handling.

If ABAP-defined types are shared among a set of released classes and interfaces, a central interface with TYPES declarations should be introduced and released accordingly.

### Exceptions

Use class-based exceptions and provide one or more dedicated exception classes for the API, inheriting from \<CX_STATIC_CHECK\> and implementing the interface \<IF_T100_DYN_MSG\>. To associate a message to an exception, either use text IDs with reference to T100 messages, or alternatively use the statement [`RAISE EXCEPTION TYPE cx_class` with the addition `MESSAGE`](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/index.htm?file=abapraise_exception_class.htm). In general, exception classes of released APIs should be FINAL.

### Documentation

Released classes and interfaces should be documented in English using [ABAP Doc](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/abendoccomment.htm). Document all public methods and their parameters as well as all public attributes. An example for ABAP Doc can be found in the released class \<CL_ABAP_API_STATE\> and the corresponding interface \<IF_ABAP_API_STATE\>.

### Contract C4

Note: Everything defined in a class/interface released for contract C4 can be used in other AMDP methods also.

| Property                        | Check                                                       | Remark                                                                                                  |
|---------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Class                           | must be released for contract C1 also                       |                                                                                                         |
| Class                           | must be final                                               |                                                                                                         |
| Class                           | must not be abstract                                        |                                                                                                         |
| Class                           | must not have a super class                                 |                                                                                                         |
| Implemented Interfaces          | all implemented interfaces must be released for contract C4 |                                                                                                         |
| Types                           | Types must be usable in AMDP methods                        | i.e. it should be possible to use all types defined in a C4 released class/interface for AMDP parameter |
| Types                           | no `C`/`N` types with length \>5000                         |                                                                                                         |
| Types                           | no reference types                                          |                                                                                                         |
| Types                           | no `DF16_SCL` and `DF34_SCL`                                |                                                                                                         |
| Types                           | no nested types                                             |                                                                                                         |
| Types                           | no boxed components                                         |                                                                                                         |
| Types                           | no enums                                                    |                                                                                                         |
| Table Types                     | no non structured line types                                | e.g. `TYPES tt TYPE STANDARD TABLE OF string` is not allowed                                            |
| Table Types                     | no nested line type                                         |                                                                                                         |
| Table Types                     | no box in line type                                         |                                                                                                         |
| Table Types                     | no enum in line type                                        |                                                                                                         |
| Methods                         | all methods must be AMDP methods                            | methods in interfaces are checked as if they are AMDP methods                                           |
| Methods                         | `FOR DDL OBJECT` addition is not allowed                    |                                                                                                         |
| Methods                         | `FOR CDS TABLE FUNCTION` addition is not allowed            |                                                                                                         |
| Methods                         | `FOR CDS SCALAR FUNCTION` addition is not allowed           |                                                                                                         |
| Method Parameters               | All parameter types must be released for contract C4        | Types defined in C4-released classes/interfaces are allowed                                             |
| Method Parameters               | must not be typed with `LIKE`                               |                                                                                                         |
| Method Parameters               | no `CONNECTION` parameter                                   |                                                                                                         |
| Method Parameters               | no `CALL_HINTS` parameter                                   |                                                                                                         |
| Method Parameter Default Values | default values must not refer to other classes              |                                                                                                         |
| Method AMDP Options             | AMDP must be `READ-ONLY`                                    |                                                                                                         |
| Method Exceptions               | exceptions must start with `CX_AMDP`                        |                                                                                                         |
| Events                          | events are not allowed                                      |                                                                                                         |
| Attributes                      | attributes are not allowed                                  |                                                                                                         |
| Constants                       | constants are not allowed                                   |                                                                                                         |
| Constructors                    | constructors are not allowed                                |                                                                                                         |
| Constructors                    | class constructors are not allowed                          |                                                                                                         |

#### Data Definitions (DDLS)

see section *CDS Entities (DDLS/CDS_STOB)*

#### Email Templates (SMTG)

### Contract C1

| Property              | Check                                                                                    | Remark |
|-----------------------|------------------------------------------------------------------------------------------|--------|
| Referenced CDS View   | CDS view must be released for contract C1                                                |        |
| Template Input Fields | input fields must be from associated CDS views that are released for contract C1 as well |        |

#### Enhancement Spots (ENHS)

see section *BAdI Definitions (ENHS/BADI_DEF)*

#### Enterprise Services - Proxy Objects (SPRX)

### Contract C2

| Property      | Check                              | Remark                                                                                                                                               |
|---------------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Object        | object must exist                  |                                                                                                                                                      |
| Header        | header must exist                  |                                                                                                                                                      |
| Object Type   | object type has to be CLAS or INTF | SPRX has multiple subtypes but only the two main object types are allowed; if the object type is INTF, also the corresponding WEBI object is checked |
| Release State | API release states have to match   | if the SPRX object is of object type INTF, the API release states of the corresponding WEBI and SPRX have to match                                   |

#### Event Consumption Models (EEEC)

### Contract C1

| Property         | Check                                                                                                                         | Remark                                                                    |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Consumer Class   | must exist                                                                                                                    |                                                                           |
| Consumer Class   | must be syntactically correct                                                                                                 |                                                                           |
| Consumer Class   | must implement interface */iwxbe/if_consumer*                                                                                 |                                                                           |
| Event Types      | every event type name must not exceed the length of *255* characters                                                          |                                                                           |
| Event Types      | every event type name must consist of at least one segment, multiple segments must be separated via '.'                       | corresponding regular expression: (\[A-Za-z0-9\]{1,})(.\[A-Za-z0-9\]{1,}) |
| Event Types      | every event type name segment must contain letters and/or numbers and must not contain special characters                     |                                                                           |
| Event Types      | every event type name segment must contain at least one character                                                             |                                                                           |
| Entity Hierarchy | for every event type an entity, its dependent entities and behaviour definitions must exist and must be syntactically correct |                                                                           |

#### Function Groups (FUGR)

see section *Function Modules (FUGR/FUNC)*

#### Function Modules (FUGR/FUNC)

### Contract C1

| Property        | Check                                                       | Remark                                                                                              |
|-----------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Function Module | must not be released with visibility *Use in Key User Apps* | the statement CALL FUNCTION is not part of the syntax of ABAP language version *ABAP for Key Users* |
| Parameters      | referenced type must be released                            |                                                                                                     |
| Exceptions      | referenced type of a class-based exception must be released |                                                                                                     |

#### Interfaces (INTF)

see section *Classes (CLAS) and Interfaces (INTF)*

#### Predefined Custom Fields (PCFN)

### Contract C1

| Property                        | Check                                                                                                                      | Remark                                         |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Node                            | corresponding behavior definition entity must have an alias                                                                |                                                |
| Node                            | corresponding behavior definition entity must not have BOPF draft                                                          |                                                |
| Node                            | corresponding behavior definition entity must have 'mapping corresponding' if node has persistence content object          |                                                |
| Node Name                       | must exist as behavior definition entity                                                                                   |                                                |
| Node Name                       | base object of the corresponding CDS view must be c1 released for cloud development                                        |                                                |
| Node Primary Database Table     | must match the persistence database table of the behavior definition entity                                                |                                                |
| Node Primary Database Table     | must be client-dependent                                                                                                   |                                                |
| Node Primary Database Table     | must be transparent table                                                                                                  |                                                |
| Node Field Name Prefix          | must not be initial                                                                                                        |                                                |
| Node Field Name Prefix          | must be part of PCFN namespace                                                                                             |                                                |
| Node Field Name Prefix          | must not be part of customer namespace                                                                                     |                                                |
| Node Field Name Prefix          | must contain only characters                                                                                               |                                                |
| Node Field Name Prefix          | must be unique                                                                                                             |                                                |
| Node Persistence Content Object | must not be initial                                                                                                        |                                                |
| Node Persistence Content Object | must exist as data dictionary structure                                                                                    |                                                |
| Node Persistence Content Object | must be included in node primary db table                                                                                  |                                                |
| Node Persistence Content Object | must have enhancement category deep or character and numeric                                                               |                                                |
| Node Persistence Content Object | must have enhancement category deep if node field of technical type string or short string exists                          |                                                |
| Node Fields                     | at least one must exist                                                                                                    |                                                |
| Node Field Names                | field name must be unique in the node                                                                                      |                                                |
| Node Field Names                | field must begin with node fieldname prefix                                                                                |                                                |
| Node Field Names                | name must not exceed 28 characters                                                                                         |                                                |
| Node Field Types                | must be one of amount, quantity, boolean, number, date, time, timestamp, numerical text, string, short_string or character |                                                |
| Node Field Lengths              | must only be defined for types with varying length                                                                         |                                                |
| Node Field Lengths              | must not exceed the maximum length                                                                                         | type-dependent                                 |
| Node-Related CDS View           | corresponding CDS view must be able to access the node primary database table                                              | there might be a stack of CDS views in between |
| Node-Related CDS View           | corresponding CDS view must be c1-released for use in cloud development                                                    |                                                |
| Node-Related CDS View           | corresponding CDS view must be extensible                                                                                  |                                                |
| Node-Related CDS View           | base object alias of the corresponding CDS view must be usable in extensions                                               |                                                |
| Node-Related CDS View Name      | must be unique in the node                                                                                                 |                                                |
| Node Enhancements               | enhancement of type append must exist                                                                                      |                                                |
| Node Enhancements               | an enhancement for each node related CDS view must exist                                                                   |                                                |
| Node Enhancements               | corresponding development object must exist                                                                                |                                                |
| Node Enhancements               | corresponding development object must comply to the definition                                                             | node fields                                    |
| Node Enhancements               | corresponding development object must be part of the same software component                                               |                                                |
| Node Enhancements               | corresponding development object must be c1 released for cloud development                                                 |                                                |
| Node Enhancement Object Names   | must be unique in the node                                                                                                 |                                                |
| Node Enhancement Object Names   | must start with PCFN namespace                                                                                             |                                                |
| Node Enhancement Object Names   | must contain only characters                                                                                               |                                                |

#### Service Definitions (SRVD)

### Contract C0

| Property                  | Check                                                                                                                                                                                                      | Remark |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Source Type               | only CDS service definitions (SRVD/SRV) can be released, in other words the service definition type must be a definition ('S') and not an extension ('X')                                                  |        |
| Extensibility Annotation  | extensibility must be defined with the annotation '`@AbapCatalog.extensibility.extensible`' or '`@AbapCatalog.extensibility.extensible`: true'                                                             |        |
| Provider Contract         | at least one provider contract (ina, sql, odata) must be specified                                                                                                                                         |        |
| Exposed Entity with Alias | the C0-release is possible only if all exposed entities use the correct namespace prefix; for repository objects developed in an SAP system, this means that the entity names must not start with YY or ZZ |        |

#### SQL Services (SQL1)

### Contract C1

| Property    | Check                                 | Remark |
|-------------|---------------------------------------|--------|
| SQL Service | must be released for contract C2 also |        |

#### Structures and Database Tables (TABL)

### Contract C0

C0-release for tables and structures with visibility *Use in Key User Apps* is available SAP-internally only. The corresponding checks are performed in transaction SCFD_REGISTRY and as ATC checks like described in the *Custom Fields Adoption Guideline*.

For tables and structures with visibility *Use in Cloud Development*, see below.

| Property            | Check                                                                                                                                              | Remark                                                                                                                                       |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Extensibility Quota | A quota needs to be defined with the annotations'`@AbapCatalog.enhancement.quotaMaximumFields`' and '`@AbapCatalog.enhancement.quotaMaximumBytes`' | This is to ensure that technical restrictions on the size of a DDIC table or structure are not violated by the addition of extension fields. |
| Field Suffix        | A field suffix needs to be set for the extensible TABL object with the annotation '`@AbapCatalog.enhancement.fieldSuffix`'                         | The field suffix ensures that extension field names of different structures / tables do not collide when they are included together.         |

### Contract C1

| Property             | Check                                           | Remark                                                                                                                                                                                |
|----------------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enhancement Category | must not be *Not classified*                    |                                                                                                                                                                                       |
| Table Category       | table must be a structure                       | this restriction applies to SAP systems only; in customer systems, database tables can be released as well                                                                            |
| Components           | typing method *Type ... Boxed* is not supported | this applies to structures only                                                                                                                                                       |
| Complex Components   | referenced type must be released                | this applies to structures only; complex components are components with typing method *Type* and typed with a structure or table type, or components with typing method *Type Ref To* |

### Contract C3

| Property       | Check                                                                                                                                                                                                                | Remark |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Table Category | table must be a database table                                                                                                                                                                                       |        |
| Delivery Class | must be *Customizing, maintenance only by customer, no SAP imports (C)*, or *Customizing, protected against SAP updates, only inserts allowed (G)*, or *Control table, SAP and customer have separate key areas (E)* |        |

#### Table Types (TTYP)

### Contract C1

| Property | Check                            | Remark |
|----------|----------------------------------|--------|
| Row Type | referenced type must be released |        |

#### Views (VIEW)

### Contract C3

| Property           | Check                                                                                                                                                                                                                | Remark |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| View Class         | must be either *Maintenance View (C)* or *View Variant (V)*                                                                                                                                                          |        |
| Delivery Class     | must be *Customizing, maintenance only by customer, no SAP imports (C)*, or *Customizing, protected against SAP updates, only inserts allowed (G)*, or *Control table, SAP and customer have separate key areas (E)* |        |
| View Maintenance   | must not be restricted to read-only access                                                                                                                                                                           |        |
| Customizing Object | the view must have a corresponding customizing object                                                                                                                                                                |        |
| Customizing Object | the view's customizing object must be automatically adjustable                                                                                                                                                       |        |
| Fields             | referenced types must be released                                                                                                                                                                                    |        |

#### Virtual Endpoint Definitions - Service Definitions (WEBI)

### Contract C2

| Property      | Check                                                           | Remark                                                                  |
|---------------|-----------------------------------------------------------------|-------------------------------------------------------------------------|
| Endpoint Type | virtual Endpoint of WEBI must not be of type FUNC, FUGR or BAPI | only proxy based WEBIs are allowed                                      |
| Release State | API release states have to match                                | the API release states of WEBI and the corresponding SPRX have to match |
