# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionSecurityQuestionsUser(object):
    """
    This extension defines attributes used to store Security Questions of User.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionSecurityQuestionsUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sec_questions:
            The value to assign to the sec_questions property of this ExtensionSecurityQuestionsUser.
        :type sec_questions: list[oci.identity_domains.models.UserExtSecQuestions]

        """
        self.swagger_types = {
            'sec_questions': 'list[UserExtSecQuestions]'
        }

        self.attribute_map = {
            'sec_questions': 'secQuestions'
        }

        self._sec_questions = None

    @property
    def sec_questions(self):
        """
        Gets the sec_questions of this ExtensionSecurityQuestionsUser.
        Security question and answers provided by end-user for Account recovery and/or MFA. While setting up security questions, end-user can also provide hint along with answer.

        **SCIM++ Properties:**
         - idcsCompositeKey: [value]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The sec_questions of this ExtensionSecurityQuestionsUser.
        :rtype: list[oci.identity_domains.models.UserExtSecQuestions]
        """
        return self._sec_questions

    @sec_questions.setter
    def sec_questions(self, sec_questions):
        """
        Sets the sec_questions of this ExtensionSecurityQuestionsUser.
        Security question and answers provided by end-user for Account recovery and/or MFA. While setting up security questions, end-user can also provide hint along with answer.

        **SCIM++ Properties:**
         - idcsCompositeKey: [value]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param sec_questions: The sec_questions of this ExtensionSecurityQuestionsUser.
        :type: list[oci.identity_domains.models.UserExtSecQuestions]
        """
        self._sec_questions = sec_questions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
