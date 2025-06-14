""" A Rolodex Full of Friends """

# dictionary of name/number pairs
rolodex = {'Aaron': 5556069,
           'Bill': 5559824,
           'Dad': 5552603,
           'David': 5558331,
           'Dillon': 5553538,
           'Jim': 5555547,
           'Mom': 5552603,
           'Olivia': 5556397,
           'Verne': 5555309}

def caller_id(lookup_number):
  for name, number in rolodex.items():
    if number == lookup_number:
      return name