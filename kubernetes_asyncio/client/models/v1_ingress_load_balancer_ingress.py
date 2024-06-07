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


class V1IngressLoadBalancerIngress(object):
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
        'hostname': 'str',
        'ip': 'str',
        'ports': 'list[V1IngressPortStatus]'
    }

    attribute_map = {
        'hostname': 'hostname',
        'ip': 'ip',
        'ports': 'ports'
    }

    def __init__(self, hostname=None, ip=None, ports=None, local_vars_configuration=None):  # noqa: E501
        """V1IngressLoadBalancerIngress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._hostname = None
        self._ip = None
        self._ports = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if ip is not None:
            self.ip = ip
        if ports is not None:
            self.ports = ports

    @property
    def hostname(self):
        """Gets the hostname of this V1IngressLoadBalancerIngress.  # noqa: E501

        hostname is set for load-balancer ingress points that are DNS based.  # noqa: E501

        :return: The hostname of this V1IngressLoadBalancerIngress.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this V1IngressLoadBalancerIngress.

        hostname is set for load-balancer ingress points that are DNS based.  # noqa: E501

        :param hostname: The hostname of this V1IngressLoadBalancerIngress.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def ip(self):
        """Gets the ip of this V1IngressLoadBalancerIngress.  # noqa: E501

        ip is set for load-balancer ingress points that are IP based.  # noqa: E501

        :return: The ip of this V1IngressLoadBalancerIngress.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this V1IngressLoadBalancerIngress.

        ip is set for load-balancer ingress points that are IP based.  # noqa: E501

        :param ip: The ip of this V1IngressLoadBalancerIngress.  # noqa: E501
        :type ip: str
        """

        self._ip = ip

    @property
    def ports(self):
        """Gets the ports of this V1IngressLoadBalancerIngress.  # noqa: E501

        ports provides information about the ports exposed by this LoadBalancer.  # noqa: E501

        :return: The ports of this V1IngressLoadBalancerIngress.  # noqa: E501
        :rtype: list[V1IngressPortStatus]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this V1IngressLoadBalancerIngress.

        ports provides information about the ports exposed by this LoadBalancer.  # noqa: E501

        :param ports: The ports of this V1IngressLoadBalancerIngress.  # noqa: E501
        :type ports: list[V1IngressPortStatus]
        """

        self._ports = ports

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
        if not isinstance(other, V1IngressLoadBalancerIngress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1IngressLoadBalancerIngress):
            return True

        return self.to_dict() != other.to_dict()
