# Copyright 2014 QCF

import datetime
from dateutil.relativedelta import relativedelta
from google.appengine.ext import ndb


class Client(ndb.Model):
    """
    This represents each client of the gym.
    """

    name = ndb.StringProperty()  # Keyword arguments mapping to the model's properties.
    dob = ndb.DateProperty()    # Use these arguments when instantiating Client.

    def __str__(self):
    # Defines what print will do, here it returns name and dob.
        return 'Client[%s:%s]' % (self.name, self.dob)

    def __repr__(self):
        return self.__str__()

    def age(self):
    # This will return the clients age based on their dob.
        return relativedelta(datetime.date.today(), self.dob).years


class Trainer(ndb.Model):
    """
    This represents each trainer at the gym.
    """

    name = ndb.StringProperty()

    def __str__(self):
    # Defines what print will do, here it returns name.
        return 'Trainer[%s]' % self.name

    def __repr__(self):
        return self.__str__()


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
