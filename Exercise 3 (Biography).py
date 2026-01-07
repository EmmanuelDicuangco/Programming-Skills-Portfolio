name = 'Emmanuel Joshua A Dicuangco'
hometown = 'Manila Valenzuela Philippines'
age = 19

my_info = {
  'Name': name,
  'Hometown': hometown,
  'Age': age
}

print(my_info['Name'], my_info['Hometown'], my_info['Age'], sep='\n')

--------------------------------------------------------------------------
# Advance Requirement

name = input('Enter your full name')
hometown = input('Enter your hometown')

while True:
  age_input = input('Enter your age')
  if age_input.isdigit():
    age = int(age_input)
    break
  else:
      print('Please enter a valid numbe.')

my_info = {
  'Name': name,
  'Hometown': hometown,
  'Age': age
}

print(my_info['Name'], my_info['Hometown'], my_info['Age'], sep='\n')
