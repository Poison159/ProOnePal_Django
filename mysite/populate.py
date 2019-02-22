import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from SiyApp.models import Team,Player,Tournament,Fixture,Result

def getDataFromCsv(path,entity):
        path = path + "\\dbo." + entity + ".csv"
        fd = open(path)
        i = 0
        List = []
        if (entity == 'Teams'):
                for line in fd:
                        if(i != 0):
                                elems = line.split(',')
                                nameTrimed = elems[1].split('"')[1]
                                kasiTrimed = elems[2].split('"')[1]
                                team = Team.objects.get_or_create(name = nameTrimed,kasi = kasiTrimed)
                                List.append(Team(name = nameTrimed,kasi = kasiTrimed))
                        i = i + 1
        if (entity == 'Players'):
                for line in fd:
                        if(i != 0):
                                elems   = line.split(',')
                                ageInt  = int(elems[2].split('"')[1])
                                player  = Player.objects.get_or_create(name = elems[1],age = ageInt, position = elems[3])
                                List.append(Player(name = elems[1],age = ageInt,position = elems[3]))
                        i = i + 1
        if (entity == 'Tournaments'):
                for line in fd:
                        if(i != 0):
                                elems           = line.split(',')
                                maxGamesInt     = int(elems[1].split('"')[1])
                                maxTeamsInt     = int(elems[2].split('"')[1])
                                maxStagesInt    = int(elems[3].split('"')[1])
                                nameTrimed      = elems[4].split('"')[1]
                                tournament      = Tournament.objects.get_or_create(name = nameTrimed,maxStages = maxStagesInt,maxGames = maxGamesInt,maxTeams = maxTeamsInt)
                                List.append(Tournament(name = nameTrimed,maxStages = maxStagesInt,maxGames = maxGamesInt,maxTeams = maxTeamsInt))
                        i = i + 1
        if (entity == 'Fixtures'):
                for line in fd:
                        if(i != 0):
                                elems = line.split(',')
                                fixture = Fixture.objects.get_or_create(stage = elems[1],homeTeam = elems[2],
                                awayTeam = elems[3],date = elems[4],pitch = elems[5])
                                List.append(Fixture(stage = elems[1],homeTeam = elems[2],
                                awayTeam = elems[3],date = elems[4],pitch = elems[5]))
                        i = i + 1
        if (entity == 'Results'):
                for line in fd:
                        if(i != 0):
                                elems = line.split(',')
                                homeGoalsInt = int(elems[1].split('"')[1])
                                awayGoalsInt = int(elems[2].split('"')[1])
                                result = Result.objects.get_or_create(homeGoals = homeGoalsInt,awayGoals = awayGoalsInt)
                                List.append(Result(homeGoals = homeGoalsInt,awayGoals = awayGoalsInt))
                        i = i + 1

        return List                


if __name__ == '__main__':
    print("Population Script Running")
    enties = {"Teams","Players","Tournaments","Results","Fixtures"}
    for entity in enties:
                getDataFromCsv("C:\\Users\\Siya\\Documents\\ProOnePalCSV","Teams")
    print("Population Complete!!")