salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0  # Подушка безопасности
current_spend = spend  # Траты текущего месяца

for _ in range(months):
# если зарплаты не хватает — берем из подушки
    if salary < current_spend:
        money_capital += current_spend - salary

    # увеличиваем траты со следующего месяца
    current_spend *= (1 + increase)

    # увеличиваем траты со следующего месяца
    money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
