class Human :
    def __init__(self, name, age):
            self.name = name
            self.age = age 
            
    def walk (self):
             return ( "Human can walk")
    def eat (self):
             return ( "XXX")
             
class Asian(Human):
    def __init__(self, name, age, language, skin_color):
        super().__init__(name, age)
        self.language = language
        self.skin_color = skin_color
        
        
    def eat(self):
        return "sss"
    
    def walk(self):
        return "I am asian I can also walk"
        
        
        
#objects
mustapha = Human("mustafa", 80)
baran = Asian("baran", 20, "Turkish"," White")

#outputs
print(mustapha.walk())
print(baran.walk())
print(baran.language)
print(baran.skin_color)