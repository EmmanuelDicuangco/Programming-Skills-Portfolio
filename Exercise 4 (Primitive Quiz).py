answer = input('What is the capital of France?')

if answer == 'Paris':
    print('Your answer is correct, which is Paris')
else:
    print('Your answer is wrong. Correct answer is Paris')


-------------------------------------------------------------------

# Advanced Requirements

capitals = {
    'France': 'Paris',
    'Belgium': 'Brussels',
    'Russia': 'Moscow',
    'Spain': 'Madrid',
    'United Kingdom': 'London',
    'Turkey': 'Ankara',
    'Norway': 'Oslo',
    'Netherlands': 'Amsterdam',
    'Romania': 'Bucharest',
    'Ukraine': 'Klev'
}

for country, capital in capitals.items():
    answer = input(f'What is the capital of this {country}?')

    if answer.lower() == capital.lower():
        print('Correct')
    else:
        (f'Wrong. The correct answer is {capital}.')
