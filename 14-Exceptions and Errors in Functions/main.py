def find_server(email):
    try:
        at_position = email.index('@')
        server = email[at_position:]
        if 'gmail' in server:
            return 'gmail'
        elif 'hotmail' in server or 'outlook' in server or 'live' in server:
            return 'hotmail'
        elif 'yahoo' in server:
            return 'yahoo'
        elif 'uol' in server or 'bol' in server:
            return 'uol'
        else:
            return 'not determined'
    except:
        print('The entered email does not contain @, please enter again')


email = input('What is your email?')
print(find_server(email))