def alcoholic(beverage):
    beverage = beverage.upper()
    if 'BEB' in beverage:
        return True
    else:
        return False


products = ['beb46275', 'TFA23962', 'TFA64715', 'TFA69555', 'TFA56743', 'BSA45510', 'TFA44968', 'CAR75448', 'CAR23596', 'CAR13490', 'BEB21365', 'BEB3']


for product in products:
    if alcoholic(product):
        print('Enviar {} para setor de bebidas alcóolicas'.format(product))
