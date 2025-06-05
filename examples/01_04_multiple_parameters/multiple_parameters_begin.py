""" A Functional Breakfast """

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')

def make_omelette(ingredient):
    mix_and_cook()
    omelette = f'a {ingredient} omelette'
    return omelette

def make_fancy_omelette (*ingredients):
    mix_and_cook()
    omelette = f'a fancy omelette with {len(ingredients)} ingredients'
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = 'a delicious pancake'
    return pancake

# make breakfast for two
barron_breakfast = make_omelette('bacon')
olivia_breakfast = make_fancy_omelette('spam', 'onion','cheese')
print(f'Barron is having {barron_breakfast}\n')
print(f'Olivia is having {olivia_breakfast}\n')
