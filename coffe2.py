from abc import ABC, abstractmethod
class coffe2:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def get_name(self):
        return self.name

    def get_ingredients(self):
        return self.ingredients
    
    @abstractmethod
    def get_info(self):
        pass

class espresso(coffe2):
    def get_info(self):
        return f"Espresso with ingredients: {self.ingredients}"
class latte(coffe2):
    def get_info(self):
        return f"Latte with ingredients: {self.ingredients}"
    
coffe1 = espresso("Espresso", ["coffee beans", "water"])
coffe2 = latte("Latte", ["coffee beans", "milk", "water"])
print(coffe1.get_info())
        
    