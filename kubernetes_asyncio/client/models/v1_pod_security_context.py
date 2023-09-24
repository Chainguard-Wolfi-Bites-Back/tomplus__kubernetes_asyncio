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


class V1PodSecurityContext(object):
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
        'fs_group': 'int',
        'fs_group_change_policy': 'str',
        'run_as_group': 'int',
        'run_as_non_root': 'bool',
        'run_as_user': 'int',
        'se_linux_options': 'V1SELinuxOptions',
        'seccomp_profile': 'V1SeccompProfile',
        'supplemental_groups': 'list[int]',
        'sysctls': 'list[V1Sysctl]',
        'windows_options': 'V1WindowsSecurityContextOptions'
    }

    attribute_map = {
        'fs_group': 'fsGroup',
        'fs_group_change_policy': 'fsGroupChangePolicy',
        'run_as_group': 'runAsGroup',
        'run_as_non_root': 'runAsNonRoot',
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
        'seccomp_profile': 'seccompProfile',
        'supplemental_groups': 'supplementalGroups',
        'sysctls': 'sysctls',
        'windows_options': 'windowsOptions'
    }

    def __init__(self, fs_group=None, fs_group_change_policy=None, run_as_group=None, run_as_non_root=None, run_as_user=None, se_linux_options=None, seccomp_profile=None, supplemental_groups=None, sysctls=None, windows_options=None, local_vars_configuration=None):  # noqa: E501
        """V1PodSecurityContext - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._fs_group = None
        self._fs_group_change_policy = None
        self._run_as_group = None
        self._run_as_non_root = None
        self._run_as_user = None
        self._se_linux_options = None
        self._seccomp_profile = None
        self._supplemental_groups = None
        self._sysctls = None
        self._windows_options = None
        self.discriminator = None

        if fs_group is not None:
            self.fs_group = fs_group
        if fs_group_change_policy is not None:
            self.fs_group_change_policy = fs_group_change_policy
        if run_as_group is not None:
            self.run_as_group = run_as_group
        if run_as_non_root is not None:
            self.run_as_non_root = run_as_non_root
        if run_as_user is not None:
            self.run_as_user = run_as_user
        if se_linux_options is not None:
            self.se_linux_options = se_linux_options
        if seccomp_profile is not None:
            self.seccomp_profile = seccomp_profile
        if supplemental_groups is not None:
            self.supplemental_groups = supplemental_groups
        if sysctls is not None:
            self.sysctls = sysctls
        if windows_options is not None:
            self.windows_options = windows_options

    @property
    def fs_group(self):
        """Gets the fs_group of this V1PodSecurityContext.  # noqa: E501

        A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:  1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----  If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :return: The fs_group of this V1PodSecurityContext.  # noqa: E501
        :rtype: int
        """
        return self._fs_group

    @fs_group.setter
    def fs_group(self, fs_group):
        """Sets the fs_group of this V1PodSecurityContext.

        A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:  1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----  If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :param fs_group: The fs_group of this V1PodSecurityContext.  # noqa: E501
        :type fs_group: int
        """

        self._fs_group = fs_group

    @property
    def fs_group_change_policy(self):
        """Gets the fs_group_change_policy of this V1PodSecurityContext.  # noqa: E501

        fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are \"OnRootMismatch\" and \"Always\". If not specified, \"Always\" is used. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :return: The fs_group_change_policy of this V1PodSecurityContext.  # noqa: E501
        :rtype: str
        """
        return self._fs_group_change_policy

    @fs_group_change_policy.setter
    def fs_group_change_policy(self, fs_group_change_policy):
        """Sets the fs_group_change_policy of this V1PodSecurityContext.

        fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are \"OnRootMismatch\" and \"Always\". If not specified, \"Always\" is used. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :param fs_group_change_policy: The fs_group_change_policy of this V1PodSecurityContext.  # noqa: E501
        :type fs_group_change_policy: str
        """

        self._fs_group_change_policy = fs_group_change_policy

    @property
    def run_as_group(self):
        """Gets the run_as_group of this V1PodSecurityContext.  # noqa: E501

        The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :return: The run_as_group of this V1PodSecurityContext.  # noqa: E501
        :rtype: int
        """
        return self._run_as_group

    @run_as_group.setter
    def run_as_group(self, run_as_group):
        """Sets the run_as_group of this V1PodSecurityContext.

        The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :param run_as_group: The run_as_group of this V1PodSecurityContext.  # noqa: E501
        :type run_as_group: int
        """

        self._run_as_group = run_as_group

    @property
    def run_as_non_root(self):
        """Gets the run_as_non_root of this V1PodSecurityContext.  # noqa: E501

        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.  # noqa: E501

        :return: The run_as_non_root of this V1PodSecurityContext.  # noqa: E501
        :rtype: bool
        """
        return self._run_as_non_root

    @run_as_non_root.setter
    def run_as_non_root(self, run_as_non_root):
        """Sets the run_as_non_root of this V1PodSecurityContext.

        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.  # noqa: E501

        :param run_as_non_root: The run_as_non_root of this V1PodSecurityContext.  # noqa: E501
        :type run_as_non_root: bool
        """

        self._run_as_non_root = run_as_non_root

    @property
    def run_as_user(self):
        """Gets the run_as_user of this V1PodSecurityContext.  # noqa: E501

        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :return: The run_as_user of this V1PodSecurityContext.  # noqa: E501
        :rtype: int
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """Sets the run_as_user of this V1PodSecurityContext.

        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :param run_as_user: The run_as_user of this V1PodSecurityContext.  # noqa: E501
        :type run_as_user: int
        """

        self._run_as_user = run_as_user

    @property
    def se_linux_options(self):
        """Gets the se_linux_options of this V1PodSecurityContext.  # noqa: E501


        :return: The se_linux_options of this V1PodSecurityContext.  # noqa: E501
        :rtype: V1SELinuxOptions
        """
        return self._se_linux_options

    @se_linux_options.setter
    def se_linux_options(self, se_linux_options):
        """Sets the se_linux_options of this V1PodSecurityContext.


        :param se_linux_options: The se_linux_options of this V1PodSecurityContext.  # noqa: E501
        :type se_linux_options: V1SELinuxOptions
        """

        self._se_linux_options = se_linux_options

    @property
    def seccomp_profile(self):
        """Gets the seccomp_profile of this V1PodSecurityContext.  # noqa: E501


        :return: The seccomp_profile of this V1PodSecurityContext.  # noqa: E501
        :rtype: V1SeccompProfile
        """
        return self._seccomp_profile

    @seccomp_profile.setter
    def seccomp_profile(self, seccomp_profile):
        """Sets the seccomp_profile of this V1PodSecurityContext.


        :param seccomp_profile: The seccomp_profile of this V1PodSecurityContext.  # noqa: E501
        :type seccomp_profile: V1SeccompProfile
        """

        self._seccomp_profile = seccomp_profile

    @property
    def supplemental_groups(self):
        """Gets the supplemental_groups of this V1PodSecurityContext.  # noqa: E501

        A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :return: The supplemental_groups of this V1PodSecurityContext.  # noqa: E501
        :rtype: list[int]
        """
        return self._supplemental_groups

    @supplemental_groups.setter
    def supplemental_groups(self, supplemental_groups):
        """Sets the supplemental_groups of this V1PodSecurityContext.

        A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :param supplemental_groups: The supplemental_groups of this V1PodSecurityContext.  # noqa: E501
        :type supplemental_groups: list[int]
        """

        self._supplemental_groups = supplemental_groups

    @property
    def sysctls(self):
        """Gets the sysctls of this V1PodSecurityContext.  # noqa: E501

        Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :return: The sysctls of this V1PodSecurityContext.  # noqa: E501
        :rtype: list[V1Sysctl]
        """
        return self._sysctls

    @sysctls.setter
    def sysctls(self, sysctls):
        """Sets the sysctls of this V1PodSecurityContext.

        Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.  # noqa: E501

        :param sysctls: The sysctls of this V1PodSecurityContext.  # noqa: E501
        :type sysctls: list[V1Sysctl]
        """

        self._sysctls = sysctls

    @property
    def windows_options(self):
        """Gets the windows_options of this V1PodSecurityContext.  # noqa: E501


        :return: The windows_options of this V1PodSecurityContext.  # noqa: E501
        :rtype: V1WindowsSecurityContextOptions
        """
        return self._windows_options

    @windows_options.setter
    def windows_options(self, windows_options):
        """Sets the windows_options of this V1PodSecurityContext.


        :param windows_options: The windows_options of this V1PodSecurityContext.  # noqa: E501
        :type windows_options: V1WindowsSecurityContextOptions
        """

        self._windows_options = windows_options

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
        if not isinstance(other, V1PodSecurityContext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PodSecurityContext):
            return True

        return self.to_dict() != other.to_dict()
