---
title: "Compatibility Checks for Released APIs"
source_file: abenrestricted_apis_atc_compa.html
section: "ABAP APIs > Release Contracts > Contract Checks for Released APIs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Compatibility Checks for Released APIs

The following shows the documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) of the [ATC](../../abap-glossary/abenatc_glosry.md) check `API_COMPATIBILITY`:

## API_COMPATIBILITY

## What is checked?

Development objects like CDS views, classes or interfaces can be released as stable APIs for a dedicated purpose.

Released APIs must not be changed incompatibly, because these changes can lead to syntax errors or runtime errors in source code and objects based on these APIs. To detect incompatible changes between software releases, the corresponding compatibility ATC checks are executed.

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

Each released API is checked for incompatible changes between releases, depending on the stability requirements of the assigned compatibility contract. These checks comprise of *basic checks* (e.g. detection of deleted elements) and *domain-specific checks* (e.g. detection of annotation changes in CDS views), provided by different application components.

**Note**: The compatibility ATC check is based on a comparison of the current API façades with their layout in relevant previous software releases. These so-called API snapshots are created per software component, ideally directly before shipment, using the app *Manage API Snapshots*. SAP-internally, API snapshots are available in dedicated ATC systems, but not necessarily in development and test systems. In systems without API snapshots, the check does not report any findings.

## Procedure

### Undoing Incompatible Changes

Each check message describes an incompatible change in a development object which was released as API.

Findings must be resolved by undoing the detected incompatible change. Undo the incompatible change by restoring the affected part of the API in the way it was previously shipped to the customer.

**Note**: If the checked development object is a package, the check messages refer to objects which were formerly contained in this package but were deleted although they have been released as APIs.

### Example

An element was removed from the projection list of a released CDS view. If this element is used in a custom CDS view based on the released CDS view, this would cause ABAP dictionary activation errors during the upgrade of the customer system.

*Check message*: Element \<ElementName\> was removed.

*Remedy*: Add this element to the projection list again, using the same data type as before.

### Exemptions for Incompatible Changes

In some cases, incompatible changes can't be avoided, but due to their potential criticality, evaluation by an expert is required.

## Checks

### Object-Type-Independent Checks

| Category      | Checks                                                   |
|---------------|----------------------------------------------------------|
| Existence     | A released object must not be deleted.                   |
| Release State | A released object must stay released (or be deprecated). |

### Object-Type-Specific Checks

### Application Job Catalog Entries (SAJC)

### Contract C1

| Property                         | Check                                                      | Remark                                                          |
|----------------------------------|------------------------------------------------------------|-----------------------------------------------------------------|
| Report/Class with Execute Method | name must not be changed                                   |                                                                 |
| Report/Class with Execute Method | must not be removed                                        |                                                                 |
| Report/Class Parameters          | must not be removed                                        | relevant for all parameters which are used in the catalog entry |
| Report/Class Parameters          | data type must not be changed                              |                                                                 |
| Report/Class Parameters          | length must not be reduced                                 |                                                                 |
| Report/Class Parameters          | number of decimals must not be reduced                     |                                                                 |
| Report/Class Parameters          | must not be changed from value range to single value       | e.g. by changing from *SELECT-OPTIONS* to *PARAMETERS*          |
| Report/Class Parameters          | must not be changed to mandatory                           |                                                                 |
| Report/Class Parameters          | must not be created as mandatory                           |                                                                 |
| Report/Class Parameters          | must not be changed to hidden                              |                                                                 |
| Report/Class Parameters          | must not be changed to a checkbox                          | by adding *AS CHECKBOX* to the *PARAMETERS* command             |
| Report/Class Parameters          | must not be changed to a radio button                      | by adding *RADIOBUTTON GROUP* to the *PARAMETERS* command       |
| Check Class                      | must not be changed                                        |                                                                 |
| Check Class                      | must not be removed                                        |                                                                 |
| Check Class                      | must not be added                                          |                                                                 |
| Scoping-Relevant                 | must not be set                                            |                                                                 |
| Spool Display                    | must not be changed from *Generic spool display* to *None* |                                                                 |
| Log Handling                     | must not be changed                                        |                                                                 |
| Parameters                       | must not be removed                                        |                                                                 |
| Parameters                       | *Mandatory* flag must not be set                           |                                                                 |
| Parameters                       | must not be created with *Mandatory* flag set              |                                                                 |
| Parameters                       | *Hidden* flag must not be set                              |                                                                 |
| Parameters                       | *Read-Only* flag must not be set                           |                                                                 |
| Parameters                       | *Screen Element* must not be changed to *Checkbox*         |                                                                 |
| Parameters                       | *Screen Element* must not be changed to *Radio Button*     |                                                                 |

#### Application Job Templates (SAJT)

### Contract C1

| Property          | Check               | Remark |
|-------------------|---------------------|--------|
| Job Catalog Entry | must not be changed |        |

#### Application Log Objects (APLO)

### Contract C1

| Property   | Check               | Remark                      |
|------------|---------------------|-----------------------------|
| Subobjects | must not be removed |                             |
|            | must not be added   | only if no subobjects exist |

#### BAdI Definitions (ENHS/BADI_DEF)

### Contract C1

| Property        | Check                                                                                | Remark |
|-----------------|--------------------------------------------------------------------------------------|--------|
| BAdI Definition | must not be deleted                                                                  |        |
| BAdI Definition | assigned interface must not be changed                                               |        |
| BAdI Definition | instantiation mode must not be changed                                               |        |
| BAdI Definition | flag 'Multiple use' must not be changed                                              |        |
| BAdI Definition | assignment of the fallback class must not be changed                                 |        |
| BAdI Definition | flag 'Limited filter use' must not be changed                                        |        |
| BAdI Definition | flag 'SAP internal' must not be changed                                              |        |
| BAdI Definition | flag 'AMDP BAdI' must not be changed                                                 |        |
| BAdI Definition | assigned example classes must not be changed in case of a release for key-user tools |        |
| Filters         | must not be deleted                                                                  |        |
| Filters         | flag 'Only constant filter values' must not be changed                               |        |
| Filter Type     | must not be changed                                                                  |        |

#### Behavior Definitions (BDEF)

### Contract C0

| Property              | Check                                                                                                                                                   | Remark                                                |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Header                | The property "extensible" must not be removed.                                                                                                          |                                                       |
| Header                | The property "extensible with determinations on modify" must not be removed.                                                                            |                                                       |
| Header                | The property "extensible with determinations on save" must not be removed.                                                                              |                                                       |
| Header                | The property "extensible with validations on save" must not be removed.                                                                                 |                                                       |
| Header                | The property "extensible with additional save" must not be removed.                                                                                     |                                                       |
| Header                | The BDEF must not be changed from "managed" to "unmanaged" or vice versa.                                                                               |                                                       |
| Header                | The property "with draft" must not be removed or added.                                                                                                 |                                                       |
| Header                | "own authorization context" must not be removed (even if it is empty).                                                                                  |                                                       |
| Header                | The base BO must not be changed.                                                                                                                        | This is relevant for interfaces and projections only. |
| Entities              | The property "extensible" must not be changed.                                                                                                          |                                                       |
| Entities              | An extensible entity must not be removed.                                                                                                               |                                                       |
| Entities              | If an alias name has been defined for an entity, it must not change.                                                                                    | This is relevant for interfaces and projections only. |
| Entities              | The property "cached" must not be removed.                                                                                                              |                                                       |
| Entities              | The attribute "persistent table ..." must not change.                                                                                                   |                                                       |
| Entities              | The draft query view ("draft table X query ...") must not change.                                                                                       |                                                       |
| Entities              | The attribute "changedocuments ..." must not be removed if the entity has the CDS annotation "`@AbapCatalog.extensibility.allowNewCompositions`: true". |                                                       |
| Fields                | Key fields must not be added or removed and their order must not change. The data type and the length of a key field must not change.                   |                                                       |
| Fields                | The property "notrigger" must not be added if extensions can have determinations or validations.                                                        |                                                       |
| Associations          | The property "notrigger" must not be added if extensions can have determinations or validations.                                                        |                                                       |
| Associations          | The property "with hierarchy" must not be added or deleted.                                                                                             | This is relevant for abstract entities only.          |
| Draft Action Activate | Adding "optimized" is incompatible.                                                                                                                     |                                                       |
| Determine Actions     | The property "extensible" must not be removed.                                                                                                          |                                                       |
| Determine Actions     | Extensible determine actions must not be removed.                                                                                                       |                                                       |
| Mappings              | The property "extensible" must not be removed.                                                                                                          |                                                       |
| Mappings              | The property "corresponding" must not be removed.                                                                                                       |                                                       |
| Mappings              | Extensible mappings must not be removed.                                                                                                                |                                                       |

### Contract C1

