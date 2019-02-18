import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from SiyApp.models import Team

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
        return List                


def delete_everything(self):
    Reporter.objects.all().delete()

def drop_table(self):
    cursor = connection.cursor()
    table_name = self.model._meta.db_table
    sql = "DROP TABLE %s;" % (table_name, )
    cursor.execute(sql)

if __name__ == '__main__':
    print("Population Script Running")
    getDataFromCsv("C:\\Users\\Siya\\Documents\\ProOnePalCSV","Teams")
    print("Population Complete!!")