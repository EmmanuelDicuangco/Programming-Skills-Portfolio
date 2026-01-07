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
  print('Invalid Month Number')
