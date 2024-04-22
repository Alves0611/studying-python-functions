def category(beverage, code_category):
    beverage = beverage.upper()
    if code_category in beverage:
        return True
    else:
        return False


products = ['beb46275', 'TFA23962', 'TFA64715', 'TFA69555', 'TFA56743', 'BSA45510', 'TFA44968', 'CAR75448', 'CAR23596', 'CAR13490', 'BEB21365', 'BEB3']


for product in products:
    if category(product, 'BEB'):
        print('Enviar {} para setor de bebidas alcóolicas'.format(product))
    elif category(product, 'BSA'): 
        print('Enviar {} para setor de bebidas não alcóolicas'.format(product))

