class laptop:
  def __init__(self, brand, release_year, color,RAM):
    self.laptop_brand = brand
    self.laptop_release_year = release_year
    self.laptop_color = color
    self.laptop_RAM = RAM

  def information(self):
    return f"""
    Brand: {self.laptop_brand}, 
    Release Year: {self.laptop_release_year}, 
    Color: {self.laptop_color}, 
    RAM: {self.laptop_RAM} GB"""

laptop_1 = laptop("Dell", 2021, "Grey", 8)
print(laptop_1.laptop_brand)
print(laptop_1.laptop_release_year)
print(laptop_1.laptop_color)
print(laptop_1.laptop_RAM)
print(laptop_1.information())


class Gaminglaptop(laptop):
  def __init__(self, brand, release_year, color, RAM, VGA):
    super().__init__(brand, release_year, color, RAM)
    self.laptop_VGA = VGA

laptop_2 = Gaminglaptop("Asus", 2022, "Black", 16, "RTX1650")
print(laptop_2.laptop_brand)
print(laptop_2.laptop_release_year)
print(laptop_2.laptop_color)
print(laptop_2.laptop_RAM)
print(laptop_2.laptop_VGA)





