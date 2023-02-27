import datetime
import glob
import json

DownloadedNotes = []
NowDateTime = datetime.datetime.now()
NowDateTime = NowDateTime.strftime("%d-%m-%Y %H:%M")
count = 0

def findNotes():
    files = glob.glob('Notes.json')
    for file in files:
        print("Заметки найдены!")
    return True

def DownloadNotes():
    try:
        global count
        print("Заметки загружаются...")
        if (findNotes() == True):
            with open('Notes.json') as file:
                for line in file:
                    a = line  
                    DownloadedNotes.append(a)
                    count = count + 1
                                      
            print(f'Заметки загружены! \n Количество: {count}')
            return True
    except:
        print("Ошибка загрузки проверьте файл!")
        return False

def NewScrab(Title,Body):
    #try:
        if (findNotes == False):
            f = open("Notes.json", "w+")
            RedactedData = {'id': count+1, 'Title': Title,'Body':Body,'DateTime':NowDateTime}
            a ='' + json.dumps(RedactedData,separators=('; ',': '))
            f.write(a +'\n')
            f.close()
            return True
        else:
            f = open("Notes.json", "a")
            RedactedData = {'id': count+1, 'Title': Title,'Body':Body,'DateTime':NowDateTime}
            a ='' + json.dumps(RedactedData,separators=('; ',': '))
            f.write(a + '\n')
            f.close()
            return True
    #except:
        print("Ошибка записи проверьте запись!")

def LastScrab():
    if (DownloadNotes() == True):
        return  print ('\n' + DownloadedNotes[len(DownloadedNotes)-1] + '\n')
    
def RedScrab(id,Title,Body):
    RedactedData = {'id': id, 'Title': Title,'Body':Body,'DateTime':NowDateTime}
    a ='' + json.dumps(RedactedData,separators=('; ',': '))
    print(a)