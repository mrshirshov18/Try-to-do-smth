counter=0
truecounter=0

fourquestions = {
    1: [print("Какая версия языка сейчас актуальна?"),print (5)],
    2: 'Какая кодировка используется в строках?',
    3: 'Какой оператор сравнения нужно использовать для работы с None и bool?',
    4: 'Сколько значений есть у bool?'}
fouranswers ={
    1: 'Python3',
    2: 'UTF8',
    3: 'is',
    4: '2'}
for i in range(1,5):
    print(fourquestions[i])
    a=input()
    if a.lower()==fouranswers[i].lower():
        print("Ответ",a,"верен")
        counter=counter+1
        truecounter=truecounter+1
    else:
        print("Неверный ответ")
        counter=counter+1
print("Пользователь дал", counter, "ответа(ов)")
print("Из них было", truecounter, "верных")
    
    
    
    
    

