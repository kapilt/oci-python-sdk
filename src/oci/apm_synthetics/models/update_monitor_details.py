# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMonitorDetails(object):
    """
    Details of the request body used to update a monitor.
    """

    #: A constant which can be used with the status property of a UpdateMonitorDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a UpdateMonitorDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a UpdateMonitorDetails.
    #: This constant has a value of "INVALID"
    STATUS_INVALID = "INVALID"

    #: A constant which can be used with the scheduling_policy property of a UpdateMonitorDetails.
    #: This constant has a value of "ALL"
    SCHEDULING_POLICY_ALL = "ALL"

    #: A constant which can be used with the scheduling_policy property of a UpdateMonitorDetails.
    #: This constant has a value of "ROUND_ROBIN"
    SCHEDULING_POLICY_ROUND_ROBIN = "ROUND_ROBIN"

    #: A constant which can be used with the scheduling_policy property of a UpdateMonitorDetails.
    #: This constant has a value of "BATCHED_ROUND_ROBIN"
    SCHEDULING_POLICY_BATCHED_ROUND_ROBIN = "BATCHED_ROUND_ROBIN"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMonitorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateMonitorDetails.
        :type display_name: str

        :param vantage_points:
            The value to assign to the vantage_points property of this UpdateMonitorDetails.
        :type vantage_points: list[str]

        :param script_id:
            The value to assign to the script_id property of this UpdateMonitorDetails.
        :type script_id: str

        :param status:
            The value to assign to the status property of this UpdateMonitorDetails.
            Allowed values for this property are: "ENABLED", "DISABLED", "INVALID"
        :type status: str

        :param repeat_interval_in_seconds:
            The value to assign to the repeat_interval_in_seconds property of this UpdateMonitorDetails.
        :type repeat_interval_in_seconds: int

        :param is_run_once:
            The value to assign to the is_run_once property of this UpdateMonitorDetails.
        :type is_run_once: bool

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this UpdateMonitorDetails.
        :type timeout_in_seconds: int

        :param target:
            The value to assign to the target property of this UpdateMonitorDetails.
        :type target: str

        :param script_parameters:
            The value to assign to the script_parameters property of this UpdateMonitorDetails.
        :type script_parameters: list[oci.apm_synthetics.models.MonitorScriptParameter]

        :param configuration:
            The value to assign to the configuration property of this UpdateMonitorDetails.
        :type configuration: oci.apm_synthetics.models.MonitorConfiguration

        :param availability_configuration:
            The value to assign to the availability_configuration property of this UpdateMonitorDetails.
        :type availability_configuration: oci.apm_synthetics.models.AvailabilityConfiguration

        :param maintenance_window_schedule:
            The value to assign to the maintenance_window_schedule property of this UpdateMonitorDetails.
        :type maintenance_window_schedule: oci.apm_synthetics.models.MaintenanceWindowSchedule

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMonitorDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMonitorDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param is_run_now:
            The value to assign to the is_run_now property of this UpdateMonitorDetails.
        :type is_run_now: bool

        :param scheduling_policy:
            The value to assign to the scheduling_policy property of this UpdateMonitorDetails.
            Allowed values for this property are: "ALL", "ROUND_ROBIN", "BATCHED_ROUND_ROBIN"
        :type scheduling_policy: str

        :param batch_interval_in_seconds:
            The value to assign to the batch_interval_in_seconds property of this UpdateMonitorDetails.
        :type batch_interval_in_seconds: int

        """
        self.swagger_types = {
            'display_name': 'str',
            'vantage_points': 'list[str]',
            'script_id': 'str',
            'status': 'str',
            'repeat_interval_in_seconds': 'int',
            'is_run_once': 'bool',
            'timeout_in_seconds': 'int',
            'target': 'str',
            'script_parameters': 'list[MonitorScriptParameter]',
            'configuration': 'MonitorConfiguration',
            'availability_configuration': 'AvailabilityConfiguration',
            'maintenance_window_schedule': 'MaintenanceWindowSchedule',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_run_now': 'bool',
            'scheduling_policy': 'str',
            'batch_interval_in_seconds': 'int'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'vantage_points': 'vantagePoints',
            'script_id': 'scriptId',
            'status': 'status',
            'repeat_interval_in_seconds': 'repeatIntervalInSeconds',
            'is_run_once': 'isRunOnce',
            'timeout_in_seconds': 'timeoutInSeconds',
            'target': 'target',
            'script_parameters': 'scriptParameters',
            'configuration': 'configuration',
            'availability_configuration': 'availabilityConfiguration',
            'maintenance_window_schedule': 'maintenanceWindowSchedule',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_run_now': 'isRunNow',
            'scheduling_policy': 'schedulingPolicy',
            'batch_interval_in_seconds': 'batchIntervalInSeconds'
        }

        self._display_name = None
        self._vantage_points = None
        self._script_id = None
        self._status = None
        self._repeat_interval_in_seconds = None
        self._is_run_once = None
        self._timeout_in_seconds = None
        self._target = None
        self._script_parameters = None
        self._configuration = None
        self._availability_configuration = None
        self._maintenance_window_schedule = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_run_now = None
        self._scheduling_policy = None
        self._batch_interval_in_seconds = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMonitorDetails.
        Unique name that can be edited. The name should not contain any confidential information.


        :return: The display_name of this UpdateMonitorDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMonitorDetails.
        Unique name that can be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this UpdateMonitorDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def vantage_points(self):
        """
        Gets the vantage_points of this UpdateMonitorDetails.
        A list of public and dedicated vantage points from which to execute the monitor.
        Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.


        :return: The vantage_points of this UpdateMonitorDetails.
        :rtype: list[str]
        """
        return self._vantage_points

    @vantage_points.setter
    def vantage_points(self, vantage_points):
        """
        Sets the vantage_points of this UpdateMonitorDetails.
        A list of public and dedicated vantage points from which to execute the monitor.
        Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.


        :param vantage_points: The vantage_points of this UpdateMonitorDetails.
        :type: list[str]
        """
        self._vantage_points = vantage_points

    @property
    def script_id(self):
        """
        Gets the script_id of this UpdateMonitorDetails.
        The `OCID`__ of the script.
        scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The script_id of this UpdateMonitorDetails.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this UpdateMonitorDetails.
        The `OCID`__ of the script.
        scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param script_id: The script_id of this UpdateMonitorDetails.
        :type: str
        """
        self._script_id = script_id

    @property
    def status(self):
        """
        Gets the status of this UpdateMonitorDetails.
        Enables or disables the monitor.

        Allowed values for this property are: "ENABLED", "DISABLED", "INVALID"


        :return: The status of this UpdateMonitorDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateMonitorDetails.
        Enables or disables the monitor.


        :param status: The status of this UpdateMonitorDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "INVALID"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def repeat_interval_in_seconds(self):
        """
        Gets the repeat_interval_in_seconds of this UpdateMonitorDetails.
        Interval in seconds after the start time when the job should be repeated.
        Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.


        :return: The repeat_interval_in_seconds of this UpdateMonitorDetails.
        :rtype: int
        """
        return self._repeat_interval_in_seconds

    @repeat_interval_in_seconds.setter
    def repeat_interval_in_seconds(self, repeat_interval_in_seconds):
        """
        Sets the repeat_interval_in_seconds of this UpdateMonitorDetails.
        Interval in seconds after the start time when the job should be repeated.
        Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.


        :param repeat_interval_in_seconds: The repeat_interval_in_seconds of this UpdateMonitorDetails.
        :type: int
        """
        self._repeat_interval_in_seconds = repeat_interval_in_seconds

    @property
    def is_run_once(self):
        """
        Gets the is_run_once of this UpdateMonitorDetails.
        If runOnce is enabled, then the monitor will run once.


        :return: The is_run_once of this UpdateMonitorDetails.
        :rtype: bool
        """
        return self._is_run_once

    @is_run_once.setter
    def is_run_once(self, is_run_once):
        """
        Sets the is_run_once of this UpdateMonitorDetails.
        If runOnce is enabled, then the monitor will run once.


        :param is_run_once: The is_run_once of this UpdateMonitorDetails.
        :type: bool
        """
        self._is_run_once = is_run_once

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this UpdateMonitorDetails.
        Timeout in seconds. If isFailureRetried is true, then timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors.
        If isFailureRetried is false, then timeout cannot be more than 50% of repeatIntervalInSeconds time for monitors.
        Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors.
        Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.


        :return: The timeout_in_seconds of this UpdateMonitorDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this UpdateMonitorDetails.
        Timeout in seconds. If isFailureRetried is true, then timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors.
        If isFailureRetried is false, then timeout cannot be more than 50% of repeatIntervalInSeconds time for monitors.
        Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors.
        Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.


        :param timeout_in_seconds: The timeout_in_seconds of this UpdateMonitorDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def target(self):
        """
        Gets the target of this UpdateMonitorDetails.
        Specify the endpoint on which to run the monitor.
        For BROWSER and REST monitor types, target is mandatory.
        If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint.
        If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.


        :return: The target of this UpdateMonitorDetails.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this UpdateMonitorDetails.
        Specify the endpoint on which to run the monitor.
        For BROWSER and REST monitor types, target is mandatory.
        If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint.
        If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.


        :param target: The target of this UpdateMonitorDetails.
        :type: str
        """
        self._target = target

    @property
    def script_parameters(self):
        """
        Gets the script_parameters of this UpdateMonitorDetails.
        List of script parameters in the monitor.
        This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.
        Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`


        :return: The script_parameters of this UpdateMonitorDetails.
        :rtype: list[oci.apm_synthetics.models.MonitorScriptParameter]
        """
        return self._script_parameters

    @script_parameters.setter
    def script_parameters(self, script_parameters):
        """
        Sets the script_parameters of this UpdateMonitorDetails.
        List of script parameters in the monitor.
        This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.
        Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`


        :param script_parameters: The script_parameters of this UpdateMonitorDetails.
        :type: list[oci.apm_synthetics.models.MonitorScriptParameter]
        """
        self._script_parameters = script_parameters

    @property
    def configuration(self):
        """
        Gets the configuration of this UpdateMonitorDetails.

        :return: The configuration of this UpdateMonitorDetails.
        :rtype: oci.apm_synthetics.models.MonitorConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this UpdateMonitorDetails.

        :param configuration: The configuration of this UpdateMonitorDetails.
        :type: oci.apm_synthetics.models.MonitorConfiguration
        """
        self._configuration = configuration

    @property
    def availability_configuration(self):
        """
        Gets the availability_configuration of this UpdateMonitorDetails.

        :return: The availability_configuration of this UpdateMonitorDetails.
        :rtype: oci.apm_synthetics.models.AvailabilityConfiguration
        """
        return self._availability_configuration

    @availability_configuration.setter
    def availability_configuration(self, availability_configuration):
        """
        Sets the availability_configuration of this UpdateMonitorDetails.

        :param availability_configuration: The availability_configuration of this UpdateMonitorDetails.
        :type: oci.apm_synthetics.models.AvailabilityConfiguration
        """
        self._availability_configuration = availability_configuration

    @property
    def maintenance_window_schedule(self):
        """
        Gets the maintenance_window_schedule of this UpdateMonitorDetails.

        :return: The maintenance_window_schedule of this UpdateMonitorDetails.
        :rtype: oci.apm_synthetics.models.MaintenanceWindowSchedule
        """
        return self._maintenance_window_schedule

    @maintenance_window_schedule.setter
    def maintenance_window_schedule(self, maintenance_window_schedule):
        """
        Sets the maintenance_window_schedule of this UpdateMonitorDetails.

        :param maintenance_window_schedule: The maintenance_window_schedule of this UpdateMonitorDetails.
        :type: oci.apm_synthetics.models.MaintenanceWindowSchedule
        """
        self._maintenance_window_schedule = maintenance_window_schedule

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateMonitorDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateMonitorDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateMonitorDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateMonitorDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateMonitorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateMonitorDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateMonitorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateMonitorDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_run_now(self):
        """
        Gets the is_run_now of this UpdateMonitorDetails.
        If isRunNow is enabled, then the monitor will run now.


        :return: The is_run_now of this UpdateMonitorDetails.
        :rtype: bool
        """
        return self._is_run_now

    @is_run_now.setter
    def is_run_now(self, is_run_now):
        """
        Sets the is_run_now of this UpdateMonitorDetails.
        If isRunNow is enabled, then the monitor will run now.


        :param is_run_now: The is_run_now of this UpdateMonitorDetails.
        :type: bool
        """
        self._is_run_now = is_run_now

    @property
    def scheduling_policy(self):
        """
        Gets the scheduling_policy of this UpdateMonitorDetails.
        Scheduling policy on Vantage points.

        Allowed values for this property are: "ALL", "ROUND_ROBIN", "BATCHED_ROUND_ROBIN"


        :return: The scheduling_policy of this UpdateMonitorDetails.
        :rtype: str
        """
        return self._scheduling_policy

    @scheduling_policy.setter
    def scheduling_policy(self, scheduling_policy):
        """
        Sets the scheduling_policy of this UpdateMonitorDetails.
        Scheduling policy on Vantage points.


        :param scheduling_policy: The scheduling_policy of this UpdateMonitorDetails.
        :type: str
        """
        allowed_values = ["ALL", "ROUND_ROBIN", "BATCHED_ROUND_ROBIN"]
        if not value_allowed_none_or_none_sentinel(scheduling_policy, allowed_values):
            raise ValueError(
                "Invalid value for `scheduling_policy`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._scheduling_policy = scheduling_policy

    @property
    def batch_interval_in_seconds(self):
        """
        Gets the batch_interval_in_seconds of this UpdateMonitorDetails.
        Time interval between 2 runs in round robin batch mode (*SchedulingPolicy - BATCHED_ROUND_ROBIN).


        :return: The batch_interval_in_seconds of this UpdateMonitorDetails.
        :rtype: int
        """
        return self._batch_interval_in_seconds

    @batch_interval_in_seconds.setter
    def batch_interval_in_seconds(self, batch_interval_in_seconds):
        """
        Sets the batch_interval_in_seconds of this UpdateMonitorDetails.
        Time interval between 2 runs in round robin batch mode (*SchedulingPolicy - BATCHED_ROUND_ROBIN).


        :param batch_interval_in_seconds: The batch_interval_in_seconds of this UpdateMonitorDetails.
        :type: int
        """
        self._batch_interval_in_seconds = batch_interval_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
