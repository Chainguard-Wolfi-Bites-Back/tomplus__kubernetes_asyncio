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


class V1alpha1ResourceClass(object):
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
        'api_version': 'str',
        'driver_name': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'parameters_ref': 'V1alpha1ResourceClassParametersReference',
        'suitable_nodes': 'V1NodeSelector'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'driver_name': 'driverName',
        'kind': 'kind',
        'metadata': 'metadata',
        'parameters_ref': 'parametersRef',
        'suitable_nodes': 'suitableNodes'
    }

    def __init__(self, api_version=None, driver_name=None, kind=None, metadata=None, parameters_ref=None, suitable_nodes=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ResourceClass - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._driver_name = None
        self._kind = None
        self._metadata = None
        self._parameters_ref = None
        self._suitable_nodes = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        self.driver_name = driver_name
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if parameters_ref is not None:
            self.parameters_ref = parameters_ref
        if suitable_nodes is not None:
            self.suitable_nodes = suitable_nodes

    @property
    def api_version(self):
        """Gets the api_version of this V1alpha1ResourceClass.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1alpha1ResourceClass.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1alpha1ResourceClass.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1alpha1ResourceClass.  # noqa: E501
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def driver_name(self):
        """Gets the driver_name of this V1alpha1ResourceClass.  # noqa: E501

        DriverName defines the name of the dynamic resource driver that is used for allocation of a ResourceClaim that uses this class.  Resource drivers have a unique name in forward domain order (acme.example.com).  # noqa: E501

        :return: The driver_name of this V1alpha1ResourceClass.  # noqa: E501
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """Sets the driver_name of this V1alpha1ResourceClass.

        DriverName defines the name of the dynamic resource driver that is used for allocation of a ResourceClaim that uses this class.  Resource drivers have a unique name in forward domain order (acme.example.com).  # noqa: E501

        :param driver_name: The driver_name of this V1alpha1ResourceClass.  # noqa: E501
        :type driver_name: str
        """
        if self.local_vars_configuration.client_side_validation and driver_name is None:  # noqa: E501
            raise ValueError("Invalid value for `driver_name`, must not be `None`")  # noqa: E501

        self._driver_name = driver_name

    @property
    def kind(self):
        """Gets the kind of this V1alpha1ResourceClass.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1alpha1ResourceClass.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1alpha1ResourceClass.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1alpha1ResourceClass.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1ResourceClass.  # noqa: E501


        :return: The metadata of this V1alpha1ResourceClass.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1ResourceClass.


        :param metadata: The metadata of this V1alpha1ResourceClass.  # noqa: E501
        :type metadata: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def parameters_ref(self):
        """Gets the parameters_ref of this V1alpha1ResourceClass.  # noqa: E501


        :return: The parameters_ref of this V1alpha1ResourceClass.  # noqa: E501
        :rtype: V1alpha1ResourceClassParametersReference
        """
        return self._parameters_ref

    @parameters_ref.setter
    def parameters_ref(self, parameters_ref):
        """Sets the parameters_ref of this V1alpha1ResourceClass.


        :param parameters_ref: The parameters_ref of this V1alpha1ResourceClass.  # noqa: E501
        :type parameters_ref: V1alpha1ResourceClassParametersReference
        """

        self._parameters_ref = parameters_ref

    @property
    def suitable_nodes(self):
        """Gets the suitable_nodes of this V1alpha1ResourceClass.  # noqa: E501


        :return: The suitable_nodes of this V1alpha1ResourceClass.  # noqa: E501
        :rtype: V1NodeSelector
        """
        return self._suitable_nodes

    @suitable_nodes.setter
    def suitable_nodes(self, suitable_nodes):
        """Sets the suitable_nodes of this V1alpha1ResourceClass.


        :param suitable_nodes: The suitable_nodes of this V1alpha1ResourceClass.  # noqa: E501
        :type suitable_nodes: V1NodeSelector
        """

        self._suitable_nodes = suitable_nodes

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
        if not isinstance(other, V1alpha1ResourceClass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ResourceClass):
            return True

        return self.to_dict() != other.to_dict()
