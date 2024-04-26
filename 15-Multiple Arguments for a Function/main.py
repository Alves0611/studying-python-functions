def my_sum(*numbers):
    print(numbers)
    total = 0
    for number in numbers:
        total += number
    return total

print(my_sum(15, 17, 13, 16))



def final_price(price, **extras):
    print(extras)
    if 'discount' in extras:
        price *= (1 - extras['discount'])
    if 'extended_warranty' in extras:
        price += extras['extended_warranty']
    if 'tax' in extras:
        price *= (1 + extras['tax'])
    return price

print(final_price(1000, discount=0.1, extended_warranty=100, tax=0.3))