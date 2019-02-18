from django.db import models

class Tournament(models.Model):
    name            = models.CharField(max_length=128,unique=True)
    maxStages       = models.IntegerField()
    maxGames        = models.IntegerField()
    maxTeams        = models.IntegerField()
    def __str__(self):
        return self.name    

class Team(models.Model):
    name            = models.CharField(max_length=128,unique=True)
    kasi            = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
    
class Player(models.Model):
    name     = models.CharField(max_length=128,unique=True)
    age      = models.IntegerField()
    
    def __str__(self):
        return self.name

class Fixture(models.Model):
    homeTeam        = models.CharField(max_length=128)
    awayTeam        = models.CharField(max_length=128)
    date            = models.DateField()
    pitch           = models.CharField(max_length=128)
    stage           = models.CharField(max_length=64)
    def __str__(self):
        return self.pitch + self.stage

class Result(models.Model):
    homeGoals       = models.IntegerField()
    awayGaols       = models.IntegerField()
    def __str__(self):
        return self.homeGoals + self.awayGaols