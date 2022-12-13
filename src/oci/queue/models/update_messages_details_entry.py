# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMessagesDetailsEntry(object):
    """
    Object that represents a message to update in a queue.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMessagesDetailsEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param receipt:
            The value to assign to the receipt property of this UpdateMessagesDetailsEntry.
        :type receipt: str

        :param visibility_in_seconds:
            The value to assign to the visibility_in_seconds property of this UpdateMessagesDetailsEntry.
        :type visibility_in_seconds: int

        """
        self.swagger_types = {
            'receipt': 'str',
            'visibility_in_seconds': 'int'
        }

        self.attribute_map = {
            'receipt': 'receipt',
            'visibility_in_seconds': 'visibilityInSeconds'
        }

        self._receipt = None
        self._visibility_in_seconds = None

    @property
    def receipt(self):
        """
        **[Required]** Gets the receipt of this UpdateMessagesDetailsEntry.
        The receipt of the message to update


        :return: The receipt of this UpdateMessagesDetailsEntry.
        :rtype: str
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt):
        """
        Sets the receipt of this UpdateMessagesDetailsEntry.
        The receipt of the message to update


        :param receipt: The receipt of this UpdateMessagesDetailsEntry.
        :type: str
        """
        self._receipt = receipt

    @property
    def visibility_in_seconds(self):
        """
        **[Required]** Gets the visibility_in_seconds of this UpdateMessagesDetailsEntry.
        The new visibility of the message relative to the current time (as-per the clock of the server receiving the request).


        :return: The visibility_in_seconds of this UpdateMessagesDetailsEntry.
        :rtype: int
        """
        return self._visibility_in_seconds

    @visibility_in_seconds.setter
    def visibility_in_seconds(self, visibility_in_seconds):
        """
        Sets the visibility_in_seconds of this UpdateMessagesDetailsEntry.
        The new visibility of the message relative to the current time (as-per the clock of the server receiving the request).


        :param visibility_in_seconds: The visibility_in_seconds of this UpdateMessagesDetailsEntry.
        :type: int
        """
        self._visibility_in_seconds = visibility_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
