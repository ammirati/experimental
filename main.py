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
    # Represents each day's workout.
    class Exercise(ndb.Model):
        # Represents each exercise with load and reps.
        name = ndb.StringProperty()
        weight = ndb.IntegerProperty()
        reps = ndb.IntegerProperty()

    class Goal(ndb.Model):
        # Goals for the workout.
        name = ndb.StringProperty()
        goal_weight = ndb.IntegerProperty()
        goal_reps = ndb.IntegerProperty()

    date = ndb.DateProperty()
    client = ndb.KeyProperty()
    exercises = ndb.StructuredProperty(Exercise, repeated=True)
    lift_goals = ndb.StructuredProperty(Goal, repeated=True)

    def set_value(self, name, weight, reps):
        self.exercises.append(Workout.Exercise(name=name, weight=weight, reps=reps))

    def make_goal(self, name, goal_weight, goal_reps):
        self.lift_goals.append(Workout.Goal(name=name, goal_weight=goal_weight, goal_reps=goal_reps))

