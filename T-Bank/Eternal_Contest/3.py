"""
У Кати насыщенный день на работе. Ей надо передать n разных договоров коллегам.
Все встречи происходят на разных этажах, а между этажами можно перемещаться
только по лестничным пролетам — считается, что это улучшает физическую форму 
сотрудников. Прохождение каждого пролета занимает ровно 1 минуту.

Сейчас Катя на парковочном этаже, планирует свой маршрут. Коллег можно 
посетить в любом порядке, но один из них покинет офис через t минут.
С парковочного этажа лестницы нет — только лифт, на котором можно подняться 
на любой этаж.

В итоге план Кати следующий:
1. Подняться на лифте на произвольный этаж. Считается, что лифт поднимается на 
любой этаж за 0 минут.
2. Передать всем коллегам договоры, перемещаясь между этажами по лестнице. 
Считается, что договоры на этаже передаются мгновенно.
3. В первые tминут передать договор тому коллеге, который планирует уйти.
4. Пройти минимальное количество лестничных пролетов.

Помогите Кате выполнить все пункты ее плана.

Входные данные: n и t.
Выходные данные: минимальное число пролетов.
"""


def main():
    n, t = [int(i) for i in input().split()]
    floors = []
    for i in range(n):
        floors.append(int(input()))
    leaving = int(input())

    
    


if __name__ == "__main__":
    main()