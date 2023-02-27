import datetime
import glob
import json

DownloadedNotes = []
NowDateTime = datetime.datetime.now()
NowDateTime = NowDateTime.strftime("%d-%m-%Y %H:%M")

def findNotes():
    files = glob.glob('Notes.json')
    for file in files:
        print("Заметки найдены!")
    return True

def DownloadNotes():
    try:
        count = 0
        print("Заметки загружаются...")
        if (findNotes() == True):
            with open('Notes.json') as file:
                for line in file:
                    string = str(line.rstrip())
                    DownloadedNotes.append(string)
                    count = count + 1
            print(f'Заметки загружены! \n Количество: {count}')
            return True
    except:
        print("Ошибка загрузки проверьте файл!")
        return False

def NewScrab():
    try:
        if (findNotes == False):
            f = open("Notes.json", "w+")
            a ='' + json.dumps({'id': id,'Title':'Text','Body':'Text','Date':NowDateTime},separators=('; ',': '))
            f.write(a +'\n')
            f.close()
            return True
        else:
            f = open("Notes.json", "a")
            a ='' + json.dumps({'id': 0,'Title':'Text','Body':'Text','Date':NowDateTime},separators=('; ',': '))
            f.write(a + '\n')
            f.close()
            return True
    except:
        print("Ошибка записи проверьте запись!")

def LastScrab():
    if (DownloadNotes() == True):
        return  print ('\n' + DownloadedNotes[len(DownloadedNotes)-1] + '\n')
