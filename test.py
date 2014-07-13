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

        def derivative_calc(integer, variable, exponent):
            # Returns the derivative of single-variable algebraic functions.
            leading_coefficient = int(integer) * int(exponent)
            new_exp = int(exponent) - 1
            return str(leading_coefficient) + variable + "^" + str(new_exp)

        self.assertEqual('6x^2', derivative_calc(2, 'x', 3))

        def facts(some_int):
        # A recursive function for finding factorial of any integer.
            if some_int <= 1:
                the_factorial = some_int
            else:
                the_factorial = some_int * facts(some_int - 1)
            return the_factorial

        self.assertEqual(24, facts(4))

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

        def isPalindrome(s):
            """
            Assumes s is a string. Returns True if letters in s form a palindrome;
            Otherwise returns False. Non-letters and caps are ignored.
            """

            def toChars(s):
                s = s.lower()
                letters = ''
                for c in s:
                    if c in 'abcdefghijklmnopqrstuvwxyz':
                        letters = letters + c
                return letters

            def isPal(s):
                if len(s) <= 1:
                    return True
                else:
                    return s[0] == s[-1] and isPal(s[1:-1])

            return isPal(toChars(s))

        self.assertEqual(False, isPalindrome('tony is great'))
        self.assertEqual(True, isPalindrome('Never odd or even'))

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

        workout = Workout(client=clients[0].key, date=datetime.date.today())
        workout.set_value('bench press', 100, 10)
        workout.set_value('shoulder press', 70, 10)
        workout.make_goal('bench press', 120, 8)
        workout.make_goal('shoulder press', 75, 12)
        workout.put()

        print workout

    def test_age(self):
        c = Client(name='Test', dob=datetime.date.today())
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



