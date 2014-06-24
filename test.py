# Copyright 2014 QCF

import datetime
from dateutil.relativedelta import relativedelta
import unittest


class Client(object):
    """
    This represents each client of the gym.
    """
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __str__(self):
        return 'Client[%s:%s]' % (self.name, self.dob)

    def __repr__(self):
        return self.__str__()

    def age(self):
        return relativedelta(datetime.date.today(), self.dob).years


class Workout(object):

    def __init__(self, client):
        self.date = datetime.date.today()
        self.client = client
        self.values = {}

    def set_value(self, name, value):
        self.values[name] = value


class ClientTest(unittest.TestCase):

    def test_age(self):
        c = Client('Test', datetime.date.today())
        self.assertEquals(0, c.age())


clients = []
clients.append(Client('Rich', datetime.date(1969, 6, 11)))
clients.append(Client('Jay',  datetime.date(1972, 6, 5)))
clients.append(Client('Tony', datetime.date(1973, 6, 17)))

print clients
print clients[0].age()

w = Workout(clients[0])
w.set_value('benchpress', 100)
w.set_value('shoulderpress', 70)
print w
print w.values


