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
from kubernetes_asyncio.client.api.admissionregistration_api import AdmissionregistrationApi  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestAdmissionregistrationApi(unittest.TestCase):
    """AdmissionregistrationApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.admissionregistration_api.AdmissionregistrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
