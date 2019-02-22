import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from SiyApp.models import Team,Player,Tournament,Fixture,Result

def getDataFromCsv(path,entity):
        path = path + "\\dbo." + entity + ".csv"
        fd = open(path)
        List = []
        if (entity == 'Teams'):
                for line in fd:
                        elems = line.split(',')
                        team = Team.objects.get_or_create(name = elems[1],
                        kasi = elems[2])
                        List.append(Team(name = elems[1],
                        kasi = elems[2]))
        if (entity == 'Player'):
                for line in fd:
                        elems = line.split(',')
                        player = Player.objects.get_or_create(name = elems[1],
                        age = elems[2], position = elems[3])
                        List.append(Player(name = elems[1],
                        kasi = elems[2],position = elems[3]))
        if (entity == 'Tournament'):
                for line in fd:
                        elems = line.split(',')
                        tournament = Tournament.objects.get_or_create(name = elems[1]
                        ,maxStages = elems[2],maxGames = elems[3],maxTeams = elems[4])
                        List.append(Tournament(name = elems[1]
                        ,maxStages = elems[2],maxGames = elems[3],maxTeams = elems[4]))
        
        if (entity == 'Fixture'):
                for line in fd:
                        elems = line.split(',')
                        fixture = Fixture.objects.get_or_create(name = elems[1]
                        ,homeTeam = elems[2],awayTeam = elems[3],pitch = elems[4])
                        List.append(Fixture(name = elems[1]
                        ,homeTeam = elems[2],awayTeam = elems[3],pitch = elems[4]))

        if (entity == 'Result'):
                for line in fd:
                        elems = line.split(',')
                        result = Result.objects.get_or_create(name = elems[1]
                        ,homeGoals = elems[2],awayGoals = elems[3])
                        List.append(Fixture(name = elems[1]
                        ,homeTeam = elems[2],awayTeam = elems[3],pitch = elems[4]))  

        return List                


if __name__ == '__main__':
    print("Population Script Running")
    getDataFromCsv("C:\\Users\\Siya\\Documents\\ProOnePalCSV","Teams")
    print("Population Complete!!")