# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublicIpPool(object):
    """
    A public IP pool is a set of public IP addresses represented as one or more IPv4 CIDR blocks. Resources like load balancers and compute instances can be allocated public IP addresses from a public IP pool.
    """

    #: A constant which can be used with the lifecycle_state property of a PublicIpPool.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PublicIpPool.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a PublicIpPool.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PublicIpPool.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a PublicIpPool.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new PublicIpPool object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_blocks:
            The value to assign to the cidr_blocks property of this PublicIpPool.
        :type cidr_blocks: list[str]

        :param compartment_id:
            The value to assign to the compartment_id property of this PublicIpPool.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this PublicIpPool.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this PublicIpPool.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PublicIpPool.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this PublicIpPool.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PublicIpPool.
            Allowed values for this property are: "INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this PublicIpPool.
        :type time_created: datetime

        """
        self.swagger_types = {
            'cidr_blocks': 'list[str]',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'cidr_blocks': 'cidrBlocks',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._cidr_blocks = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def cidr_blocks(self):
        """
        Gets the cidr_blocks of this PublicIpPool.
        The CIDR blocks added to this pool. This could be all or a portion of a BYOIP CIDR block.


        :return: The cidr_blocks of this PublicIpPool.
        :rtype: list[str]
        """
        return self._cidr_blocks

    @cidr_blocks.setter
    def cidr_blocks(self, cidr_blocks):
        """
        Sets the cidr_blocks of this PublicIpPool.
        The CIDR blocks added to this pool. This could be all or a portion of a BYOIP CIDR block.


        :param cidr_blocks: The cidr_blocks of this PublicIpPool.
        :type: list[str]
        """
        self._cidr_blocks = cidr_blocks

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PublicIpPool.
        The `OCID`__ of the compartment containing this pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PublicIpPool.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PublicIpPool.
        The `OCID`__ of the compartment containing this pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PublicIpPool.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PublicIpPool.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this PublicIpPool.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PublicIpPool.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this PublicIpPool.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this PublicIpPool.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this PublicIpPool.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PublicIpPool.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this PublicIpPool.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PublicIpPool.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this PublicIpPool.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PublicIpPool.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this PublicIpPool.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PublicIpPool.
        The `OCID`__ of the public IP pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this PublicIpPool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PublicIpPool.
        The `OCID`__ of the public IP pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this PublicIpPool.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this PublicIpPool.
        The public IP pool's current state.

        Allowed values for this property are: "INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PublicIpPool.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PublicIpPool.
        The public IP pool's current state.


        :param lifecycle_state: The lifecycle_state of this PublicIpPool.
        :type: str
        """
        allowed_values = ["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PublicIpPool.
        The date and time the public IP pool was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PublicIpPool.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PublicIpPool.
        The date and time the public IP pool was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PublicIpPool.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
