from online import get_currencies

# print(get_currencies()['data'])
currencies = get_currencies()['data']

# currencies = {
#     'EUR': 0.95,
#     'RUB': 97.45,
#     'USD': 1
# }

def convert(amount_baks, to_currency, from_currency):
    coefficient = to_currency / from_currency
    return round(amount_baks * coefficient, 2)

def inpup_currency_ticker(input_message, arr_currencies):
    currency_input = input(f"{input_message}").strip().upper()
    currency = arr_currencies.get(currency_input, None)
    if currency is None:
        print(f"Валюты {currency_input} у нас нет.")
        exit()
    return [currency_input, currency]

print('Привет, это программа Конвектор Валют!')
print("""
Для работы с программой требуется:
- выбрать исходную валюту
- выбрать в какую валюту следуют перевести
- ввести количество исходной валюты
""")
repetition = 'Y'

while repetition == 'Y':
    arr_currency = ''
    for currency in currencies:
        arr_currency += f'{currency} '

    print(f"Доступные валюты: {arr_currency}")

    from_ticker, from_currency = inpup_currency_ticker("Введите исходную валюту: ", currencies)

    to_ticker, to_currency = inpup_currency_ticker("Введите в какую валюту надо перевести: ", currencies)

    # from_currency_input = input("Введите исходную валюту: ").strip()
    # from_currency = currencies.get(from_currency_input, None)
    # if from_currency is None:
    #     print(f"Валюты {from_currency_input} у нас нет.")
    #     exit()

    # to_currency_input = input("Введите в какую валюту надо перевести: ").strip()
    # to_currency = currencies.get(to_currency_input, None)
    # if to_currency is None:
    #     print(f"Валюты {to_currency_input} у нас нет.")
    #     exit()

    amount_currency = input("Введите кол-во исходной валюты для обмена: ")
    amount_baks = float(amount_currency) # перевод кол-ва валюты в числовой тип

    # Пересчёт курса
    rezult = convert(amount_baks, to_currency, from_currency)
    print(f'Результат: {amount_baks} {from_ticker} = {rezult} {to_ticker}\n')
    check = True
    while check == True:
        repetition = input("Провести ещё одну конвертацию (Y/N)? ").upper()
        if repetition == 'N':
            repetition = 'N'
            check = False
        elif repetition == 'Y':
            repetition = 'Y'
            check = False
            print('')
        else:
            print("Надо нажать Y или N")
            check = True
print('До новых встречь!')
exit()