| Property            | Check                                                                                                                                                                        | Remark                                              |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| Header              | The property "with draft" must not be removed or added.                                                                                                                      |                                                     |
| Header              | The property "collaborative draft" must not be removed.                                                                                                                      |                                                     |
| Header              | The property "use side effects" must not be removed.                                                                                                                         |                                                     |
| Header              | The property "dependent" must not be removed or added.                                                                                                                       |                                                     |
| Header              | The property "with hierarchy like entity" must not be removed.                                                                                                               |                                                     |
| Header              | The property "with hierarchy" must not be removed.                                                                                                                           |                                                     |
| Header              | The property "with privileged mode" must not be removed.                                                                                                                     |                                                     |
| Entities            | The behavior definition for an entity must not be removed.                                                                                                                   |                                                     |
| Entities            | If an alias name has been defined for an entity, it must not be changed.                                                                                                     |                                                     |
| Entities            | If an external name has been defined for an entity, it must not be changed.                                                                                                  |                                                     |
| Entities            | The property "etag" must not be removed. (But it is compatible to change "etag dependent \[by ...\]" to "etag master ..." and vice versa.)                                   |                                                     |
| Entities            | The property "late numbering" must not be removed or added.                                                                                                                  |                                                     |
| Entities            | The operation "create" must not be disabled.                                                                                                                                 |                                                     |
| Entities            | The operation "update" must not be disabled.                                                                                                                                 |                                                     |
| Entities            | The operation "delete" must not be disabled.                                                                                                                                 |                                                     |
| Entities            | The operation "read" must not be disabled.                                                                                                                                   |                                                     |
| Entities            | The property "with control" must not be removed or added.                                                                                                                    | Relevant for abstract entities only.                |
| Scalar entities     | The specified field must not change.                                                                                                                                         |                                                     |
| Fields              | The property "mandatory" must not be added (unless there was no create nor update previously).                                                                               |                                                     |
| Fields              | The property "mandatory:create" must not be added (unless there was no create previously).                                                                                   | "mandatory" → "mandatory:create" is not compatible. |
| Fields              | The property "mandatory:update" must not be added (unless there was no update previously).                                                                                   | "mandatory" → "mandatory:update" is not compatible. |
| Fields              | The property "mandatory:execute" must not be added.                                                                                                                          | Relevant for abstract entities only.                |
| Fields              | The property "readonly" must not be added (unless the field is new or was suppressed previously or there was no create nor update previously).                               |                                                     |
| Fields              | The property "readonly:create" must not be added (unless the field is new or was suppressed previously or there was no create previously).                                   | "readonly" → "readonly:create" is compatible.       |
| Fields              | The property "readonly:update" must not be added (unless the field is new or was suppressed previously or there was no update previously).                                   | "readonly" → "readonly:update" is compatible.       |
| Fields              | The property "suppress" must not be added (unless the field is new).                                                                                                         |                                                     |
| Associations        | An association must not be disabled.                                                                                                                                         |                                                     |
| Associations        | The operation "create" must not be removed nor become internal.                                                                                                              |                                                     |
| Associations        | If an abbreviation has been defined, it must not be changed.                                                                                                                 |                                                     |
| Associations        | The property "with draft" must not be removed.                                                                                                                               |                                                     |
| Associations        | The property "unavailable read" must not be added.                                                                                                                           |                                                     |
| Associations        | The property "with hierarchy" must not be removed or added.                                                                                                                  | Relevant for abstract entities only.                |
| Associations        | The property "mandatory:execute" must not be added.                                                                                                                          | Relevant for abstract entities only.                |
| Associations        | The property "to dependent" must not be removed or added.                                                                                                                    |                                                     |
| Associations        | A link action must not be changed or removed.                                                                                                                                |                                                     |
| Associations        | An unlink action must not be changed or removed.                                                                                                                             |                                                     |
| Associations        | An inverse function must not be changed or removed.                                                                                                                          |                                                     |
| Actions/Functions   | An action/function must not be removed nor become internal.                                                                                                                  |                                                     |
| Actions/Functions   | In the action/function name, upper/lower case must not be changed.                                                                                                           |                                                     |
| Actions/Functions   | If an external name has been defined, it must not be changed.                                                                                                                |                                                     |
| Actions/Functions   | The property "static" must not be changed.                                                                                                                                   |                                                     |
| Actions/Functions   | The property "repeatable" must not be changed.                                                                                                                               |                                                     |
| Actions/Functions   | The result type must not be changed.                                                                                                                                         |                                                     |
| Actions/Functions   | The cardinality of the result must not change.                                                                                                                               |                                                     |
| Actions/Functions   | The property "selective" of the result must not be deleted.                                                                                                                  |                                                     |
| Actions/Functions   | If an external name for the result has been defined, it must not be changed.                                                                                                 |                                                     |
| Actions/Functions   | The parameter type must not be changed.                                                                                                                                      |                                                     |
| Actions/Functions   | If a parameter is added, it must be deep.                                                                                                                                    |                                                     |
| Actions/Functions   | If a parameter is added, it must not have fields or associations with "mandatory:execute".                                                                                   |                                                     |
| Actions/Functions   | For a parameter/result, the property "deep" must not be removed. Adding "deep" is allowed only if the parameter/result has "with hierarchy like entity" in its BDEF.         |                                                     |
| Actions/Functions   | The properties "save(...)" must not change, except that save(finalize) → save(finalize,adjustnumbers) and save(adjustnumbers) → save(finalize,adjustnumbers) are compatible. |                                                     |
| Actions/Functions   | The property "default factory" must not be deleted.                                                                                                                          |                                                     |
| Actions/Functions   | A factory action must not become a non-factory action and vice versa.                                                                                                        |                                                     |
| Actions/Functions   | The entity that is created by a factory action must not change.                                                                                                              |                                                     |
| Actions/Functions   | A determine action must remain a determine action.                                                                                                                           |                                                     |
| Actions/Functions   | An action must not become a function and vice versa.                                                                                                                         |                                                     |
| Events              | An event must not be removed.                                                                                                                                                |                                                     |
| Events              | In the event name, upper/lower case must not be changed.                                                                                                                     |                                                     |
| Events              | The parameter type must not be changed.                                                                                                                                      |                                                     |
| Events              | The property "deep" of the parameter must not be removed. Adding "deep" is allowed only if the parameter has "with hierarchy like entity" in its BDEF.                       |                                                     |
| Events              | The property "for side effects" must not be removed or added.                                                                                                                |                                                     |
| Secondary/pure keys | Secondary and pure keys must not be removed.                                                                                                                                 |                                                     |
| Secondary/pure keys | A secondary key must not become a pure key.                                                                                                                                  | The opposite is compatible.                         |
| Secondary/pure keys | If a key function has been defined, it must not be changed.                                                                                                                  |                                                     |
| Secondary/pure keys | No fields can be added to or removed from an existing key.                                                                                                                   |                                                     |
| Mappings            | A mapping must not be removed.                                                                                                                                               |                                                     |
| Mappings            | The property "corresponding" must not be removed or added.                                                                                                                   |                                                     |
| Foreign entities    | A foreign entity must not be removed.                                                                                                                                        |                                                     |
| Foreign entities    | The alias name must not be changed.                                                                                                                                          |                                                     |

#### CDS Entities (DDLS/CDS_STOB)

### Contract C0

C0-release for CDS entities with visibility *Use in Key User Apps* is available SAP-internally only. The corresponding checks are performed in transaction SCFD_REGISTRY and as ATC checks like described in the *Custom Fields Adoption Guideline*.

For CDS entities with visibility *Use in Cloud Development*, see below.

| Property                           | Check                                                                                                                                                                                                    | Remark                                                                                                                                              |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| DDLS Source Type                   | The DDLS source type may not be changed.                                                                                                                                                                 | Customer extends could break, because the feature set of extends differs between different source types.                                            |
| Key Fields                         | Key fields of a CDS entity may not be changed. This includes the names, the position and the datatype of the key fields. Furthermore, no key fields may be added or removed.                             |                                                                                                                                                     |
| Client-Dependency                  | A released client-dependent CDS entity may not be changed to a client-independent entity.                                                                                                                |                                                                                                                                                     |
| Extensible Property                | The annotation `@AbapCatalog.extensibility.extensible` and its value may not be changed.                                                                                                                 |                                                                                                                                                     |
| Element Suffix                     | The annotation `@AbapCatalog.extensibility.elementSuffix` and it's value must not be changed.                                                                                                            |                                                                                                                                                     |
| Extensibility Quota                | The assigned extensibility quota may not be reduced. This means:                                                                                                                                         |                                                                                                                                                     |
| Extensibility Quota                | The value of the annotation `@AbapCatalog.extensibility.quota.maximumFields` may not be lowered.                                                                                                         |                                                                                                                                                     |
| Extensibility Quota                | The value of the annotation `@AbapCatalog.extensibility.quota.maximumBytes` may not be lowered.                                                                                                          |                                                                                                                                                     |
| Data Sources                       | Released Aliases in annotation '`@AbapCatalog.extensibility.dataSources`' must not be removed completely.                                                                                                |                                                                                                                                                     |
| Data Sources                       | The datasources behind released aliases may not be changed in such a way that alias points to a different data source                                                                                    |                                                                                                                                                     |
| Data Sources                       | If a released alias points to an association, the maximal cardinality of the association definition may not be changed.                                                                                  |                                                                                                                                                     |
| Allow New Data Sources             | The annotation `@AbapCatalog.extensibility.allowNewDatasources` may not be removed. Its value may not be set to \#FALSE, if it has been previously set to \#TRUE or if its default value has been used.  |                                                                                                                                                     |
| Allow New Compositions             | The annotation `@AbapCatalog.extensibility.allowNewCompositions` may not be removed. Its value may not be set to \#FALSE, if it has been previously set to \#TRUE or if its default value has been used. |                                                                                                                                                     |
| Provider Contract                  | The provider contract of a released CDS entity may not be changed.                                                                                                                                       |                                                                                                                                                     |
| Related RAP BDEF and Draft Objects | After the release of a CDS entity, no BDEF may be added or removed.                                                                                                                                      |                                                                                                                                                     |
| Related RAP BDEF and Draft Objects | The status of draft feature enablement may not be changed after the release of the CDS entity.                                                                                                           | This check only applies to CDS projection views.                                                                                                    |
| Related RAP BDEF and Draft Objects | Draft tables or draft query views of released CDS entities may not be changed or removed.                                                                                                                | It is possible to add draft objects to a released entity, if they did not exist previously.                                                         |
| Annotations                        | as defined by meta-annotation `@CompatibilityContract.allowedChanges` in the annotation definition file of the respective annotation                                                                     | In ADT the allowed changes for annotations can displayed by clicking on the last segment of the annotation path in your CDS entity and pressing F2. |

