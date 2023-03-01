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
        print("Ошибка загрузки")
        return False

def NewScrab(Title,Body):
    try:
        
        if (findNotes == False):
            DownloadNotes()
            f = open("Notes.json", "w+")
            RedactedData = {'id': count+1, 'Title': Title,'Body':Body,'DateTime':NowDateTime}
            a ='' + json.dumps(RedactedData,separators=('; ',': '))
            f.write(a +'\n')
            f.close()
            return True
        else:
            DownloadNotes()
            f = open("Notes.json", "a")
            RedactedData = {'id': count+1, 'Title': Title,'Body':Body,'DateTime':NowDateTime}
            a ='' + json.dumps(RedactedData,separators=('; ',': '))
            f.write(a + '\n')
            f.close()
            return True
    except:
        print("Ошибка записи проверьте запись!")

def LastScrab():
    if (DownloadNotes() == True):
        return  print ('\n' + DownloadedNotes[len(DownloadedNotes)-1] + '\n')
    
def RedScrab(id,Title,Body):
    with open('Notes.json','r',encoding='utf-8') as file:
        data = file.readlines()
        if ( (id > len(data)+1) or (id <= 0) ): return
        else:
            RedactedData = {'id': id+1, 'Title': Title,'Body':Body,'DateTime':NowDateTime}
            data[id-1] = '' + json.dumps(RedactedData,separators=('; ',': '))+'\n'

    with open('Notes.json', 'w', encoding='utf-8') as file:
        file.writelines(data)
    return True

def DeleteScrab(id):

    with open('Notes.json','r',encoding='utf-8') as file:
        data = file.readlines()
        if ( (id > len(data)+1) or (id <= 0) ): return
        else:
            data[id-1] = "{NULL}\n"

    with open('Notes.json', 'w', encoding='utf-8') as file:
        file.writelines(data)
    return True

def AllScrab():
    if (findNotes() == True):
        with open("Notes.json", 'r', encoding='UTF-8') as file:
            while (line := file.readline().rstrip()):
                print(line)
        file.close()
    return True