correct_password = 12345

while True:
    password = int(input('Enter your password'))
    
    if password == correct_password:
        print('Welcome!')
        break
    else:
        print('Wrong Password, Please Try Again')