### Contract C1

| Property     | Check                                                                                                                                             | Remark                                                                                                                                              |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Entity       | client-dependency must not be changed                                                                                                             |                                                                                                                                                     |
| Entity       | case-sensitivity of name must not be changed                                                                                                      |                                                                                                                                                     |
| Entity       | addendum root of statement define root view must not be removed                                                                                   |                                                                                                                                                     |
| Elements     | case-sensitivity of element names must not be changed                                                                                             |                                                                                                                                                     |
| Elements     | key element must not be added                                                                                                                     |                                                                                                                                                     |
| Elements     | position of key element must not be changed                                                                                                       |                                                                                                                                                     |
| Elements     | position of non-key element must not be changed in views of data category OBJECTMODEL.DATACATEGORY: \#TEXT or ANALYTICS.DATACATEGORY: \#HIERARCHY |                                                                                                                                                     |
| Elements     | position of key element must not be changed                                                                                                       |                                                                                                                                                     |
| Elements     | data type of the element must not be changed                                                                                                      |                                                                                                                                                     |
| Elements     | If a CDS enumerated type is used for the element, the CDS type must not be changed.                                                               |                                                                                                                                                     |
| Elements     | If a data element is used for the element, the conversion exit must not be changed.                                                               |                                                                                                                                                     |
| Elements     | The required reference type of the element must not be changed                                                                                    |                                                                                                                                                     |
| Parameters   | parameters must not be removed                                                                                                                    |                                                                                                                                                     |
| Parameters   | parameters must not be added                                                                                                                      |                                                                                                                                                     |
| Parameters   | case-sensitivity of parameter names must not be changed                                                                                           |                                                                                                                                                     |
| Parameters   | data type of the parameter must not be changed                                                                                                    |                                                                                                                                                     |
| Parameters   | If a CDS enumerated type is used for the parameter, the CDS type must not be changed.                                                             |                                                                                                                                                     |
| Associations | associations must not be removed                                                                                                                  |                                                                                                                                                     |
| Associations | case-sensitivity of association names must not be changed                                                                                         |                                                                                                                                                     |
| Associations | associations must not be removed from the projection list                                                                                         |                                                                                                                                                     |
| Associations | target must not be changed                                                                                                                        |                                                                                                                                                     |
| Associations | formerly released target must stay released                                                                                                       |                                                                                                                                                     |
| Associations | minimum target cardinality must not be changed from 1 to 0                                                                                        |                                                                                                                                                     |
| Associations | maximum target cardinality must not be changed from 1 to                                                                                          |                                                                                                                                                     |
| Associations | maximum target cardinality must not be changed from to 1                                                                                          |                                                                                                                                                     |
| Associations | type of association must not be changed, if current type is either COMPOSITION or TO PARENT                                                       |                                                                                                                                                     |
| Associations | source fields of ON condition must not be changed                                                                                                 |                                                                                                                                                     |
| Annotations  | as defined by meta-annotation `@CompatibilityContract.allowedChanges` in the annotation definition file of the respective annotation              | In ADT the allowed changes for annotations can displayed by clicking on the last segment of the annotation path in your CDS entity and pressing F2. |

### Contract C2

| Property     | Check                                                                                                                                             | Remark                                                                                                                                              |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Entity       | client-dependency must not be changed                                                                                                             |                                                                                                                                                     |
| Entity       | case-sensitivity of name must not be changed                                                                                                      |                                                                                                                                                     |
| Entity       | addendum root of statement define root view must not be removed                                                                                   |                                                                                                                                                     |
| Elements     | case-sensitivity of element names must not be changed                                                                                             |                                                                                                                                                     |
| Elements     | key element must not be added                                                                                                                     |                                                                                                                                                     |
| Elements     | position of key element must not be changed                                                                                                       |                                                                                                                                                     |
| Elements     | position of non-key element must not be changed in views of data category OBJECTMODEL.DATACATEGORY: \#TEXT or ANALYTICS.DATACATEGORY: \#HIERARCHY |                                                                                                                                                     |
| Elements     | position of key element must not be changed                                                                                                       |                                                                                                                                                     |
| Elements     | data type of the element must not be changed                                                                                                      |                                                                                                                                                     |
| Elements     | If a CDS enumerated type is used for the element, the CDS type must not be changed.                                                               |                                                                                                                                                     |
| Elements     | If a data element is used for the element, the conversion exit must not be changed.                                                               |                                                                                                                                                     |
| Elements     | The required reference type of the element must not be changed                                                                                    |                                                                                                                                                     |
| Parameters   | parameters must not be removed                                                                                                                    |                                                                                                                                                     |
| Parameters   | parameters must not be added                                                                                                                      |                                                                                                                                                     |
| Parameters   | case-sensitivity of parameter names must not be changed                                                                                           |                                                                                                                                                     |
| Parameters   | data type of the parameter must not be changed                                                                                                    |                                                                                                                                                     |
| Parameters   | If a CDS enumerated type is used for the parameter, the CDS type must not be changed.                                                             |                                                                                                                                                     |
| Associations | associations must not be removed                                                                                                                  |                                                                                                                                                     |
| Associations | case-sensitivity of association names must not be changed                                                                                         |                                                                                                                                                     |
| Associations | associations must not be removed from the projection list                                                                                         |                                                                                                                                                     |
| Associations | target must not be changed                                                                                                                        |                                                                                                                                                     |
| Associations | formerly released target must stay released                                                                                                       |                                                                                                                                                     |
| Associations | minimum target cardinality must not be changed from 1 to 0                                                                                        |                                                                                                                                                     |
| Associations | maximum target cardinality must not be changed from 1 to                                                                                          |                                                                                                                                                     |
| Associations | maximum target cardinality must not be changed from to 1                                                                                          |                                                                                                                                                     |
| Associations | type of association must not be changed, if current type is either COMPOSITION or TO PARENT                                                       |                                                                                                                                                     |
| Associations | source fields of ON condition must not be changed                                                                                                 |                                                                                                                                                     |
| Annotations  | as defined by meta-annotation `@CompatibilityContract.allowedChanges` in the annotation definition file of the respective annotation              | In ADT the allowed changes for annotations can displayed by clicking on the last segment of the annotation path in your CDS entity and pressing F2. |

#### CDS Scalar Function Definitions (DSFD)

### Contract C1

| Property   | Check                                                                                                                                                                                                                                                                                          | Remark |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Function   | scalar function name may not be changed                                                                                                                                                                                                                                                        |        |
| Parameters | parameters may not be removed                                                                                                                                                                                                                                                                  |        |
| Parameters | parameters names may not be changed                                                                                                                                                                                                                                                            |        |
| Parameters | The order of parameters may not be changed.                                                                                                                                                                                                                                                    |        |
| Parameters | The parameter type may not be changed incompatibly. This means type changes are not allowed with the following exceptions:                                                                                                                                                                     |        |
| Parameters | In case the parameter is typed with a concrete type (i.e. directly typed or via reference but type is non-generic), it may be changed to an identically direct type or type reference to an identically typed parameter or to a direct typing with / type reference to a broader generic type. |        |
| Parameters | In case the parameter is typed with a generic type (either directly or via reference), it may be changed to a direct typing with broader generic type.                                                                                                                                         |        |
| Parameters | If a reference handling for the parameter is defined with the addition WITH REFERENCE TYPE, this reference handling must not be changed.                                                                                                                                                       |        |
| Result     | The return type of the function may not be changed incompatibly. This means type changes are not allowed with the following exceptions:                                                                                                                                                        |        |
| Result     | If the return type is a concrete type, either directly or via reference, it may be changed to an identically direct type or type reference to an identically typed parameter.                                                                                                                  |        |
| Result     | If the return type is typed with a reference to a generic type, the referenced target parameter must not be changed.                                                                                                                                                                           |        |
| Result     | If a reference handling for the return type is defined with the addition WITH REFERENCE TYPE, this reference handling must not be changed.                                                                                                                                                     |        |

### Contract C2

