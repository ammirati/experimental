# Copyright 2014 QCF

import datetime
from dateutil.relativedelta import relativedelta
from google.appengine.ext import ndb


class Client(ndb.Model):
    """
    This represents each client of the gym.
    """

    name = ndb.StringProperty()
    dob = ndb.DateProperty()

    def __str__(self):
        return 'Client[%s:%s]' % (self.name, self.dob)

    def __repr__(self):
        return self.__str__()

    def age(self):
        return relativedelta(datetime.date.today(), self.dob).years


class Workout(ndb.Model):

    class Exercise(ndb.Model):
        name = ndb.StringProperty()
        weight = ndb.IntegerProperty()
        reps = ndb.IntegerProperty()

    date = ndb.DateProperty()
    client = ndb.KeyProperty()
    exercises = ndb.StructuredProperty(Exercise, repeated=True)

    def set_value(self, name, weight, reps):
        self.exercises.append(Workout.Exercise(name=name, weight=weight, reps=reps))
