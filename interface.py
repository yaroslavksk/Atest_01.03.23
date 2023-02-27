import Scrabler

def inData(command):
    try:
        command = int (command)
        match command:
            case 1:
                print("Добро пожаловать в меню записей")
                if (NewNotes() == True): print("Запись успешна!")
                MainMenuMessage()
                inData(input())
            case 2: 
                print("Добро пожаловать в меню редактирования")
            case 3:
                print("Загрузка последней записи...")
                Scrabler.LastScrab()
                MainMenuMessage()
                inData(input())
            case 4:   
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
    print("Добро пожаловать в записную книгу: \n 1 - Сделать запись \n 2 - Редактировать запись \n 3 - Загрузить последнюю запись \n 4 - Выход \n")

def NewNotes():
    if (Scrabler.NewScrab()): return True