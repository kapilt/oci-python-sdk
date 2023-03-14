# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtApplicablePasswordPolicy(object):
    """
    Applicable Password Policy

    **Added In:** 20.1.3

    **SCIM++ Properties:**
    - caseExact: false
    - idcsCompositeKey: [value]
    - idcsSearchable: true
    - multiValued: false
    - mutability: readOnly
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtApplicablePasswordPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserExtApplicablePasswordPolicy.
        :type value: str

        :param ref:
            The value to assign to the ref property of this UserExtApplicablePasswordPolicy.
        :type ref: str

        :param display:
            The value to assign to the display property of this UserExtApplicablePasswordPolicy.
        :type display: str

        :param priority:
            The value to assign to the priority property of this UserExtApplicablePasswordPolicy.
        :type priority: int

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'priority': 'int'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'priority': 'priority'
        }

        self._value = None
        self._ref = None
        self._display = None
        self._priority = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UserExtApplicablePasswordPolicy.
        The identifier of the password policy.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this UserExtApplicablePasswordPolicy.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtApplicablePasswordPolicy.
        The identifier of the password policy.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this UserExtApplicablePasswordPolicy.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this UserExtApplicablePasswordPolicy.
        The URI of the corresponding PasswordPolicy resource.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this UserExtApplicablePasswordPolicy.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this UserExtApplicablePasswordPolicy.
        The URI of the corresponding PasswordPolicy resource.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this UserExtApplicablePasswordPolicy.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this UserExtApplicablePasswordPolicy.
        Password Policy Display Name

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this UserExtApplicablePasswordPolicy.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this UserExtApplicablePasswordPolicy.
        Password Policy Display Name

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this UserExtApplicablePasswordPolicy.
        :type: str
        """
        self._display = display

    @property
    def priority(self):
        """
        Gets the priority of this UserExtApplicablePasswordPolicy.
        PasswordPolicy priority

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The priority of this UserExtApplicablePasswordPolicy.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this UserExtApplicablePasswordPolicy.
        PasswordPolicy priority

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :param priority: The priority of this UserExtApplicablePasswordPolicy.
        :type: int
        """
        self._priority = priority

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