| Property   | Check                                                                                                                                                                                                                                                                                          | Remark |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Function   | scalar function name may not be changed                                                                                                                                                                                                                                                        |        |
| Parameters | parameters may not be removed                                                                                                                                                                                                                                                                  |        |
| Parameters | parameters names may not be changed                                                                                                                                                                                                                                                            |        |
| Parameters | The order of parameters may not be changed.                                                                                                                                                                                                                                                    |        |
| Parameters | The parameter type may not be changed incompatibly. This means type changes are not allowed with the following exceptions:                                                                                                                                                                     |        |
| Parameters | In case the parameter is typed with a concrete type (i.e. directly typed or via reference but type is non-generic), it may be changed to an identically direct type or type reference to an identically typed parameter or to a direct typing with / type reference to a broader generic type. |        |
| Parameters | In case the parameter is typed with a generic type (either directly or via reference), it may be changed to a direct typing with broader generic type.                                                                                                                                         |        |
| Parameters | If a reference handling for the parameter is defined with the addition WITH REFERENCE TYPE, this reference handling must not be changed.                                                                                                                                                       |        |
| Result     | The return type of the function may not be changed incompatibly. This means type changes are not allowed with the following exceptions:                                                                                                                                                        |        |
| Result     | If the return type is a concrete type, either directly or via reference, it may be changed to an identically direct type or type reference to an identically typed parameter.                                                                                                                  |        |
| Result     | If the return type is typed with a reference to a generic type, the referenced target parameter must not be changed.                                                                                                                                                                           |        |
| Result     | If a reference handling for the return type is defined with the addition WITH REFERENCE TYPE, this reference handling must not be changed.                                                                                                                                                     |        |

#### CDS Scalar Function Implementation References (DSFI)

### Contract C1

| Property | Check                                                                   | Remark |
|----------|-------------------------------------------------------------------------|--------|
| Function | The name of the used CDS scalar function definition may not be changed. |        |
| Engine   | The implementing engine may not be changed.                             |        |

### Contract C2

| Property                   | Check                                                                                               | Remark                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| Function                   | The name of the used CDS scalar function definition may not be changed.                             |                                                          |
| Engine                     | The implementing engine may not be changed.                                                         |                                                          |
| Automatic Service Exposure | If the scalar function was automatically exposed in SQL services, this exposure may not be revoked. | This applies to SQL-based function implementations only. |

#### CDS Simple Types (DRTY)

### Contract C1

| Property               | Check                                | Remark                                                                                                   |
|------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------|
| Typing                 | data type must not be changed        | independent of using built-in type, data element or base simple type                                     |
| Typing                 | length must not be changed           | independent of using built-in type, data element or base simple type                                     |
| Typing                 | decimals must not be changed         | independent of using built-in type, data element or base simple type                                     |
| Output Characteristics | uppercase must not be changed        | independent of using direct annotation or inherited characteristic from data element or base simple type |
| Output Characteristics | conversion exit must not be changed  | independent of using direct annotation or inherited characteristic from data element or base simple type |
| Enumerated Constants   | constant must not be deleted         |                                                                                                          |
| Enumerated Constants   | enumerated value must not be changed |                                                                                                          |

### Contract C2

| Property               | Check                                | Remark                                                                                                   |
|------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------|
| Typing                 | data type must not be changed        | independent of using built-in type, data element or base simple type                                     |
| Typing                 | length must not be changed           | independent of using built-in type, data element or base simple type                                     |
| Typing                 | decimals must not be changed         | independent of using built-in type, data element or base simple type                                     |
| Output Characteristics | uppercase must not be changed        | independent of using direct annotation or inherited characteristic from data element or base simple type |
| Output Characteristics | conversion exit must not be changed  | independent of using direct annotation or inherited characteristic from data element or base simple type |
| Enumerated Constants   | constant must not be deleted         |                                                                                                          |
| Enumerated Constants   | enumerated value must not be changed |                                                                                                          |

#### Check Objects (CHKO)

### Contract C1

| Property           | Check                                                | Remark                                                                                                                                                             |
|--------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Check Type         | 'Remote Enabled' must be kept                        |                                                                                                                                                                    |
| Implementing Class | must not be changed                                  |                                                                                                                                                                    |
| Implementing Class | attribute 'uses_checksum' must not be changed        |                                                                                                                                                                    |
| Message Codes      | must not be added                                    |                                                                                                                                                                    |
| Parameters         | must not be deleted/renamed                          |                                                                                                                                                                    |
| Parameters         | non-hidden parameters must not be added              | If the check behaves the same as before the introduction of the parameter when the parameter has its initial value, then adding the parameter is permissible, too. |
| Parameters         | visible parameters must not be changed to hidden     |                                                                                                                                                                    |
| Parameter Type     | must not be changed                                  |                                                                                                                                                                    |
| Parameter Length   | must not be changed                                  |                                                                                                                                                                    |
| Parameter Values   | must not be removed                                  |                                                                                                                                                                    |
| Parameter Values   | parameters without values must remain without values |                                                                                                                                                                    |

#### Check Variants (CHKV)

### Contract C1

| Property | Check                                           | Remark |
|----------|-------------------------------------------------|--------|
| Variant  | status 'remote enabled' of variant must be kept |        |
| Checks   | must not be removed from the variant            |        |
| Checks   | must not be added to the variant                |        |

#### Classes (CLAS)

see section *Classes (CLAS) and Interfaces (INTF)*

#### Classes (CLAS) and Interfaces (INTF)

### Contract C1

| Property             | Check                                                     | Remark                                                                                                                                                                                                       |
|----------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attributes           | must not be deleted                                       |                                                                                                                                                                                                              |
| Attributes           | type must not be changed                                  | addition of new fields to structured attributes is allowed                                                                                                                                                   |
| Attributes           | visibility must not be reduced                            |                                                                                                                                                                                                              |
| Attributes           | level must not be changed                                 |                                                                                                                                                                                                              |
| Attributes           | must not be changed to read-only                          |                                                                                                                                                                                                              |
| Constants            | must not be deleted                                       |                                                                                                                                                                                                              |
| Constants            | visibility must not be reduced                            |                                                                                                                                                                                                              |
| Constants            | type must not be changed                                  | addition of new fields to structured constants is allowed                                                                                                                                                    |
| Methods              | must not be deleted                                       |                                                                                                                                                                                                              |
| Methods              | visibility must not be reduced                            |                                                                                                                                                                                                              |
| Methods              | level must not be changed                                 |                                                                                                                                                                                                              |
| Methods              | default behavior of interface methods must not be changed | for existing methods; for new methods it must be defined                                                                                                                                                     |
| Methods              | RAP transactional contract must not be changed            |                                                                                                                                                                                                              |
| Method Parameters    | must not be deleted                                       |                                                                                                                                                                                                              |
| Method Parameters    | type must not be changed                                  |                                                                                                                                                                                                              |
| Method Parameters    | optional indicator must not be removed                    | must be set for new importing and changing parameters; if the method had only one optional parameter, the existing parameter must be set as preferred parameter when adding further parameters to the method |
| Method Parameters    | preferred indicator must not be removed                   |                                                                                                                                                                                                              |
| Exceptions           | must not be added                                         |                                                                                                                                                                                                              |
| Events               | must not be deleted                                       |                                                                                                                                                                                                              |
| Events               | visibility must not be reduced                            |                                                                                                                                                                                                              |
| Events               | level must not be changed                                 |                                                                                                                                                                                                              |
| Event Parameters     | must not be deleted                                       |                                                                                                                                                                                                              |
| Event Parameters     | type must not be changed                                  |                                                                                                                                                                                                              |
| Types                | must not be deleted                                       |                                                                                                                                                                                                              |
| Types                | type must not be changed                                  | addition of new fields to structured types is allowed                                                                                                                                                        |
| Method AMDP Options  | `READ-ONLY` must not be removed                           |                                                                                                                                                                                                              |
| Method AMDP Options  | `CDS SESSION CLIENT` must not be changed                  |                                                                                                                                                                                                              |
| Method AMDP Options  | `CLIENT INDEPENDENT` must not be removed                  |                                                                                                                                                                                                              |
| Method AMDP Category | must not be changed                                       | e.g. change from `FUNCTION` to `PROCEDURE` is not allowed                                                                                                                                                    |
| Method AMDP Category | must not be changed                                       | AMDP to ABAP method is not allowed                                                                                                                                                                           |
| Method AMDP Language | must not be changed                                       |                                                                                                                                                                                                              |
| Method Parameters    | parameter order must not be changed                       |                                                                                                                                                                                                              |

### Contract C4

| Property | Check                              | Remark |
|----------|------------------------------------|--------|
| Any      | changes are not allowed in general |        |

#### Data Definitions (DDLS)

see section *CDS Entities (DDLS/CDS_STOB)*

#### Data Elements (DTEL)

### Contract C1

| Property           | Check               | Remark |
|--------------------|---------------------|--------|
| Data Type          | must not be changed |        |
| Length             | must not be changed |        |
| Decimals           | must not be changed |        |
| Output Length      | must not be changed |        |
| Conversion Routine | must not be changed |        |
| Case-Sensitivity   | must not be changed |        |

#### Dictionary Tuning Object Dynamic Cache (DTDC)

For dynamic cache objects only the configuration relevant part is released via C1 contracts. The configuration statement included in the source allows the change of configuration via the corresponding configuration transaction or app.

### Contract C1

| Property                          | Check                                                                                                                            | Remark                                                         |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Configuration statement in source | Statement CREATION CONFIGURABLE DEFAULT `<state>` in source must not be deleted!                                                 |                                                                |
| Configuration statement in source | Introduction/adding of CREATION CONFIGURABLE DEFAULT `<state>` in source is allowed                                              | The value of `<state>` must be set to 'ON' or 'OFF'            |
| Configuration statement in source | Change of default configuration CREATION CONFIGURABLE DEFAULT `<state>` 'ON' -\> 'OFF' in source is allowed, otherwise forbidden | The value of `<state>` can be changed from 'ON' to 'OFF' only! |

