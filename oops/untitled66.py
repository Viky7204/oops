class Bike:
    def __init__(self, name, cc):
        self.bike_name = name
        self.bike_cc = cc

    def bike_type(self):
        if self.bike_cc < 200:
            print(f"{self.bike_name} is a normal bike")
        else:
            print(f"{self.bike_name} is a superbike")

Duke = Bike("RC390", 390)
RE = Bike("classic350", 350)
Hero = Bike("Splender", 110)

b = input("Enter the bike: ")

if b == "Duke":
    Duke.bike_type()
elif b == "RE":
    RE.bike_type()
else:
   Hero.bike_type()