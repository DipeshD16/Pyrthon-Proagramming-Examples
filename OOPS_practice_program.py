#create a class called microwave
class Microwave:
   
    #intialization
    def __init__(self, brand:str, power_rating:str):
        self.brand = brand
        self.power_rating = power_rating
        self.is_on = False
       
   
    def turn_on(self): #to turn ON the Microwave
        if not self.is_on:
            self.is_on = True
            print(f"The {self.brand} microwave is now ON.")
        else:
            print(f"The {self.brand} microwave is already turned ON.")
           
    def turned_off(self): #to turn OFF
        if self.is_on:
            self.is_on = False
            print(f"The {self.brand} microwave is now turned OFF.")
       
        else:
            print(f"The {self.brand} microwave is already turned OFF.")
   
    def run(self, seconds:int):
        if self.is_on:
            print(f"The {self.brand} will run for {seconds} seconds.")
        else:
            print(f"The microwave is {self.brand} needs to be turned ON first.")
       
       
       
my_microwave = Microwave("Bosch", "C")
my_microwave.turn_on()
my_microwave.turn_on()
my_microwave.turned_off()
my_microwave.run(30)
my_microwave.turn_on()
my_microwave.run(30)

       
my_microwave = Microwave("Philips", "B")
my_microwave.turn_on()
my_microwave.turn_on()
my_microwave.turned_off()
my_microwave.run(30)
my_microwave.turn_on()
my_microwave.run(30)
