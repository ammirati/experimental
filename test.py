# Copyright 2014 QCF

# Add the Google SDK
import sys
sys.path.insert(0, '/usr/local/google_appengine')

import dev_appserver
dev_appserver.fix_sys_path()
#print sys.path
#exit()
from google.appengine.ext import testbed

import datetime
import unittest

from main import Client, Trainer, Workout


# https://docs.python.org/2/library/unittest.html
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

    # Tests

    def test_sanity(self):
        string_list = ['Benchpress', 'Dumbbells']

        self.assertEqual(2, len(string_list))


        def product(x, y):
        # This is a simple multiplication test.
            return x * y

        self.assertEqual(6, product(2, 3))
        self.assertEqual(32, product(2, product(2, 8)))

        def fibonacci(end_point):
        # This will return the requested number of entries from the Fibonacci sequence.
            fib_list = [0, 1]
            if end_point <= 2:
                print fib_list[:end_point]
            else:
                for i in range(2, end_point):
                    fib_list.append(fib_list[i-1] + fib_list[i-2])
            return fib_list

        self.assertEqual([0, 1, 1, 2, 3], fibonacci(5))

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

        some_trainers = [
            Trainer(name='Trainer Tony'),
            Trainer(name='Annie')
        ]

        for trainers in some_trainers:
            trainers.put()
            print trainers

        self.assertEqual(2, len(Trainer.query().fetch()))

        workout = Workout(client=clients[0].key)
        workout.set_value('benchpress', 100, 10)
        workout.set_value('shoulderpress', 70, 10)
        workout.put()

        print workout

    def test_age(self):
        c = Client(name='Test', dob=datetime.date.today())  # creates a "Test" Client object
        self.assertEquals(0, c.age())

    def test_query(self):
        query = Client.query()
        clients = query.fetch()
        for c in clients:
            print c


if __name__ == '__main__':
    import unittest.loader
    suite = unittest.loader.TestLoader().discover('.')

    print 'Starting tests...'
    unittest.TextTestRunner(verbosity=2).run(suite)



