def format_price(price):
    num = int(price)
    return f'Цена: {num} rub.'

result = format_price(56.24)
print(result)