#### Dictionary Tuning Object Static Cache (DTSC)

For static cache objects only the configuration relevant part is released via C1 contracts. The configuration statement included in the source allows the change of configuration via the corresponding configuration transaction or app (please refer to the documentation).

### Contract C1

| Property                          | Check                                                                                                                            | Remark                                                         |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Configuration statement in source | Statement CREATION CONFIGURABLE DEFAULT `<state>` in source must not be deleted!                                                 |                                                                |
| Configuration statement in source | Introduction/adding of CREATION CONFIGURABLE DEFAULT `<state>` in source is allowed                                              | The value of `<state>` must be set to 'ON' or 'OFF'            |
| Configuration statement in source | Change of default configuration CREATION CONFIGURABLE DEFAULT `<state>` 'ON' -\> 'OFF' in source is allowed, otherwise forbidden | The value of `<state>` can be changed from 'ON' to 'OFF' only! |

#### Domains (DOMA)

### Contract C1

| Property                          | Check               | Remark                  |
|-----------------------------------|---------------------|-------------------------|
| Data Type                         | must not be changed |                         |
| Length                            | must not be changed |                         |
| Decimals                          | must not be changed |                         |
| Output Length                     | must not be changed |                         |
| Output Style                      | must not be changed |                         |
| Conversion Routine                | must not be changed |                         |
| Sign                              | must not be changed |                         |
| Case-Sensitivity                  | must not be changed |                         |
| Time Format                       | must not be changed |                         |
| Fixed Values                      | must not be removed | new values can be added |
| Fixed Value Intervals Upper Limit | must not be changed |                         |
| Value Table                       | must not be changed |                         |

#### Email Templates (SMTG)

### Contract C1

| Property            | Check                 | Remark |
|---------------------|-----------------------|--------|
| Referenced CDS View | must not be exchanged |        |

#### Enhancement Spots (ENHS)

see section *BAdI Definitions (ENHS/BADI_DEF)*

#### Event Bindings (EVTB)

### Contract C2

| Property                                   | Check                                                             | Remark                                          |
|--------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------|
| Event Binding: name                        | must not be changed                                               | Rename is not allowed                           |
| Producer                                   | must not be added, must not be changed, must not be removed       |                                                 |
| Producer: Producer Version                 | must not be added, must not be changed, must not be removed       |                                                 |
| Producer: Producer Legacy                  | must not be added, must not be changed, must not be removed       |                                                 |
| Producer: BO Name                          | must not be added, must not be changed, must not be removed       |                                                 |
| Producer: BO Operation                     | must not be added, must not be changed, must not be removed       |                                                 |
| Producer: Producer Namespace               | must not be added, must not be changed, must not be removed       |                                                 |
| Entity Event Name                          | change allowed, as long as the new structure behind is compatible |                                                 |
| Event Parameter Name                       | change allowed, as long as the new structure behind is compatible |                                                 |
| Payload Parameter                          | must not be removed                                               |                                                 |
| Payload Parameter: Name                    | must not be changed, must not be removed                          |                                                 |
| Payload Parameter: Is Key                  | must not be added, must not be changed, must not be removed       |                                                 |
| Payload Parameter: Conversion Exit         | must not be changed                                               |                                                 |
| Payload Parameter: EDM Type                | must not be changed                                               |                                                 |
| Payload Parameter: EDM Name                | must not be changed                                               |                                                 |
| Payload Parameter: Nullable                | must not be changed                                               |                                                 |
| Payload Parameter: ABAP Type               | must not be changed                                               |                                                 |
| Payload Parameter: Internal Type           | must not be changed                                               |                                                 |
| Payload Parameter: Internal Length         | must not be changed                                               |                                                 |
| Payload Parameter: Length Org              | must not be changed                                               |                                                 |
| Payload Parameter: Display Format          | must not be changed                                               |                                                 |
| Payload Parameter: Length                  | must not be changed                                               | Length must not decrease or increase            |
| Payload Parameter: Decimals                | must not be changed                                               | Number of decimal must not decrease or increase |
| Payload Parameter: Upper Case              | must not be changed                                               |                                                 |
| Payload Parameter: Scale                   | must not be changed                                               |                                                 |
| Payload Parameter: Precision               | must not be changed                                               |                                                 |
| Payload Parameter: Unit                    | must not be changed                                               |                                                 |
| `@Semantics.quantity.unitOfMeasure`        | must not be added, must not be changed, must not be removed       | Anno value must not be changed                  |
| `@Semantics.quantity.unitOfMeasureSapCode` | must not be changed, must not be removed                          | Anno value must not be changed                  |
| `@Semantics.quantity.unitOfMeasureIsoCode` | must not be changed, must not be removed                          | Anno value must not be changed                  |
| `@Semantics.unitOfMeasure`                 | must not be added, must not be changed, must not be removed       | Anno value must not be changed                  |
| `@Semantics.amount.currencyCode`           | must not be added, must not be changed, must not be removed       | Anno value must not be changed                  |
| `@Semantics.currencyCode`                  | must not be added, must not be changed, must not be removed       | Anno value must not be changed                  |
| `@Semantics.datetime`                      | must not be added, must not be changed, must not be removed       | Anno value must not be changed                  |
| `@Semantics.uuid`                          | must not be added, must not be changed, must not be removed       | Anno value must not be changed                  |
| `@Semantics.booleanIndicator`              | must not be added, must not be changed, must not be removed       | Anno value must not be changed                  |
| `@Semantics.timeZone`                      | must not be changed, must not be removed                          | Anno value must not be changed                  |
| `@Event.element.externalName`              | must not be added, must not be changed, must not be removed       |                                                 |

#### Event Objects (EVTO)

### Contract C2

| Property      | Check                                                              | Remark |
|---------------|--------------------------------------------------------------------|--------|
| Major Version | must only be changed if event is deprecated or if event is removed |        |
| Minor Version | must only be changed if new event is added to EVTO                 |        |
| Patch Version | must only be changed if there are changes to events of EVTO        |        |

#### Function Groups (FUGR)

see section *Function Modules (FUGR/FUNC)*

#### Function Modules (FUGR/FUNC)

### Contract C1

| Property               | Check                                                                     | Remark                                       |
|------------------------|---------------------------------------------------------------------------|----------------------------------------------|
| Function Module        | must not be deleted                                                       |                                              |
| Processing Type        | remote-enabled (RFC) function modules must not be changed to regular ones |                                              |
| Processing Type        | update function modules must not be changed to regular ones               |                                              |
| Start Mode             | must not be changed                                                       | this applies to update function modules only |
| RFC Scope              | must not be changed                                                       | this applies to RFC function modules only    |
| RFC Interface Contract | must not be changed                                                       | this applies to RFC function modules only    |
| BasXML Support         | must not be changed                                                       | this applies to RFC function modules only    |
| Parameters             | must not be deleted                                                       |                                              |
| Parameters             | new parameters must be marked as optional                                 |                                              |
| Parameters             | optional parameters must not become mandatory                             |                                              |
| Parameters             | type must not be changed                                                  |                                              |
| Exceptions             | must not be added                                                         |                                              |
| Exceptions             | non-class-based exceptions must not be deleted                            |                                              |

#### Inbound Services (SCO2)

### Contract C1

| Property        | Check                                        | Remark |
|-----------------|----------------------------------------------|--------|
| Inbound Service | must not be removed                          |        |
| Inbound Service | must not be changed                          |        |
| Inbound Service | ICF path must not be changed                 |        |
| Inbound Service | IDOC message type must not be changed        |        |
| Inbound Service | IDOC type must not be changed                |        |
| Inbound Service | RFC service ID must not be changed           |        |
| Inbound Service | SOAP interface name must not be changed      |        |
| Inbound Service | SOAP operation name must not be changed      |        |
| Inbound Service | OData service identifier must not be changed |        |
| Inbound Service | OData V4 group ID must not be changed        |        |
| Inbound Service | HTTP service ID must not be changed          |        |
| Inbound Service | SADT group name ID must not be changed       |        |
| Inbound Service | SQL1 name must not be changed                |        |

#### Interfaces (INTF)

see section *Classes (CLAS) and Interfaces (INTF)*

#### OData V2 Services (IWSV)

### Contract C1

