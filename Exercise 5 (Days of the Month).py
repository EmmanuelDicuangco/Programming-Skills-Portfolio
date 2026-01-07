months = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31
}

month = int(input('Enter a Month Number (1-12). '))
if month in months:
  print(f'This month has {months[month]} days.')
else:
  print('Invalid Month Number.')

--------------------------------------------------------

# Advanced Requirements

months = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31
}

month = int(input('Enter a Month Number (1-12). '))
if month in months:
  if month == 2:
    leap_year = input ('Is it a leap[ year? (yes/no)').lower()
    if leap_year == 'yes':
        print('February has 29 days if it is a leap year.')
    else:
        print('February has 28 days if it is an ordinary year.')
  else:   
      print(f'This month has {months[month]} days.')
else:
  print('Invalid Month Number')
