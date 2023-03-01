from asyncio.windows_events import NULL
import Scrabler

def inData(command):
    try:
        command = int (command)
        match command:
            case 1:
                print("Вы создаёте новую запись")

                print("Введите заголовок")
                title = str(input())
                print("Введите заметку")
                body = str(input())

                if (NewNotes(title,body) == True): print("Запись успешна!")
                
                MainMenuMessage()
                inData(input())

            case 2: 
                a = int(input())
                RedNote(a)

            case 3:
                print("Загрузка последней записи...")
                Scrabler.LastScrab()
                MainMenuMessage()
                inData(input())

            case 4:
                if (Scrabler.AllScrab()==True):
                    print('\n')
                    MainMenuMessage()
                    inData(input())
                else: print('Не удалось вывести')
            
            case 5:
                return 
            
            case _:
                print ("Команда не опознана введите команду")
                MainMenuMessage()
                inData(int(input()))
    except: 
        print ("\n Ошибка! Введите команду")
        MainMenuMessage()
        inData(input())

def MainMenuMessage():
    print("Добро пожаловать в записную книгу: \n 1 - Сделать запись \n 2 - Редактировать запись \n 3 - Загрузить последнюю запись\n 4 - Вывести все записи \n 5 - Выход \n")

def NewNotes(title,body):
    if (Scrabler.NewScrab(title,body)): return True

def RedNote():

    print ("Вы в меню редактирования: \n 1 - Изменить запись \n 2 - Удалить запись\n 3 - Назад \n")
    #try:
    comm = int(input())
    match comm:
        case 1:

            print("Введите новый заголовок")
            id = str(input())
            print("Введите новый заголовок")
            title = str(input())
            print("Введите новую заметку")
            body = str(input())

            if (Scrabler.RedScrab(id,title,body) == True): print("Запись успешна!")
        case 2:
            print('Введите ID записи')
            id = int(input())
            Scrabler.DeleteScrab(id)
            RedNote()
        case 3:
            #MainMenuMessage()
            #inData(input())
            return
        case _:
            print("Команда не опознана введите команду")
            RedNote()
    #except: 
        #print ("\n Ошибка! Введите команду")
        #MainMenuMessage()
        #inData(input())
