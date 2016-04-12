#This is the code for the core part of planet_gen

user_mass = float(raw_input("Please enter a planetary mass in units of Earth = 1: "))
user_radius = float(raw_input("Please enter a planetary radius, again in Earth = 1: "))

# import relevant modules

import UnitConv
import GravityModule
import EscapeVelModule

# Need to make sure the units are on the SI system....

converted_units = UnitConv.UnitConv(user_mass, user_radius)

#As this emits multiple things, it emits the results as a multi-value array
#PlanetGen needs the 1st and 2nd entries respectively.

planet_mass = converted_units[0]
planet_radius = converted_units[1]

# These values can be fed into the modules for surface gravity and escape velocity

Local_gravity = GravityModule.SurfaceGravity(planet_mass, planet_radius)
Escape_speed = EscapeVelModule.EscapeVel(planet_mass, planet_radius)

#Print statements to return the outputs, rounded to 3 decimal places

print 'The surface gravity is: ', round(Local_gravity, 3), 'N\kg.'
print 'The escape velocity is: ', round(Escape_speed, 3), 'm\s.'

#Now I want to write out what I've set up to some kind of permanent file.

text_output = open("PlanetStats.txt", "w")

text_output.write("M E=1    R E=1    G N\kg    V_esc m\s \n")
text_output.write(str(user_mass))
text_output.write("   ")
text_output.write(str(user_radius))
text_output.write("   ")
text_output.write(str(round(Local_gravity, 3)))
text_output.write("   ")
text_output.write(str(round(Escape_speed, 3)))
text_output.write("\n")

text_output.close()
