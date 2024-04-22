def tax_burden(price, cost, profit):
    tax = price - cost - profit
    return tax / price


price = 1500
cost = 400
profit = 800


print('A carga tributária foi de {:.1%}'.format(tax_burden(price, cost, profit)))
