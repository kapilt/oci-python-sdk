# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PodShape(object):
    """
    Pod shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PodShape object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this PodShape.
        :type name: str

        :param processor_description:
            The value to assign to the processor_description property of this PodShape.
        :type processor_description: str

        :param ocpu_options:
            The value to assign to the ocpu_options property of this PodShape.
        :type ocpu_options: list[oci.container_engine.models.ShapeOcpuOptions]

        :param memory_options:
            The value to assign to the memory_options property of this PodShape.
        :type memory_options: list[oci.container_engine.models.ShapeMemoryOptions]

        :param network_bandwidth_options:
            The value to assign to the network_bandwidth_options property of this PodShape.
        :type network_bandwidth_options: list[oci.container_engine.models.ShapeNetworkBandwidthOptions]

        """
        self.swagger_types = {
            'name': 'str',
            'processor_description': 'str',
            'ocpu_options': 'list[ShapeOcpuOptions]',
            'memory_options': 'list[ShapeMemoryOptions]',
            'network_bandwidth_options': 'list[ShapeNetworkBandwidthOptions]'
        }

        self.attribute_map = {
            'name': 'name',
            'processor_description': 'processorDescription',
            'ocpu_options': 'ocpuOptions',
            'memory_options': 'memoryOptions',
            'network_bandwidth_options': 'networkBandwidthOptions'
        }

        self._name = None
        self._processor_description = None
        self._ocpu_options = None
        self._memory_options = None
        self._network_bandwidth_options = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PodShape.
        The name of the identifying shape.


        :return: The name of this PodShape.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PodShape.
        The name of the identifying shape.


        :param name: The name of this PodShape.
        :type: str
        """
        self._name = name

    @property
    def processor_description(self):
        """
        Gets the processor_description of this PodShape.
        A short description of the VM's processor (CPU).


        :return: The processor_description of this PodShape.
        :rtype: str
        """
        return self._processor_description

    @processor_description.setter
    def processor_description(self, processor_description):
        """
        Sets the processor_description of this PodShape.
        A short description of the VM's processor (CPU).


        :param processor_description: The processor_description of this PodShape.
        :type: str
        """
        self._processor_description = processor_description

    @property
    def ocpu_options(self):
        """
        Gets the ocpu_options of this PodShape.
        Options for OCPU shape.


        :return: The ocpu_options of this PodShape.
        :rtype: list[oci.container_engine.models.ShapeOcpuOptions]
        """
        return self._ocpu_options

    @ocpu_options.setter
    def ocpu_options(self, ocpu_options):
        """
        Sets the ocpu_options of this PodShape.
        Options for OCPU shape.


        :param ocpu_options: The ocpu_options of this PodShape.
        :type: list[oci.container_engine.models.ShapeOcpuOptions]
        """
        self._ocpu_options = ocpu_options

    @property
    def memory_options(self):
        """
        Gets the memory_options of this PodShape.
        ShapeMemoryOptions.


        :return: The memory_options of this PodShape.
        :rtype: list[oci.container_engine.models.ShapeMemoryOptions]
        """
        return self._memory_options

    @memory_options.setter
    def memory_options(self, memory_options):
        """
        Sets the memory_options of this PodShape.
        ShapeMemoryOptions.


        :param memory_options: The memory_options of this PodShape.
        :type: list[oci.container_engine.models.ShapeMemoryOptions]
        """
        self._memory_options = memory_options

    @property
    def network_bandwidth_options(self):
        """
        Gets the network_bandwidth_options of this PodShape.
        ShapeNetworkBandwidthOptions.


        :return: The network_bandwidth_options of this PodShape.
        :rtype: list[oci.container_engine.models.ShapeNetworkBandwidthOptions]
        """
        return self._network_bandwidth_options

    @network_bandwidth_options.setter
    def network_bandwidth_options(self, network_bandwidth_options):
        """
        Sets the network_bandwidth_options of this PodShape.
        ShapeNetworkBandwidthOptions.


        :param network_bandwidth_options: The network_bandwidth_options of this PodShape.
        :type: list[oci.container_engine.models.ShapeNetworkBandwidthOptions]
        """
        self._network_bandwidth_options = network_bandwidth_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
