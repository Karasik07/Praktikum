masSymbols = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И',
              'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 
              'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 
              'Ь', 'Э', 'Ю', 'Я', '1', '2', '3', '4', '5', 
              '6', '7', '8', '9', '0']
masMorze = ["*-", "-***", "*--", "--*", 
            "-**", "*", "***-", "--**",
            "**", "*---", "-*-", "*-**",
            "--", "-*", "---", "*--*", 
            "*-*", "***", "-", "**-", 
            "**-*", "****", "-*-*",
            "---*", "----", "--*-",
            "-*--", "-**-", "**-**",
            "**--", "*-*-", "*----",
            "**---", "***--", "****-",
            "*****", "-****", "--***",
            "---**", "----*", "-----"]

text = input("Введите сообщение на русском языке: ")
text = text.upper()
outputTextKoder = str()
#Кодирование сообщения
for val in text:
    if val != ' ':
        outputTextKoder = outputTextKoder+masMorze[masSymbols.index(val,0)] + " "
print(outputTextKoder)

outputTextDekoder = str()

#Декодирование сообщения
textKoder = outputTextKoder.split(" ")
outputTextDekoder = str()
for val in textKoder:
    if val != " " and val != '':
        outputTextDekoder = outputTextDekoder + masSymbols[masMorze.index(val,0)] + " "
    else:
        outputTextDekoder = outputTextDekoder + " "
print(outputTextDekoder)