#  #!/usr/bin/env python
#  encoding: utf-8

my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
# Covert the height to centimeters.
my_height_in_cm = my_height * 2.54
my_weight = 180  # lbs
# Convert the weight to kilos.
my_weight_in_kg = my_weight / 2.205
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brow'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height:d} inches tall.")
print(f"He's {my_height_in_cm:.2f} centimeters tall.")
print(f"He's {my_weight:d} pounds heavy.")
print(f"He's {my_weight_in_kg:.2f} pounds heavy.")
print("Actually that's not to heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffer.")

# this line is tricky, try to get it exactly right
print(f"If I add {my_age:d}, {my_height:d}, and {my_weight:d} I get {my_age + my_height + my_weight:d}.")
