# Copyright 2014 QCF

import datetime
from dateutil.relativedelta import relativedelta


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
