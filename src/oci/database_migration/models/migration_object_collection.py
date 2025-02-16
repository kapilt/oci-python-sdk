# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationObjectCollection(object):
    """
    Database objects to migrate.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationObjectCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this MigrationObjectCollection.
        :type items: list[oci.database_migration.models.MigrationObjectSummary]

        :param csv_text:
            The value to assign to the csv_text property of this MigrationObjectCollection.
        :type csv_text: str

        """
        self.swagger_types = {
            'items': 'list[MigrationObjectSummary]',
            'csv_text': 'str'
        }

        self.attribute_map = {
            'items': 'items',
            'csv_text': 'csvText'
        }

        self._items = None
        self._csv_text = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this MigrationObjectCollection.
        Database objects to exclude/include from migration


        :return: The items of this MigrationObjectCollection.
        :rtype: list[oci.database_migration.models.MigrationObjectSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this MigrationObjectCollection.
        Database objects to exclude/include from migration


        :param items: The items of this MigrationObjectCollection.
        :type: list[oci.database_migration.models.MigrationObjectSummary]
        """
        self._items = items

    @property
    def csv_text(self):
        """
        Gets the csv_text of this MigrationObjectCollection.
        Database objects to exclude/include from migration in CSV format. The items field will be ignored if this field is not null.


        :return: The csv_text of this MigrationObjectCollection.
        :rtype: str
        """
        return self._csv_text

    @csv_text.setter
    def csv_text(self, csv_text):
        """
        Sets the csv_text of this MigrationObjectCollection.
        Database objects to exclude/include from migration in CSV format. The items field will be ignored if this field is not null.


        :param csv_text: The csv_text of this MigrationObjectCollection.
        :type: str
        """
        self._csv_text = csv_text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
