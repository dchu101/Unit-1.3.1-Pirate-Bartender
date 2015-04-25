import random

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
    for choice, question in questions.iteritems():
        user_input = raw_input(question.lower())
        #iteritem() turns a dictionary into tuple pairs
        preferences[choice] = user_input[:1] == "y"
        
def make_drink():
    drink=[]
  
    for taste, answer in preferences.iteritems():
        if answer:
            drink.append(random.choice(ingredients[taste]))
    print(drink)

    
if __name__ == '__main__':
    bartender()
    make_drink()



