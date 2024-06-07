# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.30.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.certificates_v1alpha1_api import CertificatesV1alpha1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestCertificatesV1alpha1Api(unittest.TestCase):
    """CertificatesV1alpha1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.certificates_v1alpha1_api.CertificatesV1alpha1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cluster_trust_bundle(self):
        """Test case for create_cluster_trust_bundle

        """
        pass

    def test_delete_cluster_trust_bundle(self):
        """Test case for delete_cluster_trust_bundle

        """
        pass

    def test_delete_collection_cluster_trust_bundle(self):
        """Test case for delete_collection_cluster_trust_bundle

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_cluster_trust_bundle(self):
        """Test case for list_cluster_trust_bundle

        """
        pass

    def test_patch_cluster_trust_bundle(self):
        """Test case for patch_cluster_trust_bundle

        """
        pass

    def test_read_cluster_trust_bundle(self):
        """Test case for read_cluster_trust_bundle

        """
        pass

    def test_replace_cluster_trust_bundle(self):
        """Test case for replace_cluster_trust_bundle

        """
        pass


if __name__ == '__main__':
    unittest.main()