| Property                                                         | Check                                                                         | Remark                                                           |
|------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Entity Set                                                       | must not be removed                                                           |                                                                  |
| Entity Set: Name                                                 | must not be changed                                                           | Rename is not allowed                                            |
| Entity Set: Creatable                                            | must not be removed, must not be changed                                      |                                                                  |
| Entity Set: Updatable                                            | must not be removed, must not be changed                                      |                                                                  |
| Entity Set: Deletable                                            | must not be removed, must not be changed                                      |                                                                  |
| Entity Type                                                      | must not be removed                                                           |                                                                  |
| Entity Type: Name                                                | must not be changed                                                           | Rename is not allowed                                            |
| Entity Type: Is Draft Enabled                                    | must not be changed                                                           |                                                                  |
| Property                                                         | must not be removed                                                           |                                                                  |
| Property: Name                                                   | must not be changed                                                           | Rename is not allowed                                            |
| Property: Is Key                                                 | must not be removed, must not be changed, must not be added                   |                                                                  |
| Property: Edm Type                                               | must not be changed                                                           |                                                                  |
| Property: Filterable                                             | must not be removed                                                           | Creation of (filter, search or sort) restrictions is not allowed |
| Property: Searchable                                             | must not be removed                                                           | Creation of (filter, search or sort) restrictions is not allowed |
| Property: Sortable                                               | must not be removed                                                           | Creation of (filter, search or sort) restrictions is not allowed |
| Navigation Property                                              | must not be removed                                                           |                                                                  |
| Navigation Property: Name                                        | must not be removed                                                           | Rename is not allowed                                            |
| Navigation Property: Contains Target                             | must not be changed                                                           |                                                                  |
| Navigation Property: Target Type                                 | must not be changed                                                           |                                                                  |
| Navigation Property: Source Type                                 | must not be changed                                                           |                                                                  |
| Navigation Property: Target Multiplicity                         | must not be changed                                                           | This holds even true for changes from to 1                       |
| Navigation Property: Source Multiplicity                         | must not be changed                                                           | This holds even true for changes from to 1                       |
| Navigation Property: Referential constraints: dependent property | must not be changed or removed                                                |                                                                  |
| Navigation Property: Referential constraints: principal property | must not be changed or removed                                                |                                                                  |
| Operation                                                        | must not be removed                                                           |                                                                  |
| Operation: Name                                                  | must not be changed                                                           | Rename is not allowed                                            |
| Operation Parameter Properties                                   | the same restrictions apply as for entity types respectively their properties |                                                                  |
| Operation Result Type Properties                                 | the same restrictions apply as for entity types respectively their properties |                                                                  |

### Contract C2

| Property                                               | Check                                                       | Remark                                                                 |
|--------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------|
| Semantic Version of Service                            | must be changed                                             | If service is changed, the semantic version of service must be changed |
| Service Version                                        | must not be removed                                         |                                                                        |
| Service Definition: Alias of Exposed Entity            | must not be added, changed or deleted                       |                                                                        |
| Entity Set                                             | must not be changed or removed                              |                                                                        |
| Entity Set: Creatable                                  | must not be changed                                         | A change from true to false is not allowed                             |
| Entity Set: Updatable                                  | must not be changed                                         | A change from true to false is not allowed                             |
| Entity Set: Deletable                                  | must not be changed                                         | A change from true to false is not allowed                             |
| Entity Set: Addressable                                | must not be changed                                         |                                                                        |
| Entity Set: Filter Required                            | must not be changed                                         |                                                                        |
| Entity Set: Searchable                                 | must not be changed                                         | A change from true to false is not allowed                             |
| Entity Type                                            | must not be removed                                         |                                                                        |
| Entity Type: Name                                      | must not be changed                                         | Rename is not allowed                                                  |
| Entity Type: Is Stream                                 | must not be changed                                         | A change from true to false is not allowed                             |
| Property                                               | must not be removed                                         |                                                                        |
| Property: EDM Type                                     | must not be changed                                         |                                                                        |
| Property: ABAP Type                                    | must not be changed                                         |                                                                        |
| Property: ABAP Name                                    | must not be changed                                         |                                                                        |
| Property: Length                                       | must not be changed                                         | Increase or decrease of length is not allowed                          |
| Property: Nullable                                     | must not be changed                                         | A change from true to false is not allowed                             |
| Property: Default Value                                | must not be changed                                         |                                                                        |
| Property: Is Key                                       | must not be added, changed or removed                       |                                                                        |
| Property: Is Etag                                      | must not be removed                                         |                                                                        |
| Property: Mandatory                                    | must not be changed                                         | A change from false to true is not allowed                             |
| Property: Mandatory Update                             | must not be changed                                         | A change from false to true is not allowed                             |
| Property: Read-Only                                    | must not be changed                                         |                                                                        |
| Property: Read-Only Create                             | must not be changed                                         |                                                                        |
| Property: Read-Only Update                             | must not be changed                                         |                                                                        |
| Property: Has Required Property                        | must not be changed                                         | Removing a required property is not allowed                            |
| Property: Conversion Exit                              | must not be changed                                         | Adding alpha conversion to N is checked.                               |
| Property: Display Format                               | must not be changed                                         |                                                                        |
| Property: Creatable                                    | must not be changed                                         |                                                                        |
| Property: Updatable                                    | must not be changed                                         |                                                                        |
| Property: Sortable                                     | must not be changed                                         |                                                                        |
| Property: Filterable                                   | must not be changed                                         |                                                                        |
| Navigation Property                                    | must not be removed                                         |                                                                        |
| Navigation Property: Target Multiplicity               | must not be changed                                         |                                                                        |
| Navigation Property: Source Multiplicity               | must not be changed                                         |                                                                        |
| Navigation Property: Source Type                       | must not be changed                                         |                                                                        |
| Navigation Property: Target Type                       | must not be changed                                         |                                                                        |
| Navigation Property: Ref Constraint-Principal role     | must not be changed                                         |                                                                        |
| Navigation Property: Ref Constraint-Principal Property | must not be changed                                         |                                                                        |
| Navigation Property: Ref Constraint-Dependent Role     | must not be changed                                         |                                                                        |
| Navigation Property: Ref Constraint-Dependent Property | must not be changed                                         |                                                                        |
| Navigation Property: From_on_delete_action             | must not be changed                                         |                                                                        |
| Navigation Property: To_on_delete_action               | must not be changed                                         |                                                                        |
| Navigation Property: Nullable                          | must not be changed                                         |                                                                        |
| Complex Type                                           | must not be changed, must not be removed                    | Rename is not allowed                                                  |
| Complex Type: Properties                               |                                                             | Properties checks as for entity type properties ( see above )          |
| Operation                                              | must not be changed, must not be removed                    | Rename is not allowed                                                  |
| Operation: Function/Action Import                      | must not be changed, must not be removed                    |                                                                        |
| Operation: Operation Type                              | must not be changed                                         |                                                                        |
| Operation: Corresponding Entity Set                    | must not be changed                                         |                                                                        |
| Operation: Return Type                                 | must not be added, must not be removed                      |                                                                        |
| Operation: Type of Return Type                         | must not be changed                                         |                                                                        |
| Operation: Is Collection                               | must not be changed                                         |                                                                        |
| `@Semantics.amount.currencyCode`                       | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.businessDate.from`                         | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.businessDate.to`                           | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.currencyCode`                              | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.language`                                  | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.text`                                      | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.unitOfMeasure`                             | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.quantity.unitOfMeasure`                    | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.businessDate.temporalKey`                  | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.mimeType`                                  | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.url.mimeType`                              | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.largeObject.filename`                      | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.largeObject.acceptableMimeTypes`           | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.timezone`                                  | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.timezonereference`                         | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.largeObject.filename`                      | must not be changed, must not be removed                    |                                                                        |
| Annotation: `@Feature`                                 | must not be added, must not be changed                      | Anno value must not be changed                                         |
| `@Data.action`.                                        | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.entitySet.name`                                 | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.entityType.name`                                | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.etag`                                           | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.v2.autoAggregation`                             | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.property.name`                                  | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@ObjectModel.association.reverseAssociation`          | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.compositionRoot`                         | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.createEnabled`                           | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.dataCategory`                            | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.deleteEnabled`                           | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.enttyChangeStateId`                      | must not be changed, must not be removed                    |                                                                        |
| `@ObjectModel.filter.enabled`                          | must not be changed, must not be removed                    |                                                                        |
| `@ObjectModel.filter.transformedBy`                    | must not be added, must not be changed                      |                                                                        |
| `@ObjectModel.foreignKey.association`                  | must not be changed, must not be removed                    |                                                                        |
| `@ObjectModel.representativeKey`                       | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.sort.enabled`                            | must not be changed, must not be removed                    |                                                                        |
| `@ObjectModel.sort.transformedBy`                      | must not be added, must not be changed                      |                                                                        |
| `@ObjectModel.text.association`                        | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.text.element`                            | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.text.reference.association`              | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.transactionalProcessingDelegated`        | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.updateEnabled`                           | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.virtualElement`                          | must not be added, must not be changed                      |                                                                        |
| `@ObjectModel.virtualElementCalculatedBy`              | must not be added, must not be changed                      |                                                                        |

#### OData V4 Services (G4BA)

### Contract C1

