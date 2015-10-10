from django.db import models

class Group(models.Model):
    code = models.CharField(max_length=55)
    name = models.CharField(max_length=100)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, db_column='groupID')
