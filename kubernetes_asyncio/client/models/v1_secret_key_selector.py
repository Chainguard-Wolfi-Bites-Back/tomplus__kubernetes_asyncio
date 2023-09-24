# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.26.9
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1SecretKeySelector(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'key': 'str',
        'name': 'str',
        'optional': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'optional': 'optional'
    }

    def __init__(self, key=None, name=None, optional=None, local_vars_configuration=None):  # noqa: E501
        """V1SecretKeySelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._name = None
        self._optional = None
        self.discriminator = None

        self.key = key
        if name is not None:
            self.name = name
        if optional is not None:
            self.optional = optional

    @property
    def key(self):
        """Gets the key of this V1SecretKeySelector.  # noqa: E501

        The key of the secret to select from.  Must be a valid secret key.  # noqa: E501

        :return: The key of this V1SecretKeySelector.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1SecretKeySelector.

        The key of the secret to select from.  Must be a valid secret key.  # noqa: E501

        :param key: The key of this V1SecretKeySelector.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this V1SecretKeySelector.  # noqa: E501

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  # noqa: E501

        :return: The name of this V1SecretKeySelector.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1SecretKeySelector.

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  # noqa: E501

        :param name: The name of this V1SecretKeySelector.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def optional(self):
        """Gets the optional of this V1SecretKeySelector.  # noqa: E501

        Specify whether the Secret or its key must be defined  # noqa: E501

        :return: The optional of this V1SecretKeySelector.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this V1SecretKeySelector.

        Specify whether the Secret or its key must be defined  # noqa: E501

        :param optional: The optional of this V1SecretKeySelector.  # noqa: E501
        :type optional: bool
        """

        self._optional = optional

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1SecretKeySelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SecretKeySelector):
            return True

        return self.to_dict() != other.to_dict()