| Property                                                         | Check                                                                         | Remark                                                           |
|------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Entity Set                                                       | must not be removed                                                           |                                                                  |
| Entity Set: Name                                                 | must not be changed                                                           | Rename is not allowed                                            |
| Entity Set: Creatable                                            | must not be removed, must not be changed                                      |                                                                  |
| Entity Set: Updatable                                            | must not be removed, must not be changed                                      |                                                                  |
| Entity Set: Deletable                                            | must not be removed, must not be changed                                      |                                                                  |
| Entity Type                                                      | must not be removed                                                           |                                                                  |
| Entity Type: Name                                                | must not be changed                                                           | Rename is not allowed                                            |
| Entity Type: Is Draft Enabled                                    | must not be changed                                                           |                                                                  |
| Property                                                         | must not be removed                                                           |                                                                  |
| Property: Name                                                   | must not be changed                                                           | Rename is not allowed                                            |
| Property: Is Key                                                 | must not be removed, must not be changed, must not be added                   |                                                                  |
| Property: Edm Type                                               | must not be changed                                                           |                                                                  |
| Property: Filterable                                             | must not be removed                                                           | Creation of (filter, search or sort) restrictions is not allowed |
| Property: Searchable                                             | must not be removed                                                           | Creation of (filter, search or sort) restrictions is not allowed |
| Property: Sortable                                               | must not be removed                                                           | Creation of (filter, search or sort) restrictions is not allowed |
| Navigation Property                                              | must not be removed                                                           |                                                                  |
| Navigation Property: Name                                        | must not be removed                                                           | Rename is not allowed                                            |
| Navigation Property: Contains Target                             | must not be changed                                                           |                                                                  |
| Navigation Property: Target Type                                 | must not be changed                                                           |                                                                  |
| Navigation Property: Source Type                                 | must not be changed                                                           |                                                                  |
| Navigation Property: Target Multiplicity                         | must not be changed                                                           | This holds even true for changes from to 1                       |
| Navigation Property: Source Multiplicity                         | must not be changed                                                           | This holds even true for changes from to 1                       |
| Navigation Property: Referential Constraints: Dependent Property | must not be changed or removed                                                |                                                                  |
| Navigation Property: Referential Constraints: Principal Property | must not be changed or removed                                                |                                                                  |
| Operation                                                        | must not be removed                                                           |                                                                  |
| Operation: Name                                                  | must not be changed                                                           | Rename is not allowed                                            |
| Operation Parameter Properties                                   | the same restrictions apply as for entity types respectively their properties |                                                                  |
| Operation Result Type Properties                                 | the same restrictions apply as for entity types respectively their properties |                                                                  |

### Contract C2

| Property                                        | Check                                                       | Remark                                                                 |
|-------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------|
| Semantic Version of Service                     | must be changed                                             | If service is changed, the semantic version of service must be changed |
| Service Version                                 | must not be removed                                         |                                                                        |
| Service Name Alias                              | must not be changed                                         |                                                                        |
| Service Definition: alias of exposed entity     | must not be added, changed or deleted                       |                                                                        |
| Entity Set                                      | must not be changed or removed                              |                                                                        |
| Entity Set: Creatable                           | must not be changed                                         | A change from true to false is not allowed                             |
| Entity Set: Updatable                           | must not be changed                                         | A change from true to false is not allowed                             |
| Entity Set: Deletable                           | must not be changed                                         | A change from true to false is not allowed                             |
| Entity Set: Addressable                         | must not be changed                                         |                                                                        |
| Entity Set: Filter Required                     | must not be changed                                         |                                                                        |
| Entity Type                                     | must not be removed                                         |                                                                        |
| Entity Type: Name                               | must not be changed                                         | Rename is not allowed                                                  |
| Property                                        | must not be removed                                         |                                                                        |
| Property: Aggregation                           | must not be changed                                         |                                                                        |
| Property: Conversion Exit                       | must not be changed                                         | Adding alpha conversion to N is checked.                               |
| Property: Default Value                         | must not be changed                                         |                                                                        |
| Property: EDM Type                              | must not be changed                                         |                                                                        |
| Property: Precision                             | must not be changed                                         |                                                                        |
| Property: Length                                | must not be changed                                         | Increase or decrease of length is not allowed                          |
| Property: Filterable                            | must not be changed                                         |                                                                        |
| Property: Scale                                 | must not be changed                                         |                                                                        |
| Property: Semantic                              | must not be changed                                         |                                                                        |
| Property: Sortable                              | must not be changed                                         |                                                                        |
| Property: Upper Case                            | must not be changed                                         |                                                                        |
| Property: Display Format                        | must not be changed                                         |                                                                        |
| Property: Number of Decimal Places              | must not be changed                                         | Increase or decrease of numbers of decimal is not allowed              |
| Property: Creatable                             | must not be changed                                         |                                                                        |
| Property: Mandatory                             | must not be changed                                         | A change from false to true is not allowed                             |
| Property: Mandatory Update                      | must not be changed                                         | A change from false to true is not allowed                             |
| Property: Read-Only                             | must not be changed                                         |                                                                        |
| Property: Read-Only Create                      | must not be changed                                         |                                                                        |
| Property: Read-Only Update                      | must not be changed                                         |                                                                        |
| Property: Has Required Property                 | must not be changed                                         | Removing a required property is not allowed                            |
| Property: Nullable                              | must not be changed                                         | A change from true to false is not allowed                             |
| Property: Is Key                                | must not be added, changed or removed                       |                                                                        |
| Property: Is Etag                               | must not be removed                                         |                                                                        |
| Property: Updatable                             | must not be changed                                         |                                                                        |
| Navigation Property                             | must not be removed                                         |                                                                        |
| Navigation Property: Partner                    | must not be changed                                         |                                                                        |
| Navigation Property: Contains Target            | must not be changed                                         |                                                                        |
| Complex Type                                    | must not be changed, must not be removed                    | Rename is not allowed                                                  |
| Complex Type: Properties                        |                                                             | Properties checks as for entity type properties ( see above )          |
| Operation                                       | must not be changed, must not be removed                    | Rename is not allowed                                                  |
| Operation: Operation Type                       | must not be changed                                         |                                                                        |
| Operation: Corresponding Entity Set             | must not be changed                                         |                                                                        |
| Operation: Return Type                          | must not be changed                                         |                                                                        |
| Operation: Return Type Name                     | must not be changed                                         |                                                                        |
| Operation: Is Collection                        | must not be changed                                         |                                                                        |
| `@Semantics.amount.currencyCode`                | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.businessDate.from`                  | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.businessDate.to`                    | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.currencyCode`                       | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.language`                           | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.text`                               | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.unitOfMeasure`                      | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.quantity.unitOfMeasure`             | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.businessDate.temporalKey`           | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Semantics.mimeType`                           | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.url.mimeType`                       | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.largeObject.filename`               | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.largeObject.acceptableMimeTypes`    | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.timezone`                           | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.timezonereference`                  | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@Semantics.largeObject.filename`               | must not be changed, must not be removed                    |                                                                        |
| Annotation: `@Feature`                          | must not be added, must not be changed                      | Anno value must not be changed                                         |
| Annotation: `@Data`.                            |                                                             |                                                                        |
| `@Data.action`.                                 | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.entitySet.name`                          | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.entityType.name`                         | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.etag`                                    | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.v2.autoAggregation`                      | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@Data.property.name`                           | must not be added, must not be changed, must not be removed | Anno value must not be changed                                         |
| `@ObjectModel.association.reverseAssociation`   | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.compositionRoot`                  | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.createEnabled`                    | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.dataCategory`                     | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.deleteEnabled`                    | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.enttyChangeStateId`               | must not be changed, must not be removed                    |                                                                        |
| `@ObjectModel.filter.enabled`                   | must not be changed, must not be removed                    |                                                                        |
| `@ObjectModel.filter.transformedBy`             | must not be added, must not be changed                      |                                                                        |
| `@ObjectModel.foreignKey.association`           | must not be changed, must not be removed                    |                                                                        |
| `@ObjectModel.representativeKey`                | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.sort.enabled`                     | must not be changed, must not be removed                    |                                                                        |
| `@ObjectModel.sort.transformedBy`               | must not be added, must not be changed                      |                                                                        |
| `@ObjectModel.text.association`                 | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.text.element`                     | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.text.reference.association`       | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.transactionalProcessingDelegated` | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.updateEnabled`                    | must not be changed, must not be removed                    | Anno value must not be changed                                         |
| `@ObjectModel.virtualElement`                   | must not be added, must not be changed                      |                                                                        |
| `@ObjectModel.virtualElementCalculatedBy`       | must not be added, must not be changed                      |                                                                        |

#### Predefined Custom Fields (PCFN)

### Contract C1

| Property                        | Check                                                    | Remark |
|---------------------------------|----------------------------------------------------------|--------|
| Node Primary Database Table     | must not be changed                                      |        |
| Node Persistence Content Object | must not be changed                                      |        |
| Node Fieldname Prefix           | must not be changed                                      |        |
| Node Fields                     | must not be deleted                                      |        |
| Node Field Types                | is only allowed to change from character to short string |        |
| Node Field Lengths              | must only be changed for types with varying length       |        |
| Node Field Lengths              | must not be shortened                                    |        |

#### Restriction Types (SIA2)

### Contract C1

| Property             | Check                                    | Remark |
|----------------------|------------------------------------------|--------|
| Restriction Type     | must not be removed                      |        |
| Restriction Type     | aggregation category must not be changed |        |
| Authorization Object | must not be deleted                      |        |
| Restriction Field    | must not be deleted                      |        |
| Restriction Field    | PFCG name must not be changed            |        |

#### Review Booklets (RVBC)

### Contract C1

| Entity - Property                | Check                                                                                       | Remark                                                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| DataProvider                     | Data Providers must not be deleted                                                          |                                                                                                                              |
| DataProvider - CDS View          | Must not be changed                                                                         |                                                                                                                              |
| DataProvider - Default Flag      | Must not be changed                                                                         | Changing this flag would destroy all variants created by customers.                                                          |
| Page                             | Visible pages must not be deleted                                                           |                                                                                                                              |
| Page - Visibility                | Must not be changed from "visible" to "invisible"                                           |                                                                                                                              |
| Page - UI Pattern                | Must not be changed                                                                         |                                                                                                                              |
| PageContent - DataProvider       | Must not be changed                                                                         |                                                                                                                              |
| Variable - Visibility            | Variables which are "visible" or "visible in adapt filters" must not be changed to "hidden" |                                                                                                                              |
| Variable - Move to booklet level | Variables must not be moved from page level to booklet level                                | Customer variants may have different default values on different pages. Moving to booklet level would destroy these variants |

