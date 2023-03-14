# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyGroup(object):
    """
    Group resource.
    """

    #: A constant which can be used with the idcs_prevented_operations property of a MyGroup.
    #: This constant has a value of "replace"
    IDCS_PREVENTED_OPERATIONS_REPLACE = "replace"

    #: A constant which can be used with the idcs_prevented_operations property of a MyGroup.
    #: This constant has a value of "update"
    IDCS_PREVENTED_OPERATIONS_UPDATE = "update"

    #: A constant which can be used with the idcs_prevented_operations property of a MyGroup.
    #: This constant has a value of "delete"
    IDCS_PREVENTED_OPERATIONS_DELETE = "delete"

    def __init__(self, **kwargs):
        """
        Initializes a new MyGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MyGroup.
        :type id: str

        :param ocid:
            The value to assign to the ocid property of this MyGroup.
        :type ocid: str

        :param schemas:
            The value to assign to the schemas property of this MyGroup.
        :type schemas: list[str]

        :param meta:
            The value to assign to the meta property of this MyGroup.
        :type meta: oci.identity_domains.models.Meta

        :param idcs_created_by:
            The value to assign to the idcs_created_by property of this MyGroup.
        :type idcs_created_by: oci.identity_domains.models.IdcsCreatedBy

        :param idcs_last_modified_by:
            The value to assign to the idcs_last_modified_by property of this MyGroup.
        :type idcs_last_modified_by: oci.identity_domains.models.IdcsLastModifiedBy

        :param idcs_prevented_operations:
            The value to assign to the idcs_prevented_operations property of this MyGroup.
            Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type idcs_prevented_operations: list[str]

        :param tags:
            The value to assign to the tags property of this MyGroup.
        :type tags: list[oci.identity_domains.models.Tags]

        :param delete_in_progress:
            The value to assign to the delete_in_progress property of this MyGroup.
        :type delete_in_progress: bool

        :param idcs_last_upgraded_in_release:
            The value to assign to the idcs_last_upgraded_in_release property of this MyGroup.
        :type idcs_last_upgraded_in_release: str

        :param domain_ocid:
            The value to assign to the domain_ocid property of this MyGroup.
        :type domain_ocid: str

        :param compartment_ocid:
            The value to assign to the compartment_ocid property of this MyGroup.
        :type compartment_ocid: str

        :param tenancy_ocid:
            The value to assign to the tenancy_ocid property of this MyGroup.
        :type tenancy_ocid: str

        :param external_id:
            The value to assign to the external_id property of this MyGroup.
        :type external_id: str

        :param display_name:
            The value to assign to the display_name property of this MyGroup.
        :type display_name: str

        :param non_unique_display_name:
            The value to assign to the non_unique_display_name property of this MyGroup.
        :type non_unique_display_name: str

        :param members:
            The value to assign to the members property of this MyGroup.
        :type members: list[oci.identity_domains.models.MyGroupMembers]

        :param urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group:
            The value to assign to the urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group property of this MyGroup.
        :type urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group: oci.identity_domains.models.ExtensionGroupGroup

        :param urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group:
            The value to assign to the urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group property of this MyGroup.
        :type urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group: oci.identity_domains.models.ExtensionPosixGroup

        """
        self.swagger_types = {
            'id': 'str',
            'ocid': 'str',
            'schemas': 'list[str]',
            'meta': 'Meta',
            'idcs_created_by': 'IdcsCreatedBy',
            'idcs_last_modified_by': 'IdcsLastModifiedBy',
            'idcs_prevented_operations': 'list[str]',
            'tags': 'list[Tags]',
            'delete_in_progress': 'bool',
            'idcs_last_upgraded_in_release': 'str',
            'domain_ocid': 'str',
            'compartment_ocid': 'str',
            'tenancy_ocid': 'str',
            'external_id': 'str',
            'display_name': 'str',
            'non_unique_display_name': 'str',
            'members': 'list[MyGroupMembers]',
            'urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group': 'ExtensionGroupGroup',
            'urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group': 'ExtensionPosixGroup'
        }

        self.attribute_map = {
            'id': 'id',
            'ocid': 'ocid',
            'schemas': 'schemas',
            'meta': 'meta',
            'idcs_created_by': 'idcsCreatedBy',
            'idcs_last_modified_by': 'idcsLastModifiedBy',
            'idcs_prevented_operations': 'idcsPreventedOperations',
            'tags': 'tags',
            'delete_in_progress': 'deleteInProgress',
            'idcs_last_upgraded_in_release': 'idcsLastUpgradedInRelease',
            'domain_ocid': 'domainOcid',
            'compartment_ocid': 'compartmentOcid',
            'tenancy_ocid': 'tenancyOcid',
            'external_id': 'externalId',
            'display_name': 'displayName',
            'non_unique_display_name': 'nonUniqueDisplayName',
            'members': 'members',
            'urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:group:Group',
            'urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:Group'
        }

        self._id = None
        self._ocid = None
        self._schemas = None
        self._meta = None
        self._idcs_created_by = None
        self._idcs_last_modified_by = None
        self._idcs_prevented_operations = None
        self._tags = None
        self._delete_in_progress = None
        self._idcs_last_upgraded_in_release = None
        self._domain_ocid = None
        self._compartment_ocid = None
        self._tenancy_ocid = None
        self._external_id = None
        self._display_name = None
        self._non_unique_display_name = None
        self._members = None
        self._urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group = None
        self._urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group = None

    @property
    def id(self):
        """
        Gets the id of this MyGroup.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :return: The id of this MyGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MyGroup.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :param id: The id of this MyGroup.
        :type: str
        """
        self._id = id

    @property
    def ocid(self):
        """
        Gets the ocid of this MyGroup.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :return: The ocid of this MyGroup.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this MyGroup.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :param ocid: The ocid of this MyGroup.
        :type: str
        """
        self._ocid = ocid

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this MyGroup.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The schemas of this MyGroup.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this MyGroup.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param schemas: The schemas of this MyGroup.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def meta(self):
        """
        Gets the meta of this MyGroup.

        :return: The meta of this MyGroup.
        :rtype: oci.identity_domains.models.Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this MyGroup.

        :param meta: The meta of this MyGroup.
        :type: oci.identity_domains.models.Meta
        """
        self._meta = meta

    @property
    def idcs_created_by(self):
        """
        Gets the idcs_created_by of this MyGroup.

        :return: The idcs_created_by of this MyGroup.
        :rtype: oci.identity_domains.models.IdcsCreatedBy
        """
        return self._idcs_created_by

    @idcs_created_by.setter
    def idcs_created_by(self, idcs_created_by):
        """
        Sets the idcs_created_by of this MyGroup.

        :param idcs_created_by: The idcs_created_by of this MyGroup.
        :type: oci.identity_domains.models.IdcsCreatedBy
        """
        self._idcs_created_by = idcs_created_by

    @property
    def idcs_last_modified_by(self):
        """
        Gets the idcs_last_modified_by of this MyGroup.

        :return: The idcs_last_modified_by of this MyGroup.
        :rtype: oci.identity_domains.models.IdcsLastModifiedBy
        """
        return self._idcs_last_modified_by

    @idcs_last_modified_by.setter
    def idcs_last_modified_by(self, idcs_last_modified_by):
        """
        Sets the idcs_last_modified_by of this MyGroup.

        :param idcs_last_modified_by: The idcs_last_modified_by of this MyGroup.
        :type: oci.identity_domains.models.IdcsLastModifiedBy
        """
        self._idcs_last_modified_by = idcs_last_modified_by

    @property
    def idcs_prevented_operations(self):
        """
        Gets the idcs_prevented_operations of this MyGroup.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The idcs_prevented_operations of this MyGroup.
        :rtype: list[str]
        """
        return self._idcs_prevented_operations

    @idcs_prevented_operations.setter
    def idcs_prevented_operations(self, idcs_prevented_operations):
        """
        Sets the idcs_prevented_operations of this MyGroup.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_prevented_operations: The idcs_prevented_operations of this MyGroup.
        :type: list[str]
        """
        allowed_values = ["replace", "update", "delete"]
        if idcs_prevented_operations:
            idcs_prevented_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in idcs_prevented_operations]
        self._idcs_prevented_operations = idcs_prevented_operations

    @property
    def tags(self):
        """
        Gets the tags of this MyGroup.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The tags of this MyGroup.
        :rtype: list[oci.identity_domains.models.Tags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this MyGroup.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param tags: The tags of this MyGroup.
        :type: list[oci.identity_domains.models.Tags]
        """
        self._tags = tags

    @property
    def delete_in_progress(self):
        """
        Gets the delete_in_progress of this MyGroup.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The delete_in_progress of this MyGroup.
        :rtype: bool
        """
        return self._delete_in_progress

    @delete_in_progress.setter
    def delete_in_progress(self, delete_in_progress):
        """
        Sets the delete_in_progress of this MyGroup.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param delete_in_progress: The delete_in_progress of this MyGroup.
        :type: bool
        """
        self._delete_in_progress = delete_in_progress

    @property
    def idcs_last_upgraded_in_release(self):
        """
        Gets the idcs_last_upgraded_in_release of this MyGroup.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The idcs_last_upgraded_in_release of this MyGroup.
        :rtype: str
        """
        return self._idcs_last_upgraded_in_release

    @idcs_last_upgraded_in_release.setter
    def idcs_last_upgraded_in_release(self, idcs_last_upgraded_in_release):
        """
        Sets the idcs_last_upgraded_in_release of this MyGroup.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_last_upgraded_in_release: The idcs_last_upgraded_in_release of this MyGroup.
        :type: str
        """
        self._idcs_last_upgraded_in_release = idcs_last_upgraded_in_release

    @property
    def domain_ocid(self):
        """
        Gets the domain_ocid of this MyGroup.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The domain_ocid of this MyGroup.
        :rtype: str
        """
        return self._domain_ocid

    @domain_ocid.setter
    def domain_ocid(self, domain_ocid):
        """
        Sets the domain_ocid of this MyGroup.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param domain_ocid: The domain_ocid of this MyGroup.
        :type: str
        """
        self._domain_ocid = domain_ocid

    @property
    def compartment_ocid(self):
        """
        Gets the compartment_ocid of this MyGroup.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The compartment_ocid of this MyGroup.
        :rtype: str
        """
        return self._compartment_ocid

    @compartment_ocid.setter
    def compartment_ocid(self, compartment_ocid):
        """
        Sets the compartment_ocid of this MyGroup.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param compartment_ocid: The compartment_ocid of this MyGroup.
        :type: str
        """
        self._compartment_ocid = compartment_ocid

    @property
    def tenancy_ocid(self):
        """
        Gets the tenancy_ocid of this MyGroup.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The tenancy_ocid of this MyGroup.
        :rtype: str
        """
        return self._tenancy_ocid

    @tenancy_ocid.setter
    def tenancy_ocid(self, tenancy_ocid):
        """
        Sets the tenancy_ocid of this MyGroup.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param tenancy_ocid: The tenancy_ocid of this MyGroup.
        :type: str
        """
        self._tenancy_ocid = tenancy_ocid

    @property
    def external_id(self):
        """
        Gets the external_id of this MyGroup.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The external_id of this MyGroup.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this MyGroup.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param external_id: The external_id of this MyGroup.
        :type: str
        """
        self._external_id = external_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MyGroup.
        Group display name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Display Name
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Name, deprecatedColumnHeaderName:Display Name]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: global


        :return: The display_name of this MyGroup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MyGroup.
        Group display name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Display Name
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Name, deprecatedColumnHeaderName:Display Name]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: global


        :param display_name: The display_name of this MyGroup.
        :type: str
        """
        self._display_name = display_name

    @property
    def non_unique_display_name(self):
        """
        Gets the non_unique_display_name of this MyGroup.
        A human readable name for Group as defined by the Service Consumer

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Non-Unique Display Name
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: always
         - type: string


        :return: The non_unique_display_name of this MyGroup.
        :rtype: str
        """
        return self._non_unique_display_name

    @non_unique_display_name.setter
    def non_unique_display_name(self, non_unique_display_name):
        """
        Sets the non_unique_display_name of this MyGroup.
        A human readable name for Group as defined by the Service Consumer

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Non-Unique Display Name
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: always
         - type: string


        :param non_unique_display_name: The non_unique_display_name of this MyGroup.
        :type: str
        """
        self._non_unique_display_name = non_unique_display_name

    @property
    def members(self):
        """
        Gets the members of this MyGroup.
        Group members - when requesting members attribute, a max of 10,000 members will be returned in a single request. It is recommended to use startIndex and count to return members in pages instead of in a single response, eg : #attributes=members[startIndex=1%26count=10]

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCompositeKey: [value]
         - idcsCsvAttributeNameMappings: [[columnHeaderName:User Members, mapsTo:members[User].value, multiValueDelimiter:;]]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - idcsPaginateResponse: true
         - type: complex
         - uniqueness: none


        :return: The members of this MyGroup.
        :rtype: list[oci.identity_domains.models.MyGroupMembers]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this MyGroup.
        Group members - when requesting members attribute, a max of 10,000 members will be returned in a single request. It is recommended to use startIndex and count to return members in pages instead of in a single response, eg : #attributes=members[startIndex=1%26count=10]

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCompositeKey: [value]
         - idcsCsvAttributeNameMappings: [[columnHeaderName:User Members, mapsTo:members[User].value, multiValueDelimiter:;]]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - idcsPaginateResponse: true
         - type: complex
         - uniqueness: none


        :param members: The members of this MyGroup.
        :type: list[oci.identity_domains.models.MyGroupMembers]
        """
        self._members = members

    @property
    def urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group(self):
        """
        Gets the urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group of this MyGroup.

        :return: The urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group of this MyGroup.
        :rtype: oci.identity_domains.models.ExtensionGroupGroup
        """
        return self._urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group

    @urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group.setter
    def urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group(self, urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group):
        """
        Sets the urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group of this MyGroup.

        :param urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group: The urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group of this MyGroup.
        :type: oci.identity_domains.models.ExtensionGroupGroup
        """
        self._urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group = urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group

    @property
    def urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group(self):
        """
        Gets the urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group of this MyGroup.

        :return: The urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group of this MyGroup.
        :rtype: oci.identity_domains.models.ExtensionPosixGroup
        """
        return self._urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group

    @urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group.setter
    def urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group(self, urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group):
        """
        Sets the urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group of this MyGroup.

        :param urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group: The urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group of this MyGroup.
        :type: oci.identity_domains.models.ExtensionPosixGroup
        """
        self._urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group = urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
