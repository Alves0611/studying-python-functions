def standardize_codes(code_list, standard='m'):
    for i, item in enumerate(code_list):
        item = item.replace('  ', ' ')
        item = item.strip()
        if standard == 'm':
            item = item.casefold()
        elif standard == 'M':
            item = item.upper()
        code_list[i] = item
    return code_list


product_codes = [' ABC12 ', 'abc34', 'AbC37']
print(standardize_codes(product_codes, standard='m'))