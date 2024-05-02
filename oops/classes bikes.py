class Bike:
  def __init__(self,name,cc):
    self.bike_name=name
    self.bike_cc=cc

  def Sound(self):
    print(f"{self.bike_name} is loud")

Duke=Bike("RC390",390)
RE=Bike("classic350",350)

print(Duke.bike_name)
print(RE.bike_name)
Duke.Sound()