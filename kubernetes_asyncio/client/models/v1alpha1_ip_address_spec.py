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


class V1alpha1IPAddressSpec(object):
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
        'parent_ref': 'V1alpha1ParentReference'
    }

    attribute_map = {
        'parent_ref': 'parentRef'
    }

    def __init__(self, parent_ref=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1IPAddressSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._parent_ref = None
        self.discriminator = None

        self.parent_ref = parent_ref

    @property
    def parent_ref(self):
        """Gets the parent_ref of this V1alpha1IPAddressSpec.  # noqa: E501


        :return: The parent_ref of this V1alpha1IPAddressSpec.  # noqa: E501
        :rtype: V1alpha1ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """Sets the parent_ref of this V1alpha1IPAddressSpec.


        :param parent_ref: The parent_ref of this V1alpha1IPAddressSpec.  # noqa: E501
        :type parent_ref: V1alpha1ParentReference
        """
        if self.local_vars_configuration.client_side_validation and parent_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_ref`, must not be `None`")  # noqa: E501

        self._parent_ref = parent_ref

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
        if not isinstance(other, V1alpha1IPAddressSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1IPAddressSpec):
            return True

        return self.to_dict() != other.to_dict()
