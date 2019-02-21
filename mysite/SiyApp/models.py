from django.db import models

class Tournament(models.Model):
    name            = models.CharField(max_length=128,unique=True)
    maxStages       = models.IntegerField()
    maxGames        = models.IntegerField()
    maxTeams        = models.IntegerField()
    def __str__(self):
        return self.name    

class Team(models.Model):
    tournament      = models.ForeignKey(Tournament, on_delete=models.CASCADE,null=True,default=2040)
    name            = models.CharField(max_length=128,unique=True)
    kasi            = models.CharField(max_length=64)
    imgPath         = models.CharField(max_length=128,default="./Content/imgs/fcb.jpg")
    def __str__(self):
        return self.name
    
class Player(models.Model):
    Team     = models.ForeignKey(Team, on_delete=models.CASCADE,null=True,default=2040)
    name     = models.CharField(max_length=128,unique=True)
    imgPath  = models.CharField(max_length=128,default="./Content/imgs/fcb.jpg")
    age      = models.IntegerField()
    def __str__(self):
        return self.name

class Fixture(models.Model):
    tournament      = models.ForeignKey(Tournament, on_delete=models.CASCADE,null=True,default=2040)
    homeTeam        = models.CharField(max_length=128)
    awayTeam        = models.CharField(max_length=128)
    date            = models.DateField()
    pitch           = models.CharField(max_length=128)
    stage           = models.CharField(max_length=64)
    def __str__(self):
        return self.pitch + self.stage

class Result(models.Model):
    fixture         = models.ForeignKey(Fixture, on_delete=models.CASCADE,null=True,default="1255")
    homeGoals       = models.IntegerField()
    awayGaols       = models.IntegerField()
    def __str__(self):
        return self.homeGoals + self.awayGaols