# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.30.1
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


class V1alpha2ResourceClaimSchedulingStatus(object):
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
        'name': 'str',
        'unsuitable_nodes': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'unsuitable_nodes': 'unsuitableNodes'
    }

    def __init__(self, name=None, unsuitable_nodes=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2ResourceClaimSchedulingStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._unsuitable_nodes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if unsuitable_nodes is not None:
            self.unsuitable_nodes = unsuitable_nodes

    @property
    def name(self):
        """Gets the name of this V1alpha2ResourceClaimSchedulingStatus.  # noqa: E501

        Name matches the pod.spec.resourceClaims[*].Name field.  # noqa: E501

        :return: The name of this V1alpha2ResourceClaimSchedulingStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha2ResourceClaimSchedulingStatus.

        Name matches the pod.spec.resourceClaims[*].Name field.  # noqa: E501

        :param name: The name of this V1alpha2ResourceClaimSchedulingStatus.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def unsuitable_nodes(self):
        """Gets the unsuitable_nodes of this V1alpha2ResourceClaimSchedulingStatus.  # noqa: E501

        UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced.  # noqa: E501

        :return: The unsuitable_nodes of this V1alpha2ResourceClaimSchedulingStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._unsuitable_nodes

    @unsuitable_nodes.setter
    def unsuitable_nodes(self, unsuitable_nodes):
        """Sets the unsuitable_nodes of this V1alpha2ResourceClaimSchedulingStatus.

        UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced.  # noqa: E501

        :param unsuitable_nodes: The unsuitable_nodes of this V1alpha2ResourceClaimSchedulingStatus.  # noqa: E501
        :type unsuitable_nodes: list[str]
        """

        self._unsuitable_nodes = unsuitable_nodes

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
        if not isinstance(other, V1alpha2ResourceClaimSchedulingStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2ResourceClaimSchedulingStatus):
            return True

        return self.to_dict() != other.to_dict()
