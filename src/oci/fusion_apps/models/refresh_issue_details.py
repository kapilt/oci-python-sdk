# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RefreshIssueDetails(object):
    """
    Details of refresh failure or validation failure that needs to be investigated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RefreshIssueDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param refresh_issues:
            The value to assign to the refresh_issues property of this RefreshIssueDetails.
        :type refresh_issues: str

        """
        self.swagger_types = {
            'refresh_issues': 'str'
        }

        self.attribute_map = {
            'refresh_issues': 'refreshIssues'
        }

        self._refresh_issues = None

    @property
    def refresh_issues(self):
        """
        Gets the refresh_issues of this RefreshIssueDetails.
        Detail reasons of refresh failure or validation failure that needs to be shown to customer.


        :return: The refresh_issues of this RefreshIssueDetails.
        :rtype: str
        """
        return self._refresh_issues

    @refresh_issues.setter
    def refresh_issues(self, refresh_issues):
        """
        Sets the refresh_issues of this RefreshIssueDetails.
        Detail reasons of refresh failure or validation failure that needs to be shown to customer.


        :param refresh_issues: The refresh_issues of this RefreshIssueDetails.
        :type: str
        """
        self._refresh_issues = refresh_issues

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
