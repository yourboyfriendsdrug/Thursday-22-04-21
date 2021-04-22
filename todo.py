#импорт библиотек



TOKEN = ""
#в трех кавычках текст показывается так, как есть. со всеми пробелами, переносами и тп
HELP = """ 
help - вывод списка команд
add - добавление задачи 
show - показ всех задач 
done - задача выполнена
"""
todo = {}

print ( "Привет! Введи команду help для вывода списка команд." )

while True:
  userAnswer = input("Введите команду\n") #\n - ввод каждой команды с новой строки
  if userAnswer == "add":
    print ( "Работает" ) 
  elif userAnswer == "help":
    print ( "Работает" ) 
  elif userAnswer == "show":
    print ( "Работает" ) 
  elif userAnswer == "done":
    print ( "Работает" ) 
  elif userAnswer == "exit":
    print ( "Работает" )
  else:
    print ( "Error, нет такой команды!" )
    print ( "Введите help для вывода списка команд" )


