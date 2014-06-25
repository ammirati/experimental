# Copyright 2014 QCF

import datetime
import unittest
# TODO(burdon): Need PyCharm Pro to run with App Engine.
# from google.appengine.ext import testbed

from main import Client, Workout


class DataTest(unittest.TestCase):

    # def setUp(self):
    #     """
    #     Set-up the database testbed.
    #     https://developers.google.com/appengine/docs/python/tools/localunittesting#Python_Writing_Datastore_and_memcache_tests
    #     """
    #     self.testbed = testbed.Testbed()
    #     self.testbed.activate()
    #     self.testbed.init_datastore_v3_stub()
    #     # self.testbed.init_memcache_stub()
    #     # self.testbed.init_search_stub()
    #
    # def tearDown(self):
    #     self.testbed.deactivate()
    #
    # def test_store(self):
    #     pass

    def test_models(self):
        clients = [
            Client('Rich', datetime.date(1969, 6, 11)),
            Client('Jay', datetime.date(1972, 6, 5)),
            Client('Tony', datetime.date(1973, 6, 17))
        ]
        print clients
        print clients[0].age()

        workout = Workout(clients[0])
        workout.set_value('benchpress', 100)
        workout.set_value('shoulderpress', 70)
        print workout
        print workout.values

    def test_age(self):
        c = Client('Test', datetime.date.today())
        self.assertEquals(0, c.age())