#### SAP Object Node Types (NONT)

### Contract C1

| Property    | Check                                                       | Remark |
|-------------|-------------------------------------------------------------|--------|
| Name        | must not be added, must not be changed, must not be removed |        |
| Root Flag   | must not be added, must not be changed, must not be removed |        |
| Parent Name | must not be added, must not be changed, must not be removed |        |

#### SAP Object Types (RONT)

### Contract C1

| Property         | Check                                                       | Remark |
|------------------|-------------------------------------------------------------|--------|
| Name             | must not be added, must not be changed, must not be removed |        |
| Object Type Code | must not be added, must not be changed, must not be removed |        |
| ODM Entity Name  | must not be added, must not be changed, must not be removed |        |
| Entity Interface | must not be added, must not be changed, must not be removed |        |

#### Service Definitions (SRVD)

### Contract C0

| Property                  | Check                                                                                                                                                                                      | Remark |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Extensibility Annotation  | no change or removal of the annotation '`@AbapCatalog.extensibility.extensible`' or '`@AbapCatalog.extensibility.extensible`: true'                                                        |        |
| Provider Contract         | the provider contract must remain stable; no addition of new contracts and no changes to existing contracts are allowed                                                                    |        |
| Exposed Entity with Alias | if new entities are added, these new entities must obey the naming rules; for repository objects developed in an SAP system, this means that the entity names must not start with YY or ZZ |        |

#### Software Component Relations (SWCR)

### Contract C1

| Property           | Check               | Remark                                                                                                                                                                                                                              |
|--------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access Permissions | must not be removed | software component relations cannot be released explicitly, but due to the impact of *access permissions* on the ABAP syntax check of objects in other software components, they are being checked for incompatibilities implicitly |

#### SQL Services (SQL1)

### Contract C2

| Property                     | Check                                                             | Remark                                                                                                                      |
|------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Service Binding              | name must not change, including case                              |                                                                                                                             |
| Service Binding              | enabled operations most not be removed                            | addition of new operations is allowed                                                                                       |
| Service Definition           | exposed entity names must not change, including case              |                                                                                                                             |
| Service Definition           | exposed entity name must not be removed                           | addition of new entites is allowed                                                                                          |
| Exposed Entity               | client-dependency must not be changed                             |                                                                                                                             |
| Exposed Entity               | replication capablity of entity must not be removed               | Only if service is enabled for `REPLICATE`                                                                                  |
| Exposed Entity               | delta replication capablity must not be removed                   | Only if service is enabled for `REPLICATE`                                                                                  |
| Elements of Exposed Entity   | element position must not be changed                              |                                                                                                                             |
| Elements of Exposed Entity   | key elements must not be added                                    | addition of non-key elements at the end allowed                                                                             |
| Elements of Exposed Entity   | name must not change, including case                              |                                                                                                                             |
| Elements of Exposed Entity   | elements must not be removed                                      | replacing of elements with compatible type and same exposed name allowed                                                    |
| Elements of Exposed Entity   | reference elements for amounts and quantities must not be changed | reference elements are assigned with CDS annotation `@Semantics.amount.currencyCode` or `@Semantics.quantity.unitOfMeasure` |
| Elements of Exposed Entity   | underlying ABAP dictionary type must not be changed               |                                                                                                                             |
| Parameters of Exposed Entity | must not be removed or added                                      |                                                                                                                             |
| Parameters of Exposed Entity | name must not change, including case                              |                                                                                                                             |
| Parameters of Exposed Entity | parameter position must not be changed                            |                                                                                                                             |
| Parameters of Exposed Entity | underlying ABAP dictionary type must not be changed               |                                                                                                                             |

#### Structures and Database Tables (TABL)

### Contract C0

C0-release for tables and structures with visibility *Use in Key User Apps* is available SAP-internally only. The corresponding checks are performed in transaction SCFD_REGISTRY and as ATC checks like described in the *Custom Fields Adoption Guideline*.

For tables and structures with visibility *Use in Cloud Development*, see below.

| Property             | Check                                                                                                          | Remark                                                                                                                                             |
|----------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Object Type          | The type of the released object must not be changed (e.g. from DDIC structure to table)                        |                                                                                                                                                    |
| Enhancement Category | The value of the annotation `@AbapCatalog.enhancement.category` may not be changed to a more restrictive value |                                                                                                                                                    |
| Field Suffix         | The annotation `@AbapCatalog.enhancement.fieldSuffix` and its value must not be changed                        |                                                                                                                                                    |
| Extensibility Quota  | The assigned extensibility quota must not be reduced. This means:                                              |                                                                                                                                                    |
| Extensibility Quota  | The value of the annotation `@AbapCatalog.enhancement.quotaMaximumFields` must not be lowered                  |                                                                                                                                                    |
| Extensibility Quota  | The value of the annotation `@AbapCatalog.enhancement.quotaMaximumBytes` must not be lowered                   |                                                                                                                                                    |
| Table Storage Type   | A released DDIC table must not be changed from column store table to row store table and vice versa            |                                                                                                                                                    |
| Usage                | If a released TABL object is used in another object (e.g. as an include), this usage must not be removed       | As extensions are added not only to the released object, but also to objects that use the extended structure, removing such usage is incompatible. |

### Contract C1

| Property           | Check                                                                  | Remark                                                                                                                             |
|--------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Components         | must not be removed                                                    | i.e. components with typing method *Type* and typed with a simple data type, including key fields                                  |
| Components         | new key fields must not be added                                       | relevant for database tables only; new non-key components can be added                                                             |
| Components         | position of key fields must not be changed                             | relevant for database tables only                                                                                                  |
| Components         | typing method must not be changed                                      |                                                                                                                                    |
| Components         | data type must not be changed                                          |                                                                                                                                    |
| Components         | length must not be changed                                             |                                                                                                                                    |
| Components         | decimals must not be changed                                           |                                                                                                                                    |
| Components         | output length must not be changed                                      |                                                                                                                                    |
| Components         | conversion routine must not be changed                                 |                                                                                                                                    |
| Components         | case-sensitivity must not be changed                                   |                                                                                                                                    |
| Complex Components | must not be removed                                                    | i.e. components with typing method *Type* and typed with a structure or table type, or components with typing method *Type Ref To* |
| Complex Components | referenced object must not be exchanged                                |                                                                                                                                    |
| Complex Components | typing method must not be changed                                      |                                                                                                                                    |
| Group Names        | components must be addressable via the same group name paths as before |                                                                                                                                    |

### Contract C3

| Property                        | Check                                                              | Remark                          |
|---------------------------------|--------------------------------------------------------------------|---------------------------------|
| Components                      | must not be removed                                                |                                 |
| Components                      | new key fields must not be added                                   | new non-key fields can be added |
| Components                      | position of key fields must not be changed                         |                                 |
| Components                      | data type must not be changed                                      |                                 |
| Components                      | length must not be changed                                         |                                 |
| Components                      | decimals must not be changed                                       |                                 |
| Components                      | output length must not be changed                                  |                                 |
| Components                      | conversion routine must not be changed                             |                                 |
| Components                      | case-sensitivity must not be changed                               |                                 |
| Group Names                     | fields must be addressable via the same group name paths as before |                                 |
| Customer Namespace Reservations | must not be changed                                                |                                 |

#### Table Types (TTYP)

### Contract C1

| Property          | Check                                   | Remark                             |
|-------------------|-----------------------------------------|------------------------------------|
| Row Type Category | must not be changed                     |                                    |
| Row Type          | referenced object must not be exchanged |                                    |
| Row Type          | length must not be changed              | relevant for predefined types only |
| Row Type          | decimals must not be changed            | relevant for predefined types only |
| Access Type       | must not be changed                     |                                    |
| Primary Key       | must not be changed                     |                                    |
| Secondary Keys    | must not be removed                     | new secondary keys can be added    |
| Secondary Keys    | must not be changed                     |                                    |

#### Views (VIEW)

### Contract C3

| Property           | Check                                                                  | Remark                          |
|--------------------|------------------------------------------------------------------------|---------------------------------|
| View Class         | must not be changed                                                    |                                 |
| Delivery Class     | must not be changed                                                    |                                 |
| View Maintenance   | must not be changed                                                    |                                 |
| Customizing Object | the view's customizing object must not be removed                      |                                 |
| Customizing Object | the adjustability of the view's customizing object must not be changed |                                 |
| Fields             | must not be removed                                                    |                                 |
| Fields             | new key fields must not be added                                       | new non-key fields can be added |
| Fields             | position of key fields must not be changed                             |                                 |
| Fields             | data type must not be changed                                          |                                 |
| Fields             | length must not be changed                                             |                                 |
| Fields             | decimals must not be changed                                           |                                 |
| Fields             | output length must not be changed                                      |                                 |
| Fields             | conversion routine must not be changed                                 |                                 |
| Fields             | case-sensitivity must not be changed                                   |                                 |
