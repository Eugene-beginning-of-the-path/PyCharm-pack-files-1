#Подключение БД и выборка из таблци этой БД

import  pymysql

#Подсоединяемся к базе данных, которая лежит на сервере
connect = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'shop')
#
cursor = connect.cursor()
#Помещаем команду запроса в переменную
query = ("SELECT name FROM shop WHERE bio='Менеджер'")

gmail = 'Unknown@gmail.com'
sql = "UPDATE shop SET email='%s' WHERE id=1" % gmail


#Осуществляем сортировку данных
cursor.execute(query)
connect.commit()
#Помещаем отсортированные данные в переменную(кортеж)
resault = cursor.fetchall()


print(resault)

connect.close()