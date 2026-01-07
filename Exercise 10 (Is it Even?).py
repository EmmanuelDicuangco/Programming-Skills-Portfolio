def check_even_odd(number):
  if number % 2 == 0:
    return f'The number {'number'} is odd'
  else:
    return f'The number {'number'} is even'

def main():
  num = int(input('Enter a number.'))
  result = check_even_odd(num)
  print(result)

main()
