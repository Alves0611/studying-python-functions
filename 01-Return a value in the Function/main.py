def register_product():
    product = input('Enter the name of the product you want to register: ')
    product = product.casefold()
    product = product.strip()
    return product


registered_product = register_product()

print(registered_product)