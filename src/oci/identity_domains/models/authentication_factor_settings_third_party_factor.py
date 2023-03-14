# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationFactorSettingsThirdPartyFactor(object):
    """
    Settings related to third-party factor

    **Added In:** 19.2.1

    **SCIM++ Properties:**
    - idcsSearchable: false
    - multiValued: false
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationFactorSettingsThirdPartyFactor object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param duo_security:
            The value to assign to the duo_security property of this AuthenticationFactorSettingsThirdPartyFactor.
        :type duo_security: bool

        """
        self.swagger_types = {
            'duo_security': 'bool'
        }

        self.attribute_map = {
            'duo_security': 'duoSecurity'
        }

        self._duo_security = None

    @property
    def duo_security(self):
        """
        **[Required]** Gets the duo_security of this AuthenticationFactorSettingsThirdPartyFactor.
        To enable Duo Security factor

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The duo_security of this AuthenticationFactorSettingsThirdPartyFactor.
        :rtype: bool
        """
        return self._duo_security

    @duo_security.setter
    def duo_security(self, duo_security):
        """
        Sets the duo_security of this AuthenticationFactorSettingsThirdPartyFactor.
        To enable Duo Security factor

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param duo_security: The duo_security of this AuthenticationFactorSettingsThirdPartyFactor.
        :type: bool
        """
        self._duo_security = duo_security

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
