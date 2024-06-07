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


class V1ISCSIVolumeSource(object):
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
        'chap_auth_discovery': 'bool',
        'chap_auth_session': 'bool',
        'fs_type': 'str',
        'initiator_name': 'str',
        'iqn': 'str',
        'iscsi_interface': 'str',
        'lun': 'int',
        'portals': 'list[str]',
        'read_only': 'bool',
        'secret_ref': 'V1LocalObjectReference',
        'target_portal': 'str'
    }

    attribute_map = {
        'chap_auth_discovery': 'chapAuthDiscovery',
        'chap_auth_session': 'chapAuthSession',
        'fs_type': 'fsType',
        'initiator_name': 'initiatorName',
        'iqn': 'iqn',
        'iscsi_interface': 'iscsiInterface',
        'lun': 'lun',
        'portals': 'portals',
        'read_only': 'readOnly',
        'secret_ref': 'secretRef',
        'target_portal': 'targetPortal'
    }

    def __init__(self, chap_auth_discovery=None, chap_auth_session=None, fs_type=None, initiator_name=None, iqn=None, iscsi_interface=None, lun=None, portals=None, read_only=None, secret_ref=None, target_portal=None, local_vars_configuration=None):  # noqa: E501
        """V1ISCSIVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._chap_auth_discovery = None
        self._chap_auth_session = None
        self._fs_type = None
        self._initiator_name = None
        self._iqn = None
        self._iscsi_interface = None
        self._lun = None
        self._portals = None
        self._read_only = None
        self._secret_ref = None
        self._target_portal = None
        self.discriminator = None

        if chap_auth_discovery is not None:
            self.chap_auth_discovery = chap_auth_discovery
        if chap_auth_session is not None:
            self.chap_auth_session = chap_auth_session
        if fs_type is not None:
            self.fs_type = fs_type
        if initiator_name is not None:
            self.initiator_name = initiator_name
        self.iqn = iqn
        if iscsi_interface is not None:
            self.iscsi_interface = iscsi_interface
        self.lun = lun
        if portals is not None:
            self.portals = portals
        if read_only is not None:
            self.read_only = read_only
        if secret_ref is not None:
            self.secret_ref = secret_ref
        self.target_portal = target_portal

    @property
    def chap_auth_discovery(self):
        """Gets the chap_auth_discovery of this V1ISCSIVolumeSource.  # noqa: E501

        chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication  # noqa: E501

        :return: The chap_auth_discovery of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._chap_auth_discovery

    @chap_auth_discovery.setter
    def chap_auth_discovery(self, chap_auth_discovery):
        """Sets the chap_auth_discovery of this V1ISCSIVolumeSource.

        chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication  # noqa: E501

        :param chap_auth_discovery: The chap_auth_discovery of this V1ISCSIVolumeSource.  # noqa: E501
        :type chap_auth_discovery: bool
        """

        self._chap_auth_discovery = chap_auth_discovery

    @property
    def chap_auth_session(self):
        """Gets the chap_auth_session of this V1ISCSIVolumeSource.  # noqa: E501

        chapAuthSession defines whether support iSCSI Session CHAP authentication  # noqa: E501

        :return: The chap_auth_session of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._chap_auth_session

    @chap_auth_session.setter
    def chap_auth_session(self, chap_auth_session):
        """Sets the chap_auth_session of this V1ISCSIVolumeSource.

        chapAuthSession defines whether support iSCSI Session CHAP authentication  # noqa: E501

        :param chap_auth_session: The chap_auth_session of this V1ISCSIVolumeSource.  # noqa: E501
        :type chap_auth_session: bool
        """

        self._chap_auth_session = chap_auth_session

    @property
    def fs_type(self):
        """Gets the fs_type of this V1ISCSIVolumeSource.  # noqa: E501

        fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi  # noqa: E501

        :return: The fs_type of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this V1ISCSIVolumeSource.

        fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi  # noqa: E501

        :param fs_type: The fs_type of this V1ISCSIVolumeSource.  # noqa: E501
        :type fs_type: str
        """

        self._fs_type = fs_type

    @property
    def initiator_name(self):
        """Gets the initiator_name of this V1ISCSIVolumeSource.  # noqa: E501

        initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.  # noqa: E501

        :return: The initiator_name of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._initiator_name

    @initiator_name.setter
    def initiator_name(self, initiator_name):
        """Sets the initiator_name of this V1ISCSIVolumeSource.

        initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.  # noqa: E501

        :param initiator_name: The initiator_name of this V1ISCSIVolumeSource.  # noqa: E501
        :type initiator_name: str
        """

        self._initiator_name = initiator_name

    @property
    def iqn(self):
        """Gets the iqn of this V1ISCSIVolumeSource.  # noqa: E501

        iqn is the target iSCSI Qualified Name.  # noqa: E501

        :return: The iqn of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """Sets the iqn of this V1ISCSIVolumeSource.

        iqn is the target iSCSI Qualified Name.  # noqa: E501

        :param iqn: The iqn of this V1ISCSIVolumeSource.  # noqa: E501
        :type iqn: str
        """
        if self.local_vars_configuration.client_side_validation and iqn is None:  # noqa: E501
            raise ValueError("Invalid value for `iqn`, must not be `None`")  # noqa: E501

        self._iqn = iqn

    @property
    def iscsi_interface(self):
        """Gets the iscsi_interface of this V1ISCSIVolumeSource.  # noqa: E501

        iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).  # noqa: E501

        :return: The iscsi_interface of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._iscsi_interface

    @iscsi_interface.setter
    def iscsi_interface(self, iscsi_interface):
        """Sets the iscsi_interface of this V1ISCSIVolumeSource.

        iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).  # noqa: E501

        :param iscsi_interface: The iscsi_interface of this V1ISCSIVolumeSource.  # noqa: E501
        :type iscsi_interface: str
        """

        self._iscsi_interface = iscsi_interface

    @property
    def lun(self):
        """Gets the lun of this V1ISCSIVolumeSource.  # noqa: E501

        lun represents iSCSI Target Lun number.  # noqa: E501

        :return: The lun of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: int
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """Sets the lun of this V1ISCSIVolumeSource.

        lun represents iSCSI Target Lun number.  # noqa: E501

        :param lun: The lun of this V1ISCSIVolumeSource.  # noqa: E501
        :type lun: int
        """
        if self.local_vars_configuration.client_side_validation and lun is None:  # noqa: E501
            raise ValueError("Invalid value for `lun`, must not be `None`")  # noqa: E501

        self._lun = lun

    @property
    def portals(self):
        """Gets the portals of this V1ISCSIVolumeSource.  # noqa: E501

        portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).  # noqa: E501

        :return: The portals of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._portals

    @portals.setter
    def portals(self, portals):
        """Sets the portals of this V1ISCSIVolumeSource.

        portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).  # noqa: E501

        :param portals: The portals of this V1ISCSIVolumeSource.  # noqa: E501
        :type portals: list[str]
        """

        self._portals = portals

    @property
    def read_only(self):
        """Gets the read_only of this V1ISCSIVolumeSource.  # noqa: E501

        readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.  # noqa: E501

        :return: The read_only of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1ISCSIVolumeSource.

        readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.  # noqa: E501

        :param read_only: The read_only of this V1ISCSIVolumeSource.  # noqa: E501
        :type read_only: bool
        """

        self._read_only = read_only

    @property
    def secret_ref(self):
        """Gets the secret_ref of this V1ISCSIVolumeSource.  # noqa: E501


        :return: The secret_ref of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: V1LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this V1ISCSIVolumeSource.


        :param secret_ref: The secret_ref of this V1ISCSIVolumeSource.  # noqa: E501
        :type secret_ref: V1LocalObjectReference
        """

        self._secret_ref = secret_ref

    @property
    def target_portal(self):
        """Gets the target_portal of this V1ISCSIVolumeSource.  # noqa: E501

        targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).  # noqa: E501

        :return: The target_portal of this V1ISCSIVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._target_portal

    @target_portal.setter
    def target_portal(self, target_portal):
        """Sets the target_portal of this V1ISCSIVolumeSource.

        targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).  # noqa: E501

        :param target_portal: The target_portal of this V1ISCSIVolumeSource.  # noqa: E501
        :type target_portal: str
        """
        if self.local_vars_configuration.client_side_validation and target_portal is None:  # noqa: E501
            raise ValueError("Invalid value for `target_portal`, must not be `None`")  # noqa: E501

        self._target_portal = target_portal

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
        if not isinstance(other, V1ISCSIVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ISCSIVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
