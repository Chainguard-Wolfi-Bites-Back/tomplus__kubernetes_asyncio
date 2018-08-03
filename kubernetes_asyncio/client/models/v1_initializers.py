# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.11.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class V1Initializers(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pending': 'list[V1Initializer]',
        'result': 'V1Status'
    }

    attribute_map = {
        'pending': 'pending',
        'result': 'result'
    }

    def __init__(self, pending=None, result=None):  # noqa: E501
        """V1Initializers - a model defined in Swagger"""  # noqa: E501

        self._pending = None
        self._result = None
        self.discriminator = None

        self.pending = pending
        if result is not None:
            self.result = result

    @property
    def pending(self):
        """Gets the pending of this V1Initializers.  # noqa: E501

        Pending is a list of initializers that must execute in order before this object is visible. When the last pending initializer is removed, and no failing result is set, the initializers struct will be set to nil and the object is considered as initialized and visible to all clients.  # noqa: E501

        :return: The pending of this V1Initializers.  # noqa: E501
        :rtype: list[V1Initializer]
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this V1Initializers.

        Pending is a list of initializers that must execute in order before this object is visible. When the last pending initializer is removed, and no failing result is set, the initializers struct will be set to nil and the object is considered as initialized and visible to all clients.  # noqa: E501

        :param pending: The pending of this V1Initializers.  # noqa: E501
        :type: list[V1Initializer]
        """
        if pending is None:
            raise ValueError("Invalid value for `pending`, must not be `None`")  # noqa: E501

        self._pending = pending

    @property
    def result(self):
        """Gets the result of this V1Initializers.  # noqa: E501

        If result is set with the Failure field, the object will be persisted to storage and then deleted, ensuring that other clients can observe the deletion.  # noqa: E501

        :return: The result of this V1Initializers.  # noqa: E501
        :rtype: V1Status
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this V1Initializers.

        If result is set with the Failure field, the object will be persisted to storage and then deleted, ensuring that other clients can observe the deletion.  # noqa: E501

        :param result: The result of this V1Initializers.  # noqa: E501
        :type: V1Status
        """

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1Initializers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
