# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RefreshActivitySummary(object):
    """
    Summary of the refresh activity.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RefreshActivitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RefreshActivitySummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this RefreshActivitySummary.
        :type display_name: str

        :param source_fusion_environment_id:
            The value to assign to the source_fusion_environment_id property of this RefreshActivitySummary.
        :type source_fusion_environment_id: str

        :param time_of_restoration_point:
            The value to assign to the time_of_restoration_point property of this RefreshActivitySummary.
        :type time_of_restoration_point: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RefreshActivitySummary.
        :type lifecycle_state: str

        :param time_scheduled_start:
            The value to assign to the time_scheduled_start property of this RefreshActivitySummary.
        :type time_scheduled_start: datetime

        :param time_expected_finish:
            The value to assign to the time_expected_finish property of this RefreshActivitySummary.
        :type time_expected_finish: datetime

        :param time_finished:
            The value to assign to the time_finished property of this RefreshActivitySummary.
        :type time_finished: datetime

        :param service_availability:
            The value to assign to the service_availability property of this RefreshActivitySummary.
        :type service_availability: str

        :param time_accepted:
            The value to assign to the time_accepted property of this RefreshActivitySummary.
        :type time_accepted: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RefreshActivitySummary.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this RefreshActivitySummary.
        :type lifecycle_details: str

        :param refresh_issue_details_list:
            The value to assign to the refresh_issue_details_list property of this RefreshActivitySummary.
        :type refresh_issue_details_list: list[oci.fusion_apps.models.RefreshIssueDetails]

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'source_fusion_environment_id': 'str',
            'time_of_restoration_point': 'datetime',
            'lifecycle_state': 'str',
            'time_scheduled_start': 'datetime',
            'time_expected_finish': 'datetime',
            'time_finished': 'datetime',
            'service_availability': 'str',
            'time_accepted': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'refresh_issue_details_list': 'list[RefreshIssueDetails]'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'source_fusion_environment_id': 'sourceFusionEnvironmentId',
            'time_of_restoration_point': 'timeOfRestorationPoint',
            'lifecycle_state': 'lifecycleState',
            'time_scheduled_start': 'timeScheduledStart',
            'time_expected_finish': 'timeExpectedFinish',
            'time_finished': 'timeFinished',
            'service_availability': 'serviceAvailability',
            'time_accepted': 'timeAccepted',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'refresh_issue_details_list': 'refreshIssueDetailsList'
        }

        self._id = None
        self._display_name = None
        self._source_fusion_environment_id = None
        self._time_of_restoration_point = None
        self._lifecycle_state = None
        self._time_scheduled_start = None
        self._time_expected_finish = None
        self._time_finished = None
        self._service_availability = None
        self._time_accepted = None
        self._time_updated = None
        self._lifecycle_details = None
        self._refresh_issue_details_list = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RefreshActivitySummary.
        The unique identifier (OCID) of the refresh activity. Can't be changed after creation.


        :return: The id of this RefreshActivitySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RefreshActivitySummary.
        The unique identifier (OCID) of the refresh activity. Can't be changed after creation.


        :param id: The id of this RefreshActivitySummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this RefreshActivitySummary.
        A friendly name for the refresh activity. Can be changed later.


        :return: The display_name of this RefreshActivitySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RefreshActivitySummary.
        A friendly name for the refresh activity. Can be changed later.


        :param display_name: The display_name of this RefreshActivitySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def source_fusion_environment_id(self):
        """
        **[Required]** Gets the source_fusion_environment_id of this RefreshActivitySummary.
        The OCID of the Fusion environment that is the source environment for the refresh.


        :return: The source_fusion_environment_id of this RefreshActivitySummary.
        :rtype: str
        """
        return self._source_fusion_environment_id

    @source_fusion_environment_id.setter
    def source_fusion_environment_id(self, source_fusion_environment_id):
        """
        Sets the source_fusion_environment_id of this RefreshActivitySummary.
        The OCID of the Fusion environment that is the source environment for the refresh.


        :param source_fusion_environment_id: The source_fusion_environment_id of this RefreshActivitySummary.
        :type: str
        """
        self._source_fusion_environment_id = source_fusion_environment_id

    @property
    def time_of_restoration_point(self):
        """
        Gets the time_of_restoration_point of this RefreshActivitySummary.
        The date and time of the most recent source environment backup used for the environment refresh.


        :return: The time_of_restoration_point of this RefreshActivitySummary.
        :rtype: datetime
        """
        return self._time_of_restoration_point

    @time_of_restoration_point.setter
    def time_of_restoration_point(self, time_of_restoration_point):
        """
        Sets the time_of_restoration_point of this RefreshActivitySummary.
        The date and time of the most recent source environment backup used for the environment refresh.


        :param time_of_restoration_point: The time_of_restoration_point of this RefreshActivitySummary.
        :type: datetime
        """
        self._time_of_restoration_point = time_of_restoration_point

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RefreshActivitySummary.
        The current state of the refresh activity. Valid values are Scheduled, In progress , Failed, Completed.


        :return: The lifecycle_state of this RefreshActivitySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RefreshActivitySummary.
        The current state of the refresh activity. Valid values are Scheduled, In progress , Failed, Completed.


        :param lifecycle_state: The lifecycle_state of this RefreshActivitySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_scheduled_start(self):
        """
        **[Required]** Gets the time_scheduled_start of this RefreshActivitySummary.
        The time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.


        :return: The time_scheduled_start of this RefreshActivitySummary.
        :rtype: datetime
        """
        return self._time_scheduled_start

    @time_scheduled_start.setter
    def time_scheduled_start(self, time_scheduled_start):
        """
        Sets the time_scheduled_start of this RefreshActivitySummary.
        The time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.


        :param time_scheduled_start: The time_scheduled_start of this RefreshActivitySummary.
        :type: datetime
        """
        self._time_scheduled_start = time_scheduled_start

    @property
    def time_expected_finish(self):
        """
        **[Required]** Gets the time_expected_finish of this RefreshActivitySummary.
        The time the refresh activity is scheduled to end. An RFC3339 formatted datetime string.


        :return: The time_expected_finish of this RefreshActivitySummary.
        :rtype: datetime
        """
        return self._time_expected_finish

    @time_expected_finish.setter
    def time_expected_finish(self, time_expected_finish):
        """
        Sets the time_expected_finish of this RefreshActivitySummary.
        The time the refresh activity is scheduled to end. An RFC3339 formatted datetime string.


        :param time_expected_finish: The time_expected_finish of this RefreshActivitySummary.
        :type: datetime
        """
        self._time_expected_finish = time_expected_finish

    @property
    def time_finished(self):
        """
        Gets the time_finished of this RefreshActivitySummary.
        The time the refresh activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.


        :return: The time_finished of this RefreshActivitySummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this RefreshActivitySummary.
        The time the refresh activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.


        :param time_finished: The time_finished of this RefreshActivitySummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def service_availability(self):
        """
        **[Required]** Gets the service_availability of this RefreshActivitySummary.
        Service availability / impact during refresh activity execution, up down


        :return: The service_availability of this RefreshActivitySummary.
        :rtype: str
        """
        return self._service_availability

    @service_availability.setter
    def service_availability(self, service_availability):
        """
        Sets the service_availability of this RefreshActivitySummary.
        Service availability / impact during refresh activity execution, up down


        :param service_availability: The service_availability of this RefreshActivitySummary.
        :type: str
        """
        self._service_availability = service_availability

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this RefreshActivitySummary.
        The time the refresh activity record was created. An RFC3339 formatted datetime string.


        :return: The time_accepted of this RefreshActivitySummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this RefreshActivitySummary.
        The time the refresh activity record was created. An RFC3339 formatted datetime string.


        :param time_accepted: The time_accepted of this RefreshActivitySummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RefreshActivitySummary.
        The time the refresh activity record was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this RefreshActivitySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RefreshActivitySummary.
        The time the refresh activity record was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this RefreshActivitySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this RefreshActivitySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this RefreshActivitySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this RefreshActivitySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this RefreshActivitySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def refresh_issue_details_list(self):
        """
        Gets the refresh_issue_details_list of this RefreshActivitySummary.
        Details of refresh investigation information, each item represents a different issue.


        :return: The refresh_issue_details_list of this RefreshActivitySummary.
        :rtype: list[oci.fusion_apps.models.RefreshIssueDetails]
        """
        return self._refresh_issue_details_list

    @refresh_issue_details_list.setter
    def refresh_issue_details_list(self, refresh_issue_details_list):
        """
        Sets the refresh_issue_details_list of this RefreshActivitySummary.
        Details of refresh investigation information, each item represents a different issue.


        :param refresh_issue_details_list: The refresh_issue_details_list of this RefreshActivitySummary.
        :type: list[oci.fusion_apps.models.RefreshIssueDetails]
        """
        self._refresh_issue_details_list = refresh_issue_details_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
