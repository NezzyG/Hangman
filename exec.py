"""
36. Write a Python program to add two objects if both objects are an integer type. Go to the editor
"""
class Hero:
  def __init__(self, Class, Race, Profession):
    self.Class = Class
    self.Race = Race
    self.Profession = Profession

p1=Hero("Paladin", "Orc", "Nerd")
print(p1.Class)
p2=Hero(input("What is your clas?\n"),input("What race do you belong to?\n"),input("What is your profession?\n"))

print("Character sheet.\n You are a young "+p2.Race+" "+p2.Class+" and you work as a "+p2.Profession)