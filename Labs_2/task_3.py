from itertools import count

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_mounth = 0;
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital + salary > spend:
    count_mounth += 1
    money_capital += salary
    money_capital -= spend
    spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", count_mounth)
