# Copyright 2014 QCF

# Add the Google SDK
import sys
sys.path.insert(0, 'tools/google_appengine')
import dev_appserver
dev_appserver.fix_sys_path()
from google.appengine.ext import testbed

import datetime
import unittest

from main import Client, Workout


class DataTest(unittest.TestCase):

    def setUp(self):
        """
        Set-up the database testbed.
        https://developers.google.com/appengine/docs/python/tools/localunittesting#Python_Writing_Datastore_and_memcache_tests
        """
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_store(self):
        clients = [
            Client(name='Rich', dob=datetime.date(1969, 6, 11)),
            Client(name='Jay',  dob=datetime.date(1972, 6, 5)),
            Client(name='Tony', dob=datetime.date(1973, 6, 17))
        ]

        for client in clients:
            client.put()
            print client

        self.assertEqual(3, len(Client.query().fetch()))

        workout = Workout(client=clients[0].key)
        workout.set_value('benchpress', 100, 10)
        workout.set_value('shoulderpress', 70, 10)
        workout.put()

        print workout

    def test_age(self):
        c = Client(name='Test', dob=datetime.date.today())
        self.assertEquals(0, c.age())
