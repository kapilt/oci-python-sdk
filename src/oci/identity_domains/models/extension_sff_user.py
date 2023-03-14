# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionSffUser(object):
    """
    SFF Auth Keys User extension
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionSffUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sff_auth_keys:
            The value to assign to the sff_auth_keys property of this ExtensionSffUser.
        :type sff_auth_keys: str

        """
        self.swagger_types = {
            'sff_auth_keys': 'str'
        }

        self.attribute_map = {
            'sff_auth_keys': 'sffAuthKeys'
        }

        self._sff_auth_keys = None

    @property
    def sff_auth_keys(self):
        """
        Gets the sff_auth_keys of this ExtensionSffUser.
        SFF auth keys clob

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The sff_auth_keys of this ExtensionSffUser.
        :rtype: str
        """
        return self._sff_auth_keys

    @sff_auth_keys.setter
    def sff_auth_keys(self, sff_auth_keys):
        """
        Sets the sff_auth_keys of this ExtensionSffUser.
        SFF auth keys clob

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param sff_auth_keys: The sff_auth_keys of this ExtensionSffUser.
        :type: str
        """
        self._sff_auth_keys = sff_auth_keys

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
