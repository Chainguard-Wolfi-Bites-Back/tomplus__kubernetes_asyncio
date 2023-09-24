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


class V1NodeSelectorTerm(object):
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
        'match_expressions': 'list[V1NodeSelectorRequirement]',
        'match_fields': 'list[V1NodeSelectorRequirement]'
    }

    attribute_map = {
        'match_expressions': 'matchExpressions',
        'match_fields': 'matchFields'
    }

    def __init__(self, match_expressions=None, match_fields=None, local_vars_configuration=None):  # noqa: E501
        """V1NodeSelectorTerm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._match_expressions = None
        self._match_fields = None
        self.discriminator = None

        if match_expressions is not None:
            self.match_expressions = match_expressions
        if match_fields is not None:
            self.match_fields = match_fields

    @property
    def match_expressions(self):
        """Gets the match_expressions of this V1NodeSelectorTerm.  # noqa: E501

        A list of node selector requirements by node's labels.  # noqa: E501

        :return: The match_expressions of this V1NodeSelectorTerm.  # noqa: E501
        :rtype: list[V1NodeSelectorRequirement]
        """
        return self._match_expressions

    @match_expressions.setter
    def match_expressions(self, match_expressions):
        """Sets the match_expressions of this V1NodeSelectorTerm.

        A list of node selector requirements by node's labels.  # noqa: E501

        :param match_expressions: The match_expressions of this V1NodeSelectorTerm.  # noqa: E501
        :type match_expressions: list[V1NodeSelectorRequirement]
        """

        self._match_expressions = match_expressions

    @property
    def match_fields(self):
        """Gets the match_fields of this V1NodeSelectorTerm.  # noqa: E501

        A list of node selector requirements by node's fields.  # noqa: E501

        :return: The match_fields of this V1NodeSelectorTerm.  # noqa: E501
        :rtype: list[V1NodeSelectorRequirement]
        """
        return self._match_fields

    @match_fields.setter
    def match_fields(self, match_fields):
        """Sets the match_fields of this V1NodeSelectorTerm.

        A list of node selector requirements by node's fields.  # noqa: E501

        :param match_fields: The match_fields of this V1NodeSelectorTerm.  # noqa: E501
        :type match_fields: list[V1NodeSelectorRequirement]
        """

        self._match_fields = match_fields

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
        if not isinstance(other, V1NodeSelectorTerm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1NodeSelectorTerm):
            return True

        return self.to_dict() != other.to_dict()
