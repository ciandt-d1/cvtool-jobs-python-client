# coding: utf-8

"""
    Kingpick Image ingestion jobs API

    Image ingestion jobs.

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cvtool_jobs_client
from cvtool_jobs_client.rest import ApiException
from cvtool_jobs_client.models.job_step import JobStep


class TestJobStep(unittest.TestCase):
    """ JobStep unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobStep(self):
        """
        Test JobStep
        """
        model = cvtool_jobs_client.models.job_step.JobStep()


if __name__ == '__main__':
    unittest.main()
