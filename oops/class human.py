class Human:
  def __init__(self,hobby,food):
    self.fav_hobby=hobby
    self.fav_food=food
  def display_info(self):
    print(f"SHe plays {self.fav_hobby}, and she likes {self.fav_food}")
class Spoorthi(Human):
  def __init__(self,hobby,food,language):
    super().__init__(hobby,food)
    self.fav_language=language
  def display_info(self):
    super().display_info()
    print(f"Language she speaks {self.fav_language}")
user=Spoorthi("Games","Briyani","kannada")
user.display_info()

