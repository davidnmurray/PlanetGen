def UnitConv(user_mass, user_radius):

    #A module to convert units onto the SI system

    SI_planet_mass = user_mass * 5.97219 * (10. ** 24.) # Mass of the Earth in Kg

    SI_planet_radius = user_radius * 6371000. # Radius of the Earth in metres

    return SI_planet_mass, SI_planet_radius
