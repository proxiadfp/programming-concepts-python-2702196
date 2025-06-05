""" A Functional Breakfast """

def make_omelette():
  print('Mixing the ingredients')
  print('Pouring the mixture into a frying pan')
  print('Cooking the first side')
  print('Flipping it!')
  print('Cooking the other side\n')
  omelette = 'a tasty omelette'
  return omelette

freddy_breakfast = make_omelette()
aurelie_breakfast = make_omelette()
print(f'Freddy is having {freddy_breakfast}\n')
print(f'Aurelie is having {aurelie_breakfast}\n')