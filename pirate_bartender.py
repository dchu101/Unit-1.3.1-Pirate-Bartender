questions = {
  "strong":"Do ye want a strong boozy drink? ", 
  "salty":"Do ye prefer a bit of the salt of the sea? ", 
  "bitter":"Do ye prefer a nice bitter flavor? ", 
  "sweet":"Do ye prefer yer drinks sweet as a lass' booty? ", 
  "fruity":"Do ye prefer a fruity drink with a little umbrella? "
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

preferences ={}

def bartender():
  input = raw_input(questions["strong"])
  if input=="Yes" or input=="yes" or input =="Y" or input=="y":
    preferences["strong"] = True
  else:
    preferences["strong"] = False

  input = raw_input(questions["salty"])
  if input=="Yes" or input=="yes" or input =="Y" or input=="y":
    preferences["salty"] = True
  else:
    preferences["salty"] = False

  input = raw_input(questions["bitter"])
  if input=="Yes" or input=="yes" or input =="Y" or input=="y":
    preferences["bitter"] = True
  else:
    preferences["bitter"] = False

  input = raw_input(questions["sweet"])
  if input=="Yes" or input=="yes" or input =="Y" or input=="y":
    preferences["sweet"] = True
  else:
    preferences["sweet"] = False
    
  input = raw_input(questions["fruity"])
  if input=="Yes" or input=="yes" or input =="Y" or input=="y":
    preferences["fruity"] = True
  else:
    preferences["fruity"] = False
    
"""def make_drink(**preferences)
  import random
  
  drink=[]
  
  if strong == True:
    drink.append(random.choice(ingredients("strong")))"""