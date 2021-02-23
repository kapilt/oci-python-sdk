# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Ipv6(object):
    """
    An *IPv6* is a conceptual term that refers to an IPv6 address and related properties.
    The `IPv6` object is the API representation of an IPv6.

    You can create and assign an IPv6 to any VNIC that is in an IPv6-enabled subnet in an
    IPv6-enabled VCN.

    **Note:** IPv6 addressing is currently supported only in certain regions. For important
    details about IPv6 addressing in a VCN, see `IPv6 Addresses`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Ipv6.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Ipv6.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Ipv6.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a Ipv6.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new Ipv6 object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Ipv6.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Ipv6.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Ipv6.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Ipv6.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Ipv6.
        :type id: str

        :param ip_address:
            The value to assign to the ip_address property of this Ipv6.
        :type ip_address: str

        :param is_internet_access_allowed:
            The value to assign to the is_internet_access_allowed property of this Ipv6.
        :type is_internet_access_allowed: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Ipv6.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param public_ip_address:
            The value to assign to the public_ip_address property of this Ipv6.
        :type public_ip_address: str

        :param subnet_id:
            The value to assign to the subnet_id property of this Ipv6.
        :type subnet_id: str

        :param time_created:
            The value to assign to the time_created property of this Ipv6.
        :type time_created: datetime

        :param vnic_id:
            The value to assign to the vnic_id property of this Ipv6.
        :type vnic_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'ip_address': 'str',
            'is_internet_access_allowed': 'bool',
            'lifecycle_state': 'str',
            'public_ip_address': 'str',
            'subnet_id': 'str',
            'time_created': 'datetime',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'ip_address': 'ipAddress',
            'is_internet_access_allowed': 'isInternetAccessAllowed',
            'lifecycle_state': 'lifecycleState',
            'public_ip_address': 'publicIpAddress',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated',
            'vnic_id': 'vnicId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._ip_address = None
        self._is_internet_access_allowed = None
        self._lifecycle_state = None
        self._public_ip_address = None
        self._subnet_id = None
        self._time_created = None
        self._vnic_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Ipv6.
        The `OCID`__ of the compartment containing the IPv6.
        This is the same as the VNIC's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Ipv6.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Ipv6.
        The `OCID`__ of the compartment containing the IPv6.
        This is the same as the VNIC's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Ipv6.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Ipv6.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Ipv6.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Ipv6.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Ipv6.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Ipv6.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this Ipv6.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Ipv6.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this Ipv6.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Ipv6.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Ipv6.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Ipv6.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Ipv6.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Ipv6.
        The `OCID`__ of the IPv6.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Ipv6.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Ipv6.
        The `OCID`__ of the IPv6.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Ipv6.
        :type: str
        """
        self._id = id

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this Ipv6.
        The IPv6 address of the `IPv6` object. The address is within the private IPv6 CIDR block
        of the VNIC's subnet (see the `ipv6CidrBlock` attribute for the :class:`Subnet`
        object.

        Example: `2001:0db8:0123:1111:abcd:ef01:2345:6789`


        :return: The ip_address of this Ipv6.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Ipv6.
        The IPv6 address of the `IPv6` object. The address is within the private IPv6 CIDR block
        of the VNIC's subnet (see the `ipv6CidrBlock` attribute for the :class:`Subnet`
        object.

        Example: `2001:0db8:0123:1111:abcd:ef01:2345:6789`


        :param ip_address: The ip_address of this Ipv6.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def is_internet_access_allowed(self):
        """
        Gets the is_internet_access_allowed of this Ipv6.
        Whether the IPv6 can be used for internet communication. Allowed by default for an IPv6 in
        a public subnet. Never allowed for an IPv6 in a private subnet. If the value is `true`, the
        IPv6 uses its public IP address for internet communication.

        Example: `true`


        :return: The is_internet_access_allowed of this Ipv6.
        :rtype: bool
        """
        return self._is_internet_access_allowed

    @is_internet_access_allowed.setter
    def is_internet_access_allowed(self, is_internet_access_allowed):
        """
        Sets the is_internet_access_allowed of this Ipv6.
        Whether the IPv6 can be used for internet communication. Allowed by default for an IPv6 in
        a public subnet. Never allowed for an IPv6 in a private subnet. If the value is `true`, the
        IPv6 uses its public IP address for internet communication.

        Example: `true`


        :param is_internet_access_allowed: The is_internet_access_allowed of this Ipv6.
        :type: bool
        """
        self._is_internet_access_allowed = is_internet_access_allowed

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Ipv6.
        The IPv6's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Ipv6.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Ipv6.
        The IPv6's current state.


        :param lifecycle_state: The lifecycle_state of this Ipv6.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def public_ip_address(self):
        """
        Gets the public_ip_address of this Ipv6.
        The IPv6 address to be used for internet communication. The address is within the public
        IPv6 CIDR block of the VNIC's subnet (see the `ipv6PublicCidrBlock` attribute for the
        :class:`Subnet` object).

        If your organization did NOT assign a custom IPv6 CIDR to the VCN for the private address
        space, Oracle provides the IPv6 CIDR and uses that same CIDR for the private and public
        address space. Therefore the `publicIpAddress` would be the same as the `ipAddress`.

        If your organization assigned a custom IPv6 CIDR to the VCN for the private address space,
        the right 80 bits of the IPv6 public IP (the subnet and address bits) are the same as for
        the `ipAddress`. But the left 48 bits are from the public IPv6 CIDR that Oracle assigned
        to the VCN.

        This is null if the IPv6 is created with `isInternetAccessAllowed` set to `false`.

        Example: `2001:0db8:0123:1111:abcd:ef01:2345:6789`


        :return: The public_ip_address of this Ipv6.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """
        Sets the public_ip_address of this Ipv6.
        The IPv6 address to be used for internet communication. The address is within the public
        IPv6 CIDR block of the VNIC's subnet (see the `ipv6PublicCidrBlock` attribute for the
        :class:`Subnet` object).

        If your organization did NOT assign a custom IPv6 CIDR to the VCN for the private address
        space, Oracle provides the IPv6 CIDR and uses that same CIDR for the private and public
        address space. Therefore the `publicIpAddress` would be the same as the `ipAddress`.

        If your organization assigned a custom IPv6 CIDR to the VCN for the private address space,
        the right 80 bits of the IPv6 public IP (the subnet and address bits) are the same as for
        the `ipAddress`. But the left 48 bits are from the public IPv6 CIDR that Oracle assigned
        to the VCN.

        This is null if the IPv6 is created with `isInternetAccessAllowed` set to `false`.

        Example: `2001:0db8:0123:1111:abcd:ef01:2345:6789`


        :param public_ip_address: The public_ip_address of this Ipv6.
        :type: str
        """
        self._public_ip_address = public_ip_address

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this Ipv6.
        The `OCID`__ of the subnet the VNIC is in.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this Ipv6.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Ipv6.
        The `OCID`__ of the subnet the VNIC is in.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this Ipv6.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Ipv6.
        The date and time the IPv6 was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Ipv6.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Ipv6.
        The date and time the IPv6 was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Ipv6.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this Ipv6.
        The `OCID`__ of the VNIC the IPv6 is assigned to.
        The VNIC and IPv6 must be in the same subnet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vnic_id of this Ipv6.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this Ipv6.
        The `OCID`__ of the VNIC the IPv6 is assigned to.
        The VNIC and IPv6 must be in the same subnet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vnic_id: The vnic_id of this Ipv6.
        :type: str
        """
        self._vnic_id = vnic_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
