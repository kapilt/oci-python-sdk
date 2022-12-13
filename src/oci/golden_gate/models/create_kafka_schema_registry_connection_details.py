# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateKafkaSchemaRegistryConnectionDetails(CreateConnectionDetails):
    """
    The information about a new Kafka (e.g. Confluent) Schema Registry Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateKafkaSchemaRegistryConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.CreateKafkaSchemaRegistryConnectionDetails.connection_type` attribute
        of this class is ``KAFKA_SCHEMA_REGISTRY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateKafkaSchemaRegistryConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type technology_type: str

        :param url:
            The value to assign to the url property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type url: str

        :param authentication_type:
            The value to assign to the authentication_type property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type authentication_type: str

        :param username:
            The value to assign to the username property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type password: str

        :param trust_store:
            The value to assign to the trust_store property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type trust_store: str

        :param trust_store_password:
            The value to assign to the trust_store_password property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type trust_store_password: str

        :param key_store:
            The value to assign to the key_store property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type key_store: str

        :param key_store_password:
            The value to assign to the key_store_password property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type key_store_password: str

        :param ssl_key_password:
            The value to assign to the ssl_key_password property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type ssl_key_password: str

        :param private_ip:
            The value to assign to the private_ip property of this CreateKafkaSchemaRegistryConnectionDetails.
        :type private_ip: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'url': 'str',
            'authentication_type': 'str',
            'username': 'str',
            'password': 'str',
            'trust_store': 'str',
            'trust_store_password': 'str',
            'key_store': 'str',
            'key_store_password': 'str',
            'ssl_key_password': 'str',
            'private_ip': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'url': 'url',
            'authentication_type': 'authenticationType',
            'username': 'username',
            'password': 'password',
            'trust_store': 'trustStore',
            'trust_store_password': 'trustStorePassword',
            'key_store': 'keyStore',
            'key_store_password': 'keyStorePassword',
            'ssl_key_password': 'sslKeyPassword',
            'private_ip': 'privateIp'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._nsg_ids = None
        self._technology_type = None
        self._url = None
        self._authentication_type = None
        self._username = None
        self._password = None
        self._trust_store = None
        self._trust_store_password = None
        self._key_store = None
        self._key_store_password = None
        self._ssl_key_password = None
        self._private_ip = None
        self._connection_type = 'KAFKA_SCHEMA_REGISTRY'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateKafkaSchemaRegistryConnectionDetails.
        The Kafka (e.g. Confluent) Schema Registry technology type.


        :return: The technology_type of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateKafkaSchemaRegistryConnectionDetails.
        The Kafka (e.g. Confluent) Schema Registry technology type.


        :param technology_type: The technology_type of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def url(self):
        """
        **[Required]** Gets the url of this CreateKafkaSchemaRegistryConnectionDetails.
        Kafka Schema Registry URL.
        e.g.: 'https://server1.us.oracle.com:8081'


        :return: The url of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CreateKafkaSchemaRegistryConnectionDetails.
        Kafka Schema Registry URL.
        e.g.: 'https://server1.us.oracle.com:8081'


        :param url: The url of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._url = url

    @property
    def authentication_type(self):
        """
        **[Required]** Gets the authentication_type of this CreateKafkaSchemaRegistryConnectionDetails.
        Used authentication mechanism to access Schema Registry.


        :return: The authentication_type of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this CreateKafkaSchemaRegistryConnectionDetails.
        Used authentication mechanism to access Schema Registry.


        :param authentication_type: The authentication_type of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._authentication_type = authentication_type

    @property
    def username(self):
        """
        Gets the username of this CreateKafkaSchemaRegistryConnectionDetails.
        The username to access Schema Registry using basic authentation.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.


        :return: The username of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateKafkaSchemaRegistryConnectionDetails.
        The username to access Schema Registry using basic authentation.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.


        :param username: The username of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this CreateKafkaSchemaRegistryConnectionDetails.
        The password to access Schema Registry using basic authentation.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.


        :return: The password of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateKafkaSchemaRegistryConnectionDetails.
        The password to access Schema Registry using basic authentation.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.


        :param password: The password of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._password = password

    @property
    def trust_store(self):
        """
        Gets the trust_store of this CreateKafkaSchemaRegistryConnectionDetails.
        The base64 encoded content of the TrustStore file.


        :return: The trust_store of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._trust_store

    @trust_store.setter
    def trust_store(self, trust_store):
        """
        Sets the trust_store of this CreateKafkaSchemaRegistryConnectionDetails.
        The base64 encoded content of the TrustStore file.


        :param trust_store: The trust_store of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._trust_store = trust_store

    @property
    def trust_store_password(self):
        """
        Gets the trust_store_password of this CreateKafkaSchemaRegistryConnectionDetails.
        The TrustStore password.


        :return: The trust_store_password of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._trust_store_password

    @trust_store_password.setter
    def trust_store_password(self, trust_store_password):
        """
        Sets the trust_store_password of this CreateKafkaSchemaRegistryConnectionDetails.
        The TrustStore password.


        :param trust_store_password: The trust_store_password of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._trust_store_password = trust_store_password

    @property
    def key_store(self):
        """
        Gets the key_store of this CreateKafkaSchemaRegistryConnectionDetails.
        The base64 encoded content of the KeyStore file.


        :return: The key_store of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._key_store

    @key_store.setter
    def key_store(self, key_store):
        """
        Sets the key_store of this CreateKafkaSchemaRegistryConnectionDetails.
        The base64 encoded content of the KeyStore file.


        :param key_store: The key_store of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._key_store = key_store

    @property
    def key_store_password(self):
        """
        Gets the key_store_password of this CreateKafkaSchemaRegistryConnectionDetails.
        The KeyStore password.


        :return: The key_store_password of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """
        Sets the key_store_password of this CreateKafkaSchemaRegistryConnectionDetails.
        The KeyStore password.


        :param key_store_password: The key_store_password of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._key_store_password = key_store_password

    @property
    def ssl_key_password(self):
        """
        Gets the ssl_key_password of this CreateKafkaSchemaRegistryConnectionDetails.
        The password for the cert inside the KeyStore.
        In case it differs from the KeyStore password, it should be provided.


        :return: The ssl_key_password of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._ssl_key_password

    @ssl_key_password.setter
    def ssl_key_password(self, ssl_key_password):
        """
        Sets the ssl_key_password of this CreateKafkaSchemaRegistryConnectionDetails.
        The password for the cert inside the KeyStore.
        In case it differs from the KeyStore password, it should be provided.


        :param ssl_key_password: The ssl_key_password of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._ssl_key_password = ssl_key_password

    @property
    def private_ip(self):
        """
        Gets the private_ip of this CreateKafkaSchemaRegistryConnectionDetails.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this CreateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this CreateKafkaSchemaRegistryConnectionDetails.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this CreateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
